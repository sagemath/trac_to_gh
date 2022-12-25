# Issue 4781: creation of relative number fields when defining polynomial not integral is broken

archive/issues_004781.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: K.<a> = NumberField(x^2 + 1)\nsage: L.<b> = NumberField(K['y'].0^2 + 1/2)\n---------------------------------------------------------------------------\nPariError                                 Traceback (most recent call last)\n\n/Users/wstein/sage/build/sage-3.2.2.alpha0/<ipython console> in <module>()\n\n/Users/wstein/sage/build/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in NumberField(polynomial, name, check, names, cache, embedding)\n    374 \n    375     if isinstance(R, NumberField_generic):\n--> 376         S = R.extension(polynomial, name, check=check)\n    377         if cache:\n    378             _nf_cache[key] = weakref.ref(S)\n\n/Users/wstein/sage/build/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in extension(self, poly, name, names, check, embedding)\n   2570         if name is None:\n   2571             raise TypeError, \"the variable name must be specified.\"\n-> 2572         return NumberField_relative(self, poly, str(name), check=check, embedding=embedding)\n   2573 \n   2574     def factor(self, n):\n\n/Users/wstein/sage/build/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in __init__(self, base, polynomial, name, latex_name, names, check, embedding)\n   4567 \n   4568         self.__pari_relative_polynomial = pari(str(polynomial_y))\n-> 4569         self.__rnf = self.__base_nf.rnfinit(self.__pari_relative_polynomial)\n   4570         \n   4571         self.__base_field = base\n\n/Users/wstein/sage/build/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:38578)()\n\nPariError: impossible inverse modulo:  (36)\n> /Users/wstein/sage/build/sage-3.2.2.alpha0/gen.pyx(8050)sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:38578)()\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4781\n\n",
    "created_at": "2008-12-13T03:16:45Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "creation of relative number fields when defining polynomial not integral is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4781",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
sage: K.<a> = NumberField(x^2 + 1)
sage: L.<b> = NumberField(K['y'].0^2 + 1/2)
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

PariError: impossible inverse modulo:  (36)
> /Users/wstein/sage/build/sage-3.2.2.alpha0/gen.pyx(8050)sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:38578)()

```


Issue created by migration from https://trac.sagemath.org/ticket/4781





---

archive/issue_comments_036169.json:
```json
{
    "body": "Seems to be fine now (3.4):\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: K.<a> = NumberField(x^2 + 1)\nsage: L.<b> = NumberField(K['y'].0^2 + 1/2)\nsage: L\nNumber Field in b with defining polynomial y^2 + 1/2 over its base field\n```\n",
    "created_at": "2009-03-13T09:04:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4781#issuecomment-36169",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Seems to be fine now (3.4):

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: K.<a> = NumberField(x^2 + 1)
sage: L.<b> = NumberField(K['y'].0^2 + 1/2)
sage: L
Number Field in b with defining polynomial y^2 + 1/2 over its base field
```




---

archive/issue_comments_036170.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-03-13T09:04:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4781#issuecomment-36170",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Changing priority from major to minor.



---

archive/issue_comments_036171.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-21T08:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4781#issuecomment-36171",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_036172.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-21T08:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4781#issuecomment-36172",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_036173.json:
```json
{
    "body": "In the above example, you can create the field L but you can't do much with it (for instance, `L.absolute_discriminant()` fails). But I would argue that this is covered by ticket #252. I propose closing this ticket as \"duplicate\".",
    "created_at": "2009-07-21T08:31:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4781#issuecomment-36173",
    "user": "https://github.com/loefflerd"
}
```

In the above example, you can create the field L but you can't do much with it (for instance, `L.absolute_discriminant()` fails). But I would argue that this is covered by ticket #252. I propose closing this ticket as "duplicate".



---

archive/issue_comments_036174.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-07-22T18:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4781#issuecomment-36174",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: duplicate



---

archive/issue_events_005023.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-22T18:20:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4781",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4781#event-5023"
}
```



---

archive/issue_comments_036175.json:
```json
{
    "body": "Closing this as a duplicate of #252.",
    "created_at": "2009-07-22T18:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4781#issuecomment-36175",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Closing this as a duplicate of #252.
