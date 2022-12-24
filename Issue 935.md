# Issue 935: remove no longer present files from the sage repo

archive/issues_000935.json:
```json
{
    "body": "Assignee: was\n\nWell, the title says it all. Patch is against 2.8.7.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/935\n\n",
    "created_at": "2007-10-19T22:56:39Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.10",
    "title": "remove no longer present files from the sage repo",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/935",
    "user": "mabshoff"
}
```
Assignee: was

Well, the title says it all. Patch is against 2.8.7.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/935





---

archive/issue_comments_005704.json:
```json
{
    "body": "Attachment [sage-2.8.7-remove-deleted-files-from-repo.patch](tarball://root/attachments/some-uuid/ticket935/sage-2.8.7-remove-deleted-files-from-repo.patch) by mabshoff created at 2007-10-19 22:57:11",
    "created_at": "2007-10-19T22:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/935#issuecomment-5704",
    "user": "mabshoff"
}
```

Attachment [sage-2.8.7-remove-deleted-files-from-repo.patch](tarball://root/attachments/some-uuid/ticket935/sage-2.8.7-remove-deleted-files-from-repo.patch) by mabshoff created at 2007-10-19 22:57:11



---

archive/issue_comments_005705.json:
```json
{
    "body": "Changing assignee from was to mabshoff.",
    "created_at": "2007-10-20T06:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/935#issuecomment-5705",
    "user": "mabshoff"
}
```

Changing assignee from was to mabshoff.



---

archive/issue_comments_005706.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-20T06:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/935#issuecomment-5706",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005707.json:
```json
{
    "body": "\n```\n[21:20] <wstein> #935 -- reject.\n[21:20] <mabshoff> Why?\n[21:20] <wstein> Those files *should* be in sage.\n[21:20] <mabshoff> So why aren't they in the repo?\n[21:20] <wstein> probably they didn't get included because of a mistake in MANIFEST.in.\n[21:20] <mabshoff> ok\n[21:21] <mabshoff> So mark #935 as invalid?\n[21:21] <wstein> at least the one that doctests cvxopt, scipy, definitely should be remade.\n[21:21] <mabshoff> That is another ticket.\n[21:21] <wstein> It's not invalid, it's just that the fix isn't exactly right.\n```\n",
    "created_at": "2007-10-20T19:25:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/935#issuecomment-5707",
    "user": "mabshoff"
}
```


```
[21:20] <wstein> #935 -- reject.
[21:20] <mabshoff> Why?
[21:20] <wstein> Those files *should* be in sage.
[21:20] <mabshoff> So why aren't they in the repo?
[21:20] <wstein> probably they didn't get included because of a mistake in MANIFEST.in.
[21:20] <mabshoff> ok
[21:21] <mabshoff> So mark #935 as invalid?
[21:21] <wstein> at least the one that doctests cvxopt, scipy, definitely should be remade.
[21:21] <mabshoff> That is another ticket.
[21:21] <wstein> It's not invalid, it's just that the fix isn't exactly right.
```




---

archive/issue_comments_005708.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-10-21T01:05:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/935#issuecomment-5708",
    "user": "was"
}
```

Resolution: invalid



---

archive/issue_comments_005709.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2007-10-28T16:07:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/935#issuecomment-5709",
    "user": "cwitty"
}
```

Resolution changed from invalid to 



---

archive/issue_comments_005710.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-10-28T16:07:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/935#issuecomment-5710",
    "user": "cwitty"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_005711.json:
```json
{
    "body": "Changing status from reopened to new.",
    "created_at": "2007-10-28T16:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/935#issuecomment-5711",
    "user": "cwitty"
}
```

Changing status from reopened to new.



---

archive/issue_comments_005712.json:
```json
{
    "body": "Changing assignee from mabshoff to cwitty.",
    "created_at": "2007-10-28T16:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/935#issuecomment-5712",
    "user": "cwitty"
}
```

Changing assignee from mabshoff to cwitty.



---

archive/issue_comments_005713.json:
```json
{
    "body": "Attachment [935.patch](tarball://root/attachments/some-uuid/ticket935/935.patch) by cwitty created at 2007-10-28 17:48:58",
    "created_at": "2007-10-28T17:48:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/935#issuecomment-5713",
    "user": "cwitty"
}
```

Attachment [935.patch](tarball://root/attachments/some-uuid/ticket935/935.patch) by cwitty created at 2007-10-28 17:48:58



---

archive/issue_comments_005714.json:
```json
{
    "body": "I think the attached patch should fix this problem.  (I will close the ticket once I have actually built a distribution and checked that it worked.)",
    "created_at": "2007-10-28T17:49:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/935#issuecomment-5714",
    "user": "cwitty"
}
```

I think the attached patch should fix this problem.  (I will close the ticket once I have actually built a distribution and checked that it worked.)



---

archive/issue_comments_005715.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-28T21:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/935#issuecomment-5715",
    "user": "cwitty"
}
```

Resolution: fixed
