# Issue 2718: increase the default doctest timeout to 360 seconds

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-03-29 16:28:51

Assignee: failure

E.g., issues like this:


```
The athlon 32-bit linux box has the most files failing:
   http://sage.math.washington.edu/home/was/build/tests/2.11.alpha2/Linux-meccah.log

	sage -t  devel/sage-main/sage/interfaces/psage.py
	sage -t  devel/sage-main/sage/interfaces/sage0.py
	sage -t  devel/sage-main/sage/dsage/tests/testdoc.py
	sage -t  devel/sage-main/sage/calculus/calculus.py

Also tut.tex fails due to the timeout. 

We should raise the timeout, since calculus is a timeout issue, and
it should be possible to test Sage even on a mere 2.1Ghz machine.
```



---

Attachment


---

Comment by mabshoff created at 2008-03-29 17:22:07

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-03-29 17:22:07

Changing assignee from failure to mabshoff.


---

Comment by cwitty created at 2008-03-29 17:27:14

I tested that the patch applies and doctesting still works; I did not explicitly test that the timeout changed.

Looks good.


---

Comment by mabshoff created at 2008-03-29 17:33:36

Merged in Sage 2.11.rc0


---

Comment by mabshoff created at 2008-03-29 17:33:36

Resolution: fixed
