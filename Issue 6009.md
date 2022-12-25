# Issue 6009: Bring plot/text.py to 100%

archive/issues_006009.json:
```json
{
    "body": "Assignee: mabshoff\n\nBring plot/text.py to 100%.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6009\n\n",
    "created_at": "2009-05-08T19:14:56Z",
    "labels": [
        "component: doctest",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "Bring plot/text.py to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6009",
    "user": "https://github.com/kcrisman"
}
```
Assignee: mabshoff

Bring plot/text.py to 100%.

Issue created by migration from https://trac.sagemath.org/ticket/6009





---

archive/issue_comments_047724.json:
```json
{
    "body": "Attachment [trac_6009.patch](tarball://root/attachments/some-uuid/ticket6009/trac_6009.patch) by @kcrisman created at 2009-05-08 19:16:56",
    "created_at": "2009-05-08T19:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6009#issuecomment-47724",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_6009.patch](tarball://root/attachments/some-uuid/ticket6009/trac_6009.patch) by @kcrisman created at 2009-05-08 19:16:56



---

archive/issue_comments_047725.json:
```json
{
    "body": "See [http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43](http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43) for why there is no loads(dumps()) test.",
    "created_at": "2009-05-08T19:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6009#issuecomment-47725",
    "user": "https://github.com/kcrisman"
}
```

See [http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43](http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43) for why there is no loads(dumps()) test.



---

archive/issue_comments_047726.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-08T19:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6009#issuecomment-47726",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to assigned.



---

archive/issue_comments_047727.json:
```json
{
    "body": "Changing assignee from mabshoff to @kcrisman.",
    "created_at": "2009-05-08T19:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6009#issuecomment-47727",
    "user": "https://github.com/kcrisman"
}
```

Changing assignee from mabshoff to @kcrisman.



---

archive/issue_comments_047728.json:
```json
{
    "body": "Changing component from doctest to documentation.",
    "created_at": "2009-05-09T02:51:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6009#issuecomment-47728",
    "user": "https://github.com/kcrisman"
}
```

Changing component from doctest to documentation.



---

archive/issue_comments_047729.json:
```json
{
    "body": "reviewer patch: fix typos, add consistency to the whole module",
    "created_at": "2009-05-09T02:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6009#issuecomment-47729",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

reviewer patch: fix typos, add consistency to the whole module



---

archive/issue_comments_047730.json:
```json
{
    "body": "Attachment [trac_6009-reviewer.patch](tarball://root/attachments/some-uuid/ticket6009/trac_6009-reviewer.patch) by mvngu created at 2009-05-09 03:02:16\n\nREFEREE REPORT\n\n\n\nThe patch `trac_6009.patch` applies OK against the \"post-final\" sage-3.4.2, all doctests pass with the options `-t -long`. The reference manual built fine, but note that `sage/plot/text.py` is not included in the reference manual so don't be surprised when you can't search for `sage/plot/text.py` in the reference manual. The doctest coverage for `sage/plot/text.py` is 100% as claimed.\n\n\n\nHowever, I notice that the patch introduces some typos and inconsistencies into the module `sage/plot/text.py`. These are fixed in the reviewer patch `trac_6009-reviewer.patch`. Apart from these issues, positive review for kcrisman's patch. Only my patch needs to be reviewed.",
    "created_at": "2009-05-09T03:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6009#issuecomment-47730",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6009-reviewer.patch](tarball://root/attachments/some-uuid/ticket6009/trac_6009-reviewer.patch) by mvngu created at 2009-05-09 03:02:16

REFEREE REPORT



The patch `trac_6009.patch` applies OK against the "post-final" sage-3.4.2, all doctests pass with the options `-t -long`. The reference manual built fine, but note that `sage/plot/text.py` is not included in the reference manual so don't be surprised when you can't search for `sage/plot/text.py` in the reference manual. The doctest coverage for `sage/plot/text.py` is 100% as claimed.



However, I notice that the patch introduces some typos and inconsistencies into the module `sage/plot/text.py`. These are fixed in the reviewer patch `trac_6009-reviewer.patch`. Apart from these issues, positive review for kcrisman's patch. Only my patch needs to be reviewed.



---

archive/issue_comments_047731.json:
```json
{
    "body": "Reviewer patch looks good.",
    "created_at": "2009-05-09T20:34:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6009#issuecomment-47731",
    "user": "https://github.com/jhpalmieri"
}
```

Reviewer patch looks good.



---

archive/issue_events_014116.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-11T08:52:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6009",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6009#event-14116"
}
```



---

archive/issue_comments_047732.json:
```json
{
    "body": "Changing component from documentation to doctest.",
    "created_at": "2009-05-11T08:52:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6009#issuecomment-47732",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from documentation to doctest.



---

archive/issue_comments_047733.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-11T08:52:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6009#issuecomment-47733",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_047734.json:
```json
{
    "body": "Merged both patches in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T08:52:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6009#issuecomment-47734",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 4.0.alpha0.

Cheers,

Michael
