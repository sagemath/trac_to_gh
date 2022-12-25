# Issue 1693: jmol stubles over browser caching

archive/issues_001693.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @malb\n\napplet is invoked by\n\n```\njmol_applet(500, \"/home/harri/5/cells/204/sage0-size500.jmol\")\n```\n\nbut does not get the new jmol file. possibly just needs a ?\"number\" as with plots/images\n\nIssue created by migration from https://trac.sagemath.org/ticket/1693\n\n",
    "created_at": "2008-01-05T20:20:07Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "jmol stubles over browser caching",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1693",
    "user": "https://github.com/haraldschilly"
}
```
Assignee: boothby

CC:  @malb

applet is invoked by

```
jmol_applet(500, "/home/harri/5/cells/204/sage0-size500.jmol")
```

but does not get the new jmol file. possibly just needs a ?"number" as with plots/images

Issue created by migration from https://trac.sagemath.org/ticket/1693





---

archive/issue_comments_010724.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-01-05T20:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1693#issuecomment-10724",
    "user": "https://github.com/haraldschilly"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_010725.json:
```json
{
    "body": "Attachment [trac_1693.patch](tarball://root/attachments/some-uuid/ticket1693/trac_1693.patch) by @malb created at 2008-01-06 13:11:23",
    "created_at": "2008-01-06T13:11:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1693#issuecomment-10725",
    "user": "https://github.com/malb"
}
```

Attachment [trac_1693.patch](tarball://root/attachments/some-uuid/ticket1693/trac_1693.patch) by @malb created at 2008-01-06 13:11:23



---

archive/issue_comments_010726.json:
```json
{
    "body": "Yes, this is the right fix.",
    "created_at": "2008-01-08T23:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1693#issuecomment-10726",
    "user": "https://github.com/robertwb"
}
```

Yes, this is the right fix.



---

archive/issue_comments_010727.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-08T23:24:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1693#issuecomment-10727",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010728.json:
```json
{
    "body": "Merged in Sage 2.10.alpha1.",
    "created_at": "2008-01-08T23:24:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1693#issuecomment-10728",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.alpha1.



---

archive/issue_comments_010729.json:
```json
{
    "body": "looks good to me too.",
    "created_at": "2008-01-09T04:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1693#issuecomment-10729",
    "user": "https://github.com/williamstein"
}
```

looks good to me too.
