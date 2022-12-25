# Issue 9154: boehm_gc (still, still) fails to build on Cygwin

archive/issues_009154.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @nexttime\n\nThis is a followup to #9067.  Amazingly,  the BoehmGC spkg: boehm_gc-7.1.p5.spkg in Sage 4.4.3 does not work.  \n\nI'm trying building now with the boehm_gc-7.1.p4.spkg in /home/mhansen/sage-4.3.5/spkg/standard on winxp2, and it quickly gets passed the problem that boehm_gc-7.1.p5.spkg exhibits, and so far seems to work.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9154\n\n",
    "created_at": "2010-06-06T03:50:06Z",
    "labels": [
        "component: packages: standard",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "boehm_gc (still, still) fails to build on Cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9154",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  @nexttime

This is a followup to #9067.  Amazingly,  the BoehmGC spkg: boehm_gc-7.1.p5.spkg in Sage 4.4.3 does not work.  

I'm trying building now with the boehm_gc-7.1.p4.spkg in /home/mhansen/sage-4.3.5/spkg/standard on winxp2, and it quickly gets passed the problem that boehm_gc-7.1.p5.spkg exhibits, and so far seems to work.

Issue created by migration from https://trac.sagemath.org/ticket/9154





---

archive/issue_comments_085319.json:
```json
{
    "body": "Did it work? \n\nSince libtool is used, all compiler warnings are dirrected to /dev/null. There's an option on libtool to enable the warnings, though I forget what it is.",
    "created_at": "2010-08-02T04:33:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9154#issuecomment-85319",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Did it work? 

Since libtool is used, all compiler warnings are dirrected to /dev/null. There's an option on libtool to enable the warnings, though I forget what it is.



---

archive/issue_comments_085320.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-17T04:38:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9154#issuecomment-85320",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085321.json:
```json
{
    "body": "There is a new spkg at http://boxen.math.washington.edu/home/mhansen/boehm_gc-7.1.p7.spkg which worked for me on winxp2.",
    "created_at": "2010-08-17T04:38:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9154#issuecomment-85321",
    "user": "https://github.com/mwhansen"
}
```

There is a new spkg at http://boxen.math.washington.edu/home/mhansen/boehm_gc-7.1.p7.spkg which worked for me on winxp2.



---

archive/issue_comments_085322.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-04-22T06:45:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9154#issuecomment-85322",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085323.json:
```json
{
    "body": "works for me with SAGE_CHECK=yes on Windows 7.\nIt's a Cygwin-specific change. Positive review.",
    "created_at": "2011-04-22T06:45:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9154#issuecomment-85323",
    "user": "https://github.com/dimpase"
}
```

works for me with SAGE_CHECK=yes on Windows 7.
It's a Cygwin-specific change. Positive review.



---

archive/issue_comments_085324.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-05-03T12:28:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9154#issuecomment-85324",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_009312.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2011-05-03T12:28:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9154",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9154#event-9312"
}
```



---

archive/issue_comments_085325.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2011-05-06T08:52:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9154#issuecomment-85325",
    "user": "https://github.com/jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_085326.json:
```json
{
    "body": "SPKG.txt needs to be updated to mention this ticket.",
    "created_at": "2011-05-06T08:52:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9154#issuecomment-85326",
    "user": "https://github.com/jdemeyer"
}
```

SPKG.txt needs to be updated to mention this ticket.



---

archive/issue_comments_085327.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2011-05-06T08:52:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9154#issuecomment-85327",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_events_009313.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2011-05-06T08:52:28Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/9154",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9154#event-9313"
}
```



---

archive/issue_comments_085328.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-05-19T08:32:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9154#issuecomment-85328",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085329.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-05-19T08:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9154#issuecomment-85329",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085330.json:
```json
{
    "body": "Replying to [comment:7 jdemeyer]:\n> SPKG.txt needs to be updated to mention this ticket.\n\ndone.",
    "created_at": "2011-05-19T11:15:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9154#issuecomment-85330",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:7 jdemeyer]:
> SPKG.txt needs to be updated to mention this ticket.

done.



---

archive/issue_comments_085331.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-05-19T11:15:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9154#issuecomment-85331",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_085332.json:
```json
{
    "body": "Where is the spkg?\n\nThe requested URL `/home/dima/boehm_gc-7.1.p7.spkg` was not found on this server.",
    "created_at": "2011-05-24T08:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9154#issuecomment-85332",
    "user": "https://github.com/jdemeyer"
}
```

Where is the spkg?

The requested URL `/home/dima/boehm_gc-7.1.p7.spkg` was not found on this server.



---

archive/issue_comments_085333.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-05-24T08:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9154#issuecomment-85333",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_085334.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-05-24T09:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9154#issuecomment-85334",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_085335.json:
```json
{
    "body": "Replying to [comment:11 jdemeyer]:\n> Where is the spkg?\n> \n> The requested URL `/home/dima/boehm_gc-7.1.p7.spkg` was not found on this server.\n\nMea culpa. Fixed the URL.",
    "created_at": "2011-05-24T09:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9154#issuecomment-85335",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:11 jdemeyer]:
> Where is the spkg?
> 
> The requested URL `/home/dima/boehm_gc-7.1.p7.spkg` was not found on this server.

Mea culpa. Fixed the URL.



---

archive/issue_events_009314.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2011-05-31T17:06:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9154",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9154#event-9314"
}
```



---

archive/issue_comments_085336.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-05-31T17:06:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9154#issuecomment-85336",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
