# Issue 4087: [with patch, needs review] Improved printing of polynomials with 'negative' coefficients

Issue created by migration from https://trac.sagemath.org/ticket/4087

Original creator: fwclarke

Original creation time: 2008-09-09 11:39:37

Assignee: tbd


```
sage: K.<w> = CyclotomicField(3)
sage: PK.<X> = K[]
sage: X^2 - w*X
X^2 + (-w)*X
sage: (X + w)*(X + w^2)
X^2 + (-1)*X + 1
```

It would be much better if these polynomials were printed as `X^2 - w*X` 
and `X^2 - X + 1`, respectively.  For polynomials with integer or rational 
coefficients such behaviour is already implemented.  Thus

```
sage: PolynomialRing(QQ, 'X')((X + w)*(X + w^2))
X^2 - X + 1
```

The attached patch makes this work more generally, and adjusts
`latex(polynomial)` correspondingly.

The patch also changes 59 doctests to reflect the new code; in every
case the new output is more readable.  The doctests for the
relevant `_repr` and `_latex_` functions did not previously test those
functions since they involved polynomials with rational coefficients, for
which different methods are used.




---

Attachment


---

Comment by fwclarke created at 2008-09-18 15:50:48

The patch works with 3.1.2, subject to:

```
patching file sage/rings/number_field/number_field.py
Hunk #8 succeeded at 5055 with fuzz 1 (offset 21 lines).
```

after which all doctests still pass.


---

Comment by cremona created at 2008-09-18 20:44:00

Patch applies as advertised to 3.1.2 (just the fuzz).

I take it that "sage -testall" has been done?  With or without "-long"?  Assuming so, I approve of this cosmetic but worthwhile patch.  I'm not doing a testall myself as I already have one in progress.


---

Comment by mabshoff created at 2008-09-19 00:18:47

Merged in Sage 3.1.3.alpha0


---

Comment by mabshoff created at 2008-09-19 00:18:47

Resolution: fixed
