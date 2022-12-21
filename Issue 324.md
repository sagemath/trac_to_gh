# Issue 324: NTL builds in 32-bit mode on G5 powerpc

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-03-20 15:57:14

Assignee: was

I'm just building sage on a dual core G5 powerpc and noticed that NTL seems to get built in 32-bit mode, even though it's a 64-bit machine... here's part of the build log:


```
This is NTL version 5.4

GOOD NEWS: compatible machine.
summary of machine characteristics:
bits per long = 32
bits per int = 32
bits per size_t = 32
arith right shift = yes
double precision = 53
NBITS (maximum) = 30
single mul ok = yes
register double precision = 53
double rounding detected = no
```




---

Comment by was created at 2007-03-21 22:40:14

All of SAGE (and pretty much everything else) gets built in 32-bit mode under OSX, since OS X is a 32-bit OS.  When Leopard comes out (OS X 10.5) this is supposed to change.  There was a lot of  discussion of this on the sage-devel list, especially by Jason Martin, who made a heroic but ultimately failed attempt to build SAGE 64-bit on OS X.


---

Comment by was created at 2007-03-21 22:40:14

Resolution: invalid
