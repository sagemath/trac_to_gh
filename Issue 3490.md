# Issue 3490: notebook -- improve registration error checking and reporting

archive/issues_003490.json:
```json
{
    "body": "Assignee: boothby\n\nKeywords: editor_wstein\n\nThis is a follow up to #3483.\n\nis_valid_username should be upgraded to follow this rule:\n\n```\nYour username must start with a letter and be between 4 and 32 characters long. You may only use letters, numbers, underscores, and one dot (.).\n```\n\n\nA new function, is_valid_password, should be added that follows this rule:\n\n```\nYour password must be between 6 and 32 characters long. Your password can not contain your username nor spaces.\n```\n\n\nCheck to make sure the input for password and retype_password are the same.\n\nCurrently only one error is reported even if there is several of them. Report all errors to the user.\n\nDon't loose the user's input except for password/retype_password when returning error reports.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3490\n\n",
    "created_at": "2008-06-21T04:48:49Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "notebook -- improve registration error checking and reporting",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3490",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```
Assignee: boothby

Keywords: editor_wstein

This is a follow up to #3483.

is_valid_username should be upgraded to follow this rule:

```
Your username must start with a letter and be between 4 and 32 characters long. You may only use letters, numbers, underscores, and one dot (.).
```


A new function, is_valid_password, should be added that follows this rule:

```
Your password must be between 6 and 32 characters long. Your password can not contain your username nor spaces.
```


Check to make sure the input for password and retype_password are the same.

Currently only one error is reported even if there is several of them. Report all errors to the user.

Don't loose the user's input except for password/retype_password when returning error reports.

Issue created by migration from https://trac.sagemath.org/ticket/3490





---

archive/issue_comments_024536.json:
```json
{
    "body": "Attachment [sage-3490.patch](tarball://root/attachments/some-uuid/ticket3490/sage-3490.patch) by TimothyClemans created at 2008-06-23 20:55:52",
    "created_at": "2008-06-23T20:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3490#issuecomment-24536",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [sage-3490.patch](tarball://root/attachments/some-uuid/ticket3490/sage-3490.patch) by TimothyClemans created at 2008-06-23 20:55:52



---

archive/issue_comments_024537.json:
```json
{
    "body": "Attachment [sage-3490_2.patch](tarball://root/attachments/some-uuid/ticket3490/sage-3490_2.patch) by TimothyClemans created at 2008-06-23 20:56:16",
    "created_at": "2008-06-23T20:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3490#issuecomment-24537",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [sage-3490_2.patch](tarball://root/attachments/some-uuid/ticket3490/sage-3490_2.patch) by TimothyClemans created at 2008-06-23 20:56:16



---

archive/issue_comments_024538.json:
```json
{
    "body": "Attachment [extcode-3490.patch](tarball://root/attachments/some-uuid/ticket3490/extcode-3490.patch) by TimothyClemans created at 2008-06-23 20:57:35\n\nnote: sage-3490_2.patch puts a somehow removed extract_title function",
    "created_at": "2008-06-23T20:57:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3490#issuecomment-24538",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [extcode-3490.patch](tarball://root/attachments/some-uuid/ticket3490/extcode-3490.patch) by TimothyClemans created at 2008-06-23 20:57:35

note: sage-3490_2.patch puts a somehow removed extract_title function



---

archive/issue_comments_024539.json:
```json
{
    "body": "nice",
    "created_at": "2008-06-24T07:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3490#issuecomment-24539",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

nice



---

archive/issue_events_003710.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-25T06:34:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3490",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3490#event-3710"
}
```



---

archive/issue_comments_024540.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-25T06:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3490#issuecomment-24540",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha1



---

archive/issue_comments_024541.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-25T06:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3490#issuecomment-24541",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
