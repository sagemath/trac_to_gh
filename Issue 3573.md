# Issue 3573: Finance - Implementation of opentick

archive/issues_003573.json:
```json
{
    "body": "Assignee: @cswiercz\n\nCC:  @robertwb\n\nKeywords: finance, opentick,\n\nopentick is a collection of APIs for obtaining free real-time and historical market data for trading systems and trading platforms. With these APIs, we will enable Sage to be able to stream and manipulate real-time market data.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3573\n\n",
    "created_at": "2008-07-06T21:45:34Z",
    "labels": [
        "component: finance"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Finance - Implementation of opentick",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3573",
    "user": "https://github.com/cswiercz"
}
```
Assignee: @cswiercz

CC:  @robertwb

Keywords: finance, opentick,

opentick is a collection of APIs for obtaining free real-time and historical market data for trading systems and trading platforms. With these APIs, we will enable Sage to be able to stream and manipulate real-time market data.

Issue created by migration from https://trac.sagemath.org/ticket/3573





---

archive/issue_comments_025183.json:
```json
{
    "body": "Ignore that patch. Messed up with hg. Accidentally overwrote a patch that this one depended on.",
    "created_at": "2008-07-11T04:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25183",
    "user": "https://github.com/cswiercz"
}
```

Ignore that patch. Messed up with hg. Accidentally overwrote a patch that this one depended on.



---

archive/issue_comments_025184.json:
```json
{
    "body": "Typo. Put the files in OTHeaders.tar.bz2 in /usr/local/include, _NOT_ in /usr/local/bin.",
    "created_at": "2008-07-16T13:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25184",
    "user": "https://github.com/cswiercz"
}
```

Typo. Put the files in OTHeaders.tar.bz2 in /usr/local/include, _NOT_ in /usr/local/bin.



---

archive/issue_comments_025185.json:
```json
{
    "body": "Hi, \n\nplease do not attach binaries to trac tickets since those will be backup up daily until the end of time :). I have deleted both the library and the headers.\n\nInstead link them from the safe place, i.e. you sage.math account. In general your approach is completely wrong. What you need to do is to build an optinal OpenTick.spkg.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-16T13:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25185",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi, 

please do not attach binaries to trac tickets since those will be backup up daily until the end of time :). I have deleted both the library and the headers.

Instead link them from the safe place, i.e. you sage.math account. In general your approach is completely wrong. What you need to do is to build an optinal OpenTick.spkg.

Cheers,

Michael



---

archive/issue_comments_025186.json:
```json
{
    "body": "Attachment [sage-3573-opentick1.patch](tarball://root/attachments/some-uuid/ticket3573/sage-3573-opentick1.patch) by @cswiercz created at 2008-08-28 18:27:20",
    "created_at": "2008-08-28T18:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25186",
    "user": "https://github.com/cswiercz"
}
```

Attachment [sage-3573-opentick1.patch](tarball://root/attachments/some-uuid/ticket3573/sage-3573-opentick1.patch) by @cswiercz created at 2008-08-28 18:27:20



---

archive/issue_comments_025187.json:
```json
{
    "body": "Attachment [sage-3573-opentick2.patch](tarball://root/attachments/some-uuid/ticket3573/sage-3573-opentick2.patch) by @cswiercz created at 2008-08-28 18:27:30",
    "created_at": "2008-08-28T18:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25187",
    "user": "https://github.com/cswiercz"
}
```

Attachment [sage-3573-opentick2.patch](tarball://root/attachments/some-uuid/ticket3573/sage-3573-opentick2.patch) by @cswiercz created at 2008-08-28 18:27:30



---

archive/issue_comments_025188.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-28T18:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25188",
    "user": "https://github.com/cswiercz"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025189.json:
```json
{
    "body": "This ticket comes with an spkg. Alas, I don't have administrative privileges on Trac so I can't attach it here. You can find the spkg on `sage.math` at `/home/cswiercz/opentick1.1.spkg`. I will also post it at the top of http://cswiercz.blogspot.com.",
    "created_at": "2008-08-28T19:36:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25189",
    "user": "https://github.com/cswiercz"
}
```

This ticket comes with an spkg. Alas, I don't have administrative privileges on Trac so I can't attach it here. You can find the spkg on `sage.math` at `/home/cswiercz/opentick1.1.spkg`. I will also post it at the top of http://cswiercz.blogspot.com.



---

archive/issue_comments_025190.json:
```json
{
    "body": "For the documentation in the patch `sage-3573-opentick2.patch`, here are some possible fixes to typos:\n\n1. The word \"minutely\" is usually associated with considering something in close details. The expression \"by minute\" (or something similar) more accurately describes a time interval.\n\n```\n-data on a variety of time intervals: hourly, minutely, or even\n+data on a variety of time intervals: hourly, by minute, or even\n```\n\n\n2. Again, a similar comment to that in 1. applies here. I would use \"by second\" or something similar, but not \"secondly\", which hardly describes a time interval.\n\n```\n-hourly, minutely, and even secondly. To enable use of opentick, enter\n+hourly, by minute, and even by second. To enable use of opentick, enter \n```\n\n\n3. Again, a similar comment to that in 2. applies here.\n\n```\n-to obtain data on an hourly, minutely, or even secondly rate. This\n+to obtain data on an hourly rate, or by minute, or even by second. This\n```\n\n\n4. \n\n```\n-enddate are \\code{datetime.date} objects. Retreives data using the\n+enddate are \\code{datetime.date} objects. Retrieves data using the\n```\n\n\n5.\n\n```\n-Return string representation of Opentick interface.\n+Return a string representation of Opentick interface.\n```\n\n\n6.\n\n```\n-in once of the following two formats where the time\n+in one of the following two formats where the time\n```\n\n\n7.\n\n```\n-Where 'Mon' is the first three letters of the coressponding month.\n+where 'Mon' is the first three letters of the corresponding month.\n```\n\n\nDisclaimer: I'm an Australian, so maybe my suggestions don't make sense.",
    "created_at": "2008-10-26T13:08:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25190",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

For the documentation in the patch `sage-3573-opentick2.patch`, here are some possible fixes to typos:

1. The word "minutely" is usually associated with considering something in close details. The expression "by minute" (or something similar) more accurately describes a time interval.

```
-data on a variety of time intervals: hourly, minutely, or even
+data on a variety of time intervals: hourly, by minute, or even
```


2. Again, a similar comment to that in 1. applies here. I would use "by second" or something similar, but not "secondly", which hardly describes a time interval.

```
-hourly, minutely, and even secondly. To enable use of opentick, enter
+hourly, by minute, and even by second. To enable use of opentick, enter 
```


3. Again, a similar comment to that in 2. applies here.

```
-to obtain data on an hourly, minutely, or even secondly rate. This
+to obtain data on an hourly rate, or by minute, or even by second. This
```


4. 

```
-enddate are \code{datetime.date} objects. Retreives data using the
+enddate are \code{datetime.date} objects. Retrieves data using the
```


5.

```
-Return string representation of Opentick interface.
+Return a string representation of Opentick interface.
```


6.

```
-in once of the following two formats where the time
+in one of the following two formats where the time
```


7.

```
-Where 'Mon' is the first three letters of the coressponding month.
+where 'Mon' is the first three letters of the corresponding month.
```


Disclaimer: I'm an Australian, so maybe my suggestions don't make sense.



---

archive/issue_events_008175.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-11-29T03:12:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "milestone": "sage-3.2.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3573#event-8175"
}
```



---

archive/issue_comments_025191.json:
```json
{
    "body": "sage-3573-opentick2.patch doesn't apply with sage-3.2 and with #3621 applied",
    "created_at": "2008-11-30T01:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25191",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

sage-3573-opentick2.patch doesn't apply with sage-3.2 and with #3621 applied



---

archive/issue_events_008176.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "milestone": "sage-3.2.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3573#event-8176"
}
```



---

archive/issue_events_008177.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3573#event-8177"
}
```



---

archive/issue_events_008178.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3573#event-8178"
}
```



---

archive/issue_events_008179.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3573#event-8179"
}
```



---

archive/issue_events_008180.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3573#event-8180"
}
```



---

archive/issue_events_008181.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3573#event-8181"
}
```



---

archive/issue_events_008182.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3573#event-8182"
}
```



---

archive/issue_events_008183.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3573#event-8183"
}
```



---

archive/issue_events_008184.json:
```json
{
    "actor": "https://github.com/slel",
    "created_at": "2019-05-13T05:45:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3573#event-8184"
}
```



---

archive/issue_events_008185.json:
```json
{
    "actor": "https://github.com/slel",
    "created_at": "2019-05-13T05:45:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3573#event-8185"
}
```



---

archive/issue_comments_025192.json:
```json
{
    "body": "Changing keywords from \"finance, opentick,\" to \"finance, opentick\".",
    "created_at": "2019-05-13T05:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25192",
    "user": "https://github.com/slel"
}
```

Changing keywords from "finance, opentick," to "finance, opentick".



---

archive/issue_comments_025193.json:
```json
{
    "body": "The link in comment:8 no longer works but see an archived version at\n\n- https://web.archive.org/web/20080924232257/http://cswiercz.blogspot.com:80/2008/07/sage-update-opentick-situation.html",
    "created_at": "2019-05-13T05:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25193",
    "user": "https://github.com/slel"
}
```

The link in comment:8 no longer works but see an archived version at

- https://web.archive.org/web/20080924232257/http://cswiercz.blogspot.com:80/2008/07/sage-update-opentick-situation.html



---

archive/issue_comments_025194.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2021-10-10T20:30:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25194",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_025195.json:
```json
{
    "body": "outdated after sage.finance deprecation in #32427",
    "created_at": "2021-10-10T20:30:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25195",
    "user": "https://github.com/mkoeppe"
}
```

outdated after sage.finance deprecation in #32427



---

archive/issue_events_008186.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-10-10T20:30:15Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3573#event-8186"
}
```



---

archive/issue_events_008187.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-10-10T20:30:15Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3573#event-8187"
}
```



---

archive/issue_comments_025196.json:
```json
{
    "body": "Ok.",
    "created_at": "2021-10-25T10:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25196",
    "user": "https://github.com/slel"
}
```

Ok.



---

archive/issue_comments_025197.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-10-25T10:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25197",
    "user": "https://github.com/slel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_025198.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-10-25T15:39:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25198",
    "user": "https://github.com/mkoeppe"
}
```

Resolution: invalid



---

archive/issue_events_008188.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-10-25T15:39:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3573#event-8188"
}
```
