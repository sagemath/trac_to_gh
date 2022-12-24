# Issue 362: str --> basestring

archive/issues_000362.json:
```json
{
    "body": "Assignee: @williamstein\n\nType this\n\n```\n  sage: search_src(\", str)\")\n```\n\nIn most cases change isinstance(..., str) to isinstance(..., basestring),\nsince unicode is getting more and more standard, and things break otherwise. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/362\n\n",
    "created_at": "2007-05-10T16:58:33Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "title": "str --> basestring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/362",
    "user": "@williamstein"
}
```
Assignee: @williamstein

Type this

```
  sage: search_src(", str)")
```

In most cases change isinstance(..., str) to isinstance(..., basestring),
since unicode is getting more and more standard, and things break otherwise. 


Issue created by migration from https://trac.sagemath.org/ticket/362





---

archive/issue_comments_001761.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-05-31T15:10:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/362#issuecomment-1761",
    "user": "@williamstein"
}
```

Resolution: fixed
