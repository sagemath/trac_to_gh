# Issue 3440: Our PolyBoRi's GB calculation in AES mode is broken

Issue created by migration from https://trac.sagemath.org/ticket/3440

Original creator: malb

Original creation time: 2008-06-16 20:03:55

Assignee: malb

CC:  polybori burcin

Keywords: polybori

Burcin says this broke when the iterators changed:

```
sage: sr = mq.SR(2,1,1,4,gf2=True)
sage: F,s = sr.polynomial_system()
sage: R = F.ring()
sage: B = BooleanPolynomialRing(R.ngens(),R.variable_names())
sage: I = Ideal([B(f) for f in F])
sage: type(I)
<class 'sage.rings.polynomial.pbori.BooleanPolynomialIdeal'>
sage: I.groebner_basis(aes=True)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)
...
/usr/local/sage-3.0/local/lib/python2.5/site-packages/polybori/PyPolyBoRi.py in <lambda>(x)
     21 OrderCode.__dict__ = order_dict
     22
---> 23 Variable = lambda x: get_cring().gen(x)
     24
     25 def Ring(n, order='lp'):

/home/malb/pbori.pyx in sage.rings.polynomial.pbori.BooleanPolynomialRing.gen (sage/rings/polynomial/pbori.cpp:3333)()

<type 'exceptions.TypeError'>: an integer is required
```



---

Comment by PolyBoRi created at 2008-06-17 06:03:58

in PolyBoRi 0.5 will change iterators again ;-).
I hope more SAGE-friendly

for variable in m.variables()
for term in p.terms()


---

Comment by malb created at 2008-08-18 12:10:57

this fixes the first issue


---

Attachment

The attache patch fixes the issue above, however now:


```
sage: sr = mq.SR(2,1,1,4,gf2=True)
sage: F,s = sr.polynomial_system()
sage: R = F.ring()
sage: B = BooleanPolynomialRing(R.ngens(),R.variable_names())
sage: I = Ideal([B(f) for f in F])
sage: type(I)
<class 'sage.rings.polynomial.pbori.BooleanPolynomialIdeal'>
sage: I.groebner_basis(aes=True)
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
...
/usr/local/sage-3.0.6/local/lib/python2.5/site-packages/polybori/aes.py in preprocess(I, prot)
     55     global cache
     56     if get_order_code()==OrderCode.lp:
---> 57       import cache as cache_module
     58       cache=cache_module.cache
     59       del cache_module
ImportError: No module named cache
```


Ideas, thoughts, work-arounds?


---

Comment by PolyBoRi created at 2008-08-18 12:19:24

personally, at the moment, I don't feel, that it is good to expose this option to
users. I did that for aes systems initially. But it is not about: Use that option and everything will work well...

Nevertheless: workaround
replace 57/58 by

```
cache={}
```

which will make it slower.
I think, we don't distribute cache.py (which contains some GB of the 8BIT SBOX).


---

Comment by malb created at 2008-08-18 14:03:14

I vote for applying my patch then and closing this ticket. We don't actively expose aes=True to the user, i.e. it is not documented etc. It just happens to work since we pass the parameters thru to PolyBoRi.


---

Comment by burcin created at 2008-08-27 16:08:32

Trivial patch, looks good to me.

Sorry for the very late review.


---

Comment by mabshoff created at 2008-08-27 21:28:24

Merged in Sage 3.1.2.alpha2


---

Comment by mabshoff created at 2008-08-27 21:28:24

Resolution: fixed
