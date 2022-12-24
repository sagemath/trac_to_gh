# Issue 7367: Add SageNB modules to the reference manual

archive/issues_007367.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  timdumol\n\nCurrently, the [reference manual's](http://www.sagemath.org/doc/reference/index.html) [Notebook section](http://www.sagemath.org/doc/reference/notebook.html) documents the old Sage notebook.\n\nWe should update this section with docstrings from the recently separated [SageNB](http://nb.sagemath.org/).\n\nIssue created by migration from https://trac.sagemath.org/ticket/7367\n\n",
    "created_at": "2009-11-01T13:35:58Z",
    "labels": [
        "doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "Add SageNB modules to the reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7367",
    "user": "mpatel"
}
```
Assignee: tbd

CC:  timdumol

Currently, the [reference manual's](http://www.sagemath.org/doc/reference/index.html) [Notebook section](http://www.sagemath.org/doc/reference/notebook.html) documents the old Sage notebook.

We should update this section with docstrings from the recently separated [SageNB](http://nb.sagemath.org/).

Issue created by migration from https://trac.sagemath.org/ticket/7367





---

archive/issue_comments_061737.json:
```json
{
    "body": "Attachment [trac_7367-sagenb_manual.patch](tarball://root/attachments/some-uuid/ticket7367/trac_7367-sagenb_manual.patch) by mpatel created at 2009-11-01 14:01:34\n\nAdd SageNB modules to reference manual.  Apply to sage repo.",
    "created_at": "2009-11-01T14:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7367#issuecomment-61737",
    "user": "mpatel"
}
```

Attachment [trac_7367-sagenb_manual.patch](tarball://root/attachments/some-uuid/ticket7367/trac_7367-sagenb_manual.patch) by mpatel created at 2009-11-01 14:01:34

Add SageNB modules to reference manual.  Apply to sage repo.



---

archive/issue_comments_061738.json:
```json
{
    "body": "I've commented out the \"Interfaces\" section, for now.\n\nI think `sagenb.misc.sphinxify`'s docstrings need just a bit of tweaking.",
    "created_at": "2009-11-01T14:03:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7367#issuecomment-61738",
    "user": "mpatel"
}
```

I've commented out the "Interfaces" section, for now.

I think `sagenb.misc.sphinxify`'s docstrings need just a bit of tweaking.



---

archive/issue_comments_061739.json:
```json
{
    "body": "Replying to [comment:1 mpatel]:\n> I think `sagenb.misc.sphinxify`'s docstrings need just a bit of tweaking.\n\nOf course, we can comment it out, too, temporarily.  I didn't mean to pile on more work.",
    "created_at": "2009-11-01T14:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7367#issuecomment-61739",
    "user": "mpatel"
}
```

Replying to [comment:1 mpatel]:
> I think `sagenb.misc.sphinxify`'s docstrings need just a bit of tweaking.

Of course, we can comment it out, too, temporarily.  I didn't mean to pile on more work.



---

archive/issue_comments_061740.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-01T14:10:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7367#issuecomment-61740",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061741.json:
```json
{
    "body": "Replying to [comment:2 mpatel]:\n> Replying to [comment:1 mpatel]:\n> > I think `sagenb.misc.sphinxify`'s docstrings need just a bit of tweaking.\n> \n> Of course, we can comment it out, too, temporarily.  I didn't mean to pile on more work.\n\nDocstring fixes are up at http://trac.sagemath.org/sage_trac/ticket/7384",
    "created_at": "2009-11-03T20:48:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7367#issuecomment-61741",
    "user": "timdumol"
}
```

Replying to [comment:2 mpatel]:
> Replying to [comment:1 mpatel]:
> > I think `sagenb.misc.sphinxify`'s docstrings need just a bit of tweaking.
> 
> Of course, we can comment it out, too, temporarily.  I didn't mean to pile on more work.

Docstring fixes are up at http://trac.sagemath.org/sage_trac/ticket/7384



---

archive/issue_comments_061742.json:
```json
{
    "body": "Everything looks good, but why is the miscellaneous section named \"Documentation\"? Shouldn't it be named \"Miscellaneous functions\", or \"Introspection\", or the like? The name \"Documentation\" is confusing, at least for me.",
    "created_at": "2009-11-03T21:32:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7367#issuecomment-61742",
    "user": "timdumol"
}
```

Everything looks good, but why is the miscellaneous section named "Documentation"? Shouldn't it be named "Miscellaneous functions", or "Introspection", or the like? The name "Documentation" is confusing, at least for me.



---

archive/issue_comments_061743.json:
```json
{
    "body": "\"Documentation\" is indeed confusing.  I think my motive was to identify and group the [mostly] help-related modules.  Since `support` falls under \"Online Help\" and \"Miscellaneous,\" the forthcoming patch simply puts them all under the latter.",
    "created_at": "2009-11-04T04:36:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7367#issuecomment-61743",
    "user": "mpatel"
}
```

"Documentation" is indeed confusing.  I think my motive was to identify and group the [mostly] help-related modules.  Since `support` falls under "Online Help" and "Miscellaneous," the forthcoming patch simply puts them all under the latter.



---

archive/issue_comments_061744.json:
```json
{
    "body": "Attachment [trac_7367-sagenb_manual_v2.patch](tarball://root/attachments/some-uuid/ticket7367/trac_7367-sagenb_manual_v2.patch) by mpatel created at 2009-11-04 04:46:02\n\nLess confusing subheading.  Really skip interface modules.  Apply only this patch to sage repo.",
    "created_at": "2009-11-04T04:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7367#issuecomment-61744",
    "user": "mpatel"
}
```

Attachment [trac_7367-sagenb_manual_v2.patch](tarball://root/attachments/some-uuid/ticket7367/trac_7367-sagenb_manual_v2.patch) by mpatel created at 2009-11-04 04:46:02

Less confusing subheading.  Really skip interface modules.  Apply only this patch to sage repo.



---

archive/issue_comments_061745.json:
```json
{
    "body": "Feel free to bump the milestone to 4.3.",
    "created_at": "2009-11-12T01:44:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7367#issuecomment-61745",
    "user": "mpatel"
}
```

Feel free to bump the milestone to 4.3.



---

archive/issue_comments_061746.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-12T02:12:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7367#issuecomment-61746",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061747.json:
```json
{
    "body": "Looks good to me too.",
    "created_at": "2009-11-12T02:12:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7367#issuecomment-61747",
    "user": "was"
}
```

Looks good to me too.



---

archive/issue_comments_061748.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-12T07:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7367#issuecomment-61748",
    "user": "mhansen"
}
```

Resolution: fixed
