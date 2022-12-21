# Issue 2653: norm and trace of elements of orders are Rational not Integer

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-03-23 10:34:32

Assignee: was

Keywords: orders, norm, trace

For elements of an order, the norm and trace are (mathematically) integers, but Sage returns Rationals.  More generally, the charpoly and minpoly are returned as Rational polynomials when they are (mathematically) in ZZ[].


```
sage: Zi.<i>=ZZ.extension(x^2+1)
sage: n=(1+i).norm()
sage: type(n)
<type 'sage.rings.rational.Rational'>
sage: t=(1+i).trace()
sage: type(t)
<type 'sage.rings.rational.Rational'>
sage: p=(1+i).charpoly()
sage: type(p)
<class 'sage.rings.polynomial.polynomial_element_generic.Polynomial_rational_dense'>
sage: p=(1+i).minpoly()
sage: type(p)
<class 'sage.rings.polynomial.polynomial_element_generic.Polynomial_rational_dense'>
```


I would like this to change, as it led to some very inefficient behaviour until I discovered it, and now I am having to manually coerce norms and traces into ZZ.



---

Comment by cremona created at 2008-03-23 10:38:57

Actually it is worse than that:

```
sage: Zi.<i>=ZZ.extension(x^2+1)
sage: a=1+i
sage: a.norm()
4
sage: a.trace()
4
sage: a.minpoly()
x - 2
sage: a.charpoly()
x^2 - 4*x + 4
```


These are wrong!  Both the minpoly and charpoly of 1+i should be x^2-2*x+2, the trace should be 2 and the norm 2.


---

Comment by cremona created at 2008-03-23 10:48:05

Apologies:  the code

```
sage: Zi.<i>=ZZ.extension(x^2+1)
```

results in i being asigned to the first Z-module generator of the order, which is 1:

```
sage: i
1
```

so the second posting on this ticket is incorrect to say that the minpoly and charpoly (etc) are wrongly computed.

However I do *not* think that users should be allowed to enter

```
sage: Zi.<i>=ZZ.extension(x^2+1)
```

and have i assigned to 1.


---

Attachment


---

Comment by cremona created at 2008-03-26 22:08:30

Review of patch:  the code looks just fine and appears to solve the problem raised.  I only say "appears" as I'm travelling and not in a position to test it myself, but the added doctests give me sufficitne confidence to say: OK!


---

Comment by mabshoff created at 2008-03-26 22:13:02

Merged in Sage 2.11.alpha2


---

Comment by mabshoff created at 2008-03-26 22:13:02

Resolution: fixed
