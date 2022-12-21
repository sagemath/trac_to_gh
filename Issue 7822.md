# Issue 7822: pynac log function cannot handle float arguments <= 0

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2010-01-03 01:10:54

Assignee: burcin

CC:  jason

After changes in #7490 to sage.symbolic.pynac.py_log, symbolic log function cannot handle float arguments <= 0:


```
sage: from sage.functions.log import function_log
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/burcin/.sage/temp/karr/16530/_home_burcin__sage_init_sage_0.py in <module>()

/home/burcin/sage/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/function.so in sage.symbolic.function.GinacFunction.__call__ (sage/symbolic/function.cpp:5305)()

/home/burcin/sage/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/function.so in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:3560)()

/home/burcin/sage/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/pynac.so in sage.symbolic.pynac.py_log (sage/symbolic/pynac.cpp:10778)()

ValueError: math domain error
```


Attached patch fixes the problem.


---

Attachment

make py_log handle float arguments


---

Comment by burcin created at 2010-01-03 01:31:12

Changing status from new to needs_review.


---

Comment by jason created at 2010-01-03 05:06:19

This looks nice, but causes a serious speed regression:

BEFORE:

```
sage: %timeit ln(complex(-1))
10000 loops, best of 3: 29 µs per loop
sage: %timeit log(complex(-1))
10000 loops, best of 3: 43.2 µs per loop
```


AFTER:

```
sage: %timeit ln(complex(-1))
1000 loops, best of 3: 1.47 ms per loop
sage: %timeit log(complex(-1))
100 loops, best of 3: 1.47 ms per loop
```


Can this be fixed easily?


---

Comment by jason created at 2010-01-03 05:06:19

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2010-01-13 13:24:43

Also, there are an awful lot of "ln"s when I thought we were trying to get away from those and using "log"s.  It makes sense to keep some, but maybe some should be changed to log to show preferred usage?


---

Attachment

second try, faster this time


---

Comment by burcin created at 2010-01-17 01:25:32

Changing status from needs_work to needs_review.


---

Comment by burcin created at 2010-01-17 01:25:32

attachment:trac_7822-py_log.take2.patch fixes the speed problems, although it is still not as fast as before. It depends on a very small patch to pynac. I will post a pynac package with the fix later this week.

Before:


```
sage: %timeit t = ln(float(-1))
1000 loops, best of 3: 285 µs per loop
sage: %timeit t = ln(float(1))
100000 loops, best of 3: 17.5 µs per loop
sage: %timeit t = ln(complex(1))
100000 loops, best of 3: 6.25 µs per loop
sage: %timeit t = ln(complex(1,1))
100000 loops, best of 3: 6.4 µs per loop
sage: %timeit t = ln(complex(1,-1))
100000 loops, best of 3: 6.42 µs per loop
sage: %timeit t = ln(complex(0))
100000 loops, best of 3: 9.24 µs per loop
sage: %timeit t = ln(complex(-1))
100000 loops, best of 3: 6.21 µs per loop
```


After:


```
sage: %timeit t = ln(float(-1))
100000 loops, best of 3: 15.2 µs per loop
sage: %timeit t = ln(float(1))
100000 loops, best of 3: 13.2 µs per loop
sage: %timeit t = ln(complex(1))
100000 loops, best of 3: 15 µs per loop
sage: %timeit t = ln(complex(1,1))
100000 loops, best of 3: 15.3 µs per loop
sage: %timeit t = ln(complex(0))
100000 loops, best of 3: 15.5 µs per loop
sage: %timeit t = ln(complex(-1))
100000 loops, best of 3: 15.1 µs per loop
```


Re comment:3:

The top level log function is a regular python function which handles precision, etc. Calling that in the doctest is not really testing the `Function_log` defined in `sage/functions/log.py`. If we want people to move away from using `ln`, we should deprecate it. Since the last discussion about this topic ended up by concluding we should even support printing `ln` instead of `log`, I don't see that happening soon.


---

Comment by burcin created at 2010-01-19 23:31:33

New pynac package available here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg

A lot of other patches on trac depend on this one. I'd really appreciate a quick review. :)

Apply only attachment:trac_7822-py_log.take2.patch


---

Comment by kcrisman created at 2010-01-28 21:05:47

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-01-28 21:05:47

All works okay, and after careful checking the patch seems correct, modulo my weak understanding of Cython.  I'll go ahead and put positive review, but someone please stop me if the whole PY_TYPE_CHECK stuff is not right.

To Burcin: In general, it would be very helpful if you could put a specific link to the changeset in Pynac (in the online hg server) which corresponds to each fix of a Sage issue.


---

Comment by mvngu created at 2010-02-18 21:38:13

Resolution: fixed


---

Comment by mvngu created at 2010-02-18 21:38:13

Merged [trac_7822-py_log.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7822/trac_7822-py_log.take2.patch).
