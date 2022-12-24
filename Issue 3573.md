# Issue 3573: Finance - Implementation of opentick

archive/issues_003573.json:
```json
{
    "body": "Assignee: cswiercz\n\nCC:  robertwb\n\nKeywords: finance, opentick,\n\nopentick is a collection of APIs for obtaining free real-time and historical market data for trading systems and trading platforms. With these APIs, we will enable Sage to be able to stream and manipulate real-time market data.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3573\n\n",
    "created_at": "2008-07-06T21:45:34Z",
    "labels": [
        "finance",
        "major",
        "enhancement"
    ],
    "title": "Finance - Implementation of opentick",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3573",
    "user": "cswiercz"
}
```
Assignee: cswiercz

CC:  robertwb

Keywords: finance, opentick,

opentick is a collection of APIs for obtaining free real-time and historical market data for trading systems and trading platforms. With these APIs, we will enable Sage to be able to stream and manipulate real-time market data.

Issue created by migration from https://trac.sagemath.org/ticket/3573





---

archive/issue_comments_025233.json:
```json
{
    "body": "Ignore that patch. Messed up with hg. Accidentally overwrote a patch that this one depended on.",
    "created_at": "2008-07-11T04:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25233",
    "user": "cswiercz"
}
```

Ignore that patch. Messed up with hg. Accidentally overwrote a patch that this one depended on.



---

archive/issue_comments_025234.json:
```json
{
    "body": "Typo. Put the files in OTHeaders.tar.bz2 in /usr/local/include, _NOT_ in /usr/local/bin.",
    "created_at": "2008-07-16T13:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25234",
    "user": "cswiercz"
}
```

Typo. Put the files in OTHeaders.tar.bz2 in /usr/local/include, _NOT_ in /usr/local/bin.



---

archive/issue_comments_025235.json:
```json
{
    "body": "Hi, \n\nplease do not attach binaries to trac tickets since those will be backup up daily until the end of time :). I have deleted both the library and the headers.\n\nInstead link them from the safe place, i.e. you sage.math account. In general your approach is completely wrong. What you need to do is to build an optinal OpenTick.spkg.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-16T13:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25235",
    "user": "mabshoff"
}
```

Hi, 

please do not attach binaries to trac tickets since those will be backup up daily until the end of time :). I have deleted both the library and the headers.

Instead link them from the safe place, i.e. you sage.math account. In general your approach is completely wrong. What you need to do is to build an optinal OpenTick.spkg.

Cheers,

Michael



---

archive/issue_comments_025236.json:
```json
{
    "body": "Attachment [sage-3573-opentick1.patch](tarball://root/attachments/some-uuid/ticket3573/sage-3573-opentick1.patch) by cswiercz created at 2008-08-28 18:27:20",
    "created_at": "2008-08-28T18:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25236",
    "user": "cswiercz"
}
```

Attachment [sage-3573-opentick1.patch](tarball://root/attachments/some-uuid/ticket3573/sage-3573-opentick1.patch) by cswiercz created at 2008-08-28 18:27:20



---

archive/issue_comments_025237.json:
```json
{
    "body": "Attachment [sage-3573-opentick2.patch](tarball://root/attachments/some-uuid/ticket3573/sage-3573-opentick2.patch) by cswiercz created at 2008-08-28 18:27:30",
    "created_at": "2008-08-28T18:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25237",
    "user": "cswiercz"
}
```

Attachment [sage-3573-opentick2.patch](tarball://root/attachments/some-uuid/ticket3573/sage-3573-opentick2.patch) by cswiercz created at 2008-08-28 18:27:30



---

archive/issue_comments_025238.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-28T18:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25238",
    "user": "cswiercz"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025239.json:
```json
{
    "body": "This ticket comes with an spkg. Alas, I don't have administrative privileges on Trac so I can't attach it here. You can find the spkg on `sage.math` at `/home/cswiercz/opentick1.1.spkg`. I will also post it at the top of http://cswiercz.blogspot.com.",
    "created_at": "2008-08-28T19:36:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25239",
    "user": "cswiercz"
}
```

This ticket comes with an spkg. Alas, I don't have administrative privileges on Trac so I can't attach it here. You can find the spkg on `sage.math` at `/home/cswiercz/opentick1.1.spkg`. I will also post it at the top of http://cswiercz.blogspot.com.



---

archive/issue_comments_025240.json:
```json
{
    "body": "For the documentation in the patch `sage-3573-opentick2.patch`, here are some possible fixes to typos:\n\n1. The word \"minutely\" is usually associated with considering something in close details. The expression \"by minute\" (or something similar) more accurately describes a time interval.\n\n```\n-data on a variety of time intervals: hourly, minutely, or even\n+data on a variety of time intervals: hourly, by minute, or even\n```\n\n\n\n2. Again, a similar comment to that in 1. applies here. I would use \"by second\" or something similar, but not \"secondly\", which hardly describes a time interval.\n\n```\n-hourly, minutely, and even secondly. To enable use of opentick, enter\n+hourly, by minute, and even by second. To enable use of opentick, enter \n```\n\n\n\n3. Again, a similar comment to that in 2. applies here.\n\n```\n-to obtain data on an hourly, minutely, or even secondly rate. This\n+to obtain data on an hourly rate, or by minute, or even by second. This\n```\n\n\n\n4. \n\n```\n-enddate are \\code{datetime.date} objects. Retreives data using the\n+enddate are \\code{datetime.date} objects. Retrieves data using the\n```\n\n\n\n5.\n\n```\n-Return string representation of Opentick interface.\n+Return a string representation of Opentick interface.\n```\n\n\n\n6.\n\n```\n-in once of the following two formats where the time\n+in one of the following two formats where the time\n```\n\n\n\n7.\n\n```\n-Where 'Mon' is the first three letters of the coressponding month.\n+where 'Mon' is the first three letters of the corresponding month.\n```\n\n\n\nDisclaimer: I'm an Australian, so maybe my suggestions don't make sense.",
    "created_at": "2008-10-26T13:08:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25240",
    "user": "mvngu"
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

archive/issue_comments_025241.json:
```json
{
    "body": "sage-3573-opentick2.patch doesn't apply with sage-3.2 and with #3621 applied",
    "created_at": "2008-11-30T01:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25241",
    "user": "TimothyClemans"
}
```

sage-3573-opentick2.patch doesn't apply with sage-3.2 and with #3621 applied



---

archive/issue_comments_025242.json:
```json
{
    "body": "Changing keywords from \"finance, opentick,\" to \"finance, opentick\".",
    "created_at": "2019-05-13T05:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25242",
    "user": "slelievre"
}
```

Changing keywords from "finance, opentick," to "finance, opentick".



---

archive/issue_comments_025243.json:
```json
{
    "body": "The link in comment:8 no longer works but see an archived version at\n\n- https://web.archive.org/web/20080924232257/http://cswiercz.blogspot.com:80/2008/07/sage-update-opentick-situation.html",
    "created_at": "2019-05-13T05:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25243",
    "user": "slelievre"
}
```

The link in comment:8 no longer works but see an archived version at

- https://web.archive.org/web/20080924232257/http://cswiercz.blogspot.com:80/2008/07/sage-update-opentick-situation.html



---

archive/issue_comments_025244.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2021-10-10T20:30:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25244",
    "user": "mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_025245.json:
```json
{
    "body": "outdated after sage.finance deprecation in #32427",
    "created_at": "2021-10-10T20:30:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25245",
    "user": "mkoeppe"
}
```

outdated after sage.finance deprecation in #32427



---

archive/issue_comments_025246.json:
```json
{
    "body": "Ok.",
    "created_at": "2021-10-25T10:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25246",
    "user": "slelievre"
}
```

Ok.



---

archive/issue_comments_025247.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-10-25T10:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25247",
    "user": "slelievre"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_025248.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-10-25T15:39:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3573#issuecomment-25248",
    "user": "mkoeppe"
}
```

Resolution: invalid
