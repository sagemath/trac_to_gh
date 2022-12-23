# Issue 7030: quaddouble-2.2.p9 believe Sun's C++ compiler is broken.

Issue created by migration from https://trac.sagemath.org/ticket/7030

Original creator: drkirkby

Original creation time: 2009-09-27 13:58:25

Assignee: tbd

Using

    * Solaris 10 update 7 on SPARC
    * sage-4.1.2.alpha2
    * Sun Studio 12.1
    * An updated configure script to allow the Sun compiler to be used

CC was set to the Sun C compler, and CXX to the Sun C++ compiler,

The 'quaddouble-2.2.p9' package believes the Sun C++ compiler can't create executables. 


```
configure: error: C++ compiler cannot create executables
See `config.log' for more details.
error configuring quad double
```


But other configure scripts have found the default output is a.out, so I'm pretty sure the Sun compiler can create executables! Maybe the test used is invalid. 





---

Comment by was created at 2009-10-01 15:35:37

Resolution: invalid


---

Comment by was created at 2009-10-01 15:35:37

Quaddouble was supposed to be removed from Sage long ago.   So there is no point in fixing it.
