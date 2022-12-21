# Issue 544: doctesting const.tex should not pop up any windows

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-08-31 20:12:03

Assignee: wdjoyner

It is very annoying that doctesting const.tex causes a bunch of windows to pop up.
This should not happen.  Stop this by putting #optional after all doctests that
would pop up a window, so they aren't actually run, except in the rare cases when
I'm running all optional doctests (and then popups are fine). 




---

Comment by mhansen created at 2007-09-06 23:45:18

Changing assignee from wdjoyner to mhansen.


---

Attachment

Patch attached.


---

Comment by was created at 2007-09-07 03:16:08

Resolution: fixed
