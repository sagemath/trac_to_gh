# Issue 2457: ideal.py doctest failure

archive/issues_002457.json:
```json
{
    "body": "Assignee: @garyfurnish\n\n\n```\nFile \"ideal.py\", line 384:\n    sage: I.is_prime()\nExpected:\n    Traceback (most recent call last):\n    ...\n    NotImplementedError\nGot:\n    True\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2457\n\n",
    "created_at": "2008-03-10T14:07:03Z",
    "labels": [
        "group theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "ideal.py doctest failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2457",
    "user": "@garyfurnish"
}
```
Assignee: @garyfurnish


```
File "ideal.py", line 384:
    sage: I.is_prime()
Expected:
    Traceback (most recent call last):
    ...
    NotImplementedError
Got:
    True
```



Issue created by migration from https://trac.sagemath.org/ticket/2457





---

archive/issue_comments_016639.json:
```json
{
    "body": "Attachment [trac_2457.patch](tarball://root/attachments/some-uuid/ticket2457/trac_2457.patch) by @garyfurnish created at 2008-03-10 14:08:33",
    "created_at": "2008-03-10T14:08:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2457#issuecomment-16639",
    "user": "@garyfurnish"
}
```

Attachment [trac_2457.patch](tarball://root/attachments/some-uuid/ticket2457/trac_2457.patch) by @garyfurnish created at 2008-03-10 14:08:33



---

archive/issue_comments_016640.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-10T14:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2457#issuecomment-16640",
    "user": "@garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016641.json:
```json
{
    "body": "This doctest did not work because 7 is in a PID and thus has an is_prime function.",
    "created_at": "2008-03-10T14:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2457#issuecomment-16641",
    "user": "@garyfurnish"
}
```

This doctest did not work because 7 is in a PID and thus has an is_prime function.



---

archive/issue_comments_016642.json:
```json
{
    "body": "Patch looks good to me and fixes the issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-10T14:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2457#issuecomment-16642",
    "user": "mabshoff"
}
```

Patch looks good to me and fixes the issue.

Cheers,

Michael



---

archive/issue_comments_016643.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-10T14:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2457#issuecomment-16643",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016644.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc4",
    "created_at": "2008-03-10T14:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2457#issuecomment-16644",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc4
