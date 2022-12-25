# Issue 7116: Potential bug in elliptic curve pairing code.

archive/issues_007116.json:
```json
{
    "body": "Assignee: @loefflerd\n\n\n```\nI think there is a problem in the function\n\n ell_point._line_\n\nwhich is used in _miller_. I don't know if it will necessarily lead to\nincorrect results, since it's a degenerate case...\n\nThe method has form\n\n G._line_(R, Q)\n\nand returns the evaluation of Q at the line through G and R.\n\nThe problem occurs when Q is the point at infinity. In this case, I'm\npretty sure (it's been a while since I've thought about this kind of\nthing) that _line_ should return 0 if the line through G and R is\nvertical, and otherwise it should be undefined. The method is\nreturning an answer that assumes that Q is affine.\n\nWhile I don't have the most recent version (for reasons I won't bore\nyou with) I've checked the latest code on line, and it appears to not\nhave changed from what I have.\n\nI've attached a sample session.\n\n---\n\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: E = EllipticCurve([GF(17)(-1),GF(17)(0)])\nsage: G = E.random_point(); G\n(7 : 8 : 1)\nsage: minus_G = -G; minus_G\n(7 : 9 : 1)\nsage: G._line_(minus_G, E(0)) # should return 0\n10\nsage: two_G = 2*G; two_G\n(1 : 0 : 1)\nsage: G._line_(two_G, E(0)) # should be undefined/error\n11\nsage:\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7116\n\n",
    "created_at": "2009-10-04T18:34:44Z",
    "labels": [
        "component: elliptic curves",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Potential bug in elliptic curve pairing code.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7116",
    "user": "https://github.com/williamstein"
}
```
Assignee: @loefflerd


```
I think there is a problem in the function

 ell_point._line_

which is used in _miller_. I don't know if it will necessarily lead to
incorrect results, since it's a degenerate case...

The method has form

 G._line_(R, Q)

and returns the evaluation of Q at the line through G and R.

The problem occurs when Q is the point at infinity. In this case, I'm
pretty sure (it's been a while since I've thought about this kind of
thing) that _line_ should return 0 if the line through G and R is
vertical, and otherwise it should be undefined. The method is
returning an answer that assumes that Q is affine.

While I don't have the most recent version (for reasons I won't bore
you with) I've checked the latest code on line, and it appears to not
have changed from what I have.

I've attached a sample session.

---

----------------------------------------------------------------------
----------------------------------------------------------------------
sage: E = EllipticCurve([GF(17)(-1),GF(17)(0)])
sage: G = E.random_point(); G
(7 : 8 : 1)
sage: minus_G = -G; minus_G
(7 : 9 : 1)
sage: G._line_(minus_G, E(0)) # should return 0
10
sage: two_G = 2*G; two_G
(1 : 0 : 1)
sage: G._line_(two_G, E(0)) # should be undefined/error
11
sage:
```


Issue created by migration from https://trac.sagemath.org/ticket/7116





---

archive/issue_comments_058864.json:
```json
{
    "body": "The  function P._line(R,Q), as documented,  returns the value at Q of a suitably normalized function on the curve representing the straight line through P and R, where P and/or R are allowed to be the point O at infinity but Q is not.\n\nThe code as written does not work when Q=O, but this is not documented.  I suggest a fix whereby if Q==O then a ValueError is raised -- this is stricter than the remedy suggested, but I think more consistent since in this and similar cases the functions which are being evaluated are all in the polynomial ring k(x,y) of the curve and so should not be evaluated at O where they have poles.\n\nI'm also sure that in the places where this function is used, the condition Q==O does not arise.\n\nI'll make a patch,\n\nJohn",
    "created_at": "2009-10-04T20:10:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7116#issuecomment-58864",
    "user": "https://github.com/JohnCremona"
}
```

The  function P._line(R,Q), as documented,  returns the value at Q of a suitably normalized function on the curve representing the straight line through P and R, where P and/or R are allowed to be the point O at infinity but Q is not.

The code as written does not work when Q=O, but this is not documented.  I suggest a fix whereby if Q==O then a ValueError is raised -- this is stricter than the remedy suggested, but I think more consistent since in this and similar cases the functions which are being evaluated are all in the polynomial ring k(x,y) of the curve and so should not be evaluated at O where they have poles.

I'm also sure that in the places where this function is used, the condition Q==O does not arise.

I'll make a patch,

John



---

archive/issue_comments_058865.json:
```json
{
    "body": "Applies to 3.1.2.rc0",
    "created_at": "2009-10-04T20:24:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7116#issuecomment-58865",
    "user": "https://github.com/JohnCremona"
}
```

Applies to 3.1.2.rc0



---

archive/issue_comments_058866.json:
```json
{
    "body": "Changing assignee from @loefflerd to @JohnCremona.",
    "created_at": "2009-10-04T20:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7116#issuecomment-58866",
    "user": "https://github.com/JohnCremona"
}
```

Changing assignee from @loefflerd to @JohnCremona.



---

archive/issue_comments_058867.json:
```json
{
    "body": "Attachment [trac_7116-miller_functions.patch](tarball://root/attachments/some-uuid/ticket7116/trac_7116-miller_functions.patch) by @JohnCremona created at 2009-10-04 20:25:51\n\nThe patch tests for Q=0 in the functions `_line_` and `_miller_` and raise an error if so.  Doctests added.",
    "created_at": "2009-10-04T20:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7116#issuecomment-58867",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_7116-miller_functions.patch](tarball://root/attachments/some-uuid/ticket7116/trac_7116-miller_functions.patch) by @JohnCremona created at 2009-10-04 20:25:51

The patch tests for Q=0 in the functions `_line_` and `_miller_` and raise an error if so.  Doctests added.



---

archive/issue_comments_058868.json:
```json
{
    "body": "Changing keywords from \"\" to \"elliptic curve\".",
    "created_at": "2009-10-04T20:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7116#issuecomment-58868",
    "user": "https://github.com/JohnCremona"
}
```

Changing keywords from "" to "elliptic curve".



---

archive/issue_comments_058869.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-20T05:34:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7116#issuecomment-58869",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058870.json:
```json
{
    "body": "I think that condition is fine, now that it's properly documented.",
    "created_at": "2009-11-20T05:34:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7116#issuecomment-58870",
    "user": "https://github.com/robertwb"
}
```

I think that condition is fine, now that it's properly documented.



---

archive/issue_comments_058871.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-22T07:36:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7116#issuecomment-58871",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_007337.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-11-22T07:36:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7116",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7116#event-7337"
}
```
