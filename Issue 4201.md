# Issue 4201: add .options and .reset to plot functions

archive/issues_004201.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  boothby\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4201\n\n",
    "created_at": "2008-09-26T17:08:06Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "add .options and .reset to plot functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4201",
    "user": "@mwhansen"
}
```
Assignee: @williamstein

CC:  boothby



Issue created by migration from https://trac.sagemath.org/ticket/4201





---

archive/issue_comments_030482.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2008-09-26T20:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4201#issuecomment-30482",
    "user": "@mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_030483.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-26T20:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4201#issuecomment-30483",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030484.json:
```json
{
    "body": "Note that this patch is on top of #4099.",
    "created_at": "2008-09-26T20:08:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4201#issuecomment-30484",
    "user": "@mwhansen"
}
```

Note that this patch is on top of #4099.



---

archive/issue_comments_030485.json:
```json
{
    "body": "A couple spelling problems:\n\n* defualt options \n* decorator whcich renames\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T20:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4201#issuecomment-30485",
    "user": "mabshoff"
}
```

A couple spelling problems:

* defualt options 
* decorator whcich renames

Cheers,

Michael



---

archive/issue_comments_030486.json:
```json
{
    "body": "Attachment [trac_4201.patch](tarball://root/attachments/some-uuid/ticket4201/trac_4201.patch) by @mwhansen created at 2008-09-26 20:15:12\n\nWhat spelling problems?  I don't see any ;-)",
    "created_at": "2008-09-26T20:15:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4201#issuecomment-30486",
    "user": "@mwhansen"
}
```

Attachment [trac_4201.patch](tarball://root/attachments/some-uuid/ticket4201/trac_4201.patch) by @mwhansen created at 2008-09-26 20:15:12

What spelling problems?  I don't see any ;-)



---

archive/issue_comments_030487.json:
```json
{
    "body": "This does not apply cleanly to alpha1.  For example, the plot_slope_field patch in alpha1 causes a reject.",
    "created_at": "2008-09-26T22:30:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4201#issuecomment-30487",
    "user": "@jasongrout"
}
```

This does not apply cleanly to alpha1.  For example, the plot_slope_field patch in alpha1 causes a reject.



---

archive/issue_comments_030488.json:
```json
{
    "body": "Attachment [trac_4201-rebased.patch](tarball://root/attachments/some-uuid/ticket4201/trac_4201-rebased.patch) by @jasongrout created at 2008-09-26 22:34:56\n\nApply instead of previous patch",
    "created_at": "2008-09-26T22:34:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4201#issuecomment-30488",
    "user": "@jasongrout"
}
```

Attachment [trac_4201-rebased.patch](tarball://root/attachments/some-uuid/ticket4201/trac_4201-rebased.patch) by @jasongrout created at 2008-09-26 22:34:56

Apply instead of previous patch



---

archive/issue_comments_030489.json:
```json
{
    "body": "trac_4201-rebased.patch is rebased against 3.1.3alpha1; apply it instead of the first patch.",
    "created_at": "2008-09-26T22:35:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4201#issuecomment-30489",
    "user": "@jasongrout"
}
```

trac_4201-rebased.patch is rebased against 3.1.3alpha1; apply it instead of the first patch.



---

archive/issue_comments_030490.json:
```json
{
    "body": "This could make #4154 easy now.",
    "created_at": "2008-09-26T22:39:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4201#issuecomment-30490",
    "user": "@jasongrout"
}
```

This could make #4154 easy now.



---

archive/issue_comments_030491.json:
```json
{
    "body": "The code looks reasonable, the rebased patch applies cleanly, it seems to work as advertised, and it solves the problem in a very elegant fashion.  Oh, and doctests in plot/*.py pass.\n\nPositive review.",
    "created_at": "2008-09-26T22:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4201#issuecomment-30491",
    "user": "@jasongrout"
}
```

The code looks reasonable, the rebased patch applies cleanly, it seems to work as advertised, and it solves the problem in a very elegant fashion.  Oh, and doctests in plot/*.py pass.

Positive review.



---

archive/issue_comments_030492.json:
```json
{
    "body": "the third patch above adds a docstring for the reset function.  Apply it on top of the second patch.",
    "created_at": "2008-09-26T23:04:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4201#issuecomment-30492",
    "user": "@jasongrout"
}
```

the third patch above adds a docstring for the reset function.  Apply it on top of the second patch.



---

archive/issue_comments_030493.json:
```json
{
    "body": "The trac_4207-options-doc-defaults.patch adds a defaults() method to get the default options and also modifies the reset() and defaults() docstrings to reflect the options of the current function instead of the vague general decorator docstring.",
    "created_at": "2008-09-26T23:21:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4201#issuecomment-30493",
    "user": "@jasongrout"
}
```

The trac_4207-options-doc-defaults.patch adds a defaults() method to get the default options and also modifies the reset() and defaults() docstrings to reflect the options of the current function instead of the vague general decorator docstring.



---

archive/issue_comments_030494.json:
```json
{
    "body": "Positive review for the rebased original patch.  There probably ought to be a review of my patches.  Mike, do you want to review them?",
    "created_at": "2008-09-26T23:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4201#issuecomment-30494",
    "user": "@jasongrout"
}
```

Positive review for the rebased original patch.  There probably ought to be a review of my patches.  Mike, do you want to review them?



---

archive/issue_comments_030495.json:
```json
{
    "body": "Attachment [trac_4201-reset-doc.patch](tarball://root/attachments/some-uuid/ticket4201/trac_4201-reset-doc.patch) by @mwhansen created at 2008-09-27 03:55:39",
    "created_at": "2008-09-27T03:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4201#issuecomment-30495",
    "user": "@mwhansen"
}
```

Attachment [trac_4201-reset-doc.patch](tarball://root/attachments/some-uuid/ticket4201/trac_4201-reset-doc.patch) by @mwhansen created at 2008-09-27 03:55:39



---

archive/issue_comments_030496.json:
```json
{
    "body": "Attachment [trac_4201-options-doc-defaults.patch](tarball://root/attachments/some-uuid/ticket4201/trac_4201-options-doc-defaults.patch) by @mwhansen created at 2008-09-27 03:56:27\n\nI just indented the examples on Jason's patches.  +1 to them.  Apply only the last three patches.",
    "created_at": "2008-09-27T03:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4201#issuecomment-30496",
    "user": "@mwhansen"
}
```

Attachment [trac_4201-options-doc-defaults.patch](tarball://root/attachments/some-uuid/ticket4201/trac_4201-options-doc-defaults.patch) by @mwhansen created at 2008-09-27 03:56:27

I just indented the examples on Jason's patches.  +1 to them.  Apply only the last three patches.



---

archive/issue_comments_030497.json:
```json
{
    "body": "Merged the last three patches in Sage 3.1.3.alpha2",
    "created_at": "2008-09-27T04:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4201#issuecomment-30497",
    "user": "mabshoff"
}
```

Merged the last three patches in Sage 3.1.3.alpha2



---

archive/issue_comments_030498.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-27T04:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4201#issuecomment-30498",
    "user": "mabshoff"
}
```

Resolution: fixed
