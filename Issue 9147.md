# Issue 9147: [with patch, needs review] Make sage able to compile/link with --as-needed

archive/issues_009147.json:
```json
{
    "body": "Assignee: tba\n\nWith sage-on-gentoo it is possible to compile Sage with custom CFLAGS/LDFLAGS. One common LDFLAG on gentoo is \"-Wl,--as-needed\" which has some advantages when it comes to upgrading a program's dependencies (see http://www.gentoo.org/proj/en/qa/asneeded.xml for a good explanation).\n\nThe following patch is needed to enable Sage to be compiled with --as-needed; even if one does not do so the patch should not hurt.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9147\n\n",
    "created_at": "2010-06-05T10:15:43Z",
    "labels": [
        "build",
        "minor",
        "enhancement"
    ],
    "title": "[with patch, needs review] Make sage able to compile/link with --as-needed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9147",
    "user": "cschwan"
}
```
Assignee: tba

With sage-on-gentoo it is possible to compile Sage with custom CFLAGS/LDFLAGS. One common LDFLAG on gentoo is "-Wl,--as-needed" which has some advantages when it comes to upgrading a program's dependencies (see http://www.gentoo.org/proj/en/qa/asneeded.xml for a good explanation).

The following patch is needed to enable Sage to be compiled with --as-needed; even if one does not do so the patch should not hurt.


Issue created by migration from https://trac.sagemath.org/ticket/9147





---

archive/issue_comments_085412.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-06-05T17:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9147#issuecomment-85412",
    "user": "mhansen"
}
```

Resolution: invalid



---

archive/issue_comments_085413.json:
```json
{
    "body": "Attachment\n\nThis is already handled by #8844.",
    "created_at": "2010-06-05T17:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9147#issuecomment-85413",
    "user": "mhansen"
}
```

Attachment

This is already handled by #8844.
