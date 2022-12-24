# Issue 7589: bug in coercion and cyclotomic fields

archive/issues_007589.json:
```json
{
    "body": "Assignee: robertwb\n\nCC:  vripoll stumpc5 tscrim\n\nThis should work automagically:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: a = CyclotomicField(3).random_element()\nsage: b = CyclotomicField(4).random_element()\nsage: a + b\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n| Sage Version 4.2.1, Release Date: 2009-11-14                       |\n| Type notebook() for the GUI, and license() for information.        |\n/home/ghitza/.sage/temp/artin/9098/_home_ghitza__sage_init_sage_0.py in <module>()\n\n/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:6989)()\n\n/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:7021)()\n\nTypeError: unsupported operand parent(s) for '+': 'Cyclotomic Field of order 3 and degree 2' and 'Cyclotomic Field of order 4 and degree 2'\nsage: a * b\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/ghitza/.sage/temp/artin/9098/_home_ghitza__sage_init_sage_0.py in <module>()\n\n/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10248)()\n\n/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:7021)()\n\nTypeError: unsupported operand parent(s) for '*': 'Cyclotomic Field of order 3 and degree 2' and 'Cyclotomic Field of order 4 and degree 2'\n```\n\n\nI think it's a coercion problem.  If someone knows better, please change the trac component accordingly.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7589\n\n",
    "created_at": "2009-12-03T09:45:31Z",
    "labels": [
        "coercion",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.3",
    "title": "bug in coercion and cyclotomic fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7589",
    "user": "AlexGhitza"
}
```
Assignee: robertwb

CC:  vripoll stumpc5 tscrim

This should work automagically:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: a = CyclotomicField(3).random_element()
sage: b = CyclotomicField(4).random_element()
sage: a + b
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.2.1, Release Date: 2009-11-14                       |
| Type notebook() for the GUI, and license() for information.        |
/home/ghitza/.sage/temp/artin/9098/_home_ghitza__sage_init_sage_0.py in <module>()

/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:6989)()

/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:7021)()

TypeError: unsupported operand parent(s) for '+': 'Cyclotomic Field of order 3 and degree 2' and 'Cyclotomic Field of order 4 and degree 2'
sage: a * b
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/ghitza/.sage/temp/artin/9098/_home_ghitza__sage_init_sage_0.py in <module>()

/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10248)()

/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:7021)()

TypeError: unsupported operand parent(s) for '*': 'Cyclotomic Field of order 3 and degree 2' and 'Cyclotomic Field of order 4 and degree 2'
```


I think it's a coercion problem.  If someone knows better, please change the trac component accordingly.


Issue created by migration from https://trac.sagemath.org/ticket/7589





---

archive/issue_comments_064696.json:
```json
{
    "body": "Has anyone looked at this ticket? I ran into this today and discover that the issue has been reported 4 years ago... This bug is particularly confusing for the user, especially when you read the doc that says \"Due to their default embedding into CC, cyclotomic number fields are all compatible\", and goes on to show the following example:\n\n```\n      sage: cf30 = CyclotomicField(30)\n      sage: cf5 = CyclotomicField(5)\n      sage: cf3 = CyclotomicField(3)\n      sage: cf30.gen() + cf5.gen() + cf3.gen()\n      zeta30^6 + zeta30^5 + zeta30 - 1\n```\n\nIt turns out Sage is able to compute that only because the first field contains the next two! Note the following test:\n\n```\n      \u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510\n      \u2502 Sage Version 6.2.beta7, Release Date: 2014-04-08                   \u2502\n      \u2502 Type \"notebook()\" for the browser-based notebook interface.        \u2502\n      \u2502 Type \"help()\" for help.                                            \u2502\n      \u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518\n      sage: cf15=CyclotomicField(15)\n      sage: cf5=CyclotomicField(5)\n      sage: cf3=CyclotomicField(3)\n      \n      sage: cf15.gen()+cf5.gen()+cf3.gen()\n      zeta15^5 + zeta15^3 + zeta15\n      \n      sage: cf5.gen()+cf3.gen()+cf15.gen()\n      Traceback (most recent call last)\n      ...\n      TypeError: unsupported operand parent(s) for '+': 'Cyclotomic Field of order 5 and degree 4'   and 'Cyclotomic Field of order 3 and degree 2'\n      \n      sage: cf5.gen()+cf3.gen()\n      Traceback (most recent call last)\n      ...\n      TypeError: unsupported operand parent(s) for '+': 'Cyclotomic Field of order 5 and degree 4' and 'Cyclotomic Field of order 3 and degree 2'\n      \n      sage: 0*cf15.gen()+cf5.gen()+cf3.gen()\n      zeta15^5 + zeta15^3\n```\n",
    "created_at": "2014-04-11T00:06:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7589#issuecomment-64696",
    "user": "vripoll"
}
```

Has anyone looked at this ticket? I ran into this today and discover that the issue has been reported 4 years ago... This bug is particularly confusing for the user, especially when you read the doc that says "Due to their default embedding into CC, cyclotomic number fields are all compatible", and goes on to show the following example:

```
      sage: cf30 = CyclotomicField(30)
      sage: cf5 = CyclotomicField(5)
      sage: cf3 = CyclotomicField(3)
      sage: cf30.gen() + cf5.gen() + cf3.gen()
      zeta30^6 + zeta30^5 + zeta30 - 1
```

It turns out Sage is able to compute that only because the first field contains the next two! Note the following test:

```
      ┌────────────────────────────────────────────────────────────────────┐
      │ Sage Version 6.2.beta7, Release Date: 2014-04-08                   │
      │ Type "notebook()" for the browser-based notebook interface.        │
      │ Type "help()" for help.                                            │
      └────────────────────────────────────────────────────────────────────┘
      sage: cf15=CyclotomicField(15)
      sage: cf5=CyclotomicField(5)
      sage: cf3=CyclotomicField(3)
      
      sage: cf15.gen()+cf5.gen()+cf3.gen()
      zeta15^5 + zeta15^3 + zeta15
      
      sage: cf5.gen()+cf3.gen()+cf15.gen()
      Traceback (most recent call last)
      ...
      TypeError: unsupported operand parent(s) for '+': 'Cyclotomic Field of order 5 and degree 4'   and 'Cyclotomic Field of order 3 and degree 2'
      
      sage: cf5.gen()+cf3.gen()
      Traceback (most recent call last)
      ...
      TypeError: unsupported operand parent(s) for '+': 'Cyclotomic Field of order 5 and degree 4' and 'Cyclotomic Field of order 3 and degree 2'
      
      sage: 0*cf15.gen()+cf5.gen()+cf3.gen()
      zeta15^5 + zeta15^3
```




---

archive/issue_comments_064697.json:
```json
{
    "body": "Changing keywords from \"\" to \"coercion, cyclotomic\".",
    "created_at": "2014-04-11T00:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7589#issuecomment-64697",
    "user": "vripoll"
}
```

Changing keywords from "" to "coercion, cyclotomic".



---

archive/issue_comments_064698.json:
```json
{
    "body": "see also the somehow related #20746",
    "created_at": "2016-08-31T15:41:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7589#issuecomment-64698",
    "user": "vdelecroix"
}
```

see also the somehow related #20746



---

archive/issue_comments_064699.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2018-04-30T16:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7589#issuecomment-64699",
    "user": "chapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064700.json:
```json
{
    "body": "first tentative, let us see what patchbot says\n----\nNew commits:",
    "created_at": "2018-04-30T16:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7589#issuecomment-64700",
    "user": "chapoton"
}
```

first tentative, let us see what patchbot says
----
New commits:



---

archive/issue_comments_064701.json:
```json
{
    "body": "Changing keywords from \"coercion, cyclotomic\" to \"coercion, cyclotomic, coxeter\".",
    "created_at": "2018-04-30T16:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7589#issuecomment-64701",
    "user": "chapoton"
}
```

Changing keywords from "coercion, cyclotomic" to "coercion, cyclotomic, coxeter".



---

archive/issue_comments_064702.json:
```json
{
    "body": "You should take care of embeddings. The map `add: CF(p) x CF(q) -> CF(lcm(p,q))` is not uniquely defined.",
    "created_at": "2018-04-30T16:58:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7589#issuecomment-64702",
    "user": "vdelecroix"
}
```

You should take care of embeddings. The map `add: CF(p) x CF(q) -> CF(lcm(p,q))` is not uniquely defined.



---

archive/issue_comments_064703.json:
```json
{
    "body": "Well. What we just add here is the information that we need to go through CF(lcm). No responsability is taken on the existence of a canonical coercion from CF(p) to CF(lcm). I guess that this already an existing thing..",
    "created_at": "2018-04-30T19:36:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7589#issuecomment-64703",
    "user": "chapoton"
}
```

Well. What we just add here is the information that we need to go through CF(lcm). No responsability is taken on the existence of a canonical coercion from CF(p) to CF(lcm). I guess that this already an existing thing..



---

archive/issue_comments_064704.json:
```json
{
    "body": "As Frederic said, this does not change the (canonical) coercions between cyclotomic fields but allows the analogous computation to\n\n```\nsage: R.<x,y> = ZZ[]\nsage: S.<y> = QQ[]\nsage: R.an_element() + S.an_element()\nx + y\nsage: _.parent()\nMultivariate Polynomial Ring in x, y over Rational Field\n```\n",
    "created_at": "2018-04-30T23:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7589#issuecomment-64704",
    "user": "tscrim"
}
```

As Frederic said, this does not change the (canonical) coercions between cyclotomic fields but allows the analogous computation to

```
sage: R.<x,y> = ZZ[]
sage: S.<y> = QQ[]
sage: R.an_element() + S.an_element()
x + y
sage: _.parent()
Multivariate Polynomial Ring in x, y over Rational Field
```




---

archive/issue_comments_064705.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-04-30T23:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7589#issuecomment-64705",
    "user": "tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064706.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2018-05-08T17:27:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7589#issuecomment-64706",
    "user": "vbraun"
}
```

Resolution: fixed
