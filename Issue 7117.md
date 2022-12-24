# Issue 7117: [with patch, needs review] latex fix for RIF

archive/issues_007117.json:
```json
{
    "body": "Assignee: cwitty\n\nFrom IRC:\n\n```\nBy the way, if I evaluate \"jsmath(RIF)\" in the notebook, jsMath complains: \"Unknown control sequence '\\I'\". \nIs there a missing macro definition?\n```\n\nIt looks to me as though the `_latex_` method for RIF has been defined in terms of '\\\\I' for a long time, and it has not worked since at least Sage 3.4.  The attached patch changes it from \"\\\\I \\\\R\" to \"\\\\Bold{I} \\\\Bold{R}\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/7117\n\n",
    "created_at": "2009-10-04T20:53:10Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] latex fix for RIF",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7117",
    "user": "jhpalmieri"
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

archive/issue_comments_058983.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-10-05T03:48:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7117#issuecomment-58983",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_058984.json:
```json
{
    "body": "Attachment [trac_7117-rif.patch](tarball://root/attachments/some-uuid/ticket7117/trac_7117-rif.patch) by mhansen created at 2009-10-15 08:35:31",
    "created_at": "2009-10-15T08:35:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7117#issuecomment-58984",
    "user": "mhansen"
}
```

Attachment [trac_7117-rif.patch](tarball://root/attachments/some-uuid/ticket7117/trac_7117-rif.patch) by mhansen created at 2009-10-15 08:35:31



---

archive/issue_comments_058985.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T08:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7117#issuecomment-58985",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_058986.json:
```json
{
    "body": "I had to do a minor rebasing and attached the new patch.",
    "created_at": "2009-10-15T08:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7117#issuecomment-58986",
    "user": "mhansen"
}
```

I had to do a minor rebasing and attached the new patch.
