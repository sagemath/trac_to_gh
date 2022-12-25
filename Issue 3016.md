# Issue 3016: [with patch, needs discussion ] javascript code editor spkg

archive/issues_003016.json:
```json
{
    "body": "Assignee: boothby\n\nEdit Area is one of several javascript code editors.  Here is a simple (*very* simple) spkg which installs the necessary files in sage/data/extcode/notebook/javascript/edit_area/ and also a patch to enable the functionality.\n\nThe patch currently only enables the toggle switch (between new editor and old functionality) for the first cell (the input_cell_0 cell).  That should be enough to evaluate it, though.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3016\n\n",
    "created_at": "2008-04-24T08:51:55Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, needs discussion ] javascript code editor spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3016",
    "user": "https://github.com/jasongrout"
}
```
Assignee: boothby

Edit Area is one of several javascript code editors.  Here is a simple (*very* simple) spkg which installs the necessary files in sage/data/extcode/notebook/javascript/edit_area/ and also a patch to enable the functionality.

The patch currently only enables the toggle switch (between new editor and old functionality) for the first cell (the input_cell_0 cell).  That should be enough to evaluate it, though.

Issue created by migration from https://trac.sagemath.org/ticket/3016





---

archive/issue_comments_020681.json:
```json
{
    "body": "Attachment [edit_area-0.7.1.spkg](tarball://root/attachments/some-uuid/ticket3016/edit_area-0.7.1.spkg) by @jasongrout created at 2008-04-24 08:52:21",
    "created_at": "2008-04-24T08:52:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3016#issuecomment-20681",
    "user": "https://github.com/jasongrout"
}
```

Attachment [edit_area-0.7.1.spkg](tarball://root/attachments/some-uuid/ticket3016/edit_area-0.7.1.spkg) by @jasongrout created at 2008-04-24 08:52:21



---

archive/issue_comments_020682.json:
```json
{
    "body": "Attachment [trac-3016-edit-area.patch](tarball://root/attachments/some-uuid/ticket3016/trac-3016-edit-area.patch) by mabshoff created at 2008-04-24 14:17:12\n\nHi Jason,\n\ninstead of an spkg it would be customary to add the code directly to the extcode repo. What is the license of the code? The notebook code is supposed to be BSD since other projects might be able to pick it up that way.\n\nIf you want discussion of something like this you should mention it on sage-devel since trac is certainly the wrong place to discuss this and few people will find the ticket without it being mentioned on sage-devel.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-24T14:17:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3016#issuecomment-20682",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac-3016-edit-area.patch](tarball://root/attachments/some-uuid/ticket3016/trac-3016-edit-area.patch) by mabshoff created at 2008-04-24 14:17:12

Hi Jason,

instead of an spkg it would be customary to add the code directly to the extcode repo. What is the license of the code? The notebook code is supposed to be BSD since other projects might be able to pick it up that way.

If you want discussion of something like this you should mention it on sage-devel since trac is certainly the wrong place to discuss this and few people will find the ticket without it being mentioned on sage-devel.

Cheers,

Michael



---

archive/issue_comments_020683.json:
```json
{
    "body": "I mentioned it in the thread where it was brought up in sage-devel.  I'll make another post too so that it's more visible.  As explained in the SPKG.txt file, the license is LGPL and Apache (dual-licensed).  I know that it would be customary to add the code directly, but since it was likely to be controversial (I just picked an editor and threw it in so we could at least play with it easily), I opted for the \"optional package\" route, at least for now.  I wrote the patch to notebook.py so that it would automatically take advantage of the package if it was there, but not change things if it wasn't.\n\nAlso, the spkg is barely minimally functional; it breaks everything too.  When the editor is clicked, nothing from the sage behavior works (tab completion, etc.).  Again, I just put it in there so people would have something they could start and play with.\n\nThanks for the pointers, though.\n\nJason",
    "created_at": "2008-04-24T18:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3016#issuecomment-20683",
    "user": "https://github.com/jasongrout"
}
```

I mentioned it in the thread where it was brought up in sage-devel.  I'll make another post too so that it's more visible.  As explained in the SPKG.txt file, the license is LGPL and Apache (dual-licensed).  I know that it would be customary to add the code directly, but since it was likely to be controversial (I just picked an editor and threw it in so we could at least play with it easily), I opted for the "optional package" route, at least for now.  I wrote the patch to notebook.py so that it would automatically take advantage of the package if it was there, but not change things if it wasn't.

Also, the spkg is barely minimally functional; it breaks everything too.  When the editor is clicked, nothing from the sage behavior works (tab completion, etc.).  Again, I just put it in there so people would have something they could start and play with.

Thanks for the pointers, though.

Jason



---

archive/issue_comments_020684.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-06-20T04:51:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3016#issuecomment-20684",
    "user": "https://github.com/craigcitro"
}
```

Resolution: invalid



---

archive/issue_comments_020685.json:
```json
{
    "body": "This should be brought up as a thread on sage-devel.",
    "created_at": "2008-06-20T04:51:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3016#issuecomment-20685",
    "user": "https://github.com/craigcitro"
}
```

This should be brought up as a thread on sage-devel.
