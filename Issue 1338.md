# Issue 1338: Symmetrica crashes on big-endian machines

Issue created by migration from https://trac.sagemath.org/ticket/1338

Original creator: mabshoff

Original creation time: 2007-11-29 09:53:13

Assignee: mhansen

CC:  sage-combinat

It seems that symmetrica doesn't do too well on big endian machines. On Sparc as well as PPC under Linux the sfa doctest segfaults or shows bad things happening under valgrind. Mike Hanson said that there will be a new upstream version of symmetrica soon, so let's see if those fix the issue.

Cheers,

Michael


---

Comment by mhansen created at 2007-12-08 03:29:04

Changing status from new to assigned.


---

Comment by mhansen created at 2007-12-08 03:29:04

I think this might have been fixed with the upgrade to symmetrica-2.0?  See #1417 .


---

Comment by mabshoff created at 2007-12-09 09:47:19

This bug is not invalid, since it is probably fixed by #1417. But only when we can confirm that we will close the bug as fixed.

We do not invalidate bugs because they were fixed by another ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-15 23:10:00

The new symmetrica does not fix the issue and it still dumps core during various doctests. While something else might still be involved (libSingular) the ticket should remain open until we sort this all out.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-16 15:32:02

Unfortunately this is still an issue :(

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-15 11:37:03

The spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/alpha0/symmetrica-2.0.p3.spkg

The patch posted makes the symmetrica extension depends on def.h, so it gets rebuild when symmetrica is being updated.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2009-05-15 11:41:42

Reassigned to 4.0.

And this is my ticket now :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-15 11:41:42

Changing assignee from mhansen to mabshoff.


---

Comment by mabshoff created at 2009-05-15 11:41:42

Changing status from assigned to new.


---

Comment by mabshoff created at 2009-05-15 11:41:47

Changing status from new to assigned.


---

Comment by was created at 2009-05-15 12:43:05

New spkg here with some trivial referee typo fixes:

http://sage.math.washington.edu/home/wstein/patches/symmetrica-2.0.p4.spkg


---

Comment by mabshoff created at 2009-05-15 14:22:05

Resolution: fixed


---

Comment by mabshoff created at 2009-05-15 14:22:05

Merged spkg and patch into Sage 4.0.alpha0.

Cheers,

Michael
