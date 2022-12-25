# Issue 6574: Type issue in is_quadratic_twist

archive/issues_006574.json:
```json
{
    "body": "Assignee: @loefflerd\n\nCC:  @JohnCremona\n\nKeywords: elliptic curve, quadratic twist\n\n\n```\nE = EllipticCurve('32a1')\nD = E.is_quadratic_twist(E)\nD, type(D)\n```\n\n\nyields\n\n\n```\n(1, <type 'sage.rings.rational.Rational'>)\n```\n\n\nbut\n\n\n```\nD = E.is_quadratic_twist(E.quadratic_twist(5))\nD, type(D)\n```\n\n\ngives back\n\n\n```\n(5, <type 'sage.rings.integer.Integer'>)\n```\n\n\nI think in the first case, we should also give back the integer 1. The cause of this is in ell_field.py. In the first case we exit is_quadratic_twist at line 353 with\n\n\n```\nreturn K.one_element()\n```\n\n\nIn the second case we exit at the end after\nline 394 has changed the type by \n\n\n```\nif K is rings.QQ:\n    D = D.squarefree_part()\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6574\n\n",
    "created_at": "2009-07-20T23:03:04Z",
    "labels": [
        "component: elliptic curves",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "Type issue in is_quadratic_twist",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6574",
    "user": "https://github.com/categorie"
}
```
Assignee: @loefflerd

CC:  @JohnCremona

Keywords: elliptic curve, quadratic twist


```
E = EllipticCurve('32a1')
D = E.is_quadratic_twist(E)
D, type(D)
```


yields


```
(1, <type 'sage.rings.rational.Rational'>)
```


but


```
D = E.is_quadratic_twist(E.quadratic_twist(5))
D, type(D)
```


gives back


```
(5, <type 'sage.rings.integer.Integer'>)
```


I think in the first case, we should also give back the integer 1. The cause of this is in ell_field.py. In the first case we exit is_quadratic_twist at line 353 with


```
return K.one_element()
```


In the second case we exit at the end after
line 394 has changed the type by 


```
if K is rings.QQ:
    D = D.squarefree_part()
```




Issue created by migration from https://trac.sagemath.org/ticket/6574





---

archive/issue_comments_053581.json:
```json
{
    "body": "Well spotted.  But note that this is in ell_field and general fields will not have integers, so the consistent return type should be that of the field.  So I would rather change the second behaviour, which will mean that when K is QQ we coerce back to ZZ after taking the square-free part.\n\nOn second thoughts we already have special code for QQ (calling squarefree_part()) so we could make a special case here and return a square-free integer (in ZZ) in all cases for K=QQ, and otherwise return a field element.  Is that acceptable?",
    "created_at": "2009-07-21T08:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6574#issuecomment-53581",
    "user": "https://github.com/JohnCremona"
}
```

Well spotted.  But note that this is in ell_field and general fields will not have integers, so the consistent return type should be that of the field.  So I would rather change the second behaviour, which will mean that when K is QQ we coerce back to ZZ after taking the square-free part.

On second thoughts we already have special code for QQ (calling squarefree_part()) so we could make a special case here and return a square-free integer (in ZZ) in all cases for K=QQ, and otherwise return a field element.  Is that acceptable?



---

archive/issue_comments_053582.json:
```json
{
    "body": "Attachment [trac_6574.patch](tarball://root/attachments/some-uuid/ticket6574/trac_6574.patch) by @categorie created at 2009-07-21 18:31:38\n\nI opted for your second suggestion. In case K is QQ it is ZZ(1) that is returned.",
    "created_at": "2009-07-21T18:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6574#issuecomment-53582",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_6574.patch](tarball://root/attachments/some-uuid/ticket6574/trac_6574.patch) by @categorie created at 2009-07-21 18:31:38

I opted for your second suggestion. In case K is QQ it is ZZ(1) that is returned.



---

archive/issue_comments_053583.json:
```json
{
    "body": "Positive review.  The patch fixes the problem (according to the above discussion) with a doctest + documentation to explain this special case.",
    "created_at": "2009-07-21T21:45:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6574#issuecomment-53583",
    "user": "https://github.com/JohnCremona"
}
```

Positive review.  The patch fixes the problem (according to the above discussion) with a doctest + documentation to explain this special case.



---

archive/issue_comments_053584.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-23T08:40:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6574#issuecomment-53584",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_006811.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-07-23T08:40:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6574",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6574#event-6811"
}
```
