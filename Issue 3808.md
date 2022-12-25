# Issue 3808: bug in Hom constructor for finite fields

archive/issues_003808.json:
```json
{
    "body": "Assignee: somebody\n\nReported by Nick Alexander:\n\n```\nsage: K.<a> = FiniteField(7^2)\nsage: a\na\nsage: a^7\n6*a + 1\nsage: K.Hom([a^7])\nSet of field embeddings from Finite Field in a of size 7^2 to [6*a + 1]\nsage: list(K.Hom([a^7]))\n------------------------------------------------------------------------\n---\nAttributeError                            Traceback (most recent call\nlast)\n\n/Users/ncalexan/sage-3.0.6/devel/sage-nca/<ipython console> in\n<module>()\n\n/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/\nrings/finite_field_morphism.py in __getitem__(self, n)\n    169               Defn: a |--> b^9 + b^7 + b^6 + b^5 + b^4]\n    170         \"\"\"\n--> 171         return self.list()[n]\n    172\n    173     def index(self, item):\n\n/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/\nrings/finite_field_morphism.py in list(self)\n    139         D = self.domain()\n    140         C = self.codomain()\n--> 141         if D.characteristic() == C.characteristic() and\nInteger(D.degree()).divides(Integer(C.degree())):\n    142             f = D.modulus()\n    143             g = C['x'](f)\n\nAttributeError: 'list' object has no attribute 'characteristic'\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3808\n\n",
    "created_at": "2008-08-12T02:03:57Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "bug in Hom constructor for finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3808",
    "user": "https://github.com/williamstein"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/3808





---

archive/issue_events_008740.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/fwclarke",
    "created_at": "2008-09-02T13:54:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3808",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3808#event-8740"
}
```



---

archive/issue_comments_027001.json:
```json
{
    "body": "Changing component from basic arithmetic to algebra.",
    "created_at": "2008-09-02T13:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3808#issuecomment-27001",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Changing component from basic arithmetic to algebra.



---

archive/issue_comments_027002.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-09-02T13:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3808#issuecomment-27002",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Resolution: invalid



---

archive/issue_comments_027003.json:
```json
{
    "body": "I guess what was meant here was\n\n```\nsage: K.<a> = FiniteField(7^2)\nsage: K.hom([a^7])\n\nRing endomorphism of Finite Field in a of size 7^2\n  Defn: a |--> 6*a + 1\n```\nWith 'hom' rather than 'Hom' it works fine.  As does\n\n```\nsage: K.Hom(K)\nAutomorphism group of Finite Field in a of size 7^2\nsage: K.Hom(K).list()\n\n[\nRing endomorphism of Finite Field in a of size 7^2\n  Defn: a |--> 6*a + 1,\nRing endomorphism of Finite Field in a of size 7^2\n  Defn: a |--> a\n]\n```\n\nThe reported behaviour with `K.Hom([a^7])` is much more general; it is the default for creating Homsets: if no specific method exists to construct the Homset, just name it (however meaningless that may be!).  Thus\n\n```\nsage: QQ.Hom(5)\nSet of Morphisms from Rational Field to 5 in Category of objects\n```\nAttempting to list such sets of morphisms leads to an error.\n\nI think this has to be regarded as a feature rather than a bug.",
    "created_at": "2008-09-02T13:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3808#issuecomment-27003",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

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

archive/issue_comments_027004.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2008-09-02T13:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3808#issuecomment-27004",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Changing priority from major to minor.
