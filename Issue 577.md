# Issue 577: add MPolynomialRing.long_repr method

Issue created by migration from https://trac.sagemath.org/ticket/577

Original creator: malb

Original creation time: 2007-09-03 15:03:36

Assignee: somebody

If a multivariate polynomial ring is structured via a block or product ordering and has lots and lots of variables printing it normally looks messy quickly. The proposed patch (attached) adds a method long_repr with provides a more structured view for those rings, e.g.


```
Polynomial Ring
  Base Ring : Finite Field in a of size 2^4
       Size : 52 Variables
   Block  0 : Ordering : degrevlex
              Names    : k300, k301, k302, k303, x300, x301, x302, x303, w300, w301, w302, w303, s200, s201, s202, s203
   Block  1 : Ordering : degrevlex
              Names    : k200, k201, k202, k203, x200, x201, x202, x203, w200, w201, w202, w203, s100, s101, s102, s103
   Block  2 : Ordering : degrevlex
              Names    : k100, k101, k102, k103, x100, x101, x102, x103, w100, w101, w102, w103, s000, s001, s002, s003
   Block  3 : Ordering : degrevlex
              Names    : k000, k001, k002, k003
```



---

Attachment


---

Comment by malb created at 2007-09-15 13:15:24

Let's see if I can sneak this in 2.8.4.3


---

Comment by was created at 2007-09-21 02:09:04

Resolution: fixed
