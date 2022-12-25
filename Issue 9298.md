# Issue 9298: Memory leak in libsingular polynomial evaluation

archive/issues_009298.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  polybori alexanderdreyer jpflori\n\n```\nsage: R.<A,B,C>=QQ[]\nsage: print get_memory_usage()\n180.0390625\nsage: for i in xrange(10000): v = A(1,8,9) # leaks\n....: \nsage: print get_memory_usage()\n181.5390625\nsage: for i in xrange(10000): v = A(1,8,9.0) # good\n....: \nsage: print get_memory_usage()\n181.5390625\nsage: for i in xrange(10000): v = A(1/2,1/3,1/4) # leaks\n....: \nsage: print get_memory_usage()\n183.5390625\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9298\n\n",
    "closed_at": "2013-01-10T09:27:12Z",
    "created_at": "2010-06-21T17:50:56Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Memory leak in libsingular polynomial evaluation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9298",
    "user": "https://github.com/robertwb"
}
```
Assignee: @malb

CC:  polybori alexanderdreyer jpflori

```
sage: R.<A,B,C>=QQ[]
sage: print get_memory_usage()
180.0390625
sage: for i in xrange(10000): v = A(1,8,9) # leaks
....: 
sage: print get_memory_usage()
181.5390625
sage: for i in xrange(10000): v = A(1,8,9.0) # good
....: 
sage: print get_memory_usage()
181.5390625
sage: for i in xrange(10000): v = A(1/2,1/3,1/4) # leaks
....: 
sage: print get_memory_usage()
183.5390625
```

Issue created by migration from https://trac.sagemath.org/ticket/9298





---

archive/issue_comments_087452.json:
```json
{
    "body": "There's a new version of Singular likely to be merged soon (#8059). I'd retest then.\n\nDave",
    "created_at": "2010-08-10T18:40:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9298#issuecomment-87452",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

There's a new version of Singular likely to be merged soon (#8059). I'd retest then.

Dave



---

archive/issue_events_022907.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/Bouillaguet",
    "created_at": "2013-01-02T14:57:51Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9298",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9298#event-22907"
}
```



---

archive/issue_comments_087453.json:
```json
{
    "body": "Indeed, the leak seems fixed. This ticket can be closed.",
    "created_at": "2013-01-02T14:57:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9298#issuecomment-87453",
    "user": "https://trac.sagemath.org/admin/accounts/users/Bouillaguet"
}
```

Indeed, the leak seems fixed. This ticket can be closed.



---

archive/issue_comments_087454.json:
```json
{
    "body": "Changing assignee from tbd to @malb.",
    "created_at": "2013-01-02T14:57:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9298#issuecomment-87454",
    "user": "https://trac.sagemath.org/admin/accounts/users/Bouillaguet"
}
```

Changing assignee from tbd to @malb.



---

archive/issue_comments_087455.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-01-02T14:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9298#issuecomment-87455",
    "user": "https://trac.sagemath.org/admin/accounts/users/Bouillaguet"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087456.json:
```json
{
    "body": "Since the ticker cannot easily be doctested, and I cannot reproduce the leak, I suggest we close it.",
    "created_at": "2013-01-04T13:42:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9298#issuecomment-87456",
    "user": "https://trac.sagemath.org/admin/accounts/users/Bouillaguet"
}
```

Since the ticker cannot easily be doctested, and I cannot reproduce the leak, I suggest we close it.



---

archive/issue_comments_087457.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-04T13:42:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9298#issuecomment-87457",
    "user": "https://trac.sagemath.org/admin/accounts/users/Bouillaguet"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_022908.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-01-10T09:27:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9298",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9298#event-22908"
}
```



---

archive/issue_comments_087458.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-01-10T09:27:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9298#issuecomment-87458",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
