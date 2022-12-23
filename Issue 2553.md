# Issue 2553: dsage unit tests fail on linux

archive/issues_002553.json:
```json
{
    "body": "Assignee: yi\n\nVarious users have reported that the dsage unit tests fail on linux. This is a known issue and a fix is being worked on by me. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2553\n\n",
    "created_at": "2008-03-16T21:41:26Z",
    "labels": [
        "dsage",
        "major",
        "bug"
    ],
    "title": "dsage unit tests fail on linux",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2553",
    "user": "yi"
}
```
Assignee: yi

Various users have reported that the dsage unit tests fail on linux. This is a known issue and a fix is being worked on by me. 

Issue created by migration from https://trac.sagemath.org/ticket/2553





---

archive/issue_comments_017427.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-17T02:20:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2553#issuecomment-17427",
    "user": "yi"
}
```

Attachment



---

archive/issue_comments_017428.json:
```json
{
    "body": "This patch disables the unit tests when people run the tests using the sage-maketest script.",
    "created_at": "2008-03-17T02:21:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2553#issuecomment-17428",
    "user": "yi"
}
```

This patch disables the unit tests when people run the tests using the sage-maketest script.



---

archive/issue_comments_017429.json:
```json
{
    "body": "Attachment\n\nfixes unit tests on linux 32bit.",
    "created_at": "2008-03-23T03:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2553#issuecomment-17429",
    "user": "yi"
}
```

Attachment

fixes unit tests on linux 32bit.



---

archive/issue_comments_017430.json:
```json
{
    "body": "Attached pb_unittest.patch which should fix the unittest failures on 32bit machines.",
    "created_at": "2008-03-23T03:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2553#issuecomment-17430",
    "user": "yi"
}
```

Attached pb_unittest.patch which should fix the unittest failures on 32bit machines.



---

archive/issue_comments_017431.json:
```json
{
    "body": "pb_unittest.patch does not apply cleanly for me with 3.0.alpha1",
    "created_at": "2008-04-07T01:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2553#issuecomment-17431",
    "user": "mhansen"
}
```

pb_unittest.patch does not apply cleanly for me with 3.0.alpha1



---

archive/issue_comments_017432.json:
```json
{
    "body": "Attachment\n\nThis patch should apply cleanly against 3.0.alpha5.",
    "created_at": "2008-04-15T20:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2553#issuecomment-17432",
    "user": "yi"
}
```

Attachment

This patch should apply cleanly against 3.0.alpha5.



---

archive/issue_comments_017433.json:
```json
{
    "body": "also apply this to the scripts repo",
    "created_at": "2008-04-20T23:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2553#issuecomment-17433",
    "user": "was"
}
```

also apply this to the scripts repo



---

archive/issue_comments_017434.json:
```json
{
    "body": "Attachment\n\nREFEREE REPORT:\n\nI tested this on a bunch of platforms and it works.\n\nI read the code and it looks sane.\n\nCOMPLAINT: there is not a *single* line of documentation or comments anywhere\nthat explain why the new version works when the original didn't or what is\ngoing on.  Shame!  But I still give this a positive review so we can start\ntesting again.\n\nTO USE: Apply  pb_unittest.2.patch to hg_sage and scripts-2553.patch to hg_scripts",
    "created_at": "2008-04-20T23:25:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2553#issuecomment-17434",
    "user": "was"
}
```

Attachment

REFEREE REPORT:

I tested this on a bunch of platforms and it works.

I read the code and it looks sane.

COMPLAINT: there is not a *single* line of documentation or comments anywhere
that explain why the new version works when the original didn't or what is
going on.  Shame!  But I still give this a positive review so we can start
testing again.

TO USE: Apply  pb_unittest.2.patch to hg_sage and scripts-2553.patch to hg_scripts



---

archive/issue_comments_017435.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-04-20T23:25:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2553#issuecomment-17435",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_017436.json:
```json
{
    "body": "Merged pb_unittest.2.patch and scripts-2553.patch in Sage 3.0.rc1",
    "created_at": "2008-04-21T02:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2553#issuecomment-17436",
    "user": "mabshoff"
}
```

Merged pb_unittest.2.patch and scripts-2553.patch in Sage 3.0.rc1



---

archive/issue_comments_017437.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-21T02:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2553#issuecomment-17437",
    "user": "mabshoff"
}
```

Resolution: fixed
