# Issue 2895: [with patch, needs review] add support for Laurent polynomials in Sage

archive/issues_002895.json:
```json
{
    "body": "Assignee: somebody\n\nDavid Roe did the initial implementation, and Jason Bandlow and I cleaned it up and got it ready for inclusion.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2895\n\n",
    "created_at": "2008-04-12T11:20:24Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] add support for Laurent polynomials in Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2895",
    "user": "mhansen"
}
```
Assignee: somebody

David Roe did the initial implementation, and Jason Bandlow and I cleaned it up and got it ready for inclusion.

Issue created by migration from https://trac.sagemath.org/ticket/2895





---

archive/issue_comments_019913.json:
```json
{
    "body": "Applying this to my alpha4 merge tree I get a bunch of doctest failures:\n\n```\n        sage -t -long devel/sage/sage/schemes/generic/morphism.py # 2 doctests failed\n        sage -t -long devel/sage/sage/rings/polynomial/pbori.pyx # 1 doctests failed\n        sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_element.py # 4 doctests failed\n        sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py # 2 doctests failed\n        sage -t -long devel/sage/sage/rings/quotient_ring_element.pyx # 9 doctests failed\n        sage -t -long devel/sage/sage/rings/ring.pyx # 5 doctests failed\n        sage -t -long devel/sage/sage/rings/quotient_ring_element.py # 13 doctests failed\n        sage -t -long devel/sage/sage/rings/quotient_ring.py # 16 doctests failed\n        sage -t -long devel/sage/sage/rings/morphism.pyx # 11 doctests failed\n        sage -t -long devel/sage/sage/rings/homset.py # 5 doctests failed\n        sage -t -long devel/sage/sage/ext/interactive_constructors_c.pyx # 4 doctests failed\n```\n\nThe issue in most of not all cases seems to be:\n\n```\nAttributeError: 'QuotientRing_generic' object has no attribute '_print_element'\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-04-13T02:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2895#issuecomment-19913",
    "user": "mabshoff"
}
```

Applying this to my alpha4 merge tree I get a bunch of doctest failures:

```
        sage -t -long devel/sage/sage/schemes/generic/morphism.py # 2 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/pbori.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_element.py # 4 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py # 2 doctests failed
        sage -t -long devel/sage/sage/rings/quotient_ring_element.pyx # 9 doctests failed
        sage -t -long devel/sage/sage/rings/ring.pyx # 5 doctests failed
        sage -t -long devel/sage/sage/rings/quotient_ring_element.py # 13 doctests failed
        sage -t -long devel/sage/sage/rings/quotient_ring.py # 16 doctests failed
        sage -t -long devel/sage/sage/rings/morphism.pyx # 11 doctests failed
        sage -t -long devel/sage/sage/rings/homset.py # 5 doctests failed
        sage -t -long devel/sage/sage/ext/interactive_constructors_c.pyx # 4 doctests failed
```

The issue in most of not all cases seems to be:

```
AttributeError: 'QuotientRing_generic' object has no attribute '_print_element'
```


Cheers,

Michael



---

archive/issue_comments_019914.json:
```json
{
    "body": "If the base ring is a field of rational functions \nin another indeterminate I encounter a problem:\n\nsage: P.<q>=QQ[]\nsage: F = FractionField(P)\nsage: R.<x,y> = LaurentPolynomialRing(F,2); R\nMultivariate Laurent Polynomial Ring in x, y over Fraction Field of Univariate Polynomial Ring in q over Rational Field\nsage: (x+1/y)^2\n\nThis would work if F = QQ but not for this field of fractions.\n\n<type 'exceptions.TypeError'>: unsupported operand parent(s) for '/': 'Integer Ring' and 'Multivariate Laurent Polynomial Ring in x, y over Fraction Field of Univariate Polynomial Ring in q over Rational Field'",
    "created_at": "2008-04-13T03:19:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2895#issuecomment-19914",
    "user": "bump"
}
```

If the base ring is a field of rational functions 
in another indeterminate I encounter a problem:

sage: P.<q>=QQ[]
sage: F = FractionField(P)
sage: R.<x,y> = LaurentPolynomialRing(F,2); R
Multivariate Laurent Polynomial Ring in x, y over Fraction Field of Univariate Polynomial Ring in q over Rational Field
sage: (x+1/y)^2

This would work if F = QQ but not for this field of fractions.

<type 'exceptions.TypeError'>: unsupported operand parent(s) for '/': 'Integer Ring' and 'Multivariate Laurent Polynomial Ring in x, y over Fraction Field of Univariate Polynomial Ring in q over Rational Field'



---

archive/issue_comments_019915.json:
```json
{
    "body": "To elaborate, 1/y raises an error if the base ring is ZZ, a polynomial\nring or a field of fractions of a polynomial ring.\n\nHOWEVER y^(-1) can be used in its place, and no error result.\n\nThis may be acceptable.",
    "created_at": "2008-04-13T04:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2895#issuecomment-19915",
    "user": "bump"
}
```

To elaborate, 1/y raises an error if the base ring is ZZ, a polynomial
ring or a field of fractions of a polynomial ring.

HOWEVER y^(-1) can be used in its place, and no error result.

This may be acceptable.



---

archive/issue_comments_019916.json:
```json
{
    "body": "Regarding the exceptions in schemes/generic/morphisms.py that mabshoff reported\nI can confirm that they appear if only the patch 2895.1 is applied to unaltered\nalpha3.",
    "created_at": "2008-04-13T04:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2895#issuecomment-19916",
    "user": "bump"
}
```

Regarding the exceptions in schemes/generic/morphisms.py that mabshoff reported
I can confirm that they appear if only the patch 2895.1 is applied to unaltered
alpha3.



---

archive/issue_comments_019917.json:
```json
{
    "body": "Here's what appears to have happened. The old QuotientRingElement is in\nrings/quotient_ring_element.py and it contains the following:\n\n\n```\n    def _repr_(self):\n        from sage.structure.parent_gens import localvars\n        P = self.parent()\n        R = P.cover_ring()\n        # We print by temporarily (and safely!) changing the variable\n        # names of the covering structure R to those of P.\n        # These names get changed back, since we're using \"with\".\n        with localvars(R, P.variable_names(), normalize=False):\n            return str(self.__rep)\n```\n\n\nThe new version is in the file quotient_ring_elements.pyx. The\nabove code will not work in cython. In its place, we find:\n\n\n```\n     def _repr_(self):\n         self._reduce_()\n         return self.parent()._print_element(self)\n```\n\n\nBut the parent quotient ring has no method _print_element.",
    "created_at": "2008-04-13T20:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2895#issuecomment-19917",
    "user": "bump"
}
```

Here's what appears to have happened. The old QuotientRingElement is in
rings/quotient_ring_element.py and it contains the following:


```
    def _repr_(self):
        from sage.structure.parent_gens import localvars
        P = self.parent()
        R = P.cover_ring()
        # We print by temporarily (and safely!) changing the variable
        # names of the covering structure R to those of P.
        # These names get changed back, since we're using "with".
        with localvars(R, P.variable_names(), normalize=False):
            return str(self.__rep)
```


The new version is in the file quotient_ring_elements.pyx. The
above code will not work in cython. In its place, we find:


```
     def _repr_(self):
         self._reduce_()
         return self.parent()._print_element(self)
```


But the parent quotient ring has no method _print_element.



---

archive/issue_comments_019918.json:
```json
{
    "body": "Attachment [2895-2.patch](tarball://root/attachments/some-uuid/ticket2895/2895-2.patch) by mhansen created at 2008-04-18 05:38:22",
    "created_at": "2008-04-18T05:38:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2895#issuecomment-19918",
    "user": "mhansen"
}
```

Attachment [2895-2.patch](tarball://root/attachments/some-uuid/ticket2895/2895-2.patch) by mhansen created at 2008-04-18 05:38:22



---

archive/issue_comments_019919.json:
```json
{
    "body": "I put up some new patches which remove the conversion of quotient_ring_element.py to Cython.",
    "created_at": "2008-04-18T05:40:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2895#issuecomment-19919",
    "user": "mhansen"
}
```

I put up some new patches which remove the conversion of quotient_ring_element.py to Cython.



---

archive/issue_comments_019920.json:
```json
{
    "body": "The new patch passes doctests when applied against my 3.0.alpha6 merged tree. Now we need a positive review to get this merged.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-18T07:14:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2895#issuecomment-19920",
    "user": "mabshoff"
}
```

The new patch passes doctests when applied against my 3.0.alpha6 merged tree. Now we need a positive review to get this merged.

Cheers,

Michael



---

archive/issue_comments_019921.json:
```json
{
    "body": "An issue with putting this patch in close to release of 3.0 is whether it could break anything. Revised by mhansen it does not convert quotient_polynomial_element to cython as the previous patch did. Moreover after importing both revised 2895-1.patch and 2895-2.patch I read the diffs carefully and there is nothing that alters any existing functionality. So the patch is safe from this point of view.\n\nI tested it and it seems to work as it should.\n\nI don't think substitution is working yet. In a multivariate polynomial ring you can do:\nsage: g=(q+u)*(q+v)\nsage: g.substitute(u=1)\n(q + 1)*v + q^2 + q\nIn the Laurent polynomial ring this raises an exception.\n\nThis is not a reason not to include the patch. Substitution can be implemented later. \n\nI recommend acceptance.",
    "created_at": "2008-04-18T15:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2895#issuecomment-19921",
    "user": "bump"
}
```

An issue with putting this patch in close to release of 3.0 is whether it could break anything. Revised by mhansen it does not convert quotient_polynomial_element to cython as the previous patch did. Moreover after importing both revised 2895-1.patch and 2895-2.patch I read the diffs carefully and there is nothing that alters any existing functionality. So the patch is safe from this point of view.

I tested it and it seems to work as it should.

I don't think substitution is working yet. In a multivariate polynomial ring you can do:
sage: g=(q+u)*(q+v)
sage: g.substitute(u=1)
(q + 1)*v + q^2 + q
In the Laurent polynomial ring this raises an exception.

This is not a reason not to include the patch. Substitution can be implemented later. 

I recommend acceptance.



---

archive/issue_comments_019922.json:
```json
{
    "body": "Attachment [2895-subs.patch](tarball://root/attachments/some-uuid/ticket2895/2895-subs.patch) by mhansen created at 2008-04-18 18:55:05",
    "created_at": "2008-04-18T18:55:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2895#issuecomment-19922",
    "user": "mhansen"
}
```

Attachment [2895-subs.patch](tarball://root/attachments/some-uuid/ticket2895/2895-subs.patch) by mhansen created at 2008-04-18 18:55:05



---

archive/issue_comments_019923.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-18T18:56:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2895#issuecomment-19923",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_019924.json:
```json
{
    "body": "I've added a patch which makes .substitute() work and .subs() work with dictionary arguments.",
    "created_at": "2008-04-18T18:56:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2895#issuecomment-19924",
    "user": "mhansen"
}
```

I've added a patch which makes .substitute() work and .subs() work with dictionary arguments.



---

archive/issue_comments_019925.json:
```json
{
    "body": "Changing assignee from somebody to mhansen.",
    "created_at": "2008-04-18T18:56:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2895#issuecomment-19925",
    "user": "mhansen"
}
```

Changing assignee from somebody to mhansen.



---

archive/issue_comments_019926.json:
```json
{
    "body": "Substitution works if the ground ring is QQ but the\nfollowing returns an exception:\n\n```\nsage: R.<q>=QQ[]\nsage: L.<x,y,z> = LaurentPolynomialRing(R)\nsage: f=(x+y+z^-1)^2\nsage: f.substitute(z=1)\n```\n\nI repeat that my review is positive and I'd urge these patches to be merged in alpha6.",
    "created_at": "2008-04-18T19:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2895#issuecomment-19926",
    "user": "bump"
}
```

Substitution works if the ground ring is QQ but the
following returns an exception:

```
sage: R.<q>=QQ[]
sage: L.<x,y,z> = LaurentPolynomialRing(R)
sage: f=(x+y+z^-1)^2
sage: f.substitute(z=1)
```

I repeat that my review is positive and I'd urge these patches to be merged in alpha6.



---

archive/issue_comments_019927.json:
```json
{
    "body": "Thanks for testing this out Dan. \n\nThe underlying problem is with coercing between elements of a fraction field and the Laurent polynomial ring.  I'm not familiar enough with the coercion system so I'll send an email to David Roe since he probably knows exactly how to fix it.",
    "created_at": "2008-04-18T19:27:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2895#issuecomment-19927",
    "user": "mhansen"
}
```

Thanks for testing this out Dan. 

The underlying problem is with coercing between elements of a fraction field and the Laurent polynomial ring.  I'm not familiar enough with the coercion system so I'll send an email to David Roe since he probably knows exactly how to fix it.



---

archive/issue_comments_019928.json:
```json
{
    "body": "Ok, I consider this a positive review by Dan Bump and will merge this as is into 3.0.alpha6.\n\nMike: can you open a ticket for the coercion issue and make it a blocker for 3.0. We might get the patch in if David or somebody else comes up with patch in time. If not there is still 3.0.x ;)",
    "created_at": "2008-04-18T20:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2895#issuecomment-19928",
    "user": "mabshoff"
}
```

Ok, I consider this a positive review by Dan Bump and will merge this as is into 3.0.alpha6.

Mike: can you open a ticket for the coercion issue and make it a blocker for 3.0. We might get the patch in if David or somebody else comes up with patch in time. If not there is still 3.0.x ;)



---

archive/issue_comments_019929.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-18T20:22:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2895#issuecomment-19929",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019930.json:
```json
{
    "body": "Merged in Sage 3.0.alpha6",
    "created_at": "2008-04-18T20:22:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2895#issuecomment-19930",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha6
