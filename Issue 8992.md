# Issue 8992: Coercion of univariate quotient polynomial rings

archive/issues_008992.json:
```json
{
    "body": "Assignee: @robertwb\n\nKeywords: coercion quotient ring\n\nConsider the following setting:\n\n```\nsage: P.<x> = QQ[]\nsage: Q1 = P.quo([(x^2+1)^2*(x^2-3)])\nsage: Q2 = P.quo([(x^2+1)^2*(x^5+3)])\n```\n\n\nThe gcd of the moduli is `(x<sup>2+1)</sup>2`, and so it should be true that the pushout of Q1 and Q2 is the quotient ring with this gcd as modulus. Currently, the pushout raises an error, but with #8800 one has:\n\n```\nsage: from sage.categories.pushout import pushout\nsage: Q = pushout(Q1,Q2); Q\nUnivariate Quotient Polynomial Ring in xbar over Rational Field with modulus x^4 + 2*x^2 + 1\n```\n\n\nHowever, there remain two bugs that are not covered in #8800 and that prevent a proper coercion of Q1 and Q2.\n\nFirst bug:\n\n```\nsage: Q.has_coerce_map_from(Q1)\nFalse\nsage: Q.has_coerce_map_from(Q2)\nFalse\n```\n\n\nSecond bug:\n\n```\nsage: Q(Q1.gen())\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (932, 0))\n\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (932, 0))\n\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/king/SAGE/sage-4.3.1/devel/<ipython console> in <module>()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_quotient_ring.pyc in __call__(self, x)\n    272                 return PolynomialQuotientRingElement(self, self.__ring(x.lift()), check=False)\n    273         return PolynomialQuotientRingElement(\n--> 274                         self, self.__ring(x) , check=True)\n    275\n    276     def _is_valid_homomorphism_(self, codomain, im_gens):\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.pyc in _element_constructor_(self, x, check, is_gen, construct, **kwds)\n    310                 x = x.Polrev()\n    311\n--> 312         return C(self, x, check, is_gen, construct=construct, **kwds)\n    313\n    314     def is_integral_domain(self, proof = True):\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element_generic.pyc in __init__(self, parent, x, check, is_gen, construct)\n    654\n    655         if check:\n--> 656             x = [QQ(z) for z in x]\n    657\n    658         self.__list = list(x)\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:5781)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:7052)()\n\nTypeError: Unable to coerce xbar (<class 'sage.rings.polynomial.polynomial_quotient_ring_element.PolynomialQuotientRingElement'>) to Rational\nsage: Q.gen()\nxbar\n```\n\n\nIt could be that the following is an additional bug, but perhaps it is just a special case of the previous:\n\n```\nsage: Q(str(Q.gen()))\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (932, 0))\n\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (932, 0))\n\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/king/SAGE/sage-4.3.1/devel/<ipython console> in <module>()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_quotient_ring.pyc in __call__(self, x)\n    272                 return PolynomialQuotientRingElement(self, self.__ring(x.lift()), check=False)\n    273         return PolynomialQuotientRingElement(\n--> 274                         self, self.__ring(x) , check=True)\n    275\n    276     def _is_valid_homomorphism_(self, codomain, im_gens):\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.pyc in _element_constructor_(self, x, check, is_gen, construct, **kwds)\n    297                 R = self.base_ring()\n    298                 p = Parser(Integer, R, LookupNameMaker({self.variable_name(): self.gen()}, R))\n--> 299                 return self(p.parse(x))\n    300             except NameError:\n    301                 raise TypeError,\"Unable to coerce string\"\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.parse (sage/misc/parser.c:3481)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.parse (sage/misc/parser.c:3345)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_eqn (sage/misc/parser.c:5136)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_expr (sage/misc/parser.c:5456)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_term (sage/misc/parser.c:5681)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_factor (sage/misc/parser.c:6044)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_power (sage/misc/parser.c:6158)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_atom (sage/misc/parser.c:6711)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.LookupNameMaker.__call__ (sage/misc/parser.c:7653)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:5781)()\n\n/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:6517)()\n\nTypeError: unable to convert xbar to a rational\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8992\n\n",
    "created_at": "2010-05-19T10:26:01Z",
    "labels": [
        "coercion",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.6",
    "title": "Coercion of univariate quotient polynomial rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8992",
    "user": "@simon-king-jena"
}
```
Assignee: @robertwb

Keywords: coercion quotient ring

Consider the following setting:

```
sage: P.<x> = QQ[]
sage: Q1 = P.quo([(x^2+1)^2*(x^2-3)])
sage: Q2 = P.quo([(x^2+1)^2*(x^5+3)])
```


The gcd of the moduli is `(x<sup>2+1)</sup>2`, and so it should be true that the pushout of Q1 and Q2 is the quotient ring with this gcd as modulus. Currently, the pushout raises an error, but with #8800 one has:

```
sage: from sage.categories.pushout import pushout
sage: Q = pushout(Q1,Q2); Q
Univariate Quotient Polynomial Ring in xbar over Rational Field with modulus x^4 + 2*x^2 + 1
```


However, there remain two bugs that are not covered in #8800 and that prevent a proper coercion of Q1 and Q2.

First bug:

```
sage: Q.has_coerce_map_from(Q1)
False
sage: Q.has_coerce_map_from(Q2)
False
```


Second bug:

```
sage: Q(Q1.gen())
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (932, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (932, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/king/SAGE/sage-4.3.1/devel/<ipython console> in <module>()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_quotient_ring.pyc in __call__(self, x)
    272                 return PolynomialQuotientRingElement(self, self.__ring(x.lift()), check=False)
    273         return PolynomialQuotientRingElement(
--> 274                         self, self.__ring(x) , check=True)
    275
    276     def _is_valid_homomorphism_(self, codomain, im_gens):

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.pyc in _element_constructor_(self, x, check, is_gen, construct, **kwds)
    310                 x = x.Polrev()
    311
--> 312         return C(self, x, check, is_gen, construct=construct, **kwds)
    313
    314     def is_integral_domain(self, proof = True):

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element_generic.pyc in __init__(self, parent, x, check, is_gen, construct)
    654
    655         if check:
--> 656             x = [QQ(z) for z in x]
    657
    658         self.__list = list(x)

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:5781)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:7052)()

TypeError: Unable to coerce xbar (<class 'sage.rings.polynomial.polynomial_quotient_ring_element.PolynomialQuotientRingElement'>) to Rational
sage: Q.gen()
xbar
```


It could be that the following is an additional bug, but perhaps it is just a special case of the previous:

```
sage: Q(str(Q.gen()))
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (932, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (932, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/king/SAGE/sage-4.3.1/devel/<ipython console> in <module>()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_quotient_ring.pyc in __call__(self, x)
    272                 return PolynomialQuotientRingElement(self, self.__ring(x.lift()), check=False)
    273         return PolynomialQuotientRingElement(
--> 274                         self, self.__ring(x) , check=True)
    275
    276     def _is_valid_homomorphism_(self, codomain, im_gens):

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.pyc in _element_constructor_(self, x, check, is_gen, construct, **kwds)
    297                 R = self.base_ring()
    298                 p = Parser(Integer, R, LookupNameMaker({self.variable_name(): self.gen()}, R))
--> 299                 return self(p.parse(x))
    300             except NameError:
    301                 raise TypeError,"Unable to coerce string"

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.parse (sage/misc/parser.c:3481)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.parse (sage/misc/parser.c:3345)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_eqn (sage/misc/parser.c:5136)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_expr (sage/misc/parser.c:5456)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_term (sage/misc/parser.c:5681)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_factor (sage/misc/parser.c:6044)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_power (sage/misc/parser.c:6158)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_atom (sage/misc/parser.c:6711)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.LookupNameMaker.__call__ (sage/misc/parser.c:7653)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:5781)()

/home/king/SAGE/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:6517)()

TypeError: unable to convert xbar to a rational
```


Issue created by migration from https://trac.sagemath.org/ticket/8992





---

archive/issue_comments_083125.json:
```json
{
    "body": "The quotient rings implement their own call method, instead of implementing _element_constructor_. I guess this is where I should start.",
    "created_at": "2010-05-19T10:54:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83125",
    "user": "@simon-king-jena"
}
```

The quotient rings implement their own call method, instead of implementing _element_constructor_. I guess this is where I should start.



---

archive/issue_comments_083126.json:
```json
{
    "body": "I think I found one source of the problem. The call method (that will become an element_constructor method) says:\n\n```\n        if isinstance(x, PolynomialQuotientRingElement):\n            P = x.parent()\n            if P is self:\n                return x\n            elif P == self:\n                return PolynomialQuotientRingElement(self, self.__ring(x.lift()), check=False)\n```\n\n\nIn other words: *Only* if the parent of x is equal to self, it is attempted to convert x into self via conversion in the polynomial ring. I think this condition should simply be dropped.\n\nFurthermore, after the above code block\n\n```\n        return PolynomialQuotientRingElement(self, self.__ring(x) , check=True)\n```\n\nHence, it is again tried to interprete x in the polynomial ring of self. But the problem is that the variable names in self and in `self.__ring` are usually different. So, conversion of strings must fail.",
    "created_at": "2010-05-19T11:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83126",
    "user": "@simon-king-jena"
}
```

I think I found one source of the problem. The call method (that will become an element_constructor method) says:

```
        if isinstance(x, PolynomialQuotientRingElement):
            P = x.parent()
            if P is self:
                return x
            elif P == self:
                return PolynomialQuotientRingElement(self, self.__ring(x.lift()), check=False)
```


In other words: *Only* if the parent of x is equal to self, it is attempted to convert x into self via conversion in the polynomial ring. I think this condition should simply be dropped.

Furthermore, after the above code block

```
        return PolynomialQuotientRingElement(self, self.__ring(x) , check=True)
```

Hence, it is again tried to interprete x in the polynomial ring of self. But the problem is that the variable names in self and in `self.__ring` are usually different. So, conversion of strings must fail.



---

archive/issue_comments_083127.json:
```json
{
    "body": "A side remark: I just noticed that univariate quotient rings have no representation in Singular. I guess this will be on a different ticket, though.",
    "created_at": "2010-05-19T12:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83127",
    "user": "@simon-king-jena"
}
```

A side remark: I just noticed that univariate quotient rings have no representation in Singular. I guess this will be on a different ticket, though.



---

archive/issue_comments_083128.json:
```json
{
    "body": "Attachment [8992_coercion_for_polynomial_quotient_rings.patch](tarball://root/attachments/some-uuid/ticket8992/8992_coercion_for_polynomial_quotient_rings.patch) by @simon-king-jena created at 2010-05-19 13:36:43\n\n_element_constructor_ and _coerce_map_from_ for polynomial quotient rings; may depend on #8800",
    "created_at": "2010-05-19T13:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83128",
    "user": "@simon-king-jena"
}
```

Attachment [8992_coercion_for_polynomial_quotient_rings.patch](tarball://root/attachments/some-uuid/ticket8992/8992_coercion_for_polynomial_quotient_rings.patch) by @simon-king-jena created at 2010-05-19 13:36:43

_element_constructor_ and _coerce_map_from_ for polynomial quotient rings; may depend on #8800



---

archive/issue_comments_083129.json:
```json
{
    "body": "OK, I have a ticket. I worked on top of my patches for #8807 and #8800, but *if* this new patch applies then it should be stand-alone (simply try).\n\nWhat does it provide?\n\n1. Polynomial quotient rings had a call method instead of an _element_constructor_. My patch provides one.\n\n2. Previously, a coercion between polynomial quotient rings was not used, even though it clearly should exist when the modulus of the codomain divides the modulus of the domain. This is now solved, by adding a _coerce_map_from_ method.\n\n3. The old call method relied on the variable names of the underlying polynomial ring, when processing a string. That's obviously wrong, because the variable names of the *quotient* ring may be different.\n\n4. String evaluation is possible even when one has a polynomial quotient ring over a polynomial ring (example below). This is possible by using `GenDictWithBasering`, which I had originally introduced for infinite polynomial rings.\n\n**__Examples__**\n\nConversion between two quotient rings (coercion exists only in one direction):\n\n```\nsage: P.<x> = QQ[]\nsage: Q1 = P.quo([(x^2+1)^2*(x^2-3)])\nsage: Q2 = P.quo([(x^2+1)^2])\nsage: Q2(Q1.gen())\nxbar\nsage: Q1(Q2.gen())\nxbar\nsage: Q1.has_coerce_map_from(Q2)\nFalse\nsage: Q2.has_coerce_map_from(Q1)\nTrue\n```\n\n\nHere the underlying polynomial ring has a basering that by itself is a polynomial ring:\n\n```\nsage: R.<y> = P[]\nsage: Q3 = R.quo([(y^2+1)]); Q3\nUnivariate Quotient Polynomial Ring in ybar over Univariate Polynomial Ring in x over Rational Field with modulus y^2 + 1\nsage: Q3(Q1.gen())  # this uses the lift into the underlying polynomial ring\nx\n```\n\n\nString evaluation works (if you think about it, this is non-trivial, since it involves generator names of both Q3 and R):\n\n```\nsage: Q3('x*ybar^2')\n-x\n```\n\n\nNow, back to the example from the ticket description. If #8807 and #8800 are used as well, one obtains:\n\n```\nsage: P.<x> = QQ[]\nsage: Q1 = P.quo([(x^2+1)^2*(x^2-3)])\nsage: Q2 = P.quo([(x^2+1)^2*(x^5+3)])\nsage: Q1.gen()^2*Q2.gen()^2 + 2*Q1.gen()^2 + 1\n0\nsage: (Q1.gen()^2*Q2.gen()^2 + 2*Q1.gen()^2 + 1).parent()\nUnivariate Quotient Polynomial Ring in xbar over Rational Field with modulus x^4 + 2*x^2 + 1\n```\n\n\nI just realise that I forgot to provide a doc test for _coerce_map_from_. I will post it in a few minutes, and then it's ready for review!",
    "created_at": "2010-05-19T14:01:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83129",
    "user": "@simon-king-jena"
}
```

OK, I have a ticket. I worked on top of my patches for #8807 and #8800, but *if* this new patch applies then it should be stand-alone (simply try).

What does it provide?

1. Polynomial quotient rings had a call method instead of an _element_constructor_. My patch provides one.

2. Previously, a coercion between polynomial quotient rings was not used, even though it clearly should exist when the modulus of the codomain divides the modulus of the domain. This is now solved, by adding a _coerce_map_from_ method.

3. The old call method relied on the variable names of the underlying polynomial ring, when processing a string. That's obviously wrong, because the variable names of the *quotient* ring may be different.

4. String evaluation is possible even when one has a polynomial quotient ring over a polynomial ring (example below). This is possible by using `GenDictWithBasering`, which I had originally introduced for infinite polynomial rings.

**__Examples__**

Conversion between two quotient rings (coercion exists only in one direction):

```
sage: P.<x> = QQ[]
sage: Q1 = P.quo([(x^2+1)^2*(x^2-3)])
sage: Q2 = P.quo([(x^2+1)^2])
sage: Q2(Q1.gen())
xbar
sage: Q1(Q2.gen())
xbar
sage: Q1.has_coerce_map_from(Q2)
False
sage: Q2.has_coerce_map_from(Q1)
True
```


Here the underlying polynomial ring has a basering that by itself is a polynomial ring:

```
sage: R.<y> = P[]
sage: Q3 = R.quo([(y^2+1)]); Q3
Univariate Quotient Polynomial Ring in ybar over Univariate Polynomial Ring in x over Rational Field with modulus y^2 + 1
sage: Q3(Q1.gen())  # this uses the lift into the underlying polynomial ring
x
```


String evaluation works (if you think about it, this is non-trivial, since it involves generator names of both Q3 and R):

```
sage: Q3('x*ybar^2')
-x
```


Now, back to the example from the ticket description. If #8807 and #8800 are used as well, one obtains:

```
sage: P.<x> = QQ[]
sage: Q1 = P.quo([(x^2+1)^2*(x^2-3)])
sage: Q2 = P.quo([(x^2+1)^2*(x^5+3)])
sage: Q1.gen()^2*Q2.gen()^2 + 2*Q1.gen()^2 + 1
0
sage: (Q1.gen()^2*Q2.gen()^2 + 2*Q1.gen()^2 + 1).parent()
Univariate Quotient Polynomial Ring in xbar over Rational Field with modulus x^4 + 2*x^2 + 1
```


I just realise that I forgot to provide a doc test for _coerce_map_from_. I will post it in a few minutes, and then it's ready for review!



---

archive/issue_comments_083130.json:
```json
{
    "body": "Attachment [8992_test_for_coerce_map_from.patch](tarball://root/attachments/some-uuid/ticket8992/8992_test_for_coerce_map_from.patch) by @simon-king-jena created at 2010-05-19 14:07:20\n\nAdditional doc test; to be applied after the previous patch",
    "created_at": "2010-05-19T14:07:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83130",
    "user": "@simon-king-jena"
}
```

Attachment [8992_test_for_coerce_map_from.patch](tarball://root/attachments/some-uuid/ticket8992/8992_test_for_coerce_map_from.patch) by @simon-king-jena created at 2010-05-19 14:07:20

Additional doc test; to be applied after the previous patch



---

archive/issue_comments_083131.json:
```json
{
    "body": "OK, the doc test is added (testing coercion from a polynomial ring to a quotient ring and between two quotient rings). Ready for review!",
    "created_at": "2010-05-19T14:08:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83131",
    "user": "@simon-king-jena"
}
```

OK, the doc test is added (testing coercion from a polynomial ring to a quotient ring and between two quotient rings). Ready for review!



---

archive/issue_comments_083132.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-19T14:08:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83132",
    "user": "@simon-king-jena"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083133.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-03-11T19:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83133",
    "user": "@loefflerd"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_083134.json:
```json
{
    "body": "Afraid this one has bitrotted -- it needs a rebase.",
    "created_at": "2012-03-11T19:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83134",
    "user": "@loefflerd"
}
```

Afraid this one has bitrotted -- it needs a rebase.



---

archive/issue_comments_083135.json:
```json
{
    "body": "Apparently, all but the last problem mentioned in the ticket description have already been fixed in other tickets. Namely, with vanilla sage-5.0.beta7, one has\n\n```\nsage: P.<x> = QQ[]\nsage: Q1 = P.quo([(x^2+1)^2*(x^2-3)])\nsage: Q2 = P.quo([(x^2+1)^2*(x^5+3)])\nsage: from sage.categories.pushout import pushout\nsage: Q = pushout(Q1,Q2); Q\nUnivariate Quotient Polynomial Ring in xbar over Rational Field with modulus x^4 + 2*x^2 + 1\nsage: Q.has_coerce_map_from(Q1)\nTrue\nsage: Q.has_coerce_map_from(Q2)\nTrue\nsage: Q(Q1.gen())\nxbar\nsage: Q(str(Q.gen()))\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (2068, 0))\n\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (2068, 0))\n\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (2068, 0))\n\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n...\n\nTypeError: unable to convert xbar to a rational\n```\n\n\nAlso, the `__call__` method of quotient rings has already been replaced by an `_element_constructor_`, as it should.\n\nSo, I wouldn't say that the patch needs to be rebased: It has to be rewritten,  or better, it needs to be reduced to those parts that are responsible for making a quotient ring understand the string representation of its generators.",
    "created_at": "2012-03-11T21:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83135",
    "user": "@simon-king-jena"
}
```

Apparently, all but the last problem mentioned in the ticket description have already been fixed in other tickets. Namely, with vanilla sage-5.0.beta7, one has

```
sage: P.<x> = QQ[]
sage: Q1 = P.quo([(x^2+1)^2*(x^2-3)])
sage: Q2 = P.quo([(x^2+1)^2*(x^5+3)])
sage: from sage.categories.pushout import pushout
sage: Q = pushout(Q1,Q2); Q
Univariate Quotient Polynomial Ring in xbar over Rational Field with modulus x^4 + 2*x^2 + 1
sage: Q.has_coerce_map_from(Q1)
True
sage: Q.has_coerce_map_from(Q2)
True
sage: Q(Q1.gen())
xbar
sage: Q(str(Q.gen()))
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (2068, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (2068, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (2068, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...

TypeError: unable to convert xbar to a rational
```


Also, the `__call__` method of quotient rings has already been replaced by an `_element_constructor_`, as it should.

So, I wouldn't say that the patch needs to be rebased: It has to be rewritten,  or better, it needs to be reduced to those parts that are responsible for making a quotient ring understand the string representation of its generators.



---

archive/issue_comments_083136.json:
```json
{
    "body": "Currently, I can not produce patch that would cover all examples from this ticket. The reason is another bug:\n\n```\nsage: P.<y> = QQ['x'][]\nsage: y.divides(y)\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/simon/SAGE/sage-5.0.beta7/<ipython console> in <module>()\n\n/home/simon/SAGE/sage-5.0.beta7/local/lib/python2.7/site-packages/sage/structure/element.so in sage.structure.element.CommutativeRingElement.divides (sage/structure/element.c:14887)()\n\n/home/simon/SAGE/sage-5.0.beta7/local/lib/python2.7/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.__mod__ (sage/rings/polynomial/polynomial_element.c:15562)()\n\n/home/simon/SAGE/sage-5.0.beta7/local/lib/python2.7/site-packages/sage/structure/element.so in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2919)()\n\n/home/simon/SAGE/sage-5.0.beta7/local/lib/python2.7/site-packages/sage/structure/parent.so in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:3302)()\n\nAttributeError: 'sage.rings.polynomial.polynomial_element.Polynomial_generic_dense' object has no attribute 'quo_rem'\n```\n\n\nThat bug also exists in sage-4.6.2, but apparently it has not been present when I wrote the old patch.\n\nAnyway, I think that bug could be fixed here, I see no need to open yet another ticket.",
    "created_at": "2012-03-12T09:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83136",
    "user": "@simon-king-jena"
}
```

Currently, I can not produce patch that would cover all examples from this ticket. The reason is another bug:

```
sage: P.<y> = QQ['x'][]
sage: y.divides(y)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/simon/SAGE/sage-5.0.beta7/<ipython console> in <module>()

/home/simon/SAGE/sage-5.0.beta7/local/lib/python2.7/site-packages/sage/structure/element.so in sage.structure.element.CommutativeRingElement.divides (sage/structure/element.c:14887)()

/home/simon/SAGE/sage-5.0.beta7/local/lib/python2.7/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.__mod__ (sage/rings/polynomial/polynomial_element.c:15562)()

/home/simon/SAGE/sage-5.0.beta7/local/lib/python2.7/site-packages/sage/structure/element.so in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2919)()

/home/simon/SAGE/sage-5.0.beta7/local/lib/python2.7/site-packages/sage/structure/parent.so in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:3302)()

AttributeError: 'sage.rings.polynomial.polynomial_element.Polynomial_generic_dense' object has no attribute 'quo_rem'
```


That bug also exists in sage-4.6.2, but apparently it has not been present when I wrote the old patch.

Anyway, I think that bug could be fixed here, I see no need to open yet another ticket.



---

archive/issue_comments_083137.json:
```json
{
    "body": "The reason for my complaint about `y.divides(y)` is that the following example from a comment above would not work with the patch that I am now preparing:\n\n```\nsage: P.<x> = QQ[]\nsage: Q1 = P.quo([(x^2+1)^2*(x^2-3)])\nsage: R.<y> = P[]\nsage: Q3 = R.quo([(y^2+1)]); Q3\nUnivariate Quotient Polynomial Ring in ybar over Univariate Polynomial Ring in x over Rational Field with modulus y^2 + 1\nsage: Q3(Q1.gen())  # uses the lift from Q1 to P, which is the base ring of Q3\nx\n```\n\n\nThe problem is that the coercion framework is not able to find out whether `Q3` has a coerce map from `Q1`.\n\nSo, I guess I should add a \"try-except\" clause in `Q3._coerce_map_from_`, so that an error in division is caught and results in the answer \"no, there is no coerce map\".",
    "created_at": "2012-03-12T10:55:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83137",
    "user": "@simon-king-jena"
}
```

The reason for my complaint about `y.divides(y)` is that the following example from a comment above would not work with the patch that I am now preparing:

```
sage: P.<x> = QQ[]
sage: Q1 = P.quo([(x^2+1)^2*(x^2-3)])
sage: R.<y> = P[]
sage: Q3 = R.quo([(y^2+1)]); Q3
Univariate Quotient Polynomial Ring in ybar over Univariate Polynomial Ring in x over Rational Field with modulus y^2 + 1
sage: Q3(Q1.gen())  # uses the lift from Q1 to P, which is the base ring of Q3
x
```


The problem is that the coercion framework is not able to find out whether `Q3` has a coerce map from `Q1`.

So, I guess I should add a "try-except" clause in `Q3._coerce_map_from_`, so that an error in division is caught and results in the answer "no, there is no coerce map".



---

archive/issue_comments_083138.json:
```json
{
    "body": "I have produced a new patch.\n\nRecall that most problems mentioned in the ticket description have already been solved in sage-5.0.beta7. The only remaining was conversion from strings.\n\nHere, I suggest to use a tool that I have introduced in my code for infinite polynomial rings: It is a generalisation of the gens_dict of polynomial rings. In contrast to gens_dict, it not only considers the generator names of the ring, but it also considers (recursively) the generator names of the base ring. This recursive version of gens_dict is then passed to sage_eval.\n\nHence, if Q has generator 'xbar' and is the quotient ring of some polynomial ring P with generator 'x', then `Q('x*xbar')` will be correctly evaluated as `P.gen()*Q.gen()`, which in turn evaluates as `Q(P.gen())*Q.gen()`.\n\nConcerning the problem with `y.divides(...)`: The problem can arise, if Q1 and Q2 are two polynomial quotient rings and one asks `Q1.has_coerce_map_from(Q2)`. It will try to divide the moduli of Q1 and Q2. My suggestion is: If that division fails with an error, then there is no coerce map.\n\nAfter these changes, the tests in sage/rings/polynomial/polynomial_quotient_ring.py and .../polynomial_quotient_ring_element.py pass.\n\nLet's see if the patchbot finds a reason to complain...\n\nApply trac8992_conversion_polynomial_quotient_ring.patch",
    "created_at": "2012-03-12T19:41:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83138",
    "user": "@simon-king-jena"
}
```

I have produced a new patch.

Recall that most problems mentioned in the ticket description have already been solved in sage-5.0.beta7. The only remaining was conversion from strings.

Here, I suggest to use a tool that I have introduced in my code for infinite polynomial rings: It is a generalisation of the gens_dict of polynomial rings. In contrast to gens_dict, it not only considers the generator names of the ring, but it also considers (recursively) the generator names of the base ring. This recursive version of gens_dict is then passed to sage_eval.

Hence, if Q has generator 'xbar' and is the quotient ring of some polynomial ring P with generator 'x', then `Q('x*xbar')` will be correctly evaluated as `P.gen()*Q.gen()`, which in turn evaluates as `Q(P.gen())*Q.gen()`.

Concerning the problem with `y.divides(...)`: The problem can arise, if Q1 and Q2 are two polynomial quotient rings and one asks `Q1.has_coerce_map_from(Q2)`. It will try to divide the moduli of Q1 and Q2. My suggestion is: If that division fails with an error, then there is no coerce map.

After these changes, the tests in sage/rings/polynomial/polynomial_quotient_ring.py and .../polynomial_quotient_ring_element.py pass.

Let's see if the patchbot finds a reason to complain...

Apply trac8992_conversion_polynomial_quotient_ring.patch



---

archive/issue_comments_083139.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-03-12T19:41:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83139",
    "user": "@simon-king-jena"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083140.json:
```json
{
    "body": "Sorry, I should have mentioned that the patch is for 5.0.beta7, not for 4.8.",
    "created_at": "2012-03-12T20:15:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83140",
    "user": "@simon-king-jena"
}
```

Sorry, I should have mentioned that the patch is for 5.0.beta7, not for 4.8.



---

archive/issue_comments_083141.json:
```json
{
    "body": "Findings of the patchbot: It does apply to 5.0.beta7, the tests pass (except for one test that seems unrelated with my patch).\n\nNevertheless, I had to modify my patch, because it has added trailing white space. It should be fixed now.\n\nApply trac8992_conversion_polynomial_quotient_ring.patch",
    "created_at": "2012-03-12T20:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83141",
    "user": "@simon-king-jena"
}
```

Findings of the patchbot: It does apply to 5.0.beta7, the tests pass (except for one test that seems unrelated with my patch).

Nevertheless, I had to modify my patch, because it has added trailing white space. It should be fixed now.

Apply trac8992_conversion_polynomial_quotient_ring.patch



---

archive/issue_comments_083142.json:
```json
{
    "body": "There are a few typos in your patch: \"are no unique\", \"my lift an\", \"in principal\".",
    "created_at": "2012-03-12T21:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83142",
    "user": "@loefflerd"
}
```

There are a few typos in your patch: "are no unique", "my lift an", "in principal".



---

archive/issue_comments_083143.json:
```json
{
    "body": "Typos corrected, I hope!\n\nApply trac8992_conversion_polynomial_quotient_ring.patch",
    "created_at": "2012-03-13T06:21:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83143",
    "user": "@simon-king-jena"
}
```

Typos corrected, I hope!

Apply trac8992_conversion_polynomial_quotient_ring.patch



---

archive/issue_comments_083144.json:
```json
{
    "body": "This looks pretty good to me.  The one things I worry about is that the result of sage_eval may not actually belong to the correct parent.  I would put a check to make sure that it actually does.  Then, I think we can mark this as positive review.",
    "created_at": "2012-05-28T22:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83144",
    "user": "@mwhansen"
}
```

This looks pretty good to me.  The one things I worry about is that the result of sage_eval may not actually belong to the correct parent.  I would put a check to make sure that it actually does.  Then, I think we can mark this as positive review.



---

archive/issue_comments_083145.json:
```json
{
    "body": "Changing keywords from \"coercion quotient ring\" to \"coercion quotient ring sd40.5\".",
    "created_at": "2012-05-28T22:04:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83145",
    "user": "@mwhansen"
}
```

Changing keywords from "coercion quotient ring" to "coercion quotient ring sd40.5".



---

archive/issue_comments_083146.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-05-31T08:11:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83146",
    "user": "@simon-king-jena"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_083147.json:
```json
{
    "body": "Replying to [comment:15 mhansen]:\n> This looks pretty good to me.  The one things I worry about is that the result of sage_eval may not actually belong to the correct parent.  I would put a check to make sure that it actually does.  Then, I think we can mark this as positive review.\n\nAt the moment, we have some problem with converting a string that defines an element of the base ring:\n\n```\nsage: P.<x> = QQ[]\nsage: Q1 = P.quo([(x^2+1)^2*(x^2-3)])\nsage: Q2 = P.quo([(x^2+1)^2*(x^5+3)])\nsage: from sage.categories.pushout import pushout\nsage: Q = pushout(Q1,Q2); Q\nUnivariate Quotient Polynomial Ring in xbar over Rational Field with modulus x^4 + 2*x^2 + 1\nsage: Q(Q1.gen())\nxbar\nsage: sage: Q(str(Q.gen()))\nxbar\nsage: Q1(x)\nxbar\nsage: Q1('x')\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (2061, 0))\n\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (818, 0))\n\n---------------------------------------------------------------------------\nNameError                                 Traceback (most recent call last)\n\n/home/simon/SAGE/sage-5.0/devel/sage-main/<ipython console> in <module>()\n\n/home/simon/SAGE/sage-5.0/local/lib/python2.7/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:7941)()\n\n/home/simon/SAGE/sage-5.0/local/lib/python2.7/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3345)()\n\n/home/simon/SAGE/sage-5.0/local/lib/python2.7/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3248)()\n\n/home/simon/SAGE/sage-5.0/local/lib/python2.7/site-packages/sage/rings/polynomial/polynomial_quotient_ring.pyc in _element_constructor_(self, x)\n    419         # Interpretation in self has priority over interpretation in self.__ring\n    420         try:\n--> 421             return sage_eval(x, GenDictWithBasering(self,self.gens_dict()))\n    422         except TypeError, NameError:\n    423             pass\n\n/home/simon/SAGE/sage-5.0/local/lib/python2.7/site-packages/sage/misc/sage_eval.pyc in sage_eval(source, locals, cmds, preparse)\n    197         return locals['_sage_eval_returnval_']\n    198     else:\n--> 199         return eval(source, sage.all.__dict__, locals)\n    200     \n    201         \n\n/home/simon/SAGE/sage-5.0/local/lib/python2.7/site-packages/sage/all.pyc in <module>()\n\nNameError: name 'x' is not defined\n```\n\n\nI'd like to make that work as well, and then add a test for the correct parent.",
    "created_at": "2012-05-31T08:11:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83147",
    "user": "@simon-king-jena"
}
```

Replying to [comment:15 mhansen]:
> This looks pretty good to me.  The one things I worry about is that the result of sage_eval may not actually belong to the correct parent.  I would put a check to make sure that it actually does.  Then, I think we can mark this as positive review.

At the moment, we have some problem with converting a string that defines an element of the base ring:

```
sage: P.<x> = QQ[]
sage: Q1 = P.quo([(x^2+1)^2*(x^2-3)])
sage: Q2 = P.quo([(x^2+1)^2*(x^5+3)])
sage: from sage.categories.pushout import pushout
sage: Q = pushout(Q1,Q2); Q
Univariate Quotient Polynomial Ring in xbar over Rational Field with modulus x^4 + 2*x^2 + 1
sage: Q(Q1.gen())
xbar
sage: sage: Q(str(Q.gen()))
xbar
sage: Q1(x)
xbar
sage: Q1('x')
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (2061, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (818, 0))

---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home/simon/SAGE/sage-5.0/devel/sage-main/<ipython console> in <module>()

/home/simon/SAGE/sage-5.0/local/lib/python2.7/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:7941)()

/home/simon/SAGE/sage-5.0/local/lib/python2.7/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3345)()

/home/simon/SAGE/sage-5.0/local/lib/python2.7/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3248)()

/home/simon/SAGE/sage-5.0/local/lib/python2.7/site-packages/sage/rings/polynomial/polynomial_quotient_ring.pyc in _element_constructor_(self, x)
    419         # Interpretation in self has priority over interpretation in self.__ring
    420         try:
--> 421             return sage_eval(x, GenDictWithBasering(self,self.gens_dict()))
    422         except TypeError, NameError:
    423             pass

/home/simon/SAGE/sage-5.0/local/lib/python2.7/site-packages/sage/misc/sage_eval.pyc in sage_eval(source, locals, cmds, preparse)
    197         return locals['_sage_eval_returnval_']
    198     else:
--> 199         return eval(source, sage.all.__dict__, locals)
    200     
    201         

/home/simon/SAGE/sage-5.0/local/lib/python2.7/site-packages/sage/all.pyc in <module>()

NameError: name 'x' is not defined
```


I'd like to make that work as well, and then add a test for the correct parent.



---

archive/issue_comments_083148.json:
```json
{
    "body": "Replying to [comment:17 SimonKing]:\n> At the moment, we have some problem with converting a string that defines an element of the base ring\n\nSorry, I meant \"cover ring\".",
    "created_at": "2012-05-31T08:17:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83148",
    "user": "@simon-king-jena"
}
```

Replying to [comment:17 SimonKing]:
> At the moment, we have some problem with converting a string that defines an element of the base ring

Sorry, I meant "cover ring".



---

archive/issue_comments_083149.json:
```json
{
    "body": "Funny. The code was an attempt to convert into the cover ring. But it says\n\n```\n        try: \n            return sage_eval(x, GenDictWithBasering(self,self.gens_dict())) \n        except TypeError, NameError: \n            pass \n        try: \n            return PolynomialQuotientRingElement(self, self.__ring(x), check=False) \n        except TypeError: \n            raise TypeError, \"unable to convert %s into an element of %s\"%(x,repr(self))\n```\n\nIn the third line, the `NameError` raised by sage_eval is not caught, because I forgot brackets. Arrgh.",
    "created_at": "2012-05-31T08:26:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83149",
    "user": "@simon-king-jena"
}
```

Funny. The code was an attempt to convert into the cover ring. But it says

```
        try: 
            return sage_eval(x, GenDictWithBasering(self,self.gens_dict())) 
        except TypeError, NameError: 
            pass 
        try: 
            return PolynomialQuotientRingElement(self, self.__ring(x), check=False) 
        except TypeError: 
            raise TypeError, "unable to convert %s into an element of %s"%(x,repr(self))
```

In the third line, the `NameError` raised by sage_eval is not caught, because I forgot brackets. Arrgh.



---

archive/issue_comments_083150.json:
```json
{
    "body": "Mike, you are right, the wrong parent *can* occur:\n\n```\nsage: Q1('1')\n1\nsage: _.parent()\nInteger Ring\n```\n",
    "created_at": "2012-05-31T08:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83150",
    "user": "@simon-king-jena"
}
```

Mike, you are right, the wrong parent *can* occur:

```
sage: Q1('1')
1
sage: _.parent()
Integer Ring
```




---

archive/issue_comments_083151.json:
```json
{
    "body": "Attachment [trac8992_conversion_polynomial_quotient_ring.patch](tarball://root/attachments/some-uuid/ticket8992/trac8992_conversion_polynomial_quotient_ring.patch) by @simon-king-jena created at 2012-05-31 08:39:25\n\nNew patch, replacing the old patches",
    "created_at": "2012-05-31T08:39:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83151",
    "user": "@simon-king-jena"
}
```

Attachment [trac8992_conversion_polynomial_quotient_ring.patch](tarball://root/attachments/some-uuid/ticket8992/trac8992_conversion_polynomial_quotient_ring.patch) by @simon-king-jena created at 2012-05-31 08:39:25

New patch, replacing the old patches



---

archive/issue_comments_083152.json:
```json
{
    "body": "OK, the two issues discussed in the previous posts are fixed and became doc tests. Needs review.\n\nApply trac8992_conversion_polynomial_quotient_ring.patch",
    "created_at": "2012-05-31T08:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83152",
    "user": "@simon-king-jena"
}
```

OK, the two issues discussed in the previous posts are fixed and became doc tests. Needs review.

Apply trac8992_conversion_polynomial_quotient_ring.patch



---

archive/issue_comments_083153.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-05-31T08:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83153",
    "user": "@simon-king-jena"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083154.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-11-18T20:02:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83154",
    "user": "@tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083155.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2012-11-18T20:02:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83155",
    "user": "@tscrim"
}
```

Looks good to me.



---

archive/issue_comments_083156.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-12-17T12:58:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83156",
    "user": "@jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_083157.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-12-19T15:46:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8992#issuecomment-83157",
    "user": "@jdemeyer"
}
```

Resolution: fixed
