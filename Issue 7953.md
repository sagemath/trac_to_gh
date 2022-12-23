# Issue 7953: Curve printing only shows first defining equation

Issue created by migration from https://trac.sagemath.org/ticket/7953

Original creator: wjp

Original creation time: 2010-01-16 18:10:54

Assignee: AlexGhitza

Reported by Ronald van Luijk:

The `print C` below only prints the first defining equation.


```
sage: # problem printing
sage: A.<x,y,z>=AffineSpace(QQ,3)
sage: C=Curve([x-y,2-z])
sage: print C
Affine Space Curve over Rational Field defined by x - y
sage: print C.defining_ideal()
Ideal (x - y, -z + 2) of Multivariate Polynomial Ring in x, y, z over Rational Field
```



---

Comment by wjp created at 2010-01-16 23:47:27

Changing status from new to needs_review.


---

Attachment


---

Comment by AlexGhitza created at 2010-01-17 22:39:29

Changing status from needs_review to positive_review.


---

Comment by AlexGhitza created at 2010-01-17 22:39:29

Looks good.  Thanks, Willem and Ronald!


---

Comment by wjp created at 2010-01-18 01:36:59

Changing status from positive_review to needs_work.


---

Comment by wjp created at 2010-01-18 01:36:59

After discussing with William (see also #7954), I'll move the non-plane curve code out of the plane_curves directory first, and rebase this patch on top of that afterwards.


---

Comment by novoselt created at 2010-10-23 21:56:15

TABs replaced with spaces


---

Comment by novoselt created at 2010-10-23 21:59:33

Changing status from needs_work to positive_review.


---

Attachment

I'll take the liberty to switch this patch back to positive review, since it does solve the problem described in the ticket (which is bad - Sage gives wrong answers) and there was no work done in a "better direction" for 9 month neither here nor on #7954.

The original patch uses TABs, so I changed them to spaces leaving the rest the same. Applies cleanly and passes all tests on sage-4.6.rc0.


---

Comment by jdemeyer created at 2010-11-01 10:05:20

Resolution: fixed
