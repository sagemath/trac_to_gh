# Issue 2569: Add XOR to preparser

Issue created by migration from https://trac.sagemath.org/ticket/2569

Original creator: vgermrk

Original creation time: 2008-03-17 09:35:50

Assignee: cwitty

Since the preparser replaces "^" with "**",
there should be a way to access the python-buildin-XOR again.

The discussion is here: [http://groups.google.com/group/sage-devel/browse_thread/thread/a7aaccd2081098bc/de225692ee38f0a5](http://groups.google.com/group/sage-devel/browse_thread/thread/a7aaccd2081098bc/de225692ee38f0a5)

The conclusion is:

```
Unless somebody thinks of something better, I like ^^ as well.

William
```




So the preparser should replace "^^" with "^".


---

Attachment


---

Comment by mhansen created at 2008-08-24 23:55:19

Looks good to me.


---

Comment by mabshoff created at 2008-08-25 01:13:54

Resolution: fixed


---

Comment by mabshoff created at 2008-08-25 01:13:54

Merged all three patches in Sage 3.1.2.alpha1


---

Comment by mabshoff created at 2008-08-25 01:22:00

Oops, merged the one and only patch attached to this ticket. Damn copy & paste ;)

Cheers,

Michael
