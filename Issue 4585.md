# Issue 4585: "sage -upgrade" shall call the "sage-location" script

archive/issues_004585.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nOn a system where \"root\" upgrades incrementally a system-wide Sage installation, and only \"normal\" users ever run Sage, there might be trouble.\n\nMore precisely, the rights to create the \"sage-flags.txt\" file --- or also the \"sage-location.txt\" file --- might not be owned by the normal user.\n\nEven if this would be only a corner case, the obvious fix (run \"sage-starts\" once during sage -upgrade\") does not hurt anybody, hence this ticket. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4585\n\n",
    "closed_at": "2013-05-21T07:23:55Z",
    "created_at": "2008-11-22T22:46:31Z",
    "labels": [
        "component: build",
        "trivial"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "\"sage -upgrade\" shall call the \"sage-location\" script",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4585",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```
Assignee: GeorgSWeber

On a system where "root" upgrades incrementally a system-wide Sage installation, and only "normal" users ever run Sage, there might be trouble.

More precisely, the rights to create the "sage-flags.txt" file --- or also the "sage-location.txt" file --- might not be owned by the normal user.

Even if this would be only a corner case, the obvious fix (run "sage-starts" once during sage -upgrade") does not hurt anybody, hence this ticket. 

Issue created by migration from https://trac.sagemath.org/ticket/4585





---

archive/issue_comments_034314.json:
```json
{
    "body": "Changing assignee from mabshoff to GeorgSWeber.",
    "created_at": "2008-11-22T22:50:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4585#issuecomment-34314",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Changing assignee from mabshoff to GeorgSWeber.



---

archive/issue_comments_034315.json:
```json
{
    "body": "Hmmm,\n\nit's better to call the \"sage-location\" script directly, because starting Sage as \"root\" will create certain files/directories (.sage/...) in root's home directory, which is avoidable.",
    "created_at": "2008-11-23T08:04:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4585#issuecomment-34315",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Hmmm,

it's better to call the "sage-location" script directly, because starting Sage as "root" will create certain files/directories (.sage/...) in root's home directory, which is avoidable.



---

archive/issue_comments_034316.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-05-19T13:19:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4585#issuecomment-34316",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_034317.json:
```json
{
    "body": "`sage-location` is run when doing `sage --upgrade`.",
    "created_at": "2013-05-19T13:19:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4585#issuecomment-34317",
    "user": "https://github.com/jdemeyer"
}
```

`sage-location` is run when doing `sage --upgrade`.



---

archive/issue_events_010432.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-05-19T13:19:04Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4585",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4585#event-10432"
}
```



---

archive/issue_comments_034318.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-05-19T13:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4585#issuecomment-34318",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_034319.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-05-21T07:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4585#issuecomment-34319",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme



---

archive/issue_events_010433.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-05-21T07:23:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4585",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4585#event-10433"
}
```
