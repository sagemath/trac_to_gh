# Issue 4180: magic pexpect logging switch

archive/issues_004180.json:
```json
{
    "body": "Assignee: was\n\n\n```\nYeah, I think it would greatly help if users could send an env\nvariable that dumps the pexpect communication to a file. Currently I\nhave to debug some Singular vs. pexpect problems on Solaris, but I\nguess with mhansen's help I will finally learn how to fix those\nissues. But for random users out there a magic switch that gives us\nlogs and helps us hunt down \"random\" problems would be a great thing\nIMHO.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4180\n\n",
    "created_at": "2008-09-23T22:16:39Z",
    "labels": [
        "interfaces",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "magic pexpect logging switch",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4180",
    "user": "was"
}
```
Assignee: was


```
Yeah, I think it would greatly help if users could send an env
variable that dumps the pexpect communication to a file. Currently I
have to debug some Singular vs. pexpect problems on Solaris, but I
guess with mhansen's help I will finally learn how to fix those
issues. But for random users out there a magic switch that gives us
logs and helps us hunt down "random" problems would be a great thing
IMHO.
```


Issue created by migration from https://trac.sagemath.org/ticket/4180





---

archive/issue_comments_030327.json:
```json
{
    "body": "Attachment [trac_4180.patch](tarball://root/attachments/some-uuid/ticket4180/trac_4180.patch) by mhansen created at 2008-09-24 00:14:20",
    "created_at": "2008-09-24T00:14:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4180#issuecomment-30327",
    "user": "mhansen"
}
```

Attachment [trac_4180.patch](tarball://root/attachments/some-uuid/ticket4180/trac_4180.patch) by mhansen created at 2008-09-24 00:14:20



---

archive/issue_comments_030328.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-24T00:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4180#issuecomment-30328",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030329.json:
```json
{
    "body": "I've added a patch to do this which uses the SAGE_PEXPECT_LOG environment variable.",
    "created_at": "2008-09-24T00:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4180#issuecomment-30329",
    "user": "mhansen"
}
```

I've added a patch to do this which uses the SAGE_PEXPECT_LOG environment variable.



---

archive/issue_comments_030330.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2008-09-24T00:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4180#issuecomment-30330",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_030331.json:
```json
{
    "body": "The patch looks very nice to me and will surely help us debug loads of Heisenbugs in the future. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-24T02:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4180#issuecomment-30331",
    "user": "mabshoff"
}
```

The patch looks very nice to me and will surely help us debug loads of Heisenbugs in the future. Positive review.

Cheers,

Michael



---

archive/issue_comments_030332.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha1",
    "created_at": "2008-09-24T04:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4180#issuecomment-30332",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha1



---

archive/issue_comments_030333.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-24T04:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4180#issuecomment-30333",
    "user": "mabshoff"
}
```

Resolution: fixed
