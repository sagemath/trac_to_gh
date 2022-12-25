# Issue 4780: relative number field constructor -- error message when given poly of degree < 1 is bad

archive/issues_004780.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: K.<a> = NumberField(x^2 + 1)\nsage: L.<b> = NumberField(K['y'](1))\n---------------------------------------------------------------------------\nPariError                                 Traceback (most recent call last)\n\n/Users/wstein/sage/build/sage-3.2.2.alpha0/<ipython console> in <module>()\n\n/Users/wstein/sage/build/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in NumberField(polynomial, name, check, names, cache, embedding)\n    374 \n    375     if isinstance(R, NumberField_generic):\n--> 376         S = R.extension(polynomial, name, check=check)\n    377         if cache:\n    378             _nf_cache[key] = weakref.ref(S)\n\n/Users/wstein/sage/build/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in extension(self, poly, name, names, check, embedding)\n   2570         if name is None:\n   2571             raise TypeError, \"the variable name must be specified.\"\n-> 2572         return NumberField_relative(self, poly, str(name), check=check, embedding=embedding)\n   2573 \n   2574     def factor(self, n):\n\n/Users/wstein/sage/build/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in __init__(self, base, polynomial, name, latex_name, names, check, embedding)\n   4567 \n   4568         self.__pari_relative_polynomial = pari(str(polynomial_y))\n-> 4569         self.__rnf = self.__base_nf.rnfinit(self.__pari_relative_polynomial)\n   4570         \n   4571         self.__base_field = base\n\n/Users/wstein/sage/build/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:38578)()\n\nPariError: not a polynomial (38)\n> /Users/wstein/sage/build/sage-3.2.2.alpha0/gen.pyx(8050)sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:38578)()\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4780\n\n",
    "created_at": "2008-12-13T03:14:59Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "relative number field constructor -- error message when given poly of degree < 1 is bad",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4780",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
sage: K.<a> = NumberField(x^2 + 1)
sage: L.<b> = NumberField(K['y'](1))
---------------------------------------------------------------------------
PariError                                 Traceback (most recent call last)

/Users/wstein/sage/build/sage-3.2.2.alpha0/<ipython console> in <module>()

/Users/wstein/sage/build/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in NumberField(polynomial, name, check, names, cache, embedding)
    374 
    375     if isinstance(R, NumberField_generic):
--> 376         S = R.extension(polynomial, name, check=check)
    377         if cache:
    378             _nf_cache[key] = weakref.ref(S)

/Users/wstein/sage/build/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in extension(self, poly, name, names, check, embedding)
   2570         if name is None:
   2571             raise TypeError, "the variable name must be specified."
-> 2572         return NumberField_relative(self, poly, str(name), check=check, embedding=embedding)
   2573 
   2574     def factor(self, n):

/Users/wstein/sage/build/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in __init__(self, base, polynomial, name, latex_name, names, check, embedding)
   4567 
   4568         self.__pari_relative_polynomial = pari(str(polynomial_y))
-> 4569         self.__rnf = self.__base_nf.rnfinit(self.__pari_relative_polynomial)
   4570         
   4571         self.__base_field = base

/Users/wstein/sage/build/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:38578)()

PariError: not a polynomial (38)
> /Users/wstein/sage/build/sage-3.2.2.alpha0/gen.pyx(8050)sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:38578)()

```


Issue created by migration from https://trac.sagemath.org/ticket/4780





---

archive/issue_comments_036161.json:
```json
{
    "body": "This seems to be better now:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: sage: K.<a> = NumberField(x^2 + 1)\nsage: sage: L.<b> = NumberField(K['y'](1))\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n| Sage Version 4.0.1.rc1, Release Date: 2009-06-04                   |\n| Type notebook() for the GUI, and license() for information.        |\n/home/mhansen/.sage/temp/sage.math.washington.edu/25032/_home_mhansen__sage_init_sage_0.py in <module>()\n\n/scratch/mhansen/release/4.0.1/rc1/sage-4.0.1.rc1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in NumberField(polynomial, name, check, names, cache, embedding)\n    415 \n    416     if isinstance(R, NumberField_generic):\n--> 417         S = R.extension(polynomial, name, check=check)\n    418         if cache:\n    419             _nf_cache[key] = weakref.ref(S)\n\n/scratch/mhansen/release/4.0.1/rc1/sage-4.0.1.rc1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in extension(self, poly, name, names, check, embedding)\n   2920             raise TypeError, \"the variable name must be specified.\"\n   2921         from sage.rings.number_field.number_field_rel import NumberField_relative\n-> 2922         return NumberField_relative(self, poly, str(name), check=check, embedding=embedding)\n   2923 \n   2924     def factor(self, n):\n\n/scratch/mhansen/release/4.0.1/rc1/sage-4.0.1.rc1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field_rel.pyc in __init__(self, base, polynomial, name, latex_name, names, check, embedding)\n    274                 # future, is_irreducible should be made faster for\n    275                 # polynomials over number fields -- see ticket #4724\n--> 276                 raise ValueError, \"defining polynomial (%s) must be irreducible\"%polynomial\n    277 \n    278         self.__gens = [None]\n\nValueError: defining polynomial (1) must be irreducible\n```\n\n\nComments?",
    "created_at": "2009-06-04T23:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4780#issuecomment-36161",
    "user": "https://github.com/mwhansen"
}
```

This seems to be better now:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: K.<a> = NumberField(x^2 + 1)
sage: sage: L.<b> = NumberField(K['y'](1))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
| Sage Version 4.0.1.rc1, Release Date: 2009-06-04                   |
| Type notebook() for the GUI, and license() for information.        |
/home/mhansen/.sage/temp/sage.math.washington.edu/25032/_home_mhansen__sage_init_sage_0.py in <module>()

/scratch/mhansen/release/4.0.1/rc1/sage-4.0.1.rc1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in NumberField(polynomial, name, check, names, cache, embedding)
    415 
    416     if isinstance(R, NumberField_generic):
--> 417         S = R.extension(polynomial, name, check=check)
    418         if cache:
    419             _nf_cache[key] = weakref.ref(S)

/scratch/mhansen/release/4.0.1/rc1/sage-4.0.1.rc1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in extension(self, poly, name, names, check, embedding)
   2920             raise TypeError, "the variable name must be specified."
   2921         from sage.rings.number_field.number_field_rel import NumberField_relative
-> 2922         return NumberField_relative(self, poly, str(name), check=check, embedding=embedding)
   2923 
   2924     def factor(self, n):

/scratch/mhansen/release/4.0.1/rc1/sage-4.0.1.rc1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field_rel.pyc in __init__(self, base, polynomial, name, latex_name, names, check, embedding)
    274                 # future, is_irreducible should be made faster for
    275                 # polynomials over number fields -- see ticket #4724
--> 276                 raise ValueError, "defining polynomial (%s) must be irreducible"%polynomial
    277 
    278         self.__gens = [None]

ValueError: defining polynomial (1) must be irreducible
```


Comments?



---

archive/issue_comments_036162.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-20T20:30:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4780#issuecomment-36162",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_036163.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-20T20:30:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4780#issuecomment-36163",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_036164.json:
```json
{
    "body": "Can this be closed now?",
    "created_at": "2012-03-29T07:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4780#issuecomment-36164",
    "user": "https://github.com/mwhansen"
}
```

Can this be closed now?



---

archive/issue_comments_036165.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-03-29T07:47:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4780#issuecomment-36165",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_036166.json:
```json
{
    "body": "Yes, I think so.",
    "created_at": "2012-03-29T07:47:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4780#issuecomment-36166",
    "user": "https://github.com/loefflerd"
}
```

Yes, I think so.



---

archive/issue_comments_036167.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-29T07:48:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4780#issuecomment-36167",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_036168.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2012-04-04T13:27:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4780#issuecomment-36168",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme



---

archive/issue_events_005022.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2012-04-04T13:27:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4780",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4780#event-5022"
}
```
