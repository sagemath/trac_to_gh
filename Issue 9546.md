# Issue 9546: bounded outdegree orientation

Issue created by migration from https://trac.sagemath.org/ticket/9546

Original creator: ncohen

Original creation time: 2010-07-19 05:48:54

Assignee: jason, ncohen, rlm

CC:  jthurber

Given a Graph and a value associating an integer b(v) to each vertex v, this method computes an orientation of G such that each vertex has out_degree at most v, if it exists. 

The method is to use a max flow, which is explained in the patch in several lines.

Nathann


---

Comment by ncohen created at 2010-07-19 05:49:37

Changing status from new to needs_review.


---

Comment by rlm created at 2011-01-12 03:58:12


```
----------------------------------------------------------------------

The following tests failed:

        sage -t -long devel/sage-main/sage/graphs/graph.py # 7 doctests failed
----------------------------------------------------------------------
```


These all seem to be:


```
NameError: global name 'floor' is not defined
```



---

Comment by rlm created at 2011-01-12 03:58:12

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2011-01-12 09:23:22

Right O_o

The error comes from the ford_fulkerson algorithm. I replaced "floor(x)" by "x // 1".

I know I wrote this code myself, but when I looked at it I could only think : why on earth is our implementation of flows in Python and not Cython ? O_o

Updated ! Sorry for the trouble !

Nathann


---

Comment by ncohen created at 2011-01-12 09:23:22

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by gbe created at 2011-01-12 23:05:54

Using floor division here might be nice, but I'm concerned about the coercion model:


```
sage: 1215.151//1
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/gbe/sage/dev/devel/sage-main/sage/<ipython console> in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.__floordiv__ (sage/rings/integer.c:11983)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.bin_op (sage/structure/element.c:17928)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.bin_op (sage/structure/element.c:17841)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6213)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6152)()

TypeError: unsupported operand type(s) for //: 'sage.rings.real_mpfr.RealLiteral' and 'sage.rings.real_mpfr.RealNumber'
```


Also, floor division doesn't seem to buy you any speedup:

```
sage: tests = [float(random()*10**randint(0,10)) for i in range(10)]
sage: for i in tests:
....:     timeit('floor(test)')

625 loops, best of 3: 5.14 µs per loop
625 loops, best of 3: 5.12 µs per loop
625 loops, best of 3: 5.21 µs per loop
625 loops, best of 3: 5.12 µs per loop
625 loops, best of 3: 5.12 µs per loop
625 loops, best of 3: 5.1 µs per loop
625 loops, best of 3: 5.07 µs per loop
625 loops, best of 3: 5.2 µs per loop
625 loops, best of 3: 5.11 µs per loop
625 loops, best of 3: 5.13 µs per loop

sage: for i in tests:
....:     timeit('test // 1')

625 loops, best of 3: 9.33 µs per loop
625 loops, best of 3: 9.47 µs per loop
625 loops, best of 3: 9.4 µs per loop
625 loops, best of 3: 9.44 µs per loop
625 loops, best of 3: 9.4 µs per loop
625 loops, best of 3: 9.4 µs per loop
625 loops, best of 3: 9.35 µs per loop
625 loops, best of 3: 9.31 µs per loop
625 loops, best of 3: 9.3 µs per loop
625 loops, best of 3: 9.4 µs per loop
```


All in all I think the better solution is to just bring floor(x) into scope from functions/other.py, as I've done in the attached patch.


---

Attachment


---

Comment by rlm created at 2011-01-14 21:49:51

Changing status from needs_review to positive_review.


---

Attachment

apply all three patches


---

Comment by jdemeyer created at 2011-01-19 22:22:07

Resolution: fixed
