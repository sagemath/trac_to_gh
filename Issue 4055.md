# Issue 4055: serious bug in polynomial multiplication

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-09-04 00:06:57

Assignee: tbd

CC:  boothby

Seems to be something with the generic karatsuba, perhaps it should not be used for inexact rings?


```
sage: R.<x> = RR[]
sage: (x-1e16)*(x-1e17)
 1.00000000000000*x^2 + 1.00000000000000e33

sage: R.<x> = RDF['y']['x']
sage: (x-1e123)*(x-1e100)
 1.0*x^2 + 1e+223
```




---

Comment by AlexGhitza created at 2009-01-28 21:52:13

I believe this got fixed by Tom Boothby at Sage Days 12, see #3056.  I'm ccing him so he can react.  In any case, this looks fine now:


```
[ghitza`@`artin ~]$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: R.<x> = RR[]
sage: sage: (x-1e16)*(x-1e17)
1.00000000000000*x^2 - 1.10000000000000e17*x + 1.00000000000000e33
sage: sage: R.<x> = RDF['y']['x']
sage: sage: (x-1e123)*(x-1e100)
1.0*x^2 + (-1e+123)*x + 1e+223
```



---

Comment by mabshoff created at 2009-05-22 02:56:35

Resolution: fixed


---

Comment by mabshoff created at 2009-05-22 02:56:35

Fixed via #3056.

Cheers,

Michael
