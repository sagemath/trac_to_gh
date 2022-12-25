# Issue 1958: [with patch, needs review] fix problems with ANSI codes in sage0.py

archive/issues_001958.json:
```json
{
    "body": "Assignee: @craigcitro\n\nThere were some annoying doctest failures in sage0.py in 2.10.1.rc1, which are due to weird issues with ANSI codes ending up in the result of eval(). This parses them to get the correct answer.\n\nI think there's possibly a deeper readline issue here, but that's mostly wild speculation.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1958\n\n",
    "created_at": "2008-01-28T04:36:50Z",
    "labels": [
        "component: interfaces",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch, needs review] fix problems with ANSI codes in sage0.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1958",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

There were some annoying doctest failures in sage0.py in 2.10.1.rc1, which are due to weird issues with ANSI codes ending up in the result of eval(). This parses them to get the correct answer.

I think there's possibly a deeper readline issue here, but that's mostly wild speculation.

Issue created by migration from https://trac.sagemath.org/ticket/1958





---

archive/issue_comments_012609.json:
```json
{
    "body": "Attachment [1958-sage0-fix.patch](tarball://root/attachments/some-uuid/ticket1958/1958-sage0-fix.patch) by @craigcitro created at 2008-01-28 04:39:53",
    "created_at": "2008-01-28T04:39:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1958#issuecomment-12609",
    "user": "https://github.com/craigcitro"
}
```

Attachment [1958-sage0-fix.patch](tarball://root/attachments/some-uuid/ticket1958/1958-sage0-fix.patch) by @craigcitro created at 2008-01-28 04:39:53



---

archive/issue_comments_012610.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-28T04:40:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1958#issuecomment-12610",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_012611.json:
```json
{
    "body": "There is some more info on #1942, which now has been closed as a dupe of this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-28T06:37:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1958#issuecomment-12611",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There is some more info on #1942, which now has been closed as a dupe of this ticket.

Cheers,

Michael



---

archive/issue_comments_012612.json:
```json
{
    "body": "Attachment [1958-bandaid-v2.patch](tarball://root/attachments/some-uuid/ticket1958/1958-bandaid-v2.patch) by @craigcitro created at 2008-01-28 06:50:16\n\nAttached a better band-aid for this, at wstein's suggestion.",
    "created_at": "2008-01-28T06:50:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1958#issuecomment-12612",
    "user": "https://github.com/craigcitro"
}
```

Attachment [1958-bandaid-v2.patch](tarball://root/attachments/some-uuid/ticket1958/1958-bandaid-v2.patch) by @craigcitro created at 2008-01-28 06:50:16

Attached a better band-aid for this, at wstein's suggestion.



---

archive/issue_comments_012613.json:
```json
{
    "body": "Note: you only want the second patch; it's a *replacement* for the first, not in addition to.",
    "created_at": "2008-01-28T07:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1958#issuecomment-12613",
    "user": "https://github.com/craigcitro"
}
```

Note: you only want the second patch; it's a *replacement* for the first, not in addition to.



---

archive/issue_comments_012614.json:
```json
{
    "body": "Worked for me on Fedoa 7:\n\n\n\n```\nsage -t  devel/sage-main/sage/interfaces/sage0.py           ^[[?1034h\n         [7.1 s]\n\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 7.1 seconds\n\n```\n\n\nHow about the extra escape code on each test line?",
    "created_at": "2008-01-28T11:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1958#issuecomment-12614",
    "user": "https://github.com/jaapspies"
}
```

Worked for me on Fedoa 7:



```
sage -t  devel/sage-main/sage/interfaces/sage0.py           ^[[?1034h
         [7.1 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 7.1 seconds

```


How about the extra escape code on each test line?



---

archive/issue_comments_012615.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-29T12:43:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1958#issuecomment-12615",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012616.json:
```json
{
    "body": "Merged 1958-bandaid-v2.patch in Sage 2.10.1.rc3",
    "created_at": "2008-01-29T12:43:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1958#issuecomment-12616",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 1958-bandaid-v2.patch in Sage 2.10.1.rc3
