# Issue 5482: Quotient ring can be created without generator names

archive/issues_005482.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe following code works:\n\n```\nsage: R.<x> = PolynomialRing(QQ)\nsage: f = x^2-1\nsage: S = R.quotient_by_principal_ideal(f)\n```\n\nbut then this fails:\n\n```\nsage: S\n ---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n...[snip]\n/Users/tmp/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/structure/category_object.so in sage.structure.category_object.CategoryObject.variable_names (sage/structure/category_object.c:3530)()\n\nValueError: variable names have not yet been set using self._assign_names(...)\n```\n\nThe routine should require that the name(s) be provided.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5482\n\n",
    "created_at": "2009-03-11T06:44:39Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Quotient ring can be created without generator names",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5482",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```
Assignee: @williamstein

The following code works:

```
sage: R.<x> = PolynomialRing(QQ)
sage: f = x^2-1
sage: S = R.quotient_by_principal_ideal(f)
```

but then this fails:

```
sage: S
 ---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
...[snip]
/Users/tmp/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/structure/category_object.so in sage.structure.category_object.CategoryObject.variable_names (sage/structure/category_object.c:3530)()

ValueError: variable names have not yet been set using self._assign_names(...)
```

The routine should require that the name(s) be provided.



Issue created by migration from https://trac.sagemath.org/ticket/5482





---

archive/issue_comments_042449.json:
```json
{
    "body": "Attachment [sage-5482.patch](tarball://root/attachments/some-uuid/ticket5482/sage-5482.patch) by justin created at 2009-03-11 07:42:22\n\nThe fix is to require the generator name at creation time, not when the ring is used.",
    "created_at": "2009-03-11T07:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5482#issuecomment-42449",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

Attachment [sage-5482.patch](tarball://root/attachments/some-uuid/ticket5482/sage-5482.patch) by justin created at 2009-03-11 07:42:22

The fix is to require the generator name at creation time, not when the ring is used.



---

archive/issue_comments_042450.json:
```json
{
    "body": "Why do you change the parameter name from \"names\" to \"name\"?  Is this function only used for univariate polynomial rings?  If so, fine.",
    "created_at": "2009-03-14T20:42:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5482#issuecomment-42450",
    "user": "https://github.com/JohnCremona"
}
```

Why do you change the parameter name from "names" to "name"?  Is this function only used for univariate polynomial rings?  If so, fine.



---

archive/issue_comments_042451.json:
```json
{
    "body": "REFEREE REPORT:\n\n1. It *must* be \"names\" not \"name\", so the R.<x> = foo notation works.\n\n2. Every patch has to have a doctest that illustrates that it fixes the bug.",
    "created_at": "2009-03-15T23:52:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5482#issuecomment-42451",
    "user": "https://github.com/williamstein"
}
```

REFEREE REPORT:

1. It *must* be "names" not "name", so the R.<x> = foo notation works.

2. Every patch has to have a doctest that illustrates that it fixes the bug.



---

archive/issue_comments_042452.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-16T03:16:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5482#issuecomment-42452",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_042453.json:
```json
{
    "body": "Changing assignee from @williamstein to justin.",
    "created_at": "2009-03-16T03:16:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5482#issuecomment-42453",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

Changing assignee from @williamstein to justin.



---

archive/issue_comments_042454.json:
```json
{
    "body": "Replying to [comment:4 was]:\n> REFEREE REPORT:\n> \n>  1. It *must* be \"names\" not \"name\", so the R.<x> = foo notation works.\n\nI discovered that while adding doctests.  I'll reverse that change.\n\n>  2. Every patch has to have a doctest that illustrates that it fixes the bug.\n\nDoctests?",
    "created_at": "2009-03-16T03:16:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5482#issuecomment-42454",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

Replying to [comment:4 was]:
> REFEREE REPORT:
> 
>  1. It *must* be "names" not "name", so the R.<x> = foo notation works.

I discovered that while adding doctests.  I'll reverse that change.

>  2. Every patch has to have a doctest that illustrates that it fixes the bug.

Doctests?



---

archive/issue_comments_042455.json:
```json
{
    "body": "Changing component from algebraic geometry to algebra.",
    "created_at": "2009-11-15T11:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5482#issuecomment-42455",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebraic geometry to algebra.



---

archive/issue_comments_042456.json:
```json
{
    "body": "I attached a new patch that assigns names automatically if they are not specified by the user, e.g. a quotient of `R.<x>` will have variable name `xbar`.  This is standard behaviour in other places in Sage.\n\nApply trac_5482.patch only.",
    "created_at": "2009-11-15T12:35:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5482#issuecomment-42456",
    "user": "https://github.com/aghitza"
}
```

I attached a new patch that assigns names automatically if they are not specified by the user, e.g. a quotient of `R.<x>` will have variable name `xbar`.  This is standard behaviour in other places in Sage.

Apply trac_5482.patch only.



---

archive/issue_comments_042457.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-15T12:35:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5482#issuecomment-42457",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_042458.json:
```json
{
    "body": "Attachment [trac_5482.patch](tarball://root/attachments/some-uuid/ticket5482/trac_5482.patch) by @aghitza created at 2009-11-15 12:36:20\n\napply this patch only",
    "created_at": "2009-11-15T12:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5482#issuecomment-42458",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_5482.patch](tarball://root/attachments/some-uuid/ticket5482/trac_5482.patch) by @aghitza created at 2009-11-15 12:36:20

apply this patch only



---

archive/issue_comments_042459.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-17T08:02:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5482#issuecomment-42459",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_042460.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-11-17T08:02:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5482#issuecomment-42460",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_events_005736.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-17T08:03:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5482",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5482#event-5736"
}
```



---

archive/issue_comments_042461.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-17T08:03:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5482#issuecomment-42461",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
