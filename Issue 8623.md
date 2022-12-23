# Issue 8623: User interface to lcalc library

Issue created by migration from https://trac.sagemath.org/ticket/8623

Original creator: rishi

Original creation time: 2010-03-29 12:54:49

Assignee: was

CC:  bober cremona craigcitro was robertwb ylchapuy

I am attaching a patch which gives a user interface to lcalc library wrapper. Please give me feedback. Right now only Elliptic Curve L functions are implemented.


---

Comment by rishi created at 2010-03-29 13:05:21

This is an example of user interface for lcalc library. This interface does not assume that the center is half.  This is not finished, but I would like some feedback on the design decisions.

Below is how to use it

```
sage: E=EllipticCurve([1,-1,1,-1,-14])
sage: L=E.lfunction()
sage: L
L Function of  Elliptic Curve defined by y^2 + x*y + y = x^3 - x^2 - x - 14 over Rational Field
sage: L.value(1)
0.386769938387780
sage: L(1)
0.386769938387780
sage: L.find_zeros_and_verify(4)
[4.74199315541376, 7.81910395523807, 8.69568671187028, 10.7173409988911]
sage: L.hardy_z_function(1+2*I)
1.26747446769888 + 1.11832648738039e-16*I
sage: L.hardy_z_function(1+3*I)
1.92712584463710 + 8.78500291880843e-16*I
sage: L.hardy_z_function(1+4*I)
1.53230410077723 + 1.82991418837085e-15*I
sage: L.center()
1
sage: L.analytic_rank()
0
```



---

Attachment


---

Comment by chapoton created at 2014-03-06 10:51:31

Changing keywords from "" to "lcalc".
