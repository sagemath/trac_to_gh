# Issue 1947: Implement homomorphisms between vector spaces

archive/issues_001947.json:
```json
{
    "body": "Assignee: craigcitro\n\nCC:  mmezzarobba slelievre jipilab\n\nIt's surprising that this isn't already done -- it should be easy, since the morphisms don't have to do too much, and one already has the more complicated ring homomorphism code to use as a guide. I'll do this at SD7, if no one beats me to it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1947\n\n",
    "created_at": "2008-01-27T10:46:59Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.8",
    "title": "Implement homomorphisms between vector spaces",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1947",
    "user": "craigcitro"
}
```
Assignee: craigcitro

CC:  mmezzarobba slelievre jipilab

It's surprising that this isn't already done -- it should be easy, since the morphisms don't have to do too much, and one already has the more complicated ring homomorphism code to use as a guide. I'll do this at SD7, if no one beats me to it.

Issue created by migration from https://trac.sagemath.org/ticket/1947





---

archive/issue_comments_012371.json:
```json
{
    "body": "Craig, since homomorphisms between vector spaces *are* implemented (as I explained to you in irc last week), could you change the title of this trac ticket and explain what you are actually proposing be implemented?  Thanks.\n\n```\nsage: V = QQ^3; W = QQ^2\nsage: H = V.Hom(W)\nsage: H([1..6])\n\nFree module morphism defined by the matrix\n[1 2]\n[3 4]\n[5 6]\nDomain: Vector space of dimension 3 over Rational Field\nCodomain: Vector space of dimension 2 over Rational Field\n```\n",
    "created_at": "2008-01-27T13:11:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1947#issuecomment-12371",
    "user": "was"
}
```

Craig, since homomorphisms between vector spaces *are* implemented (as I explained to you in irc last week), could you change the title of this trac ticket and explain what you are actually proposing be implemented?  Thanks.

```
sage: V = QQ^3; W = QQ^2
sage: H = V.Hom(W)
sage: H([1..6])

Free module morphism defined by the matrix
[1 2]
[3 4]
[5 6]
Domain: Vector space of dimension 3 over Rational Field
Codomain: Vector space of dimension 2 over Rational Field
```




---

archive/issue_comments_012372.json:
```json
{
    "body": "Note that my first title for this ticket was ridiculous -- Sage has homomorphisms between vector spaces. The issue is to have homomorphisms over vector spaces V --> W when V and W are over different fields, but one has a map from the base field of V to the base field of W.",
    "created_at": "2008-01-27T17:59:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1947#issuecomment-12372",
    "user": "craigcitro"
}
```

Note that my first title for this ticket was ridiculous -- Sage has homomorphisms between vector spaces. The issue is to have homomorphisms over vector spaces V --> W when V and W are over different fields, but one has a map from the base field of V to the base field of W.



---

archive/issue_comments_012373.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1947#issuecomment-12373",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_012374.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2012-02-26T18:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1947#issuecomment-12374",
    "user": "was"
}
```

Changing priority from major to minor.



---

archive/issue_comments_012375.json:
```json
{
    "body": "Works now, but may be worth a few tests:\n\n```\nsage: Hom(QQ^3, RR^2)([[1,2],[3,4],[5,6]])\nVector space morphism represented by the matrix:\n[1 2]\n[3 4]\n[5 6]\nDomain: Vector space of dimension 3 over Rational Field\nCodomain: Vector space of dimension 2 over Real Field with 53 bits of precision\n```\n",
    "created_at": "2015-04-13T14:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1947#issuecomment-12375",
    "user": "mmezzarobba"
}
```

Works now, but may be worth a few tests:

```
sage: Hom(QQ^3, RR^2)([[1,2],[3,4],[5,6]])
Vector space morphism represented by the matrix:
[1 2]
[3 4]
[5 6]
Domain: Vector space of dimension 3 over Rational Field
Codomain: Vector space of dimension 2 over Real Field with 53 bits of precision
```




---

archive/issue_comments_012376.json:
```json
{
    "body": "Where should such documentation and tests go?",
    "created_at": "2018-05-11T20:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1947#issuecomment-12376",
    "user": "slelievre"
}
```

Where should such documentation and tests go?



---

archive/issue_comments_012377.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2019-05-11T16:51:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1947#issuecomment-12377",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_012378.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2019-05-11T16:56:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1947#issuecomment-12378",
    "user": "@black-stones"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_012379.json:
```json
{
    "body": "Replying to [comment:9 mmezzarobba]:\n> Works now, but may be worth a few tests:\n> {{{\n> sage: Hom(QQ^3, RR^2)([[1,2],[3,4],[5,6]])\n> Vector space morphism represented by the matrix:\n> [1 2]\n> [3 4]\n> [5 6]\n> Domain: Vector space of dimension 3 over Rational Field\n> Codomain: Vector space of dimension 2 over Real Field with 53 bits of precision\n> }}}\n\nI took this example and turned it into two doctests. Nothing new was added, just wanted to close this decade-old ticket.",
    "created_at": "2019-05-11T16:56:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1947#issuecomment-12379",
    "user": "@black-stones"
}
```

Replying to [comment:9 mmezzarobba]:
> Works now, but may be worth a few tests:
> {{{
> sage: Hom(QQ^3, RR^2)([[1,2],[3,4],[5,6]])
> Vector space morphism represented by the matrix:
> [1 2]
> [3 4]
> [5 6]
> Domain: Vector space of dimension 3 over Rational Field
> Codomain: Vector space of dimension 2 over Real Field with 53 bits of precision
> }}}

I took this example and turned it into two doctests. Nothing new was added, just wanted to close this decade-old ticket.



---

archive/issue_comments_012380.json:
```json
{
    "body": "It seems odd that the following also works. Is there a reason that this is not prevented?\n\n\n```\nsage: f = Hom(RR^2, QQ^2)([[1,2],[3,4]]); f\nVector space morphism represented by the matrix:\n[1 2]\n[3 4]\nDomain: Vector space of dimension 2 over Real Field with 53 bits of precision\nCodomain: Vector space of dimension 2 over Rational Field\nsage: f(vector(RR, [1,2]))\n(7, 10)\n```\n",
    "created_at": "2019-05-17T15:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1947#issuecomment-12380",
    "user": "@mwageringel"
}
```

It seems odd that the following also works. Is there a reason that this is not prevented?


```
sage: f = Hom(RR^2, QQ^2)([[1,2],[3,4]]); f
Vector space morphism represented by the matrix:
[1 2]
[3 4]
Domain: Vector space of dimension 2 over Real Field with 53 bits of precision
Codomain: Vector space of dimension 2 over Rational Field
sage: f(vector(RR, [1,2]))
(7, 10)
```




---

archive/issue_comments_012381.json:
```json
{
    "body": "Moving tickets from the Sage 8.8 milestone that have been actively worked on in the last six months to the next release milestone (optimistically).",
    "created_at": "2019-07-03T11:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1947#issuecomment-12381",
    "user": "embray"
}
```

Moving tickets from the Sage 8.8 milestone that have been actively worked on in the last six months to the next release milestone (optimistically).



---

archive/issue_comments_012382.json:
```json
{
    "body": "Ticket retargeted after milestone closed",
    "created_at": "2019-12-30T14:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1947#issuecomment-12382",
    "user": "embray"
}
```

Ticket retargeted after milestone closed



---

archive/issue_comments_012383.json:
```json
{
    "body": "Please:\n- update the ticket description to something meaningful.\n- break the lines in the documentation so that there are at most 72 characters wide.",
    "created_at": "2020-02-15T15:26:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1947#issuecomment-12383",
    "user": "vdelecroix"
}
```

Please:
- update the ticket description to something meaningful.
- break the lines in the documentation so that there are at most 72 characters wide.



---

archive/issue_comments_012384.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2020-02-15T15:26:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1947#issuecomment-12384",
    "user": "vdelecroix"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_012385.json:
```json
{
    "body": "Batch modifying tickets that will likely not be ready for 9.1, based on a review of the ticket title, branch/review status, and last modification date.",
    "created_at": "2020-04-14T19:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1947#issuecomment-12385",
    "user": "mkoeppe"
}
```

Batch modifying tickets that will likely not be ready for 9.1, based on a review of the ticket title, branch/review status, and last modification date.



---

archive/issue_comments_012386.json:
```json
{
    "body": "Setting new milestone based on a cursory review of ticket status, priority, and last modification date.",
    "created_at": "2021-02-13T20:51:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1947#issuecomment-12386",
    "user": "mkoeppe"
}
```

Setting new milestone based on a cursory review of ticket status, priority, and last modification date.



---

archive/issue_comments_012387.json:
```json
{
    "body": "Setting a new milestone for this ticket based on a cursory review.",
    "created_at": "2021-07-19T00:44:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1947#issuecomment-12387",
    "user": "mkoeppe"
}
```

Setting a new milestone for this ticket based on a cursory review.
