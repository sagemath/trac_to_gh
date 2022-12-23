# Issue 3996: [with patch, needs review] doctest the Singular interface

Issue created by migration from https://trac.sagemath.org/ticket/3996

Original creator: mhansen

Original creation time: 2008-08-29 21:57:00

Assignee: was




---

Comment by malb created at 2008-08-29 22:08:54

*Review*
 * I don't think you need `sage: os.unlink(filename)` since the file is in tmp anyway
 * Sometimes the *r* before `"""` is missing but e.g. `\var` is used


If those are fixed, I'll give it a positive review.


---

Attachment


---

Comment by mabshoff created at 2008-08-29 22:37:57

Unfortunately against my current alpha3 merge tree (the only relevant patch here over alpha2 is probably #3988):

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/devel/sage$ patch -p1 --dry-run < trac_3996.patch 
patching file sage/interfaces/singular.py
Hunk #13 succeeded at 1010 with fuzz 2.
Hunk #14 succeeded at 1106 (offset 44 lines).
Hunk #15 FAILED at 1168.
Hunk #16 succeeded at 1350 (offset 44 lines).
Hunk #17 succeeded at 1375 (offset 44 lines).
Hunk #18 succeeded at 1399 (offset 44 lines).
Hunk #19 succeeded at 1474 (offset 44 lines).
Hunk #20 succeeded at 1505 (offset 44 lines).
Hunk #21 succeeded at 1524 (offset 44 lines).
Hunk #22 succeeded at 1575 (offset 44 lines).
Hunk #23 succeeded at 1625 (offset 44 lines).
1 out of 23 hunks FAILED -- saving rejects to file sage/interfaces/singular.py.rej
```


Cheers,

Michael


---

Attachment

trac_3996-rebase.patch should apply cleanly.


---

Comment by mabshoff created at 2008-08-30 00:39:17

Merged trac_3996-rebase.patch in Sage 3.1.2.alpha3


---

Comment by mabshoff created at 2008-08-30 00:39:17

Resolution: fixed
