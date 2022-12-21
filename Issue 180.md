# Issue 180: -s option to sage issues

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-12-10 19:59:06

Assignee: was


```
[justin]: Hmmm...it's actually "-s -i".  The 'sage' command seems to care about the order of switches; "-f -i" works, while "-i -f" doesn't.  "-i -s" does not save the results, while '-s -i' does.  Is that intentional?
[11:54am] was389: it's a bug.
```



---

Comment by justin created at 2006-12-11 01:27:43

Hmmm again: 
$ sage -s -i gd-2.0.33.p1
Unknown option: -s
usage: sage [options]
Try 'sage -h' for more information.

Works when used as "sage -f -s -i gd-2.0.33.p1"


---

Comment by justin created at 2006-12-11 01:29:37

And just to continue filling out forms:

sage -i -s gd-2.0.33.p1

works.  Yeesh....


---

Comment by was created at 2007-01-13 02:40:11

Changing type from defect to enhancement.


---

Comment by was created at 2007-01-13 02:40:11

change to enhancement, i.e., sage currently doesn't support complicated command
line switches and doesn't claim to!


---

Comment by mabshoff created at 2008-09-24 02:58:55

This ticket is the same issue as #21, so I am closing this as a dupe and adding a comment to #21 to also check these issues.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-24 02:58:55

Resolution: duplicate
