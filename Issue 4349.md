# Issue 4349: jmol doesn't work on the command-line on OS X 10.5(.5)

Issue created by migration from Trac.

Original creator: anakha

Original creation time: 2008-10-23 17:39:38

Assignee: anakha

If you plot something in 3D on the command-line, buy default it pops up a jmol applet window showing the graphic (at least it did).  But now java fails to start in the sage environement.


---

Comment by mabshoff created at 2008-10-23 17:44:41

Any chance you keep your OSX box uptodate with the latest Apple patches? Apple posted a borked Java update about 10 days ago that breaks all kinds of Java apps.

Cheers,

Michael


---

Comment by anakha created at 2008-10-23 17:59:40

Yes, it's always up to the latest patch


---

Comment by anakha created at 2008-10-23 18:17:26

Changing status from new to assigned.


---

Attachment

Fixes the bug by cleaning up the environment with sage-native-execute before calling jmol.


---

Comment by mabshoff created at 2008-10-26 16:32:56

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-27 02:10:59

Resolution: fixed


---

Comment by mabshoff created at 2008-10-27 02:10:59

Merged in Sage 3.2.alpha1
