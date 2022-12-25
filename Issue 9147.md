# Issue 9147: [with patch, needs review] Make sage able to compile/link with --as-needed

archive/issues_009147.json:
```json
{
    "body": "Assignee: tba\n\nWith sage-on-gentoo it is possible to compile Sage with custom CFLAGS/LDFLAGS. One common LDFLAG on gentoo is \"-Wl,--as-needed\" which has some advantages when it comes to upgrading a program's dependencies (see http://www.gentoo.org/proj/en/qa/asneeded.xml for a good explanation).\n\nThe following patch is needed to enable Sage to be compiled with --as-needed; even if one does not do so the patch should not hurt.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9147\n\n",
    "closed_at": "2010-06-05T17:37:27Z",
    "created_at": "2010-06-05T10:15:43Z",
    "labels": [
        "component: build",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, needs review] Make sage able to compile/link with --as-needed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9147",
    "user": "https://trac.sagemath.org/admin/accounts/users/cschwan"
}
```
Assignee: tba

With sage-on-gentoo it is possible to compile Sage with custom CFLAGS/LDFLAGS. One common LDFLAG on gentoo is "-Wl,--as-needed" which has some advantages when it comes to upgrading a program's dependencies (see http://www.gentoo.org/proj/en/qa/asneeded.xml for a good explanation).

The following patch is needed to enable Sage to be compiled with --as-needed; even if one does not do so the patch should not hurt.


Issue created by migration from https://trac.sagemath.org/ticket/9147





---

archive/issue_comments_085275.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-06-05T17:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9147#issuecomment-85275",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_events_022489.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-05T17:37:27Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9147",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9147#event-22489"
}
```



---

archive/issue_comments_085276.json:
```json
{
    "body": "Attachment [sage-4.4.2-enable-as-needed.patch](tarball://root/attachments/some-uuid/ticket9147/sage-4.4.2-enable-as-needed.patch) by @mwhansen created at 2010-06-05 17:37:27\n\nThis is already handled by #8844.",
    "created_at": "2010-06-05T17:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9147#issuecomment-85276",
    "user": "https://github.com/mwhansen"
}
```

Attachment [sage-4.4.2-enable-as-needed.patch](tarball://root/attachments/some-uuid/ticket9147/sage-4.4.2-enable-as-needed.patch) by @mwhansen created at 2010-06-05 17:37:27

This is already handled by #8844.



---

archive/issue_events_022490.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-05T17:37:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9147",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9147#event-22490"
}
```
