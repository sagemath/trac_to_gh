# Issue 6277: sage -tp a.py a.py will test a.py twice

archive/issues_006277.json:
```json
{
    "body": "Assignee: tbd\n\nI think this is a bug, but maybe not.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6277\n\n",
    "created_at": "2009-06-13T19:45:17Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "sage -tp a.py a.py will test a.py twice",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6277",
    "user": "https://github.com/ncalexan"
}
```
Assignee: tbd

I think this is a bug, but maybe not.

Issue created by migration from https://trac.sagemath.org/ticket/6277





---

archive/issue_events_006521.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2009-06-14T09:54:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6277",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6277#event-6521"
}
```



---

archive/issue_comments_050040.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-06-14T09:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6277#issuecomment-50040",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid



---

archive/issue_comments_050041.json:
```json
{
    "body": "Just for the record, \n`sage -tp a.py a.py`\nresults in \n\n```\nValueError: invalid literal for int() with base 10: 'devel/sage/sage/rings/arith.py'\n```\n\nso I'm fixing the title of the ticket.  \n\nI also consider this invalid.  There are good reasons to want to test the same file a bunch of times, e.g.,\n\n```\nsage -tp 10 a.py a.py  a.py a.py a.py a.py a.py a.py a.py a.py a.py\n```\n\nwould be very useful when tracking down errors that only happen with some probability.",
    "created_at": "2009-06-14T09:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6277#issuecomment-50041",
    "user": "https://github.com/williamstein"
}
```

Just for the record, 
`sage -tp a.py a.py`
results in 

```
ValueError: invalid literal for int() with base 10: 'devel/sage/sage/rings/arith.py'
```

so I'm fixing the title of the ticket.  

I also consider this invalid.  There are good reasons to want to test the same file a bunch of times, e.g.,

```
sage -tp 10 a.py a.py  a.py a.py a.py a.py a.py a.py a.py a.py a.py
```

would be very useful when tracking down errors that only happen with some probability.
