# Issue 7024: Flint ignores CC and CXX.

Issue created by migration from https://trac.sagemath.org/ticket/7024

Original creator: drkirkby

Original creation time: 2009-09-27 10:57:28

Assignee: tbd

CC:  jpflori

Flitn 1.3.0.p2 is one of several programs which ignores the settings of CC and CXX and users a gcc and g++ that it finds. 



```

flint-1.3.0.p2/src/profiler.h
flint-1.3.0.p2/src/mpn_extras-test.c
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
Found gcc 4 or later
Turning off loop unrolling on Solaris/Sparc
make[2]: Entering directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/flint-1.3.0.p2/src'
gcc -std=c99 -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include/ -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include  -fPIC  -O2  -DNDEBUG -o zn_mod.o -c zn_poly/src/zn_mod.c
```


This needs fixing to add support for the Sun Studio compilers.


---

Comment by mvngu created at 2009-09-27 11:09:16

See ticket #6919 for an updated FLINT spkg.


---

Comment by drkirkby created at 2009-11-25 03:00:49

Bill Hart reported on 27th September that:

''I've added this to a FLINT todo list and will attend to it in the next release.

Thanks for mentioning it.

Bill.''

I will chase this up, to find out if it is fixed or not.


---

Comment by ohanar created at 2012-02-09 14:37:57

Changing status from new to needs_review.


---

Attachment

for review purposes


---

Comment by leif created at 2012-03-17 01:32:28

`$CC` and `$CXX` have to be quoted.

Note that the issue is (at least partially) fixed upstream in FLINT 1.5.2 IIRC; I already made an spkg with various other changes (including the `Makefile`) a while ago btw. ... (cf. discussion at #9858)


---

Comment by leif created at 2012-03-17 01:32:28

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2013-11-23 10:36:33

Works with the newer FLINT 2.x


---

Comment by jdemeyer created at 2013-11-23 10:36:33

Resolution: worksforme
