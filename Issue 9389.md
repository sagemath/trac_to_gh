# Issue 9389: sage crashing when computing local_data() for an EC

Issue created by migration from https://trac.sagemath.org/ticket/9389

Original creator: arminstraub

Original creation time: 2010-06-30 03:26:30

Assignee: AlexGhitza

CC:  was cturner ylchapuy

Keywords: segfault crash local_data

In 4.4.4 the following crashes Sage:


```
sage: K.<b3> = NumberField(x^6 + 15*x^4 + 2*x^3 + 156*x^2 - 48*x + 701)
sage: E = EllipticCurve(K, [0, 1116/38413*b3^5+54/38413*b3^4+20460/38413*b3^3+3222/38413*b3^2+88752/38413*b3-34404/38413, 0, 54/38413*b3^5+3720/38413*b3^4+990/38413*b3^3+29895/38413*b3^2+19164/38413*b3+485313/38413, 0])
sage: E.local_data()
```


Boom!


---

Comment by arminstraub created at 2010-06-30 03:28:46

Changing assignee from AlexGhitza to cremona.


---

Comment by arminstraub created at 2010-06-30 03:28:46

Changing component from algebra to elliptic curves.


---

Comment by cremona created at 2010-06-30 11:28:06

Can you see if it still crashes after applying the patch at #9266?


---

Comment by arminstraub created at 2010-06-30 15:09:46

> Can you see if it still crashes after applying the patch at #9266?

It still crashes on my machine after applying the patch.


---

Comment by wuthrich created at 2010-07-02 17:08:58

More precisely, the verbose for the second example gives :


```
verbose 1 (568: ell_local_data.py, _tate) Running Tate's algorithm with P = Fractional ideal (3, 1/24*a^3 - 1/4*a^2 - 7/12*a + 3)                                         
[...]
verbose 1 (568: ell_local_data.py, _tate) P is not principal, uniformizer pi = 1/24*a^3 - 1/4*a^2 - 7/12*a + 3 (time = 0.174974)
verbose 1 (627: ell_local_data.py, <lambda>) mod-p multiply of 1 x 2 matrix by 2 x 2 matrix modulo 3
verbose 1 (628: ell_local_data.py, <lambda>) mod-p multiply of 1 x 2 matrix by 2 x 2 matrix modulo 3
verbose 1 (629: ell_local_data.py, <lambda>) mod-p multiply of 1 x 2 matrix by 2 x 2 matrix modulo 3
verbose 1 (629: ell_local_data.py, <lambda>) mod-p multiply of 1 x 2 matrix by 2 x 2 matrix modulo 3
verbose 2 (568: ell_local_data.py, _tate) After first transform [1/2*a^3 + 1/2*a^2 + 1, 0, 1/2*a^3 + 1/2*a^2 + 1]
, [a1,a2,a3,a4,a6] = [0, 3/2*a^3 + 3/2*a^2 + 3, a^3 + a^2 + 3, 51*a^3 + 552*a^2 - 486*a - 8019, 1797*a^3 + 4964*a^2 - 32562*a - 91701]
, valuations = [+Infinity, 1, 1, 5, 2] (time = 2.197665)
verbose 2 (568: ell_local_data.py, _tate) After second transform [0, 0, a^3 + a^2 + 3]
[a1, a2, a3, a4, a6] = [0, 3/2*a^3 + 3/2*a^2 + 3, 3*a^3 + 3*a^2 + 9, 51*a^3 + 552*a^2 - 486*a - 8019, 1657*a^3 + 3488*a^2 - 31266*a - 70335]
Valuations: [+Infinity, 1, 2, 5, 3] (time = 2.211662)
verbose 1 (629: ell_local_data.py, <lambda>) mod-p multiply of 1 x 2 matrix by 2 x 2 matrix modulo 3
verbose 1 (629: ell_local_data.py, <lambda>) mod-p multiply of 1 x 2 matrix by 2 x 2 matrix modulo 3
verbose 1 (629: ell_local_data.py, <lambda>) mod-p multiply of 1 x 2 matrix by 2 x 2 matrix modulo 3
verbose 1 (568: ell_local_data.py, _tate) Analyzing roots of cubic T^3 + 7/18*a^3 + 3/4*a^2 + 1/18*a + 1/2*T^2 + 0*T + 23/36*a^3 + a^2 + 1/18*a + 1, case 1 (time = 2.285651)
verbose 1 (568: ell_local_data.py, _tate) Distinct roots (time = 2.285651)
/usr/local/sage/local/bin/sage-sage: line 206:  6216 Aborted                 sage-ipython "$@" -i
```



---

Comment by davidloeffler created at 2010-07-02 22:24:11

I checked and this actually doesn't have anything to do with elliptic curves; it's exposing a bug in residue fields of number field ideals. Some playing around with the Sage debugger reveals that the second example fails when trying to do the following:

```
sage: K.<a> = NumberField(x^4-32*x^2+324)                                                
sage: I = K.ideal(3, 1/24*a^3 - 1/4*a^2 - 7/12*a + 3)
sage: R = PolynomialRing(I.residue_field(), 'x')
sage: R([23/36*a^3 + a^2 + 1/18*a + 1, 0, 7/18*a^3 + 3/4*a^2 + 1/18*a + 1/2, 1]) # boom!
/storage/masiao/sage-4.5.alpha1/local/bin/sage-sage: line 206: 14086 Aborted                 sage-ipython "$@" -i
```



---

Comment by davidloeffler created at 2010-07-02 22:24:11

Changing assignee from cremona to davidloeffler.


---

Comment by davidloeffler created at 2010-07-02 22:24:11

Changing component from elliptic curves to number fields.


---

Comment by jgaski created at 2010-10-27 08:26:11

Is someone working on this? Here is a trivial example in 4.5.3:


```
sage: K.<a> = QuadraticField(5)
sage: E = EllipticCurve(K,[1,2*a])
sage: E.local_data(K.ideal(2))
```


Boom. Similarly:


```
sage: K.<a> = QuadraticField(5)
sage: R = PolynomialRing(K.ring_of_integers().residue_field(K.ideal(2)), 'x')
sage: R([1/2*a])
```



---

Comment by cremona created at 2010-10-27 16:04:38

I thought this had been fixed by #9315 which was merged in 4.6.alpha1, but it is not:

```
sage: version()
'Sage Version 4.6.rc0, Release Date: 2010-10-21'
sage: K.<a> = QuadraticField(5)
sage: R = PolynomialRing(K.ring_of_integers().residue_field(K.ideal(2)), 'x')
sage: R
Univariate Polynomial Ring in x over Residue field in abar of Fractional ideal (2)
sage: R([1/2*a])
/home/jec/sage-current/local/bin/sage-sage: line 217: 15900 Aborted                 sage-ipython "$@" -i
```

Now of course a/2 cannot be pushed into the residue field, as this (perfectly correct) behaviour shows:

```
sage: R(a/2)    
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
...
ZeroDivisionError: Cannot reduce field element 1/2*a modulo Fractional ideal (2): it has negative valuation
```


 I tried tracing this through and the crash happens here:

```
> /home/jec/sage-current/local/lib/python2.6/site-packages/sage/misc/classcall_metaclass.py(258)__call__()
    257         elif hasattr(cls, "__classcall__"):
--> 258             return cls.__classcall__(cls, *args, **options)
```

after doing lots of stuff which seemed to have little to do with constructing a polynomial (element of R) out of a list of coefficients.

I am CC'ing ylchapuy since I think the code where problems start is in polynomial_zz_pex.pyx which he wrote and which was put into 4.5.3 with #7841 (of which I was one reviewer...)


---

Comment by cremona created at 2010-10-27 16:04:38

Changing keywords from "segfault crash local_data" to "segfault polynomial finite field".


---

Comment by was created at 2010-10-27 22:44:52

NOTE:

John, you are *definitely* right that the problem in polynomial coercion is caused by #7841, since by simply switching to not using NTL polynomials the proper behavior is restored:

```
sage: K.<a> = QuadraticField(5)
sage: R = PolynomialRing(K.ideal(2).residue_field(), 'x', implementation='generic')
sage: R([1/2*a])
...
TypeError
```


If ylchapuy doesn't fix this soon, we could revert his PolynomialRing implementation for the next Sage release, if necessary....
But probably the fix isn't too hard (for him -- it might be very hard for me).


---

Comment by was created at 2010-10-27 22:53:00

In fact, after disabling the buggy ylchapuy code as follows, the original elliptic curve example works.

1. The patch:

```

diff -r b5dab6864f35 sage/rings/polynomial/polynomial_ring.py
--- a/sage/rings/polynomial/polynomial_ring.py  Sat Sep 04 21:40:16 2010 -0700
+++ b/sage/rings/polynomial/polynomial_ring.py  Wed Oct 27 15:50:43 2010 -0700
@@ -1222,7 +1222,8 @@
         """
         if implementation is None: implementation="NTL"
         from sage.rings.finite_rings.finite_field_base import is_FiniteField
-        if implementation == "NTL" and is_FiniteField(base_ring):
+        # this is buggy as a florida swamp -- see trac 9389
+        if False and (implementation == "NTL" and is_FiniteField(base_ring)):
             p=base_ring.characteristic()
             from sage.libs.ntl.ntl_ZZ_pEContext import ntl_ZZ_pEContext
             from sage.libs.ntl.ntl_ZZ_pX import ntl_ZZ_pX
```


2. The result with this patch:

```
sage: K.<a> = QuadraticField(5)
sage: E = EllipticCurve(K,[1,2*a])
sage: E.local_data(K.ideal(2))
Local data at Fractional ideal (2):
Reduction type: bad additive
Local minimal model: Elliptic Curve defined by y^2 = x^3 + x + 2*a over Number Field in a with defining polynomial x^2 - 5
Minimal discriminant valuation: 9
Conductor exponent: 5
Kodaira Symbol: I0*
Tamagawa Number: 1
sage: E.conductor()
Fractional ideal (544)
sage: E.tamagawa_numbers()
[1, 1]
```



---

Comment by cremona created at 2010-10-28 08:38:56

Good work!  Let's hope ylchapuy provides a fix;  otherwise this can be used as a workaround.


---

Comment by ylchapuy created at 2010-10-28 13:12:14

polynomial_zz_pex should not be used here.


```
is_FiniteField(base_ring):
```


might be the wrong test because

```
sage: K.ideal(2).residue_field().is_finite()
yes
```


We should change the line 

```
if implementation == "NTL" and is_FiniteField(base_ring):
```

to something appropriate, it should only be used for `PolynomialRing(GF(q))` I guess

Yann


---

Comment by ylchapuy created at 2010-10-28 13:28:31

In fact those tests should probably go in `polynomial_ring_constructor.py`, in the _single_variate function. The init function for PolynomialRing_Field would then be the generic case.


---

Comment by ylchapuy created at 2010-10-28 13:54:35

as a simple workaround, this solves the problem:

```
diff -r 1b5dc2667b48 sage/rings/polynomial/polynomial_ring.py
--- a/sage/rings/polynomial/polynomial_ring.py  Sat Oct 23 15:07:20 2010 +0200
+++ b/sage/rings/polynomial/polynomial_ring.py  Thu Oct 28 15:53:58 2010 +0200
@@ -1222,7 +1222,7 @@
         """
         if implementation is None: implementation="NTL"
         from sage.rings.finite_rings.finite_field_base import is_FiniteField
-        if implementation == "NTL" and is_FiniteField(base_ring):
+        if implementation == "NTL" and is_FiniteField(base_ring) and not isinstance(base_ring, sage.rings.residue_field.ResidueField_generic):
             p=base_ring.characteristic()
             from sage.libs.ntl.ntl_ZZ_pEContext import ntl_ZZ_pEContext
             from sage.libs.ntl.ntl_ZZ_pX import ntl_ZZ_pX
```


Though I must admit I don't know which difference between GF(4) and K.ideal(2).residue_field() makes everything go boom here.


---

Comment by jdemeyer created at 2011-10-09 11:11:15

Works for me with sage-4.7.2.alpha3.


---

Comment by jdemeyer created at 2011-10-09 11:11:15

Resolution: worksforme
