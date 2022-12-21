# Issue 5401: Fix the permission issues with the CC field after the trac 0.10.3 -> 0.11.3 update

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-28 16:55:46

Assignee: schilly

CC:  mhansen jason

From #5400:

Me:

```
I assume you know about the CC field, so what is the problem? 
```

Jason:

```
The only CC option I have now with the new trac is to add myself. It's not a text box anymore. 
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-03-01 04:51:38

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-03-01 04:51:38

Jason,

I have granted authenticated users the permission "TICKET_EDIT_CC" - please check if you now can change the CC field and give this ticket a positive review in that case.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-01 04:51:38

Changing assignee from schilly to mabshoff.


---

Comment by jason created at 2009-03-01 06:13:05

I get a text box for the CC field now.


---

Comment by mabshoff created at 2009-03-01 06:15:13

Excellent. Fixed during the Sage 3.4.rc0 release cycle.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-01 06:15:13

Resolution: fixed
