# Issue 6856: cancel button in notebook user settings not working

archive/issues_006856.json:
```json
{
    "body": "Assignee: boothby\n\nThe cancel button in the 'Settings' page of a notebook user is not working because of a missing 'username' template argument to `account_settings.html`. (There's a redirect to a broken path when pressing the button now.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/6856\n\n",
    "created_at": "2009-09-01T15:09:35Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "cancel button in notebook user settings not working",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6856",
    "user": "wjp"
}
```
Assignee: boothby

The cancel button in the 'Settings' page of a notebook user is not working because of a missing 'username' template argument to `account_settings.html`. (There's a redirect to a broken path when pressing the button now.)

Issue created by migration from https://trac.sagemath.org/ticket/6856





---

archive/issue_comments_056548.json:
```json
{
    "body": "Attachment [trac_6856-fix_account_settings_cancel.patch](tarball://root/attachments/some-uuid/ticket6856/trac_6856-fix_account_settings_cancel.patch) by wjp created at 2009-09-01 15:11:55",
    "created_at": "2009-09-01T15:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6856#issuecomment-56548",
    "user": "wjp"
}
```

Attachment [trac_6856-fix_account_settings_cancel.patch](tarball://root/attachments/some-uuid/ticket6856/trac_6856-fix_account_settings_cancel.patch) by wjp created at 2009-09-01 15:11:55



---

archive/issue_comments_056549.json:
```json
{
    "body": "To reproduce, log in to the notebook, press 'Settings' at the top right, and then press 'Cancel'.",
    "created_at": "2009-09-01T15:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6856#issuecomment-56549",
    "user": "wjp"
}
```

To reproduce, log in to the notebook, press 'Settings' at the top right, and then press 'Cancel'.



---

archive/issue_comments_056550.json:
```json
{
    "body": "A one-line patch that fixes the problem! Positive review.",
    "created_at": "2009-09-01T23:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6856#issuecomment-56550",
    "user": "ddrake"
}
```

A one-line patch that fixes the problem! Positive review.



---

archive/issue_comments_056551.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-03T07:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6856#issuecomment-56551",
    "user": "mvngu"
}
```

Resolution: fixed
