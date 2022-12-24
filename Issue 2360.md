# Issue 2360: Strange Polynomial substitution problem

archive/issues_002360.json:
```json
{
    "body": "Assignee: was\n\nI made a stupid error plugging a list into a polynomial, but it uncovered this very strange bug:\n\n\n```\nsage: R.<x,y,z,u,v,w>=ZZ[]\nsage: P.<a>=ZZ[]\nsage: e=[x^2,y^3]\nsage: f=6*a^4\nsage: f(x)\n6*x^4\nsage: f(e)\nException exceptions.TypeError: \"can't multiply sequence by non-int of type 'list'\" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored\nException exceptions.TypeError: \"unsupported operand type(s) for *: 'NoneType' and 'NoneType'\" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored\nException exceptions.TypeError: \"unsupported operand parent(s) for '*': 'Integer Ring' and '<type 'NoneType'>'\" in 'sage.rings.polynomial.polynomial_compiled.mul_pd.eval' ignored\nsage: f(x)\nException exceptions.TypeError: \"can't multiply sequence by non-int of type 'list'\" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored\nException exceptions.TypeError: \"unsupported operand type(s) for *: 'NoneType' and 'NoneType'\" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored\nException exceptions.TypeError: \"unsupported operand parent(s) for '*': 'Integer Ring' and '<type 'NoneType'>'\" in 'sage.rings.polynomial.polynomial_compiled.mul_pd.eval' ignored\n```\n\n\nNotice that the plugging in the list seemed to ruin the polynomial good and proper.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2360\n\n",
    "created_at": "2008-03-01T16:52:49Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Strange Polynomial substitution problem",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2360",
    "user": "jbmohler"
}
```
Assignee: was

I made a stupid error plugging a list into a polynomial, but it uncovered this very strange bug:


```
sage: R.<x,y,z,u,v,w>=ZZ[]
sage: P.<a>=ZZ[]
sage: e=[x^2,y^3]
sage: f=6*a^4
sage: f(x)
6*x^4
sage: f(e)
Exception exceptions.TypeError: "can't multiply sequence by non-int of type 'list'" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored
Exception exceptions.TypeError: "unsupported operand type(s) for *: 'NoneType' and 'NoneType'" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored
Exception exceptions.TypeError: "unsupported operand parent(s) for '*': 'Integer Ring' and '<type 'NoneType'>'" in 'sage.rings.polynomial.polynomial_compiled.mul_pd.eval' ignored
sage: f(x)
Exception exceptions.TypeError: "can't multiply sequence by non-int of type 'list'" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored
Exception exceptions.TypeError: "unsupported operand type(s) for *: 'NoneType' and 'NoneType'" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored
Exception exceptions.TypeError: "unsupported operand parent(s) for '*': 'Integer Ring' and '<type 'NoneType'>'" in 'sage.rings.polynomial.polynomial_compiled.mul_pd.eval' ignored
```


Notice that the plugging in the list seemed to ruin the polynomial good and proper.

Issue created by migration from https://trac.sagemath.org/ticket/2360





---

archive/issue_comments_015910.json:
```json
{
    "body": "Changing assignee from was to somebody.",
    "created_at": "2008-03-01T16:53:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2360#issuecomment-15910",
    "user": "jbmohler"
}
```

Changing assignee from was to somebody.



---

archive/issue_comments_015911.json:
```json
{
    "body": "Changing component from algebraic geometry to basic arithmetic.",
    "created_at": "2008-03-01T16:53:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2360#issuecomment-15911",
    "user": "jbmohler"
}
```

Changing component from algebraic geometry to basic arithmetic.



---

archive/issue_comments_015912.json:
```json
{
    "body": "Ah, it's even easier.  No second mpoly ring required!\n\n\n```\nsage: P.<a>=ZZ[]\nsage: f=6*a^4\nsage: f(1)\n6\nsage: f([1,2,3])\nException exceptions.TypeError: \"can't multiply sequence by non-int of type 'list'\" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored\nException exceptions.TypeError: \"unsupported operand type(s) for *: 'NoneType' and 'NoneType'\" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored\nException exceptions.TypeError: \"unsupported operand parent(s) for '*': 'Integer Ring' and '<type 'NoneType'>'\" in 'sage.rings.polynomial.polynomial_compiled.mul_pd.eval' ignored\nsage: f(1)  #  WHAT HAPPENED -- this worked before.\nException exceptions.TypeError: \"can't multiply sequence by non-int of type 'list'\" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored\nException exceptions.TypeError: \"unsupported operand type(s) for *: 'NoneType' and 'NoneType'\" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored\nException exceptions.TypeError: \"unsupported operand parent(s) for '*': 'Integer Ring' and '<type 'NoneType'>'\" in 'sage.rings.polynomial.polynomial_compiled.mul_pd.eval' ignored\n```\n",
    "created_at": "2008-03-01T16:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2360#issuecomment-15912",
    "user": "jbmohler"
}
```

Ah, it's even easier.  No second mpoly ring required!


```
sage: P.<a>=ZZ[]
sage: f=6*a^4
sage: f(1)
6
sage: f([1,2,3])
Exception exceptions.TypeError: "can't multiply sequence by non-int of type 'list'" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored
Exception exceptions.TypeError: "unsupported operand type(s) for *: 'NoneType' and 'NoneType'" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored
Exception exceptions.TypeError: "unsupported operand parent(s) for '*': 'Integer Ring' and '<type 'NoneType'>'" in 'sage.rings.polynomial.polynomial_compiled.mul_pd.eval' ignored
sage: f(1)  #  WHAT HAPPENED -- this worked before.
Exception exceptions.TypeError: "can't multiply sequence by non-int of type 'list'" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored
Exception exceptions.TypeError: "unsupported operand type(s) for *: 'NoneType' and 'NoneType'" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored
Exception exceptions.TypeError: "unsupported operand parent(s) for '*': 'Integer Ring' and '<type 'NoneType'>'" in 'sage.rings.polynomial.polynomial_compiled.mul_pd.eval' ignored
```




---

archive/issue_comments_015913.json:
```json
{
    "body": "The attached patch fixes the issue. Credit goes to Tom Boothby too.",
    "created_at": "2009-01-22T06:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2360#issuecomment-15913",
    "user": "malb"
}
```

The attached patch fixes the issue. Credit goes to Tom Boothby too.



---

archive/issue_comments_015914.json:
```json
{
    "body": "The patch fixes the issue, but I'd rather have the original error about multiplying lists propagate up instead of a generic \"RuntimeError: Polynomial evaluation error in val()!\"",
    "created_at": "2009-01-23T22:34:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2360#issuecomment-15914",
    "user": "robertwb"
}
```

The patch fixes the issue, but I'd rather have the original error about multiplying lists propagate up instead of a generic "RuntimeError: Polynomial evaluation error in val()!"



---

archive/issue_comments_015915.json:
```json
{
    "body": "Attachment [trac_2360_fix.patch](tarball://root/attachments/some-uuid/ticket2360/trac_2360_fix.patch) by malb created at 2009-01-24 12:42:22",
    "created_at": "2009-01-24T12:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2360#issuecomment-15915",
    "user": "malb"
}
```

Attachment [trac_2360_fix.patch](tarball://root/attachments/some-uuid/ticket2360/trac_2360_fix.patch) by malb created at 2009-01-24 12:42:22



---

archive/issue_comments_015916.json:
```json
{
    "body": "I updated the patch.",
    "created_at": "2009-01-24T12:42:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2360#issuecomment-15916",
    "user": "malb"
}
```

I updated the patch.



---

archive/issue_comments_015917.json:
```json
{
    "body": "OK, that looks good.",
    "created_at": "2009-01-24T21:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2360#issuecomment-15917",
    "user": "robertwb"
}
```

OK, that looks good.



---

archive/issue_comments_015918.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T23:00:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2360#issuecomment-15918",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2.

Cheers,

Michael



---

archive/issue_comments_015919.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T23:00:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2360#issuecomment-15919",
    "user": "mabshoff"
}
```

Resolution: fixed
