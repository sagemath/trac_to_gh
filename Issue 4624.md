# Issue 4624: Sage 3.2.1.a1: add ipy_profile_sage.py to list of files copied when sdisting

archive/issues_004624.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @mwhansen\n\nSigh:\n\n```\nsage-3.2.1.alpha2/spkg/standard/sage_scripts-3.2.1.alpha1$ hg stat\n! ipy_profile_sage.py\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4624\n\n",
    "created_at": "2008-11-26T14:56:24Z",
    "labels": [
        "component: distribution",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "Sage 3.2.1.a1: add ipy_profile_sage.py to list of files copied when sdisting",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4624",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @mwhansen

Sigh:

```
sage-3.2.1.alpha2/spkg/standard/sage_scripts-3.2.1.alpha1$ hg stat
! ipy_profile_sage.py
```

Issue created by migration from https://trac.sagemath.org/ticket/4624





---

archive/issue_comments_034707.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-11-26T15:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4624#issuecomment-34707",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_events_010542.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-26T15:02:34Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4624",
    "milestone": "sage-3.2.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4624#event-10542"
}
```



---

archive/issue_comments_034708.json:
```json
{
    "body": "One way to fix this is to rename the file sage-ipy_profile.py which is likely a lot less pain long term.\n\nMike: any thoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-11-26T15:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4624#issuecomment-34708",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

One way to fix this is to rename the file sage-ipy_profile.py which is likely a lot less pain long term.

Mike: any thoughts?

Cheers,

Michael



---

archive/issue_comments_034709.json:
```json
{
    "body": "This doesn't work because ipython wants it explictly named that way for looking up the profile.",
    "created_at": "2008-11-26T15:09:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4624#issuecomment-34709",
    "user": "https://github.com/mwhansen"
}
```

This doesn't work because ipython wants it explictly named that way for looking up the profile.



---

archive/issue_comments_034710.json:
```json
{
    "body": "Replying to [comment:2 mhansen]:\n> This doesn't work because ipython wants it explictly named that way for looking up the profile.\n\n\nYep, I looked at the file and I came to the same conclusion. I have \"fixed\" the issue by correcting the sage_scripts repo in the 3.2.1.a1 tarball manually for now, but will take care of this once I catch some sleep.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-26T15:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4624#issuecomment-34710",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:2 mhansen]:
> This doesn't work because ipython wants it explictly named that way for looking up the profile.


Yep, I looked at the file and I came to the same conclusion. I have "fixed" the issue by correcting the sage_scripts repo in the 3.2.1.a1 tarball manually for now, but will take care of this once I catch some sleep.

Cheers,

Michael



---

archive/issue_comments_034711.json:
```json
{
    "body": "Attachment [scripts-4624.patch](tarball://root/attachments/some-uuid/ticket4624/scripts-4624.patch) by @williamstein created at 2008-11-27 01:35:10",
    "created_at": "2008-11-27T01:35:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4624#issuecomment-34711",
    "user": "https://github.com/williamstein"
}
```

Attachment [scripts-4624.patch](tarball://root/attachments/some-uuid/ticket4624/scripts-4624.patch) by @williamstein created at 2008-11-27 01:35:10



---

archive/issue_comments_034712.json:
```json
{
    "body": "Attachment [scripts-4624-part2.patch](tarball://root/attachments/some-uuid/ticket4624/scripts-4624-part2.patch) by mabshoff created at 2008-11-27 01:41:24\n\nWith the second patch this is good to go.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T01:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4624#issuecomment-34712",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [scripts-4624-part2.patch](tarball://root/attachments/some-uuid/ticket4624/scripts-4624-part2.patch) by mabshoff created at 2008-11-27 01:41:24

With the second patch this is good to go.

Cheers,

Michael



---

archive/issue_comments_034713.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-27T02:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4624#issuecomment-34713",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_010543.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-27T02:06:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4624",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4624#event-10543"
}
```



---

archive/issue_comments_034714.json:
```json
{
    "body": "Merged both patches in Sage 3.2.1.alpha2",
    "created_at": "2008-11-27T02:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4624#issuecomment-34714",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.2.1.alpha2
