# Issue 6339: multivariate polynomial content is broken

archive/issues_006339.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @malb\n\nKeywords: polynomial content\n\n\n```\nsage: QQ['x, y'].random_element().content()\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/ncalexan/.sage/temp/sage.math.washington.edu/8651/_home_ncalexan__sage_init_sage_0.py in <module>()\n\n/scratch/ncalexan/sage-4.0.2.alpha1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial.so in sage.rings.polynomial.multi_polynom\\\nial.MPolynomial.content (sage/rings/polynomial/multi_polynomial.c:9118)()\n\n/scratch/ncalexan/sage-4.0.2.alpha1/local/lib/python2.5/site-packages/sage/rings/arith.pyc in gcd(a, b, **kwargs)\n   1209     if U is ZZ or U is int or U is long:# ZZ.has_coerce_map_from(U):\n   1210         return sage.rings.integer.GCD_list(a)\n-> 1211     return __GCD_sequence(seq, **kwargs)\n   1212\n   1213 GCD = gcd\n\n/scratch/ncalexan/sage-4.0.2.alpha1/local/lib/python2.5/site-packages/sage/rings/arith.pyc in __GCD_sequence(v, **kwargs)\n   1249     one = v.universe()(1)\n   1250     for vi in v:\n-> 1251         g = vi.gcd(g, **kwargs)\n   1252         if g == one:\n   1253             return g\n\nTypeError: gcd() takes no keyword arguments\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6339\n\n",
    "created_at": "2009-06-16T19:05:07Z",
    "labels": [
        "component: commutative algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "multivariate polynomial content is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6339",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @malb

CC:  @malb

Keywords: polynomial content


```
sage: QQ['x, y'].random_element().content()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/ncalexan/.sage/temp/sage.math.washington.edu/8651/_home_ncalexan__sage_init_sage_0.py in <module>()

/scratch/ncalexan/sage-4.0.2.alpha1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial.so in sage.rings.polynomial.multi_polynom\
ial.MPolynomial.content (sage/rings/polynomial/multi_polynomial.c:9118)()

/scratch/ncalexan/sage-4.0.2.alpha1/local/lib/python2.5/site-packages/sage/rings/arith.pyc in gcd(a, b, **kwargs)
   1209     if U is ZZ or U is int or U is long:# ZZ.has_coerce_map_from(U):
   1210         return sage.rings.integer.GCD_list(a)
-> 1211     return __GCD_sequence(seq, **kwargs)
   1212
   1213 GCD = gcd

/scratch/ncalexan/sage-4.0.2.alpha1/local/lib/python2.5/site-packages/sage/rings/arith.pyc in __GCD_sequence(v, **kwargs)
   1249     one = v.universe()(1)
   1250     for vi in v:
-> 1251         g = vi.gcd(g, **kwargs)
   1252         if g == one:
   1253             return g

TypeError: gcd() takes no keyword arguments
```


Issue created by migration from https://trac.sagemath.org/ticket/6339





---

archive/issue_comments_050504.json:
```json
{
    "body": "Attachment [content.patch](tarball://root/attachments/some-uuid/ticket6339/content.patch) by @malb created at 2009-09-09 20:25:01",
    "created_at": "2009-09-09T20:25:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6339#issuecomment-50504",
    "user": "https://github.com/malb"
}
```

Attachment [content.patch](tarball://root/attachments/some-uuid/ticket6339/content.patch) by @malb created at 2009-09-09 20:25:01



---

archive/issue_comments_050505.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-09-26T04:46:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6339#issuecomment-50505",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_events_006583.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-09-26T07:47:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6339",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6339#event-6583"
}
```



---

archive/issue_comments_050506.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-26T07:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6339#issuecomment-50506",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_050507.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6339#issuecomment-50507",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
