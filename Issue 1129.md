# Issue 1129: is_irreducible()

Issue created by migration from Trac.

Original creator: jvoight

Original creation time: 2007-11-08 16:22:36

Assignee: was

sage: F.<t> = NumberField(x^2-5)
sage: Fx.<xF> = PolynomialRing(F)
sage: f = Fx([2*t - 5, 5*t - 10, 3*t - 6, -t, -t + 2, 1])
sage: f.is_irreducible()
---------------------------------------------------------------------------
<class 'sage.libs.pari.gen.PariError'>    Traceback (most recent call last)

/home/jvoight/<ipython console> in <module>()

/home/jvoight/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.is_irreducible()

/home/jvoight/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.factor()

/home/jvoight/gen.pyx in sage.libs.pari.gen._pari_trap()

<class 'sage.libs.pari.gen.PariError'>:  (8)
sage: %magma

  --> Switching to Magma <--

''
magma: F<t> := NumberField(Polynomial([-5,0,1]));

magma: Factorization(Polynomial([2*t - 5, 5*t - 10, 3*t - 6, -t, -t + 2, 1]));

[
<$.1 + 1, 1>,
<$.1 + 1/2*(-t + 1), 2>,
<$.1^2 + 1/2*(t - 5), 1>
]
magma: quit


---

Comment by AlexGhitza created at 2007-11-17 22:20:39

I don't know whether this helps, but here it is:  the problem is clearly in factor(), not in is_irreducible().  Now the function factor() first creates the pari polynomial

```
Mod(1, a^2 - 5)*x^5 + Mod(-a + 2, a^2 - 5)*x^4 + Mod(-a, a^2 - 5)*x^3 + Mod(3*a - 6, a^2 - 5)*x^2 + Mod(5*a - 10, a^2 - 5)*x + Mod(2*a - 5, a^2 - 5)
```

and then asks pari to factor it.

But this is what happens if I try that directly in pari:

```
? f=Mod(1, a^2 - 5)*x^5 + Mod(-a + 2, a^2 - 5)*x^4 + Mod(-a, a^2 - 5)*x^3 + Mod(3*a - 6, a^2 - 5)*x^2 + Mod(5*a - 10, a^2 - 5)*x + Mod(2*a - 5, a^2 - 5)
%7 = Mod(1, a^2 - 5)*x^5 + Mod(-a + 2, a^2 - 5)*x^4 + Mod(-a, a^2 - 5)*x^3 + Mod(3*a - 6, a^2 - 5)*x^2 + Mod(5*a - 10, a^2 - 5)*x + Mod(2*a - 5, a^2 - 5)
? factor(f)
  *** factor: bug in GP (Segmentation Fault), please report
```


So it seems to be an issue with pari, not with sage proper.


---

Comment by craigcitro created at 2007-12-01 23:30:15

Added a fix for this bug. This code called into the pari library function factor0, which was then calling off to factornf. The error coming from factornf is still boggling to me (see note below), but reading the documentation, it mentions that nffactor is in general faster anyway. So I switched the code to use nffactor; this required one small modification elsewhere in the NumberField code. Specifically, F.pari_polynomial would always return a polynomial in "x", but we needed it to be in a different variable (because of Pari's notion of "priority" of variables, basically). So I added an optional argument to that function, switched the factor for polynomials over a NumberField to call into nffactor, and now everything seems to work. 

Note: the Pari error can be reproduced in gp as follows:


```
? f=Mod(1, a^2 - 5)*x^5 + Mod(-a + 2, a^2 - 5)*x^4 + Mod(-a, a^2 - 5)*x^3 + Mod(3*a - 6, a^2 - 5)*x^2 + Mod(5*a - 10, a^2 - 5)*x + Mod(2*a - 5, a^2 - 5)
%1 = Mod(1, a^2 - 5)*x^5 + Mod(-a + 2, a^2 - 5)*x^4 + Mod(-a, a^2 - 5)*x^3 + Mod(3*a - 6, a^2 - 5)*x^2 + Mod(5*a - 10, a^2 - 5)*x + Mod(2*a - 5, a^2 - 5)
? factor(f)
  *** factornf: reducible modulus in factornf.
? factornf(f, a^2-5)
  *** factornf: reducible modulus in factornf.
```


The documentation for factornf says that it uses "Trager's trick" to do factorization over a number field. I think this is just a bug in Pari, which I'm happy to report, as long as someone confirms for me that I'm not doing something stupid (i.e. not knowing how to use Pari correctly).


---

Comment by craigcitro created at 2007-12-01 23:30:15

Changing status from new to assigned.


---

Comment by craigcitro created at 2007-12-01 23:30:15

Changing assignee from was to craigcitro.


---

Comment by cwitty created at 2007-12-02 00:28:37

My results for that gp session don't quite match yours:

```
parisize = 4000000, primelimit = 500000
? f=Mod(1, a^2 - 5)*x^5 + Mod(-a + 2, a^2 - 5)*x^4 + Mod(-a, a^2 - 5)*x^3 + Mod(3*a - 6, a^2 - 5)*x^2 + Mod(5*a - 10, a^2 - 5)*x + Mod(2*a - 5, a^2 - 5)
%1 = Mod(1, a^2 - 5)*x^5 + Mod(-a + 2, a^2 - 5)*x^4 + Mod(-a, a^2 - 5)*x^3 + Mod(3*a - 6, a^2 - 5)*x^2 + Mod(5*a - 10, a^2 - 5)*x + Mod(2*a - 5, a^2 - 5)
? factor(f)
  *** factor: bug in GP (Segmentation Fault), please report
```

This is with 32-bit x86 Debian testing; I get the same results from "sage -gp" and from "/usr/bin/gp" (from the Debian pari-gp package, version 2.3.2-1).


---

Comment by robertwb created at 2007-12-02 02:57:49

I don't know much about the factornf vs. nffactor, but it seems to work for me.


---

Comment by robertwb created at 2007-12-02 08:49:18

I'm now getting


```
sage:             sage: x = polygen(QQ, 'x')
sage:             sage: f = x^6 + 10/7*x^5 - 867/49*x^4 - 76/245*x^3 + 3148/35*x^2 - 25944/245*x + 48771/1225
sage:             sage: K.<a> = NumberField(f)
sage:             sage: S.<T> = K[]
sage:             sage: ff = S(f); ff
T^6 + 10/7*T^5 + (-867/49)*T^4 + (-76/245)*T^3 + 3148/35*T^2 + (-25944/245)*T + 48771/1225
sage: ff.factor()
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "polynomial_element.pyx", line 1637, in sage.rings.polynomial.polynomial_element.Polynomial.factor
  File "gen.pyx", line 6474, in sage.libs.pari.gen._pari_trap
<class 'sage.libs.pari.gen.PariError'>:  (8)
```



---

Attachment


---

Comment by craigcitro created at 2007-12-02 10:13:35

Fixed this patch up a bit. First, at cwitty's suggestion, rewrote it so that it avoids calling nfinit simply for a change in variable names. Also, wrote some (mildly unwieldy) code to deal with cases like factoring x^2-1/3 over a number field generated by x^2-1/4 -- this is particularly troublesome, since Pari only likes to work with integral polynomials. It all seems to work now, though I make no promises about the speed in the non-integral case. If someone notices it being particularly slow in this case, make a trac ticket and we'll start looking into it.


---

Comment by cwitty created at 2007-12-02 17:54:53

Mostly I like the patch.  I do have one question, though: you use the slow path if self.denominator() != 1.  Is that actually required?  (If so, why?)


---

Attachment


---

Comment by craigcitro created at 2007-12-02 19:10:23

Added a patch (that applies after trac_1129.hg) that touches up something suggested by cwitty; namely, if the number field is defined by an integral polynomial, there's no reason to do anything complicated with Pari, even if the polynomial we want to factor is non-integral.


---

Comment by cwitty created at 2007-12-02 19:29:04

I like the new version.  Doctests pass in sage/rings.  (Apply trac_1129.hg, then 1129_2.patch)


---

Comment by mabshoff created at 2007-12-02 20:19:26

Merged in 2.8.15.rc0.


---

Comment by mabshoff created at 2007-12-02 20:19:26

Resolution: fixed
