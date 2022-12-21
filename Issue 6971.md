# Issue 6971: port ECL spkg to os x 10.6

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-09-20 22:28:14

Assignee: tbd


```
ha1/spkg/build/ecl-9.8.4/src/src/gc/mach_dep.c -o mach_dep.o
In file included from /Users/wstein/sage/build/64bit/sage-4.1.2.alpha1/spkg/build/ecl-9.8.4/src/src/gc/mach_dep.c:163:
/usr/include/ucontext.h:42:2: error: #error ucontext routines are deprecated, and require _XOPEN_SOURCE to be defined
make[5]: *** [mach_dep.lo] Error 1
make[4]: *** [install-recursive] Error 1
make[3]: *** [libeclgc.a] Error 2
make[2]: *** [all] Error 2
Failed to build ECL ... exiting

```



---

Comment by was created at 2009-09-20 22:47:22

spkg up here:

    http://sage.math.washington.edu/home/wstein/patches/ecl-9.8.4-20090913cvs.p1.spkg

It's important that the name be fairly canonical like the above is.


---

Comment by mvngu created at 2009-09-27 02:05:15

See palmieri's and my reports at #6849.


---

Comment by mvngu created at 2009-09-27 02:05:15

Resolution: fixed
