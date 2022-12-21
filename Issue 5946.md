# Issue 5946: bug in content for p-adic polynomials

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2009-04-30 06:44:15

Assignee: roed

Keywords: content p-adic polynomial

We ran into this at #5921.  There are two separate issues: polynomials with coefficients in a p-adic field should not have a `content()` method, since it doesn't make sense (the same way that having a `content()` method for polynomials with rational coefficients doesn't make sense).

The second issue is with the `content()` method for polynomials with coefficients in p-adic rings.  Here's an example:


```
sage: P.<x> = ZZ[]
sage: f = x + 2
sage: f.content()
1
sage: fp = f.change_ring(pAdicRing(2, 10))
sage: fp
(1 + O(2^10))*x + (2 + O(2^11))
sage: fp.content()
0
```




---

Comment by AlexGhitza created at 2009-04-30 07:29:40

Looks good and passes doctests.


---

Comment by roed created at 2009-04-30 08:14:31

Fixed


---

Attachment

Merged in Sage 3.4.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 08:52:22

Resolution: fixed
