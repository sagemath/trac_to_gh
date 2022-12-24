# Issue 5347: divides() may fail for 1 on the rhs.

archive/issues_005347.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  mhansen\n\n\n```\nsage: K = GF(7)\nsage: K(3).divides(1)\nFalse\nsage: K(3).divides(K(1))\nTraceback (most recent call last)\n...\nZeroDivisionError: reduction modulo right not defined.\n```\n\n\nThis is because of this code added at http://hg.sagemath.org/sage-main/rev/0cb746e1a4bd\n\n\n```\ndef divides(self, x):\n    return (x % self) == 0\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5347\n\n",
    "created_at": "2009-02-23T08:21:33Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "divides() may fail for 1 on the rhs.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5347",
    "user": "malb"
}
```
Assignee: somebody

CC:  mhansen


```
sage: K = GF(7)
sage: K(3).divides(1)
False
sage: K(3).divides(K(1))
Traceback (most recent call last)
...
ZeroDivisionError: reduction modulo right not defined.
```


This is because of this code added at http://hg.sagemath.org/sage-main/rev/0cb746e1a4bd


```
def divides(self, x):
    return (x % self) == 0
```



Issue created by migration from https://trac.sagemath.org/ticket/5347





---

archive/issue_comments_041200.json:
```json
{
    "body": "Attachment [trac_5347-divides.patch](tarball://root/attachments/some-uuid/ticket5347/trac_5347-divides.patch) by cremona created at 2009-08-30 17:43:24\n\nApplies to 4.1.1",
    "created_at": "2009-08-30T17:43:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5347#issuecomment-41200",
    "user": "cremona"
}
```

Attachment [trac_5347-divides.patch](tarball://root/attachments/some-uuid/ticket5347/trac_5347-divides.patch) by cremona created at 2009-08-30 17:43:24

Applies to 4.1.1



---

archive/issue_comments_041201.json:
```json
{
    "body": "Changing keywords from \"\" to \"ring element divides\".",
    "created_at": "2009-08-30T17:45:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5347#issuecomment-41201",
    "user": "cremona"
}
```

Changing keywords from "" to "ring element divides".



---

archive/issue_comments_041202.json:
```json
{
    "body": "The patch handles this by testing all the easy cases of a.divides(b) (a is 1 or a unit, b is zero) before trying the % operation.  Doctest added to show that it works.",
    "created_at": "2009-08-30T17:45:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5347#issuecomment-41202",
    "user": "cremona"
}
```

The patch handles this by testing all the easy cases of a.divides(b) (a is 1 or a unit, b is zero) before trying the % operation.  Doctest added to show that it works.



---

archive/issue_comments_041203.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-09-08T23:52:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5347#issuecomment-41203",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_041204.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-09T04:48:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5347#issuecomment-41204",
    "user": "mvngu"
}
```

Resolution: fixed
