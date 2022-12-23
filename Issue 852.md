# Issue 852: Singular's Factorisation crashes under OSX

Issue created by migration from https://trac.sagemath.org/ticket/852

Original creator: malb

Original creation time: 2007-10-11 21:52:07

Assignee: mabshoff

Since we pass `--with-NTL` to the Singular build scripts and work around/fix the resulting build problems (see #842) Singular crashes when attempting to factor a simple multivariate polynomial.


```
> ring r= 0,(x,y),dp;
> poly f = x + y*y;
> factorize(f);

Program received signal EXC_BAD_ACCESS, Could not access memory.
Reason: KERN_PROTECTION_FAILURE at address: 0x0000001b
0x0021c0e7 in fREe ()
```


The backtrace is:


```
#0  0x0021c0e7 in fREe ()
#1  0x000a95f2 in omFreeSizeToSystem ()
#2  0x0009f815 in operator delete[] ()
#3  0x0055ae48 in NTL::SetSeed ()
#4  0x0055afbb in NTL::ran_bytes ()
#5  0x0055b06c in NTL::RandomBits ()
#6  0x0055b4a0 in NTL::RandomBnd ()
#7  0x0055b69f in NTL::RandomBnd ()
#8  0x00507595 in NTL::NextFFTPrime ()
#9  0x00507796 in NTL::UseFFTPrime ()
#10 0x005b4a88 in NTL::zz_pInfoT::zz_pInfoT ()
#11 0x005b4c55 in NTL::zz_pContext::zz_pContext ()
#12 0x005b4ca8 in NTL::zz_p::FFTInit ()
#13 0x005693f5 in NTL::GCD ()
#14 0x005704c0 in NTL::SquareFreeDecomp ()
#15 0x00579a18 in NTL::factor ()
#16 0x0021adb2 in factorize ()
#17 0x0024df2f in ZFactorizeMulti ()
#18 0x0024f19f in ZFactorizeMultivariate ()
#19 0x0021aadd in factorize ()
#20 0x001358e3 in singclap_factorize ()
#21 0x000122fd in jjFAC_P ()
#22 0x0000cff9 in iiExprArith1 ()
#23 0x0002eca5 in yyparse ()
#24 0x0000292f in main ()
```


However, this backtrace was different before I rebuilt the NTL library. I assume some linkage is wrong but I have no idea how to figure this one out.


---

Comment by malb created at 2007-10-11 22:02:35

The same computation works using libSINGULAR:


```
sage: P.<x,y> = PolynomialRing(QQ)
sage: P
Polynomial Ring in x, y over Rational Field
sage: f = x + y*y
sage: f.factor()
y^2 + x
```



---

Comment by mabshoff created at 2007-10-11 22:09:48

Changing status from new to assigned.


---

Comment by malb created at 2007-10-11 22:11:28

If Singular is built after NTL the backtrace is:

```
#0  0x0021c0e7 in fREe ()
#1  0x000a95f2 in omFreeSizeToSystem ()
#2  0x0009f815 in operator delete[] ()
#3  0x0055ae48 in NTL::SetSeed ()
#4  0x0055afbb in NTL::ran_bytes ()
#5  0x0055b06c in NTL::RandomBits ()
#6  0x0055b4a0 in NTL::RandomBnd ()
#7  0x0055b69f in NTL::RandomBnd ()
#8  0x00507595 in NTL::NextFFTPrime ()
#9  0x00507796 in NTL::UseFFTPrime ()
#10 0x005b4a88 in NTL::zz_pInfoT::zz_pInfoT ()
#11 0x005b4c55 in NTL::zz_pContext::zz_pContext ()
#12 0x005b4ca8 in NTL::zz_p::FFTInit ()
#13 0x005693f5 in NTL::GCD ()
#14 0x005704c0 in NTL::SquareFreeDecomp ()
#15 0x00579a18 in NTL::factor ()
#16 0x0021adb2 in factorize ()
#17 0x0024df2f in ZFactorizeMulti ()
#18 0x0024f19f in ZFactorizeMultivariate ()
#19 0x0021aadd in factorize ()
#20 0x001358e3 in singclap_factorize ()
#21 0x000122fd in jjFAC_P ()
#22 0x0000cff9 in iiExprArith1 ()
#23 0x0002eca5 in yyparse ()
#24 0x0000292f in main ()
```



---

Comment by mabshoff created at 2007-10-11 22:43:21

There are some issues. From sage.math:

```
==24913== Memcheck, a memory error detector.
==24913== Copyright (C) 2002-2007, and GNU GPL'd, by Julian Seward et al.
==24913== Using LibVEX rev 1791, a library for dynamic binary translation.
==24913== Copyright (C) 2004-2007, and GNU GPL'd, by OpenWorks LLP.
==24913== Using valgrind-3.3.0.SVN, a dynamic binary instrumentation framework.
==24913== Copyright (C) 2000-2007, and GNU GPL'd, by Julian Seward et al.
==24913== For more details, rerun with: -v
==24913==
                     SINGULAR                             /  Development
 A Computer Algebra System for Polynomial Computations   /   version 3-0-3
                                                       0<
     by: G.-M. Greuel, G. Pfister, H. Schoenemann        \   May 2007
FB Mathematik der Universitaet, D-67653 Kaiserslautern    \
> ring r= 0,(x,y),dp;
> poly f = x + y*y;
> factorize(f);
==24913== Invalid read of size 8
==24913==    at 0x669740: omFreeLarge (in /tmp/Work-mabshoff/sage-2.8.5.1/local/bin/Singular-3-0-3)
==24913==    by 0x4CBCAC2: NTL::SetSeed(NTL::ZZ const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD22A: NTL::ran_bytes(unsigned char*, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD2F8: NTL::RandomBits_long(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBE517: NTL::RandomBnd(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BCC7: NTL::NextFFTPrime(long&, long&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BED6: NTL::UseFFTPrime(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D15019: NTL::zz_pInfoT::zz_pInfoT(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D150C4: NTL::zz_pContext::zz_pContext(NTL::INIT_FFT_STRUCT const&, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D1511F: NTL::zz_p::FFTInit(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CCB48D: NTL::GCD(NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CCE628: NTL::SquareFreeDecomp(NTL::vec_pair_ZZX_long&, NTL::ZZX const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==  Address 0x5bc00b0 is 8 bytes before a block of size 68 alloc'd
==24913==    at 0x4A1B922: operator new[](unsigned long, std::nothrow_t const&) (vg_replace_malloc.c:291)
==24913==    by 0x4CBBD11: NTL::SetSeed(NTL::ZZ const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD22A: NTL::ran_bytes(unsigned char*, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD2F8: NTL::RandomBits_long(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBE517: NTL::RandomBnd(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BCC7: NTL::NextFFTPrime(long&, long&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BED6: NTL::UseFFTPrime(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D15019: NTL::zz_pInfoT::zz_pInfoT(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D150C4: NTL::zz_pContext::zz_pContext(NTL::INIT_FFT_STRUCT const&, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D1511F: NTL::zz_p::FFTInit(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CCB48D: NTL::GCD(NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CCE628: NTL::SquareFreeDecomp(NTL::vec_pair_ZZX_long&, NTL::ZZX const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==
==24913== Invalid read of size 8
==24913==    at 0x66E39A: fREe (in /tmp/Work-mabshoff/sage-2.8.5.1/local/bin/Singular-3-0-3)
==24913==    by 0x66969A: omFreeSizeToSystem (in /tmp/Work-mabshoff/sage-2.8.5.1/local/bin/Singular-3-0-3)
==24913==    by 0x4CBCAC2: NTL::SetSeed(NTL::ZZ const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD22A: NTL::ran_bytes(unsigned char*, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD2F8: NTL::RandomBits_long(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBE517: NTL::RandomBnd(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BCC7: NTL::NextFFTPrime(long&, long&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BED6: NTL::UseFFTPrime(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D15019: NTL::zz_pInfoT::zz_pInfoT(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D150C4: NTL::zz_pContext::zz_pContext(NTL::INIT_FFT_STRUCT const&, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D1511F: NTL::zz_p::FFTInit(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CCB48D: NTL::GCD(NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==  Address 0x5bc00a8 is 16 bytes before a block of size 68 alloc'd
==24913==    at 0x4A1B922: operator new[](unsigned long, std::nothrow_t const&) (vg_replace_malloc.c:291)
==24913==    by 0x4CBBD11: NTL::SetSeed(NTL::ZZ const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD22A: NTL::ran_bytes(unsigned char*, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD2F8: NTL::RandomBits_long(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBE517: NTL::RandomBnd(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BCC7: NTL::NextFFTPrime(long&, long&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BED6: NTL::UseFFTPrime(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D15019: NTL::zz_pInfoT::zz_pInfoT(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D150C4: NTL::zz_pContext::zz_pContext(NTL::INIT_FFT_STRUCT const&, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D1511F: NTL::zz_p::FFTInit(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CCB48D: NTL::GCD(NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CCE628: NTL::SquareFreeDecomp(NTL::vec_pair_ZZX_long&, NTL::ZZX const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==
==24913== Invalid read of size 8
==24913==    at 0x66E3BF: fREe (in /tmp/Work-mabshoff/sage-2.8.5.1/local/bin/Singular-3-0-3)
==24913==    by 0x66969A: omFreeSizeToSystem (in /tmp/Work-mabshoff/sage-2.8.5.1/local/bin/Singular-3-0-3)
==24913==    by 0x4CBCAC2: NTL::SetSeed(NTL::ZZ const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD22A: NTL::ran_bytes(unsigned char*, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD2F8: NTL::RandomBits_long(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBE517: NTL::RandomBnd(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BCC7: NTL::NextFFTPrime(long&, long&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BED6: NTL::UseFFTPrime(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D15019: NTL::zz_pInfoT::zz_pInfoT(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D150C4: NTL::zz_pContext::zz_pContext(NTL::INIT_FFT_STRUCT const&, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D1511F: NTL::zz_p::FFTInit(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CCB48D: NTL::GCD(NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==  Address 0x5bc00a8 is 16 bytes before a block of size 68 alloc'd
==24913==    at 0x4A1B922: operator new[](unsigned long, std::nothrow_t const&) (vg_replace_malloc.c:291)
==24913==    by 0x4CBBD11: NTL::SetSeed(NTL::ZZ const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD22A: NTL::ran_bytes(unsigned char*, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD2F8: NTL::RandomBits_long(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBE517: NTL::RandomBnd(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BCC7: NTL::NextFFTPrime(long&, long&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BED6: NTL::UseFFTPrime(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D15019: NTL::zz_pInfoT::zz_pInfoT(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D150C4: NTL::zz_pContext::zz_pContext(NTL::INIT_FFT_STRUCT const&, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D1511F: NTL::zz_p::FFTInit(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CCB48D: NTL::GCD(NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CCE628: NTL::SquareFreeDecomp(NTL::vec_pair_ZZX_long&, NTL::ZZX const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==
==24913== Invalid write of size 8
==24913==    at 0x66E3D9: fREe (in /tmp/Work-mabshoff/sage-2.8.5.1/local/bin/Singular-3-0-3)
==24913==    by 0x66969A: omFreeSizeToSystem (in /tmp/Work-mabshoff/sage-2.8.5.1/local/bin/Singular-3-0-3)
==24913==    by 0x4CBCAC2: NTL::SetSeed(NTL::ZZ const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD22A: NTL::ran_bytes(unsigned char*, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD2F8: NTL::RandomBits_long(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBE517: NTL::RandomBnd(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BCC7: NTL::NextFFTPrime(long&, long&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BED6: NTL::UseFFTPrime(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D15019: NTL::zz_pInfoT::zz_pInfoT(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D150C4: NTL::zz_pContext::zz_pContext(NTL::INIT_FFT_STRUCT const&, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D1511F: NTL::zz_p::FFTInit(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CCB48D: NTL::GCD(NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==  Address 0x5bc00a8 is 16 bytes before a block of size 68 alloc'd
==24913==    at 0x4A1B922: operator new[](unsigned long, std::nothrow_t const&) (vg_replace_malloc.c:291)
==24913==    by 0x4CBBD11: NTL::SetSeed(NTL::ZZ const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD22A: NTL::ran_bytes(unsigned char*, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD2F8: NTL::RandomBits_long(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBE517: NTL::RandomBnd(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BCC7: NTL::NextFFTPrime(long&, long&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BED6: NTL::UseFFTPrime(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D15019: NTL::zz_pInfoT::zz_pInfoT(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D150C4: NTL::zz_pContext::zz_pContext(NTL::INIT_FFT_STRUCT const&, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D1511F: NTL::zz_p::FFTInit(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CCB48D: NTL::GCD(NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CCE628: NTL::SquareFreeDecomp(NTL::vec_pair_ZZX_long&, NTL::ZZX const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==
==24913== Invalid read of size 8
==24913==    at 0x66E3DF: fREe (in /tmp/Work-mabshoff/sage-2.8.5.1/local/bin/Singular-3-0-3)
==24913==    by 0x66969A: omFreeSizeToSystem (in /tmp/Work-mabshoff/sage-2.8.5.1/local/bin/Singular-3-0-3)
==24913==    by 0x4CBCAC2: NTL::SetSeed(NTL::ZZ const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD22A: NTL::ran_bytes(unsigned char*, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD2F8: NTL::RandomBits_long(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBE517: NTL::RandomBnd(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BCC7: NTL::NextFFTPrime(long&, long&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BED6: NTL::UseFFTPrime(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D15019: NTL::zz_pInfoT::zz_pInfoT(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D150C4: NTL::zz_pContext::zz_pContext(NTL::INIT_FFT_STRUCT const&, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D1511F: NTL::zz_p::FFTInit(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CCB48D: NTL::GCD(NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==  Address 0x5bc00a0 is not stack'd, malloc'd or (recently) free'd
==24913==
==24913== Conditional jump or move depends on uninitialised value(s)
==24913==    at 0x66E3FA: fREe (in /tmp/Work-mabshoff/sage-2.8.5.1/local/bin/Singular-3-0-3)
==24913==    by 0x66969A: omFreeSizeToSystem (in /tmp/Work-mabshoff/sage-2.8.5.1/local/bin/Singular-3-0-3)
==24913==    by 0x4CBCAC2: NTL::SetSeed(NTL::ZZ const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD22A: NTL::ran_bytes(unsigned char*, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD2F8: NTL::RandomBits_long(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBE517: NTL::RandomBnd(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BCC7: NTL::NextFFTPrime(long&, long&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BED6: NTL::UseFFTPrime(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D15019: NTL::zz_pInfoT::zz_pInfoT(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D150C4: NTL::zz_pContext::zz_pContext(NTL::INIT_FFT_STRUCT const&, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D1511F: NTL::zz_p::FFTInit(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CCB48D: NTL::GCD(NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==
==24913== Use of uninitialised value of size 8
==24913==    at 0x66E403: fREe (in /tmp/Work-mabshoff/sage-2.8.5.1/local/bin/Singular-3-0-3)
==24913==    by 0x66969A: omFreeSizeToSystem (in /tmp/Work-mabshoff/sage-2.8.5.1/local/bin/Singular-3-0-3)
==24913==    by 0x4CBCAC2: NTL::SetSeed(NTL::ZZ const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD22A: NTL::ran_bytes(unsigned char*, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD2F8: NTL::RandomBits_long(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBE517: NTL::RandomBnd(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BCC7: NTL::NextFFTPrime(long&, long&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BED6: NTL::UseFFTPrime(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D15019: NTL::zz_pInfoT::zz_pInfoT(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D150C4: NTL::zz_pContext::zz_pContext(NTL::INIT_FFT_STRUCT const&, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D1511F: NTL::zz_p::FFTInit(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CCB48D: NTL::GCD(NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==
==24913== Invalid write of size 8
==24913==    at 0x66E403: fREe (in /tmp/Work-mabshoff/sage-2.8.5.1/local/bin/Singular-3-0-3)
==24913==    by 0x66969A: omFreeSizeToSystem (in /tmp/Work-mabshoff/sage-2.8.5.1/local/bin/Singular-3-0-3)
==24913==    by 0x4CBCAC2: NTL::SetSeed(NTL::ZZ const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD22A: NTL::ran_bytes(unsigned char*, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBD2F8: NTL::RandomBits_long(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CBE517: NTL::RandomBnd(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BCC7: NTL::NextFFTPrime(long&, long&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4C6BED6: NTL::UseFFTPrime(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D15019: NTL::zz_pInfoT::zz_pInfoT(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D150C4: NTL::zz_pContext::zz_pContext(NTL::INIT_FFT_STRUCT const&, long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4D1511F: NTL::zz_p::FFTInit(long) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==    by 0x4CCB48D: NTL::GCD(NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work-mabshoff/sage-2.8.5.1/local/lib/libntl.so)
==24913==  Address 0x18 is not stack'd, malloc'd or (recently) free'd
Singular : signal 11 (v: 3031/2007101115):
Segment fault/Bus error occurred at 7f4ae0 because of 81 (r:1192141366)
please inform the authors
trying to restart...
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-10-11 22:51:52

And some a potential resolution by cwitty:

```
[00:34] <mabshoff_> cu rpw|sleep 
[00:34] <cwitty> It looks like NTL may be using new(std::nothrow).  I wonder if overriding operator new (like Singular does in kernel/mmalloc.cc) doesn't override new (std::nothrow).
[00:34] <mabshoff_> Ahh, that is interesting.
[00:35] <mabshoff_> Actually, Singular segfaults, but then restarts when running the code.
[00:36] <mabshoff_> (on sage.math)
[00:36] <cwitty> PLUS: I just remembered that Singular normally ships its own NTL (which we delete, and use our own copy instead).  One of the only changes in Singular's NTL vs. upstream is to change NTL to not use std::nothrow.
[00:36] <mabshoff_> Well, that looks like a very nice lead, indeed ;)
[00:37] <mabshoff_> nice catch, cwitty
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-10-12 02:12:44

The suggestion by cwitty turned out to be correct. An updated NTL spkg is forthcoming assuming the "sage -testall" passes.

Cheers,

Michael


---

Comment by mabshoff created at 2007-10-12 02:47:30

Well, with the new NTL spkg I got the following doctest failure:

```
mabshoff@sage:/tmp/Work-mabshoff/sage-2.8.6$ ./sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.py
sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.py**********************************************************************
File "multi_polynomial_ideal.py", line 541:
    sage: I.minimal_associated_primes ()
Expected:
    [Ideal (z^3 + 2, -z^2 + y) of Multivariate Polynomial Ring in x, y, z over Rational Field, Ideal (z^2 + 1, -z^2 + y) of Multivariate Polynomial Ring in x, y, z over Rational Field]
Got:
    [Ideal (z^2 + 1, -z^2 + y) of Multivariate Polynomial Ring in x, y, z over Rational Field, Ideal (z^3 + 2, -z^2 + y) of Multivariate Polynomial Ring in x, y, z over Rational Field]
**********************************************************************
File "multi_polynomial_ideal.py", line 315:
    sage: pd = I.complete_primary_decomposition(); pd
Expected:
    [(Ideal (z^2 + 1, y + 1) of Multivariate Polynomial Ring in x, y, z over Rational Field, Ideal (z^2 + 1, y + 1) of Multivariate Polynomial Ring in x, y, z over Rational Field), (Ideal (z^6 + 4*z^3 + 4, y - z^2) of Multivariate Polynomial Ring in x, y, z over Rational Field, Ideal (z^3 + 2, y - z^2) of Multivariate Polynomial Ring in x, y, z over Rational Field)]
Got:
    [(Ideal (z^6 + 4*z^3 + 4, y - z^2) of Multivariate Polynomial Ring in x, y, z over Rational Field, Ideal (z^3 + 2, y - z^2) of Multivariate Polynomial Ring in x, y, z over Rational Field), (Ideal (z^2 + 1, y + 1) of Multivariate Polynomial Ring in x, y, z over Rational Field, Ideal (z^2 + 1, y + 1) of Multivariate Polynomial Ring in x, y, z over Rational Field)]
**********************************************************************
File "multi_polynomial_ideal.py", line 318:
    sage: I.complete_primary_decomposition(algorithm = 'gtz')
Expected:
    [(Ideal (z^2 + 1, y - z^2) of Multivariate Polynomial Ring in x, y, z over Rational Field, Ideal (z^2 + 1, y - z^2) of Multivariate Polynomial Ring in x, y, z over Rational Field), (Ideal (z^6 + 4*z^3 + 4, y - z^2) of Multivariate Polynomial Ring in x, y, z over Rational Field, Ideal (z^3 + 2, y - z^2) of Multivariate Polynomial Ring in x, y, z over Rational Field)]
Got:
    [(Ideal (z^6 + 4*z^3 + 4, y - z^2) of Multivariate Polynomial Ring in x, y, z over Rational Field, Ideal (z^3 + 2, y - z^2) of Multivariate Polynomial Ring in x, y, z over Rational Field), (Ideal (z^2 + 1, y - z^2) of Multivariate Polynomial Ring in x, y, z over Rational Field, Ideal (z^2 + 1, y - z^2) of Multivariate Polynomial Ring in x, y, z over Rational Field)]
**********************************************************************
File "multi_polynomial_ideal.py", line 346:
    sage: I.primary_decomposition()
Expected:
    [Ideal (z^2 + 1, y + 1) of Multivariate Polynomial Ring in x, y, z over Rational Field, Ideal (z^6 + 4*z^3 + 4, y - z^2) of Multivariate Polynomial Ring in x, y, z over Rational Field]
Got:
    [Ideal (z^6 + 4*z^3 + 4, y - z^2) of Multivariate Polynomial Ring in x, y, z over Rational Field, Ideal (z^2 + 1, y + 1) of Multivariate Polynomial Ring in x, y, z over Rational Field]
**********************************************************************
File "multi_polynomial_ideal.py", line 358:
    sage: I.associated_primes()
Expected:
    [Ideal (y + 1, z^2 + 1) of Multivariate Polynomial Ring in x, y, z over Rational Field, Ideal (z^2 - y, y*z + 2, y^2 + 2*z) of Multivariate Polynomial Ring in x, y, z over Rational Field]
Got:
    [Ideal (z^2 - y, y*z + 2, y^2 + 2*z) of Multivariate Polynomial Ring in x, y, z over Rational Field, Ideal (y + 1, z^2 + 1) of Multivariate Polynomial Ring in x, y, z over Rational Field]
**********************************************************************
```

It seems that the ideals all changed places.

Cheers,

Michael


---

Comment by mabshoff created at 2007-10-12 03:18:44

Updated spkg is at 

http://sage.math.washington.edu/home/mabshoff/ntl-5.4.1.p6.spkg

The doctest failures still need to be sorted out!

Cheers,

Michael


---

Comment by malb created at 2007-10-12 10:37:21

Doctest failure fixing patch is attached to #842.

To apply all patches for this ticket and #842:
 * install the new NTL spkg from http://sage.math.washington.edu/home/mabshoff/ntl-5.4.1.p6.spkg 
 * install the new Singular spkg from http://sage.math.washington.edu/home/malb/pkgs/singular-3-0-3-1-20071010.spkg 
 * apply `6720.patch` attached to #842
 * apply `multi_polynomial_ideal_singular_ntl_fixes.patch` attached to #842


---

Comment by was created at 2007-10-13 02:14:49

Resolution: fixed
