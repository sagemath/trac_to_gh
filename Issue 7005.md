# Issue 7005: [with patch; needs review] singular -- port to cygwin

archive/issues_007005.json:
```json
{
    "body": "Assignee: tbd\n\nNew spkg up here: \n\n   http://sage.math.washington.edu/home/wstein/patches/cygwin/singular-3-1-0-4-20090818.p1.spkg\n\nIt just has one line commented out and requirement of libncurses-devel.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7005\n\n",
    "created_at": "2009-09-25T00:52:43Z",
    "labels": [
        "component: porting"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch; needs review] singular -- port to cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7005",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

New spkg up here: 

   http://sage.math.washington.edu/home/wstein/patches/cygwin/singular-3-1-0-4-20090818.p1.spkg

It just has one line commented out and requirement of libncurses-devel.



Issue created by migration from https://trac.sagemath.org/ticket/7005





---

archive/issue_comments_057824.json:
```json
{
    "body": "This builds on my Cygwin setup. Just a few comments:\n\n* There's a bunch of ~ backup files around; those should be deleted. (Although they are useful for reviewing purposes, since I could run \"diff- u\" to see what you did.)\n* The dist/ directory should be removed. (#5903)\n* Can you include a diff of sing_win.cc in the patches directory? That seems to be the standard practice, and it makes reviewing patches easier. (I wish that the patches directory contained *only* patches, instead of entire copies of source files, but that's for another time...)\n* When I run \"local/bin/Singular\" from SAGE_ROOT, it appears to work, but says \"? cannot open `standard.lib`\". Is that okay?",
    "created_at": "2009-09-25T03:12:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7005#issuecomment-57824",
    "user": "https://github.com/dandrake"
}
```

This builds on my Cygwin setup. Just a few comments:

* There's a bunch of ~ backup files around; those should be deleted. (Although they are useful for reviewing purposes, since I could run "diff- u" to see what you did.)
* The dist/ directory should be removed. (#5903)
* Can you include a diff of sing_win.cc in the patches directory? That seems to be the standard practice, and it makes reviewing patches easier. (I wish that the patches directory contained *only* patches, instead of entire copies of source files, but that's for another time...)
* When I run "local/bin/Singular" from SAGE_ROOT, it appears to work, but says "? cannot open `standard.lib`". Is that okay?



---

archive/issue_comments_057825.json:
```json
{
    "body": "Hi, just to mention it:\n\nthis \"p1\" spkg is based on the \"original\" Singular spkg from Sage 4.1.2.alpha1/2, and not on the \"p0\" spkg referenced from trac #6951. The changes therein already were forgotten once (in the transition from Singular 3-1-0-2 to Singular 3-1-0-4), so please make sure that they are not forgotten again :-)\n\nThe issue with libSingular on Cygwin always had been that it didn't work well with Python extensions / Cython. Does this work now (I can't test it myself currently, lacking a cygwin system/install)? If so, it has taken literally years to weed out one obstacle after another ... \n\nCheers, Georg",
    "created_at": "2009-09-25T19:30:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7005#issuecomment-57825",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Hi, just to mention it:

this "p1" spkg is based on the "original" Singular spkg from Sage 4.1.2.alpha1/2, and not on the "p0" spkg referenced from trac #6951. The changes therein already were forgotten once (in the transition from Singular 3-1-0-2 to Singular 3-1-0-4), so please make sure that they are not forgotten again :-)

The issue with libSingular on Cygwin always had been that it didn't work well with Python extensions / Cython. Does this work now (I can't test it myself currently, lacking a cygwin system/install)? If so, it has taken literally years to weed out one obstacle after another ... 

Cheers, Georg



---

archive/issue_comments_057826.json:
```json
{
    "body": "Replying to [comment:2 GeorgSWeber]:\n> The issue with libSingular on Cygwin always had been that it didn't work well with Python extensions / Cython. Does this work now (I can't test it myself currently, lacking a cygwin system/install)? If so, it has taken literally years to weed out one obstacle after another ... \n\n\nI have a working Cygwin install, but don't really know anything about the interface with Python extensions and Cython. Can you give me something to test? A simple bit of code to compile and try, maybe?",
    "created_at": "2009-09-27T23:59:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7005#issuecomment-57826",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:2 GeorgSWeber]:
> The issue with libSingular on Cygwin always had been that it didn't work well with Python extensions / Cython. Does this work now (I can't test it myself currently, lacking a cygwin system/install)? If so, it has taken literally years to weed out one obstacle after another ... 


I have a working Cygwin install, but don't really know anything about the interface with Python extensions and Cython. Can you give me something to test? A simple bit of code to compile and try, maybe?



---

archive/issue_comments_057827.json:
```json
{
    "body": "Replying to [comment:2 GeorgSWeber]:\n> Hi, just to mention it:\n> \n> this \"p1\" spkg is based on the \"original\" Singular spkg from Sage 4.1.2.alpha1/2, and not on the \"p0\" spkg referenced from trac #6951. The changes therein already were forgotten once (in the transition from Singular 3-1-0-2 to Singular 3-1-0-4), so please make sure that they are not forgotten again :-)\n> \n> The issue with libSingular on Cygwin always had been that it didn't work \n> well with Python extensions / Cython. Does this work now (I can't test it \n> myself currently, lacking a cygwin system/install)? If so, it has taken\n> literally years to weed out one obstacle after another ... \n\n\nSage doesn't work on Cygwin, so *nobody knows*!   That said, Michael Abshoff claimed the problems with libSingular on Cygwin were fixed in May when Martin Albrecht and Michael Abshoff both visited UW, and were evidently the same as the problems that had to be fixed to get Sage to work on 64-bit OS X 10.5.   So yes, it is likely that this is resolved.  But that's not what this patch is about.",
    "created_at": "2009-10-01T15:06:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7005#issuecomment-57827",
    "user": "https://github.com/williamstein"
}
```

Replying to [comment:2 GeorgSWeber]:
> Hi, just to mention it:
> 
> this "p1" spkg is based on the "original" Singular spkg from Sage 4.1.2.alpha1/2, and not on the "p0" spkg referenced from trac #6951. The changes therein already were forgotten once (in the transition from Singular 3-1-0-2 to Singular 3-1-0-4), so please make sure that they are not forgotten again :-)
> 
> The issue with libSingular on Cygwin always had been that it didn't work 
> well with Python extensions / Cython. Does this work now (I can't test it 
> myself currently, lacking a cygwin system/install)? If so, it has taken
> literally years to weed out one obstacle after another ... 


Sage doesn't work on Cygwin, so *nobody knows*!   That said, Michael Abshoff claimed the problems with libSingular on Cygwin were fixed in May when Martin Albrecht and Michael Abshoff both visited UW, and were evidently the same as the problems that had to be fixed to get Sage to work on 64-bit OS X 10.5.   So yes, it is likely that this is resolved.  But that's not what this patch is about.



---

archive/issue_comments_057828.json:
```json
{
    "body": "> The issue with libSingular on Cygwin always had been that it didn't\n> work well with Python extensions / Cython. Does this work now...\n\n\nYES.  It works fine.",
    "created_at": "2009-10-25T01:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7005#issuecomment-57828",
    "user": "https://github.com/williamstein"
}
```

> The issue with libSingular on Cygwin always had been that it didn't
> work well with Python extensions / Cython. Does this work now...


YES.  It works fine.



---

archive/issue_comments_057829.json:
```json
{
    "body": "The current spkg singular-3-1-0-4-20100214.spkg builds fine more me on Cygwin.  I'm going to close this as invalid.",
    "created_at": "2010-04-27T17:37:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7005#issuecomment-57829",
    "user": "https://github.com/mwhansen"
}
```

The current spkg singular-3-1-0-4-20100214.spkg builds fine more me on Cygwin.  I'm going to close this as invalid.



---

archive/issue_events_016434.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-04-27T17:37:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7005",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7005#event-16434"
}
```



---

archive/issue_comments_057830.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-04-27T17:37:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7005#issuecomment-57830",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_events_016435.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-04-27T17:37:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7005",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7005#event-16435"
}
```
