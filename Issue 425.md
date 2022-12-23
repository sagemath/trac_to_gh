# Issue 425: Squash warning cause by using "-Wstrict-prototypes" in cython

Issue created by migration from https://trac.sagemath.org/ticket/425

Original creator: mabshoff

Original creation time: 2007-08-13 01:06:43

Assignee: was

CC:  robertwb

When compiling C code in cython some times "-Wstrict-prototypes" is added, causing the following warning:

 cc1plus: warning: command line option "-Wstrict-prototypes" is valid for C/ObjC but not for C++


---

Comment by malb created at 2007-08-13 10:09:47

IIRC this gcc option is added by `python-cflags`:


```
SAGE_ROOT/local/bin/python2.5-config --cflags
-I/home/malb/SAGE/local/include/python2.5 \ 
-I/home/malb/SAGE/local/include/python2.5 \
-fno-strict-aliasing -DNDEBUG -g -O3 -Wall \
-Wstrict-prototypes
```



---

Comment by mabshoff created at 2008-07-07 12:50:09

I agree with malb here that it is Python which is at fault here. Since this is only a minor annoyance I think we should just invalidate it.

Thoughts?

Cheers,

Michael


---

Comment by malb created at 2008-08-23 23:19:36

Resolution: invalid


---

Comment by malb created at 2008-08-23 23:19:36

I'm all for *invalid*ating.


---

Comment by mabshoff created at 2008-08-23 23:34:51

Agreed. This is a distutils problem anyway.

Cheers,

Michael
