# Issue 6236: find the dual graph of a planar graph

archive/issues_006236.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  brunellus @nvcleemp\n\nWorking code is here: http://sagenb.org/home/pub/417/\n\nThe worksheet also includes code which lists the faces of a planar embedding of a graph.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6236\n\n",
    "created_at": "2009-06-06T21:59:04Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.1",
    "title": "find the dual graph of a planar graph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6236",
    "user": "@jasongrout"
}
```
Assignee: tbd

CC:  brunellus @nvcleemp

Working code is here: http://sagenb.org/home/pub/417/

The worksheet also includes code which lists the faces of a planar embedding of a graph.

Issue created by migration from https://trac.sagemath.org/ticket/6236





---

archive/issue_comments_049783.json:
```json
{
    "body": "just in case sagenb.org goes down, here is the code:\n\n\n```\ndef faces(g):\n   d={}\n   for key,val in g.get_embedding().iteritems():\n       d[key]=dict(zip(val,val[1:]+[val[0]]))\n   list_faces=[]\n   for start in d:\n       while d[start]:\n           face=[]\n           prev=start\n           _,curr = d[start].popitem()\n           face.append(start)\n           while curr != start:\n               face.append(curr)\n               prev,curr = (curr, d[curr].pop(prev))\n           list_faces.append(face)\n   return list_faces\n\ndef graph_dual(g):\n   f = [tuple(face) for face in faces(g)]\n   f_edges = [tuple(zip(i,i[1:]+(i[0],))) for i in f]\n   dual = Graph([f_edges,lambda f1,f2: set(f1).intersection([(e[1],e[0]) for e in f2])])\n   return dual \n\nh=graphs.PathGraph(2)\ng=h.disjoint_union(h).disjoint_union(h)\ng=g.complement()\ng.relabel()\nshow(g) \n        \t\n\ng.is_planar(set_embedding=True, set_pos=True)\nshow(g) \n        \t\n\n# The vertices forming the faces of the graph\nfaces(g) \n        \t\ndual_g=graph_dual(g) \n        \t\n# Each vertex is labeled with the edges of the face that it represents.\nshow(dual_g) \n        \t\n\n# We can relabel the vertices to get a \"nice\" graph, but then we lose the information about which face corresponds to which vertex.\ndual_g.relabel()\nshow(dual_g) \n```\n",
    "created_at": "2009-06-06T22:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49783",
    "user": "@jasongrout"
}
```

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

archive/issue_comments_049784.json:
```json
{
    "body": "Changing component from algebra to graph theory.",
    "created_at": "2009-07-05T08:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49784",
    "user": "@loefflerd"
}
```

Changing component from algebra to graph theory.



---

archive/issue_comments_049785.json:
```json
{
    "body": "Changing assignee from tbd to @rlmill.",
    "created_at": "2009-07-05T08:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49785",
    "user": "@loefflerd"
}
```

Changing assignee from tbd to @rlmill.



---

archive/issue_comments_049786.json:
```json
{
    "body": "This should be filed in \"graph theory\".",
    "created_at": "2009-07-05T08:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49786",
    "user": "@loefflerd"
}
```

This should be filed in "graph theory".



---

archive/issue_comments_049787.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-01-20T07:17:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49787",
    "user": "@jasongrout"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_049788.json:
```json
{
    "body": "Hmm, I'm interested in this functionality, so if nobody else is planning on working on it, I would be up to it.\n\nIt seems that the code given as an example only 'works' for 3-edge-connected simple planar graphs. Is this sufficient, or should we also try to make it work for other graphs? Supporting multigraphs might depend on #14657.",
    "created_at": "2013-05-29T08:20:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49788",
    "user": "@nvcleemp"
}
```

Hmm, I'm interested in this functionality, so if nobody else is planning on working on it, I would be up to it.

It seems that the code given as an example only 'works' for 3-edge-connected simple planar graphs. Is this sufficient, or should we also try to make it work for other graphs? Supporting multigraphs might depend on #14657.



---

archive/issue_comments_049789.json:
```json
{
    "body": "IIRC, the only case I was interested in was cubic planar graphs, and it seemed that there was a nice simplification in that case.  Anyways, go for it!",
    "created_at": "2013-05-29T14:46:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49789",
    "user": "@jasongrout"
}
```

IIRC, the only case I was interested in was cubic planar graphs, and it seemed that there was a nice simplification in that case.  Anyways, go for it!



---

archive/issue_comments_049790.json:
```json
{
    "body": "Hi,\n\nI'm interested in this functionality too!\n\n> It seems that the code given as an example only 'works' for 3-edge-connected simple planar graphs. Is this sufficient, or should we also try to make it work for other graphs? Supporting multigraphs might depend on #14657.\n\nWhat do you mean by 'works'? I don't know enough graph theory to interpret the code above, but if someone could fix this to take care of all planar graphs, I could try to include it.",
    "created_at": "2014-11-17T06:18:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49790",
    "user": "@ayyer"
}
```

Hi,

I'm interested in this functionality too!

> It seems that the code given as an example only 'works' for 3-edge-connected simple planar graphs. Is this sufficient, or should we also try to make it work for other graphs? Supporting multigraphs might depend on #14657.

What do you mean by 'works'? I don't know enough graph theory to interpret the code above, but if someone could fix this to take care of all planar graphs, I could try to include it.



---

archive/issue_comments_049791.json:
```json
{
    "body": "Fixing it to work for all plane graphs is not that simple. The problem lies not so much with this code as with the support for plane graphs in Sage. At the moment plane multigraphs are not supported, and I guess that also plane graphs with loops are not supported.\n\nIf the input graph is not 3-edge-connected, then the dual will not be a simple plane graph, so no code will work for those graphs until we first add support for plane multigraphs and plane graphs with loops.",
    "created_at": "2014-11-18T06:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49791",
    "user": "@nvcleemp"
}
```

Fixing it to work for all plane graphs is not that simple. The problem lies not so much with this code as with the support for plane graphs in Sage. At the moment plane multigraphs are not supported, and I guess that also plane graphs with loops are not supported.

If the input graph is not 3-edge-connected, then the dual will not be a simple plane graph, so no code will work for those graphs until we first add support for plane multigraphs and plane graphs with loops.



---

archive/issue_comments_049792.json:
```json
{
    "body": "> If the input graph is not 3-edge-connected, then the dual will not be a simple plane graph, so no code will work for those graphs until we first add support for plane multigraphs and plane graphs with loops.\n\nAh, I see! Thanks for explaining the issue. Can we write a program to check for 3-edge-connectedness? If that is not too hard, then we can at least include the dual graph method for a large class of graphs (and many that other people are interested in). For graphs which fail that test, we can leave a `NotImplemented` error. Does that seem doable?",
    "created_at": "2014-11-18T08:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49792",
    "user": "@ayyer"
}
```

> If the input graph is not 3-edge-connected, then the dual will not be a simple plane graph, so no code will work for those graphs until we first add support for plane multigraphs and plane graphs with loops.

Ah, I see! Thanks for explaining the issue. Can we write a program to check for 3-edge-connectedness? If that is not too hard, then we can at least include the dual graph method for a large class of graphs (and many that other people are interested in). For graphs which fail that test, we can leave a `NotImplemented` error. Does that seem doable?



---

archive/issue_comments_049793.json:
```json
{
    "body": "That is certainly doable, since that is already implemented. (At least I think so) At the moment I'm a bit swamped with work, but I'll have a look at it after next week. feel free to poke me if I forget it, or to have a look at it yourself.",
    "created_at": "2014-11-18T08:42:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49793",
    "user": "@nvcleemp"
}
```

That is certainly doable, since that is already implemented. (At least I think so) At the moment I'm a bit swamped with work, but I'll have a look at it after next week. feel free to poke me if I forget it, or to have a look at it yourself.



---

archive/issue_comments_049794.json:
```json
{
    "body": "But I just checked before writing the previous message! There's no `G.is_3_edge_connected()` or  `G.is_three_edge_connected()` or anything of that nature when I type  `G.is` and hit <tab>. Is there another equivalent definition? I'll look if so.",
    "created_at": "2014-11-18T08:47:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49794",
    "user": "@ayyer"
}
```

But I just checked before writing the previous message! There's no `G.is_3_edge_connected()` or  `G.is_three_edge_connected()` or anything of that nature when I type  `G.is` and hit <tab>. Is there another equivalent definition? I'll look if so.



---

archive/issue_comments_049795.json:
```json
{
    "body": "No, but there is a `G.edge_connectivity()`, so just use that and check that it is at least 3. Probably something more efficient is possible when we just want to know whether it is at least 3, but for now you can just use that.",
    "created_at": "2014-11-18T08:50:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49795",
    "user": "@nvcleemp"
}
```

No, but there is a `G.edge_connectivity()`, so just use that and check that it is at least 3. Probably something more efficient is possible when we just want to know whether it is at least 3, but for now you can just use that.



---

archive/issue_comments_049796.json:
```json
{
    "body": "Great, thanks! I'll use that. Should I create a new branch and add it to the graph methods in graph.py? What is a class of planar examples which are 3-edge-connected? I thought of grid graphs, but they fail. :(",
    "created_at": "2014-11-18T09:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49796",
    "user": "@ayyer"
}
```

Great, thanks! I'll use that. Should I create a new branch and add it to the graph methods in graph.py? What is a class of planar examples which are 3-edge-connected? I thought of grid graphs, but they fail. :(



---

archive/issue_comments_049797.json:
```json
{
    "body": "The Platonic solids are 3-edge-connected. You need to have graphs with minimum degree at least 3, because otherwise deleting the edges incident to a vertex of minimum degree will disconnect the graph. Also have a look at the methods added by #16970.\n\nCreating a new branch and adding to the graph methods seems the best approach. Be sure to read the developers guide.",
    "created_at": "2014-11-18T09:13:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49797",
    "user": "@nvcleemp"
}
```

The Platonic solids are 3-edge-connected. You need to have graphs with minimum degree at least 3, because otherwise deleting the edges incident to a vertex of minimum degree will disconnect the graph. Also have a look at the methods added by #16970.

Creating a new branch and adding to the graph methods seems the best approach. Be sure to read the developers guide.



---

archive/issue_comments_049798.json:
```json
{
    "body": "Meanwhile there is a function `.faces` for graphs. Therefore it would be quite straightforward to implement the planar dual; something along the lines of :\n\n\n```\ndef planar_dual(P):\n    return Graph([[tuple(_) for _ in P.faces()], lambda f,g: len(find_intersection(f,g))==1])\n```\n\n\nTherefore my question: Is this ticket really still open or has it been implemented elsewhere?",
    "created_at": "2017-08-17T08:15:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49798",
    "user": "@mo271"
}
```

Meanwhile there is a function `.faces` for graphs. Therefore it would be quite straightforward to implement the planar dual; something along the lines of :


```
def planar_dual(P):
    return Graph([[tuple(_) for _ in P.faces()], lambda f,g: len(find_intersection(f,g))==1])
```


Therefore my question: Is this ticket really still open or has it been implemented elsewhere?



---

archive/issue_comments_049799.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2017-08-17T08:15:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49799",
    "user": "@mo271"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_049800.json:
```json
{
    "body": "I'm not aware of any such code in sagemath. So go for it.\n\nThere are trivial speedup improvements for the `.faces` method that I can implement in another ticket if you agree.",
    "created_at": "2017-08-17T09:39:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49800",
    "user": "@dcoudert"
}
```

I'm not aware of any such code in sagemath. So go for it.

There are trivial speedup improvements for the `.faces` method that I can implement in another ticket if you agree.



---

archive/issue_comments_049801.json:
```json
{
    "body": "Some speedup improvements are implemented in #23630. It also raises questions regarding the expected output when the graph has a single vertex and for disconnected graphs. It might impact the `planar_dual` method.",
    "created_at": "2017-08-17T11:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49801",
    "user": "@dcoudert"
}
```

Some speedup improvements are implemented in #23630. It also raises questions regarding the expected output when the graph has a single vertex and for disconnected graphs. It might impact the `planar_dual` method.



---

archive/issue_comments_049802.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2017-08-18T15:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49802",
    "user": "@mo271"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_049803.json:
```json
{
    "body": "I added the method, avoiding the potential difficulties with multi-edges etc, by requiring the graph to be 3-connected.  (Better to have it in these cases than nothing...)\n----\nNew commits:",
    "created_at": "2017-08-18T15:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49803",
    "user": "@mo271"
}
```

I added the method, avoiding the potential difficulties with multi-edges etc, by requiring the graph to be 3-connected.  (Better to have it in these cases than nothing...)
----
New commits:



---

archive/issue_comments_049804.json:
```json
{
    "body": "Why are you asking for 3-edge-connectivity ? If it's to prevent graphs with a cut-vertex, the requirement is not sufficient and actually the method is apparently working in this case.\n\n```\nsage: G = graphs.IcosahedralGraph()*2\nsage: G.merge_vertices([0,12])\nsage: G.planar_dual()\nGraph on 39 vertices\n```\n\nWe cannot get the dual of a 2d grid or a cycle. \n------\nWe really need a proper implementation of the decomposition into 3 connected components, or an interface with `OGDF` since it has a fast (and surely the only) implementation of the linear time algorithm.",
    "created_at": "2017-08-18T16:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49804",
    "user": "@dcoudert"
}
```

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

archive/issue_comments_049805.json:
```json
{
    "body": "Sorry, I got \"edge-connected\" confused with \"vertex-connected\"",
    "created_at": "2017-08-18T16:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49805",
    "user": "@mo271"
}
```

Sorry, I got "edge-connected" confused with "vertex-connected"



---

archive/issue_comments_049806.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-08-18T16:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49806",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_049807.json:
```json
{
    "body": "Why 3 ? With 2-vertex-connected we could get the dual of cycles, grids, etc.\n\nPlease change:\n- `Finding the planar_dual is only works if the graph is at least 3 vertex-connected` -> `the graph must be at least 3-vertex-connected`",
    "created_at": "2017-08-18T16:53:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49807",
    "user": "@dcoudert"
}
```

Why 3 ? With 2-vertex-connected we could get the dual of cycles, grids, etc.

Please change:
- `Finding the planar_dual is only works if the graph is at least 3 vertex-connected` -> `the graph must be at least 3-vertex-connected`



---

archive/issue_comments_049808.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-08-18T18:48:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49808",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_049809.json:
```json
{
    "body": "Replying to [comment:23 dcoudert]:\n> Why 3 ? With 2-vertex-connected we could get the dual of cycles, grids, etc.\nBecause then the dual will potentially have multiple edges. Take a square as an example: the dual graph has two vertices with 4 parallel edges. \n \n> Please change:\n> - `Finding the planar_dual is only works if the graph is at least 3 vertex-connected` -> `the graph must be at least 3-vertex-connected`\ndone",
    "created_at": "2017-08-18T18:50:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49809",
    "user": "@mo271"
}
```

Replying to [comment:23 dcoudert]:
> Why 3 ? With 2-vertex-connected we could get the dual of cycles, grids, etc.
Because then the dual will potentially have multiple edges. Take a square as an example: the dual graph has two vertices with 4 parallel edges. 
 
> Please change:
> - `Finding the planar_dual is only works if the graph is at least 3 vertex-connected` -> `the graph must be at least 3-vertex-connected`
done



---

archive/issue_comments_049810.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-08-18T19:13:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49810",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_049811.json:
```json
{
    "body": "Some comments:\n- add method `planar_dual` in the `Plot/embedding-related methods` table at the top of the file\n- `Return the planar dual an embedded graph.` -> `Return the planar dual of an embedded graph.` ?\n- if a graph is 4-vertex-connected, then it is also 3-vertex-connected. So you don't need to specify `at least 3-vertex-connected`.\n- the `SEEALSO` block must be after the `EXAMPLES` block\n- `for g in  [_ for _ in graphs.planar_graphs(i, minimum_connectivity=3)]` -> `for g in  graphs.planar_graphs(i, minimum_connectivity=3)`\n- In fact, the tests using `graphs.planar_graphs` are nice but unduly time consuming. Add 2 sec for the doctests of `generic_graph.py` on my laptop. This is too much. You should use simpler / faster tests.\n- in the `TODO` block. You can simply write: `Implement the method for graphs that are not 3-vertex-connected (or at least have a faster 3-vertex-connectivity test)`.\n- Usually, we use `from sage.graphs.graph import Graph` and not `from . import graph`. You should do the same\n- you have not corrected the not implemented message",
    "created_at": "2017-08-19T07:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49811",
    "user": "@dcoudert"
}
```

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

archive/issue_comments_049812.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-08-19T08:34:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49812",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_049813.json:
```json
{
    "body": "Thanks for the comments, David!\n\nI tried to work in the suggested imrovements. \n\nFirst I had tried to put `from sage.graphs.graph import Graph` in the top of the file, where all the imports are made, but this failed, due to circular imports.",
    "created_at": "2017-08-19T08:37:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49813",
    "user": "@mo271"
}
```

Thanks for the comments, David!

I tried to work in the suggested imrovements. 

First I had tried to put `from sage.graphs.graph import Graph` in the top of the file, where all the imports are made, but this failed, due to circular imports.



---

archive/issue_comments_049814.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-08-19T10:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49814",
    "user": "@dcoudert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_049815.json:
```json
{
    "body": "For me this ticket is good to go (tests, docbuild and display ok, etc.)",
    "created_at": "2017-08-19T10:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49815",
    "user": "@dcoudert"
}
```

For me this ticket is good to go (tests, docbuild and display ok, etc.)



---

archive/issue_comments_049816.json:
```json
{
    "body": "Not sure if you inted to merge this, but without milestone it won't...",
    "created_at": "2017-08-20T08:31:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49816",
    "user": "@vbraun"
}
```

Not sure if you inted to merge this, but without milestone it won't...



---

archive/issue_comments_049817.json:
```json
{
    "body": "Right. Thank you.",
    "created_at": "2017-08-20T08:34:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49817",
    "user": "@dcoudert"
}
```

Right. Thank you.



---

archive/issue_comments_049818.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2017-08-26T09:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6236#issuecomment-49818",
    "user": "@vbraun"
}
```

Resolution: fixed
