# Issue 6009: Bring plot/text.py to 100%

archive/issues_006009.json:
```json
{
    "body": "Assignee: mabshoff\n\nBring plot/text.py to 100%.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6009\n\n",
    "created_at": "2009-05-08T19:14:56Z",
    "labels": [
        "doctest",
        "minor",
        "enhancement"
    ],
    "title": "Bring plot/text.py to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6009",
    "user": "kcrisman"
}
```
Assignee: mabshoff

Bring plot/text.py to 100%.

Issue created by migration from https://trac.sagemath.org/ticket/6009





---

archive/issue_comments_047815.json:
```json
{
    "body": "Attachment [trac_6009.patch](tarball://root/attachments/some-uuid/ticket6009/trac_6009.patch) by kcrisman created at 2009-05-08 19:16:56",
    "created_at": "2009-05-08T19:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6009#issuecomment-47815",
    "user": "kcrisman"
}
```

Attachment [trac_6009.patch](tarball://root/attachments/some-uuid/ticket6009/trac_6009.patch) by kcrisman created at 2009-05-08 19:16:56



---

archive/issue_comments_047816.json:
```json
{
    "body": "See [http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43](http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43) for why there is no loads(dumps()) test.",
    "created_at": "2009-05-08T19:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6009#issuecomment-47816",
    "user": "kcrisman"
}
```

See [http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43](http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43) for why there is no loads(dumps()) test.



---

archive/issue_comments_047817.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-08T19:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6009#issuecomment-47817",
    "user": "kcrisman"
}
```

Changing status from new to assigned.



---

archive/issue_comments_047818.json:
```json
{
    "body": "Changing assignee from mabshoff to kcrisman.",
    "created_at": "2009-05-08T19:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6009#issuecomment-47818",
    "user": "kcrisman"
}
```

Changing assignee from mabshoff to kcrisman.



---

archive/issue_comments_047819.json:
```json
{
    "body": "Changing component from doctest to documentation.",
    "created_at": "2009-05-09T02:51:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6009#issuecomment-47819",
    "user": "kcrisman"
}
```

Changing component from doctest to documentation.



---

archive/issue_comments_047820.json:
```json
{
    "body": "reviewer patch: fix typos, add consistency to the whole module",
    "created_at": "2009-05-09T02:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6009#issuecomment-47820",
    "user": "mvngu"
}
```

reviewer patch: fix typos, add consistency to the whole module



---

archive/issue_comments_047821.json:
```json
{
    "body": "Attachment [trac_6009-reviewer.patch](tarball://root/attachments/some-uuid/ticket6009/trac_6009-reviewer.patch) by mvngu created at 2009-05-09 03:02:16\n\nREFEREE REPORT\n\n\n\nThe patch `trac_6009.patch` applies OK against the \"post-final\" sage-3.4.2, all doctests pass with the options `-t -long`. The reference manual built fine, but note that `sage/plot/text.py` is not included in the reference manual so don't be surprised when you can't search for `sage/plot/text.py` in the reference manual. The doctest coverage for `sage/plot/text.py` is 100% as claimed.\n\n\n\nHowever, I notice that the patch introduces some typos and inconsistencies into the module `sage/plot/text.py`. These are fixed in the reviewer patch `trac_6009-reviewer.patch`. Apart from these issues, positive review for kcrisman's patch. Only my patch needs to be reviewed.",
    "created_at": "2009-05-09T03:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6009#issuecomment-47821",
    "user": "mvngu"
}
```

Attachment [trac_6009-reviewer.patch](tarball://root/attachments/some-uuid/ticket6009/trac_6009-reviewer.patch) by mvngu created at 2009-05-09 03:02:16

REFEREE REPORT



The patch `trac_6009.patch` applies OK against the "post-final" sage-3.4.2, all doctests pass with the options `-t -long`. The reference manual built fine, but note that `sage/plot/text.py` is not included in the reference manual so don't be surprised when you can't search for `sage/plot/text.py` in the reference manual. The doctest coverage for `sage/plot/text.py` is 100% as claimed.



However, I notice that the patch introduces some typos and inconsistencies into the module `sage/plot/text.py`. These are fixed in the reviewer patch `trac_6009-reviewer.patch`. Apart from these issues, positive review for kcrisman's patch. Only my patch needs to be reviewed.



---

archive/issue_comments_047822.json:
```json
{
    "body": "Reviewer patch looks good.",
    "created_at": "2009-05-09T20:34:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6009#issuecomment-47822",
    "user": "jhpalmieri"
}
```

Reviewer patch looks good.



---

archive/issue_comments_047823.json:
```json
{
    "body": "Changing component from documentation to doctest.",
    "created_at": "2009-05-11T08:52:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6009#issuecomment-47823",
    "user": "mabshoff"
}
```

Changing component from documentation to doctest.



---

archive/issue_comments_047824.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-11T08:52:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6009#issuecomment-47824",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_047825.json:
```json
{
    "body": "Merged both patches in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T08:52:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6009#issuecomment-47825",
    "user": "mabshoff"
}
```

Merged both patches in Sage 4.0.alpha0.

Cheers,

Michael
