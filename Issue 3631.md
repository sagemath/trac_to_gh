# Issue 3631: pbuild broken by binary *.pyc files in extcode

archive/issues_003631.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nThe pbuild install in 3.0.4 was broken by (among other things) *.pyc files left in data/extcode/sagebuild.  All pyc files here should automatically get nuked when the spkg is created. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3631\n\n",
    "created_at": "2008-07-10T08:57:57Z",
    "labels": [
        "component: pbuild",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "pbuild broken by binary *.pyc files in extcode",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3631",
    "user": "https://github.com/garyfurnish"
}
```
Assignee: @garyfurnish

The pbuild install in 3.0.4 was broken by (among other things) *.pyc files left in data/extcode/sagebuild.  All pyc files here should automatically get nuked when the spkg is created. 

Issue created by migration from https://trac.sagemath.org/ticket/3631





---

archive/issue_comments_025635.json:
```json
{
    "body": "Changing assignee from @garyfurnish to mabshoff.",
    "created_at": "2008-07-14T10:49:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3631#issuecomment-25635",
    "user": "https://github.com/garyfurnish"
}
```

Changing assignee from @garyfurnish to mabshoff.



---

archive/issue_events_008334.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-03-12T21:30:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3631",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3631#event-8334"
}
```



---

archive/issue_comments_025636.json:
```json
{
    "body": "This is no longer relevant in sage-5.0, since any file which doesn't belong in the repository will be detected by `hg status`.",
    "created_at": "2012-03-12T21:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3631#issuecomment-25636",
    "user": "https://github.com/jdemeyer"
}
```

This is no longer relevant in sage-5.0, since any file which doesn't belong in the repository will be detected by `hg status`.



---

archive/issue_events_008335.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-03-12T21:30:02Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3631",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3631#event-8335"
}
```



---

archive/issue_comments_025637.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2012-03-12T21:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3631#issuecomment-25637",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid
