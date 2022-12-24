# Issue 6161: Polynomial rings have no coercion map to themselves

archive/issues_006161.json:
```json
{
    "body": "Assignee: malb\n\nKeywords: coercion polynomial\n\nThe following happens with the 'official' Sage 4.0 on sage.math and on at least one other x_86_64 machine (built from sources and in addition with the singular-3-1-0-spkg). It also occurs at least with sage 3.4.2.\n\n```\nsage: R.<x>=QQ[]\nsage: R._has_coerce_map_from(R)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/SimonKing/.sage/temp/sage.math.washington.edu/2444/_home_SimonKing__sage_init_sage_0.py in <module>()\n\nTypeError: 'dict' object is not callable\nsage: R.<x,y>=QQ[]\nsage: R._has_coerce_map_from(R)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/SimonKing/.sage/temp/sage.math.washington.edu/2444/_home_SimonKing__sage_init_sage_0.py in <module>()\n\nTypeError: 'dict' object is not callable\n```\n\n\nSo, both uni- and multivariate polynomial rings do not believe that they have a coercion to themselves. Or: Coercion of polynomial rings is seriously broken. \n\nI really wonder why this does not break hundreds of doc tests. I hope it is ok to make this a blocker.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6161\n\n",
    "created_at": "2009-05-30T22:13:32Z",
    "labels": [
        "commutative algebra",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Polynomial rings have no coercion map to themselves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6161",
    "user": "SimonKing"
}
```
Assignee: malb

Keywords: coercion polynomial

The following happens with the 'official' Sage 4.0 on sage.math and on at least one other x_86_64 machine (built from sources and in addition with the singular-3-1-0-spkg). It also occurs at least with sage 3.4.2.

```
sage: R.<x>=QQ[]
sage: R._has_coerce_map_from(R)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/SimonKing/.sage/temp/sage.math.washington.edu/2444/_home_SimonKing__sage_init_sage_0.py in <module>()

TypeError: 'dict' object is not callable
sage: R.<x,y>=QQ[]
sage: R._has_coerce_map_from(R)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/SimonKing/.sage/temp/sage.math.washington.edu/2444/_home_SimonKing__sage_init_sage_0.py in <module>()

TypeError: 'dict' object is not callable
```


So, both uni- and multivariate polynomial rings do not believe that they have a coercion to themselves. Or: Coercion of polynomial rings is seriously broken. 

I really wonder why this does not break hundreds of doc tests. I hope it is ok to make this a blocker.


Issue created by migration from https://trac.sagemath.org/ticket/6161





---

archive/issue_comments_049142.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-05-31T19:25:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6161#issuecomment-49142",
    "user": "mhansen"
}
```

Resolution: invalid



---

archive/issue_comments_049143.json:
```json
{
    "body": "Simon,\n\nYou're using _has_coerce_map_from incorrectly.  The error you get is be cause it is actually a dictionary and not an function.  See:\n\n\n```\nsage: R.<x,y> = QQ[]\nsage: R.coerce_map_from(R)\nIdentity endomorphism of Multivariate Polynomial Ring in x, y over Rational Field\nsage: R.<x> = QQ[]\nsage: R.coerce_map_from(R)\nIdentity endomorphism of Univariate Polynomial Ring in x over Rational Field\n```\n\n\nI'm going to close this an invalid.  A more appropriate ticket should be opened if there is a failure you're trying to fix.",
    "created_at": "2009-05-31T19:25:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6161#issuecomment-49143",
    "user": "mhansen"
}
```

Simon,

You're using _has_coerce_map_from incorrectly.  The error you get is be cause it is actually a dictionary and not an function.  See:


```
sage: R.<x,y> = QQ[]
sage: R.coerce_map_from(R)
Identity endomorphism of Multivariate Polynomial Ring in x, y over Rational Field
sage: R.<x> = QQ[]
sage: R.coerce_map_from(R)
Identity endomorphism of Univariate Polynomial Ring in x over Rational Field
```


I'm going to close this an invalid.  A more appropriate ticket should be opened if there is a failure you're trying to fix.
