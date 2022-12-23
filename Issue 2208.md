# Issue 2208: implement is_field for rings of integers

archive/issues_002208.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: R = CyclotomicField(4).ring_of_integers()\nsage: R.is_field()\n---------------------------------------------------------------------------\n<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)\n\n/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/<ipython console> in <module>()\n\n/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/ring.pyx in sage.rings.ring.IntegralDomain.is_field()\n\n/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/ring.pyx in sage.rings.ring.Ring.is_finite()\n\n<type 'exceptions.NotImplementedError'>: \n```\n\n\nAlso\n\n```\nsage: R = NumberField(x^3 + 2, 'a').ring_of_integers()\nsage: R.is_field()\n---------------------------------------------------------------------------\n<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)\n\n/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/<ipython console> in <module>()\n\n/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/ring.pyx in sage.rings.ring.IntegralDomain.is_field()\n\n/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/ring.pyx in sage.rings.ring.Ring.is_finite()\n\n<type 'exceptions.NotImplementedError'>:\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2208\n\n",
    "created_at": "2008-02-19T02:29:00Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "implement is_field for rings of integers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2208",
    "user": "was"
}
```
Assignee: was


```
sage: R = CyclotomicField(4).ring_of_integers()
sage: R.is_field()
---------------------------------------------------------------------------
<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)

/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/<ipython console> in <module>()

/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/ring.pyx in sage.rings.ring.IntegralDomain.is_field()

/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/ring.pyx in sage.rings.ring.Ring.is_finite()

<type 'exceptions.NotImplementedError'>: 
```


Also

```
sage: R = NumberField(x^3 + 2, 'a').ring_of_integers()
sage: R.is_field()
---------------------------------------------------------------------------
<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)

/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/<ipython console> in <module>()

/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/ring.pyx in sage.rings.ring.IntegralDomain.is_field()

/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/ring.pyx in sage.rings.ring.Ring.is_finite()

<type 'exceptions.NotImplementedError'>:
```


Issue created by migration from https://trac.sagemath.org/ticket/2208





---

archive/issue_comments_014579.json:
```json
{
    "body": "Made the obvious fix, both the examples above now work (though there are different doctests).",
    "created_at": "2008-02-19T03:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2208#issuecomment-14579",
    "user": "craigcitro"
}
```

Made the obvious fix, both the examples above now work (though there are different doctests).



---

archive/issue_comments_014580.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-19T03:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2208#issuecomment-14580",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014581.json:
```json
{
    "body": "Changing assignee from was to craigcitro.",
    "created_at": "2008-02-19T03:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2208#issuecomment-14581",
    "user": "craigcitro"
}
```

Changing assignee from was to craigcitro.



---

archive/issue_comments_014582.json:
```json
{
    "body": "I would delete \"This exists for compatibility purposes.\" from the docstring.   It really says nothing useful and if we're going to write that we could write that sort of thing all over the place.",
    "created_at": "2008-02-19T04:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2208#issuecomment-14582",
    "user": "was"
}
```

I would delete "This exists for compatibility purposes." from the docstring.   It really says nothing useful and if we're going to write that we could write that sort of thing all over the place.



---

archive/issue_comments_014583.json:
```json
{
    "body": "Attachment\n\nNew patch posted, removes the questionable verbiage. Adds another doctest.",
    "created_at": "2008-02-19T04:30:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2208#issuecomment-14583",
    "user": "craigcitro"
}
```

Attachment

New patch posted, removes the questionable verbiage. Adds another doctest.



---

archive/issue_comments_014584.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-02-21T07:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2208#issuecomment-14584",
    "user": "ncalexan"
}
```

Looks good to me.



---

archive/issue_comments_014585.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-25T01:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2208#issuecomment-14585",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014586.json:
```json
{
    "body": "Merged in Sage 2.10.3.alpha0",
    "created_at": "2008-02-25T01:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2208#issuecomment-14586",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.alpha0
