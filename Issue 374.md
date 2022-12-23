# Issue 374: Bug in factorization of polynomial over number field

Issue created by migration from https://trac.sagemath.org/ticket/374

Original creator: was

Original creation time: 2007-05-23 01:56:09

Assignee: somebody


```
x = polygen(QQ, 'x')
f = x^6 + 10/7*x^5 - 867/49*x^4 - 76/245*x^3 + 3148/35*x^2 - 25944/245*x + 48771/1225
```



```
legendre_symbol(-7,73)
///
-1
```



```
f.factor_mod(73)
///
(x^2 + 12*x + 47) * (x^2 + 15*x + 21) * (x^2 + 37*x + 21)
```



```
K.<a> = NumberField(f/1225)
S.<T> = K[]
ff = S(f)
print ff
///
1225*T^6 + 1750*T^5 + (-21675)*T^4 + (-380)*T^3 + 110180*T^2 + (-129720)*T + 48771
```



```
ff.factor()
///
MulMod: bad args
Aborted
```




---

Comment by was created at 2007-05-31 14:54:57

This was fixed by Joel Mohler's latest patch.


---

Comment by was created at 2007-05-31 14:54:57

Resolution: fixed


---

Comment by was created at 2007-08-19 06:57:53

Actually #374 can be removed, because creating number fields with non-monic polys is no longer supported.



```
sage: x = polygen(QQ, 'x')
sage: f = x^6 + 10/7*x^5 - 867/49*x^4 - 76/245*x^3 + 3148/35*x^2 - 25944/245*x + 48771/1225
sage: K.<a> = NumberField(f/1225)
sage: S.<T> = K[]
sage: ff = S(f)
sage: print ff
sage: 1225*T^6 + 1750*T^5 + (-21675)*T^4 + (-380)*T^3 + 110180*T^2 + (-129720)*T + 48771
Traceback (most recent call last):
...
NotImplementedError: number fields for non-monic polynomials not yet implemented.
```

