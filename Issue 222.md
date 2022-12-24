# Issue 222: field mutability issue

archive/issues_000222.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\ncwitty: Yuck:\n[10:48pm] cwitty: sage: RS = RealField(sci_not=True)\n[10:48pm] cwitty: sage: R == RS\n[10:48pm] cwitty: sage: RS.scientific_notation(False)\n[10:48pm] cwitty: sage: RR == RS\n[10:48pm] cwitty: (Oops... second line should be \"RR == RS\")\n[10:49pm] cwitty: Second line prints False, fourth line prints True.  Shouldn't fields be immutable?\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/222\n\n",
    "created_at": "2007-01-26T07:09:28Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "field mutability issue",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/222",
    "user": "was"
}
```
Assignee: somebody


```
cwitty: Yuck:
[10:48pm] cwitty: sage: RS = RealField(sci_not=True)
[10:48pm] cwitty: sage: R == RS
[10:48pm] cwitty: sage: RS.scientific_notation(False)
[10:48pm] cwitty: sage: RR == RS
[10:48pm] cwitty: (Oops... second line should be "RR == RS")
[10:49pm] cwitty: Second line prints False, fourth line prints True.  Shouldn't fields be immutable?
```


Issue created by migration from https://trac.sagemath.org/ticket/222





---

archive/issue_comments_000991.json:
```json
{
    "body": "\n```\n\n\n```\n",
    "created_at": "2007-10-21T02:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/222#issuecomment-991",
    "user": "was"
}
```


```


```




---

archive/issue_comments_000992.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-21T02:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/222#issuecomment-992",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_000993.json:
```json
{
    "body": "Attachment [trac222.patch](tarball://root/attachments/some-uuid/ticket222/trac222.patch) by mabshoff created at 2007-10-22 00:03:54",
    "created_at": "2007-10-22T00:03:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/222#issuecomment-993",
    "user": "mabshoff"
}
```

Attachment [trac222.patch](tarball://root/attachments/some-uuid/ticket222/trac222.patch) by mabshoff created at 2007-10-22 00:03:54
