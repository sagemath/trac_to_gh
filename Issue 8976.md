# Issue 8976: squarefree_part() fails on Python types

archive/issues_008976.json:
```json
{
    "body": "Assignee: @jasongrout\n\nKeywords: squarefree_part()\n\n\n```\nsage: squarefree_part(216)\n6\nsage: squarefree_part(216r)\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/leif/sage-4.4.1.rc0/devel/sage-8799/<ipython console> in <module>()\n\n/home/leif/sage-4.4.1.rc0/local/lib/python2.6/site-packages/sage/misc/functional.pyc in squarefree_part(x)\n   1478         pass\n   1479     F = factor(x)\n-> 1480     n = x.parent()(1)\n   1481     for p, e in F:\n   1482         if e%2 != 0:\n\nAttributeError: 'int' object has no attribute 'parent'\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8976\n\n",
    "created_at": "2010-05-15T23:54:38Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "squarefree_part() fails on Python types",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8976",
    "user": "@nexttime"
}
```
Assignee: @jasongrout

Keywords: squarefree_part()


```
sage: squarefree_part(216)
6
sage: squarefree_part(216r)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/leif/sage-4.4.1.rc0/devel/sage-8799/<ipython console> in <module>()

/home/leif/sage-4.4.1.rc0/local/lib/python2.6/site-packages/sage/misc/functional.pyc in squarefree_part(x)
   1478         pass
   1479     F = factor(x)
-> 1480     n = x.parent()(1)
   1481     for p, e in F:
   1482         if e%2 != 0:

AttributeError: 'int' object has no attribute 'parent'
```



Issue created by migration from https://trac.sagemath.org/ticket/8976





---

archive/issue_comments_082812.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-05-16T00:00:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8976#issuecomment-82812",
    "user": "@nexttime"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_082813.json:
```json
{
    "body": "This is easy to fix, but I'm not sure if one should simply replace\n\n```\nn = x.parent()(1)\n```\n\nby\n\n```\nn = parent(x)(1)\n```\n\nor e.g. test for `isinstance(x,(int,long,float))` instead.",
    "created_at": "2010-05-16T00:00:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8976#issuecomment-82813",
    "user": "@nexttime"
}
```

This is easy to fix, but I'm not sure if one should simply replace

```
n = x.parent()(1)
```

by

```
n = parent(x)(1)
```

or e.g. test for `isinstance(x,(int,long,float))` instead.



---

archive/issue_comments_082814.json:
```json
{
    "body": "Btw, wouldn't it be convenient to have `squarefree_prime_divisors()` (i.e. a generator/list of just those prime factors with exponent=1), too?\n\n(Currently, there's only `squarefree_divisors()`.)",
    "created_at": "2010-05-16T00:12:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8976#issuecomment-82814",
    "user": "@nexttime"
}
```

Btw, wouldn't it be convenient to have `squarefree_prime_divisors()` (i.e. a generator/list of just those prime factors with exponent=1), too?

(Currently, there's only `squarefree_divisors()`.)



---

archive/issue_comments_082815.json:
```json
{
    "body": "This patch implements my first suggestion. Based on 4.4.2.rc0.",
    "created_at": "2010-05-16T01:26:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8976#issuecomment-82815",
    "user": "@nexttime"
}
```

This patch implements my first suggestion. Based on 4.4.2.rc0.



---

archive/issue_comments_082816.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-05-16T01:27:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8976#issuecomment-82816",
    "user": "@nexttime"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_082817.json:
```json
{
    "body": "Attachment [trac_8976-squarefree_part-fix-variant1.patch](tarball://root/attachments/some-uuid/ticket8976/trac_8976-squarefree_part-fix-variant1.patch) by @nexttime created at 2010-05-16 01:27:55",
    "created_at": "2010-05-16T01:27:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8976#issuecomment-82817",
    "user": "@nexttime"
}
```

Attachment [trac_8976-squarefree_part-fix-variant1.patch](tarball://root/attachments/some-uuid/ticket8976/trac_8976-squarefree_part-fix-variant1.patch) by @nexttime created at 2010-05-16 01:27:55



---

archive/issue_comments_082818.json:
```json
{
    "body": "Changing keywords from \"squarefree_part()\" to \"squarefree_part(), beginner\".",
    "created_at": "2010-05-26T16:42:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8976#issuecomment-82818",
    "user": "@nexttime"
}
```

Changing keywords from "squarefree_part()" to "squarefree_part(), beginner".



---

archive/issue_comments_082819.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-17T21:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8976#issuecomment-82819",
    "user": "@rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082820.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-22T07:40:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8976#issuecomment-82820",
    "user": "@dandrake"
}
```

Resolution: fixed
