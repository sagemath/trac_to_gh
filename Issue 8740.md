# Issue 8740: Upgrade sqlalchemy to 0.6.0

archive/issues_008740.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  tdumol fbissey\n\nThe latest version of SQLAlchemy is now [0.6.0](http://www.sqlalchemy.org/trac/wiki/06Migration). This brings a bunch of changes, notably a native unicode mode, which would be a lot faster for unicode rich applications, such as the Sage Notebook.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8740\n\n",
    "created_at": "2010-04-21T19:28:18Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "title": "Upgrade sqlalchemy to 0.6.0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8740",
    "user": "timdumol"
}
```
Assignee: tbd

CC:  tdumol fbissey

The latest version of SQLAlchemy is now [0.6.0](http://www.sqlalchemy.org/trac/wiki/06Migration). This brings a bunch of changes, notably a native unicode mode, which would be a lot faster for unicode rich applications, such as the Sage Notebook.

Issue created by migration from https://trac.sagemath.org/ticket/8740





---

archive/issue_comments_079950.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-21T19:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79950",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079951.json:
```json
{
    "body": "Now at 0.6.7 anyone wants to make a new spkg?",
    "created_at": "2011-05-31T22:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79951",
    "user": "fbissey"
}
```

Now at 0.6.7 anyone wants to make a new spkg?



---

archive/issue_comments_079952.json:
```json
{
    "body": "Actually, sqlalchemy now has a release [0.7](http://www.sqlalchemy.org/download.html), and since nothing in Sage currently uses it (at least, in the standard packages), it may be best to upgrade to 0.7. What do you think?",
    "created_at": "2011-06-01T04:01:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79952",
    "user": "timdumol"
}
```

Actually, sqlalchemy now has a release [0.7](http://www.sqlalchemy.org/download.html), and since nothing in Sage currently uses it (at least, in the standard packages), it may be best to upgrade to 0.7. What do you think?



---

archive/issue_comments_079953.json:
```json
{
    "body": "Replying to [comment:5 timdumol]:\n> Actually, sqlalchemy now has a release [0.7](http://www.sqlalchemy.org/download.html), and since nothing in Sage currently uses it (at least, in the standard packages), it may be best to upgrade to 0.7. What do you think?\n\nNo objections, I seem to be in a reviewing mood. If you post it, I'll test it on a couple of systems.",
    "created_at": "2011-06-01T04:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79953",
    "user": "fbissey"
}
```

Replying to [comment:5 timdumol]:
> Actually, sqlalchemy now has a release [0.7](http://www.sqlalchemy.org/download.html), and since nothing in Sage currently uses it (at least, in the standard packages), it may be best to upgrade to 0.7. What do you think?

No objections, I seem to be in a reviewing mood. If you post it, I'll test it on a couple of systems.



---

archive/issue_comments_079954.json:
```json
{
    "body": "Alright. Package made, but it's taking a bit of time to upload to server.",
    "created_at": "2011-06-01T04:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79954",
    "user": "timdumol"
}
```

Alright. Package made, but it's taking a bit of time to upload to server.



---

archive/issue_comments_079955.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-06-01T04:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79955",
    "user": "timdumol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_079956.json:
```json
{
    "body": "Here: http://sage.math.washington.edu/home/timdumol/sqlalchemy-0.7.0.spkg",
    "created_at": "2011-06-01T04:31:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79956",
    "user": "timdumol"
}
```

Here: http://sage.math.washington.edu/home/timdumol/sqlalchemy-0.7.0.spkg



---

archive/issue_comments_079957.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-06-01T04:31:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79957",
    "user": "timdumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_079958.json:
```json
{
    "body": "everything is ok on x86 and amd64. I am testing this on OSX and then I'll give it a positive review.",
    "created_at": "2011-06-01T13:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79958",
    "user": "fbissey"
}
```

everything is ok on x86 and amd64. I am testing this on OSX and then I'll give it a positive review.



---

archive/issue_comments_079959.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-01T23:40:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79959",
    "user": "fbissey"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079960.json:
```json
{
    "body": "Fine on OS X. No doctests to run or break and there is currently no SPKG check but that should be another ticket provided that sqlalchemy has some self-tests. Positive review from me.",
    "created_at": "2011-06-01T23:40:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79960",
    "user": "fbissey"
}
```

Fine on OS X. No doctests to run or break and there is currently no SPKG check but that should be another ticket provided that sqlalchemy has some self-tests. Positive review from me.



---

archive/issue_comments_079961.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-06-08T07:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79961",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_079962.json:
```json
{
    "body": "SPKG.txt should mention version number 0.7**.0** instead of 0.7.  It would also be good to mention the ticket number in SPKG.txt",
    "created_at": "2011-06-08T07:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79962",
    "user": "jdemeyer"
}
```

SPKG.txt should mention version number 0.7**.0** instead of 0.7.  It would also be good to mention the ticket number in SPKG.txt



---

archive/issue_comments_079963.json:
```json
{
    "body": "Note that in the mean time, SQLAlchemy 0.7.1 was released (http://www.sqlalchemy.org/download.html), maybe you might as well use that version?",
    "created_at": "2011-06-08T07:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79963",
    "user": "jdemeyer"
}
```

Note that in the mean time, SQLAlchemy 0.7.1 was released (http://www.sqlalchemy.org/download.html), maybe you might as well use that version?



---

archive/issue_comments_079964.json:
```json
{
    "body": "*ping*",
    "created_at": "2011-06-18T08:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79964",
    "user": "jdemeyer"
}
```

*ping*



---

archive/issue_comments_079965.json:
```json
{
    "body": "Sorry Jeroen, I have been busy with a couple of earthquakes and I was hoping Tim would make the new spkg.",
    "created_at": "2011-06-18T20:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79965",
    "user": "fbissey"
}
```

Sorry Jeroen, I have been busy with a couple of earthquakes and I was hoping Tim would make the new spkg.



---

archive/issue_comments_079966.json:
```json
{
    "body": "I've updated the spkg to 0.7.6.",
    "created_at": "2012-03-28T21:22:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79966",
    "user": "mhansen"
}
```

I've updated the spkg to 0.7.6.



---

archive/issue_comments_079967.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-03-28T21:22:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79967",
    "user": "mhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_079968.json:
```json
{
    "body": "Ok, last version of sqlalchemy is now 0.9.4. Does not make much sense to run behind versions of pire Python modules. The following works perfectly on my computer\n\n```\nsage -sh\neasy_install pip\npip install sqlalchemy==0.9.4\n```\n\nWe should rather include `pip` in Sage as proposed in [this thread in sage-devel](https://groups.google.com/forum/#!topic/sage-devel/e48IruDu7Kg) and make 'sage -i sqlalchemy` points to the last version.",
    "created_at": "2014-06-13T22:20:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79968",
    "user": "vdelecroix"
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

archive/issue_comments_079969.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2014-06-13T22:20:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79969",
    "user": "vdelecroix"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_079970.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2014-08-20T20:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8740#issuecomment-79970",
    "user": "vbraun"
}
```

Resolution: wontfix
