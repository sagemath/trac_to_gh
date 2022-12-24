# Issue 3028: Ideals in multivariate polynomial rings raise exceptions on comparison

archive/issues_003028.json:
```json
{
    "body": "Assignee: malb\n\nKeywords: multivariate polynomial ring, no variables\n\nThis code\n\nring = PolynomialRing(QQ, names=[])\n\nid = ring.ideal(0)\n\nprint id == id\n\n\ngives the following error message\n\n---------------------------------------------------------------------------\n<type 'exceptions.StopIteration'>         Traceback (most recent call last)\n\n/Users/bjarke/sync/<ipython console> in <module>()\n\n/Users/bjarke/sync/element.pyx in sage.structure.element.Element.__richcmp__ (sage/structure/element.c:4558)()\n\n/Users/bjarke/sync/element.pyx in sage.structure.element.Element._richcmp (sage/structure/element.c:4453)()\n\n/Users/bjarke/sage-3.0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in __cmp__(self, other)\n    347             True\n    348         \"\"\"\n--> 349         l = self.groebner_basis()\n    350         r = other.groebner_basis()\n    351         return cmp(r,l)\n\n/Users/bjarke/sage-3.0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in groebner_basis(self, algorithm, *args, **kwds)\n   1836                 except TypeError: # conversion to Singular not supported\n   1837                     # we might want to print a warning here\n-> 1838                     gb = toy_buchberger.buchberger_improved(self, *args, **kwds)\n   1839         elif algorithm.startswith('singular:'):\n   1840             gb = self._groebner_basis_using_singular(algorithm[9:])\n\n/Users/bjarke/sage-3.0/local/lib/python2.5/site-packages/sage/rings/polynomial/toy_buchberger.py in buchberger_improved(F)\n    232         print \"%d reductions to zero.\"%(reductions_to_zero)\n    233 \n--> 234     return Sequence(inter_reduction(G))\n    235 \n    236 def update(G,B,h):\n\n/Users/bjarke/sage-3.0/local/lib/python2.5/site-packages/sage/rings/polynomial/toy_buchberger.py in inter_reduction(Q)\n    324         Q -- a set of polynomials\n    325     \"\"\"\n--> 326     base_ring = iter(Q).next().base_ring()\n    327     Q = set(Q)\n    328     while True:\n\n<type 'exceptions.StopIteration'>: \n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3028\n\n",
    "created_at": "2008-04-26T01:45:51Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "Ideals in multivariate polynomial rings raise exceptions on comparison",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3028",
    "user": "broune"
}
```
Assignee: malb

Keywords: multivariate polynomial ring, no variables

This code

ring = PolynomialRing(QQ, names=[])

id = ring.ideal(0)

print id == id


gives the following error message

---------------------------------------------------------------------------
<type 'exceptions.StopIteration'>         Traceback (most recent call last)

/Users/bjarke/sync/<ipython console> in <module>()

/Users/bjarke/sync/element.pyx in sage.structure.element.Element.__richcmp__ (sage/structure/element.c:4558)()

/Users/bjarke/sync/element.pyx in sage.structure.element.Element._richcmp (sage/structure/element.c:4453)()

/Users/bjarke/sage-3.0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in __cmp__(self, other)
    347             True
    348         """
--> 349         l = self.groebner_basis()
    350         r = other.groebner_basis()
    351         return cmp(r,l)

/Users/bjarke/sage-3.0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in groebner_basis(self, algorithm, *args, **kwds)
   1836                 except TypeError: # conversion to Singular not supported
   1837                     # we might want to print a warning here
-> 1838                     gb = toy_buchberger.buchberger_improved(self, *args, **kwds)
   1839         elif algorithm.startswith('singular:'):
   1840             gb = self._groebner_basis_using_singular(algorithm[9:])

/Users/bjarke/sage-3.0/local/lib/python2.5/site-packages/sage/rings/polynomial/toy_buchberger.py in buchberger_improved(F)
    232         print "%d reductions to zero."%(reductions_to_zero)
    233 
--> 234     return Sequence(inter_reduction(G))
    235 
    236 def update(G,B,h):

/Users/bjarke/sage-3.0/local/lib/python2.5/site-packages/sage/rings/polynomial/toy_buchberger.py in inter_reduction(Q)
    324         Q -- a set of polynomials
    325     """
--> 326     base_ring = iter(Q).next().base_ring()
    327     Q = set(Q)
    328     while True:

<type 'exceptions.StopIteration'>: 




Issue created by migration from https://trac.sagemath.org/ticket/3028





---

archive/issue_comments_020823.json:
```json
{
    "body": "Attachment [idcomp.changeset](tarball://root/attachments/some-uuid/ticket3028/idcomp.changeset) by broune created at 2008-05-07 22:15:59",
    "created_at": "2008-05-07T22:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3028#issuecomment-20823",
    "user": "broune"
}
```

Attachment [idcomp.changeset](tarball://root/attachments/some-uuid/ticket3028/idcomp.changeset) by broune created at 2008-05-07 22:15:59



---

archive/issue_comments_020824.json:
```json
{
    "body": "Changing assignee from malb to broune.",
    "created_at": "2008-05-07T22:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3028#issuecomment-20824",
    "user": "broune"
}
```

Changing assignee from malb to broune.



---

archive/issue_comments_020825.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-07T22:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3028#issuecomment-20825",
    "user": "broune"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020826.json:
```json
{
    "body": "Code looks good, doctests pass in sage/rings/polynomial.  Positive review.",
    "created_at": "2008-05-10T23:16:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3028#issuecomment-20826",
    "user": "cwitty"
}
```

Code looks good, doctests pass in sage/rings/polynomial.  Positive review.



---

archive/issue_comments_020827.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha0",
    "created_at": "2008-05-11T08:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3028#issuecomment-20827",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.alpha0



---

archive/issue_comments_020828.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-11T08:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3028#issuecomment-20828",
    "user": "mabshoff"
}
```

Resolution: fixed
