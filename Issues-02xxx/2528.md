# Issue 2528: [with patch; positive review] File sage/modular/dims_doc.py should be removed soon

archive/issues_002528.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis file existed for only including certain parts of dims.py into the reference manual; this is no longer necessary, and the file should be removed. Care needs to be taken to not break the reference manual -- William has a fix that he's going to submit when I post this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2528\n\n",
    "closed_at": "2008-03-15T22:30:07Z",
    "created_at": "2008-03-15T05:53:18Z",
    "labels": [
        "component: modular forms",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "[with patch; positive review] File sage/modular/dims_doc.py should be removed soon",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2528",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @williamstein

This file existed for only including certain parts of dims.py into the reference manual; this is no longer necessary, and the file should be removed. Care needs to be taken to not break the reference manual -- William has a fix that he's going to submit when I post this.

Issue created by migration from https://trac.sagemath.org/ticket/2528





---

archive/issue_comments_017206.json:
```json
{
    "body": "Attachment [doc-2528.patch](tarball://root/attachments/some-uuid/ticket2528/doc-2528.patch) by @williamstein created at 2008-03-15 06:47:43",
    "created_at": "2008-03-15T06:47:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2528#issuecomment-17206",
    "user": "https://github.com/williamstein"
}
```

Attachment [doc-2528.patch](tarball://root/attachments/some-uuid/ticket2528/doc-2528.patch) by @williamstein created at 2008-03-15 06:47:43



---

archive/issue_comments_017207.json:
```json
{
    "body": "Attachment [trac-2528.patch](tarball://root/attachments/some-uuid/ticket2528/trac-2528.patch) by @craigcitro created at 2008-03-15 08:44:22",
    "created_at": "2008-03-15T08:44:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2528#issuecomment-17207",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-2528.patch](tarball://root/attachments/some-uuid/ticket2528/trac-2528.patch) by @craigcitro created at 2008-03-15 08:44:22



---

archive/issue_comments_017208.json:
```json
{
    "body": "The second patch applies against the main repository, and removes the file in the title.",
    "created_at": "2008-03-15T08:45:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2528#issuecomment-17208",
    "user": "https://github.com/craigcitro"
}
```

The second patch applies against the main repository, and removes the file in the title.



---

archive/issue_comments_017209.json:
```json
{
    "body": "Somebody has been sneaking an extra hunk in trac-2528.patch. The first hunk has a merge conflict, which I cannot see [maybe white space?], but I ended up merging that hunk manually.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-15T22:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2528#issuecomment-17209",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Somebody has been sneaking an extra hunk in trac-2528.patch. The first hunk has a merge conflict, which I cannot see [maybe white space?], but I ended up merging that hunk manually.

Cheers,

Michael



---

archive/issue_comments_017210.json:
```json
{
    "body": "Actually, it's not an extra hunk -- I'm moving comments that were in `dims_doc.py` into `dims.py` so that they're not lost. Maybe I should have mentioned that more explicitly.",
    "created_at": "2008-03-15T22:07:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2528#issuecomment-17210",
    "user": "https://github.com/craigcitro"
}
```

Actually, it's not an extra hunk -- I'm moving comments that were in `dims_doc.py` into `dims.py` so that they're not lost. Maybe I should have mentioned that more explicitly.



---

archive/issue_comments_017211.json:
```json
{
    "body": "Replying to [comment:5 craigcitro]:\n> Actually, it's not an extra hunk -- I'm moving comments that were in `dims_doc.py` into `dims.py` so that they're not lost. Maybe I should have mentioned that more explicitly.\n> \n\n\nEither way, it is fixed :)\n\nCheers,\n\nMichael",
    "created_at": "2008-03-15T22:29:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2528#issuecomment-17211",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:5 craigcitro]:
> Actually, it's not an extra hunk -- I'm moving comments that were in `dims_doc.py` into `dims.py` so that they're not lost. Maybe I should have mentioned that more explicitly.
> 


Either way, it is fixed :)

Cheers,

Michael



---

archive/issue_comments_017212.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-15T22:30:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2528#issuecomment-17212",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005929.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-15T22:30:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2528",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2528#event-5929"
}
```



---

archive/issue_comments_017213.json:
```json
{
    "body": "Merged in Sage 2.10.4.rc0",
    "created_at": "2008-03-15T22:30:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2528#issuecomment-17213",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.4.rc0
