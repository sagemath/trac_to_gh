# Issue 6923: Matrix numerical approximation converts complex to real

archive/issues_006923.json:
```json
{
    "body": "Assignee: tbd\n\nsage: A = Matrix(CC,3); A.parent()\nFull MatrixSpace of 3 by 3 dense matrices over Complex Field with 53 bits of precision\nsage: B = A.n(20); B.parent()\nFull MatrixSpace of 3 by 3 dense matrices over Real Field with 20 bits of precision\n\nIMHO .n() only should change the precision, no other conversion.\nThis is also the behaviour of .n() on ComplexField.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6923\n\n",
    "created_at": "2009-09-11T06:40:08Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.3",
    "title": "Matrix numerical approximation converts complex to real",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6923",
    "user": "https://trac.sagemath.org/admin/accounts/users/Henryk.Trappmann"
}
```
Assignee: tbd

sage: A = Matrix(CC,3); A.parent()
Full MatrixSpace of 3 by 3 dense matrices over Complex Field with 53 bits of precision
sage: B = A.n(20); B.parent()
Full MatrixSpace of 3 by 3 dense matrices over Real Field with 20 bits of precision

IMHO .n() only should change the precision, no other conversion.
This is also the behaviour of .n() on ComplexField.

Issue created by migration from https://trac.sagemath.org/ticket/6923





---

archive/issue_comments_057062.json:
```json
{
    "body": "Changing component from algebra to linear algebra.",
    "created_at": "2009-11-15T13:09:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6923#issuecomment-57062",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebra to linear algebra.



---

archive/issue_comments_057063.json:
```json
{
    "body": "The problem being that\n\n```\nreturn self.change_ring(sage.rings.real_mpfr.RealField(prec))\n```\n\ndoesn't raise an error since it can coerce the motivating matrix to Real. should we avoid coercion, maybe using type checking ?",
    "created_at": "2016-05-30T10:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6923#issuecomment-57063",
    "user": "https://trac.sagemath.org/admin/accounts/users/jhonrubia6"
}
```

The problem being that

```
return self.change_ring(sage.rings.real_mpfr.RealField(prec))
```

doesn't raise an error since it can coerce the motivating matrix to Real. should we avoid coercion, maybe using type checking ?
