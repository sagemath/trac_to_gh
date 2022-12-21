# Issue 5430: Coleman integrals of differential forms from different rings

Issue created by migration from Trac.

Original creator: jen

Original creation time: 2009-03-03 18:10:24

Assignee: robertwb

CC:  robertwb

The coercion seems to be fine, but the Coleman integral fails:

```
sage: R.<x> = QQ['x']
sage: H = HyperellipticCurve(x*(x-1)*(x+9))
sage: K = Qp(7,10)
sage: HK = H.change_ring(K)
sage: import sage.schemes.elliptic_curves.monsky_washnitzer as mw
sage: M_frob, forms = mw.matrix_of_frobenius_hyperelliptic(HK)
sage: w = HK.invariant_differential()
sage: x,y = HK.monsky_washnitzer_gens()
sage: f = forms[0]
sage: S= HK(9,36)
sage: Q = HK.teichmuller(S)
sage: P = HK(-1,4)
sage: b = x*w*w._coeff.parent()(f)            #this is ok
sage: HK.coleman_integral(b,P,Q)              #this is not
```



---

Comment by robertwb created at 2009-03-03 22:02:10

The end of the traceback is 


```
  File "parent.pyx", line 276, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3653)
  File "coerce_maps.pyx", line 76, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:2793)
  File "coerce_maps.pyx", line 71, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2700)
  File "rational.pyx", line 189, in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:4233)
  File "rational.pyx", line 312, in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:5261)
  File "padic_generic_element.pyx", line 748, in sage.rings.padics.padic_generic_element.pAdicGenericElement.rational_reconstruction (sage/rings/padics/padic_generic_element.c:7584)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/rings/arith.py", line 1516, in rational_reconstruction
    return ZZ(a).rational_reconstruction(m)
  File "integer.pyx", line 1981, in sage.rings.integer.Integer.rational_reconstruction (sage/rings/integer.c:13544)
  File "rational.pyx", line 2345, in sage.rings.rational.pyrex_rational_reconstruction (sage/rings/rational.c:15562)
  File "gmp.pxi", line 144, in sage.rings.rational.mpq_rational_reconstruction (sage/rings/rational.c:3032)
ValueError: Rational reconstruction of 253015590 (mod 282475249) does not exist.
```


The question is, should this be an error, or just work? 


```
sage: K = Qp(5, 10)
sage: a = K(1/250037); a
3 + 4*5 + 3*5^2 + 3*5^3 + 5^4 + 5^5 + 5^6 + 5^7 + 4*5^8 + 4*5^9 + O(5^10)
sage: ZZ(a)
9472973
sage: QQ(a)
Traceback (most recent call last):
...
ValueError: Rational reconstruction of 9472973 (mod 9765625) does not exist.
```



---

Comment by mabshoff created at 2009-03-04 19:34:08

No patch -> better luck in 3.4.1.

Cheers,

Michael


---

Comment by roed created at 2009-03-17 05:43:30

> The question is, should this be an error, or just work? 
> 
> {{{
> sage: K = Qp(5, 10)
> sage: a = K(1/250037); a
> 3 + 4*5 + 3*5^2 + 3*5^3 + 5^4 + 5^5 + 5^6 + 5^7 + 4*5^8 + 4*5^9 + O(5^10)
> sage: ZZ(a)
> 9472973
> sage: QQ(a)
> Traceback (most recent call last):
> ...
> ValueError: Rational reconstruction of 9472973 (mod 9765625) does not exist.
> }}}

It seems like a valid error: 250037 is too large compared to 5^10.


---

Comment by robertwb created at 2009-03-17 05:53:34

THe question is, should QQ(a) be the same as QQ(ZZ(a)) if rational reconstruction isn't possible? (I'm not convinced either way yet.)


---

Comment by kedlaya created at 2009-05-20 19:12:02

I'd say (and I think Robert agrees) that the correct way to fix the original problem is to do all the arithmetic for Coleman integration in the p-adics, eliminating the casting to/from the rationals altogether. That was a hack from back when p-adic arithmetic was unusably slow.

If there is an issue with rational reconstruction, I'd say make that a separate ticket.


---

Attachment


---

Attachment

See attached patches. The first one eliminates all casting to/from QQ (I think). The second one adds a doctest to confirm that the above example now works:

```
sage: R.<x> = QQ['x']
sage: H = HyperellipticCurve(x*(x-1)*(x+9))
sage: K = Qp(7,10)
sage: HK = H.change_ring(K)
sage: import sage.schemes.elliptic_curves.monsky_washnitzer as mw
sage: M_frob, forms = mw.matrix_of_frobenius_hyperelliptic(HK)
sage: w = HK.invariant_differential()
sage: x,y = HK.monsky_washnitzer_gens()
sage: f = forms[0]
sage: S= HK(9,36)
sage: Q = HK.teichmuller(S)
sage: P = HK(-1,4)
sage: b = x*w*w._coeff.parent()(f)
sage: HK.coleman_integral(b,P,Q)
7 + 7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^6 + 5*7^7 + 3*7^8 + 4*7^9 + 4*7^10 + O(7^11)
```



---

Attachment

Rebased against the revised patch to #5948. You may ignore the previous two patches.


---

Comment by robertwb created at 2009-05-22 21:20:23

It's nice to have decent enough p-adics to use them!


---

Comment by kedlaya created at 2009-05-23 18:34:49

So it looks like I didn't manage to get out all of the casting; there is still some in matrix_of_frobenius_hyperelliptic. But I'd say we should wait until #6084 is resolved before looking into that; in the interim, this suffices to fix the bug in question.


---

Comment by mhansen created at 2009-06-01 06:13:09

Resolution: fixed


---

Comment by mhansen created at 2009-06-01 06:13:09

Merged 5430-v2.patch in 4.0.1.alpha0.
