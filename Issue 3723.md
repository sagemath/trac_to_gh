# Issue 3723: alarm doesn't work with the factor command on os x (but control c does)

archive/issues_003723.json:
```json
{
    "body": "Assignee: cwitty\n\n\n```\nteragon-2:~ was$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading SAGE library. Current Mercurial branch is: review\nsage: alarm(3); factor(2^997-1) \n| SAGE Version 3.0.5, Release Date: 2008-07-11                       |\n| Type notebook() for the GUI, and license() for information.        |\n#\n# and I wait 10 seconds then hit control c\n#\n\n^C---------------------------------------------------------------------------\nKeyboardInterrupt                         Traceback (most recent call last)\n\n/Users/was/s/local/lib/python2.5/site-packages/sage/misc/misc.py in __mysig(a, b)\n   1343 __alarm_time=0\n   1344 def __mysig(a,b):\n-> 1345     raise KeyboardInterrupt, \"computation timed out because alarm was set for %s seconds\"%__alarm_time\n   1346 \n   1347 def alarm(seconds):\n\nKeyboardInterrupt: computation timed out because alarm was set for 3 seconds\nsage: \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3723\n\n",
    "created_at": "2008-07-25T10:45:37Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "alarm doesn't work with the factor command on os x (but control c does)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3723",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty


```
teragon-2:~ was$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: review
sage: alarm(3); factor(2^997-1) 
| SAGE Version 3.0.5, Release Date: 2008-07-11                       |
| Type notebook() for the GUI, and license() for information.        |
#
# and I wait 10 seconds then hit control c
#

^C---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)

/Users/was/s/local/lib/python2.5/site-packages/sage/misc/misc.py in __mysig(a, b)
   1343 __alarm_time=0
   1344 def __mysig(a,b):
-> 1345     raise KeyboardInterrupt, "computation timed out because alarm was set for %s seconds"%__alarm_time
   1346 
   1347 def alarm(seconds):

KeyboardInterrupt: computation timed out because alarm was set for 3 seconds
sage: 
```


Issue created by migration from https://trac.sagemath.org/ticket/3723





---

archive/issue_comments_026351.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-05-15T13:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3723#issuecomment-26351",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_026352.json:
```json
{
    "body": "Clearly duplicate of #13311.",
    "created_at": "2013-05-15T13:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3723#issuecomment-26352",
    "user": "https://github.com/jdemeyer"
}
```

Clearly duplicate of #13311.



---

archive/issue_events_008518.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-05-15T13:37:50Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3723",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3723#event-8518"
}
```



---

archive/issue_comments_026353.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-05-15T13:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3723#issuecomment-26353",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_026354.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-05-16T07:33:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3723#issuecomment-26354",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_008519.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-05-16T07:33:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3723",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3723#event-8519"
}
```
