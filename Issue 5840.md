# Issue 5840: update SageTeX spkg to version 2.0.2

Issue created by migration from https://trac.sagemath.org/ticket/5840

Original creator: ddrake

Original creation time: 2009-04-21 04:16:23

Assignee: ddrake

I've made a new spkg for SageTeX. It now has a proper Mercurial repository layout, improved spkg-check, documentation about TeXShop, and more examples.

The spkg is available from http://sage.math.washington.edu/home/drake/code/sage/st/sagetex-2.0.2.spkg.


---

Comment by ddrake created at 2009-04-21 04:17:08

Changing status from new to assigned.


---

Comment by jason created at 2009-05-06 03:26:48

This looks good to me.  I installed and used it today too.


---

Comment by ddrake created at 2009-05-15 06:08:38

Okay, there's a yet newer version that I'd prefer get reviewed -- it has a "pause/unpause" feature that the author of TeXShop requested. The new spkg is: http://sage.math.washington.edu/home/drake/code/sage/st/sagetex-2.1.1.spkg. Changing this back to "needs review"...sorry Jason. :)


---

Comment by jason created at 2009-05-28 06:40:45

This looks great.  The one nitpicky detail that needs to be fixed (and then this is a positive review) is that the changelog inside of SPKG.txt does not mention the update to 2.1.1.  When that is fixed, change this to positive review.

Great work!


---

Comment by ddrake created at 2009-05-28 08:21:06

I updated SPKG.txt as requested. It feels slightly illicit to change my own ticket to "positive review", but Jason said so... :)


---

Comment by mhansen created at 2009-06-01 00:05:18

Do we include a sagetex spkg currently?


---

Comment by ddrake created at 2009-06-01 01:12:46

Replying to [comment:9 mhansen]:
> Do we include a sagetex spkg currently?

AFAIK it's supposed to be in the optional repository, but there were issues with spkgs there disappearing. In IRC, mabshoff has said that he wouldn't update or add new spkgs to the optional repo until someone figured out why spkgs were disappearing and fixed the problem.


---

Comment by mhansen created at 2009-06-01 01:17:41

Merged in the optional package repo.


---

Comment by mhansen created at 2009-06-01 01:17:41

Resolution: fixed
