# Issue 162: Integer.exact_log causes segfault

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2006-10-29 21:56:58

Assignee: somebody

This code (which I noticed in `Integer.exact_log`) causes a segfault:


```
sage: x = 3**10000000
sage: bits = 31699256
sage: R = RealField(bits)
sage: y = x._mpfr_(R)
sage: z = y.log()
```


I haven't investigated the underlying cause.


---

Comment by was created at 2006-11-06 07:46:14

It's mpfr (=gmp) running out of memory.   I don't know how or if it is
possible to resolve this -- they might make assumptions in those libraries
that preclude us dealing with the problem.  These things were much worse
with GMP-4.0, by the way...


---

Comment by was created at 2007-01-13 01:06:35

Looking again, it's basically just that GMP doesn't work with ridiculously
large precisions -- it just dies. 

Interesting, MAGMA seg faults on exactly the same sort of computation, and of course MAGMA uses GMP/MPFR behind the scenes:


```
was`@`sage:~$ magma
Magma V2.13-5     Fri Jan 12 2007 17:05:25 on sage     [Seed = 853493552]
Type ? for help.  Type <Ctrl>-D to quit.
> x := 3**10000000;

>> x := 3**10000000;
         ^
User error: bad syntax
> x := 3^10000000; 
> R := RealField(31699256);
> y := R!x;
> time z=Log(y);

>> time z=Log(y);
        ^
User error: Identifier 'z' has not been declared or assigned
> time z:=Log(y);
Segmentation fault
```



---

Comment by was created at 2007-08-16 10:06:26

This is a basic mpfr problem.  Any super-high precision arithmetic breaks with SAGE or Magma:

```
was`@`ubuntu:~$ magma
Magma V2.13-10    Thu Aug 16 2007 02:54:37 on ubuntu   [Seed = 3360329821]
Type ? for help.  Type <Ctrl>-D to quit.
> R := RealField(31699256);
> y := R!3;
> z := y*y;
Segmentation fault
was`@`ubuntu:~$    

Same on 64-bit:

was`@`sage:~$ magma
Magma V2.13-5     Thu Aug 16 2007 02:56:05 on sage     [Seed = 4101418455]
Type ? for help.  Type <Ctrl>-D to quit.
> R := RealField(31699256);
> y := R!3;
> z := y*y;
Segmentation fault
was`@`sage:~$   
```


Proposed solution -- in SAGE, don't allow construction of RealField(n) for
n > 2^23.


---

Attachment

fix


---

Comment by was created at 2007-08-16 10:23:49

Resolution: fixed
