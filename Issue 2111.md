# Issue 2111: [with patch, needs review] Gröbner bases over any field

archive/issues_002111.json:
```json
{
    "body": "Assignee: malb\n\nCC:  zimmerma\n\nThis now works (but is very very slow):\n\n\n```\nsage: R.<x,y> = PolynomialRing(GF(2147483659),order='lex')\nsage: ideal([x^3-2*y^2,3*x+y^4]).groebner_basis()\n[x + 1431655773*y^4, y^12 + 54*y^2]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2111\n\n",
    "created_at": "2008-02-08T12:17:23Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] Gr\u00f6bner bases over any field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2111",
    "user": "malb"
}
```
Assignee: malb

CC:  zimmerma

This now works (but is very very slow):


```
sage: R.<x,y> = PolynomialRing(GF(2147483659),order='lex')
sage: ideal([x^3-2*y^2,3*x+y^4]).groebner_basis()
[x + 1431655773*y^4, y^12 + 54*y^2]
```


Issue created by migration from https://trac.sagemath.org/ticket/2111





---

archive/issue_comments_013763.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-08T12:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2111#issuecomment-13763",
    "user": "malb"
}
```

Attachment



---

archive/issue_comments_013764.json:
```json
{
    "body": "Attachment\n\nmisc additional improvements, apply after first patch",
    "created_at": "2008-02-13T13:26:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2111#issuecomment-13764",
    "user": "malb"
}
```

Attachment

misc additional improvements, apply after first patch



---

archive/issue_comments_013765.json:
```json
{
    "body": "Both patches look good, there's a lot to like in the first patch.  Apply!\n\nI personally prefer long outputs of doctests to be all one line -- I find it makes it easier to find errors -- but that's no reason to reject a good patch :)",
    "created_at": "2008-02-15T03:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2111#issuecomment-13765",
    "user": "ncalexan"
}
```

Both patches look good, there's a lot to like in the first patch.  Apply!

I personally prefer long outputs of doctests to be all one line -- I find it makes it easier to find errors -- but that's no reason to reject a good patch :)



---

archive/issue_comments_013766.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-15T04:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2111#issuecomment-13766",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha0



---

archive/issue_comments_013767.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-15T04:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2111#issuecomment-13767",
    "user": "mabshoff"
}
```

Resolution: fixed
