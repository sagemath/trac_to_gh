# Issue 1867: suggested way to fix #1705 -- factoring multivariate polynomials over finite fields is broken in Singular

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-20 16:50:41

Assignee: malb

There is a standard algorithm to factor polynomials over a non-prime field that reduces the problem to factoring over a prime field and using gcd over the non-prime field.  It seems that gcd works fine over non-prime fields in Singular, as does factoring over prime fields, so this should work for us.   Probably singular doesn't do this because either it is slower or it is too much of a pain to implement in Singular (which isn't much of a language), or maybe they just don't care about this problem.

Anyway, to start this off, here is a sample session that illustrates the idea:

```
sage: k.<a> = GF(9)
sage: R.<x,y> = PolynomialRing(k)
sage: f = (x-a)*(y-a)
sage: f.factor()
Traceback (most recent call last):
...
NotImplementedError: factorization of multivariate polynomials over non-prime fields explicitly disabled due to bugs in Singular
sage: singular(f)
sage: x*y+(-a)*x+(-a)*y+(a+1)
x*y + ( - a)*x + ( - a)*y + (a + 1)
sage: singular(f).factorH()
[1]:
   _[1]=1
   _[2]=x*y+(-a)*x+(-a)*y+(a+1)
[2]:
   1,1
sage: g = f*(x-a^3)*(y-a^3); g
x^2*y^2 - x^2*y - x*y^2 - x^2 + x*y - y^2 + x + y + 1
sage: gg = GF(3)['x,y'](repr(g))    # why doesn't change ring or coerce work
sage: F = gg.factor()
sage: factor1 = R(F[0][0])
sage: factor2 = R(F[1][0])
sage: factor1.gcd(f)
(a)*y + ( - a - 1)
sage: factor2.gcd(f)
(a)*x + ( - a - 1)

```



---

Comment by was created at 2009-01-23 10:39:26

Change ring being broken, e.g.,


```
g.change_ring(GF(3))
```


in the above example, is now trac #5068.


---

Comment by was created at 2009-01-23 15:38:26

I have attached a patch that:

 * fully implements this idea.  This works with dramatically higher probability than singular itself.  Singular usually gives wrong answers, whereas with this code it seems right "about 99% of the time".  E.g., this runs for a long time before finding a problem:

```
k.<a> = GF(3^2); R.<x,y> = PolynomialRing(k)
for i in range(500):
    v = [R.random_element() for _ in range(3)]; print i; assert prod(v).factor(proof=False).prod() == prod(v)

1
...
328
boom!
AssertionError: bug in Singular factoring an auxiliary polynomial over GF(p): bad multiplicity (1, 2)
```


and



 * found bugs in factorization over GF(p) -- see ticket #5068.  Added a proof flag, and *only* allow factoring if proof=False.

I think this should go into sage because: 
   1. It works massively better than singular currently does over GF(q).
   2. Even if singular does fix say factoring, maybe they will only fix GF(p) factorization and not GF(p^e).  Then this code will make factoring over GF(p^e) work too.
   3. If we ever implement our own factorization then this code means we only have to implement GF(p), at least for starters.  It would be very nice if we at least had *some* implementation that works, even if is slow.
   4. This patch adds some useful functions such as map_coefficients (which has the same api as the corresponding function in sage-combinat), and _norm_over_nonprime_finite_field. 


---

TEST CODE:


```
k.<a> = GF(3^5); R.<x,y> = PolynomialRing(k)
for i in range(100):
    v = [R.random_element() for _ in range(2)]; print i; assert prod(v).factor(False).prod() == prod(v)
#good


k.<a> = GF(997^2); R.<x,y> = PolynomialRing(k)
for i in range(100):
    v = [R.random_element() for _ in range(2)]; print i; assert prod(v).factor(False).prod() == prod(v)
#good


k.<a> = GF(4); R.<x,y,z> = PolynomialRing(k)
for i in range(100):
    v = [R.random_element() for _ in range(2)]; print i; assert prod(v).factor(False).prod() == prod(v)

# HORRIBLE: 
sage: k.<a> = GF(4); R.<x,y,z> = PolynomialRing(k)
sage: for i in range(100):
....:         v = [R.random_element() for _ in range(2)]; print i; assert prod(v).factor(False).prod() == prod(v)
....: 
0
1
...
30
convertFacCF2NTLGF2X: coefficient not immidiate!
[immediately exits sage!]


k.<a> = GF(7^2); R.<x,y> = PolynomialRing(k)
for i in range(100):
    v = [R.random_element() for _ in range(3)]; print i; assert prod(v).factor(False).prod() == prod(v)
#good


k.<a> = GF(7^2); R.<x,y,z> = PolynomialRing(k)
for i in range(100):
    v = [R.random_element() for _ in range(2)]; print i; assert prod(v).factor(False).prod() == prod(v)
#good

k.<a> = GF(3^6); R.<x,y> = PolynomialRing(k)
for i in range(100):
    v = [R.random_element() for _ in range(2)]; print i; assert prod(v).factor(False).prod() == prod(v)
#good

```



---

Attachment


---

Comment by kedlaya created at 2009-01-24 04:27:31

Almost, but 

```
	sage -t  "devel/sage-dev1/sage/rings/polynomial/multi_polynomial_libsingular.pyx"
```

fails a few doctests when I try it because of missing `proof=False` arguments. See lines 3432, 3461, 3491, 3502.


---

Attachment

this fixes the other problems in the doctests


---

Comment by was created at 2009-01-24 07:34:33

NOTE (from Noam Elkies):

Maxima can factor multivariate polynomials mod p.  However it sometimes will fail, as the example below illustrates. 


```
sage: R.<x,y> = GF(5)[]

sage: f = 2*x^2*y^2 + 2*y^4 + x^3 - 2*x^2*y + x*y^2 + y^3 + x^2 - x*y - y^2 - 2*x - 2*y - 2

sage: maxima.eval('modulus:5')
sage: maxima(f).factor()
Not enough choices for substitution.
```


This is a known issue.


---

Comment by kedlaya created at 2009-01-24 14:32:51

All doctests pass now. Positive review.


---

Comment by mabshoff created at 2009-01-25 20:57:59

Merged both patches in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-25 20:57:59

Resolution: fixed
