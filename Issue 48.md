# Issue 48: spkg-install for singular

archive/issues_000048.json:
```json
{
    "body": "Assignee: somebody\n\nOn Tue, 12 Sep 2006 17:32:37 -0700, Rob Gross <gross`@`bc.edu> wrote:\n \nI finally found my error, by deleting every alias and environment\nvariable in turn and seeing if I could then build sage successfully\nfrom scratch.  I'm still not sure why defining the environment\nvariable TMPDIR as /tmp caused a problem, but it did.  TMPDIR defaults\nto /tmp anyway, according to \"man ar\" which is why I'm a bit confused\nwhy it caused a problem.\n \nI can't remember why I had bothered to define TMPDIR in the first\nplace, but there must have been some other build at some other time\nthat needed it to be defined.\n \nThanks for all of your help.  I suppose that adding a check to make\nsure that no one else commits this particular act of stupidity might\nbe a good idea, but it's impossible to guess at all of the potential\nthings that could go wrong.--Rob\n \nI can put \"unset TMPDIR\" in the spkg-install file for singular.  I'm\nreally glad you tracked this down precisely!\n \nWilliam\n\nIssue created by migration from https://trac.sagemath.org/ticket/48\n\n",
    "created_at": "2006-09-13T09:28:23Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "spkg-install for singular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/48",
    "user": "https://trac.sagemath.org/admin/accounts/users/anonymous"
}
```
Assignee: somebody

On Tue, 12 Sep 2006 17:32:37 -0700, Rob Gross <gross`@`bc.edu> wrote:
 
I finally found my error, by deleting every alias and environment
variable in turn and seeing if I could then build sage successfully
from scratch.  I'm still not sure why defining the environment
variable TMPDIR as /tmp caused a problem, but it did.  TMPDIR defaults
to /tmp anyway, according to "man ar" which is why I'm a bit confused
why it caused a problem.
 
I can't remember why I had bothered to define TMPDIR in the first
place, but there must have been some other build at some other time
that needed it to be defined.
 
Thanks for all of your help.  I suppose that adding a check to make
sure that no one else commits this particular act of stupidity might
be a good idea, but it's impossible to guess at all of the potential
things that could go wrong.--Rob
 
I can put "unset TMPDIR" in the spkg-install file for singular.  I'm
really glad you tracked this down precisely!
 
William

Issue created by migration from https://trac.sagemath.org/ticket/48





---

archive/issue_events_000047.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-01-13T02:10:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/48",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/48#event-47"
}
```



---

archive/issue_comments_000277.json:
```json
{
    "body": "put into singular-3-0-2-20070105 (version on 0112)",
    "created_at": "2007-01-13T02:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/48",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/48#issuecomment-277",
    "user": "https://github.com/williamstein"
}
```

put into singular-3-0-2-20070105 (version on 0112)



---

archive/issue_comments_000278.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-13T02:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/48",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/48#issuecomment-278",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_000279.json:
```json
{
    "body": "Changing component from basic arithmetic to packages.",
    "created_at": "2012-07-25T17:04:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/48",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/48#issuecomment-279",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from basic arithmetic to packages.
