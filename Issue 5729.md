# Issue 5729: Cleanup of crystal code: cartan_type now a method rather than attribute

Issue created by migration from https://trac.sagemath.org/ticket/5729

Original creator: aschilling

Original creation time: 2009-04-09 20:07:32

Assignee: aschillin

CC:  sage-combinat

Changed the user interface to have cartan type as a method
rather than attribute


---

Attachment

changed according to Nicolas' suggestions


---

Attachment


---

Attachment

Final version of the patch uploaded:
 - fixes 2/3 remaining calls to parent() 
 - Micro doc improvements


---

Comment by aschilling created at 2009-04-10 23:52:14

Resolution: fixed


---

Comment by mabshoff created at 2009-04-10 23:58:52

Resolution changed from fixed to 


---

Comment by mabshoff created at 2009-04-10 23:58:52

Huh? This ticket has not been merged.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-10 23:58:52

Changing status from closed to reopened.


---

Comment by mabshoff created at 2009-04-11 00:43:56

Resolution: fixed


---

Comment by mabshoff created at 2009-04-11 00:43:56

Merged crystal-5729-track.2.patch in Sage 3.4.1.rc2.

Cheers,

Michael
