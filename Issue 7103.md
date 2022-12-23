# Issue 7103: fix "mysterious error" in parallel doctesting first time: see ticket #7079

Issue created by migration from https://trac.sagemath.org/ticket/7103

Original creator: was

Original creation time: 2009-10-03 23:58:08

Assignee: tbd

See #7079


---

Comment by jhpalmieri created at 2009-10-04 00:30:43

Here's an attempt.  If init.sage isn't present, then run the script "sage-starts".  I think this makes all of the appropriate subdirectories of .sage.  In any case, it seems to fix the problem for me.


---

Attachment

apply to scripts repository


---

Comment by timdumol created at 2009-10-10 13:58:04

Changing status from needs_review to needs_work.


---

Comment by timdumol created at 2009-10-10 13:58:04

Applied patch, ran the test and still got the errors. `sage-starts` does not create the directories, at least in my system.


---

Comment by jhpalmieri created at 2009-10-10 17:42:23

Can you tell me what your system is and exactly what you did to test this?  (What directories did you delete before you started?)


---

Comment by GeorgSWeber created at 2009-11-11 21:39:54

Calling "make ptestlong" (as suggested in ticket #7079), we already call "sage-starts", as this is a part of the TESTPRELIMS in the makefile.

So the test case(s) for this ticket seems to be for directly calling "sage -tp .." from the commandline.

I don't understand the intention of the attached patch, however. If I delete the file "./sage/init.sage" and then call "sage -tp ...", the file would have been created anew before the patch, but *not* after the patch. Even if I delete the whole ".sage" directory, this file will not be recreated (after the patch).

Is it possible that the creation of "init.sage" (which should exist at least as an empty file IIRC) somehow originally did cause the problems?

Another thought: Might the presence (or not ...) of these infamous ".DS_Store" files (Mac OS X only, there's an open ticket to remove them IIRC) break the parallel building, causing somehow these "mysterious memory failures"?


---

Comment by jhpalmieri created at 2009-11-12 22:15:09

I don't think the ".DS_Store" files have anything to do it: I can recreate this problem on sage.math by deleting my .sage directory and then doing "sage -tp 4 devel/sage/sage/algebras", for example.

As far as I could tell, the presence (or lack) of init.sage was unrelated to the problem, so it wasn't in the patch.  I'm attaching a new patch which puts those lines back, just in case.  This patch runs "sage-starts" at the beginning no matter what: a few extra seconds to run this shouldn't be a big deal.

(As I said on #7079, I think the issue is that doctesting creates various subdirectories of .sage, and if two processes both try to create .sage/gap at the same time, they clash and one of them bombs.  So running sage-starts to create most of the relevant directories seems like a solution.  In some bizarre set of circumstances, I can imagine that someone will have deleted everything in .sage except for init.sage, so we don't want to put sage-starts inside that "if" clause.  I suppose instead we could look for the directories .sage/db, .sage/gap, .sage/ipython, .sage/temp, .sage/tmp, and .sage/valgrind individually, creating whichever ones are missing.  Do we need to create any subdirectories of those in addition?  It seems cleaner to just run sage-starts.)


---

Attachment

apply to scripts repository


---

Comment by mhansen created at 2009-11-13 04:37:15

Changing status from needs_work to needs_review.


---

Comment by was created at 2009-11-13 04:49:29

> "(As I said on #7079, I think the issue is that doctesting creates 
> various subdirectories of .sage, and if two processes both try to 
> create .sage/gap at the same time, they clash and one of them bombs. ..."

That's exactly right!


---

Comment by was created at 2009-11-13 04:57:00

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-11-13 04:57:00

This seems logical, the patch causes no harm, seems like a good idea, is eloquent.

I don't know if it fixes the "mysterious error" issue, since I couldn't cause that error to occur.  However, I can understand in theory how it could fix that.  Positive review.


---

Comment by mhansen created at 2009-11-13 04:57:34

Resolution: fixed
