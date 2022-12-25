# Issue 819: linenumbers in python inspect are 0-based

archive/issues_000819.json:
```json
{
    "body": "Assignee: @robertwb\n\npython's inspect.findsource returns a line number that is 0-based, because the source\nfile is considered to be a list of lines. sage.misc.sageinspect._extract_embedded_position tries to return similar data, but does so 1-based. We should probably be consistent about how line numbers are handled.\n\nLine numbers *SHOULD* be 1-based, of course, but we cannot change python's library. \n\nAt the same time, python's \"inspect\" does not have a routine to just give back a line number. It always gives the source itself as well.\n\nPerhaps the solution is to include into sageinspect a routine that gives back file name and line number? The routine \"fileandline\" included in patch #768 tries to do this. Perhaps it should be included in sageinspect and thus hide the discrepancy between 0- and 1-based line numbers that currently becomes visible because functionality has to be borrowed from both \"inspect\" and \"sageinspect\"?\n\nIssue created by migration from https://trac.sagemath.org/ticket/819\n\n",
    "created_at": "2007-10-04T03:06:52Z",
    "labels": [
        "component: user interface",
        "minor",
        "bug"
    ],
    "title": "linenumbers in python inspect are 0-based",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/819",
    "user": "https://github.com/nbruin"
}
```
Assignee: @robertwb

python's inspect.findsource returns a line number that is 0-based, because the source
file is considered to be a list of lines. sage.misc.sageinspect._extract_embedded_position tries to return similar data, but does so 1-based. We should probably be consistent about how line numbers are handled.

Line numbers *SHOULD* be 1-based, of course, but we cannot change python's library. 

At the same time, python's "inspect" does not have a routine to just give back a line number. It always gives the source itself as well.

Perhaps the solution is to include into sageinspect a routine that gives back file name and line number? The routine "fileandline" included in patch #768 tries to do this. Perhaps it should be included in sageinspect and thus hide the discrepancy between 0- and 1-based line numbers that currently becomes visible because functionality has to be borrowed from both "inspect" and "sageinspect"?

Issue created by migration from https://trac.sagemath.org/ticket/819





---

archive/issue_events_002304.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/819",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/819#event-2304"
}
```



---

archive/issue_events_002305.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/819",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/819#event-2305"
}
```



---

archive/issue_events_002306.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/819",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/819#event-2306"
}
```



---

archive/issue_events_002307.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/819",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/819#event-2307"
}
```



---

archive/issue_events_002308.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/819",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/819#event-2308"
}
```



---

archive/issue_events_002309.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/819",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/819#event-2309"
}
```



---

archive/issue_events_002310.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/819",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/819#event-2310"
}
```



---

archive/issue_comments_005066.json:
```json
{
    "body": "I doubt we want to change the convention at this point.",
    "created_at": "2015-04-13T16:10:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/819#issuecomment-5066",
    "user": "https://github.com/mezzarobba"
}
```

I doubt we want to change the convention at this point.



---

archive/issue_comments_005067.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-04-13T16:10:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/819#issuecomment-5067",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_events_002311.json:
```json
{
    "actor": "https://github.com/mezzarobba",
    "created_at": "2015-04-13T16:10:24Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/819",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/819#event-2311"
}
```



---

archive/issue_events_002312.json:
```json
{
    "actor": "https://github.com/mezzarobba",
    "created_at": "2015-04-13T16:10:24Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/819",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/819#event-2312"
}
```



---

archive/issue_comments_005068.json:
```json
{
    "body": "Replying to [comment:5 mmezzarobba]:\n> I doubt we want to change the convention at this point.\n\nwhy?",
    "created_at": "2015-04-14T09:39:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/819#issuecomment-5068",
    "user": "https://github.com/videlec"
}
```

Replying to [comment:5 mmezzarobba]:
> I doubt we want to change the convention at this point.

why?



---

archive/issue_comments_005069.json:
```json
{
    "body": "Replying to [comment:6 vdelecroix]:\n> Replying to [comment:5 mmezzarobba]:\n> > I doubt we want to change the convention at this point.\n> \n> why?\n\nI misread the description and thought the idea was to make `sageinspect` return 0-based line numbers. Sorry for the noise.",
    "created_at": "2015-04-14T09:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/819#issuecomment-5069",
    "user": "https://github.com/mezzarobba"
}
```

Replying to [comment:6 vdelecroix]:
> Replying to [comment:5 mmezzarobba]:
> > I doubt we want to change the convention at this point.
> 
> why?

I misread the description and thought the idea was to make `sageinspect` return 0-based line numbers. Sorry for the noise.



---

archive/issue_events_002313.json:
```json
{
    "actor": "https://github.com/mezzarobba",
    "created_at": "2015-04-14T09:49:30Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/819",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/819#event-2313"
}
```



---

archive/issue_comments_005070.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-04-14T09:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/819#issuecomment-5070",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from needs_review to needs_work.
