# Issue 5928: multiplication of factorisations should coerce factors into a common universe

archive/issues_005928.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  cremona\n\nKeywords: multiplication factorization coercion\n\nThis was uncovered at #5921.  Observe:\n\n\n```\nsage: P.<x> = ZZ\nsage: f = 2*x + 2\nsage: c = f.content()\nsage: g = f//c\nsage: F1 = c.factor(); [type(a[0]) for a in F1]\n[<type 'sage.rings.integer.Integer'>]\nsage: F2 = g.factor(); [type(a[0]) for a in F2]\n[<type 'sage.rings.polynomial.polynomial_integer_dense_flint.Polynomial_integer_dense_flint'>]\nsage: F1*F2\n2 * (x + 1)\nsage: [type(a[0]) for a in F1*F2]\n[<type 'sage.rings.integer.Integer'>,\n <type 'sage.rings.polynomial.polynomial_integer_dense_flint.Polynomial_integer_dense_flint'>]\n```\n\n\nI think that multiplying two factorisations should make sure that the factors can be coerced into a common universe, so that all factors have the same parent.  If that's impossible, then an error should be thrown.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5928\n\n",
    "created_at": "2009-04-29T01:43:08Z",
    "labels": [
        "factorization",
        "major",
        "bug"
    ],
    "title": "multiplication of factorisations should coerce factors into a common universe",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5928",
    "user": "AlexGhitza"
}
```
Assignee: AlexGhitza

CC:  cremona

Keywords: multiplication factorization coercion

This was uncovered at #5921.  Observe:


```
sage: P.<x> = ZZ
sage: f = 2*x + 2
sage: c = f.content()
sage: g = f//c
sage: F1 = c.factor(); [type(a[0]) for a in F1]
[<type 'sage.rings.integer.Integer'>]
sage: F2 = g.factor(); [type(a[0]) for a in F2]
[<type 'sage.rings.polynomial.polynomial_integer_dense_flint.Polynomial_integer_dense_flint'>]
sage: F1*F2
2 * (x + 1)
sage: [type(a[0]) for a in F1*F2]
[<type 'sage.rings.integer.Integer'>,
 <type 'sage.rings.polynomial.polynomial_integer_dense_flint.Polynomial_integer_dense_flint'>]
```


I think that multiplying two factorisations should make sure that the factors can be coerced into a common universe, so that all factors have the same parent.  If that's impossible, then an error should be thrown.


Issue created by migration from https://trac.sagemath.org/ticket/5928





---

archive/issue_comments_046867.json:
```json
{
    "body": "The attached patch does this for multiplication, gcd, and lcm.  The other operations either inherit it or were dealing with this already.",
    "created_at": "2009-04-29T05:50:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5928#issuecomment-46867",
    "user": "AlexGhitza"
}
```

The attached patch does this for multiplication, gcd, and lcm.  The other operations either inherit it or were dealing with this already.



---

archive/issue_comments_046868.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-29T05:50:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5928#issuecomment-46868",
    "user": "AlexGhitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046869.json:
```json
{
    "body": "Attachment [trac_5928.patch](tarball://root/attachments/some-uuid/ticket5928/trac_5928.patch) by cremona created at 2009-04-29 08:58:29\n\nThis patch looks good, applies to 3.4.2.alpha0 and tests in sage/structure pass as well as those in sage/rings/*.py (I did not go into subdirectories).\n\nI was a little disappointed by this:\n\n```\nsage: R.<x> = ZZ[]\nsage: S.<y> = QQ[]\nsage: f = x^2-1\nsage: g = y^3-1\nsage: f.factor()\n(x - 1) * (x + 1)\nsage: g.factor()\n(y - 1) * (y^2 + y + 1)\nsage: f.factor() * g.factor()\n(1) * (y - 1) * (x - 1) * (x + 1) * (y^2 + y + 1)\nsage: (f.factor() * g.factor()).universe()\nCategory of objects\n```\n\nand in fact coercion is not clever enough to allow x*y here.  but it does work if you do \n\n```\nsage: S.<x> = QQ[]\nsage: y=S.gen(0)\nsage: g = y^3-1\nsage: f.factor() * g.factor()\n(x + 1) * (x - 1)^2 * (x^2 + x + 1)\n```\n\n-- i.e. you have to define the two rings with the same name of the variable even if you use a different name for input.  Weird, but it is not going to stop this patch!",
    "created_at": "2009-04-29T08:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5928#issuecomment-46869",
    "user": "cremona"
}
```

Attachment [trac_5928.patch](tarball://root/attachments/some-uuid/ticket5928/trac_5928.patch) by cremona created at 2009-04-29 08:58:29

This patch looks good, applies to 3.4.2.alpha0 and tests in sage/structure pass as well as those in sage/rings/*.py (I did not go into subdirectories).

I was a little disappointed by this:

```
sage: R.<x> = ZZ[]
sage: S.<y> = QQ[]
sage: f = x^2-1
sage: g = y^3-1
sage: f.factor()
(x - 1) * (x + 1)
sage: g.factor()
(y - 1) * (y^2 + y + 1)
sage: f.factor() * g.factor()
(1) * (y - 1) * (x - 1) * (x + 1) * (y^2 + y + 1)
sage: (f.factor() * g.factor()).universe()
Category of objects
```

and in fact coercion is not clever enough to allow x*y here.  but it does work if you do 

```
sage: S.<x> = QQ[]
sage: y=S.gen(0)
sage: g = y^3-1
sage: f.factor() * g.factor()
(x + 1) * (x - 1)^2 * (x^2 + x + 1)
```

-- i.e. you have to define the two rings with the same name of the variable even if you use a different name for input.  Weird, but it is not going to stop this patch!



---

archive/issue_comments_046870.json:
```json
{
    "body": "Merged in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T06:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5928#issuecomment-46870",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.rc0.

Cheers,

Michael



---

archive/issue_comments_046871.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-30T06:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5928#issuecomment-46871",
    "user": "mabshoff"
}
```

Resolution: fixed
