# Issue 5815: [with patch, needs review] Disable TinyMCE in the live documentation

archive/issues_005815.json:
```json
{
    "body": "Assignee: boothby\n\nDouble-clicking on a text cell in the live documentation --- I've done this accidentally several times --- fires up TinyMCE, which acts strangely.  More importantly, no changes will be saved, as Jason Grout pointed out on sage-devel:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/8c8fe7c5d0c0f725\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5815\n\n",
    "created_at": "2009-04-18T09:32:47Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "[with patch, needs review] Disable TinyMCE in the live documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5815",
    "user": "mpatel"
}
```
Assignee: boothby

Double-clicking on a text cell in the live documentation --- I've done this accidentally several times --- fires up TinyMCE, which acts strangely.  More importantly, no changes will be saved, as Jason Grout pointed out on sage-devel:

http://groups.google.com/group/sage-devel/browse_thread/thread/8c8fe7c5d0c0f725


Issue created by migration from https://trac.sagemath.org/ticket/5815





---

archive/issue_comments_045687.json:
```json
{
    "body": "Attachment [trac_5815_tinymce_live_doc.patch](tarball://root/attachments/some-uuid/ticket5815/trac_5815_tinymce_live_doc.patch) by mpatel created at 2009-04-18 09:34:34\n\nSee the comment.",
    "created_at": "2009-04-18T09:34:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5815#issuecomment-45687",
    "user": "mpatel"
}
```

Attachment [trac_5815_tinymce_live_doc.patch](tarball://root/attachments/some-uuid/ticket5815/trac_5815_tinymce_live_doc.patch) by mpatel created at 2009-04-18 09:34:34

See the comment.



---

archive/issue_comments_045688.json:
```json
{
    "body": "The new line of code, like the CSS \"hack\" which follows it, depends, I think, on an exact match.\n\nPerhaps it's better to add code which disables editing.",
    "created_at": "2009-04-18T09:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5815#issuecomment-45688",
    "user": "mpatel"
}
```

The new line of code, like the CSS "hack" which follows it, depends, I think, on an exact match.

Perhaps it's better to add code which disables editing.



---

archive/issue_comments_045689.json:
```json
{
    "body": "I agree that the above patch is the wrong solution.  I'll post a patch momentarily which disables it just like when the sheet is published.",
    "created_at": "2009-04-22T02:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5815#issuecomment-45689",
    "user": "jason"
}
```

I agree that the above patch is the wrong solution.  I'll post a patch momentarily which disables it just like when the sheet is published.



---

archive/issue_comments_045690.json:
```json
{
    "body": "apply instead of previous patch.",
    "created_at": "2009-04-22T02:20:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5815#issuecomment-45690",
    "user": "jason"
}
```

apply instead of previous patch.



---

archive/issue_comments_045691.json:
```json
{
    "body": "Attachment [trac-5815-docs-and-tinymce.patch](tarball://root/attachments/some-uuid/ticket5815/trac-5815-docs-and-tinymce.patch) by jason created at 2009-04-22 02:22:35\n\ntrac-5815-docs-and-tinymce.patch takes care of this issue by implementing the idea from the comment above (i.e., don't put the TinyMCE trigger in when you are looking at a doc page).\n\nmpatel, can you review this patch?",
    "created_at": "2009-04-22T02:22:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5815#issuecomment-45691",
    "user": "jason"
}
```

Attachment [trac-5815-docs-and-tinymce.patch](tarball://root/attachments/some-uuid/ticket5815/trac-5815-docs-and-tinymce.patch) by jason created at 2009-04-22 02:22:35

trac-5815-docs-and-tinymce.patch takes care of this issue by implementing the idea from the comment above (i.e., don't put the TinyMCE trigger in when you are looking at a doc page).

mpatel, can you review this patch?



---

archive/issue_comments_045692.json:
```json
{
    "body": "The new patch works and is definitely better than the first.\n\nI noticed that copying or printing a docbrowser worksheet omits Sphinx' stylesheet.  One-cell mode also appears to be broken.  Of course, these are separate issues, and I can open new tickets.",
    "created_at": "2009-04-22T03:34:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5815#issuecomment-45692",
    "user": "mpatel"
}
```

The new patch works and is definitely better than the first.

I noticed that copying or printing a docbrowser worksheet omits Sphinx' stylesheet.  One-cell mode also appears to be broken.  Of course, these are separate issues, and I can open new tickets.



---

archive/issue_comments_045693.json:
```json
{
    "body": "Replying to [comment:4 mpatel]:\n> I noticed that copying or printing a docbrowser worksheet omits Sphinx' stylesheet.  One-cell mode also appears to be broken.  Of course, these are separate issues, and I can open new tickets.\nOops!  One-cell mode is fine.  Sorry.",
    "created_at": "2009-04-22T03:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5815#issuecomment-45693",
    "user": "mpatel"
}
```

Replying to [comment:4 mpatel]:
> I noticed that copying or printing a docbrowser worksheet omits Sphinx' stylesheet.  One-cell mode also appears to be broken.  Of course, these are separate issues, and I can open new tickets.
Oops!  One-cell mode is fine.  Sorry.



---

archive/issue_comments_045694.json:
```json
{
    "body": "Merged trac-5815-docs-and-tinymce.patch in Sage 3.4.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T09:46:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5815#issuecomment-45694",
    "user": "mabshoff"
}
```

Merged trac-5815-docs-and-tinymce.patch in Sage 3.4.2.alpha0.

Cheers,

Michael



---

archive/issue_comments_045695.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-24T09:46:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5815#issuecomment-45695",
    "user": "mabshoff"
}
```

Resolution: fixed
