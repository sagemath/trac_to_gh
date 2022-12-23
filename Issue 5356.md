# Issue 5356: 100r returns a Sage integer in the notebook (but commandline works fine)

Issue created by migration from https://trac.sagemath.org/ticket/5356

Original creator: jason

Original creation time: 2009-02-24 07:53:16

Assignee: boothby

type(100r) returns

<type 'sage.rings.integer.Integer'>

in the notebook in 3.3.  Similarly, type(1.0r) returns

<type 'sage.rings.real_mpfr.RealLiteral'>

Both of these examples work fine on the command line (i.e., return python int and float, respectively).




---

Attachment


---

Comment by jason created at 2009-02-24 08:37:45

This patch fixes the problem and passes doctests in preparser.py.  Someone more familiar with the preparse might look at it, but it's a positive review for me.


---

Comment by was created at 2009-02-24 14:33:27

+1 from me.


---

Comment by mabshoff created at 2009-02-24 19:53:26

Merged in Sage 3.4.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-24 19:53:26

Resolution: fixed
