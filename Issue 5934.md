# Issue 5934: [with spkg; needs review] networkx -- fix bad spkg

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-29 15:32:06

Assignee: rlm

#4860 was messed up

The networkx-0.99.p0.spkg currently in Sage contains both networkx 0.36 (what we use) and networkx 0.99.    When installed, only the old version is installed.  This has two negatives:

(1) it wastes disk space

(2) it confuses users, e.g., it made me feel like an idiot when I posted to the networkx-discuss mailing list about all their examples being broken.  I carefully checked Sage had networkx 0.99 by looking in spkg/standard, only to be fooled. 

Possible fixes:

  1. Just revert to the previous networkx spkg.  This will not solve the problem I ran into though, since sage -upgrade won't downgrade. 
  
  2. Make a new networkx spkg called networkx-0.99.p1-fake_really-0.36 and delete src/networkx-0.99 from it.


I've posted an spkg that does 2:

http://wstein.org/home/wstein/patches/networkx-0.99.p1-fake_really-0.36.spkg

By the way, this was all discussed here: http://groups.google.com/group/sage-devel/browse_thread/thread/e677517098468e32





---

Comment by mvngu created at 2009-05-05 05:03:39

REFEREE REPORT



The results of #4860 were due to bad refereeing on my part.



The current version of NetworkX in Sage 3.4.2 is, as stated, actually version 0.36 instead of 0.99 as claimed by the spkg name in SAGE_ROOT/spkg/standard. Version 0.35.1 has a demo/toy/testing implementation of `edge_betweenness`, whereas version 0.36 has an actual working implementation. Furthermore, version 0.36 doesn't have the module `networkx/matching.py`, which was introduced in 0.37. Also, 0.99 has a lot of stuff under `networkx/algorithms`, whereas 0.36 doesn't even have such a directory. So with the current actual version 0.36 as shipped with Sage 3.4.2, the following is expected:

```
sage: # version 0.36 has a working edge_centrality for the first time
sage: from networkx import *
sage: G = Graph()
sage: G.add_node(1)
sage: G.add_nodes_from([2,3])
sage: H=path_graph(10)
sage: G.add_nodes_from(H)
sage: G.add_node(H)
sage: G.add_edge( (1,2) )
sage: G.add_edges_from([(1,2),(1,3)])
sage: G.add_edges_from(H.edges())
sage: networkx.centrality.edge_betweenness(G)

{(0, 1): 0.25,
 (1, 2): 0.055555555555555552,
 (1, 3): 0.38888888888888884,
 (2, 3): 0.19444444444444442,
 (3, 4): 0.66666666666666663,
 (4, 5): 0.69444444444444442,
 (5, 6): 0.66666666666666663,
 (6, 7): 0.58333333333333326,
 (7, 8): 0.44444444444444442,
 (8, 9): 0.25}
sage: 
sage: # networkx.algorithms.* not in version 0.36, but appears in version 0.99
sage: from networkx.algorithms.isomorphism.isomorph import graph_could_be_isomorphic as isomorphic
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

/home/mvngu/.sage/temp/sage.math.washington.edu/8026/_home_mvngu__sage_init_sage_0.py in <module>()

ImportError: No module named algorithms.isomorphism.isomorph
sage: 
sage: # version 0.36 doesn't have networkx.matching, which appears for the first time in 0.37
sage: import networkx.matching
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

/home/mvngu/.sage/temp/sage.math.washington.edu/8026/_home_mvngu__sage_init_sage_0.py in <module>()

ImportError: No module named matching
```



After installing the fake spkg `0.99.p1` with



sage -i http://wstein.org/home/wstein/patches/networkx-0.99.p1-fake_really-0.36.spkg



and rebuilding with `sage -b`, I ran all tests on `sage/graphs` with the options `-t -long` and the tests passed. Running the same commands as above that use NetworkX returned similar results:

```
# version 0.36 has a working edge_centrality for the first time
sage: from networkx import *
sage: G = Graph()
sage: G.add_node(1)
sage: G.add_nodes_from([2,3])
sage: H=path_graph(10)
sage: G.add_nodes_from(H)
sage: G.add_node(H)
sage: G.add_edge( (1,2) )
sage: G.add_edges_from([(1,2),(1,3)])
sage: G.add_edges_from(H.edges())
sage: networkx.centrality.edge_betweenness(G)

{(0, 1): 0.25,
 (1, 2): 0.055555555555555552,
 (1, 3): 0.38888888888888884,
 (2, 3): 0.19444444444444442,
 (3, 4): 0.66666666666666663,
 (4, 5): 0.69444444444444442,
 (5, 6): 0.66666666666666663,
 (6, 7): 0.58333333333333326,
 (7, 8): 0.44444444444444442,
 (8, 9): 0.25}
sage: 
sage: # networkx.algorithms.* not in version 0.36, but appears in version 0.99
sage: from networkx.algorithms.isomorphism.isomorph import graph_could_be_isomorphic as isomorphic
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

/home/mvngu/.sage/temp/sage.math.washington.edu/22888/_home_mvngu__sage_init_sage_0.py in <module>()

ImportError: No module named algorithms.isomorphism.isomorph
sage: 
sage: # version 0.36 doesn't have networkx.matching, which appears for the first time in 0.37
sage: import networkx.matching
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

/home/mvngu/.sage/temp/sage.math.washington.edu/22888/_home_mvngu__sage_init_sage_0.py in <module>()

ImportError: No module named matching
```

So on the one hand, the fake `0.99.p1` installs OK against Sage 3.4.2 and all tests passed even with the option `-long`. On the other hand, it is precisely (fingers crossed) version 0.36 of NetworkX as argued above. I hope I've redeemed myself.


---

Comment by mabshoff created at 2009-05-05 05:07:29

I see little point in downgrading the spkg - why not fix the problem in the first place and use NetworkX 0.99?

Cheers,

Michael


---

Comment by mvngu created at 2009-05-05 05:19:20

From the look of it, I think it's more of a name change as the NetworkX code in `SAGE_ROOT/spkg/standard/networkx-0.99.p0.spkg` and at 



http://wstein.org/home/wstein/patches/networkx-0.99.p1-fake_really-0.36.spkg



essentially belong to the same version, viz. 0.36. From my reading of 0.99, there are some major changes in the API and heaps of modules have been shuffled around, which potentially break some doctests in `sage/graphs/*`. But that's just my suspicion, as I've not actually tried to create an spkg of NetworkX 0.99 and test things out with Sage 3.4.2. So I'm happy with William's spkg on the one hand, and also with an spkg of 0.99 on the other.


---

Comment by rlm created at 2009-05-05 16:01:14

Replying to [comment:3 mabshoff]:
> I see little point in downgrading the spkg - why not fix the problem in the first place and use NetworkX 0.99?

NetworkX changes too drastically from release to release to base Sage graphs on. Until we can finish our own implementation, it is much easier to stick to version 0.36.


---

Comment by mabshoff created at 2009-05-12 20:24:44

Merged the fake spkg in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-12 20:24:44

Resolution: fixed


---

Comment by jason created at 2009-05-14 13:44:07

Replying to [comment:5 rlm]:
> Replying to [comment:3 mabshoff]:
> > I see little point in downgrading the spkg - why not fix the problem in the first place and use NetworkX 0.99?
> 
> NetworkX changes too drastically from release to release to base Sage graphs on. Until we can finish our own implementation, it is much easier to stick to version 0.36.

I think this is a bit unfair to characterize NetworkX this way.  They did a major rewrite between versions 0.37 and 0.99, hence had some API changes.  They have a helpful page addressing API changes: http://networkx.lanl.gov/reference/api_changes.html.  I think it does require some resources to make sure that we work with 0.99, but that is normal updating based on a new major release of a project, not a constantly changing project that is difficult to keep up with.  NetworkX still saves us a lot of time implementing a number of algorithms that they already have.

That said, I don't have time right now to update to 0.99.  However, I think updating to 0.99 is a very feasible project for a student, for example.  My guess (given how seldom networkx is updated) the effort would not be wasted at all.


---

Comment by mvngu created at 2009-05-15 06:15:55

Replying to [comment:7 jason]:
<SNIP>
> That said, I don't have time right now to update to 0.99.  However, I think updating to 0.99 is a very feasible project for a student, for example.  My guess (given how seldom networkx is updated) the effort would not be wasted at all.


I'm on it. Please refer to #6041.
