# Issue 4751: if spkg/standard contains an extracted directory then "sage -upgrade" fails in multiple ways

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-10 13:28:03

Assignee: mabshoff


```
  File "/home/was/build/sage-3.2.2.alpha0/local/bin/sage-update", line 178, in do_update
    if 'Placeholder spkg file' in open(F).readline():
IOError: [Errno 21] Is a directory
Error getting new packages!
was`@`sage:~/build/sage-3.2.2.alpha0$ 
```


Also, later it would try to move the directory out of the way, which will fail.


---

Attachment


---

Comment by mabshoff created at 2008-12-11 11:14:17

Looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-11 11:15:16

Resolution: fixed


---

Comment by mabshoff created at 2008-12-11 11:15:16

Merged in Sage 3.2.2.alpha2
