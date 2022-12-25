# Issue 8211: bug in multiplication of polynomials over RR

archive/issues_008211.json:
```json
{
    "body": "Assignee: @malb\n\nKeywords: RealField, PolynomialRing\n\nas reported on sage-devel [Segfault: Polynomials over RealField]\nsage: P.<x> = PolynomialRing(RealField()) \nsage: P(0)*P(0)+P(0) \nProgram received signal SIGSEGV, Segmentation fault. \n\nit can be traced down to a bug in _mul_ that computes the degree\nof the polynomial P(0)*P(0) wrongly (-2 istead of -1 !)\nPatch is trivial, and attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8211\n\n",
    "created_at": "2010-02-08T05:32:29Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "bug in multiplication of polynomials over RR",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8211",
    "user": "https://github.com/dimpase"
}
```
Assignee: @malb

Keywords: RealField, PolynomialRing

as reported on sage-devel [Segfault: Polynomials over RealField]
sage: P.<x> = PolynomialRing(RealField()) 
sage: P(0)*P(0)+P(0) 
Program received signal SIGSEGV, Segmentation fault. 

it can be traced down to a bug in _mul_ that computes the degree
of the polynomial P(0)*P(0) wrongly (-2 istead of -1 !)
Patch is trivial, and attached.

Issue created by migration from https://trac.sagemath.org/ticket/8211





---

archive/issue_comments_072289.json:
```json
{
    "body": "Attachment [trac-8211.patch](tarball://root/attachments/some-uuid/ticket8211/trac-8211.patch) by @dimpase created at 2010-02-08 05:34:32",
    "created_at": "2010-02-08T05:34:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8211#issuecomment-72289",
    "user": "https://github.com/dimpase"
}
```

Attachment [trac-8211.patch](tarball://root/attachments/some-uuid/ticket8211/trac-8211.patch) by @dimpase created at 2010-02-08 05:34:32



---

archive/issue_comments_072290.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-08T05:34:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8211#issuecomment-72290",
    "user": "https://github.com/dimpase"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072291.json:
```json
{
    "body": "Looks good.",
    "created_at": "2010-02-08T10:33:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8211#issuecomment-72291",
    "user": "https://github.com/malb"
}
```

Looks good.



---

archive/issue_comments_072292.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-08T10:33:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8211#issuecomment-72292",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072293.json:
```json
{
    "body": "The ticket number is missing from the commit string.  I've refreshed the patch I've applied to 4.3.3.alpha0.",
    "created_at": "2010-02-10T14:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8211#issuecomment-72293",
    "user": "https://github.com/qed777"
}
```

The ticket number is missing from the commit string.  I've refreshed the patch I've applied to 4.3.3.alpha0.



---

archive/issue_comments_072294.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:44:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8211#issuecomment-72294",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_008413.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-02-11T14:44:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8211",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8211#event-8413"
}
```
