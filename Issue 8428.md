# Issue 8428: Problem with rational_points over plane curves

archive/issues_008428.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  cremona\n\nThe newly \"improved\" rational_points function for plane curves (#8193) has a bug; if for some (Y,Z) the polynomial defining the curve becomes identically 0, it returns a ValueError caused by the function trying to factorise 0 as a polynomial.\n\nHere is an example\n\n\n```\nsage: F = GF(2)\nsage: P2.<X,Y,Z> = ProjectiveSpace(F,2)\nsage: C = Curve(X*Y)\nsage: a = C.rational_points_iterator()\nsage: a.next()\n(1 : 0 : 0)\nsage: a.next()\n(0 : 1 : 0)\nsage: a.next()\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/home/charlie/<ipython console> in <module>()\n\n/home/charlie/sage-current/local/lib/python2.6/site-packages/sage/schemes/plane_curves/projective_curve.pyc\nin rational_points_iterator(self)\n   353         # points with Z = 1\n   354         for y in K:\n--> 355             for x in R(g(X,y,one)).roots(multiplicities=False):\n   356                 yield(self.point([x,y,one]))\n   357\n\n/home/charlie/sage-current/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so\nin sage.rings.polynomial.polynomial_element.Polynomial.roots\n(sage/rings/polynomial/polynomial_element.c:30111)()\n\n/home/charlie/sage-current/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so\nin sage.rings.polynomial.polynomial_element.Polynomial.factor\n(sage/rings/polynomial/polynomial_element.c:18463)()\nValueError: factorization of 0 not defined\n```\n\n\nA patch to improve this is on its way.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8428\n\n",
    "created_at": "2010-03-03T10:51:06Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Problem with rational_points over plane curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8428",
    "user": "cturner"
}
```
Assignee: AlexGhitza

CC:  cremona

The newly "improved" rational_points function for plane curves (#8193) has a bug; if for some (Y,Z) the polynomial defining the curve becomes identically 0, it returns a ValueError caused by the function trying to factorise 0 as a polynomial.

Here is an example


```
sage: F = GF(2)
sage: P2.<X,Y,Z> = ProjectiveSpace(F,2)
sage: C = Curve(X*Y)
sage: a = C.rational_points_iterator()
sage: a.next()
(1 : 0 : 0)
sage: a.next()
(0 : 1 : 0)
sage: a.next()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/charlie/<ipython console> in <module>()

/home/charlie/sage-current/local/lib/python2.6/site-packages/sage/schemes/plane_curves/projective_curve.pyc
in rational_points_iterator(self)
   353         # points with Z = 1
   354         for y in K:
--> 355             for x in R(g(X,y,one)).roots(multiplicities=False):
   356                 yield(self.point([x,y,one]))
   357

/home/charlie/sage-current/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so
in sage.rings.polynomial.polynomial_element.Polynomial.roots
(sage/rings/polynomial/polynomial_element.c:30111)()

/home/charlie/sage-current/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so
in sage.rings.polynomial.polynomial_element.Polynomial.factor
(sage/rings/polynomial/polynomial_element.c:18463)()
ValueError: factorization of 0 not defined
```


A patch to improve this is on its way.

Issue created by migration from https://trac.sagemath.org/ticket/8428





---

archive/issue_comments_075556.json:
```json
{
    "body": "Applies to 4.3.3",
    "created_at": "2010-03-04T10:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8428#issuecomment-75556",
    "user": "cturner"
}
```

Applies to 4.3.3



---

archive/issue_comments_075557.json:
```json
{
    "body": "Attachment [trac_8428_rational_points_iterator.2.patch](tarball://root/attachments/some-uuid/ticket8428/trac_8428_rational_points_iterator.2.patch) by cturner created at 2010-03-04 10:25:46\n\nApplies to 4.3.3",
    "created_at": "2010-03-04T10:25:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8428#issuecomment-75557",
    "user": "cturner"
}
```

Attachment [trac_8428_rational_points_iterator.2.patch](tarball://root/attachments/some-uuid/ticket8428/trac_8428_rational_points_iterator.2.patch) by cturner created at 2010-03-04 10:25:46

Applies to 4.3.3



---

archive/issue_comments_075558.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-04T10:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8428#issuecomment-75558",
    "user": "cturner"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075559.json:
```json
{
    "body": "Attachment [trac_8428_rational_points_iterator.patch](tarball://root/attachments/some-uuid/ticket8428/trac_8428_rational_points_iterator.patch) by cturner created at 2010-03-04 10:27:11",
    "created_at": "2010-03-04T10:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8428#issuecomment-75559",
    "user": "cturner"
}
```

Attachment [trac_8428_rational_points_iterator.patch](tarball://root/attachments/some-uuid/ticket8428/trac_8428_rational_points_iterator.patch) by cturner created at 2010-03-04 10:27:11



---

archive/issue_comments_075560.json:
```json
{
    "body": "Apologies; both copies of the patch are the same, I double-clicked and am unable to remove the 2nd copy.",
    "created_at": "2010-03-04T10:29:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8428#issuecomment-75560",
    "user": "cturner"
}
```

Apologies; both copies of the patch are the same, I double-clicked and am unable to remove the 2nd copy.



---

archive/issue_comments_075561.json:
```json
{
    "body": "Changing assignee from AlexGhitza to cturner.",
    "created_at": "2010-03-04T10:29:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8428#issuecomment-75561",
    "user": "cturner"
}
```

Changing assignee from AlexGhitza to cturner.



---

archive/issue_comments_075562.json:
```json
{
    "body": "Changing assignee from cturner to AlexGhitza.",
    "created_at": "2010-03-04T10:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8428#issuecomment-75562",
    "user": "cturner"
}
```

Changing assignee from cturner to AlexGhitza.



---

archive/issue_comments_075563.json:
```json
{
    "body": "Fixes the bug, doctested and doctests pass.  Positive review.",
    "created_at": "2010-03-13T02:04:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8428#issuecomment-75563",
    "user": "roed"
}
```

Fixes the bug, doctested and doctests pass.  Positive review.



---

archive/issue_comments_075564.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-13T02:04:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8428#issuecomment-75564",
    "user": "roed"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075565.json:
```json
{
    "body": "Merged \"trac_8428_rational_points_iterator.patch\" into 4.4.alpha0.",
    "created_at": "2010-04-15T23:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8428#issuecomment-75565",
    "user": "jhpalmieri"
}
```

Merged "trac_8428_rational_points_iterator.patch" into 4.4.alpha0.



---

archive/issue_comments_075566.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T23:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8428#issuecomment-75566",
    "user": "jhpalmieri"
}
```

Resolution: fixed
