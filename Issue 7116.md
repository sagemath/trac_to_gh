# Issue 7116: Potential bug in elliptic curve pairing code.

Issue created by migration from https://trac.sagemath.org/ticket/7116

Original creator: was

Original creation time: 2009-10-04 18:34:44

Assignee: davidloeffler


```
I think there is a problem in the function

 ell_point._line_

which is used in _miller_. I don't know if it will necessarily lead to
incorrect results, since it's a degenerate case...

The method has form

 G._line_(R, Q)

and returns the evaluation of Q at the line through G and R.

The problem occurs when Q is the point at infinity. In this case, I'm
pretty sure (it's been a while since I've thought about this kind of
thing) that _line_ should return 0 if the line through G and R is
vertical, and otherwise it should be undefined. The method is
returning an answer that assumes that Q is affine.

While I don't have the most recent version (for reasons I won't bore
you with) I've checked the latest code on line, and it appears to not
have changed from what I have.

I've attached a sample session.

---

----------------------------------------------------------------------
----------------------------------------------------------------------
sage: E = EllipticCurve([GF(17)(-1),GF(17)(0)])
sage: G = E.random_point(); G
(7 : 8 : 1)
sage: minus_G = -G; minus_G
(7 : 9 : 1)
sage: G._line_(minus_G, E(0)) # should return 0
10
sage: two_G = 2*G; two_G
(1 : 0 : 1)
sage: G._line_(two_G, E(0)) # should be undefined/error
11
sage:
```



---

Comment by cremona created at 2009-10-04 20:10:19

The  function P._line(R,Q), as documented,  returns the value at Q of a suitably normalized function on the curve representing the straight line through P and R, where P and/or R are allowed to be the point O at infinity but Q is not.

The code as written does not work when Q=O, but this is not documented.  I suggest a fix whereby if Q==O then a ValueError is raised -- this is stricter than the remedy suggested, but I think more consistent since in this and similar cases the functions which are being evaluated are all in the polynomial ring k(x,y) of the curve and so should not be evaluated at O where they have poles.

I'm also sure that in the places where this function is used, the condition Q==O does not arise.

I'll make a patch,

John


---

Comment by cremona created at 2009-10-04 20:24:00

Applies to 3.1.2.rc0


---

Comment by cremona created at 2009-10-04 20:25:51

Changing assignee from davidloeffler to cremona.


---

Attachment

The patch tests for Q=0 in the functions `_line_` and `_miller_` and raise an error if so.  Doctests added.


---

Comment by cremona created at 2009-10-04 20:25:51

Changing keywords from "" to "elliptic curve".


---

Comment by robertwb created at 2009-11-20 05:34:37

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2009-11-20 05:34:37

I think that condition is fine, now that it's properly documented.


---

Comment by mhansen created at 2009-11-22 07:36:08

Resolution: fixed
