# Issue 7038: ratpoints 2.1.2.p2 ignores CC and uses gcc whatever

Issue created by migration from https://trac.sagemath.org/ticket/7038

Original creator: drkirkby

Original creation time: 2009-09-27 15:52:54

Assignee: tbd

I gather ratpoints is causing problems with it wanting a very recent version of gcc, where here is another issue. Even if the variable CC is set to the Sun compiler, ratpoints ignores that and simply uses gcc anyway. 

The build of ratpoints was attempted using 

    * Solaris 10 update 7 on SPARC
    * sage-4.1.2.alpha2
    * Sun Studio 12.1
    * An updated configure script to allow the Sun compiler to be used http://sagetrac.org/sage_trac/ticket/7021 

So it seems there are two at least two issues to resolve in ratpoints. 


```
ratpoints-2.1.2.p2/src/testdata.h
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
make[2]: Entering directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/ratpoints-2.1.2.p2/src'
gcc sift.c -c -o sift.o -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME=7 -DUSE_SSE -funroll-loops
gcc gen_init_sieve_h.c -o gen_init_sieve_h  -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME=7 -DUSE_SSE -L/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/lib -lgmp -lm
./gen_init_sieve_h > init_sieve.h
gcc init.c -c -o init.o -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME=7 -DUSE_SSE -funroll-loops -O3
```



---

Comment by leif created at 2012-03-22 13:31:26

Changing component from build to packages.


---

Comment by leif created at 2012-03-22 13:31:26

This issue is now fixed by #12682 (which provides a ratpoints-2.1.3.p3 spkg).


---

Comment by leif created at 2012-03-22 13:31:26

Changing status from new to needs_review.


---

Comment by leif created at 2012-03-22 13:33:47

Changing status from needs_review to positive_review.


---

Comment by leif created at 2012-03-22 13:33:47

Dear release manager, I leave it up to you to close this now. :-)


---

Comment by jdemeyer created at 2012-04-04 13:23:38

Resolution: duplicate
