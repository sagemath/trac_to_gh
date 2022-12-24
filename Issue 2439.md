# Issue 2439: ZZ.random_element() crashes Sage with probability 2^-31

archive/issues_002439.json:
```json
{
    "body": "Assignee: cwitty\n\nZZ.random_element() does an integer divide by zero once every 2<sup>31</sup> calls.\n\nI'll make a patch as soon as my rc3 build finishes.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2439\n\n",
    "created_at": "2008-03-09T17:40:22Z",
    "labels": [
        "basic arithmetic",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "ZZ.random_element() crashes Sage with probability 2^-31",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2439",
    "user": "cwitty"
}
```
Assignee: cwitty

ZZ.random_element() does an integer divide by zero once every 2<sup>31</sup> calls.

I'll make a patch as soon as my rc3 build finishes.

Issue created by migration from https://trac.sagemath.org/ticket/2439





---

archive/issue_comments_016500.json:
```json
{
    "body": "Attachment [trac2439.patch](tarball://root/attachments/some-uuid/ticket2439/trac2439.patch) by cwitty created at 2008-03-09 18:42:43",
    "created_at": "2008-03-09T18:42:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2439#issuecomment-16500",
    "user": "cwitty"
}
```

Attachment [trac2439.patch](tarball://root/attachments/some-uuid/ticket2439/trac2439.patch) by cwitty created at 2008-03-09 18:42:43



---

archive/issue_comments_016501.json:
```json
{
    "body": "The attached patch fixes the crash, fixes other crashes in related code, and deletes some dead code.",
    "created_at": "2008-03-09T18:45:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2439#issuecomment-16501",
    "user": "cwitty"
}
```

The attached patch fixes the crash, fixes other crashes in related code, and deletes some dead code.



---

archive/issue_comments_016502.json:
```json
{
    "body": "Patch looks good to me. Good that cwitty found a very unlikely bug to hit :)",
    "created_at": "2008-03-09T19:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2439#issuecomment-16502",
    "user": "mabshoff"
}
```

Patch looks good to me. Good that cwitty found a very unlikely bug to hit :)



---

archive/issue_comments_016503.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc4",
    "created_at": "2008-03-09T19:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2439#issuecomment-16503",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc4



---

archive/issue_comments_016504.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-09T19:04:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2439#issuecomment-16504",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016505.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc4 - and this time I am closing the ticket, too.",
    "created_at": "2008-03-09T19:04:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2439#issuecomment-16505",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc4 - and this time I am closing the ticket, too.
