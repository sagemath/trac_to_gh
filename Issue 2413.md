# Issue 2413: Correction in "How to use the Sage Notebook"

Issue created by migration from https://trac.sagemath.org/ticket/2413

Original creator: hfvillafuerte

Original creation time: 2008-03-06 23:33:19

Assignee: tba

In SAGE Notebook Help:

The variable DATA contains the directory with data files that you upload into the worksheet. For example, to open a file in that directory, do "open(DIR+'filename')".


should be:

The variable DATA contains the directory with data files that you upload into the worksheet. For example, to open a file in that directory, do "open(DATA+'filename')".


---

Comment by jwmerrill created at 2008-09-14 05:23:07

I believe this refers to documentation which is generated from server/notebook/tutorial.py, and which shows up on the introductory page when you click help from the notebook.  If so, this is already fixed as of 3.1.2.rc2.


---

Comment by mabshoff created at 2008-09-14 05:34:56

Resolution: fixed


---

Comment by mabshoff created at 2008-09-14 05:34:56

This was fixed in Sage 3.0.1 via #3095. Thanks for tracking this down.

Cheers,

Michael
