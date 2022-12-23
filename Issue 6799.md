# Issue 6799: Speed up symbolic comparison

Issue created by migration from https://trac.sagemath.org/ticket/6799

Original creator: gmhossain

Original creation time: 2009-08-21 23:20:16

It takes too long to check whether x is in a list in new symbolics


```
sage: var('x,x1,x2,x3,x4')
(x, x1, x2, x3, x4)
sage: f = function('f')
sage: mylist = [x1,x2,x3,x4,f(x1),f(x2),f(x3),f(x4)]

sage: timeit('x in mylist')
5 loops, best of 3: 461 ms per loop
```


If we need to check it couple of more times
then it becomes worse

```
sage: timeit('x in mylist')
5 loops, best of 3: 1.26 s per loop
sage: timeit('x in mylist')
5 loops, best of 3: 3.4 s per loop
```


For a comparison

```
sage: timeit('x1 in mylist')
625 loops, best of 3: 473 ns per loop
```


Reason for this huge discrepancy stems from the fact that
except for last example, in all previous cases maxima is called
to check the equality. 

See this thread for more:

 http://groups.google.com/group/sage-devel/browse_thread/thread/d2275cb5b3d63317


---

Comment by jdemeyer created at 2013-12-05 08:24:13

The issue of ever-slowing comparisons doesn't occur anymore.


---

Comment by jdemeyer created at 2013-12-05 08:24:13

Resolution: worksforme
