# Issue 5034: stupid output of sage -br:  "using n cpus"

Issue created by migration from https://trac.sagemath.org/ticket/5034

Original creator: was

Original creation time: 2009-01-20 06:13:23

Assignee: mabshoff

I just noticed that when we do "sage -br" with "export MAKE='make -j3'" on a 2-core machine we get:


```
steragon-2:sage-3.3.alpha0 wstein$ sage -br
...
Execute 4 commands (using 3 cpus)
```


Note the "3 cpus", which looks really dumb, since I have only 1 cpu in my laptop, and it has 2 cores.  To fix this bug change "cpus" to "threads".  That's it!


---

Comment by was created at 2009-01-20 06:39:02

this is against sage-3.3.alpha0


---

Attachment

The attached patch is just a textual substitution of "threads" for "cpus".


---

Comment by cwitty created at 2009-01-20 23:02:28

Of course, "threads" is also technically incorrect; "processes" would be more accurate.


---

Comment by mabshoff created at 2009-01-23 09:07:19

Merged in Sage 3.3.alpha1


---

Comment by mabshoff created at 2009-01-23 09:07:19

Resolution: fixed
