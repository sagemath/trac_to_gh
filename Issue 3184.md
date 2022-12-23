# Issue 3184: broken p-adic getslice

Issue created by migration from https://trac.sagemath.org/ticket/3184

Original creator: dmharvey

Original creation time: 2008-05-13 13:00:20

Assignee: somebody

CC:  craigcitro

(This ticket was split off from #2943)

This is okay:


```
sage: K = Qp(13,7)
sage: R.<t> = K[]       
sage: a = 13^7*t^3 + K(169,4)*t - 13^4
sage: a[1:2]
(13^2 + O(13^4))*t
```


This dies:


```
sage: t[0:1]
[boom]
```


The original context for this bug was along the lines of (see #2943 for more examples):


```
sage: K = Qp(p,10)
sage: C.<t> = LaurentSeriesRing(K)
sage: D.<s> = PolynomialRing(C)
sage: z = (1 + O(t)) + t*s^2
sage: z * z
[boom]
```




---

Comment by mabshoff created at 2008-11-23 10:15:37

Craig has become a getslice expert, so let's CC him :)

Cheers,

Michael


---

Attachment


---

Comment by jason created at 2009-02-04 15:17:25

First comment: getslice is deprecated; it should be __getitem__ now.

Second, there is a standard block of code for slicing...using that will make sure that things are consistent for people that understand python slices.


---

Comment by dmharvey created at 2009-03-19 01:20:20

Looks good to me.


---

Comment by mabshoff created at 2009-03-20 20:34:56

Merged in Sage 3.4.1.alpha0.

Cheeers,

Michael


---

Comment by mabshoff created at 2009-03-20 20:34:56

Resolution: fixed
