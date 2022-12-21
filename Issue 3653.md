# Issue 3653: Better random complex numbers

Issue created by migration from Trac.

Original creator: novoselt

Original creation time: 2008-07-13 22:34:23

Assignee: somebody

I have tried to generate some random complex numbers today and discovered that random_element behaves somewhat unexpected - without arguments it returns integer values between -2 and 2, with an optional argument n - integers between -n and n. That is exactly what is described in the documentation, but I would expect it to be a random complex number from the square [-1,1]x[-1,1] or unit disk and with an argument - a random value from the square or the disk of given size.


---

Comment by cwitty created at 2008-08-02 13:43:30

Changing assignee from somebody to cwitty.


---

Comment by cwitty created at 2008-08-02 13:43:30

Changing status from new to assigned.


---

Attachment


---

Comment by mhansen created at 2008-08-26 22:07:36

Looks good to me.


---

Comment by mabshoff created at 2008-08-26 22:54:27

Merged in Sage 3.1.2.alpha1


---

Comment by mabshoff created at 2008-08-26 22:54:27

Resolution: fixed
