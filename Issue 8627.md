# Issue 8627: cannot coerce p-adic capped-rel to capped-abs

archive/issues_008627.json:
```json
{
    "body": "Assignee: roed\n\n(sage 4.3.1)\n\n\n```\nsage: R.<a> = Zq(25, type=\"capped-abs\")\nsage: R(1/a)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/david/<ipython console> in <module>()\n\n/Users/david/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4956)()\n\n/Users/david/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap._call_ (sage/structure/coerce_maps.c:2434)()\n\n/Users/david/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap._call_ (sage/structure/coerce_maps.c:2332)()\n\n/Users/david/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/padics/padic_ZZ_pX_CA_element.so in sage.rings.padics.padic_ZZ_pX_CA_element.pAdicZZpXCAElement.__init__ (sage/rings/padics/padic_ZZ_pX_CA_element.cpp:4574)()\n\nTypeError: Cannot convert sage.rings.padics.padic_ZZ_pX_CR_element.pAdicZZpXCRElement to sage.rings.padics.padic_ZZ_pX_CA_element.pAdicZZpXCAElement\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8627\n\n",
    "created_at": "2010-03-30T00:47:56Z",
    "labels": [
        "padics",
        "major",
        "bug"
    ],
    "title": "cannot coerce p-adic capped-rel to capped-abs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8627",
    "user": "dmharvey"
}
```
Assignee: roed

(sage 4.3.1)


```
sage: R.<a> = Zq(25, type="capped-abs")
sage: R(1/a)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/david/<ipython console> in <module>()

/Users/david/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4956)()

/Users/david/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap._call_ (sage/structure/coerce_maps.c:2434)()

/Users/david/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap._call_ (sage/structure/coerce_maps.c:2332)()

/Users/david/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/padics/padic_ZZ_pX_CA_element.so in sage.rings.padics.padic_ZZ_pX_CA_element.pAdicZZpXCAElement.__init__ (sage/rings/padics/padic_ZZ_pX_CA_element.cpp:4574)()

TypeError: Cannot convert sage.rings.padics.padic_ZZ_pX_CR_element.pAdicZZpXCRElement to sage.rings.padics.padic_ZZ_pX_CA_element.pAdicZZpXCAElement
```



Issue created by migration from https://trac.sagemath.org/ticket/8627





---

archive/issue_comments_078219.json:
```json
{
    "body": "Works now.  Need to add a doctest.",
    "created_at": "2016-02-16T20:39:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8627#issuecomment-78219",
    "user": "roed"
}
```

Works now.  Need to add a doctest.



---

archive/issue_comments_078220.json:
```json
{
    "body": "There is already a doctest for this.",
    "created_at": "2016-03-21T15:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8627#issuecomment-78220",
    "user": "rozenszt"
}
```

There is already a doctest for this.



---

archive/issue_comments_078221.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-03-21T15:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8627#issuecomment-78221",
    "user": "rozenszt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078222.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-03-21T15:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8627#issuecomment-78222",
    "user": "rozenszt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078223.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2016-03-26T12:01:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8627#issuecomment-78223",
    "user": "vbraun"
}
```

Resolution: invalid
