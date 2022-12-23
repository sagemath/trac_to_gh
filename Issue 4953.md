# Issue 4953: sage/misc/randstate.pyx doctest failure on menas

Issue created by migration from https://trac.sagemath.org/ticket/4953

Original creator: mabshoff

Original creation time: 2009-01-07 17:10:21

Assignee: cwitty

The following was introduced by #4934:

```
menas (x86_64-Linux-suse)

**********************************************************************
File "/home/mariah/sage/sage-3.2.3-x86_64-Linux-suse/devel/sage/sage/misc/randstate.pyx",
line 239:
    : with seed(1): (rtest(), rtest())
Expected:
    ((978, 0.184109262667515, -3*x^2 - 1/12, (4,5), [ 0, 1, 1, 0, 0 ],
1046254370, 60359, 0.83350776541997362), (138, -0.247578366457583, 2*x
- 24, (), [ 1, 1,
1, 0, 1 ], 1077419109, 10234, 0.0033332230808060803))
Got:
    ((978, 0.184109262667515, -3*x^2 - 1/12, (2,3)(4,5), [ 0, 1, 1, 0,
0 ], 1046254370, 60359, 0.83350776541997362), (138,
-0.247578366457583, 2*x - 24, (1,3,2)(4,5), [ 1, 1, 1, 0, 1 ],
1077419109, 10234, 0.0033332230808060803))
**********************************************************************
```



---

Comment by mabshoff created at 2009-02-10 05:52:49

I am no longer seeing this with the system compiler in 3.3.alpha6, but will try with gcc 4.3.3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-10 07:39:20

Resolution: fixed


---

Comment by mabshoff created at 2009-02-10 07:39:20

This issue does no longer happen with the system gcc as well as gcc 4.3.3 with Sage 3.3.alpha6:

```
mabshoff@menas:~/build-3.3.alpha6/sage-3.3.alpha6-menas-gcc433> ./sage -t -long devel/sage/sage/misc/randstate.pyx
sage -t -long "devel/sage/sage/misc/randstate.pyx"          
	 [22.2 s]
```


Cheers,

Michael
