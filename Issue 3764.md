# Issue 3764: notebook -- notebook.py coverage to

Issue created by migration from https://trac.sagemath.org/ticket/3764

Original creator: TimothyClemans

Original creation time: 2008-08-03 14:03:57

Assignee: boothby




---

Attachment


---

Attachment

Note: there is a script for applying the various Notebook patches. The base is sage-3.0.6. 

http://sage.math.washington.edu/home/tclemans/uw_contract_work/apply_patches.sage


---

Attachment


---

Attachment


---

Attachment

removed log_server stuff from Notebook class since it doesn't do anything


---

Comment by mabshoff created at 2008-08-08 23:51:13

Tom,

if you have time today can you look at this? It is holding up a bunch of other patches. Except the last patch I can give it a positive review myself.

Cheers,

Michael


---

Attachment

followup upon refereeing the code


---

Comment by was created at 2008-08-10 03:43:57

REFEREE REPORT:

 Excellent.  This rocks!   Positive review.

 I deleted test_notebook.py which was the ancient dead never once used code that was the reason for the log_server stuff.


---

Comment by mabshoff created at 2008-08-10 04:02:51

sage-3764_7.patch looks good to me. William explained why the non-used code has been removed.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-10 04:29:19

Merged sage-3764_1.patch-sage-3764_7.patch in Sage 3.1.alpha1


---

Comment by mabshoff created at 2008-08-10 04:29:19

Resolution: fixed
