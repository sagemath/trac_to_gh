# Issue 7740: Spped up MixedIntegerLinearProgram

Issue created by migration from https://trac.sagemath.org/ticket/7740

Original creator: ncohen

Original creation time: 2009-12-19 08:43:58

Assignee: jkantor

CC:  rlm

From Robert Miller :


```
sage: from sage.graphs.graph_coloring import vertex_coloring
sage: g = graphs.CirculantGraph(120, [2,3,5,7])
sage: vertex_coloring(g)
```


It takes longer to set up the constraint than to solve the problem, on my laptop. 


---

Comment by ncohen created at 2009-12-20 17:33:35

Well, this time is spent as expected on the add_constraint function, which may spend time over considerations coming from symbolic computations, though I did not achieve to know where... When I am profiling your example I see :

```

25448/21366    0.529    0.000    0.695    0.000 complex_interval_field.py:257(__call__)
     8642    0.427    0.000    1.136    0.000 complex_interval_field.py:330(random_element)
     8642    0.106    0.000    0.117    0.000 complex_interval_field.py:325(gen)
```


These functions are the ones responsible for the time spent defining the LP, but I could not find which line of add_constraint is calling them... If you have any idea, please tell me and I'll give it a look :-)


---

Comment by ncohen created at 2009-12-20 17:33:35

Changing status from new to needs_info.


---

Comment by ncohen created at 2009-12-26 12:21:17

Changing status from needs_info to needs_review.


---

Comment by ncohen created at 2009-12-26 12:21:17

This patch adds to the file numerical.mip a class LinearFunction which avoid using the much more general symbolic expressions from Sage ( as we only need to define linear functions ). 

Before :


```
sage: from sage.graphs.graph_coloring import vertex_coloring
sage: g = graphs.CirculantGraph(120, [2,3,5,7])
sage: timeit("vertex_coloring(g)")
5 loops, best of 3: 3.94 s per loop
```


After :


```
sage: from sage.graphs.graph_coloring import vertex_coloring
sage: g = graphs.CirculantGraph(120, [2,3,5,7])
sage: timeit("vertex_coloring(g)")
5 loops, best of 3: 2.18 s per loop
```


The next way to speed up this class would be, methinks, to cythonize it. I tried it this time but got stuck by the fact that the solving functions ( solveCoin, solveGlpk ) are not directly included in Sage and installed by the packages... The best way would really be to move these sources into Sage. It would also solve solve the problem of having to update both packages and numerical.mip t the same time .. :-/

Nathann


---

Comment by ncohen created at 2009-12-28 08:45:38

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2009-12-28 11:49:52

Before :

```
sage: g = graphs.WorldMap()
sage: %timeit g.edge_connectivity()
10 loops, best of 3: 1.29 s per loop
```


After :

```
sage: g = graphs.WorldMap()
sage: %timeit g.edge_connectivity()
10 loops, best of 3: 231 ms per loop
```


But as mentionned earlier, we will have to find other ways to improve this class ! :-)

Nathann


---

Comment by ncohen created at 2009-12-28 11:49:52

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-01-06 16:17:01

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2010-01-06 16:17:01

Looks good to me! Aside from this typo:
"An elementary algebra algebra"


---

Attachment


---

Comment by ncohen created at 2010-01-09 08:16:44

Here it is ! :-)


---

Comment by ncohen created at 2010-01-09 08:16:44

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-01-13 11:39:54

Resolution: fixed


---

Comment by rlm created at 2010-01-13 11:39:54

positive review


---

Comment by ncohen created at 2010-01-13 11:41:03

Thank you again !!! I was longing for this one :-)

Nathann


---

Comment by nthiery created at 2010-01-14 14:38:10

Hi Nathan,

Sorry to pop up late into the discussion. What was the rationale for not using CombinatorialFreeModule(whatever_ring, ZZ)?

For the record, I very much hope that FreeModule(ring, infinity, sparse = True) will be available sometime soon. That will be a faster alternative.


---

Comment by ncohen created at 2010-01-14 14:48:31

Hello !

At first I used InfinitePolynomialRing, then plain "vars", then I just wondered why it was still very slow and just wondered what it would give if I were to write the symbolics myself to understand... As it was easy enough, I wrote something to try it on my computer, and ended up writing a patch to send the code. 

This way, it stores the informations in a format that is optimal for what I need ( no powers --only linear functions--, sparse from the beginning, ... ). Since, I have also noticed that having my own symbolics would let me define expressions like double inequalities :

0 < a + b < 9

Which I had been missing for a long time.. :-)
The main problem I have is that in many cases, the symbolics take most of the time spent on the computation of a matching (or other LP problems), which is quite disturbing ;-)

Nathann
