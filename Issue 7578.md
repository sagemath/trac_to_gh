# Issue 7578: Slowness of InfinitePolynomialRing basic arithmetic

archive/issues_007578.json:
```json
{
    "body": "Assignee: @simon-king-jena\n\nKeywords: infinite polynomial ring, basic arithmetic\n\n[Martin Albrecht](http://groups.google.com/group/sage-devel/browse_thread/thread/20e0fc8f5c5be582) reported the following example:\n\n\n```\nsage: X.<x> = InfinitePolynomialRing(QQ)\nsage: x10000 = x[10000]\nsage: x10001 = x[10001]\nsage: %time 1/2*x10000\nCPU times: user 43.09 s, sys: 0.02 s, total: 43.12 s\nWall time: 43.12 s\n1/2*x10000\n```\n\n\nThis is inacceptably slow.\n\nNote that this problem does not occur with the sparse implementation of infinite polynomial rings:\n\n\n```\nsage: X.<x> = InfinitePolynomialRing(QQ,implementation='sparse')\nsage: x10000 = x[10000]\nsage: x10001 = x[10001]\nsage: %time 1/2*x10000\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\n1/2*x10000\n```\n\n\nPart of the problem is a slowness of element conversion in polynomial rings:\n\n\n```\nsage: R1 = PolynomialRing(QQ,'x',10001)\nsage: R2 = PolynomialRing(QQ,'x',10002)\nsage: x10000 = R1('x10000')\nsage: %time a = R2(x10000)\nCPU times: user 4.96 s, sys: 0.12 s, total: 5.08 s\nWall time: 5.11 s\n```\n\nwhich is rather slow as  well.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7578\n\n",
    "created_at": "2009-12-01T23:14:52Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Slowness of InfinitePolynomialRing basic arithmetic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7578",
    "user": "https://github.com/simon-king-jena"
}
```
Assignee: @simon-king-jena

Keywords: infinite polynomial ring, basic arithmetic

[Martin Albrecht](http://groups.google.com/group/sage-devel/browse_thread/thread/20e0fc8f5c5be582) reported the following example:


```
sage: X.<x> = InfinitePolynomialRing(QQ)
sage: x10000 = x[10000]
sage: x10001 = x[10001]
sage: %time 1/2*x10000
CPU times: user 43.09 s, sys: 0.02 s, total: 43.12 s
Wall time: 43.12 s
1/2*x10000
```


This is inacceptably slow.

Note that this problem does not occur with the sparse implementation of infinite polynomial rings:


```
sage: X.<x> = InfinitePolynomialRing(QQ,implementation='sparse')
sage: x10000 = x[10000]
sage: x10001 = x[10001]
sage: %time 1/2*x10000
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
1/2*x10000
```


Part of the problem is a slowness of element conversion in polynomial rings:


```
sage: R1 = PolynomialRing(QQ,'x',10001)
sage: R2 = PolynomialRing(QQ,'x',10002)
sage: x10000 = R1('x10000')
sage: %time a = R2(x10000)
CPU times: user 4.96 s, sys: 0.12 s, total: 5.08 s
Wall time: 5.11 s
```

which is rather slow as  well.

Issue created by migration from https://trac.sagemath.org/ticket/7578





---

archive/issue_comments_064427.json:
```json
{
    "body": "Improving basic arithmetic of infinite polynomial rings",
    "created_at": "2009-12-01T23:22:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7578#issuecomment-64427",
    "user": "https://github.com/simon-king-jena"
}
```

Improving basic arithmetic of infinite polynomial rings



---

archive/issue_comments_064428.json:
```json
{
    "body": "Attachment [7578_basic_arithmetic.patch](tarball://root/attachments/some-uuid/ticket7578/7578_basic_arithmetic.patch) by @simon-king-jena created at 2009-12-01 23:50:45\n\nWith the attached patch, the example improves a lot:\n\n```\nsage: X.<x> = InfinitePolynomialRing(QQ)\nsage: x10000 = x[10000]\nsage: x10001 = x[10001]\nsage: %time 1/2*x10000\nCPU times: user 7.37 s, sys: 0.01 s, total: 7.38 s\nWall time: 7.38 s\n1/2*x10000\n```\n\n\nOf course, this is still a shame. But it may be better than nothing.\n\nThe idea / reason for the slowness:\n\n* When x10001 is created, the underlying finite polynomial ring of X changes. At this point, the underlying finite polynomial of x10000 does not belong to the underlying ring of X anymore.\n* In the old code, the underlying finite polynomial of x10000 was not updated.\n* With the patch, it will be updated as soon as x10000 is involved in any multiplication, summation or difference.\n\nHence, the timing is essentially reduced to the time for conversion of the underlying polynomials; namely, after restarting sage (clearing the cache):\n\n```\nsage: X.<x> = InfinitePolynomialRing(QQ)\nsage: x10000 = x[10000]\nsage: x10001 = x[10001]\nsage: %time x10000._p = X._P(x10000._p)\nCPU times: user 6.90 s, sys: 0.01 s, total: 6.91 s\nWall time: 6.91 s\n```\n\n\nI don't think that this is a satisfying time, but it is some progress, and as long as element conversion for polynomial rings isn't improved, I see no way to do it better.",
    "created_at": "2009-12-01T23:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7578#issuecomment-64428",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [7578_basic_arithmetic.patch](tarball://root/attachments/some-uuid/ticket7578/7578_basic_arithmetic.patch) by @simon-king-jena created at 2009-12-01 23:50:45

With the attached patch, the example improves a lot:

```
sage: X.<x> = InfinitePolynomialRing(QQ)
sage: x10000 = x[10000]
sage: x10001 = x[10001]
sage: %time 1/2*x10000
CPU times: user 7.37 s, sys: 0.01 s, total: 7.38 s
Wall time: 7.38 s
1/2*x10000
```


Of course, this is still a shame. But it may be better than nothing.

The idea / reason for the slowness:

* When x10001 is created, the underlying finite polynomial ring of X changes. At this point, the underlying finite polynomial of x10000 does not belong to the underlying ring of X anymore.
* In the old code, the underlying finite polynomial of x10000 was not updated.
* With the patch, it will be updated as soon as x10000 is involved in any multiplication, summation or difference.

Hence, the timing is essentially reduced to the time for conversion of the underlying polynomials; namely, after restarting sage (clearing the cache):

```
sage: X.<x> = InfinitePolynomialRing(QQ)
sage: x10000 = x[10000]
sage: x10001 = x[10001]
sage: %time x10000._p = X._P(x10000._p)
CPU times: user 6.90 s, sys: 0.01 s, total: 6.91 s
Wall time: 6.91 s
```


I don't think that this is a satisfying time, but it is some progress, and as long as element conversion for polynomial rings isn't improved, I see no way to do it better.



---

archive/issue_comments_064429.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-01T23:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7578#issuecomment-64429",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064430.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-02T11:36:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7578#issuecomment-64430",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064431.json:
```json
{
    "body": "The change seems sensible, applies cleanly against 4.3.alpha0, doctests pass. positive review.",
    "created_at": "2009-12-02T11:36:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7578#issuecomment-64431",
    "user": "https://github.com/malb"
}
```

The change seems sensible, applies cleanly against 4.3.alpha0, doctests pass. positive review.



---

archive/issue_comments_064432.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-02T12:39:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7578#issuecomment-64432",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
