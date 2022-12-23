# Issue 1485: wrapper for invariant_ring and invariant_algebra_reynolds in Singular

Issue created by migration from https://trac.sagemath.org/ticket/1485

Original creator: wdj

Original creation time: 2007-12-13 12:30:16

Assignee: malb

Wraps Singular's invariant_algebra_reynolds and invariant_ring in finvar.lib, with help from Simon King and Martin Albrecht. Computes generators for the polynomial ring F[x1,...,xn]^G, where G in GL(n,F) is a finite matrix group.

In the "good characteristic" case the polynomials returned form a minimal generating set for the algebra of G-invariant polynomials. In the "bad" case, the polynomials returned are primary and secondary invariants, forming a not necessarily minimal generating set for the algebra of G-invariant polynomials.

Patch is at
http://sage.math.washington.edu/home/wdj/patches/matrix_group20071213.hg
and file is at
http://sage.math.washington.edu/home/wdj/patches/matrix_group.py


---

Comment by wdj created at 2007-12-13 12:31:49

This is indirectly related to trac ticket http://sagetrac.org/sage_trac/ticket/1274
but does not resolve that issue.


---

Attachment

The patch applies cleanly and the doctests pass. I cannot check the results due to lack of knowledge, though. Good to go in, if you ask me.


---

Comment by mabshoff created at 2008-01-16 17:24:00

Merged in Sage 2.10.alpha4


---

Comment by mabshoff created at 2008-01-16 17:24:00

Resolution: fixed


---

Comment by mabshoff created at 2008-01-16 22:12:39

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-01-16 22:12:39

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-01-16 22:12:39

The patch causes hangs when doctesting `plot/plot3d/transform.pyx`. The really odd thing is that everything is fine when running that doctest with the `-verbose` flag.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-16 22:17:13

While somebody is at it: please attach single commit change sets as patch in the future.

Cheers,

Michael


---

Comment by malb created at 2008-01-18 16:29:32

Changing status from reopened to new.


---

Comment by malb created at 2008-01-18 16:29:32

Changing assignee from malb to wdj.


---

Comment by mabshoff created at 2008-01-19 17:00:53

Mercurial is stupid: I applied this patch in alpha4, but reverted it by applying the inverse with patch and committed. But unbundling the bundle again doesn't commit *anything*.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-19 17:08:07

Resolution: fixed
