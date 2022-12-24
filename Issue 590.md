# Issue 590: document extended_rational_field.py

archive/issues_000590.json:
```json
{
    "body": "Assignee: @roed314\n\nThe rings/extended_rational_field.py file is terribly documented.  There are no doctests, no copyright notice, no author, etc.   I think David Roe wrote this:\n\nwas`@`ubuntu:~/d/sage/sage/rings$ sage -coverage extended_rational_field.py\n----------------------------------------------------------------------\nextended_rational_field.py\nERROR: Please define a s == loads(dumps(s)) doctest.\nOVERALL SCORE: 0%  (2 good, 71 bad)\n\nMissing documentation:\n* __init__(self)\n* _repr_(self)\n* _latex_(self)\n* __call__(self, x, base = 0)\n* _coerce_impl(self, x)\n* _is_valid_homomorphism(self, codomain, im_gens)\n* __iter__(self)\n* complex_embedding(self, prec=53)\n* gens(self)\n* gen(self, n=0)\n* is_prime_field(self)\n* ngens(self)\n* numberfield(self, poly_var, nf_var)\n* __init__(self, x = None, base = 0)\n* __cmp__(self, other)\n* copy(self)\n* lcm(self, other)\n* square_root(self)\n* nth_root(self)\n* _add_(self, right)\n* _sub_(self, right)\n* _neg_(self)\n* _mul_(self, right)\n* _div_(self, right)\n* __invert__(self)\n* __pow__(self, n)\n* __abs__(self)\n* floor(self)\n* ceil(self)\n* __lshift__(self, n)\n* __rshift__(self, n)\n* __init__(self)\n* __cmp__(self, other)\n* __repr__(self)\n* _latex_(self)\n* _add_(self, other)\n* _mul_(self, other)\n* _sub_(self, other)\n* _div_(self, other)\n* _neg_(self)\n* __invert__(self)\n* __abs__(self)\n* __pow__(self, right)\n* sqrt(self)\n* square_root(self)\n* nth_root(self, n)\n* floor(self)\n* ceil(self)\n* numerator(self)\n* denominator(self)\n* __init__(self)\n* __cmp__(self, other)\n* _repr_(self)\n* _latex_(self)\n* _add_(self, other)\n* _mul_(self, other)\n* _sub_(self, other)\n* _div_(self, other)\n* _neg_(self)\n* __invert__(self)\n* __abs__(self)\n* __pow__(self, right)\n* sqrt(self)\n* square_root(self)\n* nth_root(self, n)\n* floor(self)\n* ceil(self)\n* numerator(self)\n* denominator(self)\n\n\nMissing doctests:\n* numerator(self)\n* denominator(self)\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/590\n\n",
    "created_at": "2007-09-05T15:37:42Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "document extended_rational_field.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/590",
    "user": "@williamstein"
}
```
Assignee: @roed314

The rings/extended_rational_field.py file is terribly documented.  There are no doctests, no copyright notice, no author, etc.   I think David Roe wrote this:

was`@`ubuntu:~/d/sage/sage/rings$ sage -coverage extended_rational_field.py
----------------------------------------------------------------------
extended_rational_field.py
ERROR: Please define a s == loads(dumps(s)) doctest.
OVERALL SCORE: 0%  (2 good, 71 bad)

Missing documentation:
* __init__(self)
* _repr_(self)
* _latex_(self)
* __call__(self, x, base = 0)
* _coerce_impl(self, x)
* _is_valid_homomorphism(self, codomain, im_gens)
* __iter__(self)
* complex_embedding(self, prec=53)
* gens(self)
* gen(self, n=0)
* is_prime_field(self)
* ngens(self)
* numberfield(self, poly_var, nf_var)
* __init__(self, x = None, base = 0)
* __cmp__(self, other)
* copy(self)
* lcm(self, other)
* square_root(self)
* nth_root(self)
* _add_(self, right)
* _sub_(self, right)
* _neg_(self)
* _mul_(self, right)
* _div_(self, right)
* __invert__(self)
* __pow__(self, n)
* __abs__(self)
* floor(self)
* ceil(self)
* __lshift__(self, n)
* __rshift__(self, n)
* __init__(self)
* __cmp__(self, other)
* __repr__(self)
* _latex_(self)
* _add_(self, other)
* _mul_(self, other)
* _sub_(self, other)
* _div_(self, other)
* _neg_(self)
* __invert__(self)
* __abs__(self)
* __pow__(self, right)
* sqrt(self)
* square_root(self)
* nth_root(self, n)
* floor(self)
* ceil(self)
* numerator(self)
* denominator(self)
* __init__(self)
* __cmp__(self, other)
* _repr_(self)
* _latex_(self)
* _add_(self, other)
* _mul_(self, other)
* _sub_(self, other)
* _div_(self, other)
* _neg_(self)
* __invert__(self)
* __abs__(self)
* __pow__(self, right)
* sqrt(self)
* square_root(self)
* nth_root(self, n)
* floor(self)
* ceil(self)
* numerator(self)
* denominator(self)


Missing doctests:
* numerator(self)
* denominator(self)



Issue created by migration from https://trac.sagemath.org/ticket/590





---

archive/issue_comments_003041.json:
```json
{
    "body": "Changing assignee from @roed314 to @mwhansen.",
    "created_at": "2008-02-29T06:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/590#issuecomment-3041",
    "user": "@mwhansen"
}
```

Changing assignee from @roed314 to @mwhansen.



---

archive/issue_comments_003042.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-29T06:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/590#issuecomment-3042",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003043.json:
```json
{
    "body": "Attachment [590.patch](tarball://root/attachments/some-uuid/ticket590/590.patch) by @mwhansen created at 2008-02-29 07:34:31",
    "created_at": "2008-02-29T07:34:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/590#issuecomment-3043",
    "user": "@mwhansen"
}
```

Attachment [590.patch](tarball://root/attachments/some-uuid/ticket590/590.patch) by @mwhansen created at 2008-02-29 07:34:31



---

archive/issue_comments_003044.json:
```json
{
    "body": "I'm mostly happy with this patch; I have a few questions.\n\n* What is `IntegerWrapper`? That's been added with no explanation at all, and I don't understand its purpose. Is it really necessary? If so, there needs to be some documentation.\n\n* regarding `coerce_map_from_impl` and `Q_to_ExtendedQ`: I don't understand the coercion framework any more, so I can't vouch for correctness of the implementations. I'd like someone who understands coercion to take a quick look. Mike, if you find someone on IRC who can sign off on these, that's fine. One thing that bothers me slightly is:\n\n\n```\nsage: ExtendedRationalField.coerce_map_from_impl(ExtendedIntegerRing)\n[boom]\n```\n\n\n* docstring for `ExtendedRational.__init__` is a little confusing; \"The class of extended rational numbers\" is a little confusing, sounds like \"The set of extended rational numbers\". Perhaps better something like \"Constructor for elements of the extended rational field\".\n\n* `_mul_`: I'd like to see examples of multiplying infinity by infinity and minus infinity\n\nI have various other complaints about this module, but it's not in the new code you've written and I don't want to hold up this patch, so I won't go into them now.",
    "created_at": "2008-03-02T16:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/590#issuecomment-3044",
    "user": "dmharvey"
}
```

I'm mostly happy with this patch; I have a few questions.

* What is `IntegerWrapper`? That's been added with no explanation at all, and I don't understand its purpose. Is it really necessary? If so, there needs to be some documentation.

* regarding `coerce_map_from_impl` and `Q_to_ExtendedQ`: I don't understand the coercion framework any more, so I can't vouch for correctness of the implementations. I'd like someone who understands coercion to take a quick look. Mike, if you find someone on IRC who can sign off on these, that's fine. One thing that bothers me slightly is:


```
sage: ExtendedRationalField.coerce_map_from_impl(ExtendedIntegerRing)
[boom]
```


* docstring for `ExtendedRational.__init__` is a little confusing; "The class of extended rational numbers" is a little confusing, sounds like "The set of extended rational numbers". Perhaps better something like "Constructor for elements of the extended rational field".

* `_mul_`: I'd like to see examples of multiplying infinity by infinity and minus infinity

I have various other complaints about this module, but it's not in the new code you've written and I don't want to hold up this patch, so I won't go into them now.



---

archive/issue_comments_003045.json:
```json
{
    "body": "I'm happy with coerce_map_from_impl and Q_to_ExtendedQ, but I think _coerce_impl needs to by default check if its in ExtendedZZ then see if it can be coerced into QQ, then error out.  Current code may not work with things that can be in ExtendedQQ but are not typed as integers (3 in RR).",
    "created_at": "2008-03-02T17:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/590#issuecomment-3045",
    "user": "@garyfurnish"
}
```

I'm happy with coerce_map_from_impl and Q_to_ExtendedQ, but I think _coerce_impl needs to by default check if its in ExtendedZZ then see if it can be coerced into QQ, then error out.  Current code may not work with things that can be in ExtendedQQ but are not typed as integers (3 in RR).



---

archive/issue_comments_003046.json:
```json
{
    "body": "I attached a patch addressing the referee's concerns.",
    "created_at": "2008-03-02T23:27:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/590#issuecomment-3046",
    "user": "@mwhansen"
}
```

I attached a patch addressing the referee's concerns.



---

archive/issue_comments_003047.json:
```json
{
    "body": "Ummm, the doctests for `sage/rings/extended_integer_ring.py` do not pass for me with this patch.",
    "created_at": "2008-03-03T19:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/590#issuecomment-3047",
    "user": "dmharvey"
}
```

Ummm, the doctests for `sage/rings/extended_integer_ring.py` do not pass for me with this patch.



---

archive/issue_comments_003048.json:
```json
{
    "body": "Which ones fail?  What version are you applying against?  If it's the cmp ones, it may just be something random due to architecture differences.",
    "created_at": "2008-03-03T22:32:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/590#issuecomment-3048",
    "user": "@mwhansen"
}
```

Which ones fail?  What version are you applying against?  If it's the cmp ones, it may just be something random due to architecture differences.



---

archive/issue_comments_003049.json:
```json
{
    "body": "It's mac os 10.4.11 intel. Here's the failure:\n\n\n```\nsage -t  devel/sage-590/sage/rings/extended_integer_ring.py **********************************************************************\nFile \"extended_integer_ring.py\", line 58:\n    sage: cmp(ExtendedIntegerRing, ExtendedRationalField)\nExpected:\n    1\nGot:\n    -1\n**********************************************************************\n```\n\n\nWhy would cmp be architecture-dependent? Is it comparing pointers somewhere or something stupid like that?",
    "created_at": "2008-03-03T22:58:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/590#issuecomment-3049",
    "user": "dmharvey"
}
```

It's mac os 10.4.11 intel. Here's the failure:


```
sage -t  devel/sage-590/sage/rings/extended_integer_ring.py **********************************************************************
File "extended_integer_ring.py", line 58:
    sage: cmp(ExtendedIntegerRing, ExtendedRationalField)
Expected:
    1
Got:
    -1
**********************************************************************
```


Why would cmp be architecture-dependent? Is it comparing pointers somewhere or something stupid like that?



---

archive/issue_comments_003050.json:
```json
{
    "body": "Yep.  Python like to be able to compare everything.  With the new coercion stuff coming in, things will have more meaningful _cmp_ functions.",
    "created_at": "2008-03-03T23:00:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/590#issuecomment-3050",
    "user": "@mwhansen"
}
```

Yep.  Python like to be able to compare everything.  With the new coercion stuff coming in, things will have more meaningful _cmp_ functions.



---

archive/issue_comments_003051.json:
```json
{
    "body": "Attachment [590-referee.patch](tarball://root/attachments/some-uuid/ticket590/590-referee.patch) by dmharvey created at 2008-03-04 00:56:22\n\nokay, I'm happy now.",
    "created_at": "2008-03-04T00:56:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/590#issuecomment-3051",
    "user": "dmharvey"
}
```

Attachment [590-referee.patch](tarball://root/attachments/some-uuid/ticket590/590-referee.patch) by dmharvey created at 2008-03-04 00:56:22

okay, I'm happy now.



---

archive/issue_comments_003052.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-04T03:53:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/590#issuecomment-3052",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_003053.json:
```json
{
    "body": "Merged both patches in Sage 2.10.3.rc1",
    "created_at": "2008-03-04T03:53:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/590#issuecomment-3053",
    "user": "mabshoff"
}
```

Merged both patches in Sage 2.10.3.rc1
