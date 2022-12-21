# Issue 4867: optional gcc-4.2.1.spkg doesn't build on sage.math

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-24 05:54:21

Assignee: mabshoff


```
sage -i gcc-4.2.1
...
In file included from /usr/include/features.h:354,
                 from /usr/include/stdio.h:28,
                 from ../../gcc-4.2.1/gcc/tsystem.h:90,
                 from ../../gcc-4.2.1/gcc/libgcc2.c:33:
/usr/include/gnu/stubs.h:7:27: error: gnu/stubs-32.h: No such file or directory
In file included from /usr/include/features.h:354,
                 from /usr/include/stdio.h:28,
                 from ../../gcc-4.2.1/gcc/tsystem.h:90,
                 from ../../gcc-4.2.1/gcc/libgcc2.c:33:
```



---

Comment by mabshoff created at 2008-12-24 11:51:43

The issue here is that seemingly the 32 bit userspace bits are missing.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-11 02:20:35

The issue is not that bits are missing, the problem is plainly and simply that on Ubuntu multi lib in *any* upstream gcc is broken because the Ubuntu people chose to rename

```
lib64 -> lib
lib -> lib32
```

One can disable multilib support and get a 64 bit gcc on sage.math that way.

Cheers,

Michael


---

Comment by jdemeyer created at 2013-08-13 15:54:48

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-08-13 15:54:48

Invalid, even just because said package doesn't exist anymore.


---

Comment by jdemeyer created at 2013-08-13 16:00:10

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-08-16 11:11:46

Resolution: invalid
