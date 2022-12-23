# Issue 948: very slow factorization over a numberfield in a 2-variable ring [singular related]

Issue created by migration from https://trac.sagemath.org/ticket/948

Original creator: mabshoff

Original creation time: 2007-10-20 19:01:17

Assignee: malb


```
[11:50am] wstein2: hi: regarding #872.
[11:50am] wstein2: the new spkg definitely fixes the bug reported there with factoring.
[11:51am] wstein2: But I tried factoring in a 2-variable ring and it quickly runs out of steam.  E.g., this fails:
[11:51am] wstein2: > ring r=(0,a),(x,y),dp;
[11:51am] wstein2: > minpoly = a^2+1;
[11:51am] wstein2: > factorize(x^12 + y^12);
```

Some magma timings:

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

Comment by malb created at 2007-10-25 15:32:50

Upstream tells me that there is no short time fix for this issue, it requires some rewrite of the factorisation code for number fields. However, for this particular case this can easily be fixed by de-homogenising the polynomial before factoring. Patch to SINGULAR to implement this is attached.

I am retagging this as 2.8.10 which means applying the patch attached to this ticket to the version of Singular we ship. For anything else this ticket is best reassigned to the sage-wishlist milestone.


---

Attachment


---

Comment by malb created at 2007-10-31 12:54:23

The attached patch was applied to http://sage.math.washington.edu/home/malb/pkgs/singular-3-0-3-2-20071031.spkg

Timings:

```
sage: f = (x^4 - y^4)
sage: %time F = f.factor()
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02

sage: f = (x^12 - y^12)
sage: %time F = f.factor()
CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s
Wall time: 0.05

sage: f = (x^20 - y^20)
sage: %time F = f.factor()
CPU times: user 0.03 s, sys: 0.01 s, total: 0.03 s
Wall time: 0.07
```



---

Comment by malb created at 2007-10-31 12:54:23

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-11-01 10:34:19

Resolution: fixed


---

Comment by mabshoff created at 2007-11-01 10:34:19

applied to 2.8.11.alpha0 - please read the comment section.
