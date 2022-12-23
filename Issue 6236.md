# Issue 6236: find the dual graph of a planar graph

Issue created by migration from https://trac.sagemath.org/ticket/6236

Original creator: jason

Original creation time: 2009-06-06 21:59:04

Assignee: tbd

CC:  brunellus nvcleemp

Working code is here: http://sagenb.org/home/pub/417/

The worksheet also includes code which lists the faces of a planar embedding of a graph.


---

Comment by jason created at 2009-06-06 22:01:01

just in case sagenb.org goes down, here is the code:


```
def faces(g):
   d={}
   for key,val in g.get_embedding().iteritems():
       d[key]=dict(zip(val,val[1:]+[val[0]]))
   list_faces=[]
   for start in d:
       while d[start]:
           face=[]
           prev=start
           _,curr = d[start].popitem()
           face.append(start)
           while curr != start:
               face.append(curr)
               prev,curr = (curr, d[curr].pop(prev))
           list_faces.append(face)
   return list_faces

def graph_dual(g):
   f = [tuple(face) for face in faces(g)]
   f_edges = [tuple(zip(i,i[1:]+(i[0],))) for i in f]
   dual = Graph([f_edges,lambda f1,f2: set(f1).intersection([(e[1],e[0]) for e in f2])])
   return dual 

h=graphs.PathGraph(2)
g=h.disjoint_union(h).disjoint_union(h)
g=g.complement()
g.relabel()
show(g) 
        	

g.is_planar(set_embedding=True, set_pos=True)
show(g) 
        	

# The vertices forming the faces of the graph
faces(g) 
        	
dual_g=graph_dual(g) 
        	
# Each vertex is labeled with the edges of the face that it represents.
show(dual_g) 
        	

# We can relabel the vertices to get a "nice" graph, but then we lose the information about which face corresponds to which vertex.
dual_g.relabel()
show(dual_g) 
```



---

Comment by davidloeffler created at 2009-07-05 08:07:36

Changing component from algebra to graph theory.


---

Comment by davidloeffler created at 2009-07-05 08:07:36

Changing assignee from tbd to rlm.


---

Comment by davidloeffler created at 2009-07-05 08:07:36

This should be filed in "graph theory".


---

Comment by jason created at 2010-01-20 07:17:22

Changing type from defect to enhancement.


---

Comment by nvcleemp created at 2013-05-29 08:20:16

Hmm, I'm interested in this functionality, so if nobody else is planning on working on it, I would be up to it.

It seems that the code given as an example only 'works' for 3-edge-connected simple planar graphs. Is this sufficient, or should we also try to make it work for other graphs? Supporting multigraphs might depend on #14657.


---

Comment by jason created at 2013-05-29 14:46:32

IIRC, the only case I was interested in was cubic planar graphs, and it seemed that there was a nice simplification in that case.  Anyways, go for it!


---

Comment by ayyer created at 2014-11-17 06:18:15

Hi,

I'm interested in this functionality too!

> It seems that the code given as an example only 'works' for 3-edge-connected simple planar graphs. Is this sufficient, or should we also try to make it work for other graphs? Supporting multigraphs might depend on #14657.

What do you mean by 'works'? I don't know enough graph theory to interpret the code above, but if someone could fix this to take care of all planar graphs, I could try to include it.


---

Comment by nvcleemp created at 2014-11-18 06:18:20

Fixing it to work for all plane graphs is not that simple. The problem lies not so much with this code as with the support for plane graphs in Sage. At the moment plane multigraphs are not supported, and I guess that also plane graphs with loops are not supported.

If the input graph is not 3-edge-connected, then the dual will not be a simple plane graph, so no code will work for those graphs until we first add support for plane multigraphs and plane graphs with loops.


---

Comment by ayyer created at 2014-11-18 08:39:46

> If the input graph is not 3-edge-connected, then the dual will not be a simple plane graph, so no code will work for those graphs until we first add support for plane multigraphs and plane graphs with loops.

Ah, I see! Thanks for explaining the issue. Can we write a program to check for 3-edge-connectedness? If that is not too hard, then we can at least include the dual graph method for a large class of graphs (and many that other people are interested in). For graphs which fail that test, we can leave a `NotImplemented` error. Does that seem doable?


---

Comment by nvcleemp created at 2014-11-18 08:42:05

That is certainly doable, since that is already implemented. (At least I think so) At the moment I'm a bit swamped with work, but I'll have a look at it after next week. feel free to poke me if I forget it, or to have a look at it yourself.


---

Comment by ayyer created at 2014-11-18 08:47:15

But I just checked before writing the previous message! There's no `G.is_3_edge_connected()` or  `G.is_three_edge_connected()` or anything of that nature when I type  `G.is` and hit <tab>. Is there another equivalent definition? I'll look if so.


---

Comment by nvcleemp created at 2014-11-18 08:50:22

No, but there is a `G.edge_connectivity()`, so just use that and check that it is at least 3. Probably something more efficient is possible when we just want to know whether it is at least 3, but for now you can just use that.


---

Comment by ayyer created at 2014-11-18 09:09:32

Great, thanks! I'll use that. Should I create a new branch and add it to the graph methods in graph.py? What is a class of planar examples which are 3-edge-connected? I thought of grid graphs, but they fail. :(


---

Comment by nvcleemp created at 2014-11-18 09:13:18

The Platonic solids are 3-edge-connected. You need to have graphs with minimum degree at least 3, because otherwise deleting the edges incident to a vertex of minimum degree will disconnect the graph. Also have a look at the methods added by #16970.

Creating a new branch and adding to the graph methods seems the best approach. Be sure to read the developers guide.


---

Comment by moritz created at 2017-08-17 08:15:44

Meanwhile there is a function `.faces` for graphs. Therefore it would be quite straightforward to implement the planar dual; something along the lines of :


```
def planar_dual(P):
    return Graph([[tuple(_) for _ in P.faces()], lambda f,g: len(find_intersection(f,g))==1])
```


Therefore my question: Is this ticket really still open or has it been implemented elsewhere?


---

Comment by moritz created at 2017-08-17 08:15:44

Changing status from new to needs_info.


---

Comment by dcoudert created at 2017-08-17 09:39:15

I'm not aware of any such code in sagemath. So go for it.

There are trivial speedup improvements for the `.faces` method that I can implement in another ticket if you agree.


---

Comment by dcoudert created at 2017-08-17 11:48:28

Some speedup improvements are implemented in #23630. It also raises questions regarding the expected output when the graph has a single vertex and for disconnected graphs. It might impact the `planar_dual` method.


---

Comment by moritz created at 2017-08-18 15:15:29

Changing status from needs_info to needs_review.


---

Comment by moritz created at 2017-08-18 15:15:29

I added the method, avoiding the potential difficulties with multi-edges etc, by requiring the graph to be 3-connected.  (Better to have it in these cases than nothing...)
----
New commits:


---

Comment by dcoudert created at 2017-08-18 16:26:31

Why are you asking for 3-edge-connectivity ? If it's to prevent graphs with a cut-vertex, the requirement is not sufficient and actually the method is apparently working in this case.

```
sage: G = graphs.IcosahedralGraph()*2
sage: G.merge_vertices([0,12])
sage: G.planar_dual()
Graph on 39 vertices
```

We cannot get the dual of a 2d grid or a cycle. 
------
We really need a proper implementation of the decomposition into 3 connected components, or an interface with `OGDF` since it has a fast (and surely the only) implementation of the linear time algorithm.


---

Comment by moritz created at 2017-08-18 16:46:58

Sorry, I got "edge-connected" confused with "vertex-connected"


---

Comment by git created at 2017-08-18 16:48:44

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by dcoudert created at 2017-08-18 16:53:12

Why 3 ? With 2-vertex-connected we could get the dual of cycles, grids, etc.

Please change:
- `Finding the planar_dual is only works if the graph is at least 3 vertex-connected` -> `the graph must be at least 3-vertex-connected`


---

Comment by git created at 2017-08-18 18:48:54

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by moritz created at 2017-08-18 18:50:51

Replying to [comment:23 dcoudert]:
> Why 3 ? With 2-vertex-connected we could get the dual of cycles, grids, etc.
Because then the dual will potentially have multiple edges. Take a square as an example: the dual graph has two vertices with 4 parallel edges. 
 
> Please change:
> - `Finding the planar_dual is only works if the graph is at least 3 vertex-connected` -> `the graph must be at least 3-vertex-connected`
done


---

Comment by git created at 2017-08-18 19:13:50

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by dcoudert created at 2017-08-19 07:47:28

Some comments:
- add method `planar_dual` in the `Plot/embedding-related methods` table at the top of the file
- `Return the planar dual an embedded graph.` -> `Return the planar dual of an embedded graph.` ?
- if a graph is 4-vertex-connected, then it is also 3-vertex-connected. So you don't need to specify `at least 3-vertex-connected`.
- the `SEEALSO` block must be after the `EXAMPLES` block
- `for g in  [_ for _ in graphs.planar_graphs(i, minimum_connectivity=3)]` -> `for g in  graphs.planar_graphs(i, minimum_connectivity=3)`
- In fact, the tests using `graphs.planar_graphs` are nice but unduly time consuming. Add 2 sec for the doctests of `generic_graph.py` on my laptop. This is too much. You should use simpler / faster tests.
- in the `TODO` block. You can simply write: `Implement the method for graphs that are not 3-vertex-connected (or at least have a faster 3-vertex-connectivity test)`.
- Usually, we use `from sage.graphs.graph import Graph` and not `from . import graph`. You should do the same
- you have not corrected the not implemented message


---

Comment by git created at 2017-08-19 08:34:52

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by moritz created at 2017-08-19 08:37:48

Thanks for the comments, David!

I tried to work in the suggested imrovements. 

First I had tried to put `from sage.graphs.graph import Graph` in the top of the file, where all the imports are made, but this failed, due to circular imports.


---

Comment by dcoudert created at 2017-08-19 10:07:50

Changing status from needs_review to positive_review.


---

Comment by dcoudert created at 2017-08-19 10:07:50

For me this ticket is good to go (tests, docbuild and display ok, etc.)


---

Comment by vbraun created at 2017-08-20 08:31:05

Not sure if you inted to merge this, but without milestone it won't...


---

Comment by dcoudert created at 2017-08-20 08:34:30

Right. Thank you.


---

Comment by vbraun created at 2017-08-26 09:58:12

Resolution: fixed
