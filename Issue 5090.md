# Issue 5090: upgrade numpy to 1.2.1

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-01-24 16:35:47

Assignee: was

An spkg is at http://sage.math.washington.edu/home/jason/numpy-1.2.1.spkg


---

Comment by mabshoff created at 2009-01-24 18:03:02

Jason,

this sounds like it is ready to be reviewed. Am I correct?

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 18:03:28

Changing component from linear algebra to packages.


---

Comment by mabshoff created at 2009-01-24 18:03:28

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2009-01-24 18:03:28

And this is a package, so move it from linear algebra.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 18:04:24

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 18:04:24

Merged in Sage 3.3.alpha2

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 18:04:52

Oops, I will review this later.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 18:04:52

Resolution changed from fixed to 


---

Comment by mabshoff created at 2009-01-24 18:04:52

Changing status from closed to reopened.


---

Comment by jason created at 2009-01-24 21:40:48

Michael, yes you are correct on all accounts.


---

Comment by jason created at 2009-01-25 02:50:55

Actually, I just remembered that I removed the patch which silenced deprecation warnings.  This was because I was hoping this spkg would be merged with the new scipy 0.7, and the deprecated calls would be fixed.  So we should hold off on this upgrade for now.


---

Comment by craigcitro created at 2009-06-12 06:56:00

This has been superseded by #6140, which has been merged in `4.0.2.alpha0`. I'm closing as `wontfix`, though maybe `duplicate` is just as good.


---

Comment by craigcitro created at 2009-06-12 06:56:00

Resolution: wontfix
