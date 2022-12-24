# Issue 3291: [with patch, needs review] pbuild doesn't properly compile mwrank.so on some systems

archive/issues_003291.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nOn some systems pbuild seems to leave out wrap.o of mwrank.so, resulting in a undefined symbol error\n\nIssue created by migration from https://trac.sagemath.org/ticket/3291\n\n",
    "created_at": "2008-05-23T22:38:03Z",
    "labels": [
        "pbuild",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "[with patch, needs review] pbuild doesn't properly compile mwrank.so on some systems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3291",
    "user": "@garyfurnish"
}
```
Assignee: @garyfurnish

On some systems pbuild seems to leave out wrap.o of mwrank.so, resulting in a undefined symbol error

Issue created by migration from https://trac.sagemath.org/ticket/3291





---

archive/issue_comments_022769.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-23T22:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3291#issuecomment-22769",
    "user": "@garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_022770.json:
```json
{
    "body": "Attachment [trac_3291_extcode.patch](tarball://root/attachments/some-uuid/ticket3291/trac_3291_extcode.patch) by @garyfurnish created at 2008-05-23 22:41:11",
    "created_at": "2008-05-23T22:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3291#issuecomment-22770",
    "user": "@garyfurnish"
}
```

Attachment [trac_3291_extcode.patch](tarball://root/attachments/some-uuid/ticket3291/trac_3291_extcode.patch) by @garyfurnish created at 2008-05-23 22:41:11



---

archive/issue_comments_022771.json:
```json
{
    "body": "The patch fixed the issue with build on Fedora 9, 32 bits, 2 cpu's\n\nJaap",
    "created_at": "2008-05-23T23:28:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3291#issuecomment-22771",
    "user": "@jaapspies"
}
```

The patch fixed the issue with build on Fedora 9, 32 bits, 2 cpu's

Jaap



---

archive/issue_comments_022772.json:
```json
{
    "body": "Merged in Sage 3.0.2.rc3",
    "created_at": "2008-05-24T00:27:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3291#issuecomment-22772",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.rc3



---

archive/issue_comments_022773.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-24T00:27:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3291#issuecomment-22773",
    "user": "mabshoff"
}
```

Resolution: fixed
