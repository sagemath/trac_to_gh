# Issue 4114: [with patch, needs review] hang in lisp.py on OS X 10.5

Issue created by migration from https://trac.sagemath.org/ticket/4114

Original creator: mhansen

Original creation time: 2008-09-14 06:45:11

Assignee: was


```
One *major* issue that remains is that the lisp.py doctest hangs forever
on OS X ppc 10.5:

sage -t -long devel/sage/sage/interfaces/lie.py
        [5.5 s]
sage -t -long devel/sage/sage/interfaces/lisp.py

^Z [[10 hours later!]]
[1]+  Stopped                 ./bb
clement-pernets-imac-g5:~ was$
```



---

Attachment

On an OSX 10.4 PPC box this patch fixes the issue:

```
varro:~/sage-3.1.2.rc2 mabshoff$ ./sage -t devel/sage/sage/interfaces/lisp.py
sage -t  devel/sage/sage/interfaces/lisp.py                 
         [19.8 s]
 
----------------------------------------------------------------------
All tests passed!
```

But I am mystified why it did work on OSX Intel boxen. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-14 09:11:21

Merged in Sage 3.1.2.rc3


---

Comment by mabshoff created at 2008-09-14 09:11:21

Resolution: fixed
