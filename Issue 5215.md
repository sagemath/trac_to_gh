# Issue 5215: [with patch, needs review] Remove ipython1-20070130.spkg from Sage

Issue created by migration from https://trac.sagemath.org/ticket/5215

Original creator: mabshoff

Original creation time: 2009-02-09 12:20:24

Assignee: mabshoff

ipython1-20070130.spkg is very outdated and since ipython 0.9.0 the functionality has been migrated into ipython itself. Since we are now shipping ipython 0.9.1 remove the ipython1-20070130.spkg from the Sage distribution. Besides deleting the spkg one also needs to change deps and install.

I will post diff for deps and install momentarily.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-09 12:20:31

Changing status from new to assigned.


---

Attachment


---

Attachment

Looks good.  Hurray for removing cruft!


---

Comment by mabshoff created at 2009-02-11 06:10:33

Resolution: fixed


---

Comment by mabshoff created at 2009-02-11 06:10:33

(Un)Merged in Sage 3.3.rc0 :)

Cheers,

Michael
