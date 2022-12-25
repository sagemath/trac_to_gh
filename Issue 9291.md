# Issue 9291: Constructing a root system / coxeter group from a pair of matrices

archive/issues_009291.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat\n\nConstructing root systems / coxeter groups / ... from a pair of\nmatrices describing the coordinates of the roots and coroots in\ntheir respective basis. Interface:\n\n```\n    sage: T = CartanType(roots_as_matrix, coroots_as_matrix)\n    sage: T.root_space()\n    sage: T.root_space().simple_roots()\n    sage: T.coroot_space()\n    sage: WeylGroup(T.root_space())\n    sage: WeylGroup(T)\n    sage: ReflectionGroup(T)\n```\n\nThe root system code is designed to support such features. Attached: a\none page proof of feasibility (not following the above interface).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9291\n\n",
    "created_at": "2010-06-21T08:22:28Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "Constructing a root system / coxeter group from a pair of matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9291",
    "user": "https://github.com/nthiery"
}
```
Assignee: sage-combinat

CC:  sage-combinat

Constructing root systems / coxeter groups / ... from a pair of
matrices describing the coordinates of the roots and coroots in
their respective basis. Interface:

```
    sage: T = CartanType(roots_as_matrix, coroots_as_matrix)
    sage: T.root_space()
    sage: T.root_space().simple_roots()
    sage: T.coroot_space()
    sage: WeylGroup(T.root_space())
    sage: WeylGroup(T)
    sage: ReflectionGroup(T)
```

The root system code is designed to support such features. Attached: a
one page proof of feasibility (not following the above interface).


Issue created by migration from https://trac.sagemath.org/ticket/9291





---

archive/issue_comments_087375.json:
```json
{
    "body": "Attachment [cartan_type_from_matrices.py](tarball://root/attachments/some-uuid/ticket9291/cartan_type_from_matrices.py) by @fchapoton created at 2012-12-17 17:07:50",
    "created_at": "2012-12-17T17:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9291#issuecomment-87375",
    "user": "https://github.com/fchapoton"
}
```

Attachment [cartan_type_from_matrices.py](tarball://root/attachments/some-uuid/ticket9291/cartan_type_from_matrices.py) by @fchapoton created at 2012-12-17 17:07:50



---

archive/issue_comments_087376.json:
```json
{
    "body": "Changing keywords from \"\" to \"coxeter\".",
    "created_at": "2012-12-17T17:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9291#issuecomment-87376",
    "user": "https://github.com/fchapoton"
}
```

Changing keywords from "" to "coxeter".
