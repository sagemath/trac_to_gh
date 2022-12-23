# Issue 9335: linear independence of points on an elliptic curve

archive/issues_009335.json:
```json
{
    "body": "Assignee: was\n\nCC:  cremona\n\nDuring Sage Days 21 (while porting David Roberts' and John Cremona's  implementation of 2-descent for elliptic curves over function fields), we came across the Magma function IsLinearlyIndependent, which does not appear to have an analogue in Sage. \n\nWhat it does is the following: given a list of points on an elliptic curve, it returns true iff the points are linearly independent; else it returns false and a vector of coefficients specifying a linear combination of the points that results in torsion.\n\nWe would like to have a function that does this in Sage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9335\n\n",
    "created_at": "2010-06-25T07:11:16Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "title": "linear independence of points on an elliptic curve",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9335",
    "user": "jen"
}
```
Assignee: was

CC:  cremona

During Sage Days 21 (while porting David Roberts' and John Cremona's  implementation of 2-descent for elliptic curves over function fields), we came across the Magma function IsLinearlyIndependent, which does not appear to have an analogue in Sage. 

What it does is the following: given a list of points on an elliptic curve, it returns true iff the points are linearly independent; else it returns false and a vector of coefficients specifying a linear combination of the points that results in torsion.

We would like to have a function that does this in Sage.

Issue created by migration from https://trac.sagemath.org/ticket/9335





---

archive/issue_comments_088142.json:
```json
{
    "body": "+1!\n\nSuch a function exists somewhere in eclib.  I'm not suggesting that it should be wrapped, but could be used as a model.  Something I would be happy to do!",
    "created_at": "2010-06-25T07:42:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9335#issuecomment-88142",
    "user": "cremona"
}
```

+1!

Such a function exists somewhere in eclib.  I'm not suggesting that it should be wrapped, but could be used as a model.  Something I would be happy to do!



---

archive/issue_comments_088143.json:
```json
{
    "body": "Changing assignee from was to cremona.",
    "created_at": "2013-07-25T17:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9335#issuecomment-88143",
    "user": "davidloeffler"
}
```

Changing assignee from was to cremona.



---

archive/issue_comments_088144.json:
```json
{
    "body": "Changing component from number theory to elliptic curves.",
    "created_at": "2013-07-25T17:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9335#issuecomment-88144",
    "user": "davidloeffler"
}
```

Changing component from number theory to elliptic curves.
