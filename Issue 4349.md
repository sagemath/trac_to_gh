# Issue 4349: jmol doesn't work on the command-line on OS X 10.5(.5)

archive/issues_004349.json:
```json
{
    "body": "Assignee: anakha\n\nIf you plot something in 3D on the command-line, buy default it pops up a jmol applet window showing the graphic (at least it did).  But now java fails to start in the sage environement.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4349\n\n",
    "created_at": "2008-10-23T17:39:38Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "jmol doesn't work on the command-line on OS X 10.5(.5)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4349",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```
Assignee: anakha

If you plot something in 3D on the command-line, buy default it pops up a jmol applet window showing the graphic (at least it did).  But now java fails to start in the sage environement.

Issue created by migration from https://trac.sagemath.org/ticket/4349





---

archive/issue_comments_031882.json:
```json
{
    "body": "Any chance you keep your OSX box uptodate with the latest Apple patches? Apple posted a borked Java update about 10 days ago that breaks all kinds of Java apps.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-23T17:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4349#issuecomment-31882",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Any chance you keep your OSX box uptodate with the latest Apple patches? Apple posted a borked Java update about 10 days ago that breaks all kinds of Java apps.

Cheers,

Michael



---

archive/issue_comments_031883.json:
```json
{
    "body": "Yes, it's always up to the latest patch",
    "created_at": "2008-10-23T17:59:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4349#issuecomment-31883",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Yes, it's always up to the latest patch



---

archive/issue_comments_031884.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-23T18:17:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4349#issuecomment-31884",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Changing status from new to assigned.



---

archive/issue_comments_031885.json:
```json
{
    "body": "Attachment [trac_4349.patch](tarball://root/attachments/some-uuid/ticket4349/trac_4349.patch) by anakha created at 2008-10-23 18:17:26\n\nFixes the bug by cleaning up the environment with sage-native-execute before calling jmol.",
    "created_at": "2008-10-23T18:17:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4349#issuecomment-31885",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Attachment [trac_4349.patch](tarball://root/attachments/some-uuid/ticket4349/trac_4349.patch) by anakha created at 2008-10-23 18:17:26

Fixes the bug by cleaning up the environment with sage-native-execute before calling jmol.



---

archive/issue_comments_031886.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-26T16:32:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4349#issuecomment-31886",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_031887.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-27T02:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4349#issuecomment-31887",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004595.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-10-27T02:10:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4349",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4349#event-4595"
}
```



---

archive/issue_comments_031888.json:
```json
{
    "body": "Merged in Sage 3.2.alpha1",
    "created_at": "2008-10-27T02:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4349#issuecomment-31888",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha1
