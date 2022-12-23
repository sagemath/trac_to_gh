# Issue 958: bug in "make install"

Issue created by migration from https://trac.sagemath.org/ticket/958

Original creator: was

Original creation time: 2007-10-21 12:40:04

Assignee: was

Reported by Paul Zimmerman:

```

- in case one redefines DESTDIR in make install, one gets strange paths:
 $ make install -n DESTDIR=/usr/local/sage-2.8.7
 ...
 cp /usr/local/sage-2.8.7/usr/local/sage/sage /usr/local/sage-2.8.7/usr/bin/
 (I would expect at least 'usr' to disappear.)
```



---

Attachment

2.8.10 will have the above patch.  Then, 

make install DESTDIR=/usr/local/sage-2.8.7

will copy the entire sage directory to $(DESTDIR)/sage, and put a copy of the sage startup script in $(DESTDIR)/bin .


---

Comment by cwitty created at 2007-10-27 18:43:39

Resolution: fixed
