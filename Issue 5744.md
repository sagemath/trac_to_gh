# Issue 5744: Solaris 10: use C99 mode to compile extensions instead of using clumsy extern declarations, properly work around _Complex_I problem in complex.h

Issue created by migration from https://trac.sagemath.org/ticket/5744

Original creator: mabshoff

Original creation time: 2009-04-11 01:29:28

Assignee: mabshoff

isinf() and a bunch of friends we right now provide via solaris_fixes.h in various places is available in C99 mode with gcc via math_c99.h which is included in math.h. So building some extensions in C99 mode will allow us to get rid of nearly all Solaris specific workarounds. 

At the same time we have a new problem with _Complex_I which is expected to be provided by the compiler since complex.h just defines _Complex_I to be _Complex_I on Solaris 10. Not good :(

I have a patch coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-11 01:29:38

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2009-04-11 03:40:05

This patch removes some of the problems with C99, but some issues remain unresolved due to header issues when C99 and C++ is used.

Cheers,

Michael


---

Comment by was created at 2009-04-11 04:01:10

This looks fine to me.  I give it a positive review if it works for mabshoff.  He's the only one right now with a full Solaris build setup to test this on.


---

Comment by mabshoff created at 2009-04-11 04:53:40

It does not affect the build on non-Solaris and on Solaris it starts up, so I am making this a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-11 04:54:17

Merged in Sage 3.4.1.rc2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-11 04:54:17

Resolution: fixed
