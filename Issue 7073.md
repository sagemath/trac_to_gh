# Issue 7073: scipy_sandbox 20071020.p4 has a GNUism, sending GNU flags to the Sun compiler.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-09-29 13:44:33

Assignee: tbd

Keywords: GNUism fortran

Using

    * Solaris 10 update 7 on SPARC
    * sage-4.1.2.alpha4
    * Sun Studio 12.1
    * An updated configure script to allow the Sun compiler to be used #7021 


```
scipy_sandbox-20071020.p4/patches/setup.py.arpack
scipy_sandbox-20071020.p4/patches/setup.py~
scipy_sandbox-20071020.p4/patches/setup.py.spline
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v
usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
f95: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
f95: Warning: Option --version passed to ld, if ld is invoked, ignored otherwise
Usage: f95 [ options ] files.  Use 'f95 -flags' for details
```




---

Comment by jdemeyer created at 2015-09-08 12:49:30

scipy_sandbox is no longer a package.


---

Comment by jdemeyer created at 2015-09-08 12:49:30

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2015-09-08 12:49:34

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-09-12 13:59:42

Resolution: fixed


---

Comment by drkirkby created at 2015-09-12 15:19:40

Maybe I am being pedantic, but should this not be wontfix?


---

Comment by jdemeyer created at 2015-09-12 22:33:37

More likely invalid, but it doesn't really matter.
