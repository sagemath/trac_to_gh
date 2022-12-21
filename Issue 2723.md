# Issue 2723: [with patch] coercion error in monomial_quotient

Issue created by migration from Trac.

Original creator: jbmohler

Original creation time: 2008-03-29 18:49:27

Assignee: malb

The monomial_quotient method can give invalid data:

```
sage: R.<x,y>=ZZ[]
sage: R.monomial_quotient(2*x*y,y,coeff=True)
2*x
sage: R.monomial_quotient(2*x*y,3*y,coeff=True)
2/3*x
sage: R.monomial_quotient(2*x*y,3*y,coeff=True).parent()
Multivariate Polynomial Ring in x, y over Integer Ring
```

2/3 is *not* an Integer!

The attached patch gives:

```
sage: R.<x,y>=ZZ[]
sage: R.monomial_quotient(2*x*y,y,coeff=True)
2*x
sage: R.monomial_quotient(2*x*y,3*y,coeff=True)
...
<type 'exceptions.TypeError'>: no coercion of this rational to integer
```




---

Attachment


---

Comment by malb created at 2008-03-29 19:03:24

patch looks good.


---

Comment by mabshoff created at 2008-03-29 19:19:35

Resolution: fixed


---

Comment by mabshoff created at 2008-03-29 19:19:35

Merged in Sage 2.11.rc0
