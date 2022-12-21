# Issue 4364: major bug in singular polynomial GCD (?)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-10-24 18:57:32

Assignee: malb

This looks like maybe a serious bug in Singular's GCD:


```
sage: def f(n):
....:         p = next_prime(n)
....:     a = GF(p)(1)
....:     b = GF(p)(1)
....:     E = EllipticCurve([a, b])
....:     ret = E.multiplication_by_m(2)
....:     return ret
....:
sage: f(next_prime(2^30-41))

Program received signal SIGABRT, Aborted.
[Switching to Thread -1210337072 (LWP 6522)]
0xffffe410 in __kernel_vsyscall ()
(gdb)
(gdb) bt
#0  0xffffe410 in __kernel_vsyscall ()
#1  0xb7de5df0 in raise () from /lib/tls/i686/cmov/libc.so.6
#2  0xb7de7641 in abort () from /lib/tls/i686/cmov/libc.so.6
#3  0xb7b6ff12 in global_NTL_error_callback (s=0xb7a3c8c8
"zz_pContext: modulus too big", context=0x0) at src/stdsage.c:42
#4  0xb79f9ef7 in NTL::Error (s=0xb7a3c8c8 "zz_pContext: modulus too
big") at tools.c:38
#5  0xb79a26db in zz_pInfoT (this=0xa1be668, NewP=1073741827,
maxroot=25) at lzz_p.c:15
#6  0xb79a280e in zz_pContext (this=0xbfa40744, p=1073741827,
maxroot=25) at lzz_p.c:157
#7  0xb47649c5 in gcd_poly_p (f=`@`0xbfa40908, g=`@`0xbfa40904) at cf_gcd.cc:852
#8  0xb47660b8 in gcd_poly (f=`@`0xbfa40b4c, g=`@`0xbfa40b50) at cf_gcd.cc:538
#9  0xb4766ca3 in gcd (f=`@`0xbfa40b4c, g=`@`0xbfa40b50) at cf_gcd.cc:776
#10 0xb45dd1f1 in singclap_gcd (f=0xb445e220, g=0xb445e324) at clapsing.cc:230
#11 0xb4849286 in
__pyx_pf_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular_gcd
(__pyx_v_self=0xb7c80acc, __pyx_args=0xa1d158c, __pyx_kwds=0x0)
   at sage/rings/polynomial/multi_polynomial_libsingular.cpp:23491
```



---

Comment by mabshoff created at 2008-10-24 19:05:46

This is actually an uncaught error in NTL: 

```
zz_pContext: modulus too big
```

This then likely segfaults libSingular.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2009-01-28 15:22:27

Merged in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-28 15:22:27

Resolution: fixed
