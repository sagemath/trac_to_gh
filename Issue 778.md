# Issue 778: Finite Field __call__ doesn't accept polynomials over F_p

archive/issues_000778.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  alexghitza\n\nKeywords: finite fields\n\nNeither Givaro nor pari finite fields accept polynomial arguments.\n\nIssue created by migration from https://trac.sagemath.org/ticket/778\n\n",
    "created_at": "2007-10-02T01:42:34Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Finite Field __call__ doesn't accept polynomials over F_p",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/778",
    "user": "roed"
}
```
Assignee: somebody

CC:  alexghitza

Keywords: finite fields

Neither Givaro nor pari finite fields accept polynomial arguments.

Issue created by migration from https://trac.sagemath.org/ticket/778





---

archive/issue_comments_004640.json:
```json
{
    "body": "Sorry, should have given an example.\n\nsage: Q.<q> = GF(5^7)\nsage: L = GF(5)\nsage: LL.<xx> = L[]\nsage: Q(xx^2 + 2*xx + 4)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/roed/<ipython console> in <module>()\n\n/Users/roed/Math/sage/local/lib/python2.5/site-packages/sage/rings/finite_field.py in __call__(self, x)\n    624                 return self(x.constant_coefficient())\n    625             else:\n--> 626                 raise TypeError, \"no coercion defined\"\n    627 \n    628         elif isinstance(x, str):\n\n<type 'exceptions.TypeError'>: no coercion defined",
    "created_at": "2007-11-03T19:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/778#issuecomment-4640",
    "user": "roed"
}
```

Sorry, should have given an example.

sage: Q.<q> = GF(5^7)
sage: L = GF(5)
sage: LL.<xx> = L[]
sage: Q(xx^2 + 2*xx + 4)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/roed/<ipython console> in <module>()

/Users/roed/Math/sage/local/lib/python2.5/site-packages/sage/rings/finite_field.py in __call__(self, x)
    624                 return self(x.constant_coefficient())
    625             else:
--> 626                 raise TypeError, "no coercion defined"
    627 
    628         elif isinstance(x, str):

<type 'exceptions.TypeError'>: no coercion defined



---

archive/issue_comments_004641.json:
```json
{
    "body": "\n```\nSorry.\nsage: Q.<q> = GF(5^7)\nsage: L = GF(5)\nsage: LL.<xx> = L[]\nsage: Q(xx^2 + 2*xx + 4)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError '>             Traceback (most recent call last)\n\n/Users/roed/<ipython console> in <module>()\n\n/Users/roed/Math/sage/local/lib/python2.5/site-packages/sage/rings/finite_field.py in __call__(self, x)\n    624                 return self(x.constant_coefficient())\n    625             else:\n--> 626                 raise TypeError, \"no coercion defined\"\n    627\n    628         elif isinstance(x, str):\n\n<type 'exceptions.TypeError'>: no coercion defined\n- Show quoted text -\n```\n",
    "created_at": "2007-11-03T20:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/778#issuecomment-4641",
    "user": "was"
}
```


```
Sorry.
sage: Q.<q> = GF(5^7)
sage: L = GF(5)
sage: LL.<xx> = L[]
sage: Q(xx^2 + 2*xx + 4)
---------------------------------------------------------------------------
<type 'exceptions.TypeError '>             Traceback (most recent call last)

/Users/roed/<ipython console> in <module>()

/Users/roed/Math/sage/local/lib/python2.5/site-packages/sage/rings/finite_field.py in __call__(self, x)
    624                 return self(x.constant_coefficient())
    625             else:
--> 626                 raise TypeError, "no coercion defined"
    627
    628         elif isinstance(x, str):

<type 'exceptions.TypeError'>: no coercion defined
- Show quoted text -
```




---

archive/issue_comments_004642.json:
```json
{
    "body": "I don't understamd what you expect to be done here.  How can you coerce a polynomial over GF(5) into the field GF(5**7)?  If you mean to coerce it into a polynomial over GF(5**7) then do this:\n\n```\nsage: PolynomialRing(Q,x)(xx^2 + 2*xx + 4)\nx^2 + 2*x + 4\n```\n\n\nor this:\n\n```\nsage: f=LL.base_extend(Q)(xx^2 + 2*xx + 4)\nsage: f\nxx^2 + 2*xx + 4\nsage: f.parent()\nUnivariate Polynomial Ring in xx over Finite Field in q of size 5^7\n```\n\n\nCan roed explain?  Otherwise I vote for this to be closed.",
    "created_at": "2008-02-18T11:47:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/778#issuecomment-4642",
    "user": "cremona"
}
```

I don't understamd what you expect to be done here.  How can you coerce a polynomial over GF(5) into the field GF(5**7)?  If you mean to coerce it into a polynomial over GF(5**7) then do this:

```
sage: PolynomialRing(Q,x)(xx^2 + 2*xx + 4)
x^2 + 2*x + 4
```


or this:

```
sage: f=LL.base_extend(Q)(xx^2 + 2*xx + 4)
sage: f
xx^2 + 2*xx + 4
sage: f.parent()
Univariate Polynomial Ring in xx over Finite Field in q of size 5^7
```


Can roed explain?  Otherwise I vote for this to be closed.



---

archive/issue_comments_004643.json:
```json
{
    "body": "David wants something like one has with quotients of polynomial rings, since finite extension fields can be thought of as polynomial quotient rings.  E.g.,:\n\n\n```\nsage: R.<x> = GF(5)[]\nsage: Q.<q> = R.quotient(x^7 + 3*x + 3)\nsage: Q(x^2 + 2*x + 4)\nq^2 + 2*q + 4\n```\n\n\nI think this is a reasonable request, since there is a natural ring homomorphism\nfrom GF(5)['x'] to GF(5^7), when the GF(5^7) is presented as an explicit quotient of a polynomial ring modulo an irred. polynomial, as our are. \n\n -- William",
    "created_at": "2008-02-19T00:08:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/778#issuecomment-4643",
    "user": "was"
}
```

David wants something like one has with quotients of polynomial rings, since finite extension fields can be thought of as polynomial quotient rings.  E.g.,:


```
sage: R.<x> = GF(5)[]
sage: Q.<q> = R.quotient(x^7 + 3*x + 3)
sage: Q(x^2 + 2*x + 4)
q^2 + 2*q + 4
```


I think this is a reasonable request, since there is a natural ring homomorphism
from GF(5)['x'] to GF(5^7), when the GF(5^7) is presented as an explicit quotient of a polynomial ring modulo an irred. polynomial, as our are. 

 -- William



---

archive/issue_comments_004644.json:
```json
{
    "body": "Now I understand.  In that case you can just evaluate the polynomial at the generator of the extension field:\n\n\n```\nsage: Q.<q> = GF(5^7)\nsage: L = GF(5)\nsage: LL.<xx> = L[]\nsage: (xx^2 + 2*xx + 4)(q)\nq^2 + 2*q + 4\n```\n\n\nSo what roed wants is for Q(f) to evaluate as f(Q.gen()), where f is a polynomial over the base ring of Q.  That is now understandable, and reasonable, and presumably not hard to implement!",
    "created_at": "2008-02-19T09:11:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/778#issuecomment-4644",
    "user": "cremona"
}
```

Now I understand.  In that case you can just evaluate the polynomial at the generator of the extension field:


```
sage: Q.<q> = GF(5^7)
sage: L = GF(5)
sage: LL.<xx> = L[]
sage: (xx^2 + 2*xx + 4)(q)
q^2 + 2*q + 4
```


So what roed wants is for Q(f) to evaluate as f(Q.gen()), where f is a polynomial over the base ring of Q.  That is now understandable, and reasonable, and presumably not hard to implement!



---

archive/issue_comments_004645.json:
```json
{
    "body": "Attachment [trac778.patch](tarball://root/attachments/some-uuid/ticket778/trac778.patch) by cremona created at 2008-04-04 22:03:49",
    "created_at": "2008-04-04T22:03:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/778#issuecomment-4645",
    "user": "cremona"
}
```

Attachment [trac778.patch](tarball://root/attachments/some-uuid/ticket778/trac778.patch) by cremona created at 2008-04-04 22:03:49



---

archive/issue_comments_004646.json:
```json
{
    "body": "Attached patch (trac778.patch, based on 2.11) adds coercion of univariate polynomials into finite field elements, for all three finite field classes, with extra doctests.",
    "created_at": "2008-04-04T22:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/778#issuecomment-4646",
    "user": "cremona"
}
```

Attached patch (trac778.patch, based on 2.11) adds coercion of univariate polynomials into finite field elements, for all three finite field classes, with extra doctests.



---

archive/issue_comments_004647.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-04T22:18:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/778#issuecomment-4647",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_004648.json:
```json
{
    "body": "Merged in Sage 3.0.alpha1",
    "created_at": "2008-04-04T22:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/778#issuecomment-4648",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha1



---

archive/issue_comments_004649.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-04T22:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/778#issuecomment-4649",
    "user": "mabshoff"
}
```

Resolution: fixed
