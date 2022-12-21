# Issue 5320: update Sphinx to 0.5.1

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-02-20 11:20:32

Assignee: mabshoff

The spkg can be found at http://sage.math.washington.edu/home/mhansen/sphinx-0.5.1.spkg

This requires an update to setuptools 0.6c9 as well.


---

Comment by mhansen created at 2009-02-20 11:27:41

Changing status from new to assigned.


---

Comment by mhansen created at 2009-02-20 11:27:41

Changing assignee from mabshoff to mhansen.


---

Comment by mhansen created at 2009-02-20 11:27:41

The setup tools spkg can be found at http://sage.math.washington.edu/home/mhansen/setuptools-0.6c9.spkg


---

Comment by mabshoff created at 2009-02-20 12:07:31

Both spkgs are clean, all changes checked in and documented. Positive review. I made spkg-install in setuptools-0.6c9.spkg executable without bumping the patch level, but if that would get lost it wouldn't matter too much.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 12:07:55

Merged in Sage 3.3.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 12:07:55

Resolution: fixed
