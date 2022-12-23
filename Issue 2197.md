# Issue 2197: Elliptic Curve quadratic/quartic/sextic twists: unhelpful error message when D=0

archive/issues_002197.json:
```json
{
    "body": "Assignee: was\n\nThe code for quadratic, quartic and sextic twists of elliptic curves does not check that the twisting parameter is nonzero, and hence fail when a singular curve tries to be constructed.  Instead we output a helpful message.\n\nNote that in characteristic 2, the quadratic twist by 0 is allowed (but gives back the same curve), just as twisting by 1 in odd characteristic.\n\nThe patch provided also enhances the Hasse_bounds function (which should probably be put somewhere other than ell_generic.py).\n\nIssue created by migration from https://trac.sagemath.org/ticket/2197\n\n",
    "created_at": "2008-02-17T19:10:18Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "Elliptic Curve quadratic/quartic/sextic twists: unhelpful error message when D=0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2197",
    "user": "cremona"
}
```
Assignee: was

The code for quadratic, quartic and sextic twists of elliptic curves does not check that the twisting parameter is nonzero, and hence fail when a singular curve tries to be constructed.  Instead we output a helpful message.

Note that in characteristic 2, the quadratic twist by 0 is allowed (but gives back the same curve), just as twisting by 1 in odd characteristic.

The patch provided also enhances the Hasse_bounds function (which should probably be put somewhere other than ell_generic.py).

Issue created by migration from https://trac.sagemath.org/ticket/2197





---

archive/issue_comments_014434.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-02-17T21:16:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2197#issuecomment-14434",
    "user": "mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_014435.json:
```json
{
    "body": "This is a duplicate of #2196.",
    "created_at": "2008-02-17T21:16:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2197#issuecomment-14435",
    "user": "mabshoff"
}
```

This is a duplicate of #2196.
