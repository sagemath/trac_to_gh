# Issue 3351: update SAGE_ROOT/COPYING.txt to clarify situation wrt Maxima license

Issue created by migration from https://trac.sagemath.org/ticket/3351

Original creator: was

Original creation time: 2008-06-02 13:43:34

Assignee: mabshoff

See 

   http://www.math.utexas.edu/pipermail/maxima/2008/011882.html

where we learn that Maxima is GPLv2 only, not GPLv2+.  This means that
we can not binary link Maxima and Sage. 

Something from the email at the above link should be mentioned in the
COPYING.txt file, and the statement at the top of COPYING.txt that

"Every component of SAGE except jsmath is licensed under a GPL v2 (or
later) compatible license." may need to be changed to

"Every component of SAGE except jsmath is licensed under a GPL v2 compatible
or GPLv2+  compatible license.  All components that are binary linked
to Sage are GPLv2+."


---

Comment by was created at 2008-06-02 13:43:45

Changing component from Cygwin to packages.


---

Comment by mabshoff created at 2008-06-02 15:21:46

The statement "All components that are binary linked to Sage are GPLv2+." is incorrect since we are linking against a [L]GPL V3+ GSL, GMP and GNUTSL library.

Cheers,

Michael


---

Comment by aapitzsch created at 2014-08-12 21:04:28

This has been fixed in #12447.


---

Comment by aapitzsch created at 2014-08-12 21:04:28

Changing status from new to needs_review.


---

Comment by kcrisman created at 2014-08-14 13:46:45

Yes, you are right!


---

Comment by kcrisman created at 2014-08-14 13:46:45

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-08-20 20:32:45

Resolution: duplicate
