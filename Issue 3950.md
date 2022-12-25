# Issue 3950: notebook -- template(s) for generating worksheet listings

archive/issues_003950.json:
```json
{
    "body": "Assignee: boothby\n\nMake templates to replace `notebook.html_worksheet_list_public` and `notebook.html_worksheet_list_for_user` \n\nCreate a new folder to do this. Maybe use `{% include %`}\n\nRelies on #3949.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3950\n\n",
    "created_at": "2008-08-25T18:05:19Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "notebook -- template(s) for generating worksheet listings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3950",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```
Assignee: boothby

Make templates to replace `notebook.html_worksheet_list_public` and `notebook.html_worksheet_list_for_user` 

Create a new folder to do this. Maybe use `{% include %`}

Relies on #3949.

Issue created by migration from https://trac.sagemath.org/ticket/3950





---

archive/issue_comments_028296.json:
```json
{
    "body": "Timothy, are you planning on finishing this in the near future, or do you want me to?",
    "created_at": "2008-10-24T00:01:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3950#issuecomment-28296",
    "user": "https://github.com/mwhansen"
}
```

Timothy, are you planning on finishing this in the near future, or do you want me to?



---

archive/issue_comments_028297.json:
```json
{
    "body": "Don't apply extcode_3950.patch. Do apply extcode_3950_1.patch",
    "created_at": "2008-10-24T10:41:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3950#issuecomment-28297",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Don't apply extcode_3950.patch. Do apply extcode_3950_1.patch



---

archive/issue_comments_028298.json:
```json
{
    "body": "Apply extcode_3950_1.patch, extcode_3950_2.patch, trac_3950.patch, and sage-3950_part2.patch",
    "created_at": "2008-11-09T01:26:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3950#issuecomment-28298",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Apply extcode_3950_1.patch, extcode_3950_2.patch, trac_3950.patch, and sage-3950_part2.patch



---

archive/issue_comments_028299.json:
```json
{
    "body": "Also apply sage-3950_part3.patch",
    "created_at": "2008-11-10T04:17:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3950#issuecomment-28299",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Also apply sage-3950_part3.patch



---

archive/issue_comments_028300.json:
```json
{
    "body": "Changing assignee from boothby to TimothyClemans.",
    "created_at": "2008-11-10T04:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3950#issuecomment-28300",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Changing assignee from boothby to TimothyClemans.



---

archive/issue_comments_028301.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-10T04:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3950#issuecomment-28301",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Changing status from new to assigned.



---

archive/issue_comments_028302.json:
```json
{
    "body": "This should be done in a way such that there is a template for each html_* method in notebook.py (and worksheet.py) and then the templates just use the {%include%} directive to build them out of these pieces.  This makes things easy to change / update.\n\nFor example, the topbar should be in its own template so that it can be reused by what ever needs it.  As it is now, there would be lots of duplicate HTML code floating around.",
    "created_at": "2008-11-28T21:57:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3950#issuecomment-28302",
    "user": "https://github.com/mwhansen"
}
```

This should be done in a way such that there is a template for each html_* method in notebook.py (and worksheet.py) and then the templates just use the {%include%} directive to build them out of these pieces.  This makes things easy to change / update.

For example, the topbar should be in its own template so that it can be reused by what ever needs it.  As it is now, there would be lots of duplicate HTML code floating around.



---

archive/issue_comments_028303.json:
```json
{
    "body": "I haven't made a template for every html_* yet but the worksheet listing template now uses several templates.",
    "created_at": "2008-11-29T23:24:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3950#issuecomment-28303",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

I haven't made a template for every html_* yet but the worksheet listing template now uses several templates.



---

archive/issue_comments_028304.json:
```json
{
    "body": "Attachment [trac_3950.patch](tarball://root/attachments/some-uuid/ticket3950/trac_3950.patch) by @mwhansen created at 2008-12-02 10:33:36",
    "created_at": "2008-12-02T10:33:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3950#issuecomment-28304",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3950.patch](tarball://root/attachments/some-uuid/ticket3950/trac_3950.patch) by @mwhansen created at 2008-12-02 10:33:36



---

archive/issue_comments_028305.json:
```json
{
    "body": "Attachment [trac_3950-2.patch](tarball://root/attachments/some-uuid/ticket3950/trac_3950-2.patch) by @mwhansen created at 2008-12-03 00:43:35",
    "created_at": "2008-12-03T00:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3950#issuecomment-28305",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3950-2.patch](tarball://root/attachments/some-uuid/ticket3950/trac_3950-2.patch) by @mwhansen created at 2008-12-03 00:43:35



---

archive/issue_comments_028306.json:
```json
{
    "body": "Attachment [trac_3950-folded.patch](tarball://root/attachments/some-uuid/ticket3950/trac_3950-folded.patch) by @mwhansen created at 2008-12-03 00:50:00\n\nI attached my changes as trac_3950-2.patch.  trac_3950-folded.patch is a patch showing the combined effect of the two patches.  It is helpful for reviewing purposes, but the two other ones are the ones that should be applied for credit reasons.",
    "created_at": "2008-12-03T00:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3950#issuecomment-28306",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3950-folded.patch](tarball://root/attachments/some-uuid/ticket3950/trac_3950-folded.patch) by @mwhansen created at 2008-12-03 00:50:00

I attached my changes as trac_3950-2.patch.  trac_3950-folded.patch is a patch showing the combined effect of the two patches.  It is helpful for reviewing purposes, but the two other ones are the ones that should be applied for credit reasons.



---

archive/issue_comments_028307.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-04T14:55:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3950#issuecomment-28307",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028308.json:
```json
{
    "body": "Merged all three patches in Sage 3.2.2.alpha0",
    "created_at": "2008-12-04T14:55:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3950#issuecomment-28308",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three patches in Sage 3.2.2.alpha0
