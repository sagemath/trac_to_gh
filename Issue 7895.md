# Issue 7895: Flint says SIZE_MAX is undeclared on Solaris 8

Issue created by migration from https://trac.sagemath.org/ticket/7895

Original creator: drkirkby

Original creation time: 2010-01-11 06:21:37

Assignee: drkirkby

CC:  goodwillhart@googlemail.com dimpase


```
ning.o -c zn_poly/src/tuning.c
zn_poly/src/tuning.c:42: error: 'SIZE_MAX' undeclared here (not in a function)
make[2]: *** [tuning.o] Error 1
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3/spkg/build/flint-1.5.0.p2/src'
Error building flint shared library.

real    0m7.207s
user    0m6.680s
sys     0m0.350s
sage: An error occurred while installing flint-1.5.0.p2
```


It is actually defined in the file


```
/usr/include/limits.h
```


at least on this Solaris 8 installation. 


```
bash-2.03$ uname -a
SunOS solaris8 5.8 Generic_108528-11 sun4u sparc SUNW,Sun-Blade-1000
bash-2.03$ cat /etc/release
                       Solaris 8 10/01 s28s_u6wos_08a SPARC
           Copyright 2001 Sun Microsystems, Inc.  All Rights Reserved.
                           Assembled 12 September 2001
```




---

Comment by mkoeppe created at 2020-07-08 16:51:35

Outdated, should be closed


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Changing status from new to needs_review.


---

Comment by dimpase created at 2020-07-08 19:30:37

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-07-14 16:33:43

Resolution: invalid
