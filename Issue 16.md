# Issue 16: failures building optional packages

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-12 23:17:16

Assignee: somebody

* Building optional packages under OS X Intel (status report on 08-25-06 by William Stein)
   Everything works except the following --
      * dvipng doesn't build (but shouldn't be needed, since this comes with tex)
      * RealLib3 -- fails with "LongFloat.cpp:6:20: error: malloc.h: No such file or directory"
      * numpy-2006-08-16.spkg -- fails with "KeyError: 'linker_exe'"
      * scipy-2006-08-16.spkg -- depends on numpy
      * soya-0.11.2.p0.spkg -- fails to find GL/glew.h  (soya is probably very hard to build in OSX...)



---

Comment by was created at 2007-01-12 21:53:50


```
  * numpy and scipy now fixed
  * soya is not and never will be supported
```



---

Comment by was created at 2007-01-12 21:53:50

Changing type from defect to enhancement.


---

Comment by malb created at 2007-08-09 21:52:26

fixed.


---

Comment by malb created at 2007-08-09 21:52:26

Resolution: fixed
