# Issue 3840: [with patch, needs review] conversion of 0 from MV polynomial rings broken

archive/issues_003840.json:
```json
{
    "body": "Assignee: somebody\n\nThe following (and all similar conversions) fail:\n\n```\nRR(RR[x,y](0))\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/gfurnish/sage-3.1.alpha0-sage.math-only-x86_64-Linux/<ipython console> in <module>()\n\n/home/gfurnish/sage-3.1.alpha0-sage.math-only-x86_64-Linux/real_mpfr.pyx in sage.rings.real_mpfr.RealField.__call__ (sage/rings/real_mpfr.c:3408)()\n\n/home/gfurnish/sage-3.1.alpha0-sage.math-only-x86_64-Linux/multi_polynomial.pyx in sage.rings.polynomial.multi_polynomial.MPolynomial._mpfr_ (sage/rings/polynomial/multi_polynomial.c:1656)()\n```\nThe attached patch provides doctests and fixes.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/3840\n\n",
    "created_at": "2008-08-13T17:30:25Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with patch, needs review] conversion of 0 from MV polynomial rings broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3840",
    "user": "https://github.com/garyfurnish"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/3840





---

archive/issue_comments_027246.json:
```json
{
    "body": "Attachment [trac_3840.patch](tarball://root/attachments/some-uuid/ticket3840/trac_3840.patch) by @williamstein created at 2008-08-13 18:06:21\n\nREVIEW:\n\nThis should be redone by changing the == to <= like this.  This is much nicer than using an if statement like in the patch.  Redo it. \n\n```\ndiff -r 22105a8d4591 sage/rings/polynomial/multi_polynomial.pyx\n--- a/sage/rings/polynomial/multi_polynomial.pyx        Wed Aug 13 09:54:40 2008 +0100\n+++ b/sage/rings/polynomial/multi_polynomial.pyx        Wed Aug 13 11:02:59 2008 -0700\n@@ -15,7 +15,7 @@ cdef class MPolynomial(CommutativeRingEl\n     # Some standard conversions\n     ####################\n     def __int__(self):\n-        if self.degree() == 0:\n+        if self.degree() <= 0:\n             return int(self.constant_coefficient())\n         else:\n             raise TypeError\n```",
    "created_at": "2008-08-13T18:06:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3840#issuecomment-27246",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_3840.patch](tarball://root/attachments/some-uuid/ticket3840/trac_3840.patch) by @williamstein created at 2008-08-13 18:06:21

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

archive/issue_comments_027247.json:
```json
{
    "body": "Attachment [3840-gfurnish-multivariate-conversion-from-0.patch](tarball://root/attachments/some-uuid/ticket3840/3840-gfurnish-multivariate-conversion-from-0.patch) by @ncalexan created at 2008-08-13 18:50:40",
    "created_at": "2008-08-13T18:50:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3840#issuecomment-27247",
    "user": "https://github.com/ncalexan"
}
```

Attachment [3840-gfurnish-multivariate-conversion-from-0.patch](tarball://root/attachments/some-uuid/ticket3840/3840-gfurnish-multivariate-conversion-from-0.patch) by @ncalexan created at 2008-08-13 18:50:40



---

archive/issue_comments_027248.json:
```json
{
    "body": "Apply only `3840-gfurnish-multivariate-conversion-from-0.patch`; hopefully the credit in hg remains with gfurnish.  Let me know if not; I used the hg export command this time.\n\nI think this patch does what the referee wants and strikes a better doctesting balance.\n\nWhether -1 is correct or -Infinity is correct, this at least makes sage internally more consistent.",
    "created_at": "2008-08-13T18:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3840#issuecomment-27248",
    "user": "https://github.com/ncalexan"
}
```

Apply only `3840-gfurnish-multivariate-conversion-from-0.patch`; hopefully the credit in hg remains with gfurnish.  Let me know if not; I used the hg export command this time.

I think this patch does what the referee wants and strikes a better doctesting balance.

Whether -1 is correct or -Infinity is correct, this at least makes sage internally more consistent.



---

archive/issue_comments_027249.json:
```json
{
    "body": "Positive review for the second patch.  All credit to Gfurnish (except Nick and I get referee credit).",
    "created_at": "2008-08-13T19:08:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3840#issuecomment-27249",
    "user": "https://github.com/williamstein"
}
```

Positive review for the second patch.  All credit to Gfurnish (except Nick and I get referee credit).



---

archive/issue_comments_027250.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-13T21:05:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3840#issuecomment-27250",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027251.json:
```json
{
    "body": "Merged 3840-gfurnish-multivariate-conversion-from-0.patch in Sage 3.1.alpha2",
    "created_at": "2008-08-13T21:05:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3840#issuecomment-27251",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 3840-gfurnish-multivariate-conversion-from-0.patch in Sage 3.1.alpha2



---

archive/issue_events_008793.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-13T21:05:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3840",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3840#event-8793"
}
```
