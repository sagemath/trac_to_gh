# Issue 2661: sage cannot compute floor / ceil of log(8)/log(2)

archive/issues_002661.json:
```json
{
    "body": "Assignee: was\n\nThis happens because the interval remains centered around an integer.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2661\n\n",
    "created_at": "2008-03-24T20:13:01Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "sage cannot compute floor / ceil of log(8)/log(2)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2661",
    "user": "mhansen"
}
```
Assignee: was

This happens because the interval remains centered around an integer.

Issue created by migration from https://trac.sagemath.org/ticket/2661





---

archive/issue_comments_018319.json:
```json
{
    "body": "Some concerns about this were raised on IRC.  It seems that the real problem is telling if log(8)/log(2) is an integer.  The (log(8)/log(2)).simplify_log() function tells us that this is 3.",
    "created_at": "2008-03-24T21:12:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2661#issuecomment-18319",
    "user": "jason"
}
```

Some concerns about this were raised on IRC.  It seems that the real problem is telling if log(8)/log(2) is an integer.  The (log(8)/log(2)).simplify_log() function tells us that this is 3.



---

archive/issue_comments_018320.json:
```json
{
    "body": "Attachment [2661.patch](tarball://root/attachments/some-uuid/ticket2661/2661.patch) by jason created at 2008-03-24 21:26:49\n\nlooks good to me.",
    "created_at": "2008-03-24T21:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2661#issuecomment-18320",
    "user": "jason"
}
```

Attachment [2661.patch](tarball://root/attachments/some-uuid/ticket2661/2661.patch) by jason created at 2008-03-24 21:26:49

looks good to me.



---

archive/issue_comments_018321.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-25T04:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2661#issuecomment-18321",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018322.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-25T04:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2661#issuecomment-18322",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha2
