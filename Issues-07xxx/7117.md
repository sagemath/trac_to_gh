# Issue 7117: [with patch, positive review] latex fix for RIF

archive/issues_007117.json:
```json
{
    "body": "Assignee: cwitty\n\nFrom IRC:\n\n```\nBy the way, if I evaluate \"jsmath(RIF)\" in the notebook, jsMath complains: \"Unknown control sequence '\\I'\". \nIs there a missing macro definition?\n```\nIt looks to me as though the `_latex_` method for RIF has been defined in terms of '\\\\I' for a long time, and it has not worked since at least Sage 3.4.  The attached patch changes it from \"\\\\I \\\\R\" to \"\\\\Bold{I} \\\\Bold{R}\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/7117\n\n",
    "closed_at": "2009-10-15T08:36:07Z",
    "created_at": "2009-10-04T20:53:10Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "[with patch, positive review] latex fix for RIF",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7117",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: cwitty

From IRC:

```
By the way, if I evaluate "jsmath(RIF)" in the notebook, jsMath complains: "Unknown control sequence '\I'". 
Is there a missing macro definition?
```
It looks to me as though the `_latex_` method for RIF has been defined in terms of '\\I' for a long time, and it has not worked since at least Sage 3.4.  The attached patch changes it from "\\I \\R" to "\\Bold{I} \\Bold{R}".

Issue created by migration from https://trac.sagemath.org/ticket/7117





---

archive/issue_comments_058872.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-10-05T03:48:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7117#issuecomment-58872",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_058873.json:
```json
{
    "body": "Attachment [trac_7117-rif.patch](tarball://root/attachments/some-uuid/ticket7117/trac_7117-rif.patch) by @mwhansen created at 2009-10-15 08:35:31",
    "created_at": "2009-10-15T08:35:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7117#issuecomment-58873",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_7117-rif.patch](tarball://root/attachments/some-uuid/ticket7117/trac_7117-rif.patch) by @mwhansen created at 2009-10-15 08:35:31



---

archive/issue_comments_058874.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T08:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7117#issuecomment-58874",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_016822.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-15T08:36:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7117",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7117#event-16822"
}
```



---

archive/issue_comments_058875.json:
```json
{
    "body": "I had to do a minor rebasing and attached the new patch.",
    "created_at": "2009-10-15T08:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7117#issuecomment-58875",
    "user": "https://github.com/mwhansen"
}
```

I had to do a minor rebasing and attached the new patch.
