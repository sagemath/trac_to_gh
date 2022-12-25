# Issue 882: 2.8.7-alpha0: doctest failures due to RR->ZZ coercion patch

archive/issues_000882.json:
```json
{
    "body": "Assignee: somebody\n\n2.8.6 behavior:\n\n```\nsage: 2.5 in ZZ\nFalse\n```\n\n\n2.8.7-alpha0 behavior:\n\n```\nsage: 2.5 in ZZ\n---------------------------------------------------------------------------\n<type 'exceptions.ValueError'>            Traceback (most recent call last)\n\n/home/cwitty/pre-sage/<ipython console> in <module>()\n\n/home/cwitty/pre-sage/parent.pyx in parent.Parent.__contains__()\n\n/home/cwitty/pre-sage/integer_ring.pyx in integer_ring.IntegerRing_class.__call__()\n\n/home/cwitty/pre-sage/integer.pyx in integer.Integer.__init__()\n\n/home/cwitty/pre-sage/real_mpfr.pyx in real_mpfr.RealNumber._integer_()\n\n<type 'exceptions.ValueError'>: Attempt to coerce non-integral RealNumber to Integer\n```\n\n\nI'm pretty sure this is the underlying cause behind several 2.8.7-alpha0 doctest failures.\n\nI have prepared a patch for this, which I will be testing shortly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/882\n\n",
    "created_at": "2007-10-13T19:45:40Z",
    "labels": [
        "component: basic arithmetic",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "2.8.7-alpha0: doctest failures due to RR->ZZ coercion patch",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/882",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: somebody

2.8.6 behavior:

```
sage: 2.5 in ZZ
False
```


2.8.7-alpha0 behavior:

```
sage: 2.5 in ZZ
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/home/cwitty/pre-sage/<ipython console> in <module>()

/home/cwitty/pre-sage/parent.pyx in parent.Parent.__contains__()

/home/cwitty/pre-sage/integer_ring.pyx in integer_ring.IntegerRing_class.__call__()

/home/cwitty/pre-sage/integer.pyx in integer.Integer.__init__()

/home/cwitty/pre-sage/real_mpfr.pyx in real_mpfr.RealNumber._integer_()

<type 'exceptions.ValueError'>: Attempt to coerce non-integral RealNumber to Integer
```


I'm pretty sure this is the underlying cause behind several 2.8.7-alpha0 doctest failures.

I have prepared a patch for this, which I will be testing shortly.

Issue created by migration from https://trac.sagemath.org/ticket/882





---

archive/issue_comments_005438.json:
```json
{
    "body": "Attachment [6928.patch](tarball://root/attachments/some-uuid/ticket882/6928.patch) by cwitty created at 2007-10-13 19:58:41\n\nI have attached a patch to change RR->ZZ coercion failure from ValueError to TypeError.  This fixes the doctest errors in sets/set.py and matrix/matrix_integer_dense.py.",
    "created_at": "2007-10-13T19:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/882#issuecomment-5438",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [6928.patch](tarball://root/attachments/some-uuid/ticket882/6928.patch) by cwitty created at 2007-10-13 19:58:41

I have attached a patch to change RR->ZZ coercion failure from ValueError to TypeError.  This fixes the doctest errors in sets/set.py and matrix/matrix_integer_dense.py.



---

archive/issue_events_000996.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-14T17:34:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/882",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/882#event-996"
}
```



---

archive/issue_comments_005439.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-14T17:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/882#issuecomment-5439",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
