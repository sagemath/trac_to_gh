# Issue 3311: [with patch; positive review] dsage.setup() is broken in Sage 3.0.2

archive/issues_003311.json:
```json
{
    "body": "Assignee: mabshoff\n\n#3097 broke dsage.setup() since we moved dsage_setup.py and dsage_worker.py into the local/bin repo. For some reason this is neither caught by the Sage doctests now DSage unit tests.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3311\n\n",
    "closed_at": "2008-05-27T05:42:43Z",
    "created_at": "2008-05-27T02:50:46Z",
    "labels": [
        "component: dsage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "[with patch; positive review] dsage.setup() is broken in Sage 3.0.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3311",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

#3097 broke dsage.setup() since we moved dsage_setup.py and dsage_worker.py into the local/bin repo. For some reason this is neither caught by the Sage doctests now DSage unit tests.



Issue created by migration from https://trac.sagemath.org/ticket/3311





---

archive/issue_comments_022849.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-27T02:52:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3311#issuecomment-22849",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_007436.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-27T02:52:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3311",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3311#event-7436"
}
```



---

archive/issue_comments_022850.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-05-27T03:01:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3311#issuecomment-22850",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_022851.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-05-27T03:01:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3311#issuecomment-22851",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_events_007437.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-27T03:01:19Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/3311",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3311#event-7437"
}
```



---

archive/issue_comments_022852.json:
```json
{
    "body": "Attachment [trac_3311_sage.patch](tarball://root/attachments/some-uuid/ticket3311/trac_3311_sage.patch) by mabshoff created at 2008-05-27 03:18:49",
    "created_at": "2008-05-27T03:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3311#issuecomment-22852",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_3311_sage.patch](tarball://root/attachments/some-uuid/ticket3311/trac_3311_sage.patch) by mabshoff created at 2008-05-27 03:18:49



---

archive/issue_comments_022853.json:
```json
{
    "body": "Attachment [trac_3311_scripts_hgignore.patch](tarball://root/attachments/some-uuid/ticket3311/trac_3311_scripts_hgignore.patch) by mabshoff created at 2008-05-27 03:19:33",
    "created_at": "2008-05-27T03:19:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3311#issuecomment-22853",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_3311_scripts_hgignore.patch](tarball://root/attachments/some-uuid/ticket3311/trac_3311_scripts_hgignore.patch) by mabshoff created at 2008-05-27 03:19:33



---

archive/issue_comments_022854.json:
```json
{
    "body": "Attachment [trac_3311_scripts_remove_dsage.patch](tarball://root/attachments/some-uuid/ticket3311/trac_3311_scripts_remove_dsage.patch) by @williamstein created at 2008-05-27 04:07:42",
    "created_at": "2008-05-27T04:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3311#issuecomment-22854",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_3311_scripts_remove_dsage.patch](tarball://root/attachments/some-uuid/ticket3311/trac_3311_scripts_remove_dsage.patch) by @williamstein created at 2008-05-27 04:07:42



---

archive/issue_comments_022855.json:
```json
{
    "body": "Attachment [trac_3311_extcode.patch](tarball://root/attachments/some-uuid/ticket3311/trac_3311_extcode.patch) by @garyfurnish created at 2008-05-27 05:20:49",
    "created_at": "2008-05-27T05:20:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3311#issuecomment-22855",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_3311_extcode.patch](tarball://root/attachments/some-uuid/ticket3311/trac_3311_extcode.patch) by @garyfurnish created at 2008-05-27 05:20:49



---

archive/issue_comments_022856.json:
```json
{
    "body": "one liner fix to add correct system path",
    "created_at": "2008-05-27T05:39:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3311#issuecomment-22856",
    "user": "https://github.com/yqiang"
}
```

one liner fix to add correct system path



---

archive/issue_comments_022857.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-27T05:42:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3311#issuecomment-22857",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_007438.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-27T05:42:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3311",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3311#event-7438"
}
```



---

archive/issue_comments_022858.json:
```json
{
    "body": "Attachment [3311_dsage_setup.patch](tarball://root/attachments/some-uuid/ticket3311/3311_dsage_setup.patch) by mabshoff created at 2008-05-27 05:42:43\n\nMerged trac_3311* in Sage 3.0.3.alpha0",
    "created_at": "2008-05-27T05:42:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3311#issuecomment-22858",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [3311_dsage_setup.patch](tarball://root/attachments/some-uuid/ticket3311/3311_dsage_setup.patch) by mabshoff created at 2008-05-27 05:42:43

Merged trac_3311* in Sage 3.0.3.alpha0
