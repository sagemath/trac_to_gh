# Issue 3958: interact gives "unterminated string literal" in the browser

archive/issues_003958.json:
```json
{
    "body": "Assignee: @itolkov\n\ntry:\n\n\n```\n@interact\ndef _(a=range_slider(-1,1),b=range_slider(-1,1),c=slider(-1,1),d=slider(-1,1)):\n    pass\n```\n\nA browser error and a \"truncated output\" error result.  The resulting interact also is missing labels and the \"c\" slider.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3958\n\n",
    "created_at": "2008-08-26T17:12:49Z",
    "labels": [
        "interact",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "interact gives \"unterminated string literal\" in the browser",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3958",
    "user": "@jasongrout"
}
```
Assignee: @itolkov

try:


```
@interact
def _(a=range_slider(-1,1),b=range_slider(-1,1),c=slider(-1,1),d=slider(-1,1)):
    pass
```

A browser error and a "truncated output" error result.  The resulting interact also is missing labels and the "c" slider.


Issue created by migration from https://trac.sagemath.org/ticket/3958





---

archive/issue_comments_028429.json:
```json
{
    "body": "This should be fixed with #3854.",
    "created_at": "2008-08-27T00:37:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3958#issuecomment-28429",
    "user": "@itolkov"
}
```

This should be fixed with #3854.



---

archive/issue_comments_028430.json:
```json
{
    "body": "This is fixed with #3854 applied.",
    "created_at": "2008-08-27T00:46:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3958#issuecomment-28430",
    "user": "@mwhansen"
}
```

This is fixed with #3854 applied.



---

archive/issue_comments_028431.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-27T00:46:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3958#issuecomment-28431",
    "user": "@mwhansen"
}
```

Resolution: fixed
