# Issue 3808: bug in Hom constructor for finite fields

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-08-12 02:03:57

Assignee: somebody

Reported by Nick Alexander:


```
sage: K.<a> = FiniteField(7^2)
sage: a
a
sage: a^7
6*a + 1
sage: K.Hom([a^7])
Set of field embeddings from Finite Field in a of size 7^2 to [6*a + 1]
sage: list(K.Hom([a^7]))
------------------------------------------------------------------------
---
AttributeError                            Traceback (most recent call
last)

/Users/ncalexan/sage-3.0.6/devel/sage-nca/<ipython console> in
<module>()

/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/
rings/finite_field_morphism.py in __getitem__(self, n)
    169               Defn: a |--> b^9 + b^7 + b^6 + b^5 + b^4]
    170         """
--> 171         return self.list()[n]
    172
    173     def index(self, item):

/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/
rings/finite_field_morphism.py in list(self)
    139         D = self.domain()
    140         C = self.codomain()
--> 141         if D.characteristic() == C.characteristic() and
Integer(D.degree()).divides(Integer(C.degree())):
    142             f = D.modulus()
    143             g = C['x'](f)

AttributeError: 'list' object has no attribute 'characteristic'
```



---

Comment by fwclarke created at 2008-09-02 13:54:03

Changing component from basic arithmetic to algebra.


---

Comment by fwclarke created at 2008-09-02 13:54:03

Resolution: invalid


---

Comment by fwclarke created at 2008-09-02 13:54:03

I guess what was meant here was

```
sage: K.<a> = FiniteField(7^2)
sage: K.hom([a^7])

Ring endomorphism of Finite Field in a of size 7^2
  Defn: a |--> 6*a + 1
```

With 'hom' rather than 'Hom' it works fine.  As does

```
sage: K.Hom(K)
Automorphism group of Finite Field in a of size 7^2
sage: K.Hom(K).list()

[
Ring endomorphism of Finite Field in a of size 7^2
  Defn: a |--> 6*a + 1,
Ring endomorphism of Finite Field in a of size 7^2
  Defn: a |--> a
]
```


The reported behaviour with `K.Hom([a^7])` is much more general; it is the default for creating Homsets: if no specific method exists to construct the Homset, just name it (however meaningless that may be!).  Thus

```
sage: QQ.Hom(5)
Set of Morphisms from Rational Field to 5 in Category of objects
```

Attempting to list such sets of morphisms leads to an error.

I think this has to be regarded as a feature rather than a bug.


---

Comment by fwclarke created at 2008-09-02 13:54:03

Changing priority from major to minor.
