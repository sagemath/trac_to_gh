# Issue 800: make _sig_on and _sig_off faster when stacked

archive/issues_000800.json:
```json
{
    "body": "Assignee: @tornaria\n\nGonzalo brought up the following very good idea: one should rewrite the code for _sig_on and _sig_off to keep a counter of how many _sig_on calls it has seen, and run less than the full amount of code (i.e. nothing involving system calls) if we've already had a _sig_on. Then _sig_off can just decrement the counter, and only do the \"real work\" if it's being decremented to zero.\n\nIssue created by migration from https://trac.sagemath.org/ticket/800\n\n",
    "created_at": "2007-10-03T06:35:24Z",
    "labels": [
        "interfaces",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "make _sig_on and _sig_off faster when stacked",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/800",
    "user": "@craigcitro"
}
```
Assignee: @tornaria

Gonzalo brought up the following very good idea: one should rewrite the code for _sig_on and _sig_off to keep a counter of how many _sig_on calls it has seen, and run less than the full amount of code (i.e. nothing involving system calls) if we've already had a _sig_on. Then _sig_off can just decrement the counter, and only do the "real work" if it's being decremented to zero.

Issue created by migration from https://trac.sagemath.org/ticket/800





---

archive/issue_comments_004825.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-24T12:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/800#issuecomment-4825",
    "user": "@malb"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_004826.json:
```json
{
    "body": "Changing assignee from @tornaria to @malb.",
    "created_at": "2009-01-25T19:03:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/800#issuecomment-4826",
    "user": "@malb"
}
```

Changing assignee from @tornaria to @malb.



---

archive/issue_comments_004827.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-25T19:03:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/800#issuecomment-4827",
    "user": "@malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_004828.json:
```json
{
    "body": "This should be implemented as part of #9678.",
    "created_at": "2010-10-06T09:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/800#issuecomment-4828",
    "user": "@jdemeyer"
}
```

This should be implemented as part of #9678.



---

archive/issue_comments_004829.json:
```json
{
    "body": "Fixed by #9678.",
    "created_at": "2011-01-14T17:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/800#issuecomment-4829",
    "user": "@jdemeyer"
}
```

Fixed by #9678.



---

archive/issue_comments_004830.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-14T17:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/800#issuecomment-4830",
    "user": "@jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_004831.json:
```json
{
    "body": "If this is a sage-duplicate/invalid/wontfix, then I believe this ticket can be closed.",
    "created_at": "2011-05-13T15:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/800#issuecomment-4831",
    "user": "mariah"
}
```

If this is a sage-duplicate/invalid/wontfix, then I believe this ticket can be closed.



---

archive/issue_comments_004832.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-05-13T15:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/800#issuecomment-4832",
    "user": "mariah"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_004833.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-05-15T14:41:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/800#issuecomment-4833",
    "user": "@jdemeyer"
}
```

Resolution: duplicate
