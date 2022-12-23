# Issue 5846: small bug in caching the precision for p-adic L-series

Issue created by migration from https://trac.sagemath.org/ticket/5846

Original creator: wuthrich

Original creation time: 2009-04-21 14:27:11

Assignee: was

Keywords: p-adic L-series

When looking up cached values of the p-adic L-series of an elliptic curve, there is a problem with the precision (as a powe-series in T) :


```
sage: E = EllipticCurve('389a')
sage: p = 3
sage: L = E.padic_lseries(p)
sage: L.series(3)
O(3^5) + O(3^2)*T + (2 + 2*3 + O(3^2))*T^2 + (2 + O(3))*T^3 + (1 + 3 + O(3^2))*T^4 + O(T^5)
sage: L.series(3,prec=6)
O(3^5) + O(3^2)*T + (2 + 2*3 + O(3^2))*T^2 + (2 + O(3))*T^3 + (1 + 3 + O(3^2))*T^4 + O(T^5)
```


The attached patch changes the inequality sign in question.


---

Attachment


---

Comment by mabshoff created at 2009-04-21 22:17:20

One slight nitpick: The trac number in the patch is missing.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-21 22:37:54

And this is not going into 3.4.1 since it is basically done, so better luck in 3.4.2 :)

Cheers,

Michael


---

Comment by wuthrich created at 2009-04-22 10:38:18

to apply after the first patch


---

Attachment

I added the forgotten trac number in the doctest.

Chris.


---

Attachment

apply only this one


---

Comment by GeorgSWeber created at 2009-04-28 20:00:05

The first two hunks of the first patch didn't apply to sage-3.4.2.alpha0, but they contained only whitespace beautification. Probably this had already been adressed. I merged the remaining two hunks with the "real" patch and the the second patch. Ready to go.


---

Comment by mabshoff created at 2009-04-29 23:38:44

Merged  trac_5846_combined.patch in Sage 3.4.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-29 23:38:44

Resolution: fixed
