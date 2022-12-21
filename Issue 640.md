# Issue 640: get rid of the circular link that is created when installing the python spkg

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-11 20:25:30

Assignee: was


```
was`@`ubuntu:~/s/local/lib/python$ ls -l|grep python
lrwxrwxrwx  1 was was      6 2007-09-03 20:06 python -> python
lrwxrwxrwx  1 was was      9 2007-09-03 20:06 python2.5 -> python2.5
```



---

Comment by mabshoff created at 2007-09-13 12:38:22

A fixed spkg can be found at:

http://fsmath.mathematik.uni-dortmund.de/~mabshoff/sage/python-2.5.1.p7.spkg

Cheers,

Michael


---

Comment by was created at 2007-09-13 14:03:20

Resolution: fixed
