# Issue 4390: elliptic curves: heegner_index command broken

archive/issues_004390.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: EllipticCurve('675b').heegner_index(-11)\nTraceback (most recent call last):\n...\nTypeError: regulator() got an unexpected keyword argument 'verbose'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4390\n\n",
    "created_at": "2008-10-30T05:35:53Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "elliptic curves: heegner_index command broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4390",
    "user": "@williamstein"
}
```
Assignee: @williamstein


```
sage: EllipticCurve('675b').heegner_index(-11)
Traceback (most recent call last):
...
TypeError: regulator() got an unexpected keyword argument 'verbose'
```


Issue created by migration from https://trac.sagemath.org/ticket/4390





---

archive/issue_comments_032311.json:
```json
{
    "body": "Attachment [sage-4390.patch](tarball://root/attachments/some-uuid/ticket4390/sage-4390.patch) by @williamstein created at 2008-10-30 05:40:48",
    "created_at": "2008-10-30T05:40:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4390#issuecomment-32311",
    "user": "@williamstein"
}
```

Attachment [sage-4390.patch](tarball://root/attachments/some-uuid/ticket4390/sage-4390.patch) by @williamstein created at 2008-10-30 05:40:48



---

archive/issue_comments_032312.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-10-30T05:43:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4390#issuecomment-32312",
    "user": "@craigcitro"
}
```

Looks good.



---

archive/issue_comments_032313.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-30T05:46:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4390#issuecomment-32313",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha2



---

archive/issue_comments_032314.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-30T05:46:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4390#issuecomment-32314",
    "user": "mabshoff"
}
```

Resolution: fixed
