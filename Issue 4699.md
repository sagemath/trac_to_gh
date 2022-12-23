# Issue 4699: should be even more easier to change how many threads used for "make ptest" and friends

Issue created by migration from https://trac.sagemath.org/ticket/4699

Original creator: ddrake

Original creation time: 2008-12-04 23:53:04

Assignee: mabshoff

CC:  gfurnish

From http://trac.sagemath.org/sage_trac/ticket/4684#comment:5 :

> This is already closed, but I want to comment that I would vastly prefer if "make ptest" were to by default just parse the MAKE environment variable, and if it is "make -j6", say, then use 6 threads. This is what "sage -t" does now. This way, I just set MAKE in my .bash_profile, and everything works right.


---

Comment by ddrake created at 2008-12-04 23:56:45

...and, from http://trac.sagemath.org/sage_trac/ticket/4684#comment:6:
> I think we should postpone any work in that direction until we use pyprocessing for -tp. As it the feature is undocumented since it is still considered experimental due to bad behavior when doctests hang. Once we have #4538 and a pyprocessing based -tp we should finally document its existence.


---

Comment by mabshoff created at 2008-12-05 00:21:01

I renamed and changed the ticket description.

Cheers,

Micheal


---

Comment by mabshoff created at 2008-12-05 04:52:16

Also see #838 for something closely related that could be solved using pyprocessing by using an initialized sage session and then forking.

Cheers,

Michael


---

Comment by gfurnish created at 2008-12-10 19:02:32

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-12-10 19:02:32

Changing assignee from mabshoff to gfurnish.


---

Comment by gfurnish created at 2008-12-10 19:02:32

This also fixes #4711


---

Comment by mabshoff created at 2008-12-11 13:12:11

Oops:

```
(Stripping trailing CRs from patch.)
patching file sage-ptest
Hunk #2 FAILED at 279.
Hunk #3 FAILED at 291.
```


Cheers,

Michael


---

Comment by gfurnish created at 2008-12-11 13:13:59

apply instead of other patches


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2008-12-11 15:02:39

Nice work, positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-11 15:07:24

Merged trac_4699_fix.patch and trac_4699_new_bin.patch in Sage 3.2.2.alpha2


---

Comment by mabshoff created at 2008-12-11 15:07:24

Resolution: fixed
