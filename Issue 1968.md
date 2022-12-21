# Issue 1968: notebook -- remove capability of using live tutorial for users not signed in to the notebook server

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-29 10:20:17

Assignee: boothby

Timothy Clemans points out to me in chat a *major* security issue with the notebook.  If a user visits the live tutorial, e.g., 

    https://your_computer:port/doc/live/tut/node5.html

then they can execute code even if they aren't logged in!

This is a major security hole if somebody is running their own notebook server.

Solution: by changing about 2 lines in server/notebook/twist.py, one can change it
so the entire live tutorial is inaccessible accept to users that are logged in.  This should be done. 




---

Attachment


---

Comment by jkantor created at 2008-02-01 04:56:09

This seems to work.
Directly visiting the tutorial as above works when logged in but not when logged out
(you get a not found error in the browser).


was: can you clarify that this is the intended effect.


---

Comment by was created at 2008-02-01 05:12:04

> was: can you clarify that this is the intended effect.

Yes, that is exactly the intended effect.  Excellent.


---

Comment by mabshoff created at 2008-02-01 05:15:45

Ok, then the review is positive.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-01 05:17:18

Resolution: fixed


---

Comment by mabshoff created at 2008-02-01 05:17:18

Merged in Sage 2.10.1.rc4
