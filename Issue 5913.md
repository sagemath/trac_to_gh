# Issue 5913: implement graph coloring in sage

Issue created by migration from https://trac.sagemath.org/ticket/5913

Original creator: was

Original creation time: 2009-04-27 18:38:12

Assignee: rlm

CC:  boothby

Sage should have some sort of implementation of code for computing a vertex coloring with n colors of a graph, assuming the chromatic number is at most n. 

Even a stupid initial greedy algorithm implementation would be a lot faster than what we have now, which is _nothing_. 




---

Comment by was created at 2009-04-27 18:38:59

Some offlist emails about this

```
I agree, graph coloring is rather important.  You might want to look at http://www.cs.ualberta.ca/~joe/Coloring/ which has a lot of good links.  As a stop-gap, it's possible to easily transform a graph-coloring problem into a satisfiability problem and hand it to a SAT solver (like minisat).  This works ok for fairly small graphs, but more specialized algorithms seem to work much better when the graphs get at all large.

Victor

Godsil had suggested looking at Joe Culberson's program a while ago,
but as far as I know, nobody has looked into this.

(  http://www.cs.ualberta.ca/~joe/Coloring/Colorsrc/index.html  )

I can bring this up during the Friday session as an alternative
project for someone to try if you want.

Robert L. Miller

It looks like Joe Culberson's programs don't have a clearly defined
license, just something kind of "as is"/no-warranty -ish. Maybe you
should email him and ask him to allow us to distribute it under
GPLv2+...

Another thing to look at is the recent paper of Miroslav Velev (which I've attached).  To implement this it would involve implementing his algorithms (probably in SAGE) for translating the graph coloring problem into SAT input and then passing it to Minisat.  He says that by his encodings he's gotten speedups of 3 orders of magnitude, and is competitive (or better) than the existing coloring programs.
```



---

Comment by was created at 2009-04-27 19:00:34


```
>> from sage.graphs import graph_coloring
>> G = Graph("Fooba")
>> C = graph_coloring.first_coloring(4)
>> G.show(vertex_colors=C)

Why does this have to be obfuscated?   Nobody will ever find this by doing

  G.<tab> 

with a graph.    Is it because you didn't view the code as ready? 

If the code is "ready",  this will make solving #5913 fairly easy -- just add a function to graphs that calls graph_coloring.first_coloring. 

 -- William

```



---

Comment by was created at 2009-04-27 19:25:26

rlm, could you throw in something like

```
G.plot(vertex_colors=c)
```

to your example, since it is very nice to visualize what happens, and it's extra nice to not have to spend 5 minutes digging through the plot docs to remember to use vertex_colors.  Also, you can be clear that the html colors dict answer works with plot, but the partition one doesn't.   It's just 1-2 more lines.


---

Comment by rlm created at 2009-04-27 19:47:53

Done!


---

Comment by was created at 2009-04-28 14:06:04

The coloring doctest will fail, since it involves a dictionary whose order is random:

```
sage -t  devel/sage/sage/graphs/graph.py
**********************************************************************
File "/Users/wstein/build/sage-3.4.1.rc3/devel/sage-main/sage/graphs/graph.py", line 8846:
    sage: H = G.coloring(hex_colors=True); H
Expected:
    {'#0000ff': [4], '#00ff00': [1, 2, 3], '#ff0000': [0, 5, 6]}
Got:
    {'#00ff00': [1, 2, 3], '#ff0000': [0, 5, 6], '#0000ff': [4]}
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_162
***Test Failed*** 1 failures.
```


Nothing else fails, and nothing else is wrong with this patch as far as I can tell.


---

Comment by rlm created at 2009-04-28 14:54:32

Doctest now sorts the keys first.


---

Attachment


---

Comment by was created at 2009-04-28 22:34:09

I just noticed that Discrete Applied Mathematics had a special issue last year:

Volume 156, Issue 2, Pages 145-288 (15 January 2008)
on Computational Methods for Graph Coloring.

It's probably worth looking at.

 -- victor miller


---

Comment by AlexGhitza created at 2009-04-30 09:43:24

I applied this, doctested, and spent some time picking graphs and plotting their colorings.  Looks good!


---

Comment by mabshoff created at 2009-05-12 22:03:57

Resolution: fixed


---

Comment by mabshoff created at 2009-05-12 22:03:57

Merged in Sage 4.0.alpha0.

Cheers,

Michael
