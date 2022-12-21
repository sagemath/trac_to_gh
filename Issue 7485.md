# Issue 7485: make fortran a prerequisite on all platforms except OS X.  Remove g95 binaries from Sage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-11-18 07:14:59

Assignee: was




---

Comment by was created at 2010-01-17 11:52:15

Changing status from new to needs_review.


---

Comment by was created at 2010-01-17 11:52:15

Here is the spkg:

   http://wstein.org/home/wstein/patches/fortran-20100117.spkg

Note, after first trying to do something very complicated, involving changing the gfortran OS X binary to really use its quadcore stuff, etc., etc., I realized that could cause endless trouble, so can be put off.  So the point of this spkg is just a very simple and humble goal -- no more g95 binaries when building Sage on linux.  That is it.

Oh, regarding SAGE_FORTRAN_LIB, one shouldn't need to set that unless one's setup is weird, in which case one sets SAGE_FORTAN and SAGE_FORTRAN_LIB anyways.  So in the attached spkg, I only set SAGE_FORTRAN, not SAGE_FORTRAN_LIB.

NOTE: On Linux, this spkg change makes Sage depend on having gfortran installed.  So it would be a good idea to update prereq accordingly, but that should not be part of this ticket.


---

Comment by mvngu created at 2010-01-18 12:10:19

The new Fortran spkg cuts about 7 MB. The Fortran spkg in Sage 4.3.1.rc0 is about 40MB:

```
mvngu`@`mod standard]$ du -hs fortran-20071120.p9.spkg 
40M     fortran-20071120.p9.spkg
```

while the new spkg is about 33 MB:

```
[mvngu`@`mod fortran]$ du -hs fortran-20100117.spkg 
33M	fortran-20100117.spkg
```

That should be good news for mirroring and downloading the source distribution. Just a trivial nit-pick. The file `spkg-install` has changes that are not yet checked in:

```
[mvngu`@`mod fortran-20100117]$ hg st
M spkg-install
```

Since the Linux Fortran binaries have been removed from the Fortran spkg, do you still want to keep the following conditional in the file `spkg-install`? Between lines 75--81:

```
    elif OS == 'linux':
       if arch == 'x86_64':
          print "Installing Linux x86-64 g95 compiler"
          file = 'g95_linux_64.tar.bz2'
       elif arch == 'i686' or arch == 'i586' or arch == 'i486' or arch == 'i386':
          print "Installing Linux i686 g95 compiler"
          file = 'g95_linux_32.tar.bz2'
```



---

Comment by was created at 2010-01-18 13:30:51

> Since the Linux Fortran binaries have been removed from the 
>Fortran spkg, do you still want to keep the following conditional in the file spkg-install? 

I do.  I want to make minimal changes to the spkg so that it works.  I'm not keen on breaking anything, and there is arbitrarily much that can go wrong.

Note that in future we should be able to get rid of the rest of the g95 binaries, shrinking the size of the spkg another 10MB or so.

The new spkg is here:

    http://wstein.org/home/wstein/patches/fortran-20100118.spkg

It just checks in the changes.


---

Comment by mvngu created at 2010-01-19 18:23:33

Looks good. On Linux and Solaris machines (mod.math, rosemary.math, t2.math), only the script `sage_fortran` is installed under `SAGE_LOCAL/bin`. This is in contrast to the previous behaviour, which was to install Linux Fortran binaries regardless of whether the Linux system already had a system-wide Fortran compiler. On OS X machine (bsd.math), `sage_fortran` and OS X specific Fortran binaries are installed under `SAGE_LOCAL/bin` as expected. I tested [fortran-20100118.spkg](http://wstein.org/home/wstein/patches/fortran-20100118.spkg) with Sage 4.3.1.rc1 on mod.math, rosemary.math, and bsd.math. Doctesting resulted in the following known failure as reported on [sage-devel](http://groups.google.com/group/sage-devel/msg/7c9e8c5a006e4f9f):

```
[mvngu`@`boxen sage-4.3.1.rc1]$ ./sage -t -long devel/sage-main/sage/misc/sagedoc.py 
sage -t -long "devel/sage-main/sage/misc/sagedoc.py"        
**********************************************************************
File "/dev/shm/mvngu/sage-4.3.1.rc1/devel/sage-main/sage/misc/sagedoc.py", line 365:
    sage: 'abvar/homology' in _search_src_or_doc('doc', 'homology', 'variety', interact=False)
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_5
***Test Failed*** 1 failures.
For whitespace errors, see the file /dev/shm/mvngu/dot_sage/tmp/.doctest_sagedoc.py
	 [20.8 s]
exit code: 1024
```

The changes in this updated Fortran spkg are minimal. Linux specific Fortran binaries have been removed. The install script `spkg-install` is essentially as it was previously, with the added test that if the current system is Linux, then test to see if that system has a Fortran compiler.


---

Comment by mvngu created at 2010-01-19 18:23:33

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-19 20:27:55

Resolution: fixed


---

Comment by kcrisman created at 2010-01-19 20:57:07

This may also fix some of the R issues we have seen, e.g at #6279.  See #6532 for more details.


---

Comment by mvngu created at 2010-01-20 20:37:45

See #7484 for a follow-up to update README.txt to require Fortran as a pre-requisite under Linux.


---

Comment by drkirkby created at 2010-01-21 13:51:31

See #8024 for an update to 'prereq' to check a Fortran compiler exists on platforms other than OS X.


---

Comment by magawake created at 2010-02-17 13:37:40

Why not include it for Linux? I think having a good fortran compiler is essential for library dependencies such as BLAS
