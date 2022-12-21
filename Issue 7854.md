# Issue 7854: speed up edge_connectivity in easy cases

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-01-06 12:27:35

Assignee: rlm

This functions uses LP and has a big overhead because of that... Is many cases, though, the graph is not connected, or not 2-connected.

To test if a graph is connected, we already have the function is_connected which does the job very efficiently through depth-first-searches.

We also have a function is_strongly_connected for DiGraphs.

To test if a Graph is 2-connected, we can first :
*  compute a strongly_connected_orientation with a linear-time function
*  check whether the returned graph is strongly-connected ( linear time too )

Without this, much time is spent over building a useless Linear Program.

Nathann




---

Comment by ncohen created at 2010-01-16 16:59:51

Small modifications, good results :
Before :

```
sage: %timeit graphs.WorldMap().edge_connectivity()
10 loops, best of 3: 200 ms per loop
```


After :

```
sage: %timeit graphs.WorldMap().edge_connectivity()
100 loops, best of 3: 4.75 ms per loop
```



---

Comment by ncohen created at 2010-01-16 16:59:51

Changing status from new to needs_review.


---

Comment by zimmerma created at 2010-02-25 22:23:58

Changing status from needs_review to needs_info.


---

Comment by zimmerma created at 2010-02-25 22:23:58

Nathann, I tried before the patch but got:

```
sage: %timeit graphs.WorldMap().edge_connectivity()
...
ValueError: There does not seem to be any Linear Program solver installed. Please visit http://www.sagemath.org/packages/optional/ to install CBC or GLPK.
```

Which LP package did you use? CBC or GLPK? Did you check you got a speedup with both?


---

Comment by ncohen created at 2010-02-26 06:57:31

Hello !!!!

Actually, the patch works with any LP solver which is installed.
What you get is is a totally unrelated "bug". After installing the package corresponding to a LP solver, the user has to run "sage -b" but has no way to know about it for the moment. There is an update of GLPK waiting for review (#8298) and Cbc will follow (#8171). Sorry for the trouble !

This patch just avoids the use of LP when it is possible -- when the graph isn't connected, or not 2-connected. The functions used are written in Cython, which makes them almost instantaneous to use. Actually, checking the connectivity for low values this way is even faster than just generating the linear program, so it definitely is good to have :-)

Nathann


---

Comment by ncohen created at 2010-02-26 06:57:31

Changing status from needs_info to needs_review.


---

Comment by zimmerma created at 2010-02-26 08:58:51

Changing status from needs_review to needs_work.


---

Comment by zimmerma created at 2010-02-26 08:58:51

thanks Nathann for your answer.
I successfully installed the cbc package from http://www.sagemath.org/packages/optional/ in 4.3.3
(btw, there are several compiler warnings during compilation, on a 64-bit Core 2 Duo).
*Before* applying your patch, I get:

```
sage: g = 2 * graphs.PetersenGraph() 
sage: g.edge_connectivity() 
0.0
sage: g = graphs.PathGraph(10) 
sage: g.edge_connectivity() 
1.0
sage: g = digraphs.ButterflyGraph(3) 
sage: g.edge_connectivity() 
0.0
sage: g = 2 * graphs.PetersenGraph() 
sage: g.vertex_connectivity() 
0.0
sage: g = graphs.PathGraph(10) 
sage:  g.vertex_connectivity() 
1.0
sage: g = digraphs.ButterflyGraph(3) 
sage: g.vertex_connectivity() 
0.0
```

thus it seems to me some work is needed, because according to the patch documentation, after
applying the patch I will get integer values instead of floating-point numbers, which may break
some code using those functions.

Paul


---

Comment by ncohen created at 2010-02-26 10:27:01

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-02-26 10:27:01

Hello !! 

It was even worse than this... The patch made Sage check manually if the graph was 1- or 2-connected, even if the user requested the weights on the edges to be taken into account, which would clearly have returned wrong results at some point, as the speedup only considered the graph's topology. It now checks this option is set to False. I also set it to False by default, so that the user will be able to enjoy these speed-ups. Anyway, I think it is best not to use the edges'  weights by default. I very frequently deal with graph having tuples as labels to remember a lot of informations, and this function wouldn't like it at all :-)

(several minutes later)

Ahem... And I also noticed a bug that had me worried for a while. When testing docstrings, I found that the PappusGraph was only 1-connected instead of 3-connected, and the LP seemed to be in fault. In the end, I just noticed I had called "g" the strongly connected orientation, which was the main graph's name !!!!!

Better this way... ;-)

Thank you for your help !

Nathann


---

Attachment


---

Comment by zimmerma created at 2010-02-27 22:23:11

Now the patch gives floating-point values as before.
However I wonder why those values are floating-point numbers and not integers, since for example
the connectivity is an integer according to the reference wikipedia page.

(This might be solved in a further ticket, thus I give a positive review for the present one.)


---

Comment by zimmerma created at 2010-02-27 22:23:11

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-02-28 01:06:14

The reason is that this function handles weighted edges, and those edges may be weighted with floating-point values :-)

I am myself only interested by "topological" connectivity, in which all edges are weighted with 1, but I do not really mind as long as connectivity() == k works... 

Thank you very much for your help !!!

Nathann


---

Comment by mvngu created at 2010-03-03 14:18:55

Resolution: fixed
