# Issue 4684: should be easier to change how many threads used for "make ptest" and friends

Issue created by migration from https://trac.sagemath.org/ticket/4684

Original creator: ddrake

Original creation time: 2008-12-03 05:53:28

Assignee: mabshoff

I just ran a `make ptest` and was surprised to see my 4-core machine overwhelmed. Of course, that's because the makefile in $SAGE_ROOT defaults to "`-tp 12`" for all the parallel testing.

I added a variable at the top of the makefile so that the, uh, tiny minority of Sage users with fewer than 16 cores can easily edit the makefile so that parallel testing doesn't kill their machines. :)

Since $SAGE_ROOT isn't under version control, I'm just uploading the entire new makefile. The changes are really simple.


---

Attachment


---

Comment by mabshoff created at 2008-12-03 05:55:23

Hi,

please post a diff to the original version of the makefile.

Cheers,

Michael


---

Attachment

Looks good to me. I posted a diff between the current and the patched version for the record.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-03 06:55:02

Resolution: fixed


---

Comment by mabshoff created at 2008-12-03 06:55:02

Merged in Sage 3.2.2.alpha0


---

Comment by was created at 2008-12-04 20:36:47

Hi,

This is already closed, but I want to comment that I would vastly prefer if "make ptest" were to by default just parse the MAKE environment variable, and if it is "make -j6", say, then use 6 threads.  This is what "sage -t" does now.   This way, I just set MAKE in my .bash_profile, and everything works right.


---

Comment by mabshoff created at 2008-12-04 23:52:49

I think we should postpone any work in that direction until we use pyprocessing for -tp. As it the feature is undocumented since it is still considered experimental due to bad behavior when doctests hang. Once we have #4538 and a pyprocessing based -tp we should finally document its existence.

Cheers,

Michael


---

Comment by ddrake created at 2008-12-04 23:58:17

Oops, I was busy opening #4699 while mabshoff was commenting!
