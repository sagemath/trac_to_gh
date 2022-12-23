# Issue 1170: Behaviour of the order function for infinite groups

archive/issues_001170.json:
```json
{
    "body": "Assignee: was\n\nWhen one tries to use the order function on group elements of infinite order, one gets an error:\n\ngl=GL(2,ZZ)\ng=gl.gens()[2]\ng.order()\n\nIn MAGMA, one (often) gets the answer 0 if one calls the Order function on elements of infinite order.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1170\n\n",
    "created_at": "2007-11-14T15:02:07Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "title": "Behaviour of the order function for infinite groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1170",
    "user": "ljpk"
}
```
Assignee: was

When one tries to use the order function on group elements of infinite order, one gets an error:

gl=GL(2,ZZ)
g=gl.gens()[2]
g.order()

In MAGMA, one (often) gets the answer 0 if one calls the Order function on elements of infinite order.

Issue created by migration from https://trac.sagemath.org/ticket/1170





---

archive/issue_comments_007171.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-09-04T15:43:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1170#issuecomment-7171",
    "user": "cremona"
}
```

Attachment



---

archive/issue_comments_007172.json:
```json
{
    "body": "The patch fixes this:  for consistency with other groups, +Infinity is returned as the order for group elements of infinite order.  A doctest has been added.\n\nThe patch should apply to 3.1.2.alpha4 and later, and all doctests in sage.groups pass.\n\nReview, Lloyd?",
    "created_at": "2008-09-04T15:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1170#issuecomment-7172",
    "user": "cremona"
}
```

The patch fixes this:  for consistency with other groups, +Infinity is returned as the order for group elements of infinite order.  A doctest has been added.

The patch should apply to 3.1.2.alpha4 and later, and all doctests in sage.groups pass.

Review, Lloyd?



---

archive/issue_comments_007173.json:
```json
{
    "body": "One small nitpick which I corrected in the patch I applied: The `#` in the doctests need to be escaped, i.e.\n\n```\nSee trac \\#1170\n```\n\nI am not sure if this applies in case the docstring is not raw, but let's do it so that downroad we do not get bitten by it.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-04T22:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1170#issuecomment-7173",
    "user": "mabshoff"
}
```

One small nitpick which I corrected in the patch I applied: The `#` in the doctests need to be escaped, i.e.

```
See trac \#1170
```

I am not sure if this applies in case the docstring is not raw, but let's do it so that downroad we do not get bitten by it.

Cheers,

Michael



---

archive/issue_comments_007174.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc0",
    "created_at": "2008-09-04T23:22:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1170#issuecomment-7174",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc0



---

archive/issue_comments_007175.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-04T23:22:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1170#issuecomment-7175",
    "user": "mabshoff"
}
```

Resolution: fixed
