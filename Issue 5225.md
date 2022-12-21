# Issue 5225: unhandled case in converting to polynomial ring

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2009-02-09 22:14:57

Assignee: malb

Normally, Sage tries to allow explicit conversions between arbitrary polynomial rings, if they share the same variable names.

Here's a case where that doesn't work:

```
R.<a,b,c,d,e,f,x,y,z,t,s,r>=PolynomialRing(QQ,12,order='lex')
I=R.ideal(a^2+d^2-x,a*b+d*e-y,a*c+d*f-z,b^2+e^2-t,b*c+e*f-s,c*c+f*f-r)
j=I.groebner_basis()
R1.<x,y,z,t,s,r>=QQ[]
R2=FractionField(R1)
R3.<a,b,c,d,e,f>=R1.fraction_field()[]
R3(j[0])
```


For now, the workaround is:

```
 sage_eval(str(j[0]), locals=locals())
```

but IMHO the original code should work.


---

Comment by bruno created at 2016-04-13 14:08:34

A smaller example (minimal I hope ;-)):

```python
sage: R = QQ['a,b,x,y']
sage: S = Frac(QQ['x,y'])['a,b']
sage: p = R.gen(0) + R.gen(1) + R.gen(2)
sage: S(p)
Traceback (most recent call last):
...
TypeError: Could not find a mapping of the passed element to this ring.
```



---

Comment by mkoeppe created at 2022-05-04 23:06:44

In 9.6.rc3:

```
sage: R.<a,b,c,d,e,f,x,y,z,t,s,r>=PolynomialRing(QQ,12,order='lex')
....: I=R.ideal(a^2+d^2-x,a*b+d*e-y,a*c+d*f-z,b^2+e^2-t,b*c+e*f-s,c*c+f*f-r)
....: j=I.groebner_basis()
....: R1.<x,y,z,t,s,r>=QQ[]
....: R2=FractionField(R1)
....: R3.<a,b,c,d,e,f>=R1.fraction_field()[]
....: R3(j[0])
a^2 + d^2 + (-x)
```

and

```
sage: R = QQ['a,b,x,y']
....: S = Frac(QQ['x,y'])['a,b']
....: p = R.gen(0) + R.gen(1) + R.gen(2)
....: S(p)
a + b + x
```



---

Comment by mkoeppe created at 2022-05-04 23:06:44

Changing status from new to needs_review.


---

Comment by vdelecroix created at 2022-05-10 16:21:55

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2022-05-11 02:14:43

Resolution: invalid
