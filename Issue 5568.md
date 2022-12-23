# Issue 5568: [with patch, needs review] a few latex methods

Issue created by migration from https://trac.sagemath.org/ticket/5568

Original creator: jhpalmieri

Original creation time: 2009-03-19 17:59:55

Assignee: jhpalmieri

Two issues: QQbar doesn't seem to have a latex method. Also, the latex method for CC is "\\C", which is not a valid LaTeX command. For example, if I type "view(CC)" in the notebook, jsmath gives an error, and if I type "view(CC)" from the command line, I get a blank page.

This patch provides a latex method for QQbar and changes the latex method for CC (note that it uses `\mathbf`, just as the latex methods for RR, ZZ, and QQ do).



---

Attachment

Looks good.  Positive review.


---

Comment by mabshoff created at 2009-03-25 07:42:08

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-25 07:42:08

Resolution: fixed
