# Issue 5215: [with patch, needs review] Remove ipython1-20070130.spkg from Sage

archive/issues_005215.json:
```json
{
    "body": "Assignee: mabshoff\n\nipython1-20070130.spkg is very outdated and since ipython 0.9.0 the functionality has been migrated into ipython itself. Since we are now shipping ipython 0.9.1 remove the ipython1-20070130.spkg from the Sage distribution. Besides deleting the spkg one also needs to change deps and install.\n\nI will post diff for deps and install momentarily.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5215\n\n",
    "created_at": "2009-02-09T12:20:24Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] Remove ipython1-20070130.spkg from Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5215",
    "user": "mabshoff"
}
```
Assignee: mabshoff

ipython1-20070130.spkg is very outdated and since ipython 0.9.0 the functionality has been migrated into ipython itself. Since we are now shipping ipython 0.9.1 remove the ipython1-20070130.spkg from the Sage distribution. Besides deleting the spkg one also needs to change deps and install.

I will post diff for deps and install momentarily.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5215





---

archive/issue_comments_039955.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-09T12:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5215#issuecomment-39955",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039956.json:
```json
{
    "body": "Attachment [trac_5215_deps.patch](tarball://root/attachments/some-uuid/ticket5215/trac_5215_deps.patch) by mabshoff created at 2009-02-11 04:37:53",
    "created_at": "2009-02-11T04:37:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5215#issuecomment-39956",
    "user": "mabshoff"
}
```

Attachment [trac_5215_deps.patch](tarball://root/attachments/some-uuid/ticket5215/trac_5215_deps.patch) by mabshoff created at 2009-02-11 04:37:53



---

archive/issue_comments_039957.json:
```json
{
    "body": "Attachment [trac_5215_install.patch](tarball://root/attachments/some-uuid/ticket5215/trac_5215_install.patch) by @mwhansen created at 2009-02-11 05:48:38\n\nLooks good.  Hurray for removing cruft!",
    "created_at": "2009-02-11T05:48:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5215#issuecomment-39957",
    "user": "@mwhansen"
}
```

Attachment [trac_5215_install.patch](tarball://root/attachments/some-uuid/ticket5215/trac_5215_install.patch) by @mwhansen created at 2009-02-11 05:48:38

Looks good.  Hurray for removing cruft!



---

archive/issue_comments_039958.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-11T06:10:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5215#issuecomment-39958",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039959.json:
```json
{
    "body": "(Un)Merged in Sage 3.3.rc0 :)\n\nCheers,\n\nMichael",
    "created_at": "2009-02-11T06:10:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5215#issuecomment-39959",
    "user": "mabshoff"
}
```

(Un)Merged in Sage 3.3.rc0 :)

Cheers,

Michael
