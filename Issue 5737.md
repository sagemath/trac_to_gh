# Issue 5737: pynac interface improvements

Issue created by migration from https://trac.sagemath.org/ticket/5737

Original creator: burcin

Original creation time: 2009-04-10 21:09:13

Assignee: burcin

CC:  wstein mhansen ncalexan

Attached patches fix some bugs in the pynac interface and add .find() and .is_polynomial() functions.


---

Comment by burcin created at 2009-04-10 21:09:51

add .find() method


---

Attachment

fix py_real() and py_imag()


---

Comment by burcin created at 2009-04-10 21:10:40

add .is_polynomial()


---

Comment by burcin created at 2009-04-10 21:11:55

Changing status from new to assigned.


---

Attachment


---

Comment by ncalexan created at 2009-04-11 21:54:38

It's not clear that defaulting all objects to be "real" is a good choice, but it'll do for now.  Apply!


---

Comment by mabshoff created at 2009-04-13 09:25:30

Merged all three patches in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-13 09:25:30

Resolution: fixed
