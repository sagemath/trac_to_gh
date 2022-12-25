# Issue 9368: sage_fortran ignores SAGE64 except on Solaris/OpenSolaris

archive/issues_009368.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  justin @qed777 @jhpalmieri\n\n#9346 which corrects a problem with the variable has a problem, because SAGE64 is ignored on any plaform other than OS X. \n\nThis needs correcting urgently. \n\nDave\n\nIssue created by migration from https://trac.sagemath.org/ticket/9368\n\n",
    "created_at": "2010-06-28T23:25:39Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "sage_fortran ignores SAGE64 except on Solaris/OpenSolaris",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9368",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: GeorgSWeber

CC:  justin @qed777 @jhpalmieri

#9346 which corrects a problem with the variable has a problem, because SAGE64 is ignored on any plaform other than OS X. 

This needs correcting urgently. 

Dave

Issue created by migration from https://trac.sagemath.org/ticket/9368





---

archive/issue_comments_088840.json:
```json
{
    "body": "Mercurial patch which hopefully finally fixes this fortran issue. (Long-term, it would be good to get rid of files like sage_fortran)",
    "created_at": "2010-06-28T23:44:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9368#issuecomment-88840",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Mercurial patch which hopefully finally fixes this fortran issue. (Long-term, it would be good to get rid of files like sage_fortran)



---

archive/issue_comments_088841.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-28T23:46:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9368#issuecomment-88841",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088842.json:
```json
{
    "body": "Attachment [9368.patch](tarball://root/attachments/some-uuid/ticket9368/9368.patch) by drkirkby created at 2010-06-28 23:46:42\n\nA new package can be found at \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/fortran-20100629.spkg\n\nNote, this is just a tar file, not a compressed tar file, as compressing the contents, which are already compressed, just makes the package bigger and need more CPU time to process",
    "created_at": "2010-06-28T23:46:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9368#issuecomment-88842",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [9368.patch](tarball://root/attachments/some-uuid/ticket9368/9368.patch) by drkirkby created at 2010-06-28 23:46:42

A new package can be found at 

http://boxen.math.washington.edu/home/kirkby/patches/fortran-20100629.spkg

Note, this is just a tar file, not a compressed tar file, as compressing the contents, which are already compressed, just makes the package bigger and need more CPU time to process



---

archive/issue_comments_088843.json:
```json
{
    "body": "The change makes sense to me, but I'm not sure I can referee it properly: I don't have any problem with fortran on my Mac OS X box.  This is OS X 10.6 on a 64-bit machine.  No matter how I set SAGE64, the file sage_fortran always says\n\n```/bin/bash\ngfortran -m64 \"$@\"\n```\n\nIn fact, the lines which get changed by the patch occur in the function `install_SAGE_FORTRAN`, which should only get run if the environment variable `SAGE_FORTRAN` is set.  I don't know why anyone on OS X should set this.",
    "created_at": "2010-06-29T15:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9368#issuecomment-88843",
    "user": "https://github.com/jhpalmieri"
}
```

The change makes sense to me, but I'm not sure I can referee it properly: I don't have any problem with fortran on my Mac OS X box.  This is OS X 10.6 on a 64-bit machine.  No matter how I set SAGE64, the file sage_fortran always says

```/bin/bash
gfortran -m64 "$@"
```

In fact, the lines which get changed by the patch occur in the function `install_SAGE_FORTRAN`, which should only get run if the environment variable `SAGE_FORTRAN` is set.  I don't know why anyone on OS X should set this.



---

archive/issue_comments_088844.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-29T16:14:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9368#issuecomment-88844",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009521.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-06-29T16:15:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9368#event-9521"
}
```



---

archive/issue_comments_088845.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-29T16:15:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9368#issuecomment-88845",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_088846.json:
```json
{
    "body": "Replying to [comment:5 jhpalmieri]:\n> The change makes sense to me, but I'm not sure I can referee it properly: I don't have any problem with fortran on my Mac OS X box.  This is OS X 10.6 on a 64-bit machine.  No matter how I set SAGE64, the file sage_fortran always says\n> {{{\n> #!/bin/bash\n> gfortran -m64 \"$`@`\"\n> }}}\n> In fact, the lines which get changed by the patch occur in the function `install_SAGE_FORTRAN`, which should only get run if the environment variable `SAGE_FORTRAN` is set.  I don't know why anyone on OS X should set this.\n\nI'm pretty sure I've seen it written that one can do this on OS X if you want to use a different compiler. I guess with Apple shipping 4.0.1, it is not surprising some people are using more recent compilers. \n\nSorry for the mess up!\n\nDave",
    "created_at": "2010-06-29T20:52:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9368#issuecomment-88846",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:5 jhpalmieri]:
> The change makes sense to me, but I'm not sure I can referee it properly: I don't have any problem with fortran on my Mac OS X box.  This is OS X 10.6 on a 64-bit machine.  No matter how I set SAGE64, the file sage_fortran always says
> {{{
> #!/bin/bash
> gfortran -m64 "$`@`"
> }}}
> In fact, the lines which get changed by the patch occur in the function `install_SAGE_FORTRAN`, which should only get run if the environment variable `SAGE_FORTRAN` is set.  I don't know why anyone on OS X should set this.

I'm pretty sure I've seen it written that one can do this on OS X if you want to use a different compiler. I guess with Apple shipping 4.0.1, it is not surprising some people are using more recent compilers. 

Sorry for the mess up!

Dave



---

archive/issue_comments_088847.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2010-07-15T12:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9368#issuecomment-88847",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to needs_work.



---

archive/issue_events_009522.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-07-15T12:22:55Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9368#event-9522"
}
```



---

archive/issue_comments_088848.json:
```json
{
    "body": "I'm re-opening this ticket because the fortran-20100629.spkg is broken.  On OS X, it installs g95 now, whereas the previous fortran spkg (the one in sage-4.4.4) installs gfortran.      Somebody was a bit sloppy.  \n\nWhen this package is properly updated for OS X, make sure to type\n\n  ./sage -sh\n   local/bin/sage_fortran.bin --version\n\nand ensure that you've actually got gfortran installed, not g95.  The gfortran binary for OS X is quad-architecture -- it covers 32 and 64-bit on both ppc and intel.",
    "created_at": "2010-07-15T12:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9368#issuecomment-88848",
    "user": "https://github.com/williamstein"
}
```

I'm re-opening this ticket because the fortran-20100629.spkg is broken.  On OS X, it installs g95 now, whereas the previous fortran spkg (the one in sage-4.4.4) installs gfortran.      Somebody was a bit sloppy.  

When this package is properly updated for OS X, make sure to type

  ./sage -sh
   local/bin/sage_fortran.bin --version

and ensure that you've actually got gfortran installed, not g95.  The gfortran binary for OS X is quad-architecture -- it covers 32 and 64-bit on both ppc and intel.



---

archive/issue_comments_088849.json:
```json
{
    "body": "I'm also moving this to sage-4.5.1, so that the release manager can release sage-4.5.",
    "created_at": "2010-07-15T12:23:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9368#issuecomment-88849",
    "user": "https://github.com/williamstein"
}
```

I'm also moving this to sage-4.5.1, so that the release manager can release sage-4.5.



---

archive/issue_comments_088850.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2010-07-15T12:23:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9368#issuecomment-88850",
    "user": "https://github.com/williamstein"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_088851.json:
```json
{
    "body": "Replying to [comment:9 was]:\n> I'm re-opening this ticket because the fortran-20100629.spkg is broken.  On OS X, it installs g95 now, whereas the previous fortran spkg (the one in sage-4.4.4) installs gfortran.      Somebody was a bit sloppy.  \n> \n> When this package is properly updated for OS X, make sure to type\n> \n>   ./sage -sh\n>    local/bin/sage_fortran.bin --version\n> \n> and ensure that you've actually got gfortran installed, not g95.  The gfortran binary for OS X is quad-architecture -- it covers 32 and 64-bit on both ppc and intel.    \n\nSince I created it, I guess you are saying I was sloppy. It is hard to know how I can check this any more, given it builds for me on OS X (bsd.math) using \n* My normal environment\n* Your script. \n\nIt also builds for everyone else. There are numerous reports of successful builds on OS X. \n\nWould it be sensible to remove 'g95' from the package, and ensure that the packages assumes 'gfortran' - then the perl script can be removed. \n\nDave",
    "created_at": "2010-07-15T12:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9368#issuecomment-88851",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:9 was]:
> I'm re-opening this ticket because the fortran-20100629.spkg is broken.  On OS X, it installs g95 now, whereas the previous fortran spkg (the one in sage-4.4.4) installs gfortran.      Somebody was a bit sloppy.  
> 
> When this package is properly updated for OS X, make sure to type
> 
>   ./sage -sh
>    local/bin/sage_fortran.bin --version
> 
> and ensure that you've actually got gfortran installed, not g95.  The gfortran binary for OS X is quad-architecture -- it covers 32 and 64-bit on both ppc and intel.    

Since I created it, I guess you are saying I was sloppy. It is hard to know how I can check this any more, given it builds for me on OS X (bsd.math) using 
* My normal environment
* Your script. 

It also builds for everyone else. There are numerous reports of successful builds on OS X. 

Would it be sensible to remove 'g95' from the package, and ensure that the packages assumes 'gfortran' - then the perl script can be removed. 

Dave



---

archive/issue_comments_088852.json:
```json
{
    "body": "> Since I created it, I guess you are saying I was sloppy. It is hard to know how I can check \n> this any more, given it builds for me on OS X (bsd.math) using\n\nI wrote the spkg and most of the script in the first place, and looking it over, I think now it would be more accurate to conclude that I'm saying that *I* was sloppy.    As penance, I'll move this back to sage-4.5, and try to improve the sloppiness.",
    "created_at": "2010-07-15T12:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9368#issuecomment-88852",
    "user": "https://github.com/williamstein"
}
```

> Since I created it, I guess you are saying I was sloppy. It is hard to know how I can check 
> this any more, given it builds for me on OS X (bsd.math) using

I wrote the spkg and most of the script in the first place, and looking it over, I think now it would be more accurate to conclude that I'm saying that *I* was sloppy.    As penance, I'll move this back to sage-4.5, and try to improve the sloppiness.



---

archive/issue_comments_088853.json:
```json
{
    "body": "Replying to [comment:12 was]:\n> > Since I created it, I guess you are saying I was sloppy. It is hard to know how I can check \n> > this any more, given it builds for me on OS X (bsd.math) using\n> \n> I wrote the spkg and most of the script in the first place, and looking it over, I think now it would be more accurate to conclude that I'm saying that *I* was sloppy.    As penance, I'll move this back to sage-4.5, and try to improve the sloppiness.  \n\nThank you. \n\nDave",
    "created_at": "2010-07-15T12:51:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9368#issuecomment-88853",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:12 was]:
> > Since I created it, I guess you are saying I was sloppy. It is hard to know how I can check 
> > this any more, given it builds for me on OS X (bsd.math) using
> 
> I wrote the spkg and most of the script in the first place, and looking it over, I think now it would be more accurate to conclude that I'm saying that *I* was sloppy.    As penance, I'll move this back to sage-4.5, and try to improve the sloppiness.  

Thank you. 

Dave



---

archive/issue_comments_088854.json:
```json
{
    "body": "OK, I've found the problem.  The build script is written in Python.  Thus the fortran spkg *depends* on Python.   However, for me, when I built the fortran spkg, it got built before Python, hence some random system-wide wrong python was used, and this broke the build.  This was a problem that could have happened on many different systems in weird ways, so it's very good that Robert Miller and I persisted and tracked this down, instead of brushing it off. \n\nThe fix:  change the deps file, and make sure to include a comment in the deps file explaining this dependency.\n\nOne could also add a check that $SAGE_LOCAL/bin/python exists in this spkg-install script. \n\nAnother good idea, would be to change the sage build system, so that when if spkg-install is a Python script, but Python hasn't been built yet, then an error is immediately raised.  This would keep this problem from ever happening again.  I've opened a ticket: #9507.",
    "created_at": "2010-07-15T13:14:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9368#issuecomment-88854",
    "user": "https://github.com/williamstein"
}
```

OK, I've found the problem.  The build script is written in Python.  Thus the fortran spkg *depends* on Python.   However, for me, when I built the fortran spkg, it got built before Python, hence some random system-wide wrong python was used, and this broke the build.  This was a problem that could have happened on many different systems in weird ways, so it's very good that Robert Miller and I persisted and tracked this down, instead of brushing it off. 

The fix:  change the deps file, and make sure to include a comment in the deps file explaining this dependency.

One could also add a check that $SAGE_LOCAL/bin/python exists in this spkg-install script. 

Another good idea, would be to change the sage build system, so that when if spkg-install is a Python script, but Python hasn't been built yet, then an error is immediately raised.  This would keep this problem from ever happening again.  I've opened a ticket: #9507.



---

archive/issue_events_009523.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-07-15T13:18:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9368#event-9523"
}
```



---

archive/issue_comments_088855.json:
```json
{
    "body": "Re-closing this ticket :)",
    "created_at": "2010-07-15T13:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9368#issuecomment-88855",
    "user": "https://github.com/rlmill"
}
```

Re-closing this ticket :)



---

archive/issue_comments_088856.json:
```json
{
    "body": "Attachment [deps](tarball://root/attachments/some-uuid/ticket9368/deps) by @rlmill created at 2010-07-15 13:21:01",
    "created_at": "2010-07-15T13:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9368#issuecomment-88856",
    "user": "https://github.com/rlmill"
}
```

Attachment [deps](tarball://root/attachments/some-uuid/ticket9368/deps) by @rlmill created at 2010-07-15 13:21:01



---

archive/issue_comments_088857.json:
```json
{
    "body": "Looks good!\n\n```\n471,472c471\n< # Do not remove PYTHON below -- see trac 9368\n< $(INST)/$(FORTRAN): $(BASE)  $(INST)/$(PYTHON)\n---\n> $(INST)/$(FORTRAN): $(BASE)\n```\n",
    "created_at": "2010-07-15T13:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9368#issuecomment-88857",
    "user": "https://github.com/rlmill"
}
```

Looks good!

```
471,472c471
< # Do not remove PYTHON below -- see trac 9368
< $(INST)/$(FORTRAN): $(BASE)  $(INST)/$(PYTHON)
---
> $(INST)/$(FORTRAN): $(BASE)
```




---

archive/issue_comments_088858.json:
```json
{
    "body": "Replying to [comment:14 was]:\n> OK, I've found the problem.  The build script is written in Python.  Thus the fortran spkg *depends* on Python.   However, for me, when I built the fortran spkg, it got built before Python, hence some random system-wide wrong python was used, and this broke the build.  This was a problem that could have happened on many different systems in weird ways, so it's very good that Robert Miller and I persisted and tracked this down, instead of brushing it off. \n\nI'm afraid to say I don't share your confidence that you and Robert have tracked this down completely, though you have found a serious flaw. \n\nClearly adding this dependency to `$SAGE_ROOT/spkg/standard/deps` is correct - the fortran package uses Python, so Python must be built first. I'm not arguing with that. \n\nHowever, I'm not convinced this was William's problem, as the `$SAGE_LOCAL/bin/sage_fortain` script **must** have been working at one point, otherwise ATLAS, Linpack, Numpy and other things that used Fortran would not have built. As I posted on sage-release, William's `install.log` had in it\n\n\n```\nsage_fortran -fPIC  -c lsame.f -o lsame.o\nsage_fortran -fPIC  -c lsametst.f -o lsametst.o\nsage_fortran  -o testlsame lsame.o lsametst.o\nsage_fortran -fPIC  -c slamch.f -o slamch.o\nsage_fortran -fPIC  -c slamchtst.f -o slamchtst.o\nsage_fortran  -o testslamch slamch.o lsame.o slamchtst.o \n```\n\n\nHowever, when I looked at William's $SAGE_LOCAL/bin/sage_fortran, it had only:\n\n\n```/bin/sh\n```\n\n\nin it. There is **no way** that could have been used to compile ATLAS, Linbox, Numpy etc, all of which had built successfully. \n\nHence I believe that something other than the fortran package later modified `$SAGE_LOCAL/bin/sage_fortran`. Unless I'm mistaken, the bug does not reside in the fortran package at all, but rather in something that was built after ATLAS, Numpy and Linbox. \n\nComments? \n\nDave",
    "created_at": "2010-07-15T22:45:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9368#issuecomment-88858",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:14 was]:
> OK, I've found the problem.  The build script is written in Python.  Thus the fortran spkg *depends* on Python.   However, for me, when I built the fortran spkg, it got built before Python, hence some random system-wide wrong python was used, and this broke the build.  This was a problem that could have happened on many different systems in weird ways, so it's very good that Robert Miller and I persisted and tracked this down, instead of brushing it off. 

I'm afraid to say I don't share your confidence that you and Robert have tracked this down completely, though you have found a serious flaw. 

Clearly adding this dependency to `$SAGE_ROOT/spkg/standard/deps` is correct - the fortran package uses Python, so Python must be built first. I'm not arguing with that. 

However, I'm not convinced this was William's problem, as the `$SAGE_LOCAL/bin/sage_fortain` script **must** have been working at one point, otherwise ATLAS, Linpack, Numpy and other things that used Fortran would not have built. As I posted on sage-release, William's `install.log` had in it


```
sage_fortran -fPIC  -c lsame.f -o lsame.o
sage_fortran -fPIC  -c lsametst.f -o lsametst.o
sage_fortran  -o testlsame lsame.o lsametst.o
sage_fortran -fPIC  -c slamch.f -o slamch.o
sage_fortran -fPIC  -c slamchtst.f -o slamchtst.o
sage_fortran  -o testslamch slamch.o lsame.o slamchtst.o 
```


However, when I looked at William's $SAGE_LOCAL/bin/sage_fortran, it had only:


```/bin/sh
```


in it. There is **no way** that could have been used to compile ATLAS, Linbox, Numpy etc, all of which had built successfully. 

Hence I believe that something other than the fortran package later modified `$SAGE_LOCAL/bin/sage_fortran`. Unless I'm mistaken, the bug does not reside in the fortran package at all, but rather in something that was built after ATLAS, Numpy and Linbox. 

Comments? 

Dave



---

archive/issue_comments_088859.json:
```json
{
    "body": "> I'm afraid to say I don't share your confidence that you and Robert have tracked this down completely, though you have found a serious flaw. \n\nAs you also say, the change to deps is clearly right, so since this seems to fix the problem, we should leave this ticket closed, but keep an eye on this issue.\n\n(It would have been interesting to know the modification time of sage_fortran.  I can't imagine that anything else would have modified this; it seems more likely that something is broken in the ATLAS build, etc.  The broken build doesn't seem to be around anymore, though.)",
    "created_at": "2010-07-15T22:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9368#issuecomment-88859",
    "user": "https://github.com/jhpalmieri"
}
```

> I'm afraid to say I don't share your confidence that you and Robert have tracked this down completely, though you have found a serious flaw. 

As you also say, the change to deps is clearly right, so since this seems to fix the problem, we should leave this ticket closed, but keep an eye on this issue.

(It would have been interesting to know the modification time of sage_fortran.  I can't imagine that anything else would have modified this; it seems more likely that something is broken in the ATLAS build, etc.  The broken build doesn't seem to be around anymore, though.)



---

archive/issue_comments_088860.json:
```json
{
    "body": "Replying to [comment:18 drkirkby]:\n> I'm afraid to say I don't share your confidence that you and Robert have tracked this down completely, though you have found a serious flaw.\n\nOf course you don't share the same confidence, you didn't trace the bug down to its source like we did. It was the configure script for the R spkg calling a very specific fortran command that made the build eventually fail. It is very easy to imagine that none of the other configure scripts called fortran in this way. In fact, they couldn't have or the build would have failed earlier.\n\n> However, I'm not convinced this was William's problem, as the `$SAGE_LOCAL/bin/sage_fortain` script **must** have been working at one point, otherwise ATLAS, Linpack, Numpy and other things that used Fortran would not have built.\n\nDefine working.\n\n> However, when I looked at William's $SAGE_LOCAL/bin/sage_fortran, it had only:\n> \n> {{{\n> #!/bin/sh\n> }}}\n\nAs I pointed out earlier, this is just plain wrong!\n\n> Unless I'm mistaken...\n\nYou are!",
    "created_at": "2010-07-15T23:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9368#issuecomment-88860",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:18 drkirkby]:
> I'm afraid to say I don't share your confidence that you and Robert have tracked this down completely, though you have found a serious flaw.

Of course you don't share the same confidence, you didn't trace the bug down to its source like we did. It was the configure script for the R spkg calling a very specific fortran command that made the build eventually fail. It is very easy to imagine that none of the other configure scripts called fortran in this way. In fact, they couldn't have or the build would have failed earlier.

> However, I'm not convinced this was William's problem, as the `$SAGE_LOCAL/bin/sage_fortain` script **must** have been working at one point, otherwise ATLAS, Linpack, Numpy and other things that used Fortran would not have built.

Define working.

> However, when I looked at William's $SAGE_LOCAL/bin/sage_fortran, it had only:
> 
> {{{
> #!/bin/sh
> }}}

As I pointed out earlier, this is just plain wrong!

> Unless I'm mistaken...

You are!



---

archive/issue_comments_088861.json:
```json
{
    "body": "I accept R could have called sage_fortran in a different way, which resulted in ATLAS, Linbox and Numpy building, but not R. \n\nBut can you explain how ATLAS, Numpy and Linbox built, when I clearly see the sage_fortran script had in it\n\n\n```/bin/sh\n```\n\n\n? \n\nI'm not wrong about the contents of the file. It **did** have that in it. \n\nDave",
    "created_at": "2010-07-15T23:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9368#issuecomment-88861",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I accept R could have called sage_fortran in a different way, which resulted in ATLAS, Linbox and Numpy building, but not R. 

But can you explain how ATLAS, Numpy and Linbox built, when I clearly see the sage_fortran script had in it


```/bin/sh
```


? 

I'm not wrong about the contents of the file. It **did** have that in it. 

Dave



---

archive/issue_comments_088862.json:
```json
{
    "body": "Replying to [comment:21 drkirkby]:\n\n> But can you explain how ATLAS, Numpy and Linbox built, when I clearly see the sage_fortran script had in it\n> \n> {{{\n> #!/bin/sh\n> }}}\n> \n> ? \n> \n> I'm not wrong about the contents of the file. It **did** have that in it. \n> \n> Dave \n\nI realise I was mistaken here. Justin is almost certainly right when he says the lack of a new line in the file can fool the eye into believing that the contents of the file are just\n\n\n```/bin/sh\n```\n  \n\nwhen in fact there is more to it. This is how it looks on my screen - it is easy to see that this could be confusing. \n\n\n```\ndrkirkby@hawk:~/sage-4.5.rc0$ cat local/bin/sage_fortran\n#!/bin/sh \n\n/usr/local/gcc-4.4.4-multilib/bin/gfortran -m64 -fPIC $@drkirkby@hawk:~/sage-4.5.rc0$ \n```\n\n\n\nI'm glad I was wrong about this. \n\nDave",
    "created_at": "2010-07-16T00:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9368#issuecomment-88862",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:21 drkirkby]:

> But can you explain how ATLAS, Numpy and Linbox built, when I clearly see the sage_fortran script had in it
> 
> {{{
> #!/bin/sh
> }}}
> 
> ? 
> 
> I'm not wrong about the contents of the file. It **did** have that in it. 
> 
> Dave 

I realise I was mistaken here. Justin is almost certainly right when he says the lack of a new line in the file can fool the eye into believing that the contents of the file are just


```/bin/sh
```
  

when in fact there is more to it. This is how it looks on my screen - it is easy to see that this could be confusing. 


```
drkirkby@hawk:~/sage-4.5.rc0$ cat local/bin/sage_fortran
#!/bin/sh 

/usr/local/gcc-4.4.4-multilib/bin/gfortran -m64 -fPIC $@drkirkby@hawk:~/sage-4.5.rc0$ 
```



I'm glad I was wrong about this. 

Dave
