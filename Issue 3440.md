# Issue 3440: Our PolyBoRi's GB calculation in AES mode is broken

archive/issues_003440.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  polybori @burcin\n\nKeywords: polybori\n\nBurcin says this broke when the iterators changed:\n\n```\nsage: sr = mq.SR(2,1,1,4,gf2=True)\nsage: F,s = sr.polynomial_system()\nsage: R = F.ring()\nsage: B = BooleanPolynomialRing(R.ngens(),R.variable_names())\nsage: I = Ideal([B(f) for f in F])\nsage: type(I)\n<class 'sage.rings.polynomial.pbori.BooleanPolynomialIdeal'>\nsage: I.groebner_basis(aes=True)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n...\n/usr/local/sage-3.0/local/lib/python2.5/site-packages/polybori/PyPolyBoRi.py in <lambda>(x)\n     21 OrderCode.__dict__ = order_dict\n     22\n---> 23 Variable = lambda x: get_cring().gen(x)\n     24\n     25 def Ring(n, order='lp'):\n\n/home/malb/pbori.pyx in sage.rings.polynomial.pbori.BooleanPolynomialRing.gen (sage/rings/polynomial/pbori.cpp:3333)()\n\n<type 'exceptions.TypeError'>: an integer is required\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3440\n\n",
    "created_at": "2008-06-16T20:03:55Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "Our PolyBoRi's GB calculation in AES mode is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3440",
    "user": "@malb"
}
```
Assignee: @malb

CC:  polybori @burcin

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


Issue created by migration from https://trac.sagemath.org/ticket/3440





---

archive/issue_comments_024271.json:
```json
{
    "body": "in PolyBoRi 0.5 will change iterators again ;-).\nI hope more SAGE-friendly\n\nfor variable in m.variables()\nfor term in p.terms()",
    "created_at": "2008-06-17T06:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3440#issuecomment-24271",
    "user": "PolyBoRi"
}
```

in PolyBoRi 0.5 will change iterators again ;-).
I hope more SAGE-friendly

for variable in m.variables()
for term in p.terms()



---

archive/issue_comments_024272.json:
```json
{
    "body": "this fixes the first issue",
    "created_at": "2008-08-18T12:10:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3440#issuecomment-24272",
    "user": "@malb"
}
```

this fixes the first issue



---

archive/issue_comments_024273.json:
```json
{
    "body": "Attachment [trac_3440_gen.patch](tarball://root/attachments/some-uuid/ticket3440/trac_3440_gen.patch) by @malb created at 2008-08-18 12:13:00\n\nThe attache patch fixes the issue above, however now:\n\n\n```\nsage: sr = mq.SR(2,1,1,4,gf2=True)\nsage: F,s = sr.polynomial_system()\nsage: R = F.ring()\nsage: B = BooleanPolynomialRing(R.ngens(),R.variable_names())\nsage: I = Ideal([B(f) for f in F])\nsage: type(I)\n<class 'sage.rings.polynomial.pbori.BooleanPolynomialIdeal'>\nsage: I.groebner_basis(aes=True)\n---------------------------------------------------------------------------\nImportError                               Traceback (most recent call last)\n...\n/usr/local/sage-3.0.6/local/lib/python2.5/site-packages/polybori/aes.py in preprocess(I, prot)\n     55     global cache\n     56     if get_order_code()==OrderCode.lp:\n---> 57       import cache as cache_module\n     58       cache=cache_module.cache\n     59       del cache_module\nImportError: No module named cache\n```\n\n\nIdeas, thoughts, work-arounds?",
    "created_at": "2008-08-18T12:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3440#issuecomment-24273",
    "user": "@malb"
}
```

Attachment [trac_3440_gen.patch](tarball://root/attachments/some-uuid/ticket3440/trac_3440_gen.patch) by @malb created at 2008-08-18 12:13:00

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

archive/issue_comments_024274.json:
```json
{
    "body": "personally, at the moment, I don't feel, that it is good to expose this option to\nusers. I did that for aes systems initially. But it is not about: Use that option and everything will work well...\n\nNevertheless: workaround\nreplace 57/58 by\n\n```\ncache={}\n```\n\nwhich will make it slower.\nI think, we don't distribute cache.py (which contains some GB of the 8BIT SBOX).",
    "created_at": "2008-08-18T12:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3440#issuecomment-24274",
    "user": "PolyBoRi"
}
```

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

archive/issue_comments_024275.json:
```json
{
    "body": "I vote for applying my patch then and closing this ticket. We don't actively expose aes=True to the user, i.e. it is not documented etc. It just happens to work since we pass the parameters thru to PolyBoRi.",
    "created_at": "2008-08-18T14:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3440#issuecomment-24275",
    "user": "@malb"
}
```

I vote for applying my patch then and closing this ticket. We don't actively expose aes=True to the user, i.e. it is not documented etc. It just happens to work since we pass the parameters thru to PolyBoRi.



---

archive/issue_comments_024276.json:
```json
{
    "body": "Trivial patch, looks good to me.\n\nSorry for the very late review.",
    "created_at": "2008-08-27T16:08:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3440#issuecomment-24276",
    "user": "@burcin"
}
```

Trivial patch, looks good to me.

Sorry for the very late review.



---

archive/issue_comments_024277.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha2",
    "created_at": "2008-08-27T21:28:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3440#issuecomment-24277",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha2



---

archive/issue_comments_024278.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-27T21:28:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3440#issuecomment-24278",
    "user": "mabshoff"
}
```

Resolution: fixed
