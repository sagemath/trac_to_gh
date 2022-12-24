# Issue 906: bugs in special.py

archive/issues_000906.json:
```json
{
    "body": "Assignee: @wdjoyner\n\nOver a year ago there were some bugs reported by someone on the email lists regarding the implementation of the special functions. SAGE's special functions are wrappers for Pari or Maxima functions, so basically this is an interface issue. Basically, some of the functions implemented as F(x,n) should have been called using F(n,x). A patch was created last October 2006 but never applied. This patch includes most of that old patch. \n\nAlso, at someone's request (I think William Stein), a Bessel function class was created which implemented a few Bessel functions as class instances. \n\nAll this is in the patch \nhttp://sage.math.washington.edu/home/wdj/patches/special-functions.hg\nIt passed sage-t.\n\nIssue created by migration from https://trac.sagemath.org/ticket/906\n\n",
    "created_at": "2007-10-16T03:29:15Z",
    "labels": [
        "interfaces",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "bugs in special.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/906",
    "user": "@wdjoyner"
}
```
Assignee: @wdjoyner

Over a year ago there were some bugs reported by someone on the email lists regarding the implementation of the special functions. SAGE's special functions are wrappers for Pari or Maxima functions, so basically this is an interface issue. Basically, some of the functions implemented as F(x,n) should have been called using F(n,x). A patch was created last October 2006 but never applied. This patch includes most of that old patch. 

Also, at someone's request (I think William Stein), a Bessel function class was created which implemented a few Bessel functions as class instances. 

All this is in the patch 
http://sage.math.washington.edu/home/wdj/patches/special-functions.hg
It passed sage-t.

Issue created by migration from https://trac.sagemath.org/ticket/906





---

archive/issue_comments_005579.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-20T22:26:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/906#issuecomment-5579",
    "user": "@williamstein"
}
```

Resolution: fixed
