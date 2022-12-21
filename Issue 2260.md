# Issue 2260: Upgrade ATLAS to 3.8.1

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-02-22 17:03:07

Assignee: m abs


```
ATLAS 3.8.1 has been released.  It fixes all the known bugs in 3.8.0.  There
are also several other improvements, but probably the most important is that
I have finally fixed the Level 1 timing, so that it doesn't die so much with
"unable to get timings within tolerance" when you don't have architectural
defaults.

The ChangeLog entry is below.

Cheers,
Clint
ATLAS 3.8.1 released 02/21/08, Changes from 3.8.0:
   * Fixed bug in slvtst that counted complex flops same as real
   * Fixed bug causing wrong answer for row-major gemm C=A*A' or A'A 
   * Fixed bug in configure causing Pentium-M to be IDed as CoreDuo
   * Fixed bug in tfc.c causing memory overwrite when too many samples taken
   * Improved L1 BLAS timers so they work like the rest of the package, and
     thus don't die all the time on tolerance failures
   * Improved ATLAS/tune/blas/gemm/mmsearch.c:
     - for x86, tried more registers, since smart compiler can reduce A & B
       regs to 2 (and possibly even 1)
     - Made it so search tries both load-C-at-top and load-C-at-bottom of
       M loop.  Bottom is superior for error, and ATLAS originally defaulted
       to load-C-at-top.
   * Added configure support for new K10h platform from AMD, as well as
     basic architectural defaults (no new kernels, just good search)
```



---

Comment by mabshoff created at 2008-02-22 17:03:14

Changing assignee from m abs to mabshoff.


---

Comment by mabshoff created at 2008-02-22 18:40:30

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-02-22 18:40:30

While I am at it I should fix all open ATLAS tickets:

 * #1495
 * #1641
 * #1767
 * #2108

Cheers,

Michael


---

Comment by gfurnish created at 2008-03-20 10:51:39

Power throttling checking was disabled as per irc discussion, and after testing from me, positive review.


---

Comment by mabshoff created at 2008-03-20 10:57:47

The updated spkg is at

http://sage.math.washington.edu/home/mabshoff/SPKG/atlas-3.8.1.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-20 10:58:01

Resolution: fixed


---

Comment by mabshoff created at 2008-03-20 10:58:01

Merged in Sage 2.11.alpha0
