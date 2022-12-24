# Issue 6392: modular abelian quotient -- something goes wrong

archive/issues_006392.json:
```json
{
    "body": "Assignee: craigcitro\n\nCC:  mderickx\n\nThis isn't right:\n\n```\nsage: J = J0(43)\nsage: G,_ = J[0].intersection(J[1])\nsage: J[1]/G\nSimple abelian subvariety 43b(1,43) of dimension 2 of J0(43)\n```\n\n\nThis is\n\n```\nsage: J[0]/G\n\n(Abelian variety factor of dimension 1 of J0(43),\n Abelian variety morphism:\n  From: Simple abelian subvariety 43a(1,43) of dimension 1 of J0(43)\n  To:   Abelian variety factor of dimension 1 of J0(43))\n```\n\n\nFor some reason J[1]/G isn't even creating the right output (i.e., pair (abvar, map)). \n\nIssue created by migration from https://trac.sagemath.org/ticket/6392\n\n",
    "created_at": "2009-06-24T09:53:32Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.4",
    "title": "modular abelian quotient -- something goes wrong",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6392",
    "user": "was"
}
```
Assignee: craigcitro

CC:  mderickx

This isn't right:

```
sage: J = J0(43)
sage: G,_ = J[0].intersection(J[1])
sage: J[1]/G
Simple abelian subvariety 43b(1,43) of dimension 2 of J0(43)
```


This is

```
sage: J[0]/G

(Abelian variety factor of dimension 1 of J0(43),
 Abelian variety morphism:
  From: Simple abelian subvariety 43a(1,43) of dimension 1 of J0(43)
  To:   Abelian variety factor of dimension 1 of J0(43))
```


For some reason J[1]/G isn't even creating the right output (i.e., pair (abvar, map)). 

Issue created by migration from https://trac.sagemath.org/ticket/6392





---

archive/issue_comments_051356.json:
```json
{
    "body": "G is strictly speaking not a subgroup of J[1] in this example it's a subgroup of J[0]. What happens if you travel down the code is equivalent to this:\n\n```\nG=J[1].finite_subgroup(G) #This should raise an error since J[0] and J[1] have empty intersection\nJ[1]._quotient_by_finite_subgroup(G):\n```\n\n\nNow the source code of _quotient_by_finite_subgroup is\n\n\n```\ndef _quotient_by_finite_subgroup(self, G):\n    if G.order() == 1:\n        return self\n    L = self.lattice() + G.lattice()\n    A = ModularAbelianVariety(self.groups(), L, G.field_of_definition())\n    M = L.coordinate_module(self.lattice()).basis_matrix()\n    phi = self.Hom(A)(M)\n    return A, phi\n```\n\nSo i guess it should instead return\n\n```\nreturn self, self.Hom(self).identity()\n```\n\n\nThere is also a problem with the is_subgroup code:\nsage: G.is_subgroup(J[1])\nTrue\nThis error is caused by the intersection code:\nsage: G.intersection(J[1])\nFinite subgroup with invariants [2, 2] over QQ of Simple abelian subvariety 43b(1,43) of dimension 2 of J0(43)\n\nMaybe I'm a bit confused but is the intersection of abelian varieties defined in an other way than just the set theoretic one. Because by reading the source code I really get the feeling that it does. The errors certainly seem to come from different assumtions about this in different parts of the code.",
    "created_at": "2010-12-21T15:41:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6392#issuecomment-51356",
    "user": "mderickx"
}
```

G is strictly speaking not a subgroup of J[1] in this example it's a subgroup of J[0]. What happens if you travel down the code is equivalent to this:

```
G=J[1].finite_subgroup(G) #This should raise an error since J[0] and J[1] have empty intersection
J[1]._quotient_by_finite_subgroup(G):
```


Now the source code of _quotient_by_finite_subgroup is


```
def _quotient_by_finite_subgroup(self, G):
    if G.order() == 1:
        return self
    L = self.lattice() + G.lattice()
    A = ModularAbelianVariety(self.groups(), L, G.field_of_definition())
    M = L.coordinate_module(self.lattice()).basis_matrix()
    phi = self.Hom(A)(M)
    return A, phi
```

So i guess it should instead return

```
return self, self.Hom(self).identity()
```


There is also a problem with the is_subgroup code:
sage: G.is_subgroup(J[1])
True
This error is caused by the intersection code:
sage: G.intersection(J[1])
Finite subgroup with invariants [2, 2] over QQ of Simple abelian subvariety 43b(1,43) of dimension 2 of J0(43)

Maybe I'm a bit confused but is the intersection of abelian varieties defined in an other way than just the set theoretic one. Because by reading the source code I really get the feeling that it does. The errors certainly seem to come from different assumtions about this in different parts of the code.



---

archive/issue_comments_051357.json:
```json
{
    "body": "My confusion mainly comes from the following:\n\n\n```\nsage: J[1].finite_subgroup(G)\nFinite subgroup with invariants [] over QQ of Simple abelian subvariety\n43b(1,43) of dimension 2 of J0(43)\nJ[1].intersection(G)\nFinite subgroup with invariants [2, 2] over QQ of Simple abelian\nsubvariety 43b(1,43) of dimension 2 of J0(43)\n```\n",
    "created_at": "2010-12-21T15:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6392#issuecomment-51357",
    "user": "mderickx"
}
```

My confusion mainly comes from the following:


```
sage: J[1].finite_subgroup(G)
Finite subgroup with invariants [] over QQ of Simple abelian subvariety
43b(1,43) of dimension 2 of J0(43)
J[1].intersection(G)
Finite subgroup with invariants [2, 2] over QQ of Simple abelian
subvariety 43b(1,43) of dimension 2 of J0(43)
```




---

archive/issue_comments_051358.json:
```json
{
    "body": "The issue was in `finite_subgroup`. We had to include the lattice of the ambient jacobian and not just the ambient abelian subvariety. \n\nThis branch returns the identity map as well when quotienting by a trivial group. \n----\nNew commits:",
    "created_at": "2018-09-19T23:19:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6392#issuecomment-51358",
    "user": "klui"
}
```

The issue was in `finite_subgroup`. We had to include the lattice of the ambient jacobian and not just the ambient abelian subvariety. 

This branch returns the identity map as well when quotienting by a trivial group. 
----
New commits:



---

archive/issue_comments_051359.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2018-09-19T23:20:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6392#issuecomment-51359",
    "user": "klui"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_051360.json:
```json
{
    "body": "ok, let it be. Please add author full name.",
    "created_at": "2018-09-20T12:11:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6392#issuecomment-51360",
    "user": "chapoton"
}
```

ok, let it be. Please add author full name.



---

archive/issue_comments_051361.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-09-20T12:11:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6392#issuecomment-51361",
    "user": "chapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_051362.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2018-09-20T17:48:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6392#issuecomment-51362",
    "user": "vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_051363.json:
```json
{
    "body": "Author name is missing..",
    "created_at": "2018-09-20T17:48:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6392#issuecomment-51363",
    "user": "vbraun"
}
```

Author name is missing..



---

archive/issue_comments_051364.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2018-09-20T17:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6392#issuecomment-51364",
    "user": "chapoton"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_051365.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2018-09-21T22:20:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6392#issuecomment-51365",
    "user": "vbraun"
}
```

Resolution: fixed
