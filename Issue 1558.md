# Issue 1558: [with patch] more NTL wrapping, coefficient access and factoring

archive/issues_001558.json:
```json
{
    "body": "Assignee: somebody\n\nThe attached patch provides some more lines in ntl/decl.pxi to give direct access to some more of NTL.  The are two main functionality improvements:\n\n1) !__getitem!__ now has one less copy of the coefficient.  This results in a noticable speed improvement for coefficients (and !__hash!__)\n\n2) New _factor_ntl and _factor_pari in sage/rings/polynomial/polynomial_integer_dense_ntl.pyx enable us to have more fun with head-to-head comparisons of their factoring routines.  It really seems a mixed bag about who is faster.  I have a basic check in place that keeps the factoring all in NTL for small coefficients, but this really isn't the end of the story as far as the benchmarking goes.\n\n\n```\n# original\nsage: R.<x>=ZZ[]\nsage: f=x^2-1\nsage: timeit f.factor()\n1000 loops, best of 3: 784 \u00b5s per loop\n```\n\n\n\n```\n# patched\nsage: R.<x>=ZZ[]\nsage: f=x^2-1\nsage: timeit f.factor()\n10000 loops, best of 3: 153 \u00b5s per loop\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1558\n\n",
    "created_at": "2007-12-18T16:26:15Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.1",
    "title": "[with patch] more NTL wrapping, coefficient access and factoring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1558",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```
Assignee: somebody

The attached patch provides some more lines in ntl/decl.pxi to give direct access to some more of NTL.  The are two main functionality improvements:

1) !__getitem!__ now has one less copy of the coefficient.  This results in a noticable speed improvement for coefficients (and !__hash!__)

2) New _factor_ntl and _factor_pari in sage/rings/polynomial/polynomial_integer_dense_ntl.pyx enable us to have more fun with head-to-head comparisons of their factoring routines.  It really seems a mixed bag about who is faster.  I have a basic check in place that keeps the factoring all in NTL for small coefficients, but this really isn't the end of the story as far as the benchmarking goes.


```
# original
sage: R.<x>=ZZ[]
sage: f=x^2-1
sage: timeit f.factor()
1000 loops, best of 3: 784 µs per loop
```



```
# patched
sage: R.<x>=ZZ[]
sage: f=x^2-1
sage: timeit f.factor()
10000 loops, best of 3: 153 µs per loop
```


Issue created by migration from https://trac.sagemath.org/ticket/1558





---

archive/issue_comments_009904.json:
```json
{
    "body": "Attachment [uni-factoring-ntl.patch](tarball://root/attachments/some-uuid/ticket1558/uni-factoring-ntl.patch) by jbmohler created at 2007-12-19 19:51:48\n\na patch with better decision process for pari or ntl",
    "created_at": "2007-12-19T19:51:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1558#issuecomment-9904",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Attachment [uni-factoring-ntl.patch](tarball://root/attachments/some-uuid/ticket1558/uni-factoring-ntl.patch) by jbmohler created at 2007-12-19 19:51:48

a patch with better decision process for pari or ntl



---

archive/issue_comments_009905.json:
```json
{
    "body": "The patch applies, builds, and passes tests for me.",
    "created_at": "2007-12-22T23:11:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1558#issuecomment-9905",
    "user": "https://github.com/mwhansen"
}
```

The patch applies, builds, and passes tests for me.



---

archive/issue_events_001712.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2007-12-23T07:08:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1558",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1558#event-1712"
}
```



---

archive/issue_comments_009906.json:
```json
{
    "body": "merged in 2.9.1 rc2",
    "created_at": "2007-12-23T07:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1558#issuecomment-9906",
    "user": "https://github.com/rlmill"
}
```

merged in 2.9.1 rc2



---

archive/issue_comments_009907.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-23T07:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1558#issuecomment-9907",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
