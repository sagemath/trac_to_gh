# Issue 8221: blank space at bottom of worksheet missing

archive/issues_008221.json:
```json
{
    "body": "Assignee: @williamstein\n\nThere used to be blank space (via CSS) at the bottom of the notebook that would prevent interacts from jumping when updated.  See  #4963 for the CSS code that was used and the reason for it.  In 4.3.2, it seems that the blank space was removed.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8221\n\n",
    "created_at": "2010-02-09T15:45:41Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "blank space at bottom of worksheet missing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8221",
    "user": "@jasongrout"
}
```
Assignee: @williamstein

There used to be blank space (via CSS) at the bottom of the notebook that would prevent interacts from jumping when updated.  See  #4963 for the CSS code that was used and the reason for it.  In 4.3.2, it seems that the blank space was removed.


Issue created by migration from https://trac.sagemath.org/ticket/8221





---

archive/issue_comments_072559.json:
```json
{
    "body": "Attachment [trac_8221-ws_blank_space.patch](tarball://root/attachments/some-uuid/ticket8221/trac_8221-ws_blank_space.patch) by @qed777 created at 2010-02-14 03:35:35\n\nBig blank space at bottom of live worksheets.  sagenb repo.",
    "created_at": "2010-02-14T03:35:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8221#issuecomment-72559",
    "user": "@qed777"
}
```

Attachment [trac_8221-ws_blank_space.patch](tarball://root/attachments/some-uuid/ticket8221/trac_8221-ws_blank_space.patch) by @qed777 created at 2010-02-14 03:35:35

Big blank space at bottom of live worksheets.  sagenb repo.



---

archive/issue_comments_072560.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-14T03:36:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8221#issuecomment-72560",
    "user": "@qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072561.json:
```json
{
    "body": "Works as advertised. I tried before/after with a worksheet with an interact as the last block. In this case the cell about is fairly large. The page would jump significantly every time the interact updated. Adding the space stopped the jumping.\n\nIs there a suitable place to document this? Other than in trac? I can see this as something that can get changed as people forget the reason for it. Perhaps just a suitable comment in the source is all that is needed.  \n\nAdam",
    "created_at": "2010-03-07T13:42:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8221#issuecomment-72561",
    "user": "@maxthemouse"
}
```

Works as advertised. I tried before/after with a worksheet with an interact as the last block. In this case the cell about is fairly large. The page would jump significantly every time the interact updated. Adding the space stopped the jumping.

Is there a suitable place to document this? Other than in trac? I can see this as something that can get changed as people forget the reason for it. Perhaps just a suitable comment in the source is all that is needed.  

Adam



---

archive/issue_comments_072562.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-07T13:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8221#issuecomment-72562",
    "user": "@maxthemouse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072563.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-09T05:10:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8221#issuecomment-72563",
    "user": "@qed777"
}
```

Resolution: fixed



---

archive/issue_comments_072564.json:
```json
{
    "body": "Possibly in `sagenb.notebook.interact`, I think.  The space is useful for other reasons, of course, but we should try to fix the flickering interact problem.  I had what *may* be a promising solution at #7908.  I'll try to rebase it in the near future.",
    "created_at": "2010-03-09T05:10:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8221#issuecomment-72564",
    "user": "@qed777"
}
```

Possibly in `sagenb.notebook.interact`, I think.  The space is useful for other reasons, of course, but we should try to fix the flickering interact problem.  I had what *may* be a promising solution at #7908.  I'll try to rebase it in the near future.
