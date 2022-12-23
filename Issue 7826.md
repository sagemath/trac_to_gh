# Issue 7826: [with spkg] mpfi ignores SAGE64

Issue created by migration from https://trac.sagemath.org/ticket/7826

Original creator: drkirkby

Original creation time: 2010-01-03 03:05:51

Assignee: drkirkby

CC:  jsp

mpfi like many packages ignores the setting of SAGE64. mpfi clears CFLAGS, so even setting environment variables will not allow this to build. Hence spkg-install needed updating. 

I left some remarks for the package maintainer, on how to get rid of the SAGE64 junk. 

An updated package can be found at the following address. All changes are checked in. 

See:
http://boxen.math.washington.edu/home/kirkby/portability/mpfi-1.3.4-cvs20071125.p8/



---

Comment by drkirkby created at 2010-01-06 00:53:07

Changing status from new to needs_review.


---

Comment by zimmerma created at 2010-02-25 22:19:30

Changing status from needs_review to needs_info.


---

Comment by zimmerma created at 2010-02-25 22:19:30

David, please can you explain how to reproduce the defect, and thus how to check your patch
solves it?


---

Comment by jsp created at 2010-02-25 22:35:43

The issue seems to be fixed:

[http://trac.sagemath.org/sage_trac/ticket/8069](http://trac.sagemath.org/sage_trac/ticket/8069)

An example of a communication failure?

Sorry,

Jaap


---

Comment by drkirkby created at 2010-02-25 22:38:05

It looks like this has been fixed, but the idea was to do exactly what was done on OS X. i.e. add the flag -m64 if the environment variable SAGE64 is set to "yes"

dave


---

Comment by zimmerma created at 2010-02-25 22:46:40

> It looks like this has been fixed, but the idea was to do exactly what was done on OS X. i.e. add the flag -m64 if the environment variable SAGE64 is set to "yes" 

Dave, do you want to submit a patch, or should we close that ticket?

Paul


---

Comment by drkirkby created at 2010-02-25 22:57:52

There is a patch in the directory http://boxen.math.washington.edu/home/kirkby/portability/mpfi-1.3.4-cvs20071125.p8/ but I think the issue has been resolved on another ticket, so I believe this can be closed. 

Dave


---

Comment by zimmerma created at 2010-02-25 23:02:22

> so I believe this can be  closed

How to tell the release manager? (I've been told I am not allowed to close a ticket.)


---

Comment by jsp created at 2010-02-25 23:09:41

Replying to [comment:7 zimmerma]:
> > so I believe this can be  closed
> 
> How to tell the release manager? (I've been told I am not allowed to close a ticket.)

Maybe the owner can? Dave?

Jaap


---

Comment by drkirkby created at 2010-02-26 00:16:10

No, I am not allowed to close the ticket, despite the fact I opened it. But I can leave a note for the release manager to close it. 

 == Note to Release Manager ==

*Another ticket, #8069 was created by Jaap to fix the same issue. Since the issue has been resolved, this ticket can be closed.*

Dave


---

Comment by jsp created at 2010-02-26 00:20:40

Replying to [comment:9 drkirkby]:
> No, I am not allowed to close the ticket, despite the fact I opened it. But I can leave a note for the release manager to close it. 
> 

Why not? I remember that I closed tickets some time ago.

Jaap


---

Comment by drkirkby created at 2010-02-26 00:31:21

I got told off for doing this this other day (see #8201), though in that case I marked someone elses ticket as "wontfix". 

It was pointed out to me by Alex that the trac guidelines 

http://wiki.sagemath.org/devel/TracGuidelines 

do not permit you to close tickets. 

More specifically, the paragraph about closing tickets: "No Closing Or Invalidating: Unless you have admin powers in trac (which includes all the people who have ever done releases of Sage), do not close tickets unless you are explicitly told to do so. Since we have email notification now this has become less of an issue. If you think that a ticket is invalid or has been fixed, just comment on it and the current release manager will take a look and close it if appropriate." 

I'll drop an email on sage-devel and ask someone to close it, or someone might give me permission to close it, in which case I'll do it. 

Dave


---

Comment by mvngu created at 2010-06-05 19:29:16

Resolution: fixed


---

Comment by mvngu created at 2010-06-05 19:29:16

Close as fixed by #8069.
