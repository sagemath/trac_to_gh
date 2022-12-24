# Issue 3103: coercion errors of vectors from ZZ^2 and QQ^2 into CDF^2

archive/issues_003103.json:
```json
{
    "body": "Assignee: was\n\nCC:  ncalexan rbradshaw jason\n\nKeywords: vector CDF coerce\n\nWith\n\n```\nsage: version()\n'SAGE Version 3.0.1.alpha0, Release Date: 2008-04-26'\n```\n\nI get the following coercion errors:\n\n\n```\nsage: vector(CDF, [2, 2]) * vector(ZZ, [1, 3])\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/ncalexan/sage-3.0.1.alpha0/devel/sage-nca/sage/rings/<ipython console> in <module>()\n\n/Users/ncalexan/sage-3.0.1.alpha0/devel/sage-nca/sage/rings/element.pyx in sage.structure.element.Vector.__mul__ (sage/structure/element.c:10413)()\n\n/Users/ncalexan/sage-3.0.1.alpha0/devel/sage-nca/sage/rings/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/structure/coerce.c:5292)()\n\n<type 'exceptions.TypeError'>: unsupported operand parent(s) for '*': 'Vector space of dimension 2 over Complex Double Field' and 'Ambient free module of rank 2 over the principal ideal domain Integer Ring'\nsage: vector(CDF, [2, 2]) * vector(QQ, [1, 3])\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/ncalexan/sage-3.0.1.alpha0/devel/sage-nca/sage/rings/<ipython console> in <module>()\n\n/Users/ncalexan/sage-3.0.1.alpha0/devel/sage-nca/sage/rings/element.pyx in sage.structure.element.Vector.__mul__ (sage/structure/element.c:10413)()\n\n/Users/ncalexan/sage-3.0.1.alpha0/devel/sage-nca/sage/rings/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/structure/coerce.c:5292)()\n\n<type 'exceptions.TypeError'>: unsupported operand parent(s) for '*': 'Vector space of dimension 2 over Complex Double Field' and 'Vector space of dimension 2 over Rational Field'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3103\n\n",
    "created_at": "2008-05-05T04:12:05Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "coercion errors of vectors from ZZ^2 and QQ^2 into CDF^2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3103",
    "user": "ncalexan"
}
```
Assignee: was

CC:  ncalexan rbradshaw jason

Keywords: vector CDF coerce

With

```
sage: version()
'SAGE Version 3.0.1.alpha0, Release Date: 2008-04-26'
```

I get the following coercion errors:


```
sage: vector(CDF, [2, 2]) * vector(ZZ, [1, 3])
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/ncalexan/sage-3.0.1.alpha0/devel/sage-nca/sage/rings/<ipython console> in <module>()

/Users/ncalexan/sage-3.0.1.alpha0/devel/sage-nca/sage/rings/element.pyx in sage.structure.element.Vector.__mul__ (sage/structure/element.c:10413)()

/Users/ncalexan/sage-3.0.1.alpha0/devel/sage-nca/sage/rings/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/structure/coerce.c:5292)()

<type 'exceptions.TypeError'>: unsupported operand parent(s) for '*': 'Vector space of dimension 2 over Complex Double Field' and 'Ambient free module of rank 2 over the principal ideal domain Integer Ring'
sage: vector(CDF, [2, 2]) * vector(QQ, [1, 3])
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/ncalexan/sage-3.0.1.alpha0/devel/sage-nca/sage/rings/<ipython console> in <module>()

/Users/ncalexan/sage-3.0.1.alpha0/devel/sage-nca/sage/rings/element.pyx in sage.structure.element.Vector.__mul__ (sage/structure/element.c:10413)()

/Users/ncalexan/sage-3.0.1.alpha0/devel/sage-nca/sage/rings/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/structure/coerce.c:5292)()

<type 'exceptions.TypeError'>: unsupported operand parent(s) for '*': 'Vector space of dimension 2 over Complex Double Field' and 'Vector space of dimension 2 over Rational Field'
```


Issue created by migration from https://trac.sagemath.org/ticket/3103





---

archive/issue_comments_021433.json:
```json
{
    "body": "This is not due to coercion, but rather that dot product is not implemented for CDF^n. \n\n\n```\nsage: (CDF^2)([1,2]) * (CDF^2)([2,3])\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\n  File \"element.pyx\", line 1884, in sage.structure.element.Vector.__mul__ (sage/structure/element.c:10398)\n  File \"element.pyx\", line 1898, in sage.structure.element.Vector._dot_product_c (sage/structure/element.c:10564)\n  File \"element.pyx\", line 1904, in sage.structure.element.Vector._dot_product_c_impl (sage/structure/element.c:10649)\n<type 'exceptions.TypeError'>: unsupported operand parent(s) for '*': 'Vector space of dimension 2 over Complex Double Field' and 'Vector space of dimension 2 over Complex Double Field'\n```\n\n\nWhich, looking at element.pyx line 1904 shows that _dot_product_c_impl was never implemented for CDF. This should almost certainly be a NotImplementedError, or something like that, not a TypeError. In fact, there should just be a generic implementation.",
    "created_at": "2008-05-08T16:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3103#issuecomment-21433",
    "user": "robertwb"
}
```

This is not due to coercion, but rather that dot product is not implemented for CDF^n. 


```
sage: (CDF^2)([1,2]) * (CDF^2)([2,3])
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "element.pyx", line 1884, in sage.structure.element.Vector.__mul__ (sage/structure/element.c:10398)
  File "element.pyx", line 1898, in sage.structure.element.Vector._dot_product_c (sage/structure/element.c:10564)
  File "element.pyx", line 1904, in sage.structure.element.Vector._dot_product_c_impl (sage/structure/element.c:10649)
<type 'exceptions.TypeError'>: unsupported operand parent(s) for '*': 'Vector space of dimension 2 over Complex Double Field' and 'Vector space of dimension 2 over Complex Double Field'
```


Which, looking at element.pyx line 1904 shows that _dot_product_c_impl was never implemented for CDF. This should almost certainly be a NotImplementedError, or something like that, not a TypeError. In fact, there should just be a generic implementation.



---

archive/issue_comments_021434.json:
```json
{
    "body": "The attached patch fixes the errors (they were in fact dot_product errors and not coercion) and adds doctests and functionality for preserving inner product matrices.",
    "created_at": "2008-06-18T04:37:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3103#issuecomment-21434",
    "user": "ncalexan"
}
```

The attached patch fixes the errors (they were in fact dot_product errors and not coercion) and adds doctests and functionality for preserving inner product matrices.



---

archive/issue_comments_021435.json:
```json
{
    "body": "The patch solves the problem and cleans up a lot of old code.",
    "created_at": "2008-06-18T08:56:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3103#issuecomment-21435",
    "user": "robertwb"
}
```

The patch solves the problem and cleans up a lot of old code.



---

archive/issue_comments_021436.json:
```json
{
    "body": "This patch causes a number of doctest failures:\n\n```\n        sage -t -long devel/sage/sage/modular/modsym/space.py # 5 doctests failed\n        sage -t -long devel/sage/sage/modular/modform/constructor.py # 3 doctests failed\n        sage -t -long devel/sage/sage/modular/hecke/module.py # 12 doctests failed\n        sage -t -long devel/sage/sage/modular/abvar/abvar_newform.py # 19 doctests failed\n        sage -t -long devel/sage/sage/modular/abvar/abvar_ambient_jacobian.py # 2 doctests failed\n        sage -t -long devel/sage/sage/modular/abvar/abvar.py # 3 doctests failed\n        sage -t -long devel/sage/sage/modular/abvar/homspace.py # 2 doctests failed\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-06-23T04:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3103#issuecomment-21436",
    "user": "mabshoff"
}
```

This patch causes a number of doctest failures:

```
        sage -t -long devel/sage/sage/modular/modsym/space.py # 5 doctests failed
        sage -t -long devel/sage/sage/modular/modform/constructor.py # 3 doctests failed
        sage -t -long devel/sage/sage/modular/hecke/module.py # 12 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/abvar_newform.py # 19 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/abvar_ambient_jacobian.py # 2 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/abvar.py # 3 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/homspace.py # 2 doctests failed
```


Cheers,

Michael



---

archive/issue_comments_021437.json:
```json
{
    "body": "In Sage 3.4.1.rc2, this works:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: vector(CDF, [2, 2]) * vector(ZZ, [1, 3])\n8.0\n```\n\n| Sage Version 3.4.1.rc2, Release Date: 2009-04-10                   |\n| Type notebook() for the GUI, and license() for information.        |\nSo this sounds like it is fixed.  However, are there nice doctests from the above patch that could be added to the current code?  Nick?",
    "created_at": "2009-04-15T06:17:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3103#issuecomment-21437",
    "user": "jason"
}
```

In Sage 3.4.1.rc2, this works:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: vector(CDF, [2, 2]) * vector(ZZ, [1, 3])
8.0
```

| Sage Version 3.4.1.rc2, Release Date: 2009-04-10                   |
| Type notebook() for the GUI, and license() for information.        |
So this sounds like it is fixed.  However, are there nice doctests from the above patch that could be added to the current code?  Nick?



---

archive/issue_comments_021438.json:
```json
{
    "body": "Yes, I agree with Jason. Once we add a patch that adds a doctest this ticket can be merged and closed. By maybe someone ought to check out if Nick's patch contains anything else.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T06:36:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3103#issuecomment-21438",
    "user": "mabshoff"
}
```

Yes, I agree with Jason. Once we add a patch that adds a doctest this ticket can be merged and closed. By maybe someone ought to check out if Nick's patch contains anything else.

Cheers,

Michael



---

archive/issue_comments_021439.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-01-12T12:36:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3103#issuecomment-21439",
    "user": "Bouillaguet"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_021440.json:
```json
{
    "body": "Since the problem has been fixed, here is a very simple doctest that enforces it won't happen again.\n\nPatchbot !\n\napply trac_3103_add_doctest.patch",
    "created_at": "2013-01-12T12:36:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3103#issuecomment-21440",
    "user": "Bouillaguet"
}
```

Since the problem has been fixed, here is a very simple doctest that enforces it won't happen again.

Patchbot !

apply trac_3103_add_doctest.patch



---

archive/issue_comments_021441.json:
```json
{
    "body": "Attachment [trac_3103_add_doctest.patch](tarball://root/attachments/some-uuid/ticket3103/trac_3103_add_doctest.patch) by Bouillaguet created at 2013-01-20 10:43:23",
    "created_at": "2013-01-20T10:43:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3103#issuecomment-21441",
    "user": "Bouillaguet"
}
```

Attachment [trac_3103_add_doctest.patch](tarball://root/attachments/some-uuid/ticket3103/trac_3103_add_doctest.patch) by Bouillaguet created at 2013-01-20 10:43:23



---

archive/issue_comments_021442.json:
```json
{
    "body": "took care of stupid TAB in the patch",
    "created_at": "2013-01-20T10:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3103#issuecomment-21442",
    "user": "Bouillaguet"
}
```

took care of stupid TAB in the patch



---

archive/issue_comments_021443.json:
```json
{
    "body": "Apply only trac_3103_add_doctest.patch",
    "created_at": "2013-01-21T19:51:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3103#issuecomment-21443",
    "user": "robertwb"
}
```

Apply only trac_3103_add_doctest.patch



---

archive/issue_comments_021444.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-22T00:34:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3103#issuecomment-21444",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_021445.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-01-25T13:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3103#issuecomment-21445",
    "user": "jdemeyer"
}
```

Resolution: fixed
