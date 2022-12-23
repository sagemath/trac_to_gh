# Issue 247: bug in __contains__ for polynomial rings over ZZ

archive/issues_000247.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nage: R.<x,y,z,w> = ZZ['x,y,z,w']\nsage: i = ideal(x^2 + y^2 - z^2 - w^2, x-y)\nsage: j = i^2\nsage: j.groebner_basis()\n[y^2 - 2*x*y + x^2, y*w^2 + y*z^2 - 2*y^3 - x*w^2 - x*z^2 + 2*x*y^2, w^4 + 2*z^2*w^2 + z^4 - 4*y^2*w^2 - 4*y^2*z^2 + 4*y^4]\nsage: y^2 - 2*x*y + x^2 in j\nFalse\nsage: 0 in j\nFalse\n```\n\n\nThe last two lines are WRONG!!\n\nIssue created by migration from https://trac.sagemath.org/ticket/247\n\n",
    "created_at": "2007-02-07T04:22:07Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "bug in __contains__ for polynomial rings over ZZ",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/247",
    "user": "William Stein"
}
```
Assignee: somebody


```
age: R.<x,y,z,w> = ZZ['x,y,z,w']
sage: i = ideal(x^2 + y^2 - z^2 - w^2, x-y)
sage: j = i^2
sage: j.groebner_basis()
[y^2 - 2*x*y + x^2, y*w^2 + y*z^2 - 2*y^3 - x*w^2 - x*z^2 + 2*x*y^2, w^4 + 2*z^2*w^2 + z^4 - 4*y^2*w^2 - 4*y^2*z^2 + 4*y^4]
sage: y^2 - 2*x*y + x^2 in j
False
sage: 0 in j
False
```


The last two lines are WRONG!!

Issue created by migration from https://trac.sagemath.org/ticket/247





---

archive/issue_comments_001089.json:
```json
{
    "body": "Changing assignee from somebody to malb.",
    "created_at": "2007-02-07T04:32:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/247#issuecomment-1089",
    "user": "malb"
}
```

Changing assignee from somebody to malb.



---

archive/issue_comments_001090.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-02-07T05:02:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/247#issuecomment-1090",
    "user": "malb"
}
```

Resolution: fixed



---

archive/issue_comments_001091.json:
```json
{
    "body": "fixed in r2808",
    "created_at": "2007-02-07T05:02:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/247#issuecomment-1091",
    "user": "malb"
}
```

fixed in r2808
