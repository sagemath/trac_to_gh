# Issue 3237: update ecm to 6.2

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-05-17 09:51:38

Assignee: mabshoff

CC:  zimmerma

Paul Zimmermann writes:

```
Release notes:
* New stage 2 for P-1 and P+1, described in Montgomery and Kruppa,
  Improved Stage 2 to P+-1 Factoring Algorithms,
  in A. J. van der Poorten and A. Stein (Eds.), ANTS-VIII 2008,
  LNCS 5011, pp. 180-195.
* Parallelization in the new P+-1 stage 2 (with --enable-openmp).
* Optimizations to the NTT code by Jason S. Papadopoulos
* Improved mulredc assembly code for Athlon64/Opteron
* Improved modular reduction in the mpzmod range
* Bugfix in P+1 stage 2 which caused incorrect initialisation if
  Brent-Suyama polynomial had degree > 1 and i0 was negative (occurs
  only with non-standard parameters)
* Bugfix in generation of Lucas chains for P+1 and ECM, causing some
  stage 1 primes close to 2^32 to be processed incorrectly on 32 bit
  systems
* Added build project for VC++ by Brian Gladman
* File ecm.h changed from GPL to LGPL: the fact it was under GPL was an
  unvoluntary mistake, which has the consequence that applications
  linking with libecm for version < 6.2 should be under GPL too.
* Fixed a regression introduced in 6.1.1: the default arithmetic (NTT)
  for stage 2 was slower for large inputs. Now defaults to -no-ntt for
  input numbers >30 machine words.
```



---

Comment by mabshoff created at 2008-05-31 22:37:58

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-05-31 22:37:58

A new patch release 6.2.1 out. To quote:

```
we consider a patch release (6.2.1) to fix a few issues in 6.2:

* the default B2 bound is way too small for the new P-1/P+1 algorithms
* on some architectures, ecm-6.2 fails to compile due to undefined
  udiv_qrnnd_preinv(). We will define LONGLONG_STANDALONE before including
  longlong.h (this might slow down some architectures like HPPA, but we didn't
  figure out a simple patch for now)
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-11-27 00:24:26

Man, this ticket has gone stale, so I will hopefully fix it soon.

Anyway: Paul, I have been seeing the following on occasion in Sage 3.x for a while:

```
sage -t -long devel/sage/sage/interfaces/ecm.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha2/devel/sage-main/sage/interfaces/ecm.py", line 317:
    sage: ecm.factor((2^197 + 1)/3)           # takes a long time
Expected:
    [197002597249, 1348959352853811313, 251951573867253012259144010843]
Got:
    [251951573867253012259144010843, 265748496095531068869578877937]
**********************************************************************
```

What happens in that case was that ecm did not finish quickly, but spend a long, long time burning 100% CPU until I killed it via top for example. Then the above output was printed. Is this something I should be concerned about? Will the 6.2.1 release fix this? The problem happens on occasion, i.e. maybe a percent of the tries, but I have no exact numbers.

Cheers,

Michael


---

Comment by zimmerma created at 2008-11-27 08:03:18

What happens is that find factors is given as input the prime factor 251...843 (I don't know why).
Of course ECM takes a long time to factor it! It seems some primality test is missing (or wrong):

```
enter find_factor, n= 6695575184412459481424842051421510843842512474094970147089
1 B1= 2000
[265748496095531068869578877937, 251951573867253012259144010843]
enter find_factor, n= 251951573867253012259144010843 B1= 2399
```



---

Attachment

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.3/alpha0/ecm-6.2.1.spkg

updates to lates upstream. The growth of the spkg is caused by upstream and there is no obvious far to cut. The patch attached to this ticket makes the ecm extension depend on ecm.h, so the next -b will automatically rebuild the ecm extension after the upgrade.

Cheers,

Michael


---

Comment by rlm created at 2008-12-23 23:38:28

Builds and passes tests for me.

+1


---

Comment by mabshoff created at 2008-12-23 23:44:07

Merged in Sage 3.2.3.alpha0


---

Comment by mabshoff created at 2008-12-23 23:44:07

Resolution: fixed
