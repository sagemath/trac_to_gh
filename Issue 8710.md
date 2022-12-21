# Issue 8710: eigenmatrix_right returns inconsistent results for eigenvectors

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2010-04-18 03:30:23

Assignee: jason, was

CC:  jhpalmieri alexghitza

Doctests introduced in #4756 return the negative of certain eigenvectors on certain hardware.

See initital discussion at 

http://groups.google.com/group/sage-release/browse_thread/thread/9136569bd1c67f6


---

Attachment


---

Comment by rbeezer created at 2010-04-19 04:53:29

This patch massages the doctests that were causing failures for 4.4.alpha0 on the Skynet machine, sextus.  Its not pretty, but I hope the results are now hardware-neutral.

Alex - you reviewed the original ticket (#4756), so maybe this would be an easy review for you?

John - I don't know if it is easy for you to test this on sextus in advance of merging it?  Sounds like it will be a while before I have that kind of access.

Rob


---

Comment by rbeezer created at 2010-04-19 04:53:29

Changing status from new to needs_review.


---

Comment by was created at 2010-04-19 05:00:50

1. John will have to test, since he has the build on sextus. 

2. The doctests actually look much nicer normalized to have first entry 1! 

(I would give this a positive review if this works.)


---

Comment by rbeezer created at 2010-04-19 05:15:39

Replying to [comment:3 was]:
> 2. The doctests actually look much nicer normalized to have first entry 1! 

The output looks nicer because this matrix is out of my textbook and was *designed* to have nice-looking answers.  I don't like the hard-to-decipher code that gets you there, but that's the way it goes.  Thanks for having a look and for the advice on getting this squared away.

Rob


---

Comment by jhpalmieri created at 2010-04-19 05:35:56

Tests pass on sextus.  I'll test it on a few more machines, and if it works, I'll give it a positive review and merge it into 4.4.alpha1.


---

Comment by rbeezer created at 2010-04-27 05:23:53

Hi John,

Did this eventually past muster on skynet, or does it need more testing?

I still haven't done the `SciPy` tests I'd like to do skynet yet, but hope to get to that soon.

Rob


---

Comment by jhpalmieri created at 2010-04-27 05:59:12

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-27 05:59:12

Sorry, Rob.  This was actually merged in 4.4.alpha1 but I forgot to mark it as closed.  (So it didn't get recorded in the release notes, either.)
