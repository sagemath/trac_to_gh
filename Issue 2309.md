# Issue 2309: [with patch, needs review] #2267 introduced spurious linebreak commands '\\'

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-02-26 03:45:18

Assignee: tba

mabshoff changed `\&` to `\\&`; the correct fix is to change to `&`.  I rebuilt the manual, and verified that it does rebuild and that the spurious linebreaks are gone (although the formatting in the second relevant section is still pretty bad).



---

Attachment

Nice catch by cwitty. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-26 04:07:13

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-02-26 04:07:13

Merged in Sage 2.10.3.alpha0


---

Comment by mabshoff created at 2008-02-26 04:07:13

Changing assignee from tba to mabshoff.


---

Comment by mabshoff created at 2008-02-26 04:27:05

Resolution: fixed


---

Comment by mabshoff created at 2008-02-26 04:27:05

Merged in Sage 2.10.3.alpha0
