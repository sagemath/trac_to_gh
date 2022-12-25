# Issue 9831: Invalid HTML in data/sage/html/login.html

archive/issues_009831.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @jasongrout\n\nThe W3C validator gives errors about missing targets for the <label> elements.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9832\n\n",
    "created_at": "2010-08-28T13:42:47Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "Invalid HTML in data/sage/html/login.html",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9831",
    "user": "https://github.com/TimDumol"
}
```
Assignee: jason, was

CC:  @jasongrout

The W3C validator gives errors about missing targets for the <label> elements.

Issue created by migration from https://trac.sagemath.org/ticket/9832





---

archive/issue_comments_096856.json:
```json
{
    "body": "Fixes the error.",
    "created_at": "2010-08-28T13:43:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9831#issuecomment-96856",
    "user": "https://github.com/TimDumol"
}
```

Fixes the error.



---

archive/issue_comments_096857.json:
```json
{
    "body": "Attachment [trac_9832-invalid-html.patch](tarball://root/attachments/some-uuid/ticket9832/trac_9832-invalid-html.patch) by @TimDumol created at 2010-08-28 14:15:48",
    "created_at": "2010-08-28T14:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9831#issuecomment-96857",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_9832-invalid-html.patch](tarball://root/attachments/some-uuid/ticket9832/trac_9832-invalid-html.patch) by @TimDumol created at 2010-08-28 14:15:48



---

archive/issue_comments_096858.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-28T14:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9831#issuecomment-96858",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096859.json:
```json
{
    "body": "Changing assignee from jason, was to @jasongrout.",
    "created_at": "2010-10-08T20:49:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9831#issuecomment-96859",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from jason, was to @jasongrout.



---

archive/issue_comments_096860.json:
```json
{
    "body": "This looks right, though I haven't applied it yet.",
    "created_at": "2010-10-08T20:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9831#issuecomment-96860",
    "user": "https://github.com/jasongrout"
}
```

This looks right, though I haven't applied it yet.



---

archive/issue_comments_096861.json:
```json
{
    "body": "Looks fine.  Testing with W3C validator still gives an error though:\n\n\n```\nLine 29, Column 79: The align attribute on the img element is obsolete. Use CSS instead.\n```\n\n\nBut I suppose this is for backwards compatibility?",
    "created_at": "2010-10-12T12:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9831#issuecomment-96861",
    "user": "https://github.com/jdemeyer"
}
```

Looks fine.  Testing with W3C validator still gives an error though:


```
Line 29, Column 79: The align attribute on the img element is obsolete. Use CSS instead.
```


But I suppose this is for backwards compatibility?



---

archive/issue_comments_096862.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-12T12:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9831#issuecomment-96862",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096863.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-11T19:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9831#issuecomment-96863",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_009953.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2010-11-11T19:37:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9831",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9831#event-9953"
}
```
