# Issue 6363: [with patch, needs review] Display Sage version on notebook login page

archive/issues_006363.json:
```json
{
    "body": "Assignee: boothby\n\nCf. [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/3e8484254e3a1cfb).\n\nIssue created by migration from https://trac.sagemath.org/ticket/6363\n\n",
    "created_at": "2009-06-20T12:21:47Z",
    "labels": [
        "notebook",
        "trivial",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "[with patch, needs review] Display Sage version on notebook login page",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6363",
    "user": "mpatel"
}
```
Assignee: boothby

Cf. [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/3e8484254e3a1cfb).

Issue created by migration from https://trac.sagemath.org/ticket/6363





---

archive/issue_comments_050908.json:
```json
{
    "body": "Attachment [trac_6363_notebook_version.patch](tarball://root/attachments/some-uuid/ticket6363/trac_6363_notebook_version.patch) by mpatel created at 2009-06-20 12:26:40",
    "created_at": "2009-06-20T12:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6363#issuecomment-50908",
    "user": "mpatel"
}
```

Attachment [trac_6363_notebook_version.patch](tarball://root/attachments/some-uuid/ticket6363/trac_6363_notebook_version.patch) by mpatel created at 2009-06-20 12:26:40



---

archive/issue_comments_050909.json:
```json
{
    "body": "The patch displays the Sage version on the notebook login page, e.g.,\n\n```\nSign into the Sage Notebook v4.0.2\n```\n\nin place of\n\n```\nSign into the Sage Notebook\n```\n",
    "created_at": "2009-06-20T12:29:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6363#issuecomment-50909",
    "user": "mpatel"
}
```

The patch displays the Sage version on the notebook login page, e.g.,

```
Sign into the Sage Notebook v4.0.2
```

in place of

```
Sign into the Sage Notebook
```




---

archive/issue_comments_050910.json:
```json
{
    "body": "Review: patch applies fine to 4.0.2 and does what it says.  I tried both from the command line (sage -notebook) and also using notebook() from Sage prompt.",
    "created_at": "2009-06-20T13:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6363#issuecomment-50910",
    "user": "cremona"
}
```

Review: patch applies fine to 4.0.2 and does what it says.  I tried both from the command line (sage -notebook) and also using notebook() from Sage prompt.



---

archive/issue_comments_050911.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T09:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6363#issuecomment-50911",
    "user": "rlm"
}
```

Resolution: fixed
