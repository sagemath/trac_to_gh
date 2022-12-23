# Issue 7346: notebook -- needless vertical scroll bars on output

archive/issues_007346.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\nI mentioned this on IRC, but just to make sure it doesn't fall through the cracks:\n\nWhen the jsmath fonts are installed, the following input gives an output that the browser thinks is slightly bigger than the output div area.\nvar('x_1')\n\nprint jsmath(sqrt(x_1/x))\n\n\nSince the output div has a (calculated) style of overflow-y: auto, a scrollbar appears on the right of the output div.  However, everything is visible without scrolling, and scrolling down just scrolls the answer out of view.\n\nI think the best thing we can do in this case is make overflow-y: hidden for output divs, or some other value so that scroll bars do not appear.  In other words, in the CSS file:\n\ndiv.cell_output_div {\noverflow-x:auto;\noverflow-y:hidden;\n}\n\n\nThanks,\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7346\n\n",
    "created_at": "2009-10-29T07:04:01Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook -- needless vertical scroll bars on output",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7346",
    "user": "was"
}
```
Assignee: boothby


```
I mentioned this on IRC, but just to make sure it doesn't fall through the cracks:

When the jsmath fonts are installed, the following input gives an output that the browser thinks is slightly bigger than the output div area.
var('x_1')

print jsmath(sqrt(x_1/x))


Since the output div has a (calculated) style of overflow-y: auto, a scrollbar appears on the right of the output div.  However, everything is visible without scrolling, and scrolling down just scrolls the answer out of view.

I think the best thing we can do in this case is make overflow-y: hidden for output divs, or some other value so that scroll bars do not appear.  In other words, in the CSS file:

div.cell_output_div {
overflow-x:auto;
overflow-y:hidden;
}


Thanks,
```


Issue created by migration from https://trac.sagemath.org/ticket/7346





---

archive/issue_comments_061564.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-10-29T07:04:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7346#issuecomment-61564",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_061565.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-29T07:05:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7346#issuecomment-61565",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061566.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-06T05:59:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7346#issuecomment-61566",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061567.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-09T17:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7346#issuecomment-61567",
    "user": "was"
}
```

Resolution: fixed
