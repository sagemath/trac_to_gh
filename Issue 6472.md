# Issue 6472: ideal.groebner_basis gives incorrect answers

Issue created by migration from https://trac.sagemath.org/ticket/6472

Original creator: broune

Original creation time: 2009-07-07 04:49:45

Assignee: tbd

This is wrong:


```
sage: R.<a,b,c,d>=PolynomialRing(QQ,order="lex")
sage: ideal(a-b^16,b-c^16,c-d^1024).groebner_basis()
[a - d^4096, b - d^16384, c - d^1024]
```


The correct answer as given by Macaulay 2:


```
i30 : R=QQ[a,b,c,d, MonomialOrder=>Lex];
i31 : I=ideal(a-b^16,b-c^16,c-d^1024);
i32 : gens gb I
o32 = | c-d1024 b-d16384 a-d262144 |
```


In particular the binomial involving a should raise d to the power 262144=2<sup>18</sup>, not 4096=2<sup>12</sup> as Sage reports.

I suspect that the reason is that by default Sage uses Singular to implement groebner_basis, and Singular has limitations on the size of exponents. See http://www.singular.uni-kl.de/Manual/latest/sing_343.htm#SEC384 which in particular says


```
the maximal allowed exponent of a ring variable depends on the ordering of the ring and is at least 32767.
```



---

Comment by AlexGhitza created at 2009-11-15 13:15:21

Changing component from algebra to commutative algebra.


---

Comment by jakobkroeker created at 2016-10-04 23:18:59

reported upstream:

https://www.singular.uni-kl.de:8005/trac/ticket/774#ticket


---

Comment by jakobkroeker created at 2016-10-04 23:50:00

another funny example :


```
R.<b,c,d>=PolynomialRing(QQ,order="lex")
sage: ideal(b-c^64,c-d^1024).groebner_basis()
```

(wrong result and zero not shown)

```
[b - , c - d^1024]
```



---

Comment by dimpase created at 2016-10-05 23:49:22

Does Singular simply return incorrect results, or it's rather a Sage interface bug?


---

Comment by jakobkroeker created at 2016-10-06 22:57:13

fixed in https://github.com/Singular/Sources/commit/349e5e898aad7e735b03bda328f2741a7c36a092

broken again for 'groebner' with https://github.com/Singular/Sources/commit/17510a828cdc33aa541d40a9bbfb825b72812521


---

Comment by sbrandhorst created at 2018-07-01 20:44:07

Changing status from new to needs_review.


---

Comment by sbrandhorst created at 2018-07-01 20:44:07


```
sage: R.<a,b,c,d>=PolynomialRing(QQ,order="lex")
....: 
sage: I = ideal(a-b^16,b-c^16,c-d^1024)
sage: I.groebner_basis()
   skipping text from `)` error at token `)`
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
RuntimeError: Error raised calling singular function
...
RuntimeError: error in Singular function call 'groebner':
exponent bound is 65535
error occurred in or before standard.lib::stdhilb line 381: `    i=interred(i);`
leaving standard.lib::stdhilb
leaving standard.lib::groebner
```


Looks good to me.


---

Comment by dimpase created at 2018-07-01 20:51:11

This 

```
  skipping text from `)` error at token `)`
```

looks ugly, but otherwise there seems nothing to fix here---unless nowadays Singular offers an option to have bigger exponents.


---

Comment by embray created at 2018-08-14 17:30:02

Resolution: worksforme
