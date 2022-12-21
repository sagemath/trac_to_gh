# Issue 7082: SageNB -- WorksheetProcess is an old-style class

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2009-09-30 10:21:43

Assignee: boothby

Keywords: sagenb notebook

WorksheetProcess in `worksheet_process.py` does not inherit from `object`


---

Comment by timdumol created at 2009-09-30 10:23:01

Makes `WorksheetProcess` a new-style class. Also fixes some docstring problems, and updates `misc.py`


---

Attachment

I applied this patch and there are a spectacular number of merge conflicts:


```
flat:sagenb wstein$ hg import trac_7082-old-style-class.patch 
applying trac_7082-old-style-class.patch
patching file sagenb/interfaces/reference.py
Hunk #1 FAILED at 79
1 out of 1 hunks FAILED -- saving rejects to file sagenb/interfaces/reference.py.rej
patching file sagenb/interfaces/reference.py
Hunk #1 FAILED at 79
1 out of 1 hunks FAILED -- saving rejects to file sagenb/interfaces/reference.py.rej
patching file sagenb/interfaces/worksheet_process.py
Hunk #1 FAILED at 17
1 out of 1 hunks FAILED -- saving rejects to file sagenb/interfaces/worksheet_process.py.rej
patching file sagenb/misc/sageinspect.py
Hunk #1 FAILED at 11
Hunk #2 FAILED at 223
Hunk #3 FAILED at 265
Hunk #4 FAILED at 307
Hunk #5 succeeded at 396 with fuzz 2 (offset 4 lines).
Hunk #6 FAILED at 624
Hunk #7 FAILED at 663
6 out of 7 hunks FAILED -- saving rejects to file sagenb/misc/sageinspect.py.rej
patching file sagenb/interfaces/reference.py
Hunk #1 FAILED at 79
1 out of 1 hunks FAILED -- saving rejects to file sagenb/interfaces/reference.py.rej
patching file sagenb/interfaces/worksheet_process.py
Hunk #1 FAILED at 17
1 out of 1 hunks FAILED -- saving rejects to file sagenb/interfaces/worksheet_process.py.rej
patching file sagenb/misc/sageinspect.py
Hunk #1 FAILED at 11
Hunk #2 FAILED at 223
Hunk #3 FAILED at 265
Hunk #4 FAILED at 307
Hunk #5 succeeded at 401 with fuzz 2 (offset 9 lines).
Hunk #6 FAILED at 624
Hunk #7 FAILED at 663
6 out of 7 hunks FAILED -- saving rejects to file sagenb/misc/sageinspect.py.rej
patching file sagenb/interfaces/worksheet_process.py
Hunk #1 FAILED at 17
1 out of 1 hunks FAILED -- saving rejects to file sagenb/interfaces/worksheet_process.py.rej
patching file sagenb/misc/sageinspect.py
Hunk #1 FAILED at 11
Hunk #2 FAILED at 223
Hunk #3 FAILED at 265
Hunk #4 FAILED at 307
Hunk #5 succeeded at 406 with fuzz 2 (offset 14 lines).
Hunk #6 FAILED at 624
Hunk #7 FAILED at 663
6 out of 7 hunks FAILED -- saving rejects to file sagenb/misc/sageinspect.py.rej
abort: patch failed to apply
```


Could you rebase it against my repo?  http://sage.math.washington.edu:8100/


---

Comment by timdumol created at 2009-10-23 17:40:32

The changes in this patch have already been included.


---

Comment by mhansen created at 2009-11-15 14:15:41

Resolution: invalid
