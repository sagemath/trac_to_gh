# Issue 3465: Number Field base rings for NumberFieldTower

archive/issues_003465.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @craigcitro\n\nKeywords: relative number fields\n\nWhen creating towers of number fields, the base rings don't behave as I think they should.  The following is from the coercion branch (the opposite problem exists in the normal branch).\n\nsage: sage: L.<cuberoot2, zeta3> = CyclotomicField(3).extension(x^3 - 2)\nsage: type(L)\n<class 'sage.rings.number_field.number_field.NumberField_relative'>\nsage: L.ngens()\n1 (2 in current Sage, I think it should be 1)\nsage: L.base_ring()\nCyclotomic Field of order 3 and degree 2 (I agree)\nsage: L.base_field()\nCyclotomic Field of order 3 and degree 2 (I agree)\nsage: L.base()\nRational Field (I think it should be Cyclotomic Field of order 3 and degree 2)\nsage: K.<a, b> = NumberField( [x^2 + x + 1, x^3 + 2] )\nsage: K.ngens()\n1 (2 in current Sage, I think it should be 2)sage: type(K)\n<class 'sage.rings.number_field.number_field.NumberField_relative'>  \nsage: K.base_ring()\nNumber Field in b with defining polynomial x^3 + 2 (I think it should be Rational Field)\nsage: K.base_field()\nNumber Field in b with defining polynomial x^3 + 2 (I think it should be Rational Field)\nsage: K.base()\nRational Field (um... ok, I agree)\n\nIssue created by migration from https://trac.sagemath.org/ticket/3465\n\n",
    "created_at": "2008-06-18T22:29:07Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Number Field base rings for NumberFieldTower",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3465",
    "user": "@roed314"
}
```
Assignee: @williamstein

CC:  @craigcitro

Keywords: relative number fields

When creating towers of number fields, the base rings don't behave as I think they should.  The following is from the coercion branch (the opposite problem exists in the normal branch).

sage: sage: L.<cuberoot2, zeta3> = CyclotomicField(3).extension(x^3 - 2)
sage: type(L)
<class 'sage.rings.number_field.number_field.NumberField_relative'>
sage: L.ngens()
1 (2 in current Sage, I think it should be 1)
sage: L.base_ring()
Cyclotomic Field of order 3 and degree 2 (I agree)
sage: L.base_field()
Cyclotomic Field of order 3 and degree 2 (I agree)
sage: L.base()
Rational Field (I think it should be Cyclotomic Field of order 3 and degree 2)
sage: K.<a, b> = NumberField( [x^2 + x + 1, x^3 + 2] )
sage: K.ngens()
1 (2 in current Sage, I think it should be 2)sage: type(K)
<class 'sage.rings.number_field.number_field.NumberField_relative'>  
sage: K.base_ring()
Number Field in b with defining polynomial x^3 + 2 (I think it should be Rational Field)
sage: K.base_field()
Number Field in b with defining polynomial x^3 + 2 (I think it should be Rational Field)
sage: K.base()
Rational Field (um... ok, I agree)

Issue created by migration from https://trac.sagemath.org/ticket/3465





---

archive/issue_comments_024432.json:
```json
{
    "body": "Note that this affects the doctests for sage.rings.number_field.RelativeNumberFieldHomset.list",
    "created_at": "2008-06-18T22:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3465#issuecomment-24432",
    "user": "@roed314"
}
```

Note that this affects the doctests for sage.rings.number_field.RelativeNumberFieldHomset.list



---

archive/issue_comments_024433.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-20T20:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3465#issuecomment-24433",
    "user": "@loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_024434.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-20T20:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3465#issuecomment-24434",
    "user": "@loefflerd"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_024435.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-02T23:39:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3465#issuecomment-24435",
    "user": "@loefflerd"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_024436.json:
```json
{
    "body": "This ticket has been idle for nearly two years, and moreover it's not really clear to me exactly what the reporter considers to be a bug. Is the suggestion that the objects created via the NumberFieldTower constructor should somehow behave differently from ones created via the extension() method? That sounds like a bad idea to me.\n\nI suggest closing this as wontfix. I'm setting this to \"needs review\" in order to request a second opinion on my proposal not to fix this.",
    "created_at": "2010-07-02T23:39:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3465#issuecomment-24436",
    "user": "@loefflerd"
}
```

This ticket has been idle for nearly two years, and moreover it's not really clear to me exactly what the reporter considers to be a bug. Is the suggestion that the objects created via the NumberFieldTower constructor should somehow behave differently from ones created via the extension() method? That sounds like a bad idea to me.

I suggest closing this as wontfix. I'm setting this to "needs review" in order to request a second opinion on my proposal not to fix this.



---

archive/issue_comments_024437.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-03T10:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3465#issuecomment-24437",
    "user": "@lftabera"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_024438.json:
```json
{
    "body": "I agree, the result should be homogenenous no matter how you have constructed the field.\n\nI think that the problem is that base had no documentation.",
    "created_at": "2010-07-03T10:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3465#issuecomment-24438",
    "user": "@lftabera"
}
```

I agree, the result should be homogenenous no matter how you have constructed the field.

I think that the problem is that base had no documentation.



---

archive/issue_comments_024439.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-07-20T07:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3465#issuecomment-24439",
    "user": "@qed777"
}
```

Resolution: wontfix
