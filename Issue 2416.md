# Issue 2416: jmol error on FF3

Issue created by migration from Trac.

Original creator: edrex

Original creation time: 2008-03-07 04:39:17

Assignee: mabshoff

Keywords: jmol

jmol doesn't go

Tested on OSX 10.5.1, FF3 Beta 1, Sage 2.10.2


```
plot3d(lambda x,y:x^2+y^2,(0,pi),(0,pi))
```

Popup says:

```
ReferenceError: _jmolInitCheck is not defined
```



---

Comment by mabshoff created at 2008-03-07 04:41:38

Changing assignee from mabshoff to was.


---

Comment by mabshoff created at 2008-03-07 04:41:38

Changing component from Cygwin to graphics.


---

Comment by edrex created at 2008-03-07 04:53:50

Same error on JMOL demo pages, so it's not a Sage issue.


---

Comment by edrex created at 2008-03-07 04:54:55

Working with FF3-Beta3 Linux 32bit Java 1.6.0

Maybe it's a FF3/Mac issue or FF3/Java1.5 issue. Correction: broken with FF3 Beta 3 on OS X


---

Comment by anakha created at 2008-10-23 19:59:31

Tested with FF3/OSX 10.5, java 1.5 and everything works.


---

Comment by mabshoff created at 2008-10-23 20:04:18

Ok, worksforme it is :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-23 20:04:18

Resolution: worksforme
