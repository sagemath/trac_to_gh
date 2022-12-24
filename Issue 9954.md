# Issue 9954: Rational(3)%Rational(-1) fails

archive/issues_009954.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nThis is inconsistent\n\n\n```\nsage: Rational(3)%Rational(-1)\nZeroDivisionError: Inverse does not exist.\n```\n\n\nbut\n\n\n```\nsage: 3%(-1)\n0\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9955\n\n",
    "created_at": "2010-09-20T18:20:29Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "Rational(3)%Rational(-1) fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9954",
    "user": "schilly"
}
```
Assignee: AlexGhitza

This is inconsistent


```
sage: Rational(3)%Rational(-1)
ZeroDivisionError: Inverse does not exist.
```


but


```
sage: 3%(-1)
0
```


Issue created by migration from https://trac.sagemath.org/ticket/9955





---

archive/issue_comments_099296.json:
```json
{
    "body": "This is caused by the following simpler bug:\n\n```\n\nsage: a=Integer(3)\nsage: b=Integer(-1)\nsage: a.inverse_mod(b)\n---------------------------------------------------------------------------\nZeroDivisionError                         Traceback (most recent call last)\n...\n\nZeroDivisionError: Inverse does not exist.\n```\n\nwhich is easy to fix.  In `sage.rings.integer.Integer.inverse_mod` there is special case for modulus n=1 but not for -1.  Either ass this special case, or replace n by abs(n).",
    "created_at": "2010-12-21T23:23:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9954#issuecomment-99296",
    "user": "cremona"
}
```

This is caused by the following simpler bug:

```

sage: a=Integer(3)
sage: b=Integer(-1)
sage: a.inverse_mod(b)
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
...

ZeroDivisionError: Inverse does not exist.
```

which is easy to fix.  In `sage.rings.integer.Integer.inverse_mod` there is special case for modulus n=1 but not for -1.  Either ass this special case, or replace n by abs(n).



---

archive/issue_comments_099297.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-27T11:08:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9954#issuecomment-99297",
    "user": "aapitzsch"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_099298.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-27T17:05:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9954#issuecomment-99298",
    "user": "cremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_099299.json:
```json
{
    "body": "The patch looks right and I tested that it works (but did not yet test the whole library).\n\nBUT you need to add a doctest to show that the bug has been fixed.  There's a similar doctest in the same function, so just add something similar.\n\nThen I'll look at it again.",
    "created_at": "2011-01-27T17:05:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9954#issuecomment-99299",
    "user": "cremona"
}
```

The patch looks right and I tested that it works (but did not yet test the whole library).

BUT you need to add a doctest to show that the bug has been fixed.  There's a similar doctest in the same function, so just add something similar.

Then I'll look at it again.



---

archive/issue_comments_099300.json:
```json
{
    "body": "Attachment [trac_9955.patch](tarball://root/attachments/some-uuid/ticket9955/trac_9955.patch) by aapitzsch created at 2011-01-28 08:42:14",
    "created_at": "2011-01-28T08:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9954#issuecomment-99300",
    "user": "aapitzsch"
}
```

Attachment [trac_9955.patch](tarball://root/attachments/some-uuid/ticket9955/trac_9955.patch) by aapitzsch created at 2011-01-28 08:42:14



---

archive/issue_comments_099301.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-28T08:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9954#issuecomment-99301",
    "user": "aapitzsch"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099302.json:
```json
{
    "body": "doctest added",
    "created_at": "2011-01-28T08:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9954#issuecomment-99302",
    "user": "aapitzsch"
}
```

doctest added



---

archive/issue_comments_099303.json:
```json
{
    "body": "Replying to [comment:4 aapitzsch]:\n> doctest added\n\nThanks!  Positive review.",
    "created_at": "2011-01-28T20:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9954#issuecomment-99303",
    "user": "cremona"
}
```

Replying to [comment:4 aapitzsch]:
> doctest added

Thanks!  Positive review.



---

archive/issue_comments_099304.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-28T20:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9954#issuecomment-99304",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_099305.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-02-07T08:13:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9954#issuecomment-99305",
    "user": "jdemeyer"
}
```

Resolution: fixed
