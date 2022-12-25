# Issue 5237: qsieve hangs on some machines when doctesting book_stein_ent.py

archive/issues_005237.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  alexghitza\n\nReported in http://groups.google.com/group/sage-devel/browse_thread/thread/894d29e0bde4550c as well as once by Alex Ghitza:\n\n```\nTrying: \n    qsieve(n)###line 289:_sage_    : qsieve(n) \nExpecting: \n    ([6340271405786663791648052309, \n      46102313108592180286398757159], '') \n*** *** Error: TIMED OUT! PROCESS KILLED! *** *** \n*** *** Error: TIMED OUT! *** *** \n         [360.3 s] \nexit code: 1024 \n```\n\n\nThis is Bill Hart's quadratic sieve, but an ancient version from 2007. We should really get rid of that code and use the current code in FLINT 1.1.x.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5237\n\n",
    "created_at": "2009-02-11T22:56:54Z",
    "labels": [
        "component: factorization",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "qsieve hangs on some machines when doctesting book_stein_ent.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5237",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: tbd

CC:  alexghitza

Reported in http://groups.google.com/group/sage-devel/browse_thread/thread/894d29e0bde4550c as well as once by Alex Ghitza:

```
Trying: 
    qsieve(n)###line 289:_sage_    : qsieve(n) 
Expecting: 
    ([6340271405786663791648052309, 
      46102313108592180286398757159], '') 
*** *** Error: TIMED OUT! PROCESS KILLED! *** *** 
*** *** Error: TIMED OUT! *** *** 
         [360.3 s] 
exit code: 1024 
```


This is Bill Hart's quadratic sieve, but an ancient version from 2007. We should really get rid of that code and use the current code in FLINT 1.1.x.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5237





---

archive/issue_comments_040053.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-01-22T10:57:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5237#issuecomment-40053",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_040054.json:
```json
{
    "body": "I assume this very old ticket is no longer relevant.",
    "created_at": "2016-01-22T10:57:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5237#issuecomment-40054",
    "user": "https://github.com/jdemeyer"
}
```

I assume this very old ticket is no longer relevant.



---

archive/issue_comments_040055.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-01-22T10:57:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5237#issuecomment-40055",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_040056.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2016-02-23T22:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5237#issuecomment-40056",
    "user": "https://github.com/vbraun"
}
```

Resolution: wontfix



---

archive/issue_events_005493.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2016-02-23T22:52:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5237",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5237#event-5493"
}
```
