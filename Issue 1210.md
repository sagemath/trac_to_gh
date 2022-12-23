# Issue 1210: Cannot create distinct polynomial rings over p-adic rings with different print_modes

archive/issues_001210.json:
```json
{
    "body": "Assignee: roed\n\nKeywords: polynomial p-adic print mode cache caching\n\nThe issue is in the caching:\n\n\n```\nsage: R = Qp(7, print_mode='val-unit')\nsage: S = Qp(7)\nsage: R(7^2 + 1)\n7^2 * 1 + O(7^22)\nsage: S(7^2)\n7^2 + O(7^22)\nsage: R(7^2 + 1)\n50 + O(7^20)\nsage: S(7^2 + 1)\n1 + 7^2 + O(7^20)\nsage: R is S\nFalse\nsage: R['x'] is S['x']\nTrue\n```\n\nThe issue manifests itself in polynomial_ring_constructor, which fails because the cache is keyed by ==, not identity, and\n\n```\nsage: R == S\nTrue\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1210\n\n",
    "created_at": "2007-11-19T21:54:44Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "Cannot create distinct polynomial rings over p-adic rings with different print_modes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1210",
    "user": "ncalexan"
}
```
Assignee: roed

Keywords: polynomial p-adic print mode cache caching

The issue is in the caching:


```
sage: R = Qp(7, print_mode='val-unit')
sage: S = Qp(7)
sage: R(7^2 + 1)
7^2 * 1 + O(7^22)
sage: S(7^2)
7^2 + O(7^22)
sage: R(7^2 + 1)
50 + O(7^20)
sage: S(7^2 + 1)
1 + 7^2 + O(7^20)
sage: R is S
False
sage: R['x'] is S['x']
True
```

The issue manifests itself in polynomial_ring_constructor, which fails because the cache is keyed by ==, not identity, and

```
sage: R == S
True
```


Issue created by migration from https://trac.sagemath.org/ticket/1210





---

archive/issue_comments_007505.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-23T02:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1210#issuecomment-7505",
    "user": "roed"
}
```

Attachment



---

archive/issue_comments_007506.json:
```json
{
    "body": "Attachment\n\nUse this one instead",
    "created_at": "2009-01-24T02:43:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1210#issuecomment-7506",
    "user": "roed"
}
```

Attachment

Use this one instead



---

archive/issue_comments_007507.json:
```json
{
    "body": "I have lots of doctest failures... wrong versions?  The argument \"print_pos\" does not appear anywhere in my sage/rings/padics directory, btw.\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: nca\nsage: import sage_emacs as emacs\nsage: R = Qp(7, print_mode='digits', print_pos=True)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n| Sage Version 3.3.alpha0, Release Date: 2009-01-19                  |\n| Type notebook() for the GUI, and license() for information.        |\n/home/ncalexan/.sage/temp/sage.math.washington.edu/16970/_home_ncalexan__sage_init_sage_0.py in <module>()\n----> 1 \n      2 \n      3 \n      4 \n      5 \n\n/scratch/nca/sage-3.3.alpha1-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/factory.so in sage.structure.factory.UniqueFactory.__call__ (sage/structure/factory.c:579)()\n    106 \n    107 \n--> 108 \n    109 \n    110 \n\n/scratch/nca/sage-3.3.alpha1-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/factory.so in sage.structure.factory.UniqueFactory.create_key_and_extra_args (sage/structure/factory.c:1373)()\n    193 \n    194 \n--> 195 \n    196 \n    197 \n\nTypeError: create_key() got an unexpected keyword argument 'print_pos'\nsage: S = Qp(7, print_mode='digits', print_pos=False)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/ncalexan/.sage/temp/sage.math.washington.edu/16970/_home_ncalexan__sage_init_sage_0.py in <module>()\n----> 1 \n      2 \n      3 \n      4 \n      5 \n\n/scratch/nca/sage-3.3.alpha1-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/factory.so in sage.structure.factory.UniqueFactory.__call__ (sage/structure/factory.c:579)()\n    106 \n    107 \n--> 108 \n    109 \n    110 \n\n/scratch/nca/sage-3.3.alpha1-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/factory.so in sage.structure.factory.UniqueFactory.create_key_and_extra_args (sage/structure/factory.c:1373)()\n    193 \n    194 \n--> 195 \n    196 \n    197 \n\nTypeError: create_key() got an unexpected keyword argument 'print_pos'\nsage: \n```\n",
    "created_at": "2009-01-24T22:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1210#issuecomment-7507",
    "user": "ncalexan"
}
```

I have lots of doctest failures... wrong versions?  The argument "print_pos" does not appear anywhere in my sage/rings/padics directory, btw.


```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: nca
sage: import sage_emacs as emacs
sage: R = Qp(7, print_mode='digits', print_pos=True)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 3.3.alpha0, Release Date: 2009-01-19                  |
| Type notebook() for the GUI, and license() for information.        |
/home/ncalexan/.sage/temp/sage.math.washington.edu/16970/_home_ncalexan__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/scratch/nca/sage-3.3.alpha1-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/factory.so in sage.structure.factory.UniqueFactory.__call__ (sage/structure/factory.c:579)()
    106 
    107 
--> 108 
    109 
    110 

/scratch/nca/sage-3.3.alpha1-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/factory.so in sage.structure.factory.UniqueFactory.create_key_and_extra_args (sage/structure/factory.c:1373)()
    193 
    194 
--> 195 
    196 
    197 

TypeError: create_key() got an unexpected keyword argument 'print_pos'
sage: S = Qp(7, print_mode='digits', print_pos=False)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/ncalexan/.sage/temp/sage.math.washington.edu/16970/_home_ncalexan__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/scratch/nca/sage-3.3.alpha1-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/factory.so in sage.structure.factory.UniqueFactory.__call__ (sage/structure/factory.c:579)()
    106 
    107 
--> 108 
    109 
    110 

/scratch/nca/sage-3.3.alpha1-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/factory.so in sage.structure.factory.UniqueFactory.create_key_and_extra_args (sage/structure/factory.c:1373)()
    193 
    194 
--> 195 
    196 
    197 

TypeError: create_key() got an unexpected keyword argument 'print_pos'
sage: 
```




---

archive/issue_comments_007508.json:
```json
{
    "body": "David, Nick: Has this problem been fixed due to the work by David merged in 3.4.1.rc3?\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T03:21:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1210#issuecomment-7508",
    "user": "mabshoff"
}
```

David, Nick: Has this problem been fixed due to the work by David merged in 3.4.1.rc3?

Cheers,

Michael



---

archive/issue_comments_007509.json:
```json
{
    "body": "Replying to [comment:3 mabshoff]:\n> David, Nick: Has this problem been fixed due to the work by David merged in 3.4.1.rc3?\n> \n> Cheers,\n> \n> Michael\n\nIt would appear so. Consider:\n\n```\nsage: R = Qp(7, print_mode='val-unit')\nsage: S = Qp(7)\nsage: R(7^2 + 1)\n7^2 * 1 + O(7^22)\nsage: S(7^2)\n7^2 + O(7^22)\nsage: R(7^2 + 1)\n50 + O(7^20)\nsage: S(7^2 + 1)\n1 + 7^2 + O(7^20)\nsage: R is S\nFalse\nsage: R['x'] is S['x']\nFalse # this is now fixed\nsage: R['x'](7^2)\n(7^2 * 1 + O(7^22))\nsage: S['x'](7^2)\n(7^2 + O(7^22))\nsage: R['x'](7^2+1)\n(50 + O(7^20))\nsage: S['x'](7^2+1)\n(1 + 7^2 + O(7^20))\n```\n\nHowever, this is still puzzling:\n\n```\nsage: R['x'] == S['x']\nFalse\n```\n",
    "created_at": "2009-05-20T21:42:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1210#issuecomment-7509",
    "user": "kedlaya"
}
```

Replying to [comment:3 mabshoff]:
> David, Nick: Has this problem been fixed due to the work by David merged in 3.4.1.rc3?
> 
> Cheers,
> 
> Michael

It would appear so. Consider:

```
sage: R = Qp(7, print_mode='val-unit')
sage: S = Qp(7)
sage: R(7^2 + 1)
7^2 * 1 + O(7^22)
sage: S(7^2)
7^2 + O(7^22)
sage: R(7^2 + 1)
50 + O(7^20)
sage: S(7^2 + 1)
1 + 7^2 + O(7^20)
sage: R is S
False
sage: R['x'] is S['x']
False # this is now fixed
sage: R['x'](7^2)
(7^2 * 1 + O(7^22))
sage: S['x'](7^2)
(7^2 + O(7^22))
sage: R['x'](7^2+1)
(50 + O(7^20))
sage: S['x'](7^2+1)
(1 + 7^2 + O(7^20))
```

However, this is still puzzling:

```
sage: R['x'] == S['x']
False
```




---

archive/issue_comments_007510.json:
```json
{
    "body": "I get with `5.9.beta1`:\n\n```\nsage: sage: R = Qp(7, print_mode='val-unit')\nsage: sage: S = Qp(7)\nsage: R is S\nFalse\nsage: R == S\nFalse\nsage: R['x'] == S['x']\nFalse\nsage: R['x'] is S['x']\nFalse\n```\n\nwhich is the expected behavior due to `UniqueRepresentation` parents.",
    "created_at": "2013-04-10T23:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1210#issuecomment-7510",
    "user": "tscrim"
}
```

I get with `5.9.beta1`:

```
sage: sage: R = Qp(7, print_mode='val-unit')
sage: sage: S = Qp(7)
sage: R is S
False
sage: R == S
False
sage: R['x'] == S['x']
False
sage: R['x'] is S['x']
False
```

which is the expected behavior due to `UniqueRepresentation` parents.



---

archive/issue_comments_007511.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-04-10T23:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1210#issuecomment-7511",
    "user": "tscrim"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_007512.json:
```json
{
    "body": "Replying to [comment:5 tscrim]:\n> I get with `5.9.beta1`:\n> {{{\n> sage: sage: R = Qp(7, print_mode='val-unit')\n> sage: sage: S = Qp(7)\n> sage: R is S\n> False\n> sage: R == S\n> False\n> sage: R['x'] == S['x']\n> False\n> sage: R['x'] is S['x']\n> False\n> }}}\n> which is the expected behavior due to `UniqueRepresentation` parents.\n\nIt should be due to `UniqueFactory` (in `6.2.beta3`). But anyway, documentation of `Qp` says \n\n```\nPRINTING:\n\n    There are many different ways to print `p`-adic elements.\n    ...\n    Note that the printing options affect whether different\n    `p`-adic fields are considered equal.\n```\n",
    "created_at": "2014-03-09T22:43:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1210#issuecomment-7512",
    "user": "aapitzsch"
}
```

Replying to [comment:5 tscrim]:
> I get with `5.9.beta1`:
> {{{
> sage: sage: R = Qp(7, print_mode='val-unit')
> sage: sage: S = Qp(7)
> sage: R is S
> False
> sage: R == S
> False
> sage: R['x'] == S['x']
> False
> sage: R['x'] is S['x']
> False
> }}}
> which is the expected behavior due to `UniqueRepresentation` parents.

It should be due to `UniqueFactory` (in `6.2.beta3`). But anyway, documentation of `Qp` says 

```
PRINTING:

    There are many different ways to print `p`-adic elements.
    ...
    Note that the printing options affect whether different
    `p`-adic fields are considered equal.
```




---

archive/issue_comments_007513.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-03-09T22:43:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1210#issuecomment-7513",
    "user": "aapitzsch"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_007514.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-03-11T14:04:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1210#issuecomment-7514",
    "user": "vbraun"
}
```

Resolution: fixed
