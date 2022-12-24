# Issue 9831: Invalid HTML in data/sage/html/login.html

archive/issues_009831.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @jasongrout\n\nThe W3C validator gives errors about missing targets for the <label> elements.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9832\n\n",
    "created_at": "2010-08-28T13:42:47Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "Invalid HTML in data/sage/html/login.html",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9831",
    "user": "@TimDumol"
}
```
Assignee: jason, was

CC:  @jasongrout

The W3C validator gives errors about missing targets for the <label> elements.

Issue created by migration from https://trac.sagemath.org/ticket/9832





---

archive/issue_comments_097015.json:
```json
{
    "body": "Fixes the error.",
    "created_at": "2010-08-28T13:43:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9831#issuecomment-97015",
    "user": "@TimDumol"
}
```

Fixes the error.



---

archive/issue_comments_097016.json:
```json
{
    "body": "Attachment [trac_9832-invalid-html.patch](tarball://root/attachments/some-uuid/ticket9832/trac_9832-invalid-html.patch) by @TimDumol created at 2010-08-28 14:15:48",
    "created_at": "2010-08-28T14:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9831#issuecomment-97016",
    "user": "@TimDumol"
}
```

Attachment [trac_9832-invalid-html.patch](tarball://root/attachments/some-uuid/ticket9832/trac_9832-invalid-html.patch) by @TimDumol created at 2010-08-28 14:15:48



---

archive/issue_comments_097017.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-28T14:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9831#issuecomment-97017",
    "user": "@TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097018.json:
```json
{
    "body": "Changing assignee from jason, was to @jasongrout.",
    "created_at": "2010-10-08T20:49:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9831#issuecomment-97018",
    "user": "@jasongrout"
}
```

Changing assignee from jason, was to @jasongrout.



---

archive/issue_comments_097019.json:
```json
{
    "body": "This looks right, though I haven't applied it yet.",
    "created_at": "2010-10-08T20:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9831#issuecomment-97019",
    "user": "@jasongrout"
}
```

This looks right, though I haven't applied it yet.



---

archive/issue_comments_097020.json:
```json
{
    "body": "Looks fine.  Testing with W3C validator still gives an error though:\n\n\n```\nLine 29, Column 79: The align attribute on the img element is obsolete. Use CSS instead.\n```\n\n\nBut I suppose this is for backwards compatibility?",
    "created_at": "2010-10-12T12:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9831#issuecomment-97020",
    "user": "@jdemeyer"
}
```

Looks fine.  Testing with W3C validator still gives an error though:


```
Line 29, Column 79: The align attribute on the img element is obsolete. Use CSS instead.
```


But I suppose this is for backwards compatibility?



---

archive/issue_comments_097021.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-12T12:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9831#issuecomment-97021",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097022.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-11T19:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9831#issuecomment-97022",
    "user": "@jdemeyer"
}
```

Resolution: fixed
