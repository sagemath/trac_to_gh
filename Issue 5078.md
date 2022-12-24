# Issue 5078: bug in factoring out constant literal

archive/issues_005078.json:
```json
{
    "body": "Assignee: cwitty\n\n\n```\nsage: R1 = PolynomialRing(QQ, 'x,y,z')\nsage: R1.0\nTraceback (most recent call last):\n...\nNameError: name 'R1_sage_const_p0' is not defined\nsage: R1.gen(0)\nx\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5078\n\n",
    "created_at": "2009-01-23T22:23:39Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "bug in factoring out constant literal",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5078",
    "user": "was"
}
```
Assignee: cwitty


```
sage: R1 = PolynomialRing(QQ, 'x,y,z')
sage: R1.0
Traceback (most recent call last):
...
NameError: name 'R1_sage_const_p0' is not defined
sage: R1.gen(0)
x
```


Issue created by migration from https://trac.sagemath.org/ticket/5078





---

archive/issue_comments_038669.json:
```json
{
    "body": "Attachment [5078-preparse-const.patch](tarball://root/attachments/some-uuid/ticket5078/5078-preparse-const.patch) by robertwb created at 2009-01-24 02:05:15",
    "created_at": "2009-01-24T02:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5078#issuecomment-38669",
    "user": "robertwb"
}
```

Attachment [5078-preparse-const.patch](tarball://root/attachments/some-uuid/ticket5078/5078-preparse-const.patch) by robertwb created at 2009-01-24 02:05:15



---

archive/issue_comments_038670.json:
```json
{
    "body": "Works for me.",
    "created_at": "2009-01-24T02:36:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5078#issuecomment-38670",
    "user": "boothby"
}
```

Works for me.



---

archive/issue_comments_038671.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T16:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5078#issuecomment-38671",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2



---

archive/issue_comments_038672.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T16:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5078#issuecomment-38672",
    "user": "mabshoff"
}
```

Resolution: fixed
