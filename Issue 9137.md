# Issue 9137: Infinite konqueror windows when opening notebook

Issue created by migration from https://trac.sagemath.org/ticket/9137

Original creator: ryan

Original creation time: 2010-06-03 23:45:26

Assignee: somebody

CC:  jason mhansen was

Keywords: konqueror, infinite, windows

This is to make sage users aware of a bug that apparently exists in KDE and not in SAGE.

*Behavior:*  On certain system setups, when starting SAGE notebook, konqueror goes haywire and starts opening up an infinite number of windows in the taskbar (none of the windows will show themselves).  Konqueror will continue to open new windows until Xorg is killed.

*References:* [https://bugs.kde.org/show_bug.cgi?id=234620](https://bugs.kde.org/show_bug.cgi?id=234620) (includes screenshots of the problem)

*Workaround:* 1) use ` notebook(open_viewer=False) ` and manually open browser to notebook port  2) Use a browser other than konqueror (you can change the defualt browser in KDE system settings).

*Conclusion:* As stated above, this appears to be a bug in KDE as it affects other software as well.  If you see this bug, please contact the KDE developers.


---

Comment by ryan created at 2010-06-03 23:46:39

Changing status from new to needs_info.


---

Comment by ryan created at 2010-08-28 18:24:14

this bug is closed in KDE 4.5


---

Comment by ryan created at 2010-08-28 18:25:51

[https://bugs.kde.org/show_bug.cgi?id=240677](https://bugs.kde.org/show_bug.cgi?id=240677)

Here is the KDE bug ticket.


---

Comment by jason created at 2010-08-28 19:20:31

I'm not sure who the current release manager is, but this ticket should be closed (see comments above).


---

Comment by mhansen created at 2010-08-28 19:24:33

Resolution: invalid
