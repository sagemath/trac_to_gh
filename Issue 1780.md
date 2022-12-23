# Issue 1780: [with spkg] add 64 bit MacIntel build support to mpfr, fix stack smashing issue

Issue created by migration from https://trac.sagemath.org/ticket/1780

Original creator: mabshoff

Original creation time: 2008-01-15 01:48:59

Assignee: mabshoff

While mpfr 2.3.1 should be out shortly I integrated a patch from http://websympa.loria.fr/wwsympa/arc/mpfr/2008-01/msg00044.html

What happens is that mpfr uses alloca() instead of the default gmp allocator. alloca() uses the stack and on most modern systems causes segfaults by smashing the stack. One example is the following Sage code (by Paul Zimmermann):


```
sage: R=RealField(16777216)
sage: t=[]
sage: for n in range(1500):
   t.append(R(n)) 
```


The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha3/mpfr-2.3.0.p1.spkg

fixes this issue and also adds build support for 64 bit MacIntel builds.

Cheers,

Michael




---

Comment by mabshoff created at 2008-01-15 01:51:22

Build work on Linux and OSX, including running MPFR's test suite.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-15 01:51:22

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-01-15 02:40:16

Merged in Sage 2.10.alph3


---

Comment by mabshoff created at 2008-01-15 02:40:16

Resolution: fixed
