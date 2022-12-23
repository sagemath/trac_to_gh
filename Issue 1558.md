# Issue 1558: [with patch] more NTL wrapping, coefficient access and factoring

archive/issues_001558.json:
```json
{
    "body": "Assignee: somebody\n\nThe attached patch provides some more lines in ntl/decl.pxi to give direct access to some more of NTL.  The are two main functionality improvements:\n\n1) !__getitem!__ now has one less copy of the coefficient.  This results in a noticable speed improvement for coefficients (and !__hash!__)\n\n2) New _factor_ntl and _factor_pari in sage/rings/polynomial/polynomial_integer_dense_ntl.pyx enable us to have more fun with head-to-head comparisons of their factoring routines.  It really seems a mixed bag about who is faster.  I have a basic check in place that keeps the factoring all in NTL for small coefficients, but this really isn't the end of the story as far as the benchmarking goes.\n\n\n```\n# original\nsage: R.<x>=ZZ[]\nsage: f=x^2-1\nsage: timeit f.factor()\n1000 loops, best of 3: 784 \u00b5s per loop\n```\n\n\n\n```\n# patched\nsage: R.<x>=ZZ[]\nsage: f=x^2-1\nsage: timeit f.factor()\n10000 loops, best of 3: 153 \u00b5s per loop\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1558\n\n",
    "created_at": "2007-12-18T16:26:15Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "[with patch] more NTL wrapping, coefficient access and factoring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1558",
    "user": "jbmohler"
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

archive/issue_comments_009930.json:
```json
{
    "body": "Attachment\n\na patch with better decision process for pari or ntl",
    "created_at": "2007-12-19T19:51:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1558#issuecomment-9930",
    "user": "jbmohler"
}
```

Attachment

a patch with better decision process for pari or ntl



---

archive/issue_comments_009931.json:
```json
{
    "body": "The patch applies, builds, and passes tests for me.",
    "created_at": "2007-12-22T23:11:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1558#issuecomment-9931",
    "user": "mhansen"
}
```

The patch applies, builds, and passes tests for me.



---

archive/issue_comments_009932.json:
```json
{
    "body": "merged in 2.9.1 rc2",
    "created_at": "2007-12-23T07:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1558#issuecomment-9932",
    "user": "rlm"
}
```

merged in 2.9.1 rc2



---

archive/issue_comments_009933.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-23T07:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1558#issuecomment-9933",
    "user": "rlm"
}
```

Resolution: fixed
