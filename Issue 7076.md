# Issue 7076: SageNB -- Do ReST introspection on a `worksheet_process`

archive/issues_007076.json:
```json
{
    "body": "Assignee: boothby\n\nKeywords: sagenb notebook\n\nThis increases security (prevents a DoS by introspecting constantly), and ensures that it is done in a separate process (which may be in an entirely different server)\n\nIssue created by migration from https://trac.sagemath.org/ticket/7076\n\n",
    "created_at": "2009-09-29T19:48:30Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "SageNB -- Do ReST introspection on a `worksheet_process`",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7076",
    "user": "timdumol"
}
```
Assignee: boothby

Keywords: sagenb notebook

This increases security (prevents a DoS by introspecting constantly), and ensures that it is done in a separate process (which may be in an entirely different server)

Issue created by migration from https://trac.sagemath.org/ticket/7076





---

archive/issue_comments_058518.json:
```json
{
    "body": "Attachment [trac_7076-introspection-reimplementation.patch](tarball://root/attachments/some-uuid/ticket7076/trac_7076-introspection-reimplementation.patch) by timdumol created at 2009-09-29 19:49:59\n\nReimplements introspection.",
    "created_at": "2009-09-29T19:49:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7076#issuecomment-58518",
    "user": "timdumol"
}
```

Attachment [trac_7076-introspection-reimplementation.patch](tarball://root/attachments/some-uuid/ticket7076/trac_7076-introspection-reimplementation.patch) by timdumol created at 2009-09-29 19:49:59

Reimplements introspection.



---

archive/issue_comments_058519.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-29T20:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7076#issuecomment-58519",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_058520.json:
```json
{
    "body": "I've applied this to the notebook.",
    "created_at": "2009-09-29T20:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7076#issuecomment-58520",
    "user": "was"
}
```

I've applied this to the notebook.
