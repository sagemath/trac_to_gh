# Issue 9131: sage-4.4.3.alpha2: OS X 10.4 PPC -- readline fails to build

Issue created by migration from https://trac.sagemath.org/ticket/9131

Original creator: was

Original creation time: 2010-06-03 15:24:27

Assignee: GeorgSWeber


```

gcc version 4.0.1 (Apple Computer, Inc. build 5370)
****************************************************
Building a 32-bit version of Readline
Code will be built with debugging information present. Set 'SAGE_DEBUG' to 'no' if you don't want that.
No Fortran compiler has been defined. This is not normally a problem.
Using CC=gcc
Using CXX=g++
Using FC=
Using F77=
Using SAGE_FORTRAN=
Using SAGE_FORTRAN_LIB=
The following environment variables will be exported.
Using CFLAGS= -O2  -g  -Wall 
Using CXXFLAGS= -O2  -g  -Wall
Using FCFLAGS= -O2  -g  -Wall
Using F77FLAGS= -O2  -g  -Wall
Using CPPFLAGS=
Using LDFLAGS=
Using ABI=
configure scripts and/or makefiles might override these later

Deleting old readline headers and libs
./spkg-install: line 204: ./configure: No such file or directory

real    0m0.101s
user    0m0.016s
sys     0m0.062s
sage: An error occurred while installing readline-6.0.p1
```



---

Comment by was created at 2010-06-03 16:17:08

This is caused by:

```

readline-6.0.p1/src/doc/readline.dvi
tar: Skipping to next header
tar: Archive contains obsolescent base-64 headers

bzip2: Data integrity error when decompressing.
        Input file = (stdin), output file = (stdout)

It is possible that the compressed file(s) have become corrupted.
You can use the -tvv option to test integrity of such files.

You can use the `bzip2recover' program to attempt to recover
data from undamaged sections of corrupted files.

tar: Read 3272 bytes from spkg/standard/readline-6.0.p1.spkg
tar: Child returned status 2
tar: Error exit delayed from previous errors
```



---

Comment by was created at 2010-06-03 16:27:24

I tried using "sage -pkg_nc" instead of "sage -pkg", which produces a non-bzip2 compressed tarball spkg.  This completely fixed the above problem.  So there is so some subtle issue with bz2 compression and tar on OS X 10.4.   Crazy.

Here is the non-bzip2'd readline spkg:

   http://sage.math.washington.edu/home/wstein/patches/readline-6.0.p1.spkg

It's 6MB instead of 2MB.  I'm just going to leave this here for the record.    I'm not proposing this be merged into sage.


---

Comment by was created at 2010-06-04 14:25:33

Resolution: invalid


---

Comment by was created at 2010-06-04 14:25:33

This went away when I used a new tarball.   So it's some random corruption...
