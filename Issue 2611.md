# Issue 2611: [with patch, needs review] add monomial_coefficent to boolean polynomials

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-03-20 11:53:32

Assignee: malb

CC:  burcin

With the attached patch this works:

```
sage: sr = mq.SR(gf2=True)
sage: sr
SR(1,1,1,4)

sage: F,s = sr.polynomial_system()
sage: R = F.ring()
sage: B = BooleanPolynomialRing(R.ngens(),R.variable_names(),R.term_order())
sage: F = [B(f) for f in F]
sage: F = mq.MPolynomialSystem(B,F)
sage: F
Polynomial System with 56 Polynomials in 20 Variables
sage: A,v = F.coefficient_matrix() # this relies on monomial_coefficient
```



---

Attachment


---

Comment by jbmohler created at 2008-03-20 12:26:21

I'm concerned by this:

```
sage: R.<x,y,z,a,b,c>=BooleanPolynomialRing(6)
sage: f=(1-x)*(1+y)
sage: f
x*y + x + y + 1
sage: f.monomial_coefficient(1)  # Shouldn't this return 1?
0
sage: f.monomial_coefficient(x^0)
1
```

I think a little bit of type checking would improve things.

I also notice that we don't have a coefficient method like the other mpoly rings.  However, I don't think we should let lack of associated functionality hold up a patch providing functionality.


---

Attachment

The attached patch fixes the issue with different types.


---

Comment by AlexGhitza created at 2008-03-28 14:08:36

Looks good to me, and Joel's concerns have been addressed.


---

Comment by mabshoff created at 2008-03-28 15:14:39

Merged in Sage 2.11.alpha2


---

Comment by mabshoff created at 2008-03-28 15:14:39

Resolution: fixed
