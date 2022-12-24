# Issue 7715: implement vectors mod 2 as M4RI matrices with one row

archive/issues_007715.json:
```json
{
    "body": "Assignee: was\n\nCC:  simonking\n\nKeywords: vector, M4RI, matrix, GF(2)\n\nIn order to resolve the embarrassing situation at #3684, we need faster vectors mod 2.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7715\n\n",
    "created_at": "2009-12-16T17:18:14Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "implement vectors mod 2 as M4RI matrices with one row",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7715",
    "user": "malb"
}
```
Assignee: was

CC:  simonking

Keywords: vector, M4RI, matrix, GF(2)

In order to resolve the embarrassing situation at #3684, we need faster vectors mod 2.

Issue created by migration from https://trac.sagemath.org/ticket/7715





---

archive/issue_comments_066261.json:
```json
{
    "body": "The speed-up provided by this patch is considerable (but not as much as one would hope for). Here's the example from #3684:\n\n**Before**\n\n\n```python\nsage: A = random_matrix(GF(2),1000,2000)\nsage: %time K = A.right_kernel()\nCPU times: user 11.24 s, sys: 0.02 s, total: 11.25 s\nWall time: 11.42 s\n```\n\n\n\n**After**\n\n\n```python\nsage: A = random_matrix(GF(2),1000,2000)\nsage: %time K = A.right_kernel()\nCPU times: user 0.15 s, sys: 0.00 s, total: 0.15 s\nWall time: 0.16 s\n```\n\n\nSpeed-up: 11.25/0.15 = 75\n\n\n----\n\nAnother example\n\n**Before**\n\n\n```python\nsage: VS = VectorSpace(GF(2),10^4)\nsage: e = VS.random_element()\nsage: f = VS.random_element()\nsage: %timeit e+f\n10000 loops, best of 3: 89.8 \u00b5s per loop\nsage: %timeit e*f\n10000 loops, best of 3: 146 \u00b5s per loop\n```\n\n\n**After**\n\n\n```python\nsage: VS = VectorSpace(GF(2),10^4)\nsage: e = VS.random_element()\nsage: f = VS.random_element()\nsage: %timeit e+f\n1000000 loops, best of 3: 1.08 \u00b5s per loop\nsage: %timeit e*f\n100000 loops, best of 3: 2.47 \u00b5s per loop\n```\n\n\nSpeed-ups: 83 and 59.\n\n----\nThe attached patch might indeed depend on #3684.",
    "created_at": "2009-12-16T17:29:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7715#issuecomment-66261",
    "user": "malb"
}
```

The speed-up provided by this patch is considerable (but not as much as one would hope for). Here's the example from #3684:

**Before**


```python
sage: A = random_matrix(GF(2),1000,2000)
sage: %time K = A.right_kernel()
CPU times: user 11.24 s, sys: 0.02 s, total: 11.25 s
Wall time: 11.42 s
```



**After**


```python
sage: A = random_matrix(GF(2),1000,2000)
sage: %time K = A.right_kernel()
CPU times: user 0.15 s, sys: 0.00 s, total: 0.15 s
Wall time: 0.16 s
```


Speed-up: 11.25/0.15 = 75


----

Another example

**Before**


```python
sage: VS = VectorSpace(GF(2),10^4)
sage: e = VS.random_element()
sage: f = VS.random_element()
sage: %timeit e+f
10000 loops, best of 3: 89.8 µs per loop
sage: %timeit e*f
10000 loops, best of 3: 146 µs per loop
```


**After**


```python
sage: VS = VectorSpace(GF(2),10^4)
sage: e = VS.random_element()
sage: f = VS.random_element()
sage: %timeit e+f
1000000 loops, best of 3: 1.08 µs per loop
sage: %timeit e*f
100000 loops, best of 3: 2.47 µs per loop
```


Speed-ups: 83 and 59.

----
The attached patch might indeed depend on #3684.



---

archive/issue_comments_066262.json:
```json
{
    "body": "Attachment [vector_mod2_dense.patch](tarball://root/attachments/some-uuid/ticket7715/vector_mod2_dense.patch) by malb created at 2009-12-16 17:38:51",
    "created_at": "2009-12-16T17:38:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7715#issuecomment-66262",
    "user": "malb"
}
```

Attachment [vector_mod2_dense.patch](tarball://root/attachments/some-uuid/ticket7715/vector_mod2_dense.patch) by malb created at 2009-12-16 17:38:51



---

archive/issue_comments_066263.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-16T18:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7715#issuecomment-66263",
    "user": "malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066264.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-12-19T22:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7715#issuecomment-66264",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_066265.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-19T22:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7715#issuecomment-66265",
    "user": "mhansen"
}
```

Resolution: fixed
