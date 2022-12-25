# Issue 5917: Failing conversions for multipolynomial rings over fraction fields

archive/issues_005917.json:
```json
{
    "body": "Assignee: @malb\n\nKeywords: polynomial ring fraction field conversion\n\nThe following is with sage-3.4.1 on sage.math:\n\nSetting:\n\n```\nsage: F1 = FractionField(PolynomialRing(QQ,'a'))\nsage: R11 = F1['x']\nsage: R12 = F1['x','y']\nsage: F2 = FractionField(PolynomialRing(QQ,['a','b']))\nsage: R21 = F2['x']\nsage: R22 = F2['x','y']\n```\n\n\nHere I try various conversions, some of them go boom:\n\n```\nsage: F1('a')\na\nsage: F2('a')\na\nsage: R11('a')\na\nsage: R12('a')\nTraceback (most recent call last):\n...\nTypeError: unable to convert string\nsage: R21('a')\na\nsage: R22('a')\nTraceback (most recent call last):\n...\nTypeError: unable to convert string\nsage: R11(F1('a'))\na\nsage: R12(F1('a'))\na\nsage: R21(F2('a'))\na\nsage: R22(F2('a'))\na\nsage: F1(R11(F1('a')))\na\nsage: F1(R12(F1('a')))\nTraceback (most recent call last)\n...\nTypeError: unable to convert a to a rational\nsage: F2(R21(F2('a')))\na\nsage: F2(R22(F2('a')))\nTraceback (most recent call last)\n...\nTypeError:\n```\n\n\nNote that in the last example there is no error message. So, it seems to be different from the previous error (\"unable to convert a to a rational\")\n\n**__Conclusion:__**\n* Conversion from string to fraction field is OK both with one and two variables.\n* Conversion from a string to a univariate polynomial ring over a fraction field works, but fails for multivariate polynomial rings over a fraction field.\n* Conversion from a fraction field to a polynomial ring over this fraction field works both uni- and multivariately.\n* Conversion of a *scalar* element of a *multivariate* polynomial ring over a fraction field into that fraction field fails. The univariate case seems ok. The error seems to depend on the number of variables of the fraction field.\n\nSince conversion is something very elementary, I consider it a critical bug if it does not work (but not a blocker since it doesn't affect coercion). \n\nProbably it is too late for sage-3.4.2, so, I give it the Milestone 4.0.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5917\n\n",
    "created_at": "2009-04-28T10:48:22Z",
    "labels": [
        "component: commutative algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.7",
    "title": "Failing conversions for multipolynomial rings over fraction fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5917",
    "user": "https://github.com/simon-king-jena"
}
```
Assignee: @malb

Keywords: polynomial ring fraction field conversion

The following is with sage-3.4.1 on sage.math:

Setting:

```
sage: F1 = FractionField(PolynomialRing(QQ,'a'))
sage: R11 = F1['x']
sage: R12 = F1['x','y']
sage: F2 = FractionField(PolynomialRing(QQ,['a','b']))
sage: R21 = F2['x']
sage: R22 = F2['x','y']
```


Here I try various conversions, some of them go boom:

```
sage: F1('a')
a
sage: F2('a')
a
sage: R11('a')
a
sage: R12('a')
Traceback (most recent call last):
...
TypeError: unable to convert string
sage: R21('a')
a
sage: R22('a')
Traceback (most recent call last):
...
TypeError: unable to convert string
sage: R11(F1('a'))
a
sage: R12(F1('a'))
a
sage: R21(F2('a'))
a
sage: R22(F2('a'))
a
sage: F1(R11(F1('a')))
a
sage: F1(R12(F1('a')))
Traceback (most recent call last)
...
TypeError: unable to convert a to a rational
sage: F2(R21(F2('a')))
a
sage: F2(R22(F2('a')))
Traceback (most recent call last)
...
TypeError:
```


Note that in the last example there is no error message. So, it seems to be different from the previous error ("unable to convert a to a rational")

**__Conclusion:__**
* Conversion from string to fraction field is OK both with one and two variables.
* Conversion from a string to a univariate polynomial ring over a fraction field works, but fails for multivariate polynomial rings over a fraction field.
* Conversion from a fraction field to a polynomial ring over this fraction field works both uni- and multivariately.
* Conversion of a *scalar* element of a *multivariate* polynomial ring over a fraction field into that fraction field fails. The univariate case seems ok. The error seems to depend on the number of variables of the fraction field.

Since conversion is something very elementary, I consider it a critical bug if it does not work (but not a blocker since it doesn't affect coercion). 

Probably it is too late for sage-3.4.2, so, I give it the Milestone 4.0.

Issue created by migration from https://trac.sagemath.org/ticket/5917





---

archive/issue_comments_046670.json:
```json
{
    "body": "This has (apparently?) been fixed. At the very least, in sage 5.5 these examples no longer raise any exceptions...",
    "created_at": "2013-01-03T10:26:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5917#issuecomment-46670",
    "user": "https://trac.sagemath.org/admin/accounts/users/Bouillaguet"
}
```

This has (apparently?) been fixed. At the very least, in sage 5.5 these examples no longer raise any exceptions...



---

archive/issue_comments_046671.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-01-03T10:26:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5917#issuecomment-46671",
    "user": "https://trac.sagemath.org/admin/accounts/users/Bouillaguet"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_046672.json:
```json
{
    "body": "Add doctest to make sure it won't happen again",
    "created_at": "2013-01-04T16:29:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5917#issuecomment-46672",
    "user": "https://trac.sagemath.org/admin/accounts/users/Bouillaguet"
}
```

Add doctest to make sure it won't happen again



---

archive/issue_comments_046673.json:
```json
{
    "body": "Changing keywords from \"polynomial ring fraction field conversion\" to \"polynomial ring fraction field conversion trivial beginner\".",
    "created_at": "2013-01-04T16:30:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5917#issuecomment-46673",
    "user": "https://trac.sagemath.org/admin/accounts/users/Bouillaguet"
}
```

Changing keywords from "polynomial ring fraction field conversion" to "polynomial ring fraction field conversion trivial beginner".



---

archive/issue_comments_046674.json:
```json
{
    "body": "Attachment [5917_add_doctest.patch](tarball://root/attachments/some-uuid/ticket5917/5917_add_doctest.patch) by Bouillaguet created at 2013-01-04 16:30:09",
    "created_at": "2013-01-04T16:30:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5917#issuecomment-46674",
    "user": "https://trac.sagemath.org/admin/accounts/users/Bouillaguet"
}
```

Attachment [5917_add_doctest.patch](tarball://root/attachments/some-uuid/ticket5917/5917_add_doctest.patch) by Bouillaguet created at 2013-01-04 16:30:09



---

archive/issue_comments_046675.json:
```json
{
    "body": "Since the patchbot does not complain and the added tests do ensure that the bug remains fixed, I'm giving it a positive review.",
    "created_at": "2013-01-21T11:00:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5917#issuecomment-46675",
    "user": "https://github.com/simon-king-jena"
}
```

Since the patchbot does not complain and the added tests do ensure that the bug remains fixed, I'm giving it a positive review.



---

archive/issue_comments_046676.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-21T11:00:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5917#issuecomment-46676",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_046677.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-01-25T13:06:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5917#issuecomment-46677",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
