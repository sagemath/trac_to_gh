# Issue 4624: Sage 3.2.1.a1: add ipy_profile_sage.py to list of files copied when sdisting

archive/issues_004624.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  mhansen\n\nSigh:\n\n```\nsage-3.2.1.alpha2/spkg/standard/sage_scripts-3.2.1.alpha1$ hg stat\n! ipy_profile_sage.py\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4624\n\n",
    "created_at": "2008-11-26T14:56:24Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "Sage 3.2.1.a1: add ipy_profile_sage.py to list of files copied when sdisting",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4624",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  mhansen

Sigh:

```
sage-3.2.1.alpha2/spkg/standard/sage_scripts-3.2.1.alpha1$ hg stat
! ipy_profile_sage.py
```


Issue created by migration from https://trac.sagemath.org/ticket/4624





---

archive/issue_comments_034774.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-11-26T15:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4624#issuecomment-34774",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_034775.json:
```json
{
    "body": "One way to fix this is to rename the file sage-ipy_profile.py which is likely a lot less pain long term.\n\nMike: any thoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-11-26T15:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4624#issuecomment-34775",
    "user": "mabshoff"
}
```

One way to fix this is to rename the file sage-ipy_profile.py which is likely a lot less pain long term.

Mike: any thoughts?

Cheers,

Michael



---

archive/issue_comments_034776.json:
```json
{
    "body": "This doesn't work because ipython wants it explictly named that way for looking up the profile.",
    "created_at": "2008-11-26T15:09:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4624#issuecomment-34776",
    "user": "mhansen"
}
```

This doesn't work because ipython wants it explictly named that way for looking up the profile.



---

archive/issue_comments_034777.json:
```json
{
    "body": "Replying to [comment:2 mhansen]:\n> This doesn't work because ipython wants it explictly named that way for looking up the profile.\n\nYep, I looked at the file and I came to the same conclusion. I have \"fixed\" the issue by correcting the sage_scripts repo in the 3.2.1.a1 tarball manually for now, but will take care of this once I catch some sleep.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-26T15:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4624#issuecomment-34777",
    "user": "mabshoff"
}
```

Replying to [comment:2 mhansen]:
> This doesn't work because ipython wants it explictly named that way for looking up the profile.

Yep, I looked at the file and I came to the same conclusion. I have "fixed" the issue by correcting the sage_scripts repo in the 3.2.1.a1 tarball manually for now, but will take care of this once I catch some sleep.

Cheers,

Michael



---

archive/issue_comments_034778.json:
```json
{
    "body": "Attachment [scripts-4624.patch](tarball://root/attachments/some-uuid/ticket4624/scripts-4624.patch) by was created at 2008-11-27 01:35:10",
    "created_at": "2008-11-27T01:35:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4624#issuecomment-34778",
    "user": "was"
}
```

Attachment [scripts-4624.patch](tarball://root/attachments/some-uuid/ticket4624/scripts-4624.patch) by was created at 2008-11-27 01:35:10



---

archive/issue_comments_034779.json:
```json
{
    "body": "Attachment [scripts-4624-part2.patch](tarball://root/attachments/some-uuid/ticket4624/scripts-4624-part2.patch) by mabshoff created at 2008-11-27 01:41:24\n\nWith the second patch this is good to go.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T01:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4624#issuecomment-34779",
    "user": "mabshoff"
}
```

Attachment [scripts-4624-part2.patch](tarball://root/attachments/some-uuid/ticket4624/scripts-4624-part2.patch) by mabshoff created at 2008-11-27 01:41:24

With the second patch this is good to go.

Cheers,

Michael



---

archive/issue_comments_034780.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-27T02:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4624#issuecomment-34780",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034781.json:
```json
{
    "body": "Merged both patches in Sage 3.2.1.alpha2",
    "created_at": "2008-11-27T02:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4624#issuecomment-34781",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.2.1.alpha2
