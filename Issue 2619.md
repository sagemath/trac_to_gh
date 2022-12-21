# Issue 2619: [with patch, needs review] Gröbner bases over quotient rings

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-03-20 21:58:52

Assignee: malb

After the patch was applied (which depends on #2618) this should work again:

```
sage: P.<a,b,c,d,e> = PolynomialRing(GF(2), 5, order='lex')
sage: I1 = ideal([a*b + c*d + 1, a*c*e + d*e, a*b*e + c*e, b*c + c*d*e + 1])
sage: Q = P.quotient( sage.rings.ideal.FieldIdeal(P) )
sage: I2 = ideal([Q(f) for f in I1.gens()])
sage: I2.groebner_basis()
[ebar, cbar + 1, bbar + 1, abar + dbar + 1]
```



---

Attachment

Looks good to me.


---

Comment by mabshoff created at 2008-03-21 02:23:12

Merged in Sage 2.11.alpha1


---

Comment by mabshoff created at 2008-03-21 02:23:12

Resolution: fixed
