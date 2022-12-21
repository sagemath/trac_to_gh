# Issue 1651: bug in decode

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-01-01 14:46:56

Assignee: wdj

Reported by Harald Schilly:

Here what I've tried (documentation does it a bit more "difficult",
but should be the same -- at least I hope so)
http://www.sagemath.org/doc/html/const/node37.html

C = HammingCode(2,GF(5))
v = matrix(GF(5),[This is the Trac macro *1,0,0,2,1,0* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1,0,0,2,1,0-macro))
C.decode(v)

works (at least no errors), but

v = vector(GF(5),[1,0,0,2,1,0])
C.decode(v)

says:

TypeError: Gap produced error output
Permutation: <expr> must be a positive integer (not a integer)
executing $sage333:=(1, 0, 0, 2, 1, 0);;

I can see the different braces in the output, but internally a 1xn/nx1
matrix should handled in some way the same as a vector.



---

Comment by wdj created at 2008-01-02 17:47:33

I fixed this bug. The patch is at
http://sage.math.washington.edu/home/wdj/patches/linear-codes20071210.hg
It passes sage -t.


---

Comment by wdj created at 2008-01-02 17:56:11

patch for bug fix of decode in linear_code.py


---

Attachment


---

Attachment


---

Comment by ncalexan created at 2008-01-22 18:03:08

Seems reasonable, I say apply.  The formatting on the 1651-doctest patch is not the best, and I don't think the docstring to decode() is clear about what the acceptable inputs are.


---

Attachment

I added an attachment which includes (1) my fix of the H Schilly bug, (2) M Hansen's docstring addition (reformatted, as the referee suggested), (3) an additional doctest (as suggested by the referee).


---

Comment by mabshoff created at 2008-02-02 03:21:53

Could we get somebody to review this updated patch?

Cheers,

Michael


---

Comment by ncalexan created at 2008-02-16 17:19:25

Thumbs up from me!


---

Comment by mabshoff created at 2008-02-16 17:25:32

Resolution: fixed


---

Comment by mabshoff created at 2008-02-16 17:25:32

Merged linear_code20080127.hg in Sage 2.10.2.alpha0


---

Comment by mabshoff created at 2008-02-16 18:17:51

Arrg, it was actually merged in Sage 2.10.2.alpha1
