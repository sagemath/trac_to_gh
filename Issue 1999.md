# Issue 1999: delete mpl3d code from sage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-31 05:16:17

Assignee: was

The code in 

```
 devel/sage-main/sage/plot/mpl3d
```

should all be deleted from Sage.  It's ugly toy code, and Sage has much better 3d code now.  Also, there is likely a better version of that code in matplotlib itself. 


---

Comment by was created at 2008-01-31 05:18:18

The code in 

```
devel/sage/sage/server/server1
```

should all be deleted.


---

Comment by mabshoff created at 2008-02-02 07:12:50

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-02-02 07:12:50

Changing assignee from was to mabshoff.


---

Attachment


---

Comment by was created at 2008-02-02 07:53:08

Positive review on mabshoff's part 1 patch.


---

Comment by mabshoff created at 2008-02-02 07:55:52

The second patch looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-02 07:58:05

Both patches merged in Sage 2.10.1.rc5


---

Comment by mabshoff created at 2008-02-02 07:58:05

Resolution: fixed
