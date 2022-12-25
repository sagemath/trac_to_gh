# Issue 6856: cancel button in notebook user settings not working

archive/issues_006856.json:
```json
{
    "body": "Assignee: boothby\n\nThe cancel button in the 'Settings' page of a notebook user is not working because of a missing 'username' template argument to `account_settings.html`. (There's a redirect to a broken path when pressing the button now.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/6856\n\n",
    "created_at": "2009-09-01T15:09:35Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "cancel button in notebook user settings not working",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6856",
    "user": "https://github.com/wjp"
}
```
Assignee: boothby

The cancel button in the 'Settings' page of a notebook user is not working because of a missing 'username' template argument to `account_settings.html`. (There's a redirect to a broken path when pressing the button now.)

Issue created by migration from https://trac.sagemath.org/ticket/6856





---

archive/issue_comments_056444.json:
```json
{
    "body": "Attachment [trac_6856-fix_account_settings_cancel.patch](tarball://root/attachments/some-uuid/ticket6856/trac_6856-fix_account_settings_cancel.patch) by @wjp created at 2009-09-01 15:11:55",
    "created_at": "2009-09-01T15:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6856#issuecomment-56444",
    "user": "https://github.com/wjp"
}
```

Attachment [trac_6856-fix_account_settings_cancel.patch](tarball://root/attachments/some-uuid/ticket6856/trac_6856-fix_account_settings_cancel.patch) by @wjp created at 2009-09-01 15:11:55



---

archive/issue_comments_056445.json:
```json
{
    "body": "To reproduce, log in to the notebook, press 'Settings' at the top right, and then press 'Cancel'.",
    "created_at": "2009-09-01T15:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6856#issuecomment-56445",
    "user": "https://github.com/wjp"
}
```

To reproduce, log in to the notebook, press 'Settings' at the top right, and then press 'Cancel'.



---

archive/issue_comments_056446.json:
```json
{
    "body": "A one-line patch that fixes the problem! Positive review.",
    "created_at": "2009-09-01T23:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6856#issuecomment-56446",
    "user": "https://github.com/dandrake"
}
```

A one-line patch that fixes the problem! Positive review.



---

archive/issue_comments_056447.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-03T07:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6856#issuecomment-56447",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_007089.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-09-03T07:03:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6856",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6856#event-7089"
}
```
