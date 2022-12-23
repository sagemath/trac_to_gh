# Issue 2418: pari polroots gives division by zero sometimes

Issue created by migration from https://trac.sagemath.org/ticket/2418

Original creator: cwitty

Original creation time: 2008-03-07 05:01:20

Assignee: was

I think the problem may be in how Sage calls polroots; in particular, I'm suspicious of the coercion from CC to pari.

```
sage: x = polygen(QQ)
sage: p = (x^50/2^100 + x^10 + x + 1).change_ring(ComplexField(106))
sage: len(p.roots())
50
sage: (p/2^100).roots()
---------------------------------------------------------------------------
<class 'sage.libs.pari.gen.PariError'>    Traceback (most recent call last)

/home/cwitty/my-sage/<ipython console> in <module>()

/home/cwitty/my-sage/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.roots()

/home/cwitty/my-sage/gen.pyx in sage.libs.pari.gen._pari_trap()

<class 'sage.libs.pari.gen.PariError'>: division by zero (46)
```



---

Comment by craigcitro created at 2009-01-23 13:09:02

Actually, this is really just pari giving us an error: 


```
? fp
%4 = (6.223015277861140000000000000 E-61 + 0.E-38*I)*x^50 + (0.E-38 + 0.E-38*I)*x^49 + (0.E-38 + 0.E-38*I)*x^48 + (0.E-38 + 0.E-38*I)*x^47 + (0.E-38 + 0.E-38*I)*x^46 + (0.E-38 + 0.E-38*I)*x^45 + (0.E-38 + 0.E-38*I)*x^44 + (0.E-38 + 0.E-38*I)*x^43 + (0.E-38 + 0.E-38*I)*x^42 + (0.E-38 + 0.E-38*I)*x^41 + (0.E-38 + 0.E-38*I)*x^40 + (0.E-38 + 0.E-38*I)*x^39 + (0.E-38 + 0.E-38*I)*x^38 + (0.E-38 + 0.E-38*I)*x^37 + (0.E-38 + 0.E-38*I)*x^36 + (0.E-38 + 0.E-38*I)*x^35 + (0.E-38 + 0.E-38*I)*x^34 + (0.E-38 + 0.E-38*I)*x^33 + (0.E-38 + 0.E-38*I)*x^32 + (0.E-38 + 0.E-38*I)*x^31 + (0.E-38 + 0.E-38*I)*x^30 + (0.E-38 + 0.E-38*I)*x^29 + (0.E-38 + 0.E-38*I)*x^28 + (0.E-38 + 0.E-38*I)*x^27 + (0.E-38 + 0.E-38*I)*x^26 + (0.E-38 + 0.E-38*I)*x^25 + (0.E-38 + 0.E-38*I)*x^24 + (0.E-38 + 0.E-38*I)*x^23 + (0.E-38 + 0.E-38*I)*x^22 + (0.E-38 + 0.E-38*I)*x^21 + (0.E-38 + 0.E-38*I)*x^20 + (0.E-38 + 0.E-38*I)*x^19 + (0.E-38 + 0.E-38*I)*x^18 + (0.E-38 + 0.E-38*I)*x^17 + (0.E-38 + 0.E-38*I)*x^16 + (0.E-38 + 0.E-38*I)*x^15 + (0.E-38 + 0.E-38*I)*x^14 + (0.E-38 + 0.E-38*I)*x^13 + (0.E-38 + 0.E-38*I)*x^12 + (0.E-38 + 0.E-38*I)*x^11 + (7.888609052210120000000000000 E-31 + 0.E-38*I)*x^10 + (0.E-38 + 0.E-38*I)*x^9 + (0.E-38 + 0.E-38*I)*x^8 + (0.E-38 + 0.E-38*I)*x^7 + (0.E-38 + 0.E-38*I)*x^6 + (0.E-38 + 0.E-38*I)*x^5 + (0.E-38 + 0.E-38*I)*x^4 + (0.E-38 + 0.E-38*I)*x^3 + (0.E-38 + 0.E-38*I)*x^2 + (7.888609052210120000000000000 E-31 + 0.E-38*I)*x + (7.888609052210120000000000000 E-31 + 0.E-38*I)
? polroots(fp)
  *** polroots: division by zero
```


I think that makes this ticket invalid ... Carl, does that seem reasonable to you? In particular, do you have any code you've written that we might fall back on if Pari fails like this?


---

Comment by cwitty created at 2009-01-23 20:59:10

I certainly don't think the ticket is invalid; it's definitely a bug in Sage (via Pari), even if it's not a bug in the Sage library code.

For this example, it presumably works to divide through by the leading coefficient (to get a monic polynomial) before handing off to Pari.  Maybe that's a reasonable strategy in general?

Or, we could just report it as a bug to Pari upstream, and hope they fix it.


---

Comment by AlexGhitza created at 2010-01-03 06:47:52

I've followed Carl's suggestion -- see the attached patch.


---

Comment by AlexGhitza created at 2010-01-03 06:47:52

Changing status from new to needs_review.


---

Attachment


---

Comment by cremona created at 2010-01-06 16:37:13

Positive review.  The patch applies to 4.3 and all tests in rings/polynomial pass.


---

Comment by cremona created at 2010-01-06 16:37:13

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-13 10:50:23

Changing status from positive_review to needs_work.


---

Comment by rlm created at 2010-01-13 10:50:23


```
patching file sage/rings/polynomial/polynomial_element.pyx
Hunk #1 FAILED at 4281
1 out of 2 hunks FAILED -- saving rejects to file sage/rings/polynomial/polynomial_element.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_2418.patch
```



---

Comment by AlexGhitza created at 2010-01-13 11:23:00

Robert,

The merging failure is due to the fact that this patch touches the same code as #6237, which just got merged (thank you!).  It is a trivial rebase job, and I am attaching the rebased version.  I kept the old version around so you can see that no other changes were made.

I'm not sure what the protocol is here.  I'd normally go from needs_work to needs_review, but this doesn't really need review...


---

Comment by AlexGhitza created at 2010-01-13 11:23:00

Changing status from needs_work to needs_review.


---

Comment by AlexGhitza created at 2010-01-13 11:23:45

rebased on 4.3.1.alpha1 and #6237, apply instead of the previous patch


---

Attachment

I checked that this applies fine on top of 4.3.1.alpha1 + #6237, and tests pass, so positive review.


---

Comment by cremona created at 2010-01-13 11:47:31

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-14 08:00:30

Resolution: fixed
