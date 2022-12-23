# Issue 3349: OSX: make sure LDFLAGS are set for linking purposes

Issue created by migration from https://trac.sagemath.org/ticket/3349

Original creator: mabshoff

Original creation time: 2008-06-02 00:44:24

Assignee: mabshoff

On OSX it seems that using DYLD_LIBRARY_PATH on OSX is not equivalent to using LD_LIBRARY_PATH on Linux for example since there the linker takes that into consideration as a last resort when not finding libraries. I tried to figure out if there is some magic mode for the OSX ld to consider DYLD_LIBRARY_PATH, but I couldn't find anything. Either way, I can systematically fix those issues, but it will take some time to get this right and tested since this appears to be an OSX specific issue. 

This is somewhat of a META ticket and will take some time to fix.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-02 00:44:33

Changing status from new to assigned.


---

Comment by kcrisman created at 2012-06-01 17:55:58

This ticket is very vague, and we have been dealing with these issues on a per-spkg basis, I think - not to mention that it has gotten no comments in four years.  I'm recommending to close this, though the release manager could have another view.


---

Comment by kcrisman created at 2012-06-01 17:55:58

Changing status from new to needs_review.


---

Comment by kcrisman created at 2012-06-01 17:56:23

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-06-02 12:37:26

Sage is building perfectly fine now on a lot of OS X machines.  The ticket doesn't mention any _concrete_ instance of the issue.


---

Comment by jdemeyer created at 2012-06-02 12:37:26

Resolution: invalid
