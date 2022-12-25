# Issue 8502: evaluating multivariate polynomials yields non-constant

archive/issues_008502.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @categorie @malb\n\nKeywords: polynomial evaluation\n\nThe following behaviour does not agree with the documentation for the {{{__call__}} function on multivariable polynomials, which states that (as one would expect and hope) the result should lie in the constant field:\n\n```\nsage: K.<t> = NumberField(x^2+47)\nsage: R.<X,Y,Z> = K[]\nsage: f = X+Y+Z\nsage: a = f(t,t,t)\nsage: a.parent()\nMultivariate Polynomial Ring in X, Y, Z over Number Field in t with defining polynomial x^2 + 47\n```\n\nIt is also inconsistent:\n\n```\nsage: R.<X,Y,Z> = QQ[]\nsage: f = X+Y+Z\nsage: a = f(2,3,4)\nsage: a.parent()\nRational Field\n```\n\nThis causes strange bugs -- see #8498 for an example.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8502\n\n",
    "created_at": "2010-03-11T22:08:11Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "evaluating multivariate polynomials yields non-constant",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8502",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @aghitza

CC:  @categorie @malb

Keywords: polynomial evaluation

The following behaviour does not agree with the documentation for the {{{__call__}} function on multivariable polynomials, which states that (as one would expect and hope) the result should lie in the constant field:

```
sage: K.<t> = NumberField(x^2+47)
sage: R.<X,Y,Z> = K[]
sage: f = X+Y+Z
sage: a = f(t,t,t)
sage: a.parent()
Multivariate Polynomial Ring in X, Y, Z over Number Field in t with defining polynomial x^2 + 47
```

It is also inconsistent:

```
sage: R.<X,Y,Z> = QQ[]
sage: f = X+Y+Z
sage: a = f(2,3,4)
sage: a.parent()
Rational Field
```

This causes strange bugs -- see #8498 for an example.

Issue created by migration from https://trac.sagemath.org/ticket/8502





---

archive/issue_comments_076641.json:
```json
{
    "body": "Bug fixed:  I added tests for when the resulting value is either 0, or a nonzero constant, in which case an element of the base ring is returned.  Otherwise an element of the parent is returned (so you can still evaluate f(x+y,y) and similar.)\n\nPatch up as soon as testing is finished.\n\nmalb: I'm CC-ing you as the past person to work on this file.",
    "created_at": "2010-04-02T11:22:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8502#issuecomment-76641",
    "user": "https://github.com/JohnCremona"
}
```

Bug fixed:  I added tests for when the resulting value is either 0, or a nonzero constant, in which case an element of the base ring is returned.  Otherwise an element of the parent is returned (so you can still evaluate f(x+y,y) and similar.)

Patch up as soon as testing is finished.

malb: I'm CC-ing you as the past person to work on this file.



---

archive/issue_comments_076642.json:
```json
{
    "body": "Applies to 4.3.5",
    "created_at": "2010-04-02T11:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8502#issuecomment-76642",
    "user": "https://github.com/JohnCremona"
}
```

Applies to 4.3.5



---

archive/issue_comments_076643.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-02T11:44:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8502#issuecomment-76643",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076644.json:
```json
{
    "body": "Attachment [trac_8502-mpoly.patch](tarball://root/attachments/some-uuid/ticket8502/trac_8502-mpoly.patch) by @JohnCremona created at 2010-04-02 11:44:20",
    "created_at": "2010-04-02T11:44:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8502#issuecomment-76644",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_8502-mpoly.patch](tarball://root/attachments/some-uuid/ticket8502/trac_8502-mpoly.patch) by @JohnCremona created at 2010-04-02 11:44:20



---

archive/issue_comments_076645.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-03T08:12:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8502#issuecomment-76645",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076646.json:
```json
{
    "body": "Looks good.",
    "created_at": "2010-04-03T08:12:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8502#issuecomment-76646",
    "user": "https://github.com/aghitza"
}
```

Looks good.



---

archive/issue_comments_076647.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:44:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8502#issuecomment-76647",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_076648.json:
```json
{
    "body": "Merged \"trac_8502-mpoly.patch\" in 4.4.alpha0.",
    "created_at": "2010-04-16T18:44:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8502#issuecomment-76648",
    "user": "https://github.com/jhpalmieri"
}
```

Merged "trac_8502-mpoly.patch" in 4.4.alpha0.



---

archive/issue_events_008682.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-16T18:44:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8502",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8502#event-8682"
}
```
