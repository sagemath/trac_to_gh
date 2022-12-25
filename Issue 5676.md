# Issue 5676: Preparser identifies hex literals as floating point.

archive/issues_005676.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @robertwb\n\n\n```\n    sage: 0xe\n    Traceback (most recent call last)\n    ...\n    TypeError: Unable to convert x (='0xe') to real number.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5676\n\n",
    "created_at": "2009-04-03T16:26:19Z",
    "labels": [
        "component: user interface",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "Preparser identifies hex literals as floating point.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5676",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: @williamstein

CC:  @robertwb


```
    sage: 0xe
    Traceback (most recent call last)
    ...
    TypeError: Unable to convert x (='0xe') to real number.
```


Issue created by migration from https://trac.sagemath.org/ticket/5676





---

archive/issue_events_013348.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/boothby",
    "created_at": "2009-04-14T17:39:41Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5676",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5676#event-13348"
}
```



---

archive/issue_comments_044320.json:
```json
{
    "body": "Unless someone is working on this I will bump it tomorrow. \n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T04:15:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5676#issuecomment-44320",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Unless someone is working on this I will bump it tomorrow. 

Cheers,

Michael



---

archive/issue_comments_044321.json:
```json
{
    "body": "I have a fix for this, I'll post a patch in 1 hour.",
    "created_at": "2009-04-15T17:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5676#issuecomment-44321",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

I have a fix for this, I'll post a patch in 1 hour.



---

archive/issue_comments_044322.json:
```json
{
    "body": "Attachment [sage-5676.patch](tarball://root/attachments/some-uuid/ticket5676/sage-5676.patch) by boothby created at 2009-04-15 18:39:53",
    "created_at": "2009-04-15T18:39:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5676#issuecomment-44322",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [sage-5676.patch](tarball://root/attachments/some-uuid/ticket5676/sage-5676.patch) by boothby created at 2009-04-15 18:39:53



---

archive/issue_comments_044323.json:
```json
{
    "body": "Yep, that works great.",
    "created_at": "2009-04-15T21:35:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5676#issuecomment-44323",
    "user": "https://github.com/robertwb"
}
```

Yep, that works great.



---

archive/issue_events_013349.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-15T23:37:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5676",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5676#event-13349"
}
```



---

archive/issue_comments_044324.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T23:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5676#issuecomment-44324",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_comments_044325.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-15T23:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5676#issuecomment-44325",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
