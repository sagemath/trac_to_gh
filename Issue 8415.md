# Issue 8415: bug in complex period lattice

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-03-02 08:59:06

Assignee: was

CC:  cremona


```
E = EllipticCurve('37a')
K.<a> = QuadraticField(-7)
EK = E.change_ring(K)
L = EK.period_lattice(K.complex_embeddings()[0])
[hang, can't control-c]
```


GDB Backtrace: 


```
#0  0x00007f87d128506a in Flx_to_ZX ()
   from /usr/local/sage/local/lib/libpari-gmp.so.2
#1  0x00007f87d13a378f in FpX_split_Berlekamp ()
   from /usr/local/sage/local/lib/libpari-gmp.so.2
#2  0x00007f87d146fbda in nfsqff ()
   from /usr/local/sage/local/lib/libpari-gmp.so.2
#3  0x00007f87d1470383 in nffactor ()
   from /usr/local/sage/local/lib/libpari-gmp.so.2
#4  0x00007f87cc206364 in __pyx_pf_4sage_4libs_4pari_3gen_3gen_nffactor (
    __pyx_v_self=0x4a0bc58, __pyx_v_x=<value optimized out>)
    at sage/libs/pari/gen.c:27077
#5  0x00000000004978b1 in PyEval_EvalFrameEx (f=0x485aea0, 
    throwflag=<value optimized out>) at Python/ceval.c:3694
#6  0x0000000000498e61 in PyEval_EvalCodeEx (co=0x20635d0, 
    globals=<value optimized out>, locals=<value optimized out>, args=0x20, 
    argcount=2, kws=0x48b1c38, kwcount=0, defs=0x0, defcount=0, closure=0x0)
    at Python/ceval.c:2968
#7  0x0000000000496c7e in PyEval_EvalFrameEx (f=0x48b1a60, 
    throwflag=<value optimized out>) at Python/ceval.c:3802
#8  0x0000000000497540 in PyEval_EvalFrameEx (f=0x48b1890, 
    throwflag=<value optimized out>) at Python/ceval.c:3792
#9  0x0000000000497540 in PyEval_EvalFrameEx (f=0x48b1660, 
    throwflag=<value optimized out>) at Python/ceval.c:3792
```



---

Comment by cremona created at 2010-03-02 09:37:17

The fault is when refine_embedding is called;  and in that function (in sage.rings.number_field.number_field) the line which hangs is

```
elist = K.embeddings(sage.rings.qqbar.QQbar)
```


So a minimal hang-causing session is simply

```
sage: K.<a> = QuadraticField(-7)
sage: K.embeddings(QQbar)
```



---

Comment by cremona created at 2010-03-02 09:50:47


```
sage: x=polygen(QQbar)
sage: f=x^2+7
sage: r=f.roots()
sage: r
[(-2.645751311064591?*I, 1), (2.645751311064591?*I, 1)]
sage: r.sort()
```

hangs.  So it's the sorting -- in fact the comparison! -- of two elements of QQbar which is the problem.


---

Comment by robertwb created at 2010-03-02 09:54:27

Ah, I bet it's trying to compare them lexicographically! Wonder why this doesn't happen with other quadratic number fields...


---

Comment by cremona created at 2010-03-02 16:48:38


```
sage: r = QQbar(-7).sqrt()
sage: s = r.conjugate()   
sage: (r-s).exactify()    # hangs
```


It's  in the QQbqr code...    The actual hanging is happening in a call to pari's nffactor on line 1632 of qqbar.py.  So I think it's yet another manifestation of pari's nnffactor bugs:

```
jec`@`selmer%sage -gp
...
                  GP/PARI CALCULATOR Version 2.3.3 (released)
         amd64 running linux (x86-64/GMP-4.2.1 kernel) 64-bit version
           compiled: Feb 22 2010, gcc-4.3.3 (Ubuntu 4.3.3-5ubuntu4) 
               (readline v6.0 enabled, extended help available)
...
? nf = nfinit(y^2-y+2);                                                       
? nffactor(nf,x^2-x+2)                                                        
  *** nffactor: the PARI stack overflows !
  current stack size: 8000000 (7.629 Mbytes)
  [hint] you can increase GP stack with allocatemem()
```

( from inside sage, this just hangs).

According to http://old.nabble.com/New-PARI-stable-release-2.3.5-td27467266.html there are 3 bug-fixes to nffactor in 2.3.5 which is a bug-fix release.  Current development version is 2.4.3, in which the above example works fine.  I have not tried 2.3.5.


---

Comment by cremona created at 2010-03-11 21:10:08

All the problems listed here are solved after the new spkg and patches at #8453.

This ticket can be closed after that one is merged.


---

Comment by davidloeffler created at 2010-03-11 22:55:54

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2010-03-11 22:57:13

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-03-11 22:57:13

I'm marking this as "positive review", to bring it to the attention of the release maintainer who can close it.


---

Comment by was created at 2010-04-29 05:14:25

Resolution: fixed


---

Comment by mvngu created at 2010-04-29 15:37:12

Close as fixed by #8453.
