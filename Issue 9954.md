# Issue 9954: Rational(3)%Rational(-1) fails

archive/issues_009954.json:
```json
{
    "body": "Assignee: @aghitza\n\nThis is inconsistent\n\n\n```\nsage: Rational(3)%Rational(-1)\nZeroDivisionError: Inverse does not exist.\n```\n\n\nbut\n\n\n```\nsage: 3%(-1)\n0\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9955\n\n",
    "created_at": "2010-09-20T18:20:29Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "Rational(3)%Rational(-1) fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9954",
    "user": "https://github.com/haraldschilly"
}
```
Assignee: @aghitza

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

archive/issue_comments_099131.json:
```json
{
    "body": "This is caused by the following simpler bug:\n\n```\n\nsage: a=Integer(3)\nsage: b=Integer(-1)\nsage: a.inverse_mod(b)\n---------------------------------------------------------------------------\nZeroDivisionError                         Traceback (most recent call last)\n...\n\nZeroDivisionError: Inverse does not exist.\n```\n\nwhich is easy to fix.  In `sage.rings.integer.Integer.inverse_mod` there is special case for modulus n=1 but not for -1.  Either ass this special case, or replace n by abs(n).",
    "created_at": "2010-12-21T23:23:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9954#issuecomment-99131",
    "user": "https://github.com/JohnCremona"
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

archive/issue_comments_099132.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-27T11:08:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9954#issuecomment-99132",
    "user": "https://github.com/a-andre"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_099133.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-27T17:05:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9954#issuecomment-99133",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_099134.json:
```json
{
    "body": "The patch looks right and I tested that it works (but did not yet test the whole library).\n\nBUT you need to add a doctest to show that the bug has been fixed.  There's a similar doctest in the same function, so just add something similar.\n\nThen I'll look at it again.",
    "created_at": "2011-01-27T17:05:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9954#issuecomment-99134",
    "user": "https://github.com/JohnCremona"
}
```

The patch looks right and I tested that it works (but did not yet test the whole library).

BUT you need to add a doctest to show that the bug has been fixed.  There's a similar doctest in the same function, so just add something similar.

Then I'll look at it again.



---

archive/issue_comments_099135.json:
```json
{
    "body": "Attachment [trac_9955.patch](tarball://root/attachments/some-uuid/ticket9955/trac_9955.patch) by @a-andre created at 2011-01-28 08:42:14",
    "created_at": "2011-01-28T08:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9954#issuecomment-99135",
    "user": "https://github.com/a-andre"
}
```

Attachment [trac_9955.patch](tarball://root/attachments/some-uuid/ticket9955/trac_9955.patch) by @a-andre created at 2011-01-28 08:42:14



---

archive/issue_comments_099136.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-28T08:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9954#issuecomment-99136",
    "user": "https://github.com/a-andre"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099137.json:
```json
{
    "body": "doctest added",
    "created_at": "2011-01-28T08:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9954#issuecomment-99137",
    "user": "https://github.com/a-andre"
}
```

doctest added



---

archive/issue_comments_099138.json:
```json
{
    "body": "Replying to [comment:4 aapitzsch]:\n> doctest added\n\nThanks!  Positive review.",
    "created_at": "2011-01-28T20:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9954#issuecomment-99138",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:4 aapitzsch]:
> doctest added

Thanks!  Positive review.



---

archive/issue_comments_099139.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-28T20:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9954#issuecomment-99139",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_025114.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-02-07T08:13:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9954",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9954#event-25114"
}
```



---

archive/issue_comments_099140.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-02-07T08:13:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9954#issuecomment-99140",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
