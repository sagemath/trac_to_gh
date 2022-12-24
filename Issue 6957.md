# Issue 6957: $SAGE_DATA/extcode/javascript/jsmath appears to be the same as $SAGE_LOCAL/notebook/javascript/jsmath

archive/issues_006957.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis appears to be a duplicate directory tree.\n\nThe other places where there are javascript files appear to not share any files.\n\nI just tried moving $SAGE_DATA/extcode/javascript/jsmath from a sage 4.1.1 binary downloaded from a mirror, and the notebook appears to runs just fine.\n\nIf this is really a duplicate, it can reduce a sage install by around 18Mb.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6957\n\n",
    "created_at": "2009-09-18T23:10:48Z",
    "labels": [
        "packages: standard",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "$SAGE_DATA/extcode/javascript/jsmath appears to be the same as $SAGE_LOCAL/notebook/javascript/jsmath",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6957",
    "user": "pcpa"
}
```
Assignee: mabshoff

This appears to be a duplicate directory tree.

The other places where there are javascript files appear to not share any files.

I just tried moving $SAGE_DATA/extcode/javascript/jsmath from a sage 4.1.1 binary downloaded from a mirror, and the notebook appears to runs just fine.

If this is really a duplicate, it can reduce a sage install by around 18Mb.


Issue created by migration from https://trac.sagemath.org/ticket/6957





---

archive/issue_comments_057550.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-05-16T07:55:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6957#issuecomment-57550",
    "user": "@jdemeyer"
}
```

Resolution: worksforme



---

archive/issue_comments_057551.json:
```json
{
    "body": "Fixed already.",
    "created_at": "2013-05-16T07:55:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6957#issuecomment-57551",
    "user": "@jdemeyer"
}
```

Fixed already.
