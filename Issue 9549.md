# Issue 9549: InfinitePolynomialRing_sparse.is_field lacks `proof=...` option

archive/issues_009549.json:
```json
{
    "body": "Assignee: malb\n\nThe class `InfinitePolynomialRing_sparse` defines two methods called `is_field()`. The second definition rejects keyword arguments. This prevents from creating polynomial rings over infinite polynomial rings:\n\n```\n$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: InfinitePolynomialRing(QQ, 'a')['x']\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n| Sage Version 4.5, Release Date: 2010-07-16                         |\n| Type notebook() for the GUI, and license() for information.        |\n/home/marc/opt/sage-4.5/<ipython console> in <module>()\n\n/home/marc/opt/sage-4.5/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:2550)()\n\n/home/marc/opt/sage-4.5/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc in PolynomialRing(base_ring, arg1, arg2, sparse, order, names, name, implementation)\n    341                 raise TypeError, \"if second arguments is a string with no commas, then there must be no other non-optional arguments\"\n    342             name = arg1\n--> 343             R = _single_variate(base_ring, name, sparse, implementation)\n    344         else:\n    345             # 2-4. PolynomialRing(base_ring, names, order='degrevlex'):\n\n/home/marc/opt/sage-4.5/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc in _single_variate(base_ring, name, sparse, implementation)\n    420             R = m.PolynomialRing_dense_padic_ring_fixed_mod(base_ring, name)\n    421 \n--> 422         elif base_ring.is_field(proof = False):\n    423             R = m.PolynomialRing_field(base_ring, name, sparse, implementation=implementation)\n    424 \n\nTypeError: is_field() got an unexpected keyword argument 'proof'\n```\n\n\nThere is a similar issue with ``is_integral_domain``, too.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9549\n\n",
    "created_at": "2010-07-19T11:47:08Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "InfinitePolynomialRing_sparse.is_field lacks `proof=...` option",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9549",
    "user": "mmezzarobba"
}
```
Assignee: malb

The class `InfinitePolynomialRing_sparse` defines two methods called `is_field()`. The second definition rejects keyword arguments. This prevents from creating polynomial rings over infinite polynomial rings:

```
$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: InfinitePolynomialRing(QQ, 'a')['x']
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.5, Release Date: 2010-07-16                         |
| Type notebook() for the GUI, and license() for information.        |
/home/marc/opt/sage-4.5/<ipython console> in <module>()

/home/marc/opt/sage-4.5/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:2550)()

/home/marc/opt/sage-4.5/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc in PolynomialRing(base_ring, arg1, arg2, sparse, order, names, name, implementation)
    341                 raise TypeError, "if second arguments is a string with no commas, then there must be no other non-optional arguments"
    342             name = arg1
--> 343             R = _single_variate(base_ring, name, sparse, implementation)
    344         else:
    345             # 2-4. PolynomialRing(base_ring, names, order='degrevlex'):

/home/marc/opt/sage-4.5/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc in _single_variate(base_ring, name, sparse, implementation)
    420             R = m.PolynomialRing_dense_padic_ring_fixed_mod(base_ring, name)
    421 
--> 422         elif base_ring.is_field(proof = False):
    423             R = m.PolynomialRing_field(base_ring, name, sparse, implementation=implementation)
    424 

TypeError: is_field() got an unexpected keyword argument 'proof'
```


There is a similar issue with ``is_integral_domain``, too.

Issue created by migration from https://trac.sagemath.org/ticket/9549





---

archive/issue_comments_092045.json:
```json
{
    "body": "Please disregard (or better, delete) the previous attachment.",
    "created_at": "2010-07-19T12:08:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9549#issuecomment-92045",
    "user": "mmezzarobba"
}
```

Please disregard (or better, delete) the previous attachment.



---

archive/issue_comments_092046.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-19T12:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9549#issuecomment-92046",
    "user": "mmezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092047.json:
```json
{
    "body": "Replying to [comment:1 mmezzarobba]:\n> Please disregard (or better, delete) the previous attachment.\n\nI have now replaced it with the correct file. (It seems that for some reason, unprivilegied trac users are allowed to replace attached files but not to delete them??!)",
    "created_at": "2010-07-19T12:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9549#issuecomment-92047",
    "user": "mmezzarobba"
}
```

Replying to [comment:1 mmezzarobba]:
> Please disregard (or better, delete) the previous attachment.

I have now replaced it with the correct file. (It seems that for some reason, unprivilegied trac users are allowed to replace attached files but not to delete them??!)



---

archive/issue_comments_092048.json:
```json
{
    "body": "You probably don't want the line\n\n\n```\nprint \"coucou\" \n```\n\n\nin the patch.",
    "created_at": "2010-07-19T17:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9549#issuecomment-92048",
    "user": "mhansen"
}
```

You probably don't want the line


```
print "coucou" 
```


in the patch.



---

archive/issue_comments_092049.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-19T17:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9549#issuecomment-92049",
    "user": "mhansen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_092050.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-07-19T20:08:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9549#issuecomment-92050",
    "user": "mmezzarobba"
}
```

Attachment



---

archive/issue_comments_092051.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-19T20:16:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9549#issuecomment-92051",
    "user": "mmezzarobba"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_092052.json:
```json
{
    "body": "Replying to [comment:3 mhansen]:\n> You probably don't want the line\n> \n> {{{\n> print \"coucou\" \n> }}}\n> \n> in the patch.\n\nSorry--I was sure I had double-checked that it wasn't in the patch after uploading it... :-/ Thanks for spotting my blunder.",
    "created_at": "2010-07-19T20:16:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9549#issuecomment-92052",
    "user": "mmezzarobba"
}
```

Replying to [comment:3 mhansen]:
> You probably don't want the line
> 
> {{{
> print "coucou" 
> }}}
> 
> in the patch.

Sorry--I was sure I had double-checked that it wasn't in the patch after uploading it... :-/ Thanks for spotting my blunder.



---

archive/issue_comments_092053.json:
```json
{
    "body": "In is_integral_domain, we should pass on the keywords to self._base.is_integral_domain() so that that can take a proof option.",
    "created_at": "2010-08-11T20:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9549#issuecomment-92053",
    "user": "mhansen"
}
```

In is_integral_domain, we should pass on the keywords to self._base.is_integral_domain() so that that can take a proof option.



---

archive/issue_comments_092054.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-11T20:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9549#issuecomment-92054",
    "user": "mhansen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_092055.json:
```json
{
    "body": "This has been fixed by\u00a0#9443.",
    "created_at": "2010-11-05T12:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9549#issuecomment-92055",
    "user": "fwclarke"
}
```

This has been fixed by #9443.



---

archive/issue_comments_092056.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-11-05T12:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9549#issuecomment-92056",
    "user": "fwclarke"
}
```

Resolution: duplicate
