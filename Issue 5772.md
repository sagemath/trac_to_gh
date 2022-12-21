# Issue 5772: notebook -- typo in twist.py causes Internal Server Error

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-13 04:10:42

Assignee: boothby


```
	  File "/Users/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/server/notebook/twist.py", line 379, in callback
	    return HTMLRespone(stream = message(s, '/'))
	exceptions.NameError: global name 'HTMLRespone' is not defined
```



---

Attachment


---

Comment by ddrake created at 2009-04-13 04:17:34

I give this a positie review. :)


---

Comment by mabshoff created at 2009-04-13 05:49:39

Resolution: fixed


---

Comment by mabshoff created at 2009-04-13 05:49:39

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
