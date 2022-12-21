# Issue 408: Notebook glitch in Safari

Issue created by migration from Trac.

Original creator: justin

Original creation time: 2007-07-27 05:16:05

Assignee: was

This is on Mac OS X, 10.4.10, with Safari, using SAGE 2.7.1.

If I create a worksheet, fiddle around with it, and then quit and restart the server,
going to "localhost/8000" gives me a page with the worksheet shown (as possibly
one of many).  If I click the adjacent check box and then the DELETE button, the
check box is cleared but the worksheet entry remains.  Only when I 'refresh' the page
does the worksheet entry disappear.



---

Comment by justin created at 2007-07-27 05:16:34

Oh: on a MacBook Pro, FWIW.


---

Comment by was created at 2007-07-27 19:19:55

Changing assignee from was to boothby.


---

Comment by was created at 2007-07-27 19:19:55

Changing component from algebraic geometry to notebook.


---

Comment by was created at 2007-07-27 19:19:55

I think this is indeed safari-specific.  I think for some reason safari doesn't
update the page when the javascript attempts a refresh, though firefox does.
We need to either directly modify the DOM (more work, but the right thing to do), 
or improve the refresh() javascript function so it also works with safari.


---

Comment by was created at 2007-08-19 08:33:17

This is really an enhancement -- i.e., this dynamic stuff needs to be implemented for that screen (without
using refresh).


---

Comment by was created at 2007-08-19 08:33:17

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2008-04-20 07:19:19

This is quite an old ticket. Can somebody check with 3.0 if this is still a problem?

Cheers,

Michael


---

Comment by was created at 2008-05-10 20:30:56

Resolution: fixed


---

Comment by was created at 2008-05-10 20:30:56

I fixed this.  It is no longer a problem.
