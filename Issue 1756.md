# Issue 1756: implement MPolynomialIdeal.hilbert_[series|polynomial]

Issue created by migration from https://trac.sagemath.org/ticket/1756

Original creator: malb

Original creation time: 2008-01-11 18:34:12

Assignee: malb

The result should be somewhat similar to what MAGMA has to offer

   http://magma.maths.usyd.edu.au/magma/htmlhelp/text1128.htm

. SINGULAR has support for Hilbert Series computation

  http://www.singular.uni-kl.de/Manual/3-0-4/sing_212.htm

which probably can be wrapped to provide the desired functionality.


---

Comment by mabshoff created at 2008-01-11 18:40:06

Singular's Hilbert series has overflow issues in certain situations. Let me digg out some email about a test case and report this to the Singular team.

Cheers,

Michael


---

Comment by malb created at 2008-01-16 15:47:08

See #1793 for a patch, copying mabshoff's comment over to that ticket now and closing this as dupe.


---

Comment by malb created at 2008-01-16 15:47:08

Resolution: duplicate
