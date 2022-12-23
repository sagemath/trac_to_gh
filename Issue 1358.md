# Issue 1358: update libtool's la files upon detection of a moved Sage install

Issue created by migration from https://trac.sagemath.org/ticket/1358

Original creator: mabshoff

Original creation time: 2007-12-02 02:01:04

Assignee: mabshoff

The following just happened to me on OSX 10.5.1:

```
Making all in src
g++ -DPACKAGE_NAME=\"libfplll\" -DPACKAGE_TARNAME=\"libfplll\" -DPACKAGE_VERSION=\"2.0.0\" -DPACKAGE_STRING=\"libfplll\ 2.0.0\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE=\"\" -DVERSION=\"\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DSTDC_HEADERS=1 -DHAVE_LIBMPFR=1 -DHAVE_LIBGMP=1  -I. -I.    -I/Users/mabshoff/sage-2.8.14-moved/local/include/  -fPIC -I/Users/mabshoff/sage-2.8.14-moved/local/include/ -L/Users/mabshoff/sage-2.8.14-moved/local/lib -c main.cpp
/bin/sh ../libtool --mode=link g++  -fPIC -I/Users/mabshoff/sage-2.8.14-moved/local/include/ -L/Users/mabshoff/sage-2.8.14-moved/local/lib  -o fplll  main.o  -lgmp -lmpfr
mkdir .libs
libtool: link: warning: library `/Users/mabshoff/sage-2.8.14-moved/local/lib/libgmp.la' was moved.
libtool: link: warning: library `/Users/mabshoff/sage-2.8.14-moved/local/lib/libmpfr.la' was moved.
libtool: link: warning: library `/Users/mabshoff/sage-2.8.14-moved/local/lib/libgmp.la' was moved.
libtool: link: warning: library `/Users/mabshoff/sage-2.8.14-moved/local/lib/libmpfr.la' was moved.
libtool: link: cannot find the library `/Users/mabshoff/sage-2.8.14/local/lib/libgmp.la' or unhandled argument `/Users/mabshoff/sage-2.8.14/local/lib/libgmp.la'
make[3]: *** [fplll] Error 1
make[2]: *** [all-recursive] Error 1
Error building libfplll
```

The fix is to correct the paths in the libtool files.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-03 05:15:23

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-06-03 05:15:23

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-06-03 05:15:23

This is actually an issue that causes a lot of problems when updating an install that has been moved, i.e. installed directly or via some binary.


---

Comment by mabshoff created at 2008-06-03 05:31:27

Changing assignee from mabshoff to wstein.


---

Comment by mabshoff created at 2008-06-03 05:31:27

This was fixed by William Stein a while back.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-03 05:31:27

Changing status from assigned to new.


---

Comment by mabshoff created at 2008-06-03 05:31:44

Fixed prior to Sage 3.0.3.alpha1


---

Comment by mabshoff created at 2008-06-03 05:31:44

Resolution: fixed
