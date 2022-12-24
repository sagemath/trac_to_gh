# Issue 3949: notebook -- move all HTML in twist.py to templates

archive/issues_003949.json:
```json
{
    "body": "Assignee: boothby\n\nMove the HTML in twist.py in the classes/functions ` ForgotPassPage, ListOfUsers, message, Worksheet_rating_info, and RegConfirmation. `\n\nRelies on #3937\n\nIssue created by migration from https://trac.sagemath.org/ticket/3949\n\n",
    "created_at": "2008-08-25T16:10:35Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "notebook -- move all HTML in twist.py to templates",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3949",
    "user": "TimothyClemans"
}
```
Assignee: boothby

Move the HTML in twist.py in the classes/functions ` ForgotPassPage, ListOfUsers, message, Worksheet_rating_info, and RegConfirmation. `

Relies on #3937

Issue created by migration from https://trac.sagemath.org/ticket/3949





---

archive/issue_comments_028345.json:
```json
{
    "body": "Ignore the class ` Worksheet_rating_info `",
    "created_at": "2008-08-25T17:39:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3949#issuecomment-28345",
    "user": "TimothyClemans"
}
```

Ignore the class ` Worksheet_rating_info `



---

archive/issue_comments_028346.json:
```json
{
    "body": "Attachment [extcode-3949_1.patch](tarball://root/attachments/some-uuid/ticket3949/extcode-3949_1.patch) by TimothyClemans created at 2008-08-25 17:49:34",
    "created_at": "2008-08-25T17:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3949#issuecomment-28346",
    "user": "TimothyClemans"
}
```

Attachment [extcode-3949_1.patch](tarball://root/attachments/some-uuid/ticket3949/extcode-3949_1.patch) by TimothyClemans created at 2008-08-25 17:49:34



---

archive/issue_comments_028347.json:
```json
{
    "body": "See #3923",
    "created_at": "2008-09-24T11:04:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3949#issuecomment-28347",
    "user": "@malb"
}
```

See #3923



---

archive/issue_comments_028348.json:
```json
{
    "body": "Attachment [trac_3949.patch](tarball://root/attachments/some-uuid/ticket3949/trac_3949.patch) by @mwhansen created at 2008-10-23 23:30:02",
    "created_at": "2008-10-23T23:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3949#issuecomment-28348",
    "user": "@mwhansen"
}
```

Attachment [trac_3949.patch](tarball://root/attachments/some-uuid/ticket3949/trac_3949.patch) by @mwhansen created at 2008-10-23 23:30:02



---

archive/issue_comments_028349.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2008-10-23T23:31:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3949#issuecomment-28349",
    "user": "@mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_comments_028350.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-23T23:31:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3949#issuecomment-28350",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_028351.json:
```json
{
    "body": "Attachment [extcode_3949.patch](tarball://root/attachments/some-uuid/ticket3949/extcode_3949.patch) by @mwhansen created at 2008-10-23 23:31:47\n\nI've rebased this against 3.2.alpha0 and moved the templates into sage/server/notebook/templates/\n\nApply only the last two patches: trac_3949.patch and extcode_3949.patch",
    "created_at": "2008-10-23T23:31:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3949#issuecomment-28351",
    "user": "@mwhansen"
}
```

Attachment [extcode_3949.patch](tarball://root/attachments/some-uuid/ticket3949/extcode_3949.patch) by @mwhansen created at 2008-10-23 23:31:47

I've rebased this against 3.2.alpha0 and moved the templates into sage/server/notebook/templates/

Apply only the last two patches: trac_3949.patch and extcode_3949.patch



---

archive/issue_comments_028352.json:
```json
{
    "body": "Merged trac_3949.patch and extcode_3949.patch in Sage 3.2.alpha1",
    "created_at": "2008-10-25T23:01:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3949#issuecomment-28352",
    "user": "mabshoff"
}
```

Merged trac_3949.patch and extcode_3949.patch in Sage 3.2.alpha1



---

archive/issue_comments_028353.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-25T23:01:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3949#issuecomment-28353",
    "user": "mabshoff"
}
```

Resolution: fixed
