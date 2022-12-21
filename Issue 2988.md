# Issue 2988: notebook -- issues with the CSS for the print display

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-21 14:24:04

Assignee: boothby

Mabshoff -- sorry I have to put this in as a 3.0 block (and fix it now).  It won't affect anything doctested.  I've had several professors (including me!) complain about issues with the notebook css and printing.  And, I told them I would fix this for 3.0.  




---

Attachment

Excellent!


---

Comment by mabshoff created at 2008-04-22 03:53:03

It doesn't apply cleanly against rc1:

```
sage`@`modular:~/build/sage-3.0.rc1/devel/sage$ hg import /home2/mabshoff/trac_2988.patch
applying /home2/mabshoff/trac_2988.patch
patching file sage/server/notebook/cell.py
Hunk #1 FAILED at 645
1 out of 2 hunks FAILED -- saving rejects to file sage/server/notebook/cell.py.rej
abort: patch failed to apply
```


Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-04-22 04:36:56

Merged sage-2988_rebased.patch in Sage 3.0.final


---

Comment by mabshoff created at 2008-04-22 04:36:56

Resolution: fixed
