# Issue 6210: docs for the property option of graphs() should include a pointer to the docs for the augment parameter

archive/issues_006210.json:
```json
{
    "body": "Assignee: tba\n\nA sentence in the docs for the property parameter should say something about possibly missing graphs, due to the reasons explained in the docs for the augment parameter.  See http://groups.google.com/group/sage-devel/browse_thread/thread/e8516faf818a6fb7\n\nIssue created by migration from https://trac.sagemath.org/ticket/6210\n\n",
    "created_at": "2009-06-04T19:48:38Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "docs for the property option of graphs() should include a pointer to the docs for the augment parameter",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6210",
    "user": "https://github.com/jasongrout"
}
```
Assignee: tba

A sentence in the docs for the property parameter should say something about possibly missing graphs, due to the reasons explained in the docs for the augment parameter.  See http://groups.google.com/group/sage-devel/browse_thread/thread/e8516faf818a6fb7

Issue created by migration from https://trac.sagemath.org/ticket/6210





---

archive/issue_comments_049519.json:
```json
{
    "body": "Attachment [trac_6210_clarify_graphs_property_argument.patch](tarball://root/attachments/some-uuid/ticket6210/trac_6210_clarify_graphs_property_argument.patch) by dsm created at 2011-03-10 05:06:00\n\nI just got bitten by this..",
    "created_at": "2011-03-10T05:06:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6210#issuecomment-49519",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Attachment [trac_6210_clarify_graphs_property_argument.patch](tarball://root/attachments/some-uuid/ticket6210/trac_6210_clarify_graphs_property_argument.patch) by dsm created at 2011-03-10 05:06:00

I just got bitten by this..



---

archive/issue_comments_049520.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-03-10T05:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6210#issuecomment-49520",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_049521.json:
```json
{
    "body": "Hello !!!\n\nIt's true that this part's tricky, but what about just saying after \n\n```\n``property`` -- (default: ``lambda x: True``) any property to be tested on graphs before generation\n```\n\n\nSomething like \"The property must fill an inheritance property to work as intended. Please refer to the help of parameter ``augment``\" ?\n\nOtherwise the explanations are given twice and we're sure users will read them `:-)`\n\nNathann",
    "created_at": "2011-05-02T13:50:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6210#issuecomment-49521",
    "user": "https://github.com/nathanncohen"
}
```

Hello !!!

It's true that this part's tricky, but what about just saying after 

```
``property`` -- (default: ``lambda x: True``) any property to be tested on graphs before generation
```


Something like "The property must fill an inheritance property to work as intended. Please refer to the help of parameter ``augment``" ?

Otherwise the explanations are given twice and we're sure users will read them `:-)`

Nathann



---

archive/issue_comments_049522.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-05-02T13:50:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6210#issuecomment-49522",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_049523.json:
```json
{
    "body": "We got bitten too, in our undergrad course :) I think I agree with Nathann.",
    "created_at": "2011-10-14T04:20:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6210#issuecomment-49523",
    "user": "https://github.com/kini"
}
```

We got bitten too, in our undergrad course :) I think I agree with Nathann.



---

archive/issue_comments_049524.json:
```json
{
    "body": "Replying to [comment:4 kini]:\n> We got bitten too, in our undergrad course :) I think I agree with Nathann.\n\nbetter more, than less...",
    "created_at": "2011-10-15T06:59:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6210#issuecomment-49524",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:4 kini]:
> We got bitten too, in our undergrad course :) I think I agree with Nathann.

better more, than less...



---

archive/issue_comments_049525.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-10-15T06:59:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6210#issuecomment-49525",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_049526.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-10-15T06:59:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6210#issuecomment-49526",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_049527.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-10-17T07:50:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6210#issuecomment-49527",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_006459.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-10-17T07:50:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6210",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6210#event-6459"
}
```
