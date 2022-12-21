# Issue 1051: pari/gp extended help stops working when sage tree is moved

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-11-01 06:25:48

Assignee: cwitty

With the new pari-2.3.2.p4.spkg, the ?? help works.  However, it stops working when the Sage tree is moved, because libpari hardcodes the path to the gphelp binary.

This path can be overridden with the GPHELP environment variable; sage-env should set that variable.


---

Attachment


---

Comment by cwitty created at 2007-11-02 01:03:48

The attached patch (to sage_scripts) fixes this problem.


---

Comment by mabshoff created at 2007-11-02 02:00:02

Resolution: fixed


---

Comment by mabshoff created at 2007-11-02 02:00:02

applied to 2.8.11.rc1
