# Issue 1667: [with patch, needs review] coercion fixes for PolyBoRi

archive/issues_001667.json:
```json
{
    "body": "Assignee: was\n\nKeywords: polybori\n\n`BooleanPolynomialRing` supports coercion from rings where the number of variables is greater than self. This code should be in `__call__` and coercion should first check for the number of variables of the parent ring.\n\nAttached patch fixes this problem, and adds similar coercion and `__call__` semantics to `BooleanMonomialMonoid`. It also fixes minor problems where using iterators of polynomials over a ring other than the current one messes `PolyBoRi` up.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1667\n\n",
    "created_at": "2008-01-03T14:54:15Z",
    "labels": [
        "interfaces",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] coercion fixes for PolyBoRi",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1667",
    "user": "burcin"
}
```
Assignee: was

Keywords: polybori

`BooleanPolynomialRing` supports coercion from rings where the number of variables is greater than self. This code should be in `__call__` and coercion should first check for the number of variables of the parent ring.

Attached patch fixes this problem, and adds similar coercion and `__call__` semantics to `BooleanMonomialMonoid`. It also fixes minor problems where using iterators of polynomials over a ring other than the current one messes `PolyBoRi` up.

Issue created by migration from https://trac.sagemath.org/ticket/1667





---

archive/issue_comments_010591.json:
```json
{
    "body": "coercion & minor fixes to polybori",
    "created_at": "2008-01-03T14:54:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1667#issuecomment-10591",
    "user": "burcin"
}
```

coercion & minor fixes to polybori



---

archive/issue_comments_010592.json:
```json
{
    "body": "Attachment\n\nLooks good to me. This is isolated to polybori, so I merged it.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-03T16:00:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1667#issuecomment-10592",
    "user": "mabshoff"
}
```

Attachment

Looks good to me. This is isolated to polybori, so I merged it.

Cheers,

Michael



---

archive/issue_comments_010593.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-03T16:01:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1667#issuecomment-10593",
    "user": "mabshoff"
}
```

Resolution: fixed
