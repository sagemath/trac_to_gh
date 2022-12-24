# Issue 4810: qepcad-1.50 fails to build without tcsh

archive/issues_004810.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @jondo\n\nMartin Rubey reported in http://groups.google.com/group/sage-devel/browse_thread/thread/d48a4139afd07da8\n\n```\njust for the record: installing tcsh makes the problem go away.  This hint was \nburied in a longer mail on this list, so I repeat it here... \n```\n\nHe also reported an interface problem which could also be split off to another ticket:\n\n```\nAnother hint:  qepcad does not like fractions, not even of integers, and the \nsage interface doesn't deal with this.  So you have to reduce them yourself, \ni.e., instead of \na < b/2 \nwrite \n2*a < b \nOtherwise qepcad will appear to do nothing. \n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4810\n\n",
    "created_at": "2008-12-16T06:37:59Z",
    "labels": [
        "packages: optional",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "qepcad-1.50 fails to build without tcsh",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4810",
    "user": "mabshoff"
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

archive/issue_comments_036468.json:
```json
{
    "body": "See also #19450",
    "created_at": "2015-10-22T08:02:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4810#issuecomment-36468",
    "user": "@rwst"
}
```

See also #19450



---

archive/issue_comments_036469.json:
```json
{
    "body": "Any reason to think that these two tickets are related?",
    "created_at": "2015-10-22T08:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4810#issuecomment-36469",
    "user": "@jdemeyer"
}
```

Any reason to think that these two tickets are related?



---

archive/issue_comments_036470.json:
```json
{
    "body": "Probably obsolete",
    "created_at": "2017-03-14T16:25:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4810#issuecomment-36470",
    "user": "@jdemeyer"
}
```

Probably obsolete



---

archive/issue_comments_036471.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2017-03-14T16:25:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4810#issuecomment-36471",
    "user": "@jdemeyer"
}
```

Resolution: invalid



---

archive/issue_comments_036472.json:
```json
{
    "body": "Indeed, it has been fixed in #10224, with a patch to remove that dependency to tcsh : https://git.sagemath.org/sage.git/diff/build/pkgs/qepcad/patches/makefile_no_csh.patch?id=9b43535c1221c86b6e4f17cd36951d88a2c350fb",
    "created_at": "2017-03-15T07:21:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4810#issuecomment-36472",
    "user": "tmonteil"
}
```

Indeed, it has been fixed in #10224, with a patch to remove that dependency to tcsh : https://git.sagemath.org/sage.git/diff/build/pkgs/qepcad/patches/makefile_no_csh.patch?id=9b43535c1221c86b6e4f17cd36951d88a2c350fb
