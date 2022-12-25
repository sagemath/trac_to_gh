# Issue 6624: remove json function from server/simple/twist.py

archive/issues_006624.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @jasongrout\n\nIn twist.py, we have our own json-encoding function, which is no longer necessary now that we use Python 2.6. It should be removed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6624\n\n",
    "created_at": "2009-07-26T05:38:49Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "remove json function from server/simple/twist.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6624",
    "user": "https://github.com/dandrake"
}
```
Assignee: boothby

CC:  @jasongrout

In twist.py, we have our own json-encoding function, which is no longer necessary now that we use Python 2.6. It should be removed.

Issue created by migration from https://trac.sagemath.org/ticket/6624





---

archive/issue_comments_054164.json:
```json
{
    "body": "This ticket depends on #6251, which has been merged in 4.1.1.alpha1.",
    "created_at": "2009-07-26T07:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6624#issuecomment-54164",
    "user": "https://github.com/dandrake"
}
```

This ticket depends on #6251, which has been merged in 4.1.1.alpha1.



---

archive/issue_comments_054165.json:
```json
{
    "body": "Replying to [comment:1 ddrake]:\n> This ticket depends on #6251, which has been merged in 4.1.1.alpha1.\n\nAck. No, that's wrong. It *hasn't* been merged as I write this (although it almost certainly will be very soon). Also, I'm going to make a patch that depends on *both* patches at #6251.",
    "created_at": "2009-07-26T08:02:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6624#issuecomment-54165",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:1 ddrake]:
> This ticket depends on #6251, which has been merged in 4.1.1.alpha1.

Ack. No, that's wrong. It *hasn't* been merged as I write this (although it almost certainly will be very soon). Also, I'm going to make a patch that depends on *both* patches at #6251.



---

archive/issue_comments_054166.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-26T08:02:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6624#issuecomment-54166",
    "user": "https://github.com/dandrake"
}
```

Changing status from new to assigned.



---

archive/issue_comments_054167.json:
```json
{
    "body": "Changing assignee from boothby to @dandrake.",
    "created_at": "2009-07-26T08:02:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6624#issuecomment-54167",
    "user": "https://github.com/dandrake"
}
```

Changing assignee from boothby to @dandrake.



---

archive/issue_comments_054168.json:
```json
{
    "body": "I've #6576 closed as a duplicate of this ticket.",
    "created_at": "2010-02-01T08:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6624#issuecomment-54168",
    "user": "https://github.com/qed777"
}
```

I've #6576 closed as a duplicate of this ticket.



---

archive/issue_comments_054169.json:
```json
{
    "body": "I assume that this is completely outdated with the new notebook (as well as the cell server)?",
    "created_at": "2013-06-14T17:12:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6624#issuecomment-54169",
    "user": "https://github.com/kcrisman"
}
```

I assume that this is completely outdated with the new notebook (as well as the cell server)?



---

archive/issue_comments_054170.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-06-14T17:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6624#issuecomment-54170",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_054171.json:
```json
{
    "body": "Note that #11409 would remove this completely.",
    "created_at": "2013-06-14T18:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6624#issuecomment-54171",
    "user": "https://github.com/kcrisman"
}
```

Note that #11409 would remove this completely.



---

archive/issue_comments_054172.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2013-06-14T18:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6624#issuecomment-54172",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_054173.json:
```json
{
    "body": "There is no longer any twist.py. Can we close this ticket ?",
    "created_at": "2014-02-17T12:38:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6624#issuecomment-54173",
    "user": "https://github.com/fchapoton"
}
```

There is no longer any twist.py. Can we close this ticket ?



---

archive/issue_comments_054174.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2014-02-21T22:20:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6624#issuecomment-54174",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_events_006864.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2014-02-21T22:37:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6624",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6624#event-6864"
}
```



---

archive/issue_comments_054175.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2014-02-21T22:37:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6624#issuecomment-54175",
    "user": "https://github.com/vbraun"
}
```

Resolution: wontfix
