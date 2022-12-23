# Issue 8348: find_root only works in fixed (double) precision

archive/issues_008348.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  was\n\nHow can one approximate the root of an equation in arbitrary\nprecision? For example I want the root of log(x+2) = x to\n50 digits of precision:\n\n```\nsage: (log(x+2)-x).find_root(1,2)\n1.1461932206205643\nsage: (log(x+2)-x).find_root(1,2,prec=150)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/users/caramel/zimmerma/try/<ipython console> in <module>()\n\n/usr/local/sage-core2/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.find_root (sage/symbolic/expression.cpp:24383)()\n\nTypeError: find_root() got an unexpected keyword argument 'prec'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8348\n\n",
    "created_at": "2010-02-24T16:23:17Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "find_root only works in fixed (double) precision",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8348",
    "user": "zimmerma"
}
```
Assignee: AlexGhitza

CC:  was

How can one approximate the root of an equation in arbitrary
precision? For example I want the root of log(x+2) = x to
50 digits of precision:

```
sage: (log(x+2)-x).find_root(1,2)
1.1461932206205643
sage: (log(x+2)-x).find_root(1,2,prec=150)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/users/caramel/zimmerma/try/<ipython console> in <module>()

/usr/local/sage-core2/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.find_root (sage/symbolic/expression.cpp:24383)()

TypeError: find_root() got an unexpected keyword argument 'prec'
```


Issue created by migration from https://trac.sagemath.org/ticket/8348





---

archive/issue_comments_074543.json:
```json
{
    "body": "This is about adding capability not currently present, so should be an enhancement.",
    "created_at": "2010-03-17T05:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8348",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8348#issuecomment-74543",
    "user": "jason"
}
```

This is about adding capability not currently present, so should be an enhancement.



---

archive/issue_comments_074544.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-03-17T05:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8348",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8348#issuecomment-74544",
    "user": "jason"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_074545.json:
```json
{
    "body": "> This is about adding capability not currently present, so should be an enhancement. \n\nI do not agree. The documentation does not say that `find_root` only works in double precision,\nthus this is a defect (at least of the documentation). Do you agree with that?",
    "created_at": "2010-03-17T07:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8348",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8348#issuecomment-74545",
    "user": "zimmerma"
}
```

> This is about adding capability not currently present, so should be an enhancement. 

I do not agree. The documentation does not say that `find_root` only works in double precision,
thus this is a defect (at least of the documentation). Do you agree with that?



---

archive/issue_comments_074546.json:
```json
{
    "body": "The docs for find_root don't imply that it uses arbitrary precision to me, so I agree it's an omission, but not a bug (i.e., it doesn't claim one thing and do another).  The only mention of precision in the docs (in the xtol and rtol parameters) implies that things work with double precision.\n\nBut this is a minor point.  I was trying to clean up the large number of tickets that are classified as \"bugs\" (which to me means things that Sage claims should work, but don't).\n\nIn this case, the error returned indicates that find_root knows nothing about a prec argument, which is appropriate.\n\nI've switched it back so we don't waste any more time fretting about how to classify this ticket.",
    "created_at": "2010-03-17T16:25:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8348",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8348#issuecomment-74546",
    "user": "jason"
}
```

The docs for find_root don't imply that it uses arbitrary precision to me, so I agree it's an omission, but not a bug (i.e., it doesn't claim one thing and do another).  The only mention of precision in the docs (in the xtol and rtol parameters) implies that things work with double precision.

But this is a minor point.  I was trying to clean up the large number of tickets that are classified as "bugs" (which to me means things that Sage claims should work, but don't).

In this case, the error returned indicates that find_root knows nothing about a prec argument, which is appropriate.

I've switched it back so we don't waste any more time fretting about how to classify this ticket.



---

archive/issue_comments_074547.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2010-03-17T16:25:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8348",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8348#issuecomment-74547",
    "user": "jason"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_074548.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-08-24T07:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8348",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8348#issuecomment-74548",
    "user": "zimmerma"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074549.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2013-08-24T07:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8348",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8348#issuecomment-74549",
    "user": "zimmerma"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_074550.json:
```json
{
    "body": "Attachment\n\nthe attached patch (produced against Sage 5.9) adds documentation to `find_root`.\nNote: I found out that `find_root` is duplicated in `numerical/optimize.py` and in `symbolic/expression.pyx`, which is unfortunate.\n\nPaul",
    "created_at": "2013-08-24T07:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8348",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8348#issuecomment-74550",
    "user": "zimmerma"
}
```

Attachment

the attached patch (produced against Sage 5.9) adds documentation to `find_root`.
Note: I found out that `find_root` is duplicated in `numerical/optimize.py` and in `symbolic/expression.pyx`, which is unfortunate.

Paul



---

archive/issue_comments_074551.json:
```json
{
    "body": "LGTM.\n\nReplying to [comment:6 zimmerma]:\n> Note: I found out that `find_root` is duplicated in `numerical/optimize.py` and in `symbolic/expression.pyx`, which is unfortunate.\n\nOnly (part of) the documentation is duplicated; one of the function is a wrapper for the other. It is unfortunate indeed, but that's a problem that occurs everywhere in Sage, so I don't think it really makes sense to open a ticket for that particular instance.\n----\nNew commits:",
    "created_at": "2014-01-29T07:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8348",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8348#issuecomment-74551",
    "user": "mmezzarobba"
}
```

LGTM.

Replying to [comment:6 zimmerma]:
> Note: I found out that `find_root` is duplicated in `numerical/optimize.py` and in `symbolic/expression.pyx`, which is unfortunate.

Only (part of) the documentation is duplicated; one of the function is a wrapper for the other. It is unfortunate indeed, but that's a problem that occurs everywhere in Sage, so I don't think it really makes sense to open a ticket for that particular instance.
----
New commits:



---

archive/issue_comments_074552.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-01-29T07:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8348",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8348#issuecomment-74552",
    "user": "mmezzarobba"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074553.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-02-01T15:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8348",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8348#issuecomment-74553",
    "user": "vbraun"
}
```

Resolution: fixed
