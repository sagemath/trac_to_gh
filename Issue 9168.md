# Issue 9168: cygwin: ratpoints does not work correctly

archive/issues_009168.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  jpflori\n\nSome ratpoints tests fail on cygwin, e.g.:\n\n```\n\nsage -t  \"devel/sage/sage/libs/ratpoints.pyx\"               \n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/libs/ratpoints.pyx\", line 57:\n    sage: for x,y,z in ratpoints([1..6], 200):\n       print -Integer(1)*y**Integer(2) + Integer(1)*z**Integer(6) + Integer(2)*x*z**Integer(5) + Integer(3)*x**Integer(2)*z**Integer(4) + Integer(4)*x**Integer(3)*z**Integer(3) + Integer(5)*x**Integer(4)*z**Integer(2) + Integer(6)*x**Integer(5)*z\nExpected:\n    0\n    0\n    0\n    0\n    0\n    0\n    0\nGot:\n    0\n    0\n    0\n```\n\n\nWhat happens when the same is done manually:\n\n\n```\n\nsage: from sage.libs.ratpoints import ratpoints\nsage: \nsage: for x,y,z in ratpoints([1..6], 200):\n....:     print -1*y^2 + 1*z^6 + 2*x*z^5 + 3*x^2*z^4 + 4*x^3*z^3 + 5*x^4*z^2 + 6*x^5*z\n....:     \n0\n0\n0\n```\n\n\nSo the problem is simply that less points are found.  Sounds pretty serious...\n\nIssue created by migration from https://trac.sagemath.org/ticket/9168\n\n",
    "created_at": "2010-06-07T04:28:53Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "cygwin: ratpoints does not work correctly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9168",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  jpflori

Some ratpoints tests fail on cygwin, e.g.:

```

sage -t  "devel/sage/sage/libs/ratpoints.pyx"               
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/libs/ratpoints.pyx", line 57:
    sage: for x,y,z in ratpoints([1..6], 200):
       print -Integer(1)*y**Integer(2) + Integer(1)*z**Integer(6) + Integer(2)*x*z**Integer(5) + Integer(3)*x**Integer(2)*z**Integer(4) + Integer(4)*x**Integer(3)*z**Integer(3) + Integer(5)*x**Integer(4)*z**Integer(2) + Integer(6)*x**Integer(5)*z
Expected:
    0
    0
    0
    0
    0
    0
    0
Got:
    0
    0
    0
```


What happens when the same is done manually:


```

sage: from sage.libs.ratpoints import ratpoints
sage: 
sage: for x,y,z in ratpoints([1..6], 200):
....:     print -1*y^2 + 1*z^6 + 2*x*z^5 + 3*x^2*z^4 + 4*x^3*z^3 + 5*x^4*z^2 + 6*x^5*z
....:     
0
0
0
```


So the problem is simply that less points are found.  Sounds pretty serious...

Issue created by migration from https://trac.sagemath.org/ticket/9168





---

archive/issue_comments_085587.json:
```json
{
    "body": "This files passes tests on a recent build on XP.",
    "created_at": "2011-08-02T02:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9168#issuecomment-85587",
    "user": "https://github.com/kcrisman"
}
```

This files passes tests on a recent build on XP.



---

archive/issue_comments_085588.json:
```json
{
    "body": "But the same thing happens by hand. Why are all these tests passing on Cygwin?",
    "created_at": "2011-08-19T14:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9168#issuecomment-85588",
    "user": "https://github.com/kcrisman"
}
```

But the same thing happens by hand. Why are all these tests passing on Cygwin?



---

archive/issue_comments_085589.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-01-15T16:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9168#issuecomment-85589",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085590.json:
```json
{
    "body": "This now passes, *and* when I do it by hand I do indeed get seven zeros.  JP, if you can confirm this, then we can close this ticket as no longer valid.",
    "created_at": "2013-01-15T16:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9168#issuecomment-85590",
    "user": "https://github.com/kcrisman"
}
```

This now passes, *and* when I do it by hand I do indeed get seven zeros.  JP, if you can confirm this, then we can close this ticket as no longer valid.



---

archive/issue_comments_085591.json:
```json
{
    "body": "Works for me too.",
    "created_at": "2013-01-15T17:54:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9168#issuecomment-85591",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Works for me too.



---

archive/issue_comments_085592.json:
```json
{
    "body": "Changing keywords from \"\" to \"cygwin\".",
    "created_at": "2013-01-15T17:54:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9168#issuecomment-85592",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing keywords from "" to "cygwin".



---

archive/issue_comments_085593.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-15T17:54:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9168#issuecomment-85593",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085594.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-01-17T10:04:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9168#issuecomment-85594",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme



---

archive/issue_events_009325.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2013-01-17T10:04:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9168",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9168#event-9325"
}
```
