# Issue 1738: [with patch] fraction field __pow__ doesn't handle negative exp. elegantly

Issue created by migration from Trac.

Original creator: jbmohler

Original creation time: 2008-01-10 01:49:26

Assignee: was

Negative exponents put fraction field elements in the denominator of a fraction field element.


```
sage: R.<x>=ZZ[]
sage: (1/x)^-3
1/(1/x^3)
```


With the patch:

```
sage: R.<x>=ZZ[]
sage: (1/x)^-3
x^3
```

 


---

Attachment

It looks good to me except change the somewhat too verbose

```
  sage: x = PolynomialRing(RationalField(),'x').gen() 
```

to one of the following (take your pick):

```
  sage: x = polygen(QQ, 'x')
```

or 

```
  sage: R.<x> = QQ[]
```

or 

```
  sage: x = PolynomialRing(QQ,'x').gen()
```


I think it is important that the docstrings give illustrations of good usage of Sage.


---

Comment by mhansen created at 2008-01-16 22:05:40

Resolution: duplicate


---

Comment by mhansen created at 2008-01-16 22:06:19

This is a duplicate of #1786.  I didn't realize that this was indeed the issue when opening #1786.
