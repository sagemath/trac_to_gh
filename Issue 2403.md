# Issue 2403: Cannot copy Sequence

archive/issues_002403.json:
```json
{
    "body": "Assignee: cwitty\n\nI get an error when I am trying to copy a sequence:\n\n\n\n```\nsage: copy([1,2])\n[1, 2]\nsage: copy(Sequence([1,2]))\nTraceback (most recent call last):\n...\nTypeError: sage.structure.sage_object.SageObject.__new__(Sequence) is not safe, use list.__new__()\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2403\n\n",
    "created_at": "2008-03-06T06:18:45Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "title": "Cannot copy Sequence",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2403",
    "user": "novoselt"
}
```
Assignee: cwitty

I get an error when I am trying to copy a sequence:



```
sage: copy([1,2])
[1, 2]
sage: copy(Sequence([1,2]))
Traceback (most recent call last):
...
TypeError: sage.structure.sage_object.SageObject.__new__(Sequence) is not safe, use list.__new__()
```



Issue created by migration from https://trac.sagemath.org/ticket/2403





---

archive/issue_comments_016227.json:
```json
{
    "body": "Attachment [2403.patch](tarball://root/attachments/some-uuid/ticket2403/2403.patch) by dfdeshom created at 2008-03-06 15:47:46",
    "created_at": "2008-03-06T15:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2403#issuecomment-16227",
    "user": "dfdeshom"
}
```

Attachment [2403.patch](tarball://root/attachments/some-uuid/ticket2403/2403.patch) by dfdeshom created at 2008-03-06 15:47:46



---

archive/issue_comments_016228.json:
```json
{
    "body": "Looks good; testall passes.",
    "created_at": "2008-03-14T01:28:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2403#issuecomment-16228",
    "user": "cwitty"
}
```

Looks good; testall passes.



---

archive/issue_comments_016229.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-14T02:31:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2403#issuecomment-16229",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.alpha0



---

archive/issue_comments_016230.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-14T02:31:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2403#issuecomment-16230",
    "user": "mabshoff"
}
```

Resolution: fixed
