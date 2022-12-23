# Issue 938: graph_database.py has some mysterious problems.

Issue created by migration from https://trac.sagemath.org/ticket/938

Original creator: was

Original creation time: 2007-10-20 06:44:05

Assignee: was

The graph_database.py file has lots of problems now that I've removed the sage.:'s.  This needs to be fixed, and I don't know enough about the code to fix it. 


---

Comment by rlm created at 2007-10-22 02:25:24

On a fresh copy of 2.8.8.1, I removed the nodoctest at the top, searched for sage.:'s, found none, and tried testing:

```
sha:~/sage-2.8.8.1 robert$ ./sage -t devel/sage/sage/graphs/graph_database.py 
sage -t  devel/sage-db/sage/graphs/graph_database.py        
         [62.1 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 62.1 seconds
```


That's pretty mysterious!


---

Comment by rlm created at 2007-10-22 02:27:01

PS - this was on a macbook pro...


---

Comment by mhansen created at 2007-10-24 00:45:05

I think William fixed all of these.


---

Comment by rlm created at 2007-10-24 01:09:11

No, actually this isn't fixed. The doctests pass, but that's because the expected output is <html>..., in other words, anything that starts with <html> will pass. There was a change that William made, leaving the comment
            # TODO: this line is a HACK to get around something
            # being broken with the database/query system.  
which is unfortunate, because now not a single value is returned by the query (they are all "?"). Is a completely broken doctest that passes better? I'd like to know why those changes were made, and what they were supposed to get around...

If we change things back to before this change, then we can get the failures William was talking about, which seems a lot closer to the problem...

I'm moving this back to 2.9.


---

Comment by rlm created at 2007-10-24 01:35:59

Ok, here's the problem. On the old way of thinking, before the big "database class" thingy, the argument query was just a plain string sqlite3 query. Now it's a highfalutin' python class object: line 1302 forward:

```
if ( query is None):
    param = None
    query = __query_string__(graph6=graph6, num_vertices=num_vertices, num_edges=num_edges, num_cycles=num_cycles, num_hamiltonian_cycles=num_hamiltonian_cycles, eulerian=eulerian, planar=planar, perfect=perfect, lovasz_number=lovasz_number, complement_graph6=complement_graph6, aut_grp_size=aut_grp_size, num_orbits=num_orbits, num_fixed_points=num_fixed_points, vertex_transitive=vertex_transitive, edge_transitive=edge_transitive, degree_sequence=degree_sequence, min_degree=min_degree, max_degree=max_degree, average_degree=average_degree, degrees_sd=degrees_sd, regular=regular, vertex_connectivity=vertex_connectivity, edge_connectivity=edge_connectivity, num_components=num_components, girth=girth, radius=radius, diameter=diameter, clique_number=clique_number, independence_number=independence_number, num_cut_vertices=num_cut_vertices, min_vertex_cover_size=min_vertex_cover_size, num_spanning_trees=num_spanning_trees, induced_subgraphs=induced_subgraphs, spectrum=spectrum, min_eigenvalue=min_eigenvalue, max_eigenvalue=max_eigenvalue, eigenvalues_sd=eigenvalues_sd, energy=energy)
    query = re.sub('INNER JOIN .* WHERE','INNER JOIN aut_grp on aut_grp.graph_id=graph_data.graph_id INNER JOIN degrees on degrees.graph_id=graph_data.graph_id INNER JOIN misc on misc.graph_id=graph_data.graph_id INNER JOIN spectrum on spectrum.graph_id=graph_data.graph_id WHERE',query)
    query = re.sub('FROM graph_data WHERE','FROM graph_data INNER JOIN aut_grp on aut_grp.graph_id=graph_data.graph_id INNER JOIN degrees on degrees.graph_id=graph_data.graph_id INNER JOIN misc on misc.graph_id=graph_data.graph_id INNER JOIN spectrum on spectrum.graph_id=graph_data.graph_id WHERE',query)
    query = re.sub('SELECT graph_data.graph6','SELECT graph_data.graph6,graph_data.num_vertices,degrees.regular,aut_grp.aut_grp_size,graph_data.num_edges,degrees.min_degree,aut_grp.num_orbits,graph_data.num_cycles,degrees.max_degree,aut_grp.num_fixed_points,graph_data.num_hamiltonian_cycles,degrees.average_degree,aut_grp.vertex_transitive,graph_data.eulerian,degrees.degrees_sd,aut_grp.edge_transitive,graph_data.planar,degrees.degree_sequence,misc.vertex_connectivity,graph_data.perfect,spectrum.min_eigenvalue,misc.edge_connectivity,graph_data.lovasz_number,misc.girth,spectrum.max_eigenvalue,misc.num_cut_vertices,misc.independence_number,misc.radius,spectrum.eigenvalues_sd,misc.min_vertex_cover_size,misc.clique_number,misc.diameter,spectrum.energy,misc.num_spanning_trees,misc.num_components,graph_data.complement_graph6,spectrum.spectrum,misc.induced_subgraphs',query)
else:
    # Deal only with the string:
    param = query.__param_tuple__
    query = query.__query_string__
```



The problem is in the else block, where query is something. The problem is, this else block is confused about what that is.


---

Attachment


---

Comment by rlm created at 2007-10-25 19:10:44

This patches cleanly onto 2.8.9.


---

Comment by cwitty created at 2007-10-27 02:42:49

Resolution: fixed
