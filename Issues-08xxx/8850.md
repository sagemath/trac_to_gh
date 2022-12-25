# Issue 8850: Cython should link against BLAS instead of ATLAS on Cygwin

archive/issues_008850.json:
```json
{
    "body": "Assignee: tbd\n\nThis is the same behavior as in OS X\n\nIssue created by migration from https://trac.sagemath.org/ticket/8850\n\n",
    "closed_at": "2010-05-25T02:22:03Z",
    "created_at": "2010-05-03T12:23:21Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "Cython should link against BLAS instead of ATLAS on Cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8850",
    "user": "https://github.com/mwhansen"
}
```
Assignee: tbd

This is the same behavior as in OS X

Issue created by migration from https://trac.sagemath.org/ticket/8850





---

archive/issue_comments_081219.json:
```json
{
    "body": "Attachment [trac_8850-fix_load_cython.patch](tarball://root/attachments/some-uuid/ticket8850/trac_8850-fix_load_cython.patch) by @mwhansen created at 2010-05-03 13:16:57",
    "created_at": "2010-05-03T13:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8850#issuecomment-81219",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_8850-fix_load_cython.patch](tarball://root/attachments/some-uuid/ticket8850/trac_8850-fix_load_cython.patch) by @mwhansen created at 2010-05-03 13:16:57



---

archive/issue_comments_081220.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-03T13:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8850#issuecomment-81220",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081221.json:
```json
{
    "body": "looks fine and safe; it can't break anything.",
    "created_at": "2010-05-25T02:22:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8850#issuecomment-81221",
    "user": "https://github.com/williamstein"
}
```

looks fine and safe; it can't break anything.



---

archive/issue_events_021597.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-05-25T02:22:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8850",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8850#event-21597"
}
```



---

archive/issue_comments_081222.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-25T02:22:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8850#issuecomment-81222",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_081223.json:
```json
{
    "body": "ATLAS is faster than BLAS, so this is not an ideal solution.",
    "created_at": "2010-08-02T04:37:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8850#issuecomment-81223",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

ATLAS is faster than BLAS, so this is not an ideal solution.
