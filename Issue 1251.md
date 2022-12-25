# Issue 1251: tutorial out of date

archive/issues_001251.json:
```json
{
    "body": "Assignee: @wdjoyner\n\nThe tut.tex file needed a few updates and corrections. The patch is at\nhttp://sage.math.washington.edu/home/wdj/patches/tut20071123.hg\nThe new latex file (which passes sage -t) is at\nhttp://sage.math.washington.edu/home/wdj/patches/tut.tex\nI also tried to change the file copyright.tex (which is\nin the commontex subdirectory). I don't think the changes stuck, but\nthe revised version is at\nhttp://sage.math.washington.edu/home/wdj/patches/copyright.tex\n(The old one said \"See the end of this document for licensing\ninformation. However, those sections were commented out, so I just\ncopied some lines from the start of the wiki.)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1251\n\n",
    "created_at": "2007-11-23T22:54:56Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.14",
    "title": "tutorial out of date",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1251",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: @wdjoyner

The tut.tex file needed a few updates and corrections. The patch is at
http://sage.math.washington.edu/home/wdj/patches/tut20071123.hg
The new latex file (which passes sage -t) is at
http://sage.math.washington.edu/home/wdj/patches/tut.tex
I also tried to change the file copyright.tex (which is
in the commontex subdirectory). I don't think the changes stuck, but
the revised version is at
http://sage.math.washington.edu/home/wdj/patches/copyright.tex
(The old one said "See the end of this document for licensing
information. However, those sections were commented out, so I just
copied some lines from the start of the wiki.)


Issue created by migration from https://trac.sagemath.org/ticket/1251





---

archive/issue_comments_007808.json:
```json
{
    "body": "Just apply the tut bundle http://sage.math.washington.edu/home/wdj/patches/tut20071123.hg \nthen manually place the copyright file in commontex (it is not\npart of the repo and shouldn't be for now).\n\nWilliam",
    "created_at": "2007-11-24T18:44:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1251#issuecomment-7808",
    "user": "https://github.com/williamstein"
}
```

Just apply the tut bundle http://sage.math.washington.edu/home/wdj/patches/tut20071123.hg 
then manually place the copyright file in commontex (it is not
part of the repo and shouldn't be for now).

William



---

archive/issue_comments_007809.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-25T04:55:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1251#issuecomment-7809",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
