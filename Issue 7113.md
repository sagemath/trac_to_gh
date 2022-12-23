# Issue 7113: Maxima does not build on SUSE Itanium  (Iras)

Issue created by migration from https://trac.sagemath.org/ticket/7113

Original creator: was

Original creation time: 2009-10-04 17:32:53

Assignee: tbd

The build of Sage fails when trying to build Maxima on Iras. 

```

;;; Emitting code for FLOAT.
;;; Emitting code for DO-MERGE-SYMM.
;;; Emitting code for DO-MERGE-ASYM.
;;; Internal error: #<a floating-point-overflow>
;      - Loading binary file "binary-ecl/clmacs.fas" An error occurred during initialization:
Filesystem error with pathname #P"/home/wstein/screen/iras/build/sage-4.1.2.rc1.alpha1/spkg/build/maxima-5.19.1.p0/src/src/binary-ecl/clmacs.fas".
Either
 1) the file does not exist, or
 2) we are not allow to access the file, or
 3) the pathname points to a broken symbolic link..
make[3]: *** [binary-ecl/maxima] Error 1
make[3]: Leaving directory `/home/wstein/screen/iras/build/sage-4.1.2.rc1.alpha1/spkg/build/maxima-5.19.1.p0/src/src'
make[2]: *** [all-recursive] Error 1
make[2]: Leaving directory `/home/wstein/screen/iras/build/sage-4.1.2.rc1.alpha1/spkg/build/maxima-5.19.1.p0/src'
***********************************************************
Failed to make Maxima.
***********************************************************

real    0m30.404s
user    0m9.684s
sys     0m1.984s
sage: An error occurred while installing maxima-5.19.1.p0





```



---

Comment by was created at 2009-10-24 05:47:20

This same exact problem also happens on RHEL 5 (cleo).


---

Comment by was created at 2009-10-24 05:47:20

Changing component from doctest to build.


---

Comment by was created at 2009-10-25 15:20:22

Juan Jose Garcia (author of ECL) has maybe found the bug, which is in ECL:

```
I have found that the GNU C library routines for controlling the
signalling of floating point exceptions, which are not really C
standard but GNU extensions, do not work in the itanium. Well, they
work in the sense that they can suppress the signalling but when
activating it, saving and restoring exceptions, etc, they break.

The solution is taking src/h/config.h
and surrounding the line that contains #undef HAVE_FEENABLEEXCEPT
with something like
#ifndef __ia64__
#endif

I must say I tested this with ECL 9.10.2 but I think the fix should
also work in the versions that Sage is using.

BTW, I do not have access to  my development machine so this fix has
not yet been committed.

Juanjo
```



---

Comment by mhansen created at 2009-11-06 07:21:43

Resolution: fixed


---

Comment by mhansen created at 2009-11-06 07:21:43

Fixed by #7993
