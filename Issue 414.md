# Issue 414: Attaching .pyx doesn't work anymore (only .spyx)

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-08-09 13:36:35

Assignee: was

Apparently, the list of allowed file formats to attach got shorter recently:


```
<type 'exceptions.ImportError'>: Attaching of '/home/malb/foobar.pyx'
not implemented (load .py, .spyx, and .sage files)
```


but `attach 'foobar.spyx'` works.


---

Comment by was created at 2007-08-31 21:52:29

I never remember allowing attaching of .pyx.  ????


---

Comment by was created at 2007-09-14 02:57:43

Resolution: wontfix


---

Comment by malb created at 2007-09-14 09:14:06

Resolution changed from wontfix to 


---

Comment by malb created at 2007-09-14 09:14:06

Why is this wontfix? AFAIK there is no preparsing involved in the spyx anyway. Is reopening the right way of dealing with this question? Let's try.


---

Comment by malb created at 2007-09-14 09:14:06

Changing status from closed to reopened.


---

Comment by was created at 2007-09-14 22:07:40

Resolution: fixed


---

Attachment

Fixed for sage-2.8.4.3.  Now both .spyx and .pyx files are accepted.
