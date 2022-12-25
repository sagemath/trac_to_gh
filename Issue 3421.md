# Issue 3421: [with patch, needs review] MPolynomialRing_libsingular should accept longs in __call__

archive/issues_003421.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @burcin\n\nThis now works:\n\n```\nsage: P.<x,y> = PolynomialRing(QQ)\nsage: P(\"111111111111111111111111111111111111111111111111111111111\")\n111111111111111111111111111111111111111111111111111111111\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3421\n\n",
    "created_at": "2008-06-13T22:08:37Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "[with patch, needs review] MPolynomialRing_libsingular should accept longs in __call__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3421",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @burcin

This now works:

```
sage: P.<x,y> = PolynomialRing(QQ)
sage: P("111111111111111111111111111111111111111111111111111111111")
111111111111111111111111111111111111111111111111111111111
```


Issue created by migration from https://trac.sagemath.org/ticket/3421





---

archive/issue_comments_024030.json:
```json
{
    "body": "This still fails on sage.math:\n\n\n```\nsage: P(\"31367566080\")\n---------------------------------------------------------------------------\nOverflowError                             Traceback (most recent call last)\n\n/home/burcin/sage-3.0.2/<ipython console> in <module>()\n\n/home/burcin/sage-3.0.2/multi_polynomial_libsingular.pyx in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:4707)()\n\n/home/burcin/sage-3.0.2/parent.pyx in sage.structure.parent.Parent._coerce_c (sage/structure/parent.c:3400)()\n\n/home/burcin/sage-3.0.2/multi_polynomial_libsingular.pyx in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular._coerce_c_impl (sage/rings/polynomial/multi_polynomial_libsingular.cpp:4283)()\n\nOverflowError: value too large to convert to int\n```\n",
    "created_at": "2008-06-14T00:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3421#issuecomment-24030",
    "user": "https://github.com/burcin"
}
```

This still fails on sage.math:


```
sage: P("31367566080")
---------------------------------------------------------------------------
OverflowError                             Traceback (most recent call last)

/home/burcin/sage-3.0.2/<ipython console> in <module>()

/home/burcin/sage-3.0.2/multi_polynomial_libsingular.pyx in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:4707)()

/home/burcin/sage-3.0.2/parent.pyx in sage.structure.parent.Parent._coerce_c (sage/structure/parent.c:3400)()

/home/burcin/sage-3.0.2/multi_polynomial_libsingular.pyx in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular._coerce_c_impl (sage/rings/polynomial/multi_polynomial_libsingular.cpp:4283)()

OverflowError: value too large to convert to int
```




---

archive/issue_comments_024031.json:
```json
{
    "body": "updated patch to address review",
    "created_at": "2008-06-14T00:47:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3421#issuecomment-24031",
    "user": "https://github.com/malb"
}
```

updated patch to address review



---

archive/issue_comments_024032.json:
```json
{
    "body": "Attachment [libsingular_longs.patch](tarball://root/attachments/some-uuid/ticket3421/libsingular_longs.patch) by @malb created at 2008-06-14 00:47:42\n\nThe updated patch addresses that bug.",
    "created_at": "2008-06-14T00:47:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3421#issuecomment-24032",
    "user": "https://github.com/malb"
}
```

Attachment [libsingular_longs.patch](tarball://root/attachments/some-uuid/ticket3421/libsingular_longs.patch) by @malb created at 2008-06-14 00:47:42

The updated patch addresses that bug.



---

archive/issue_comments_024033.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-06-14T00:57:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3421#issuecomment-24033",
    "user": "https://github.com/burcin"
}
```

Looks good to me.



---

archive/issue_events_003637.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-15T15:09:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3421",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3421#event-3637"
}
```



---

archive/issue_comments_024034.json:
```json
{
    "body": "Merged in Sage 3.0.3.rc0",
    "created_at": "2008-06-15T15:09:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3421#issuecomment-24034",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.3.rc0



---

archive/issue_comments_024035.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-15T15:09:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3421#issuecomment-24035",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
