# Issue 6473: ideal.interreduced_basis hangs forever

Issue created by migration from Trac.

Original creator: broune

Original creation time: 2009-07-07 05:00:28

Assignee: tbd

This completes in a fraction of a second:


```
sage: R.<a,b,c,d>=PolynomialRing(QQ,order="lex")
sage: ideal(a^16,a-b^16,b-c^16,c-d^15).interreduced_basis()
[d^61440, c - d^15, b - d^240, a - d^3840]
```


I stopped the following after more than an hour, which leads me to believe that Sage is stuck in an infinite loop:


```
sage: R.<a,b,c,d>=PolynomialRing(QQ,order="lex")
sage: ideal(a^16,a-b^16,b-c^16,c-d^16).interreduced_basis()
```


The only difference between the two is that the power of d in the input binomial involving c as the initial term is increased from 15 to 16. This difference has no mathematical significance and should have no impact on the computation time.

I suspect that the reason is that by default Sage uses Singular to implement interreduced_basis, and Singular has limitations on the size of exponents. See http://www.singular.uni-kl.de/Manual/latest/sing_343.htm#SEC384 which in particular says


```
the maximal allowed exponent of a ring variable depends on the ordering of the ring and is at least 32767.
```


In this case increasing the exponent from 15 to 16 makes the output have an exponent of 16<sup>4</sup>=2<sup>16</sup>=65536, while leaving it at 15 puts it just a bit below that, allowing to contain it within a 16 bit integer.



---

Comment by AlexGhitza created at 2009-11-15 13:15:53

Changing component from algebra to commutative algebra.


---

Comment by chapoton created at 2020-10-13 11:18:28

Changing keywords from "" to "groebner".
