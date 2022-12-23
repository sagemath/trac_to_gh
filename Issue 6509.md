# Issue 6509: sum of four squares function

Issue created by migration from https://trac.sagemath.org/ticket/6509

Original creator: mhampton

Original creation time: 2009-07-10 20:19:55

Assignee: somebody

This can probably be improved, but its a first attempt that seems to work.


---

Attachment


---

Comment by mhampton created at 2009-07-10 21:09:00

Oops, last one had a few mistakes.  Current version is correct up to 10000 I think with the new "long" doctest.


---

Comment by jsp created at 2009-07-10 21:23:43

Tested this with a lot of values taken from:
[http://www.research.att.com/~njas/sequences/A006431](http://www.research.att.com/~njas/sequences/A006431)

and usage of:

[http://www.alpertron.com.ar/FSQUARES.HTM](http://www.alpertron.com.ar/FSQUARES.HTM)

When we look at [http://www.research.att.com/~njas/sequences/A002635](http://www.research.att.com/~njas/sequences/A002635)
we see that for instance 82 can be written in 7 ways as the sum of
4 squares. For more results see:
[http://www.research.att.com/~njas/sequences/b002635.txt](http://www.research.att.com/~njas/sequences/b002635.txt)

So indeed this can be improved. But for now this is ok for a first attempt.
Positive review.

Jaap


---

Comment by mvngu created at 2009-07-18 18:34:01

This is a duplicate of ticket #6529. That ticket also incorporates the code contained in `trac_6509_four_squares.patch`.


---

Comment by mvngu created at 2009-07-18 18:34:01

Resolution: duplicate
