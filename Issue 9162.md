# Issue 9162: cygwin:

archive/issues_009162.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  snark\n\nThis is a followup to #8847, which was supposed to fix this, but simply didn't. \n\n\n```\n\nsage -t  \"devel/sage/sage/functions/other.py\"               \n**********************************************************************\nFile \"/home/wstein/sage-4.4.3/devel/sage/sage/functions/other.py\", line 475:\n    sage: gamma1(float(6))\nExpected:\n    120.0\nGot:\n    119.99999999999997\n**********************************************************************\n1 items had failures:\n   1 of  29 in __main__.example_12\n```\n\n\nSee #8847 for more details.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9162\n\n",
    "created_at": "2010-06-07T03:57:50Z",
    "labels": [
        "component: porting: cygwin",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "cygwin:",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9162",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  snark

This is a followup to #8847, which was supposed to fix this, but simply didn't. 


```

sage -t  "devel/sage/sage/functions/other.py"               
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/functions/other.py", line 475:
    sage: gamma1(float(6))
Expected:
    120.0
Got:
    119.99999999999997
**********************************************************************
1 items had failures:
   1 of  29 in __main__.example_12
```


See #8847 for more details.

Issue created by migration from https://trac.sagemath.org/ticket/9162





---

archive/issue_comments_085395.json:
```json
{
    "body": "I don't think that #8847 was supposed to fix this.  #8847 was to make it so that we get 120.0 instead of 119.99999999999997 on Linux.  Cygwin has always given 119.9999...",
    "created_at": "2010-06-07T08:58:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9162#issuecomment-85395",
    "user": "https://github.com/mwhansen"
}
```

I don't think that #8847 was supposed to fix this.  #8847 was to make it so that we get 120.0 instead of 119.99999999999997 on Linux.  Cygwin has always given 119.9999...



---

archive/issue_comments_085396.json:
```json
{
    "body": "Somewhat miraculously, this passes tests on a recent build of mine on XP.  Perhaps due to using mpmath now or something?",
    "created_at": "2011-08-02T02:31:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9162#issuecomment-85396",
    "user": "https://github.com/kcrisman"
}
```

Somewhat miraculously, this passes tests on a recent build of mine on XP.  Perhaps due to using mpmath now or something?



---

archive/issue_comments_085397.json:
```json
{
    "body": "But this, once again, does *not* pass when done by hand.  What is going on?",
    "created_at": "2011-08-19T14:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9162#issuecomment-85397",
    "user": "https://github.com/kcrisman"
}
```

But this, once again, does *not* pass when done by hand.  What is going on?



---

archive/issue_comments_085398.json:
```json
{
    "body": "exactly the same problem also pops up on ARM running Ubuntu 11.10.",
    "created_at": "2012-01-17T03:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9162#issuecomment-85398",
    "user": "https://github.com/dimpase"
}
```

exactly the same problem also pops up on ARM running Ubuntu 11.10.



---

archive/issue_comments_085399.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-02-13T11:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9162#issuecomment-85399",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_events_022544.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2012-02-13T11:10:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9162",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9162#event-22544"
}
```



---

archive/issue_comments_085400.json:
```json
{
    "body": "#12449 contains a patch to fix. We should close this as a duplicate.",
    "created_at": "2012-02-13T11:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9162#issuecomment-85400",
    "user": "https://github.com/burcin"
}
```

#12449 contains a patch to fix. We should close this as a duplicate.



---

archive/issue_comments_085401.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-02-13T11:13:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9162#issuecomment-85401",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_022545.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-02-16T21:32:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9162",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9162#event-22545"
}
```



---

archive/issue_comments_085402.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-02-16T21:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9162#issuecomment-85402",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
