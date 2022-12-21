# Issue 3149: [with patch, needs review] off-by-one error in real_roots on AA coefficients

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-05-10 17:36:20

Assignee: malb

The code in real_roots.pyx for handling polynomials with AA coefficients had an off-by-one error in the case of integral coefficients.


---

Attachment


---

Comment by malb created at 2008-06-03 16:29:16

Remove assignee malb.


---

Comment by craigcitro created at 2008-06-15 21:43:29

Changing keywords from "" to "editor_craigcitro".


---

Comment by craigcitro created at 2008-06-15 22:34:03

Looks good. Just so that it's on record:

the 4 -> 6 change simply ups the default precision to which something is computed. The `ceil()` to `floor() + 1` change only applies in the case of an exact answer, and this way the strict inequality requested in the new comment is always satisfied. The doctest exactly checks this.


---

Comment by mabshoff created at 2008-06-16 19:06:38

Set assignee to cwitty.


---

Comment by mabshoff created at 2008-06-23 05:53:59

Resolution: fixed


---

Comment by mabshoff created at 2008-06-23 05:53:59

Merged in Sage 3.0.4.alpha0
