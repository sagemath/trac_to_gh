# Issue 9209: Sage build can go wrong if there is a python install in /usr/local.

archive/issues_009209.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @jasongrout\n\nThere are at least two failed reports of Sage failing to build properly if there is an installation of python in /usr/local\n\n* http://groups.google.com/group/sage-solaris/browse_thread/thread/5dcc7ed68d279f67?hl=en\n* http://groups.google.com/group/sage-devel/browse_thread/thread/37a67ce63e68d55b?hl=en-GB\n\nwhere an installation in /usr/local of python screw up Sage. \n\nIn my own case, the only way I could find to stop the install in /usr/local preventing Sage building, was to execute as root\n\n```\nchmod 000 /usr/local/lib/libpython2.6.a /usr/local/lib/python2.6\n```\n\nDave\n\nIssue created by migration from https://trac.sagemath.org/ticket/9209\n\n",
    "created_at": "2010-06-10T23:45:54Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Sage build can go wrong if there is a python install in /usr/local.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9209",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: GeorgSWeber

CC:  @jasongrout

There are at least two failed reports of Sage failing to build properly if there is an installation of python in /usr/local

* http://groups.google.com/group/sage-solaris/browse_thread/thread/5dcc7ed68d279f67?hl=en
* http://groups.google.com/group/sage-devel/browse_thread/thread/37a67ce63e68d55b?hl=en-GB

where an installation in /usr/local of python screw up Sage. 

In my own case, the only way I could find to stop the install in /usr/local preventing Sage building, was to execute as root

```
chmod 000 /usr/local/lib/libpython2.6.a /usr/local/lib/python2.6
```

Dave

Issue created by migration from https://trac.sagemath.org/ticket/9209





---

archive/issue_comments_086058.json:
```json
{
    "body": "Changing assignee from GeorgSWeber to drkirkby.",
    "created_at": "2010-06-11T00:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9209#issuecomment-86058",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from GeorgSWeber to drkirkby.



---

archive/issue_comments_086059.json:
```json
{
    "body": "Remove assignee drkirkby.",
    "created_at": "2010-06-11T00:49:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9209#issuecomment-86059",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Remove assignee drkirkby.



---

archive/issue_comments_086060.json:
```json
{
    "body": "Set assignee to GeorgSWeber.",
    "created_at": "2010-06-11T00:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9209#issuecomment-86060",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Set assignee to GeorgSWeber.



---

archive/issue_events_022680.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9209#event-22680"
}
```



---

archive/issue_events_022681.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9209#event-22681"
}
```



---

archive/issue_events_022682.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9209#event-22682"
}
```



---

archive/issue_events_022683.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9209#event-22683"
}
```



---

archive/issue_events_022684.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9209#event-22684"
}
```



---

archive/issue_events_022685.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9209#event-22685"
}
```



---

archive/issue_events_022686.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9209#event-22686"
}
```



---

archive/issue_comments_086061.json:
```json
{
    "body": "Does this still happen?",
    "created_at": "2015-01-09T14:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9209#issuecomment-86061",
    "user": "https://github.com/a-andre"
}
```

Does this still happen?



---

archive/issue_comments_086062.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2017-04-19T13:14:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9209#issuecomment-86062",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_events_022687.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2017-04-19T13:14:42Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9209#event-22687"
}
```



---

archive/issue_events_022688.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2017-04-19T13:14:42Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9209#event-22688"
}
```



---

archive/issue_comments_086063.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-04-19T13:14:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9209#issuecomment-86063",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_022689.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2017-07-13T07:54:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9209#event-22689"
}
```



---

archive/issue_comments_086064.json:
```json
{
    "body": "Closing tickets in the sage-duplicate/invalid/wontfix module with positive_review (i.e. someone has confirmed they should be closed).",
    "created_at": "2017-07-13T07:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9209#issuecomment-86064",
    "user": "https://github.com/embray"
}
```

Closing tickets in the sage-duplicate/invalid/wontfix module with positive_review (i.e. someone has confirmed they should be closed).



---

archive/issue_comments_086065.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2017-07-13T07:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9209#issuecomment-86065",
    "user": "https://github.com/embray"
}
```

Resolution: wontfix
