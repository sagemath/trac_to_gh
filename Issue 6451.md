# Issue 6451: Fint uses a non-portable option to 'cp' which fails on Solaris.

Issue created by migration from https://trac.sagemath.org/ticket/6451

Original creator: drkirkby

Original creation time: 2009-06-30 16:16:14

Assignee: tbd

Keywords: solaris GNUism

I noticed a problem when building 'sage-4.1.alpha2.spkg'. It complains

```
ld: fatal: library -lflint: not found
```


But the flint package indicates it was installed. However, when I tried to build flint again, I see this error message:


```
Deleting old FLINT
Installing new library file
cp: illegal option -- a
Usage: cp [-f] [-i] [-p] [-@] f1 f2
        cp [-f] [-i] [-p] [-@] f1 ... fn d1
        cp -r|-R [-H|-L|-P] [-f] [-i] [-p] [-@] d1 ... dn-1 dn
```


It's clear flint is making use of some GNU-specific option to 'cp' The fact the copy fails means of course the library does not get installed.

I'll post a fix later - it should be trivial 



---

Comment by drkirkby created at 2009-06-30 17:04:30

One of the easier patches - it just needed one byte changed. In spkg-install:




```
  $CP -a libflint* "$SAGE_LOCAL/lib/"
```


was changed to


```
  $CP -p libflint* "$SAGE_LOCAL/lib/"
```



See http://sage.math.washington.edu/home/kirkby/Solaris-fixes/flint/


---

Comment by drkirkby created at 2009-06-30 17:04:30

Changing assignee from tbd to drkirkby.


---

Comment by drkirkby created at 2009-06-30 17:04:30

Changing status from new to assigned.


---

Comment by wbhart created at 2009-07-06 21:41:24

The patch posted here:

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/flint/spkg-install.patch

changes the -a option to cp to -p. I have checked that -a is exactly equivalent to -dpR. Here R is not relevant as only one file is copied and R is for recursive. The -d is not relevant as it is for symbolic links and is again not relevant for copying a single actual file.

The -p option is indeed available on Solaris and T2, so the patch is good. The patch is clearly conservative.

Note this is not an issue with FLINT itself, but with the FLINT spkg installer.


---

Comment by mvngu created at 2009-07-16 18:53:33

The spkg posted by David Kirkby didn't check in all changes. I've checked in the changes in David's name. The updated spkg is up at

http://sage.math.washington.edu/home/mvngu/patch/flint-1.3.0.p2.spkg

Just to let people know, the updated spkg has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(


---

Comment by mvngu created at 2009-07-16 21:12:50

Resolution: fixed
