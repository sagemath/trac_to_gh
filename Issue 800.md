# Issue 800: make _sig_on and _sig_off faster when stacked

archive/issues_000800.json:
```json
{
    "body": "Assignee: @malb\n\nGonzalo brought up the following very good idea: one should rewrite the code for _sig_on and _sig_off to keep a counter of how many _sig_on calls it has seen, and run less than the full amount of code (i.e. nothing involving system calls) if we've already had a _sig_on. Then _sig_off can just decrement the counter, and only do the \"real work\" if it's being decremented to zero.\n\nIssue created by migration from https://trac.sagemath.org/ticket/800\n\n",
    "closed_at": "2011-05-15T14:41:07Z",
    "created_at": "2007-10-03T06:35:24Z",
    "labels": [
        "component: interfaces",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "make _sig_on and _sig_off faster when stacked",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/800",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @malb

Gonzalo brought up the following very good idea: one should rewrite the code for _sig_on and _sig_off to keep a counter of how many _sig_on calls it has seen, and run less than the full amount of code (i.e. nothing involving system calls) if we've already had a _sig_on. Then _sig_off can just decrement the counter, and only do the "real work" if it's being decremented to zero.

Issue created by migration from https://trac.sagemath.org/ticket/800





---

archive/issue_events_002215.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-04T14:42:19Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/800",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/800#event-2215"
}
```



---

archive/issue_comments_004809.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-24T12:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/800#issuecomment-4809",
    "user": "https://github.com/malb"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_004810.json:
```json
{
    "body": "Changing assignee from @tornaria to @malb.",
    "created_at": "2009-01-25T19:03:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/800#issuecomment-4810",
    "user": "https://github.com/malb"
}
```

Changing assignee from @tornaria to @malb.



---

archive/issue_comments_004811.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-25T19:03:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/800#issuecomment-4811",
    "user": "https://github.com/malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_004812.json:
```json
{
    "body": "This should be implemented as part of #9678.",
    "created_at": "2010-10-06T09:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/800#issuecomment-4812",
    "user": "https://github.com/jdemeyer"
}
```

This should be implemented as part of #9678.



---

archive/issue_comments_004813.json:
```json
{
    "body": "Fixed by #9678.",
    "created_at": "2011-01-14T17:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/800#issuecomment-4813",
    "user": "https://github.com/jdemeyer"
}
```

Fixed by #9678.



---

archive/issue_comments_004814.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-14T17:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/800#issuecomment-4814",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_events_002216.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-14T17:38:54Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/800",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/800#event-2216"
}
```



---

archive/issue_events_002217.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-14T17:38:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/800",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/800#event-2217"
}
```



---

archive/issue_comments_004815.json:
```json
{
    "body": "If this is a sage-duplicate/invalid/wontfix, then I believe this ticket can be closed.",
    "created_at": "2011-05-13T15:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/800#issuecomment-4815",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

If this is a sage-duplicate/invalid/wontfix, then I believe this ticket can be closed.



---

archive/issue_comments_004816.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-05-13T15:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/800#issuecomment-4816",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_002218.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-05-15T14:41:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/800",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/800#event-2218"
}
```



---

archive/issue_comments_004817.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-05-15T14:41:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/800#issuecomment-4817",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
