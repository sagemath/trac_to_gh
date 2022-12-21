# Issue 2240: Docstrings and Doctests: calculus.py

Issue created by migration from Trac.

Original creator: cswiercz

Original creation time: 2008-02-21 00:33:46

Assignee: tba

Goal: Enter all missing docstrings and doctests for functions (not beginning with an underscore "_") in the file

calculus/calculus.py.


---

Comment by cswiercz created at 2008-02-21 00:33:57

Changing assignee from tba to cswiercz.


---

Comment by cswiercz created at 2008-02-21 00:36:25

Changing keywords from "" to "docstring, doctest".


---

Attachment


---

Attachment


---

Comment by cswiercz created at 2008-02-25 21:03:52

Attached are patches including docstrings and doctests for some (but not all) functions without docstrings in calculus.py. There are still some low-level functions in calculus.py that require docstrings. However, the author of these patches isn't familiar enough with the functions to do them justice.


---

Comment by cswiercz created at 2008-02-25 21:04:21

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-02-25 21:36:53

Changing priority from minor to major.


---

Attachment


---

Comment by mhansen created at 2008-02-26 05:09:53

Looks good to me.  I've added the last patch which replaces the first and fixes the wont-typo.


---

Comment by mabshoff created at 2008-02-26 05:28:49

No dice, i.e. rejects for all patches:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-2.10.3.alpha0/devel/sage$ patch -p1 --dry-run < trac_2240_8311-2.patch
patching file sage/calculus/calculus.py
Hunk #1 FAILED at 4409.
1 out of 1 hunk FAILED -- saving rejects to file sage/calculus/calculus.py.rej
patching file sage/misc/hg.py
Hunk #1 succeeded at 169 (offset 32 lines).
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-2.10.3.alpha0/devel/sage$ patch -p1 --dry-run < trac_2240_8312.patch
patching file sage/calculus/calculus.py
Hunk #1 FAILED at 437.
1 out of 1 hunk FAILED -- saving rejects to file sage/calculus/calculus.py.rej
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-2.10.3.alpha0/devel/sage$ patch -p1 --dry-run < trac_2240_8313.patch
patching file sage/calculus/calculus.py
Hunk #1 FAILED at 449.
Hunk #2 FAILED at 2545.
Hunk #3 FAILED at 2625.
Hunk #4 FAILED at 5817.
Hunk #5 FAILED at 6459.
Hunk #6 FAILED at 6541.
Hunk #7 FAILED at 6813.
7 out of 7 hunks FAILED -- saving rejects to file sage/calculus/calculus.py.rej
```


Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2008-02-26 05:55:18

New patch posted.


---

Comment by mabshoff created at 2008-02-26 07:39:04

Resolution: fixed


---

Comment by mabshoff created at 2008-02-26 07:39:04

Merged 2240.patch in Sage 2.10.3.alpha0
