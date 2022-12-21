# Issue 7005: [with patch; needs review] singular -- port to cygwin

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-09-25 00:52:43

Assignee: tbd

New spkg up here: 

   http://sage.math.washington.edu/home/wstein/patches/cygwin/singular-3-1-0-4-20090818.p1.spkg

It just has one line commented out and requirement of libncurses-devel.




---

Comment by ddrake created at 2009-09-25 03:12:13

This builds on my Cygwin setup. Just a few comments:

  * There's a bunch of ~ backup files around; those should be deleted. (Although they are useful for reviewing purposes, since I could run "diff- u" to see what you did.)
  * The dist/ directory should be removed. (#5903)
  * Can you include a diff of sing_win.cc in the patches directory? That seems to be the standard practice, and it makes reviewing patches easier. (I wish that the patches directory contained _only_ patches, instead of entire copies of source files, but that's for another time...)
  * When I run "local/bin/Singular" from SAGE_ROOT, it appears to work, but says "? cannot open `standard.lib`". Is that okay?


---

Comment by GeorgSWeber created at 2009-09-25 19:30:29

Hi, just to mention it:

this "p1" spkg is based on the "original" Singular spkg from Sage 4.1.2.alpha1/2, and not on the "p0" spkg referenced from trac #6951. The changes therein already were forgotten once (in the transition from Singular 3-1-0-2 to Singular 3-1-0-4), so please make sure that they are not forgotten again :-)

The issue with libSingular on Cygwin always had been that it didn't work well with Python extensions / Cython. Does this work now (I can't test it myself currently, lacking a cygwin system/install)? If so, it has taken literally years to weed out one obstacle after another ... 

Cheers, Georg


---

Comment by ddrake created at 2009-09-27 23:59:31

Replying to [comment:2 GeorgSWeber]:
> The issue with libSingular on Cygwin always had been that it didn't work well with Python extensions / Cython. Does this work now (I can't test it myself currently, lacking a cygwin system/install)? If so, it has taken literally years to weed out one obstacle after another ... 

I have a working Cygwin install, but don't really know anything about the interface with Python extensions and Cython. Can you give me something to test? A simple bit of code to compile and try, maybe?


---

Comment by was created at 2009-10-01 15:06:48

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

Comment by was created at 2009-10-25 01:11:05

> The issue with libSingular on Cygwin always had been that it didn't
> work well with Python extensions / Cython. Does this work now...

YES.  It works fine.


---

Comment by mhansen created at 2010-04-27 17:37:55

The current spkg singular-3-1-0-4-20100214.spkg builds fine more me on Cygwin.  I'm going to close this as invalid.


---

Comment by mhansen created at 2010-04-27 17:37:55

Resolution: invalid
