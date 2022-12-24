# Issue 2732: cython in Debian build doesn't work

archive/issues_002732.json:
```json
{
    "body": "Assignee: @timabbott\n\nDoing cython builds on Debian doesn't work, because it doesn't have the right include_dirs.\n\nThere seems to be a lot of code re-use between spkg/standard/sage-2.10.5/sage/misc/cython.py and spkg/standard/sage-2.10.5/setup.py.  It might be good to merge that code into only one place; if we don't do that, we'll probably want to make the changes we made to spkg/standard/sage-2.10.5/setup.py to spkg/standard/sage-2.10.5/sage/misc/cython.py.  \n\nRegardless, we should have a way of specifying that we've got a Debian build at runtime (currently we only have a build-time specification).  Probably this will just mean having the SAGE wrapper script in Debian set SAGE_DEBIAN=yes.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2732\n\n",
    "created_at": "2008-03-30T02:43:24Z",
    "labels": [
        "debian-package",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "cython in Debian build doesn't work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2732",
    "user": "@timabbott"
}
```
Assignee: @timabbott

Doing cython builds on Debian doesn't work, because it doesn't have the right include_dirs.

There seems to be a lot of code re-use between spkg/standard/sage-2.10.5/sage/misc/cython.py and spkg/standard/sage-2.10.5/setup.py.  It might be good to merge that code into only one place; if we don't do that, we'll probably want to make the changes we made to spkg/standard/sage-2.10.5/setup.py to spkg/standard/sage-2.10.5/sage/misc/cython.py.  

Regardless, we should have a way of specifying that we've got a Debian build at runtime (currently we only have a build-time specification).  Probably this will just mean having the SAGE wrapper script in Debian set SAGE_DEBIAN=yes.

Issue created by migration from https://trac.sagemath.org/ticket/2732





---

archive/issue_comments_018803.json:
```json
{
    "body": "Well, I installed all the development libraries needed to build SAGE at runtime, and the doctests for misc/cython.py all pass at the moment.  But I suspect there will probably still be problems with the include path not having everything.",
    "created_at": "2008-03-30T05:40:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2732#issuecomment-18803",
    "user": "@timabbott"
}
```

Well, I installed all the development libraries needed to build SAGE at runtime, and the doctests for misc/cython.py all pass at the moment.  But I suspect there will probably still be problems with the include path not having everything.



---

archive/issue_comments_018804.json:
```json
{
    "body": "Tim,\n\ncan this ticket be closed? It seems to have gone stale.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-22T20:05:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2732#issuecomment-18804",
    "user": "mabshoff"
}
```

Tim,

can this ticket be closed? It seems to have gone stale.

Cheers,

Michael



---

archive/issue_comments_018805.json:
```json
{
    "body": "This has indeed grown stale, in part because I've not actually had any problems passing tests despite this issue and in part because I've been very busy lately.\n\nHowever, I think there is a real problem if someone wants to write some code using libraries normally packaged as part of Sage in the Sage cython environment in a packaged sage.",
    "created_at": "2008-08-22T20:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2732#issuecomment-18805",
    "user": "@timabbott"
}
```

This has indeed grown stale, in part because I've not actually had any problems passing tests despite this issue and in part because I've been very busy lately.

However, I think there is a real problem if someone wants to write some code using libraries normally packaged as part of Sage in the Sage cython environment in a packaged sage.



---

archive/issue_comments_018806.json:
```json
{
    "body": "Closing this, since we've dropped support for a Debian package.",
    "created_at": "2012-04-19T10:00:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2732#issuecomment-18806",
    "user": "@jdemeyer"
}
```

Closing this, since we've dropped support for a Debian package.



---

archive/issue_comments_018807.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2012-04-19T10:00:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2732#issuecomment-18807",
    "user": "@jdemeyer"
}
```

Resolution: invalid
