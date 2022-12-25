# Issue 4150: [with patch, positive review] migrate graphs to new refinement code

archive/issues_004150.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @jasongrout\n\nThis moves the automorphism group and isomorphism functions for graphs over to the new framework. It should be tested on a few different architectures before getting merged.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4150\n\n",
    "closed_at": "2008-09-19T23:55:39Z",
    "created_at": "2008-09-19T07:42:32Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "[with patch, positive review] migrate graphs to new refinement code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4150",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill

CC:  @jasongrout

This moves the automorphism group and isomorphism functions for graphs over to the new framework. It should be tested on a few different architectures before getting merged.

Issue created by migration from https://trac.sagemath.org/ticket/4150





---

archive/issue_comments_030069.json:
```json
{
    "body": "Attachment [trac_4150-switchover-graphs.patch](tarball://root/attachments/some-uuid/ticket4150/trac_4150-switchover-graphs.patch) by @rlmill created at 2008-09-19 07:43:20",
    "created_at": "2008-09-19T07:43:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4150#issuecomment-30069",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_4150-switchover-graphs.patch](tarball://root/attachments/some-uuid/ticket4150/trac_4150-switchover-graphs.patch) by @rlmill created at 2008-09-19 07:43:20



---

archive/issue_comments_030070.json:
```json
{
    "body": "Dependends on #4115, if you're applying to 3.1.2.final",
    "created_at": "2008-09-19T07:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4150#issuecomment-30070",
    "user": "https://github.com/rlmill"
}
```

Dependends on #4115, if you're applying to 3.1.2.final



---

archive/issue_comments_030071.json:
```json
{
    "body": "Positive review for Robert's part.  He just needs to sign off on my small second patch.",
    "created_at": "2008-09-19T08:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4150#issuecomment-30071",
    "user": "https://github.com/mwhansen"
}
```

Positive review for Robert's part.  He just needs to sign off on my small second patch.



---

archive/issue_comments_030072.json:
```json
{
    "body": "+1",
    "created_at": "2008-09-19T08:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4150#issuecomment-30072",
    "user": "https://github.com/rlmill"
}
```

+1



---

archive/issue_comments_030073.json:
```json
{
    "body": "Note that the second patch depends on #4139 being applied.",
    "created_at": "2008-09-19T08:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4150#issuecomment-30073",
    "user": "https://github.com/mwhansen"
}
```

Note that the second patch depends on #4139 being applied.



---

archive/issue_comments_030074.json:
```json
{
    "body": "The first hunk from trac_4150-fixes.patch ought to be deleted since I ended up fixing that doctest failure at #4139.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-19T14:50:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4150#issuecomment-30074",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The first hunk from trac_4150-fixes.patch ought to be deleted since I ended up fixing that doctest failure at #4139.

Cheers,

Michael



---

archive/issue_comments_030075.json:
```json
{
    "body": "Attachment [trac_4150-fixes.patch](tarball://root/attachments/some-uuid/ticket4150/trac_4150-fixes.patch) by @rlmill created at 2008-09-19 14:54:01\n\nPatch fixed.",
    "created_at": "2008-09-19T14:54:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4150#issuecomment-30075",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_4150-fixes.patch](tarball://root/attachments/some-uuid/ticket4150/trac_4150-fixes.patch) by @rlmill created at 2008-09-19 14:54:01

Patch fixed.



---

archive/issue_comments_030076.json:
```json
{
    "body": "Thanks, valgrinds clean and also works on Itanium with Python build with `-fwrapv`, which caused trouble with the old codebase, so what could go wrong :)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-19T23:52:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4150#issuecomment-30076",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Thanks, valgrinds clean and also works on Itanium with Python build with `-fwrapv`, which caused trouble with the old codebase, so what could go wrong :)

Cheers,

Michael



---

archive/issue_comments_030077.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-19T23:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4150#issuecomment-30077",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030078.json:
```json
{
    "body": "Merged both patches in Sage 3.1.3.alpha0",
    "created_at": "2008-09-19T23:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4150#issuecomment-30078",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.1.3.alpha0



---

archive/issue_events_009441.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-19T23:55:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4150",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4150#event-9441"
}
```
