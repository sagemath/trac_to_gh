# Issue 3204: [with spkg, needs review] update M4RI to version 20080514

Issue created by migration from https://trac.sagemath.org/ticket/3204

Original creator: malb

Original creation time: 2008-05-14 20:35:58

Assignee: malb

Keywords: linear algebra, gf(2), m4ri

A new version of M4RI is available at:

   http://sage.math.washington.edu/home/malb/m4ri/

The matching SPKG is at:

  http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20080514.p0.spkg

This SPKG needs a patch which is attached to this ticket.

The new version has quite a new features:
 * Strassen-Winograd matrix multiplication (though not used by default yet),
 * Native support for Solaris and Windows,
 * SSE2 support,
 * Much improved documentation,
 * Nicer calling conventions.

The SSE2 support could cause trouble but I've successfully built the library on 32 and 64-bit Linux, OSX (Intel and PPC), OpenSolaris 2008.05 and Windows XP.


---

Comment by jason created at 2008-05-14 22:45:40

I'm curious what the speed differences are with SSE2 support now.  Do you have any timings?


---

Comment by malb created at 2008-05-14 23:07:36

Replying to [comment:1 jason]:
> I'm curious what the speed differences are with SSE2 support now.  Do you have any timings?

It is not too overwhelming:
 * It only improves things up t L2 cache size for my code since then the cache miss is more expensive, however a more clever programmer might be able to prefetch around this problem.
 * On AMD CPUs it seems slower (see my mail to [sage-devel])

*64-bit Debian/Linux Core2Duo 2.33Ghz without SSE2*


```
sage: A = random_matrix(GF(2),8*1024,8*1024)
sage: B = random_matrix(GF(2),8*1024,8*1024)
sage: time C = A._multiply_strassen(B,cutoff=1024)
CPU times: user 2.25 s, sys: 0.01 s, total: 2.26 s
Wall time: 2.28

sage: time C = A._multiply_strassen(B,cutoff=2*1024)
CPU times: user 2.11 s, sys: 0.02 s, total: 2.13 s
Wall time: 2.13

sage: time C = A._multiply_strassen(B,cutoff=4*1024)
CPU times: user 4.27 s, sys: 0.01 s, total: 4.28 s
Wall time: 4.31

sage: A = random_matrix(GF(2),16*1024,16*1024)
sage: B = random_matrix(GF(2),16*1024,16*1024)
sage: time C = A._multiply_strassen(B,cutoff=2*1024)
CPU times: user 25.01 s, sys: 0.09 s, total: 25.09 s
Wall time: 25.23
```


*64-bit Debian/Linux Core2Duo 2.33Ghz with SSE2*


```
sage: A = random_matrix(GF(2),8*1024,8*1024)
sage: B = random_matrix(GF(2),8*1024,8*1024)
sage: time C = A._multiply_strassen(B,cutoff=1024)
CPU times: user 2.29 s, sys: 0.01 s, total: 2.30 s
Wall time: 2.32

sage: time C = A._multiply_strassen(B,cutoff=2*1024)
CPU times: user 1.82 s, sys: 0.02 s, total: 1.84 s
Wall time: 1.86

sage: time C = A._multiply_strassen(B,cutoff=4*1024)
CPU times: user 3.73 s, sys: 0.16 s, total: 3.89 s
Wall time: 3.99

sage: A = random_matrix(GF(2),16*1024,16*1024)
sage: B = random_matrix(GF(2),16*1024,16*1024)
sage: time C = A._multiply_strassen(B,cutoff=2*1024)
CPU times: user 22.84 s, sys: 0.08 s, total: 22.93 s
Wall time: 23.06
```


I don't claim to have a close to optimal implementation, though. In fact, this experience taught me that there is much I don't yet understand about writing tight C code.


---

Comment by was created at 2008-05-15 00:42:10

REVIEW:

```
tried your new code up at #3204 under OS X and get this:

sage: A = random_matrix(GF(2),10^4,10^4)
sage: B = random_matrix(GF(2),10^4,10^4)
sage: time C = A._multiply_strassen(B,cutoff=3200)
sage.bin(39971) malloc: *** error for object 0xb95c010: Non-aligned
pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
sage.bin(39971) malloc: *** error for object 0x79c9c10: Non-aligned
pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
sage.bin(39971) malloc: *** error for object 0x7465a00:
non-page-aligned, non-allocated pointer being freed
*** set a breakpoint in malloc_error_break to debug
sage.bin(39971) malloc: *** error for object 0x79ca610: Non-aligned
pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
...
CPU times: user 10.29 s, sys: 0.26 s, total: 10.55 s
Wall time: 16.31

Maybe you're doing something wrong?
```



---

Comment by was created at 2008-05-16 04:24:10

REPORT:

I'm using OS X 10.5.1 with GCC gcc version 4.0.1 (Apple Inc. build 5465) on my os x core 2 duo laptop.   After using your updated spkg (libm4ri-20080514.p0) and latest posted patch
I get even more memory errors!:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: m4ri
sage: A = random_matrix(GF(2),10^4,10^4)
sage: B = random_matrix(GF(2),10^4,10^4)
sage: time C = A._multiply_strassen(B,cutoff=3200)
sage: sage: A = random_matrix(GF(2),10^4,10^4)
sage: sage: B = random_matrix(GF(2),10^4,10^4)
sage: sage: time C = A._multiply_strassen(B,cutoff=3200)
sage.bin(58961) malloc: *** error for object 0xbaba010: Non-aligned pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
sage.bin(58961) malloc: *** error for object 0x78f3610: Non-aligned pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
thousands more
CPU times: user 9.03 s, sys: 0.29 s, total: 9.32 s
Wall time: 13.70
```



---

Comment by malb created at 2008-05-16 08:43:52

Replying to [comment:4 was]:
> REPORT:
> 
> I'm using OS X 10.5.1 with GCC gcc version 4.0.1 (Apple Inc. build 5465) on my os x core 2 duo laptop.   After using your updated spkg (libm4ri-20080514.p0) and latest posted patch
> I get even more memory errors!:

If the above is not a typo then you are still using 200805*14* which was never fixed. The bug is supposed to be fixed in 200805*15*.


---

Comment by was created at 2008-05-16 13:33:05

Using 

http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20080515.p0.spkg

works fine!

 -- William


---

Comment by malb created at 2008-05-16 14:51:23

Upgraded the link to 200805*16* which fixes a bug discovered by the Gentoo QA:


```
 * QA Notice: Package has poor programming practices which may compile
 *            fine but exhibit random runtime failures.
 * src/misc.c:121: warning: implicit declaration of function '_mm_free'
```


and was brought to my attention by Francois Bissey.


---

Comment by mabshoff created at 2008-05-19 05:45:49

this patch has been applied the current m4ri.spkg and should also be applied to this spkg before it is merged


---

Attachment


---

Comment by malb created at 2008-05-21 21:29:14

* `libm4ri-20080521.p0.spkg` has the OSX 64-bit patch applied.


---

Comment by malb created at 2008-05-21 21:30:04

Use `new_m4ri_2.patch` instead of `new_m4ri.patch`.


---

Comment by malb created at 2008-05-28 12:33:15

silly little script to check the results against Magma for a small range of matrices


---

Attachment

The SPKG + patch passes the test in `m4ri_test.py` in addition to the Sage doctests and the M4RI tests.


---

Attachment


---

Comment by malb created at 2008-05-28 16:34:41

The attached patch `new_m4ri_corner_cases.patch` should fix all zero number of rows / zero number of columns problems.


---

Comment by mabshoff created at 2008-05-28 19:06:13

Positive review for new_m4ri.patch and new_m4ri_corner_cases.patch as well as the spkg. The patches looks good, all the issues uncovered regarding degenerated matrices were addressed and doctested in new_m4ri_corner_cases.patch. Positive review! Really nice work malb!

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-28 19:06:30

Resolution: fixed


---

Comment by mabshoff created at 2008-05-28 19:06:30

Merged in Sage 3.0.3.alpha0
