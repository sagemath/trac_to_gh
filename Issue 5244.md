# Issue 5244: is_unit is mostly not implemented for symbolic ring.

archive/issues_005244.json:
```json
{
    "body": "Assignee: hivert\n\nCC:  sage-combinat\n\nKeywords: is_unit, symbolic ring\n\nHere is the code of is_unit for symbolic rings (it is actually iherited from Ring):\n\n```\n    def is_unit(self):\n        if self == 1 or self == -1:\n            return True\n        raise NotImplementedError\n```\n\nOn can do better !!!\n\nAs a result\n\n```\nsage: m=matrix(SR, 2,2)\nsage: m.is_invertible()\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5244\n\n",
    "created_at": "2009-02-12T14:06:17Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "is_unit is mostly not implemented for symbolic ring.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5244",
    "user": "hivert"
}
```
Assignee: hivert

CC:  sage-combinat

Keywords: is_unit, symbolic ring

Here is the code of is_unit for symbolic rings (it is actually iherited from Ring):

```
    def is_unit(self):
        if self == 1 or self == -1:
            return True
        raise NotImplementedError
```

On can do better !!!

As a result

```
sage: m=matrix(SR, 2,2)
sage: m.is_invertible()
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
```



Issue created by migration from https://trac.sagemath.org/ticket/5244





---

archive/issue_comments_040204.json:
```json
{
    "body": "Attachment [symb_ring_is_unit-fh.patch](tarball://root/attachments/some-uuid/ticket5244/symb_ring_is_unit-fh.patch) by hivert created at 2009-02-13 15:59:40\n\nPatch proposal for is_unit is SR",
    "created_at": "2009-02-13T15:59:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5244#issuecomment-40204",
    "user": "hivert"
}
```

Attachment [symb_ring_is_unit-fh.patch](tarball://root/attachments/some-uuid/ticket5244/symb_ring_is_unit-fh.patch) by hivert created at 2009-02-13 15:59:40

Patch proposal for is_unit is SR



---

archive/issue_comments_040205.json:
```json
{
    "body": "The attached patch propose a solution.",
    "created_at": "2009-02-13T16:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5244#issuecomment-40205",
    "user": "hivert"
}
```

The attached patch propose a solution.



---

archive/issue_comments_040206.json:
```json
{
    "body": "Sage 3.4 is for ReST patches only at the moment, so I am bumping it to 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-13T17:34:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5244#issuecomment-40206",
    "user": "mabshoff"
}
```

Sage 3.4 is for ReST patches only at the moment, so I am bumping it to 3.4.1.

Cheers,

Michael



---

archive/issue_comments_040207.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-13T18:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5244#issuecomment-40207",
    "user": "hivert"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040208.json:
```json
{
    "body": "I have doctested this patch on top of #5242 in my current Sage 3.3.rc1 merge tree and:\n\n```\nAll tests passed!\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T16:33:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5244#issuecomment-40208",
    "user": "mabshoff"
}
```

I have doctested this patch on top of #5242 in my current Sage 3.3.rc1 merge tree and:

```
All tests passed!
```


Cheers,

Michael



---

archive/issue_comments_040209.json:
```json
{
    "body": "Patch reads good, since in SR really everything != 0 is a unit.",
    "created_at": "2009-02-14T17:10:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5244#issuecomment-40209",
    "user": "malb"
}
```

Patch reads good, since in SR really everything != 0 is a unit.



---

archive/issue_comments_040210.json:
```json
{
    "body": "Merged in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-15T07:17:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5244#issuecomment-40210",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc1.

Cheers,

Michael



---

archive/issue_comments_040211.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-15T07:17:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5244#issuecomment-40211",
    "user": "mabshoff"
}
```

Resolution: fixed
