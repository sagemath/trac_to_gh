# Issue 110: srange should accept negative step value

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2006-10-04 23:15:38

Assignee: somebody

It should work more like Python's ordinary `range`, not like this:


```
sage: srange(1, 5, -1)
---------------------------------------------------------------------------
exceptions.ValueError                                Traceback (most recent call last)

/home/dmharvey/sage-1.3.7.3.3/<ipython console> 

/home/dmharvey/sage/local/lib/python2.4/site-packages/sage/misc/misc.py in srange(a, b, step, include_endpoint)
    630         
    631     if step <= 0:
--> 632         raise ValueError, "step (=%s) must be positive"%step
    633     num_steps = int(float((b-a)/step)) + 1
    634     v = [a] + [a + k*step for k in range(1,num_steps)]

ValueError: step (=-1) must be positive
```




---

Comment by was created at 2006-10-05 07:44:13

Resolution: fixed


---

Comment by was created at 2006-10-05 07:44:13

I fixed this for sage-1.4
