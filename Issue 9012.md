# Issue 9012: singular_decomposition fails on non-interreduced Gröbner basis

archive/issues_009012.json:
```json
{
    "body": "Assignee: @malb\n\nThe docstring of ``sage.ring.polynomial.multi_polynomial_ideal.triangular_decomposition`` says:\n\n```\n        This requires that the given basis is reduced w.r.t. to the\n        lexicographical monomial ordering. If the basis of self does\n        not have this property, the required Groebner basis is\n        computed implicitly.\n```\n\nhowever (Sage 4.4.1):\n\n```\nsage: R.<x,y> = QQ[]\nsage: J = Ideal(x^2+y^2-2, y^2-1)\nsage: J.triangular_decomposition()\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n[...]\nTypeError: Singular error:\n// ** _ is no standard basis\n   ? The ideal sage22 has to be given by a reduced SB\n   ? error occurred in STDIN line 101: `def sage24=fglm(sage19,sage22);\n\nIssue created by migration from https://trac.sagemath.org/ticket/9012\n\n",
    "created_at": "2010-05-21T20:14:24Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "singular_decomposition fails on non-interreduced Gr\u00f6bner basis",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9012",
    "user": "https://github.com/mezzarobba"
}
```
Assignee: @malb

The docstring of ``sage.ring.polynomial.multi_polynomial_ideal.triangular_decomposition`` says:

```
        This requires that the given basis is reduced w.r.t. to the
        lexicographical monomial ordering. If the basis of self does
        not have this property, the required Groebner basis is
        computed implicitly.
```

however (Sage 4.4.1):

```
sage: R.<x,y> = QQ[]
sage: J = Ideal(x^2+y^2-2, y^2-1)
sage: J.triangular_decomposition()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

[...]
TypeError: Singular error:
// ** _ is no standard basis
   ? The ideal sage22 has to be given by a reduced SB
   ? error occurred in STDIN line 101: `def sage24=fglm(sage19,sage22);

Issue created by migration from https://trac.sagemath.org/ticket/9012





---

archive/issue_comments_083228.json:
```json
{
    "body": "Attachment [trac_9012.patch](tarball://root/attachments/some-uuid/ticket9012/trac_9012.patch) by @malb created at 2010-07-12 15:39:07",
    "created_at": "2010-07-12T15:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9012",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9012#issuecomment-83228",
    "user": "https://github.com/malb"
}
```

Attachment [trac_9012.patch](tarball://root/attachments/some-uuid/ticket9012/trac_9012.patch) by @malb created at 2010-07-12 15:39:07



---

archive/issue_comments_083229.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-12T15:39:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9012",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9012#issuecomment-83229",
    "user": "https://github.com/malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083230.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-14T15:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9012",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9012#issuecomment-83230",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083231.json:
```json
{
    "body": "The changes in the code are reasonable, it is doctested, and `sage -testall` passes.\n\nSo: Positive review!\n\nMartin and I discussed one potential issue, namely that the method does not set `degBound=0` in Singular. But this should be on a different ticket and will involve decorators.",
    "created_at": "2010-07-14T15:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9012",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9012#issuecomment-83231",
    "user": "https://github.com/simon-king-jena"
}
```

The changes in the code are reasonable, it is doctested, and `sage -testall` passes.

So: Positive review!

Martin and I discussed one potential issue, namely that the method does not set `degBound=0` in Singular. But this should be on a different ticket and will involve decorators.



---

archive/issue_comments_083232.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T01:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9012",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9012#issuecomment-83232",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_022051.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-21T01:45:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9012",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9012#event-22051"
}
```
