# Issue 46: modular symbols -- crash when computing an eigenform

archive/issues_000046.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: M = ModularSymbols(12,4,sign=1).cuspidal_submodule()\n\nsage: M.decomposition()[1].q_eigenform(10)\nTraceback (most recent call last):\n...\nTypeError: Unable to coerce x (=[   0    1   -1    0 -7/2  7/2  3/2 -3/2    0]) to a morphism in Set of Morphisms from Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 9 for Gamma_0(12) of weight 4 with sign 1 over Rational Field to Modular Symbols space of dimension 9 for Gamma_0(12) of weight 4 with sign 1 over Rational Field in Category of sets\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/46\n\n",
    "created_at": "2006-09-13T03:40:57Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "modular symbols -- crash when computing an eigenform",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/46",
    "user": "was"
}
```
Assignee: was


```
sage: M = ModularSymbols(12,4,sign=1).cuspidal_submodule()

sage: M.decomposition()[1].q_eigenform(10)
Traceback (most recent call last):
...
TypeError: Unable to coerce x (=[   0    1   -1    0 -7/2  7/2  3/2 -3/2    0]) to a morphism in Set of Morphisms from Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 9 for Gamma_0(12) of weight 4 with sign 1 over Rational Field to Modular Symbols space of dimension 9 for Gamma_0(12) of weight 4 with sign 1 over Rational Field in Category of sets
```



Issue created by migration from https://trac.sagemath.org/ticket/46





---

archive/issue_comments_000272.json:
```json
{
    "body": "It's really A.factorization() that's not implemented yet when A involves old forms.",
    "created_at": "2006-09-13T03:52:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/46",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/46#issuecomment-272",
    "user": "was"
}
```

It's really A.factorization() that's not implemented yet when A involves old forms.



---

archive/issue_comments_000273.json:
```json
{
    "body": "The factorization fails because A.degeneracy_map(1)  fails.",
    "created_at": "2006-09-13T03:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/46",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/46#issuecomment-273",
    "user": "was"
}
```

The factorization fails because A.degeneracy_map(1)  fails.



---

archive/issue_comments_000274.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-09-13T04:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/46",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/46#issuecomment-274",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_000275.json:
```json
{
    "body": "OK, fixed.  The problem was that a self.category() instead of sub.category() in modules/matrix_morphism.py",
    "created_at": "2006-09-13T04:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/46",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/46#issuecomment-275",
    "user": "was"
}
```

OK, fixed.  The problem was that a self.category() instead of sub.category() in modules/matrix_morphism.py
