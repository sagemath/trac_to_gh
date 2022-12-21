# Issue 2175: genus2reduction makefile

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-02-16 01:41:19

Assignee: tabbott

I wrote a Makefile for genus2reduction Debian builds, and made Debian apply it as a quilt patch (so it's available as a patch in dist/debian/patches/ of the genus2reduction spkg).  We should probably move the Makefile into the "upstream" eventually.


---

Comment by mabshoff created at 2008-02-20 14:10:42

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-02-20 14:10:42

Since Sage is now upstream for genus2reduction I would suggest that we close this ticket once we have resolved #2225.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-20 14:10:42

Changing assignee from tabbott to mabshoff.


---

Comment by mabshoff created at 2008-02-21 19:18:56

The makefile has been merged and fixes by William to work on OSX again.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-21 19:19:21

Resolution: fixed


---

Comment by mabshoff created at 2008-02-21 19:19:21

Fixed since #2225 was merged.
