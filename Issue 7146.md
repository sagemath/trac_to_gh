# Issue 7146: MAKE and sqlite on Solaris: bomb!

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-10-07 15:33:27

Assignee: tbd

I set MAKE to "make -j10" on solaris x86 (disk.math) and while building sqlite got quite a surprise:

```
wstein`@`disk:~$ ps -u wstein  |grep make|wc -l
    5915
```



---

Comment by jdemeyer created at 2013-05-23 14:03:39

I assume this refers to an old version of SQLite which is no longer relevant.


---

Comment by jdemeyer created at 2013-05-23 14:03:39

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-05-23 14:03:45

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-05-27 11:24:59

Resolution: invalid
