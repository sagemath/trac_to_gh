# Issue 9701: NumberFieldElement should have a conversion to float

archive/issues_009701.json:
```json
{
    "body": "Assignee: @loefflerd\n\nThe missing conversion from `NumberFieldElement` to float is the cause of this strangeness:\n\n\n```\nsage: RR(I*I)\n-1.00000000000000\nsage: float(I*I)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/cwitty/svn-ironpython/IronPython_Main/<ipython console> in <module>()\n\n/home/cwitty/sage-4.5.2.alpha1/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__float__ (sage/symbolic/expression.cpp:5205)()\n\nTypeError: unable to simplify to float approximation\n```\n\n\n(I'll have a patch posted for this in a few minutes.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/9701\n\n",
    "created_at": "2010-08-07T00:37:10Z",
    "labels": [
        "component: number fields",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "NumberFieldElement should have a conversion to float",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9701",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @loefflerd

The missing conversion from `NumberFieldElement` to float is the cause of this strangeness:


```
sage: RR(I*I)
-1.00000000000000
sage: float(I*I)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/cwitty/svn-ironpython/IronPython_Main/<ipython console> in <module>()

/home/cwitty/sage-4.5.2.alpha1/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__float__ (sage/symbolic/expression.cpp:5205)()

TypeError: unable to simplify to float approximation
```


(I'll have a patch posted for this in a few minutes.)

Issue created by migration from https://trac.sagemath.org/ticket/9701





---

archive/issue_comments_094180.json:
```json
{
    "body": "Attachment [trac_9701-float-of-number-field-element.patch](tarball://root/attachments/some-uuid/ticket9701/trac_9701-float-of-number-field-element.patch) by cwitty created at 2010-08-07 01:17:34\n\nThe attached patch adds the missing method and adds a doctest in symbolics where I originally saw the problem.\n\nAll doctests pass.",
    "created_at": "2010-08-07T01:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9701#issuecomment-94180",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac_9701-float-of-number-field-element.patch](tarball://root/attachments/some-uuid/ticket9701/trac_9701-float-of-number-field-element.patch) by cwitty created at 2010-08-07 01:17:34

The attached patch adds the missing method and adds a doctest in symbolics where I originally saw the problem.

All doctests pass.



---

archive/issue_comments_094181.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-07T01:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9701#issuecomment-94181",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_094182.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-09-23T10:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9701#issuecomment-94182",
    "user": "https://github.com/loefflerd"
}
```

Looks good to me.



---

archive/issue_comments_094183.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-23T10:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9701#issuecomment-94183",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094184.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T04:23:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9701#issuecomment-94184",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
