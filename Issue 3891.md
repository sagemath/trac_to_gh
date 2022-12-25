# Issue 3891: polynomial sqrt method

archive/issues_003891.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @JohnCremona\n\nJohn Cremona requests a sqrt for polynomial rings:\n\n```\nI have needed the following.  g(x) is a univariate polynomial which I\nknow to be a square, and i want its square root.  g.factor() does too\nmuch, as does g.squarefree_decomposition().  I can get the sqrt via\ng.gcd(g.derivative()), which works in my case since I know that the\nsqrt is itself square-free.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3891\n\n",
    "created_at": "2008-08-18T14:00:37Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "polynomial sqrt method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3891",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```
Assignee: somebody

CC:  @JohnCremona

John Cremona requests a sqrt for polynomial rings:

```
I have needed the following.  g(x) is a univariate polynomial which I
know to be a square, and i want its square root.  g.factor() does too
much, as does g.squarefree_decomposition().  I can get the sqrt via
g.gcd(g.derivative()), which works in my case since I know that the
sqrt is itself square-free.
```


Issue created by migration from https://trac.sagemath.org/ticket/3891





---

archive/issue_comments_027747.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2008-11-19T21:56:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3891#issuecomment-27747",
    "user": "https://github.com/jhpalmieri"
}
```

Changing priority from major to minor.



---

archive/issue_comments_027748.json:
```json
{
    "body": "For an integer n, there are two options: n.sqrt() or n.is_square().  n.sqrt() returns a square root by passing to a larger ring (like CC) if it needs to, while n.is_square() returns True (and optionally returns a square root) if n is the square of an integer, false otherwise.  I think that we need an is_square method for polynomials, not a sqrt method.\n\nThe attached patch provides an is_square method.  It also fixes a bug in squarefree_decomposition: that method would barf for the wrong reason if you gave it a polynomial over a finite field.  Now it barfs for the right reason.",
    "created_at": "2008-11-19T21:56:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3891#issuecomment-27748",
    "user": "https://github.com/jhpalmieri"
}
```

For an integer n, there are two options: n.sqrt() or n.is_square().  n.sqrt() returns a square root by passing to a larger ring (like CC) if it needs to, while n.is_square() returns True (and optionally returns a square root) if n is the square of an integer, false otherwise.  I think that we need an is_square method for polynomials, not a sqrt method.

The attached patch provides an is_square method.  It also fixes a bug in squarefree_decomposition: that method would barf for the wrong reason if you gave it a polynomial over a finite field.  Now it barfs for the right reason.



---

archive/issue_comments_027749.json:
```json
{
    "body": "Changing keywords from \"\" to \"polynomial, square root\".",
    "created_at": "2008-11-19T21:56:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3891#issuecomment-27749",
    "user": "https://github.com/jhpalmieri"
}
```

Changing keywords from "" to "polynomial, square root".



---

archive/issue_comments_027750.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-11-19T21:56:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3891#issuecomment-27750",
    "user": "https://github.com/jhpalmieri"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_027751.json:
```json
{
    "body": "Attachment [polynomial_is_square.patch](tarball://root/attachments/some-uuid/ticket3891/polynomial_is_square.patch) by @jhpalmieri created at 2008-11-19 21:57:40",
    "created_at": "2008-11-19T21:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3891#issuecomment-27751",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [polynomial_is_square.patch](tarball://root/attachments/some-uuid/ticket3891/polynomial_is_square.patch) by @jhpalmieri created at 2008-11-19 21:57:40



---

archive/issue_comments_027752.json:
```json
{
    "body": "Attachment [trac3891-reviewer-fixes.patch](tarball://root/attachments/some-uuid/ticket3891/trac3891-reviewer-fixes.patch) by cwitty created at 2008-11-23 00:52:29\n\nPositive review for polynomial_is_square.patch, after my own trac3891-reviewer-fixes.patch is applied (so only my patch needs further review).\n\nI think Cremona may have been hoping for a polynomial sqrt that was more efficient than squarefree_decomposition; maybe that should be opened as a new wishlist ticket after this one is closed.",
    "created_at": "2008-11-23T00:52:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3891#issuecomment-27752",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac3891-reviewer-fixes.patch](tarball://root/attachments/some-uuid/ticket3891/trac3891-reviewer-fixes.patch) by cwitty created at 2008-11-23 00:52:29

Positive review for polynomial_is_square.patch, after my own trac3891-reviewer-fixes.patch is applied (so only my patch needs further review).

I think Cremona may have been hoping for a polynomial sqrt that was more efficient than squarefree_decomposition; maybe that should be opened as a new wishlist ticket after this one is closed.



---

archive/issue_comments_027753.json:
```json
{
    "body": "The reviewer's patch looks good to me, and all tests passed.  (I based the docstring for is_square on the one for the is_square method for integers, but your modifications make it better.)",
    "created_at": "2008-11-23T23:37:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3891#issuecomment-27753",
    "user": "https://github.com/jhpalmieri"
}
```

The reviewer's patch looks good to me, and all tests passed.  (I based the docstring for is_square on the one for the is_square method for integers, but your modifications make it better.)



---

archive/issue_events_008924.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-24T00:47:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3891",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3891#event-8924"
}
```



---

archive/issue_comments_027754.json:
```json
{
    "body": "Merged both patches in Sage 3.2.1.alpha1",
    "created_at": "2008-11-24T00:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3891#issuecomment-27754",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.2.1.alpha1



---

archive/issue_comments_027755.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-24T00:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3891#issuecomment-27755",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
