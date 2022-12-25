# Issue 2376: [with patch, needs review] Sage 2.10.3.rc1: various doctest failure in abvar

archive/issues_002376.json:
```json
{
    "body": "Assignee: failure\n\nWe have various doctest failures in\n\n```\nsage -t -long devel/sage-main/sage/modular/abvar/abvar.py\nsage -t -long devel/sage-main/sage/modular/abvar/finite_subgroup.py\nsage -t -long devel/sage-main/sage/modular/abvar/torsion_subgroup.py\n```\n\n\nThe attached patch fixes those.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2376\n\n",
    "created_at": "2008-03-03T16:54:38Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "[with patch, needs review] Sage 2.10.3.rc1: various doctest failure in abvar",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2376",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: failure

We have various doctest failures in

```
sage -t -long devel/sage-main/sage/modular/abvar/abvar.py
sage -t -long devel/sage-main/sage/modular/abvar/finite_subgroup.py
sage -t -long devel/sage-main/sage/modular/abvar/torsion_subgroup.py
```


The attached patch fixes those.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2376





---

archive/issue_comments_015995.json:
```json
{
    "body": "Changing assignee from failure to mabshoff.",
    "created_at": "2008-03-03T16:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2376#issuecomment-15995",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from failure to mabshoff.



---

archive/issue_comments_015996.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-03T16:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2376#issuecomment-15996",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015997.json:
```json
{
    "body": "Attachment [trac_2376.patch](tarball://root/attachments/some-uuid/ticket2376/trac_2376.patch) by mabshoff created at 2008-03-03 17:01:31",
    "created_at": "2008-03-03T17:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2376#issuecomment-15997",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_2376.patch](tarball://root/attachments/some-uuid/ticket2376/trac_2376.patch) by mabshoff created at 2008-03-03 17:01:31



---

archive/issue_comments_015998.json:
```json
{
    "body": "Looks great!",
    "created_at": "2008-03-03T17:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2376#issuecomment-15998",
    "user": "https://github.com/williamstein"
}
```

Looks great!



---

archive/issue_events_002553.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-03T17:21:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2376",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2376#event-2553"
}
```



---

archive/issue_comments_015999.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-03T17:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2376#issuecomment-15999",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016000.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc1",
    "created_at": "2008-03-03T17:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2376#issuecomment-16000",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc1



---

archive/issue_comments_016001.json:
```json
{
    "body": "Attachment [trac_2376-2.patch](tarball://root/attachments/some-uuid/ticket2376/trac_2376-2.patch) by mabshoff created at 2008-03-03 19:21:56\n\nI just attached another trivial, \"obviously\" correct doctest fix related to trac-2245-lseries.patch to this ticket. It has already been merged, but feel free to review it.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-03T19:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2376#issuecomment-16001",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_2376-2.patch](tarball://root/attachments/some-uuid/ticket2376/trac_2376-2.patch) by mabshoff created at 2008-03-03 19:21:56

I just attached another trivial, "obviously" correct doctest fix related to trac-2245-lseries.patch to this ticket. It has already been merged, but feel free to review it.

Cheers,

Michael
