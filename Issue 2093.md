# Issue 2093: floats - sage is inconsistant at times

Issue created by migration from https://trac.sagemath.org/ticket/2093

Original creator: moretti

Original creation time: 2008-02-08 01:07:37

Assignee: moretti

This is really confusing to calculus level students:

```
sage: x(x+1)
x + 1
```


There may be no good fix here, but one idea is to override __call__() on SmybolicVariable to raise an exception.


---

Comment by mhansen created at 2008-02-08 01:57:17

We sort of thought about this awhile ago, and it does raise an exception in cases there the thing being called is a constant.


```
sage: (sqrt(2) + 17)(x+2)
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/opt/sage-2.10.1.rc0/devel/sage-main/sage/<ipython console> in <module>()

/opt/sage-2.10.1.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.py in __call__(self, *args, **kwargs)
   3778 
   3779             if len(args) > self.number_of_arguments():
-> 3780                 raise ValueError, "the number of arguments must be less than or equal to %s"%self.number_of_arguments()
   3781             
   3782             new_ops = []

<type 'exceptions.ValueError'>: the number of arguments must be less than or equal to 0
```


There is a fair amount of functionality that would be lost by removing function calls on symbolic  objects.


---

Comment by mhansen created at 2008-02-08 01:57:17

Changing assignee from moretti to mhansen.


---

Comment by mhansen created at 2008-02-08 01:57:17

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-07-14 10:22:28

Should this be closed as not a bug?


---

Comment by burcin created at 2009-04-16 13:57:32

Resolution: fixed


---

Comment by burcin created at 2009-04-16 13:57:32

This was fixed by #5413. This call behavior is deprecated in 3.4.1.
