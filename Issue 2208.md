# Issue 2208: implement is_field for rings of integers

archive/issues_002208.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: R = CyclotomicField(4).ring_of_integers()\nsage: R.is_field()\n---------------------------------------------------------------------------\n<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)\n\n/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/<ipython console> in <module>()\n\n/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/ring.pyx in sage.rings.ring.IntegralDomain.is_field()\n\n/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/ring.pyx in sage.rings.ring.Ring.is_finite()\n\n<type 'exceptions.NotImplementedError'>: \n```\n\n\nAlso\n\n```\nsage: R = NumberField(x^3 + 2, 'a').ring_of_integers()\nsage: R.is_field()\n---------------------------------------------------------------------------\n<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)\n\n/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/<ipython console> in <module>()\n\n/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/ring.pyx in sage.rings.ring.IntegralDomain.is_field()\n\n/Users/was/build/sage-2.10.2.alpha0/devel/sage-review/sage/modular/ring.pyx in sage.rings.ring.Ring.is_finite()\n\n<type 'exceptions.NotImplementedError'>:\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2208\n\n",
    "created_at": "2008-02-19T02:29:00Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "implement is_field for rings of integers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2208",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


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

archive/issue_comments_014548.json:
```json
{
    "body": "Made the obvious fix, both the examples above now work (though there are different doctests).",
    "created_at": "2008-02-19T03:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2208#issuecomment-14548",
    "user": "https://github.com/craigcitro"
}
```

Made the obvious fix, both the examples above now work (though there are different doctests).



---

archive/issue_comments_014549.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-19T03:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2208#issuecomment-14549",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014550.json:
```json
{
    "body": "Changing assignee from @williamstein to @craigcitro.",
    "created_at": "2008-02-19T03:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2208#issuecomment-14550",
    "user": "https://github.com/craigcitro"
}
```

Changing assignee from @williamstein to @craigcitro.



---

archive/issue_comments_014551.json:
```json
{
    "body": "I would delete \"This exists for compatibility purposes.\" from the docstring.   It really says nothing useful and if we're going to write that we could write that sort of thing all over the place.",
    "created_at": "2008-02-19T04:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2208#issuecomment-14551",
    "user": "https://github.com/williamstein"
}
```

I would delete "This exists for compatibility purposes." from the docstring.   It really says nothing useful and if we're going to write that we could write that sort of thing all over the place.



---

archive/issue_comments_014552.json:
```json
{
    "body": "Attachment [trac-2208.patch](tarball://root/attachments/some-uuid/ticket2208/trac-2208.patch) by @craigcitro created at 2008-02-19 04:30:18\n\nNew patch posted, removes the questionable verbiage. Adds another doctest.",
    "created_at": "2008-02-19T04:30:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2208#issuecomment-14552",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-2208.patch](tarball://root/attachments/some-uuid/ticket2208/trac-2208.patch) by @craigcitro created at 2008-02-19 04:30:18

New patch posted, removes the questionable verbiage. Adds another doctest.



---

archive/issue_comments_014553.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-02-21T07:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2208#issuecomment-14553",
    "user": "https://github.com/ncalexan"
}
```

Looks good to me.



---

archive/issue_comments_014554.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-25T01:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2208#issuecomment-14554",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014555.json:
```json
{
    "body": "Merged in Sage 2.10.3.alpha0",
    "created_at": "2008-02-25T01:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2208#issuecomment-14555",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.alpha0
