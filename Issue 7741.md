# Issue 7741: Can't construct a rational fraction from a symbolic one.

archive/issues_007741.json:
```json
{
    "body": "Assignee: robertwb\n\nCC:  burcin\n\nKeywords: Fraction Field, coercion\n\nGiven a symbolic expression which is a rational fraction sage refuse to convert it to a element of the Field of rational fraction:\n\n```\nhivert@boxen:~$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: fr = (1+x)/(1+x+x^2)\nsage: Fld = FractionField(PolynomialRing(QQ,x))\nsage: Fld(fr)\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (1181, 0))\n| Sage Version 4.2.1, Release Date: 2009-11-14                       |\n| Type notebook() for the GUI, and license() for information.        |\n[...]\n\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n[...]\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.pyc in _element_constructor_(self, x, check, is_gen, construct, **kwds)\n    304                 x = x.numerator() * x.denominator().inverse_of_unit()\n    305             else:\n--> 306                 raise TypeError, \"denominator must be a unit\"\n    307\n    308         elif isinstance(x, pari_gen):\n\nTypeError: denominator must be a unit\n```\n\n\nIt seems that it needs to convert is to a polynomial. Of course if one convert numerator and denominator separately everything is Ok:\n\n```\nsage: Fld((1+x))/(1+x+x^2)\n(x + 1)/(x^2 + x + 1)\n```\n\n\nI'm not sure about which component should be selected... Is it algebra, calculus or coercion...\n\nFlorent\n\nIssue created by migration from https://trac.sagemath.org/ticket/7741\n\n",
    "created_at": "2009-12-19T09:12:57Z",
    "labels": [
        "coercion",
        "major",
        "bug"
    ],
    "title": "Can't construct a rational fraction from a symbolic one.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7741",
    "user": "hivert"
}
```
Assignee: robertwb

CC:  burcin

Keywords: Fraction Field, coercion

Given a symbolic expression which is a rational fraction sage refuse to convert it to a element of the Field of rational fraction:

```
hivert@boxen:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: fr = (1+x)/(1+x+x^2)
sage: Fld = FractionField(PolynomialRing(QQ,x))
sage: Fld(fr)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1181, 0))
| Sage Version 4.2.1, Release Date: 2009-11-14                       |
| Type notebook() for the GUI, and license() for information.        |
[...]

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

[...]

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.pyc in _element_constructor_(self, x, check, is_gen, construct, **kwds)
    304                 x = x.numerator() * x.denominator().inverse_of_unit()
    305             else:
--> 306                 raise TypeError, "denominator must be a unit"
    307
    308         elif isinstance(x, pari_gen):

TypeError: denominator must be a unit
```


It seems that it needs to convert is to a polynomial. Of course if one convert numerator and denominator separately everything is Ok:

```
sage: Fld((1+x))/(1+x+x^2)
(x + 1)/(x^2 + x + 1)
```


I'm not sure about which component should be selected... Is it algebra, calculus or coercion...

Florent

Issue created by migration from https://trac.sagemath.org/ticket/7741





---

archive/issue_comments_066529.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T10:04:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7741#issuecomment-66529",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066530.json:
```json
{
    "body": "Attachment [7741-symbolic-frac.patch](tarball://root/attachments/some-uuid/ticket7741/7741-symbolic-frac.patch) by robertwb created at 2010-01-17 10:04:02",
    "created_at": "2010-01-17T10:04:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7741#issuecomment-66530",
    "user": "robertwb"
}
```

Attachment [7741-symbolic-frac.patch](tarball://root/attachments/some-uuid/ticket7741/7741-symbolic-frac.patch) by robertwb created at 2010-01-17 10:04:02



---

archive/issue_comments_066531.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T11:49:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7741#issuecomment-66531",
    "user": "hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066532.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-18T22:45:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7741#issuecomment-66532",
    "user": "rlm"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_066533.json:
```json
{
    "body": "Attachment [trac_7741-symbolic-frac-rebase.patch](tarball://root/attachments/some-uuid/ticket7741/trac_7741-symbolic-frac-rebase.patch) by davidloeffler created at 2010-06-29 09:41:41\n\nrebased to 4.4.4",
    "created_at": "2010-06-29T09:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7741#issuecomment-66533",
    "user": "davidloeffler"
}
```

Attachment [trac_7741-symbolic-frac-rebase.patch](tarball://root/attachments/some-uuid/ticket7741/trac_7741-symbolic-frac-rebase.patch) by davidloeffler created at 2010-06-29 09:41:41

rebased to 4.4.4



---

archive/issue_comments_066534.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-29T09:42:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7741#issuecomment-66534",
    "user": "davidloeffler"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066535.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-14T09:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7741#issuecomment-66535",
    "user": "demosd235"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066536.json:
```json
{
    "body": "William points out that `denominator is 1` will fail unless denominator is the Python int 1, and nothing else...\n\nIs this really preferable to `denominator == 1`?\n\nPS, Passes tests in `sage/rings/fraction_field_element.pyx`",
    "created_at": "2010-07-14T09:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7741#issuecomment-66536",
    "user": "demosd235"
}
```

William points out that `denominator is 1` will fail unless denominator is the Python int 1, and nothing else...

Is this really preferable to `denominator == 1`?

PS, Passes tests in `sage/rings/fraction_field_element.pyx`



---

archive/issue_comments_066537.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-29T05:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7741#issuecomment-66537",
    "user": "robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066538.json:
```json
{
    "body": "Attachment [7741-symbolic-frac-fixed.patch](tarball://root/attachments/some-uuid/ticket7741/7741-symbolic-frac-fixed.patch) by robertwb created at 2010-07-29 05:47:35\n\nActually, the \"is 1\" was intentional, as I wasn't thinking of taking that path if the user passed in a ring element (as opposed to the default value) and didn't want to make the default value None and handle it everywhere. In retrospect, I think it's fine for it to be equal to 1.",
    "created_at": "2010-07-29T05:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7741#issuecomment-66538",
    "user": "robertwb"
}
```

Attachment [7741-symbolic-frac-fixed.patch](tarball://root/attachments/some-uuid/ticket7741/7741-symbolic-frac-fixed.patch) by robertwb created at 2010-07-29 05:47:35

Actually, the "is 1" was intentional, as I wasn't thinking of taking that path if the user passed in a ring element (as opposed to the default value) and didn't want to make the default value None and handle it everywhere. In retrospect, I think it's fine for it to be equal to 1.



---

archive/issue_comments_066539.json:
```json
{
    "body": "apply only attachment:7741-symbolic-frac-fixed.patch.",
    "created_at": "2010-09-25T10:49:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7741#issuecomment-66539",
    "user": "burcin"
}
```

apply only attachment:7741-symbolic-frac-fixed.patch.



---

archive/issue_comments_066540.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-25T10:49:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7741#issuecomment-66540",
    "user": "burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066541.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T04:25:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7741#issuecomment-66541",
    "user": "mpatel"
}
```

Resolution: fixed
