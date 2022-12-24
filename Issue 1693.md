# Issue 1693: jmol stubles over browser caching

archive/issues_001693.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @malb\n\napplet is invoked by\n\n```\njmol_applet(500, \"/home/harri/5/cells/204/sage0-size500.jmol\")\n```\n\nbut does not get the new jmol file. possibly just needs a ?\"number\" as with plots/images\n\nIssue created by migration from https://trac.sagemath.org/ticket/1693\n\n",
    "created_at": "2008-01-05T20:20:07Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "jmol stubles over browser caching",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1693",
    "user": "@haraldschilly"
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

archive/issue_comments_010751.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-01-05T20:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1693#issuecomment-10751",
    "user": "@haraldschilly"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_010752.json:
```json
{
    "body": "Attachment [trac_1693.patch](tarball://root/attachments/some-uuid/ticket1693/trac_1693.patch) by @malb created at 2008-01-06 13:11:23",
    "created_at": "2008-01-06T13:11:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1693#issuecomment-10752",
    "user": "@malb"
}
```

Attachment [trac_1693.patch](tarball://root/attachments/some-uuid/ticket1693/trac_1693.patch) by @malb created at 2008-01-06 13:11:23



---

archive/issue_comments_010753.json:
```json
{
    "body": "Yes, this is the right fix.",
    "created_at": "2008-01-08T23:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1693#issuecomment-10753",
    "user": "@robertwb"
}
```

Yes, this is the right fix.



---

archive/issue_comments_010754.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-08T23:24:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1693#issuecomment-10754",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010755.json:
```json
{
    "body": "Merged in Sage 2.10.alpha1.",
    "created_at": "2008-01-08T23:24:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1693#issuecomment-10755",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.alpha1.



---

archive/issue_comments_010756.json:
```json
{
    "body": "looks good to me too.",
    "created_at": "2008-01-09T04:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1693#issuecomment-10756",
    "user": "@williamstein"
}
```

looks good to me too.
