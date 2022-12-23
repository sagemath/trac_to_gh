# Issue 3840: [with patch, needs review] conversion of 0 from MV polynomial rings broken

Issue created by migration from https://trac.sagemath.org/ticket/3840

Original creator: gfurnish

Original creation time: 2008-08-13 17:30:25

Assignee: somebody

The following (and all similar conversions) fail:

```
RR(RR[x,y](0))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/gfurnish/sage-3.1.alpha0-sage.math-only-x86_64-Linux/<ipython console> in <module>()

/home/gfurnish/sage-3.1.alpha0-sage.math-only-x86_64-Linux/real_mpfr.pyx in sage.rings.real_mpfr.RealField.__call__ (sage/rings/real_mpfr.c:3408)()

/home/gfurnish/sage-3.1.alpha0-sage.math-only-x86_64-Linux/multi_polynomial.pyx in sage.rings.polynomial.multi_polynomial.MPolynomial._mpfr_ (sage/rings/polynomial/multi_polynomial.c:1656)()
```

The attached patch provides doctests and fixes.  


---

Attachment

REVIEW:

This should be redone by changing the == to <= like this.  This is much nicer than using an if statement like in the patch.  Redo it. 

```
diff -r 22105a8d4591 sage/rings/polynomial/multi_polynomial.pyx
--- a/sage/rings/polynomial/multi_polynomial.pyx        Wed Aug 13 09:54:40 2008 +0100
+++ b/sage/rings/polynomial/multi_polynomial.pyx        Wed Aug 13 11:02:59 2008 -0700
@@ -15,7 +15,7 @@ cdef class MPolynomial(CommutativeRingEl
     # Some standard conversions
     ####################
     def __int__(self):
-        if self.degree() == 0:
+        if self.degree() <= 0:
             return int(self.constant_coefficient())
         else:
             raise TypeError
```



---

Attachment


---

Comment by ncalexan created at 2008-08-13 18:52:22

Apply only `3840-gfurnish-multivariate-conversion-from-0.patch`; hopefully the credit in hg remains with gfurnish.  Let me know if not; I used the hg export command this time.

I think this patch does what the referee wants and strikes a better doctesting balance.

Whether -1 is correct or -Infinity is correct, this at least makes sage internally more consistent.


---

Comment by was created at 2008-08-13 19:08:58

Positive review for the second patch.  All credit to Gfurnish (except Nick and I get referee credit).


---

Comment by mabshoff created at 2008-08-13 21:05:29

Resolution: fixed


---

Comment by mabshoff created at 2008-08-13 21:05:29

Merged 3840-gfurnish-multivariate-conversion-from-0.patch in Sage 3.1.alpha2
