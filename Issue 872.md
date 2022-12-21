# Issue 872: singular fails factorization over a numberfield

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-10-13 03:57:03

Assignee: malb

CC:  singular number fields factorization

See also http://www.singular.uni-kl.de/forum/viewtopic.php?t=1639

But since it was reported by a Sage user it is worth tracking here:

```
mabshoff`@`sage:/tmp/Work-mabshoff/sage-2.8.6/local/bin$ ./valgrind --tool=memcheck --leak-resolution=high ./Singular-3-0-3
==25414== Memcheck, a memory error detector.
==25414== Copyright (C) 2002-2007, and GNU GPL'd, by Julian Seward et al.
==25414== Using LibVEX rev 1788, a library for dynamic binary translation.
==25414== Copyright (C) 2004-2007, and GNU GPL'd, by OpenWorks LLP.
==25414== Using valgrind-3.3.0.SVN, a dynamic binary instrumentation framework.
==25414== Copyright (C) 2000-2007, and GNU GPL'd, by Julian Seward et al.
==25414== For more details, rerun with: -v
==25414==
                     SINGULAR                             /  Development
 A Computer Algebra System for Polynomial Computations   /   version 3-0-3
                                                       0<
     by: G.-M. Greuel, G. Pfister, H. Schoenemann        \   May 2007
FB Mathematik der Universitaet, D-67653 Kaiserslautern    \
> ring r=(0,a),(x),dp;
> minpoly=a^2+1;
> factorize(x^18+1);
start Factorize2(int_flag=0)
end Factorize2(0)
[1]:
   _[1]=1
   _[2]=x6+(-a)*x3-1
   _[3]=x6+(a)*x3-1
   _[4]=x2+(a)*x-1
   _[5]=x2+(-a)*x-1
   _[6]=x+(-a)
   _[7]=x+(a)
[2]:
   1,1,1,1,1,1,1
> factorize(x^20+1);
start Factorize2(int_flag=0)
==25414== Source and destination overlap in memcpy(0x4214460, 0x4215300, 3752)
==25414==    at 0x4A1DA2B: memcpy (mc_replace_strmem.c:402)
==25414==    by 0x66F7A0: rEALLOc (in /tmp/Work-mabshoff/sage-2.8.6/local/bin/Singular-3-0-3)
==25414==    by 0x669788: omReallocSizeFromSystem (in /tmp/Work-mabshoff/sage-2.8.6/local/bin/Singular-3-0-3)
==25414==    by 0x6698A0: omReallocLarge (in /tmp/Work-mabshoff/sage-2.8.6/local/bin/Singular-3-0-3)
==25414==    by 0x5CA5F6: reallocSize (in /tmp/Work-mabshoff/sage-2.8.6/local/bin/Singular-3-0-3)
==25414==    by 0x4F04E30: __gmpz_realloc (in /tmp/Work-mabshoff/sage-2.8.6/local/lib/libgmp.so.3.4.1)
==25414==    by 0x4EF76FE: __gmpz_add (in /tmp/Work-mabshoff/sage-2.8.6/local/lib/libgmp.so.3.4.1)
==25414==    by 0x654485: InternalInteger::addsame(InternalCF*) (in /tmp/Work-mabshoff/sage-2.8.6/local/bin/Singular-3-0-3)
==25414==    by 0x628FD7: CanonicalForm::operator+=(CanonicalForm const&) (in /tmp/Work-mabshoff/sage-2.8.6/local/bin/Singular-3-0-3)
==25414==    by 0x657B95: InternalPoly::mulAddTermList(term*, term*, CanonicalForm const&, int, term*&, bool) (in /tmp/Work-mabshoff/sage-2.8.6/local/bin/Singular-3-0-3)
==25414==    by 0x657F4E: InternalPoly::mulsame(InternalCF*) (in /tmp/Work-mabshoff/sage-2.8.6/local/bin/Singular-3-0-3)
==25414==    by 0x627D44: CanonicalForm::operator*=(CanonicalForm const&) (in /tmp/Work-mabshoff/sage-2.8.6/local/bin/Singular-3-0-3)

error: no more memory
System 9920k:19584k Appl 8315k/1604k Malloc 8234k/1173k Valloc 512k/431k Pages 57/71 Regions 1:1

halt 14
==25414==
==25414== ERROR SUMMARY: 11 errors from 1 contexts (suppressed: 13 from 2)
==25414== malloc/free: in use at exit: 0 bytes in 0 blocks.
==25414== malloc/free: 0 allocs, 0 frees, 0 bytes allocated.
==25414== For counts of detected errors, rerun with: -v
==25414== All heap blocks were freed -- no leaks are possible.
```


Cheers,

Michael


---

Comment by cwitty created at 2007-10-13 13:33:31

BTW: It is now my belief that the memcpy error discovered by Michael is not the cause of the problem.  I rebuilt Singular in "omalloc just wraps the system malloc" mode and that valgrind problem report went away, but the infinite loop (or extreme slowness, at least) remains.


---

Comment by cwitty created at 2007-10-14 16:55:47

I have tracked down the problem.  It is due to coefficient explosion in libfac/charset/csutil.cc:alg_gcd() (which implements the Euclidean gcd algorithm).  There is an attempt to control the coefficient size in the function myfitting(), but it is ineffective for this problem.

myfitting() controls coefficient size by dividing by the leading coefficient (an integer), and then clearing denominators.  I have attached a patch that makes myfitting use a different notion of "leading coefficient", where the algebraic variable is considered to be part of the coefficient domain.

This patch does vastly speed up this particular problem, but I would like somebody who knows more about the internals of Singular to look at it before it gets applied (so I am not yet marking it "with patch").


---

Attachment

a potential patch for libfac/charset/csutil.cc


---

Comment by cwitty created at 2007-10-17 22:59:59

My patch has been accepted into the upstream Singular (as well as the invalid call to memcpy noted by Michael in the first comment to this ticket).  I'm told that this:
ftp://www.mathematik.uni-kl.de/pub/Math/Singular/src/3-0-3/Singular-3-0-3-2.tar.gz
has both changes.


---

Comment by was created at 2007-10-20 18:52:11

Resolution: fixed


---

Comment by was created at 2007-10-20 18:52:11

[11:50am] wstein2: hi: regarding #872.
[11:50am] wstein2: the new spkg definitely fixes the bug reported there with factoring.
[11:51am] wstein2: But I tried factoring in a 2-variable ring and it quickly runs out of steam.  E.g., this fails:
[11:51am] wstein2: > ring r=(0,a),(x,y),dp;
[11:51am] wstein2: > minpoly = a^2+1;
[11:51am] wstein2: > factorize(x^12 + y^12);


---

Comment by was created at 2007-10-20 18:52:40


```
[11:50am] wstein2: hi: regarding #872.
[11:50am] wstein2: the new spkg definitely fixes the bug reported there with factoring.
[11:51am] wstein2: But I tried factoring in a 2-variable ring and it quickly runs out of steam.  E.g., this fails:
[11:51am] wstein2: > ring r=(0,a),(x,y),dp;
[11:51am] wstein2: > minpoly = a^2+1;
[11:51am] wstein2: > factorize(x^12 + y^12);
```



---

Comment by was created at 2007-10-20 18:55:54

Changing status from closed to reopened.


---

Comment by was created at 2007-10-20 18:55:54

Resolution changed from fixed to 


---

Comment by was created at 2007-10-20 18:55:54

Magma is much better:


```
bsd0:~ was$ magma
Magma V2.13-10    Sat Oct 20 2007 11:53:54 on bsd0     [Seed = 3168908577]
Type ? for help.  Type <Ctrl>-D to quit.
K<i> := NumberField(x^2 + 1^H>                            
> 
> R<x> := PolynomialRing(RationalField());
> K<i> := NumberField(x^2 + 1);
> S<y,z> := PolynomialRing(K, 2);
> time Factorization(y^4 - z^4);
[
    <y - z, 1>,
    <y + z, 1>,
    <y - i*z, 1>,
    <y + i*z, 1>
]
Time: 0.030
> time Factorization(y^12 - z^12);
[
    <y - z, 1>,
    <y + z, 1>,
    <y - i*z, 1>,
    <y + i*z, 1>,
    <y^2 - y*z + z^2, 1>,
    <y^2 + y*z + z^2, 1>,
    <y^2 - i*y*z - z^2, 1>,
    <y^2 + i*y*z - z^2, 1>
]
Time: 0.030
> time Factorization(y^20 - z^20);
[
    <y - z, 1>,
    <y + z, 1>,
    <y - i*z, 1>,
    <y + i*z, 1>,
    <y^4 - y^3*z + y^2*z^2 - y*z^3 + z^4, 1>,
    <y^4 + y^3*z + y^2*z^2 + y*z^3 + z^4, 1>,
    <y^4 - i*y^3*z - y^2*z^2 + i*y*z^3 + z^4, 1>,
    <y^4 + i*y^3*z - y^2*z^2 - i*y*z^3 + z^4, 1>
]
Time: 0.050
```



---

Comment by was created at 2007-10-20 19:03:45

Resolution: fixed
