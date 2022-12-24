# Issue 3490: notebook -- improve registration error checking and reporting

archive/issues_003490.json:
```json
{
    "body": "Assignee: boothby\n\nKeywords: editor_wstein\n\nThis is a follow up to #3483.\n\nis_valid_username should be upgraded to follow this rule:\n\n```\nYour username must start with a letter and be between 4 and 32 characters long. You may only use letters, numbers, underscores, and one dot (.).\n```\n\n\nA new function, is_valid_password, should be added that follows this rule:\n\n```\nYour password must be between 6 and 32 characters long. Your password can not contain your username nor spaces.\n```\n\n\nCheck to make sure the input for password and retype_password are the same.\n\nCurrently only one error is reported even if there is several of them. Report all errors to the user.\n\nDon't loose the user's input except for password/retype_password when returning error reports.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3490\n\n",
    "created_at": "2008-06-21T04:48:49Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "title": "notebook -- improve registration error checking and reporting",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3490",
    "user": "TimothyClemans"
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

archive/issue_comments_024585.json:
```json
{
    "body": "Attachment [sage-3490.patch](tarball://root/attachments/some-uuid/ticket3490/sage-3490.patch) by TimothyClemans created at 2008-06-23 20:55:52",
    "created_at": "2008-06-23T20:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3490#issuecomment-24585",
    "user": "TimothyClemans"
}
```

Attachment [sage-3490.patch](tarball://root/attachments/some-uuid/ticket3490/sage-3490.patch) by TimothyClemans created at 2008-06-23 20:55:52



---

archive/issue_comments_024586.json:
```json
{
    "body": "Attachment [sage-3490_2.patch](tarball://root/attachments/some-uuid/ticket3490/sage-3490_2.patch) by TimothyClemans created at 2008-06-23 20:56:16",
    "created_at": "2008-06-23T20:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3490#issuecomment-24586",
    "user": "TimothyClemans"
}
```

Attachment [sage-3490_2.patch](tarball://root/attachments/some-uuid/ticket3490/sage-3490_2.patch) by TimothyClemans created at 2008-06-23 20:56:16



---

archive/issue_comments_024587.json:
```json
{
    "body": "Attachment [extcode-3490.patch](tarball://root/attachments/some-uuid/ticket3490/extcode-3490.patch) by TimothyClemans created at 2008-06-23 20:57:35\n\nnote: sage-3490_2.patch puts a somehow removed extract_title function",
    "created_at": "2008-06-23T20:57:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3490#issuecomment-24587",
    "user": "TimothyClemans"
}
```

Attachment [extcode-3490.patch](tarball://root/attachments/some-uuid/ticket3490/extcode-3490.patch) by TimothyClemans created at 2008-06-23 20:57:35

note: sage-3490_2.patch puts a somehow removed extract_title function



---

archive/issue_comments_024588.json:
```json
{
    "body": "nice",
    "created_at": "2008-06-24T07:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3490#issuecomment-24588",
    "user": "boothby"
}
```

nice



---

archive/issue_comments_024589.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-25T06:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3490#issuecomment-24589",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha1



---

archive/issue_comments_024590.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-25T06:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3490#issuecomment-24590",
    "user": "mabshoff"
}
```

Resolution: fixed
