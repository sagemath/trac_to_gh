# Issue 4099: Fix documentation for point2d, line2d, ...

archive/issues_004099.json:
```json
{
    "body": "Assignee: tba\n\nSince #3853, the documentation for the *2d functions in plot/plot.py is outdated.  \n\nIt refers to things like point.options and line.reset which are gone and produce errors when you try to access them.\n\nIf I had the time I would do a patch for this, but I am currently swamped with other work.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4099\n\n",
    "created_at": "2008-09-11T02:41:34Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "Fix documentation for point2d, line2d, ...",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4099",
    "user": "anakha"
}
```
Assignee: tba

Since #3853, the documentation for the *2d functions in plot/plot.py is outdated.  

It refers to things like point.options and line.reset which are gone and produce errors when you try to access them.

If I had the time I would do a patch for this, but I am currently swamped with other work.

Issue created by migration from https://trac.sagemath.org/ticket/4099





---

archive/issue_comments_029577.json:
```json
{
    "body": "Attachment [4099.patch](tarball://root/attachments/some-uuid/ticket4099/4099.patch) by @jicama created at 2008-09-14 02:56:21\n\nThe patch just nukes all mention of .options and .reset.  So far as I can tell, this functionality is gone without replacement.  If there is now some other way to learn what these attributes used to tell you, then this patch should probably not be accepted, and the doc should be rewritten to explain the new functionality.",
    "created_at": "2008-09-14T02:56:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4099#issuecomment-29577",
    "user": "@jicama"
}
```

Attachment [4099.patch](tarball://root/attachments/some-uuid/ticket4099/4099.patch) by @jicama created at 2008-09-14 02:56:21

The patch just nukes all mention of .options and .reset.  So far as I can tell, this functionality is gone without replacement.  If there is now some other way to learn what these attributes used to tell you, then this patch should probably not be accepted, and the doc should be rewritten to explain the new functionality.



---

archive/issue_comments_029578.json:
```json
{
    "body": "Changing assignee from tba to @jicama.",
    "created_at": "2008-09-14T02:56:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4099#issuecomment-29578",
    "user": "@jicama"
}
```

Changing assignee from tba to @jicama.



---

archive/issue_comments_029579.json:
```json
{
    "body": "I think this is good for now.",
    "created_at": "2008-09-19T00:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4099#issuecomment-29579",
    "user": "@mwhansen"
}
```

I think this is good for now.



---

archive/issue_comments_029580.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha0",
    "created_at": "2008-09-19T03:19:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4099#issuecomment-29580",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha0



---

archive/issue_comments_029581.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-19T03:19:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4099#issuecomment-29581",
    "user": "mabshoff"
}
```

Resolution: fixed
