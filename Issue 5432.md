# Issue 5432: sage-combinat fixes: sage calls and qselect

archive/issues_005432.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat\n\nBug fixes:\n- Honor the SAGE_ROOT env variable to call sage\n- Removed config file handling which is now useless\n- Fixed missing default value for guards in qselect_backward_compatibility_patches\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5432\n\n",
    "created_at": "2009-03-03T23:28:24Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "sage-combinat fixes: sage calls and qselect",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5432",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat

Bug fixes:
- Honor the SAGE_ROOT env variable to call sage
- Removed config file handling which is now useless
- Fixed missing default value for guards in qselect_backward_compatibility_patches


Issue created by migration from https://trac.sagemath.org/ticket/5432





---

archive/issue_comments_041946.json:
```json
{
    "body": "Attachment [sage-combinat-fixes.patch](tarball://root/attachments/some-uuid/ticket5432/sage-combinat-fixes.patch) by @nthiery created at 2009-03-03 23:29:19",
    "created_at": "2009-03-03T23:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5432#issuecomment-41946",
    "user": "https://github.com/nthiery"
}
```

Attachment [sage-combinat-fixes.patch](tarball://root/attachments/some-uuid/ticket5432/sage-combinat-fixes.patch) by @nthiery created at 2009-03-03 23:29:19



---

archive/issue_comments_041947.json:
```json
{
    "body": "Mike,\n\ncan you review this?\n\nCheers,\n\nMichael",
    "created_at": "2009-03-04T19:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5432#issuecomment-41947",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Mike,

can you review this?

Cheers,

Michael



---

archive/issue_comments_041948.json:
```json
{
    "body": "Well, no point of shipping 3.4 with a broken combinat script, so make this a blocker :)\n\nCheers,\n\nMichael",
    "created_at": "2009-03-04T22:36:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5432#issuecomment-41948",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Well, no point of shipping 3.4 with a broken combinat script, so make this a blocker :)

Cheers,

Michael



---

archive/issue_comments_041949.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-03-04T22:36:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5432#issuecomment-41949",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_041950.json:
```json
{
    "body": "Patch applies smootly and is working for me ! I'm giving it a +1.",
    "created_at": "2009-03-04T23:15:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5432#issuecomment-41950",
    "user": "https://github.com/hivert"
}
```

Patch applies smootly and is working for me ! I'm giving it a +1.



---

archive/issue_comments_041951.json:
```json
{
    "body": "Merged in Sage 3.4.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-04T23:54:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5432#issuecomment-41951",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.rc1.

Cheers,

Michael



---

archive/issue_comments_041952.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-04T23:54:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5432#issuecomment-41952",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005684.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-04T23:54:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5432",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5432#event-5684"
}
```
