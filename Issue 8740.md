# Issue 8740: Upgrade sqlalchemy to 0.6.0

archive/issues_008740.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  tdumol @kiwifb\n\nThe latest version of SQLAlchemy is now [0.6.0](http://www.sqlalchemy.org/trac/wiki/06Migration). This brings a bunch of changes, notably a native unicode mode, which would be a lot faster for unicode rich applications, such as the Sage Notebook.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8740\n\n",
    "created_at": "2010-04-21T19:28:18Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Upgrade sqlalchemy to 0.6.0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8740",
    "user": "https://github.com/TimDumol"
}
```
Assignee: tbd

CC:  tdumol @kiwifb

The latest version of SQLAlchemy is now [0.6.0](http://www.sqlalchemy.org/trac/wiki/06Migration). This brings a bunch of changes, notably a native unicode mode, which would be a lot faster for unicode rich applications, such as the Sage Notebook.

Issue created by migration from https://trac.sagemath.org/ticket/8740





---

archive/issue_comments_079820.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-21T19:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79820",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079821.json:
```json
{
    "body": "Now at 0.6.7 anyone wants to make a new spkg?",
    "created_at": "2011-05-31T22:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79821",
    "user": "https://github.com/kiwifb"
}
```

Now at 0.6.7 anyone wants to make a new spkg?



---

archive/issue_comments_079822.json:
```json
{
    "body": "Actually, sqlalchemy now has a release [0.7](http://www.sqlalchemy.org/download.html), and since nothing in Sage currently uses it (at least, in the standard packages), it may be best to upgrade to 0.7. What do you think?",
    "created_at": "2011-06-01T04:01:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79822",
    "user": "https://github.com/TimDumol"
}
```

Actually, sqlalchemy now has a release [0.7](http://www.sqlalchemy.org/download.html), and since nothing in Sage currently uses it (at least, in the standard packages), it may be best to upgrade to 0.7. What do you think?



---

archive/issue_comments_079823.json:
```json
{
    "body": "Replying to [comment:5 timdumol]:\n> Actually, sqlalchemy now has a release [0.7](http://www.sqlalchemy.org/download.html), and since nothing in Sage currently uses it (at least, in the standard packages), it may be best to upgrade to 0.7. What do you think?\n\n\nNo objections, I seem to be in a reviewing mood. If you post it, I'll test it on a couple of systems.",
    "created_at": "2011-06-01T04:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79823",
    "user": "https://github.com/kiwifb"
}
```

Replying to [comment:5 timdumol]:
> Actually, sqlalchemy now has a release [0.7](http://www.sqlalchemy.org/download.html), and since nothing in Sage currently uses it (at least, in the standard packages), it may be best to upgrade to 0.7. What do you think?


No objections, I seem to be in a reviewing mood. If you post it, I'll test it on a couple of systems.



---

archive/issue_comments_079824.json:
```json
{
    "body": "Alright. Package made, but it's taking a bit of time to upload to server.",
    "created_at": "2011-06-01T04:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79824",
    "user": "https://github.com/TimDumol"
}
```

Alright. Package made, but it's taking a bit of time to upload to server.



---

archive/issue_comments_079825.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-06-01T04:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79825",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_079826.json:
```json
{
    "body": "Here: http://sage.math.washington.edu/home/timdumol/sqlalchemy-0.7.0.spkg",
    "created_at": "2011-06-01T04:31:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79826",
    "user": "https://github.com/TimDumol"
}
```

Here: http://sage.math.washington.edu/home/timdumol/sqlalchemy-0.7.0.spkg



---

archive/issue_comments_079827.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-06-01T04:31:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79827",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_079828.json:
```json
{
    "body": "everything is ok on x86 and amd64. I am testing this on OSX and then I'll give it a positive review.",
    "created_at": "2011-06-01T13:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79828",
    "user": "https://github.com/kiwifb"
}
```

everything is ok on x86 and amd64. I am testing this on OSX and then I'll give it a positive review.



---

archive/issue_comments_079829.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-01T23:40:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79829",
    "user": "https://github.com/kiwifb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079830.json:
```json
{
    "body": "Fine on OS X. No doctests to run or break and there is currently no SPKG check but that should be another ticket provided that sqlalchemy has some self-tests. Positive review from me.",
    "created_at": "2011-06-01T23:40:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79830",
    "user": "https://github.com/kiwifb"
}
```

Fine on OS X. No doctests to run or break and there is currently no SPKG check but that should be another ticket provided that sqlalchemy has some self-tests. Positive review from me.



---

archive/issue_comments_079831.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-06-08T07:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79831",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_079832.json:
```json
{
    "body": "SPKG.txt should mention version number 0.7**.0** instead of 0.7.  It would also be good to mention the ticket number in SPKG.txt",
    "created_at": "2011-06-08T07:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79832",
    "user": "https://github.com/jdemeyer"
}
```

SPKG.txt should mention version number 0.7**.0** instead of 0.7.  It would also be good to mention the ticket number in SPKG.txt



---

archive/issue_comments_079833.json:
```json
{
    "body": "Note that in the mean time, SQLAlchemy 0.7.1 was released (http://www.sqlalchemy.org/download.html), maybe you might as well use that version?",
    "created_at": "2011-06-08T07:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79833",
    "user": "https://github.com/jdemeyer"
}
```

Note that in the mean time, SQLAlchemy 0.7.1 was released (http://www.sqlalchemy.org/download.html), maybe you might as well use that version?



---

archive/issue_comments_079834.json:
```json
{
    "body": "*ping*",
    "created_at": "2011-06-18T08:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79834",
    "user": "https://github.com/jdemeyer"
}
```

*ping*



---

archive/issue_comments_079835.json:
```json
{
    "body": "Sorry Jeroen, I have been busy with a couple of earthquakes and I was hoping Tim would make the new spkg.",
    "created_at": "2011-06-18T20:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79835",
    "user": "https://github.com/kiwifb"
}
```

Sorry Jeroen, I have been busy with a couple of earthquakes and I was hoping Tim would make the new spkg.



---

archive/issue_comments_079836.json:
```json
{
    "body": "I've updated the spkg to 0.7.6.",
    "created_at": "2012-03-28T21:22:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79836",
    "user": "https://github.com/mwhansen"
}
```

I've updated the spkg to 0.7.6.



---

archive/issue_comments_079837.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-03-28T21:22:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79837",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_events_021234.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8740#event-21234"
}
```



---

archive/issue_events_021235.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8740#event-21235"
}
```



---

archive/issue_events_021236.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8740#event-21236"
}
```



---

archive/issue_events_021237.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8740#event-21237"
}
```



---

archive/issue_events_021238.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8740#event-21238"
}
```



---

archive/issue_comments_079838.json:
```json
{
    "body": "Ok, last version of sqlalchemy is now 0.9.4. Does not make much sense to run behind versions of pire Python modules. The following works perfectly on my computer\n\n```\nsage -sh\neasy_install pip\npip install sqlalchemy==0.9.4\n```\nWe should rather include `pip` in Sage as proposed in [this thread in sage-devel](https://groups.google.com/forum/#!topic/sage-devel/e48IruDu7Kg) and make 'sage -i sqlalchemy` points to the last version.",
    "created_at": "2014-06-13T22:20:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79838",
    "user": "https://github.com/videlec"
}
```

Ok, last version of sqlalchemy is now 0.9.4. Does not make much sense to run behind versions of pire Python modules. The following works perfectly on my computer

```
sage -sh
easy_install pip
pip install sqlalchemy==0.9.4
```
We should rather include `pip` in Sage as proposed in [this thread in sage-devel](https://groups.google.com/forum/#!topic/sage-devel/e48IruDu7Kg) and make 'sage -i sqlalchemy` points to the last version.



---

archive/issue_comments_079839.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2014-06-13T22:20:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79839",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_events_021239.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8740#event-21239"
}
```



---

archive/issue_events_021240.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8740#event-21240"
}
```



---

archive/issue_events_021241.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-08-20T20:33:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8740#event-21241"
}
```



---

archive/issue_comments_079840.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2014-08-20T20:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79840",
    "user": "https://github.com/vbraun"
}
```

Resolution: wontfix



---

archive/issue_events_021242.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-08-20T20:34:36Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8740#event-21242"
}
```



---

archive/issue_events_021243.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-08-20T20:34:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8740#event-21243"
}
```
