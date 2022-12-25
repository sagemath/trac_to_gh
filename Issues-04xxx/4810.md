# Issue 4810: qepcad-1.50 fails to build without tcsh

archive/issues_004810.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @jondo\n\nMartin Rubey reported in http://groups.google.com/group/sage-devel/browse_thread/thread/d48a4139afd07da8\n\n```\njust for the record: installing tcsh makes the problem go away.  This hint was \nburied in a longer mail on this list, so I repeat it here... \n```\nHe also reported an interface problem which could also be split off to another ticket:\n\n```\nAnother hint:  qepcad does not like fractions, not even of integers, and the \nsage interface doesn't deal with this.  So you have to reduce them yourself, \ni.e., instead of \na < b/2 \nwrite \n2*a < b \nOtherwise qepcad will appear to do nothing. \n```\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4810\n\n",
    "closed_at": "2017-03-14T16:25:48Z",
    "created_at": "2008-12-16T06:37:59Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "qepcad-1.50 fails to build without tcsh",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4810",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: cwitty

CC:  @jondo

Martin Rubey reported in http://groups.google.com/group/sage-devel/browse_thread/thread/d48a4139afd07da8

```
just for the record: installing tcsh makes the problem go away.  This hint was 
buried in a longer mail on this list, so I repeat it here... 
```
He also reported an interface problem which could also be split off to another ticket:

```
Another hint:  qepcad does not like fractions, not even of integers, and the 
sage interface doesn't deal with this.  So you have to reduce them yourself, 
i.e., instead of 
a < b/2 
write 
2*a < b 
Otherwise qepcad will appear to do nothing. 
```

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4810





---

archive/issue_events_011011.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4810",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4810#event-11011"
}
```



---

archive/issue_events_011012.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4810",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4810#event-11012"
}
```



---

archive/issue_events_011013.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4810",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4810#event-11013"
}
```



---

archive/issue_events_011014.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4810",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4810#event-11014"
}
```



---

archive/issue_events_011015.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4810",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4810#event-11015"
}
```



---

archive/issue_events_011016.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4810",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4810#event-11016"
}
```



---

archive/issue_events_011017.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4810",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4810#event-11017"
}
```



---

archive/issue_comments_036396.json:
```json
{
    "body": "See also #19450",
    "created_at": "2015-10-22T08:02:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4810#issuecomment-36396",
    "user": "https://github.com/rwst"
}
```

See also #19450



---

archive/issue_comments_036397.json:
```json
{
    "body": "Any reason to think that these two tickets are related?",
    "created_at": "2015-10-22T08:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4810#issuecomment-36397",
    "user": "https://github.com/jdemeyer"
}
```

Any reason to think that these two tickets are related?



---

archive/issue_comments_036398.json:
```json
{
    "body": "Probably obsolete",
    "created_at": "2017-03-14T16:25:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4810#issuecomment-36398",
    "user": "https://github.com/jdemeyer"
}
```

Probably obsolete



---

archive/issue_comments_036399.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2017-03-14T16:25:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4810#issuecomment-36399",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid



---

archive/issue_events_011018.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2017-03-14T16:25:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4810",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4810#event-11018"
}
```



---

archive/issue_events_011019.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2017-03-14T16:25:48Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4810",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4810#event-11019"
}
```



---

archive/issue_events_011020.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2017-03-14T16:25:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4810",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4810#event-11020"
}
```



---

archive/issue_comments_036400.json:
```json
{
    "body": "Indeed, it has been fixed in #10224, with a patch to remove that dependency to tcsh : https://git.sagemath.org/sage.git/diff/build/pkgs/qepcad/patches/makefile_no_csh.patch?id=9b43535c1221c86b6e4f17cd36951d88a2c350fb",
    "created_at": "2017-03-15T07:21:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4810#issuecomment-36400",
    "user": "https://trac.sagemath.org/admin/accounts/users/tmonteil"
}
```

Indeed, it has been fixed in #10224, with a patch to remove that dependency to tcsh : https://git.sagemath.org/sage.git/diff/build/pkgs/qepcad/patches/makefile_no_csh.patch?id=9b43535c1221c86b6e4f17cd36951d88a2c350fb
