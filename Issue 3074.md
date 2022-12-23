# Issue 3074: [with spkg] Cyton 0.9.6.14 released

Issue created by migration from https://trac.sagemath.org/ticket/3074

Original creator: robertwb

Original creation time: 2008-05-01 21:42:01

Assignee: mabshoff

This contains all the changes in the latest spkg, as well as better unicode handling (mostly irrelevant for Sage), optimized append method, and the ability to declare cdef variable as python builtin types (list, dict, etc.) 

Spkg up at http://sage.math.washington.edu/home/robertwb/cython/


---

Comment by mabshoff created at 2008-05-02 15:00:35

Hi Robert,

I am curious about the supposed repo status. In the spkg we have an unclean state:

```
! .hgtags
! Demos/callback/Makefile
! Demos/callback/Makefile.nodistutils
! Demos/callback/README.txt
! Demos/callback/Setup.py
! Demos/callback/cheesefinder.c
! Demos/callback/cheesefinder.h
! Demos/callback/run_cheese.py
! Demos/embed/Makefile
! Demos/embed/Makefile.msc
! Demos/embed/Makefile.msc.static
! Demos/embed/Makefile.unix
! Demos/embed/README
! Demos/embed/embedded.pyx
! Demos/embed/main.c
! Demos/pyprimes.py
! Demos/run_numeric_demo.py
! Demos/run_primes.py
! Demos/run_spam.py
! bin/update_references
! tests/compile/altet1.pyx.BROKEN
! tests/compile/belchenko2.pyx.BROKEN
! tests/compile/burton1.pyx.BROKEN
! tests/compile/getattr3ref.pyx.BROKEN
! tests/compile/hinsen1.pyx.BROKEN
? Cython/Compiler/Lexicon.pickle
? Demos/api.pyx
? Demos/api2.pxd
? Demos/append.pyx
? Demos/builtin_types.pyx
? Demos/public_enums.pyx
? Demos/repr.pyx
? Demos/weakref.pxd
? Demos/weakref.pyx
? Demos/weakref2.pyx
? PKG-INFO
? tests/run/public_enums.pyx
```

So: we can either nuke the .hg repo from the spkg or clean it up. It is your call :).

Provided Sage builds and doctests fine I will merge this spkg even with the slightly dirty repo since going back to a clean upstream is more important than some odd repo state IMHO.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-02 16:16:08

The spkg builds fine, Sage does rebuild and doctests fine. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-02 16:16:23

Resolution: fixed


---

Comment by mabshoff created at 2008-05-02 16:16:23

Merged in Sage 3.0.1.rc0


---

Comment by robertwb created at 2008-05-02 20:47:20

I think this is due to a difference in the MANIFEST file vs. the files tracked by hg. (I did python setup.py sdist and then made the spkg from that). I'll be sure to clean it up before the next release, but it shouldn't affect anything. Thanks for pointing this out.
