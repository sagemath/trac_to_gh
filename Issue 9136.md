# Issue 9136: more named graphs

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-06-03 22:09:47

Assignee: jason, ncohen, rlm

CC:  brunellus

The [database of common graphs](http://www.sagemath.org/doc/reference/sage/graphs/graph_generators.html) currently implements lots of named graphs. Here is a list of named graphs to add to that database:

 * [Balaban 10-cage](http://en.wikipedia.org/wiki/Balaban_10-cage)
 * [Balaban 11-cage](http://en.wikipedia.org/wiki/Balaban_11-cage)
 * [Bidiakis cube](http://en.wikipedia.org/wiki/Bidiakis_cube)
 * [Brinkmann graph](http://en.wikipedia.org/wiki/Brinkmann_graph)
 * [Butterfly graph](http://en.wikipedia.org/wiki/Butterfly_graph)
 * [Double-star snark](http://en.wikipedia.org/wiki/Double-star_snark)
 * [Dürer graph](http://en.wikipedia.org/wiki/D%C3%BCrer_graph)
 * [Ellingham–Horton graph](http://en.wikipedia.org/wiki/Ellingham%E2%80%93Horton_graph)
 * [Errera graph](http://en.wikipedia.org/wiki/Errera_graph)
 * [Franklin graph](http://en.wikipedia.org/wiki/Franklin_graph)
 * [fullerene graphs](http://en.wikipedia.org/wiki/Gallery_of_named_graphs#Fullerene_graphs)
 * [Goldner–Harary graph](http://en.wikipedia.org/wiki/Goldner%E2%80%93Harary_graph)
 * [Grötzsch graph](http://en.wikipedia.org/wiki/Gr%C3%B6tzsch_graph)
 * [Harries–Wong graph](http://en.wikipedia.org/wiki/Harries-Wong_graph)
 * [Herschel graph](http://en.wikipedia.org/wiki/Herschel_graph)
 * [Hoffman graph](http://en.wikipedia.org/wiki/Hoffman_graph)
 * [Holt graph](http://en.wikipedia.org/wiki/Holt_graph)
 * [Horton graph](http://en.wikipedia.org/wiki/Horton_graph)
 * [Kittell graph](http://mathworld.wolfram.com/KittellGraph.html)
 * [Markström graph](http://commons.wikimedia.org/wiki/File:Markstr%C3%B6m-Graph.svg)
 * [McGee graph](http://en.wikipedia.org/wiki/McGee_graph)
 * [Meredith graph](http://en.wikipedia.org/wiki/Meredith_graph)
 * [Moser spindle](http://mathworld.wolfram.com/MoserSpindle.html)
 * [Sousselier graph](http://en.wikipedia.org/wiki/File:Sousselier_graph.svg)
 * [Poussin graph](http://mathworld.wolfram.com/PoussinGraph.html)
 * [Robertson graph](http://en.wikipedia.org/wiki/Robertson_graph)
 * [Tutte's fragment](http://en.wikipedia.org/wiki/Tutte%27s_fragment)
 * [Tutte graph](http://en.wikipedia.org/wiki/Tutte_graph)
 * [Young–Fibonacci lattice](http://en.wikipedia.org/wiki/Young%E2%80%93Fibonacci_lattice)
 * [Wagner graph](http://en.wikipedia.org/wiki/Wagner_graph)
 * [Wiener-Araya graph](http://mathworld.wolfram.com/Wiener-ArayaGraph.html)
 * [Clebsch graph](http://en.wikipedia.org/wiki/Clebsch_graph)
 * [Hall–Janko graph](http://en.wikipedia.org/wiki/Hall%E2%80%93Janko_graph)
 * [Paley graph](http://en.wikipedia.org/wiki/Paley_graph)
 * [Shrikhande graph](http://en.wikipedia.org/wiki/Shrikhande_graph)
 * [Möbius–Kantor graph](http://en.wikipedia.org/wiki/M%C3%B6bius%E2%80%93Kantor_graph)
 * [Nauru graph](http://en.wikipedia.org/wiki/Nauru_graph)
 * [Coxeter graph](http://en.wikipedia.org/wiki/Coxeter_graph)
 * [Tutte–Coxeter graph](http://en.wikipedia.org/wiki/Tutte%E2%80%93Coxeter_graph)
 * [Dyck graph](http://en.wikipedia.org/wiki/Dyck_graph)
 * [Foster graph](http://en.wikipedia.org/wiki/Foster_graph)
 * [Biggs–Smith graph](http://en.wikipedia.org/wiki/Biggs-Smith_graph)
 * [Rado graph](http://en.wikipedia.org/wiki/Rado_graph)
 * [Folkman graph](http://en.wikipedia.org/wiki/Folkman_graph)
 * [Gray graph](http://en.wikipedia.org/wiki/Gray_graph)
 * [Ljubljana graph](http://en.wikipedia.org/wiki/Ljubljana_graph)
 * [Tutte 12-cage](http://en.wikipedia.org/wiki/Tutte_12-cage)
 * [Friendship graph](http://en.wikipedia.org/wiki/Friendship_graph)
 * [Blanuša snarks](http://en.wikipedia.org/wiki/Blanu%C5%A1a_snarks)
 * [Szekeres snark](http://en.wikipedia.org/wiki/Szekeres_snark)
 * [Tietze's graph](http://en.wikipedia.org/wiki/Tietze_graph)
 * [Watkins snark](http://en.wikipedia.org/wiki/Watkins_snark)


---

Comment by ncohen created at 2010-06-04 07:07:51

My god O_O
SO you are basically saying I'm not sending enough ? :-D

To be honest I have tried to implement some of them, but felt I should ask for the help of Sage's algebraists... This one, for example : is there any way to build it using Sage's tools ?

http://www.win.tue.nl/~aeb/graphs/Schlaefli.html

Nathann


---

Comment by dimpase created at 2010-11-24 16:26:50

Many of these graphs can be trivially generated in GAP using its package Grape (a part of the optional gap_packages spkg) and
a library of primitive groups (a part of optional databases_gap spkg).
E.g. here is how to get Schlaefli graph:

```
sage: gap.load_package('grape')
sage: gap.eval('G:=NullGraph(PrimitiveGroup(27,12),27);')
'rec( isGraph := true, order := 27, group := PSp(4, 3), \n  schreierVector := [ -1, 1, 2, 1, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 1, \n      2, 1, 1, 2, 2, 1, 1, 1, 2 ], adjacencies := [ [  ] ], \n  representatives := [ 1 ], isSimple := true )'
sage: gap.eval('AddEdgeOrbit(G,[1,2]);')
''
sage: gap.eval('VertexDegrees(G);')
'[ 10 ]'
sage: edges=gap('Orbit(G.group,[1,2],OnSets)')
sage: len(edges)
135
sage: schlaefli=Graph([[int(x[1])-1,int(x[2])-1] for x in edges])
sage: schlaefli.degree()
[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
sage: schlaefli.diameter()
2
```


IMHO there is a more fundamental issue here: Sage should handle such graphs in an efficient way --- just keeping all the edges is pretty much a waste, in particular for bigger examples with hundreds of vertices...


---

Comment by dimpase created at 2010-11-24 16:44:51

Replying to [comment:7 dimpase]:
> Many of these graphs can be trivially generated in GAP using its package Grape (a part of the optional gap_packages spkg) and
> a library of primitive groups (a part of optional databases_gap spkg).

actually, Grape isn't even needed (I mentioned it for illustrative purposes): to construct the Sage graph, 
all you need is the following:


```
sage: edges=gap('Orbit(PrimitiveGroup(27,12),[1,2],OnSets)')
sage: schlaefli=Graph([[int(x[1])-1,int(x[2])-1] for x in edges])
```


PS. To get e.g. Hall-Janko graph, use `PrimitiveGroup(100,1)`...


---

Comment by dimpase created at 2010-11-26 11:19:52

Fullerens are in fact a family, that can be generated.
G.Brinkmann wrote a program called fullgen
http://cs.anu.edu.au/~bdm/plantri/
that does just this, generating all non-isomorphic fullerens with given number of
hexagonal faces. Unfortunately it has a weird license, so it cannot be just hooked up to Sage, at least not in a standard package.


---

Comment by ncohen created at 2010-11-26 11:22:12

I have been sighing at plantri for a while.... I *need* to generate random planar graphs `:-p`

Nathann


---

Comment by dimpase created at 2010-11-26 12:23:55

Replying to [comment:15 ncohen]:
> I have been sighing at plantri for a while.... I *need* to generate random planar graphs `:-p`
> 

Sage way: throw random points on the sphere, generate the facets of their convex closuse (using e.g. cdd), then take the skeleton of the polytope (again, using cdd).
Slow, but trivial to code :-)


---

Comment by rlm created at 2010-11-26 17:20:32

Replying to [comment:7 dimpase]:
> IMHO there is a more fundamental issue here: Sage should handle such graphs in an efficient way --- just keeping all the edges is pretty much a waste, in particular for bigger examples with hundreds of vertices...

The underlying architecture is already in place; one needs only to implement a GraphBackend which represents the graph in question. Implementing simple methods such as has_edge, has_vertex, etc. one can then get the rest of the methods automatically. Check out the source!


---

Comment by dimpase created at 2010-11-26 17:53:57

Replying to [comment:17 rlm]:
> Replying to [comment:7 dimpase]:
> > IMHO there is a more fundamental issue here: Sage should handle such graphs in an efficient way --- just keeping all the edges is pretty much a waste, in particular for bigger examples with hundreds of vertices...
> 
> The underlying architecture is already in place; one needs only to implement a GraphBackend which represents the graph in question. Implementing simple methods such as has_edge, has_vertex, etc. one can then get the rest of the methods automatically. Check out the source!

I am not sure I understand how to implement things like add_vertex() and add_edge() - as we would start with a permutation group G, the set of vertices is the domain of the group, and edges cannot be added one by one, but only as whole G-orbits.
(Alternatively, not all orbits of G are used as the vertex set, and then adding a vertex would mean adding its G-orbit.)


---

Comment by rlm created at 2010-11-26 23:36:36

Replying to [comment:18 dimpase]:
> I am not sure I understand how to implement things like add_vertex() and add_edge() - as we would start with a permutation group G, the set of vertices is the domain of the group, and edges cannot be added one by one, but only as whole G-orbits.
> (Alternatively, not all orbits of G are used as the vertex set, and then adding a vertex would mean adding its G-orbit.)

Well, you can always raise an error in the add_vertex function:

RuntimeError: You can't add vertices to this kind of graph.

Or something similar. Then whenever you called a function which tried to add a vertex you would get that error, but the rest of the graph library would work just fine.


---

Comment by wdj created at 2012-03-15 23:57:05

The following at 3-regular Hamiltonian graphs, hence covered by the LCF construction
(http://en.wikipedia.org/wiki/LCF_notation):


```
Balaban 10-cage
L = [-9, -25, -19, 29, 13, 35, -13, -29, 19, 25, 9, -29, 29, 17, 33, 21, 9,-13, -31, -9, 25, 17, 9, -31, 27, -9, 17, -19, -29, 27, -17, -9, -29, 33, -25,25, -21, 17, -17, 29, 35, -29, 17, -17, 21, -25, 25, -33, 29, 9, 17, -27, 29, 19, -17, 9, -27, 31, -9, -17, -25, 9, 31, 13, -9, -21, -33, -17, -29, 29]
G = graphs.LCFGraph(70, L, 1)

Balaban 11-cage
L = [44, 26, -47, -15, 35, -39, 11, -27, 38, -37, 43, 14, 28, 51, -29, -16, 41, -11, -26, 15, 22, -51, -35, 36, 52, -14, -33, -26, -46, 52, 26, 16, 43, 33, -15, 17, -53, 23, -42, -35, -28, 30, -22, 45, -44, 16, -38, -16, 50, -55, 20, 28, -17, -43, 47, 34, -26, -41, 11, -36, -23, -16, 41, 17, -51, 26, -33, 47, 17, -11, -20, -30, 21, 29, 36, -43, -52, 10, 39, -28, -17, -52, 51, 26, 37, -17, 10, -10, -45, -34, 17, -26, 27, -21, 46, 53, -10, 29, -50, 35, 15, -47, -29, -41, 26, 33, 55, -17, 42, -26, -36, 16]
G = graphs.LCFGraph(112, L, 1)


Bidiakis cube 
G = graphs.LCFGraph(12, [6,4,-4], 4) 

Biggs-Smith graph
L = [16, 24, -38, 17, 34, 48, -19, 41, -35, 47, -20, 34, -36, 21, 14, 48, -16, -36, -43, 28, -17, 21, 29, -43, 46, -24, 28, -38, -14, -50, -45, 21, 8, 27, -21, 20, -37, 39, -34, -44, -8, 38, -21, 25, 15, -34, 18, -28, -41, 36, 8, -29, -21, -48, -28, -20, -47, 14, -8, -15, -27, 38, 24, -48, -18, 25, 38, 31, -25, 24, -46, -14, 28, 11, 21, 35, -39, 43, 36, -38, 14, 50, 43, 36, -11, -36, -24, 45, 8, 19, -25, 38, 20, -24, -14, -21, -8, 44, -31, -38, -28, 37]
G = graphs.LCFGraph(102, L, 1)


Dyck graph
G = graphs.LCFGraph(32, [5,-5,13,-13], 8) 


Foster graph
G = graphs.LCFGraph(90, [17,-9,37,-37,9,-17], 15)  

Franklin graph
G = graphs.LCFGraph(12, [5,-5], 6) 


Gray graph
G = graphs.LCFGraph(54, [-25,7,-7,13,-13,25], 9)

Harries graph
G = graphs.LCFGraph(70, [-29,-19,-13,13,21,-27,27,33,-13,13,19,-21,-33,29], 5)

Harries-Wong graph
L = [9, 25, 31, -17, 17, 33, 9, -29, -15, -9, 9, 25, -25, 29, 17, -9, 9, -27, 35, -9, 9, -17, 21, 27, -29, -9, -25, 13, 19, -9, -33, -17, 19, -31, 27, 11, -25, 29, -33, 13, -13, 21, -29, -21, 25, 9, -11, -19, 29, 9, -27, -19, -13, -35, -9, 9, 17, 25, -9, 9, 27, -27, -21, 15, -9, 29, -29, 33, -9, -25]
G = graphs.LCFGraph(70, L, 1)


Ljubljana graph
L = [47, -23, -31, 39, 25, -21, -31, -41, 25, 15, 29, -41, -19, 15, -49, 33, 39, -35, -21, 17, -33, 49, 41, 31, -15, -29, 41, 31, -15, -25, 21, 31, -51, -25, 23, 9, -17, 51, 35, -29, 21, -51, -39, 33, -9, -51, 51, -47, -33, 19, 51, -21, 29, 21, -31, -39] 
G = graphs.LCFGraph(112, L, 2)

McGee graph
G = graphs.LCFGraph(24, [12,7,-7], 8) 

Möbius–Kantor graph
G = graphs.LCFGraph(16, [5,-5], 8) 


Nauru graph
G = graphs.LCFGraph(24, [5,-9,7,-7,9,-5], 4)

Tutte 12-cage
G = graphs.LCFGraph(126, [17, 27, -13, -59, -35, 35, -11, 13, -53, 53, -27, 21, 57, 11, -21, -57, 59, -17], 7)

Tutte–Coxeter graph
G = graphs.LCFGraph(30, [-13,-9,7,-7,9,13], 5) 

Wagner graph
G = graphs.LCFGraph(8, [4], 8)
```


Some of the Fullerene graphs can be expressed in LCF notation as well.


---

Comment by kini created at 2012-03-16 00:00:46

It's nice to have them explicitly constructed so you get a nice picture in a plot, though. I have a really old patch lying around for the Balaban 11-cage, I'll see if I can rebase it...


---

Comment by ncohen created at 2012-05-20 14:11:33

Well David, all of your graphs are now Sage patches or are included already. My only regret is that I found not nice embedding for Tutte's 12 cage `:-/`

Nathann


---

Comment by nvcleemp created at 2013-05-18 12:43:15

Replying to [comment:14 dimpase]:
> Fullerens are in fact a family, that can be generated.
> G.Brinkmann wrote a program called fullgen
> http://cs.anu.edu.au/~bdm/plantri/
> that does just this, generating all non-isomorphic fullerens with given number of
> hexagonal faces. Unfortunately it has a weird license, so it cannot be just hooked up to Sage, at least not in a standard package.

Brinkmann's student J. Goedgebeur implemented a new version using a different algorithm which is faster for the `small' cases: http://caagt.ugent.be/buckygen/ This program is available under the GPL, so I assume it can be integrated in Sage. I'm willing to work on this. I have some familiarity with the program, since I integrated it into CaGe (http://caagt.ugent.be/CaGe).


---

Comment by ncohen created at 2013-05-18 12:47:38

> Brinkmann's student J. Goedgebeur implemented a new version using a different algorithm which is faster for the `small' cases: http://caagt.ugent.be/buckygen/ This program is available under the GPL, so I assume it can be integrated in Sage. I'm willing to work on this. I have some familiarity with the program, since I integrated it into CaGe (http://caagt.ugent.be/CaGe).

Wow ! Coooooooooool ! When you will create this ticket, could you please add in Cc : "azi, Slani, Stefan, ncohen" ? `:-)`

THaaaaaaaaaaanks !!

Nathann


---

Comment by chapoton created at 2014-01-09 19:36:35

Maybe we can close that one ?


---

Comment by ncohen created at 2014-01-09 21:05:28

Changing status from new to needs_review.


---

Comment by ncohen created at 2014-01-09 21:05:28

I think that we can !

Funny.. It seemed unreachable when Minh created it... `;-)`

Nathann


---

Comment by ncohen created at 2014-01-09 21:05:54

Everything has been implemented.


---

Comment by ncohen created at 2014-01-09 21:05:54

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-01-10 08:47:44

Resolution: fixed
