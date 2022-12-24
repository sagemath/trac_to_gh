# Issue 2376: [with patch, needs review] Sage 2.10.3.rc1: various doctest failure in abvar

archive/issues_002376.json:
```json
{
    "body": "Assignee: failure\n\nWe have various doctest failures in\n\n```\nsage -t -long devel/sage-main/sage/modular/abvar/abvar.py\nsage -t -long devel/sage-main/sage/modular/abvar/finite_subgroup.py\nsage -t -long devel/sage-main/sage/modular/abvar/torsion_subgroup.py\n```\n\n\nThe attached patch fixes those.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2376\n\n",
    "created_at": "2008-03-03T16:54:38Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "[with patch, needs review] Sage 2.10.3.rc1: various doctest failure in abvar",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2376",
    "user": "mabshoff"
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

archive/issue_comments_016030.json:
```json
{
    "body": "Changing assignee from failure to mabshoff.",
    "created_at": "2008-03-03T16:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2376#issuecomment-16030",
    "user": "mabshoff"
}
```

Changing assignee from failure to mabshoff.



---

archive/issue_comments_016031.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-03T16:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2376#issuecomment-16031",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016032.json:
```json
{
    "body": "Attachment [trac_2376.patch](tarball://root/attachments/some-uuid/ticket2376/trac_2376.patch) by mabshoff created at 2008-03-03 17:01:31",
    "created_at": "2008-03-03T17:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2376#issuecomment-16032",
    "user": "mabshoff"
}
```

Attachment [trac_2376.patch](tarball://root/attachments/some-uuid/ticket2376/trac_2376.patch) by mabshoff created at 2008-03-03 17:01:31



---

archive/issue_comments_016033.json:
```json
{
    "body": "Looks great!",
    "created_at": "2008-03-03T17:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2376#issuecomment-16033",
    "user": "was"
}
```

Looks great!



---

archive/issue_comments_016034.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-03T17:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2376#issuecomment-16034",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016035.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc1",
    "created_at": "2008-03-03T17:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2376#issuecomment-16035",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc1



---

archive/issue_comments_016036.json:
```json
{
    "body": "Attachment [trac_2376-2.patch](tarball://root/attachments/some-uuid/ticket2376/trac_2376-2.patch) by mabshoff created at 2008-03-03 19:21:56\n\nI just attached another trivial, \"obviously\" correct doctest fix related to trac-2245-lseries.patch to this ticket. It has already been merged, but feel free to review it.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-03T19:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2376#issuecomment-16036",
    "user": "mabshoff"
}
```

Attachment [trac_2376-2.patch](tarball://root/attachments/some-uuid/ticket2376/trac_2376-2.patch) by mabshoff created at 2008-03-03 19:21:56

I just attached another trivial, "obviously" correct doctest fix related to trac-2245-lseries.patch to this ticket. It has already been merged, but feel free to review it.

Cheers,

Michael
