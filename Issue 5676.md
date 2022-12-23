# Issue 5676: Preparser identifies hex literals as floating point.

archive/issues_005676.json:
```json
{
    "body": "Assignee: was\n\nCC:  robertwb\n\n\n```\n    sage: 0xe\n    Traceback (most recent call last)\n    ...\n    TypeError: Unable to convert x (='0xe') to real number.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5676\n\n",
    "created_at": "2009-04-03T16:26:19Z",
    "labels": [
        "user interface",
        "blocker",
        "bug"
    ],
    "title": "Preparser identifies hex literals as floating point.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5676",
    "user": "boothby"
}
```
Assignee: was

CC:  robertwb


```
    sage: 0xe
    Traceback (most recent call last)
    ...
    TypeError: Unable to convert x (='0xe') to real number.
```


Issue created by migration from https://trac.sagemath.org/ticket/5676





---

archive/issue_comments_044405.json:
```json
{
    "body": "Unless someone is working on this I will bump it tomorrow. \n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T04:15:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5676#issuecomment-44405",
    "user": "mabshoff"
}
```

Unless someone is working on this I will bump it tomorrow. 

Cheers,

Michael



---

archive/issue_comments_044406.json:
```json
{
    "body": "I have a fix for this, I'll post a patch in 1 hour.",
    "created_at": "2009-04-15T17:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5676#issuecomment-44406",
    "user": "boothby"
}
```

I have a fix for this, I'll post a patch in 1 hour.



---

archive/issue_comments_044407.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-15T18:39:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5676#issuecomment-44407",
    "user": "boothby"
}
```

Attachment



---

archive/issue_comments_044408.json:
```json
{
    "body": "Yep, that works great.",
    "created_at": "2009-04-15T21:35:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5676#issuecomment-44408",
    "user": "robertwb"
}
```

Yep, that works great.



---

archive/issue_comments_044409.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T23:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5676#issuecomment-44409",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_comments_044410.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-15T23:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5676#issuecomment-44410",
    "user": "mabshoff"
}
```

Resolution: fixed
