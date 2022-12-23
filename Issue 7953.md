# Issue 7953: Curve printing only shows first defining equation

archive/issues_007953.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nReported by Ronald van Luijk:\n\nThe `print C` below only prints the first defining equation.\n\n\n```\nsage: # problem printing\nsage: A.<x,y,z>=AffineSpace(QQ,3)\nsage: C=Curve([x-y,2-z])\nsage: print C\nAffine Space Curve over Rational Field defined by x - y\nsage: print C.defining_ideal()\nIdeal (x - y, -z + 2) of Multivariate Polynomial Ring in x, y, z over Rational Field\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7953\n\n",
    "created_at": "2010-01-16T18:10:54Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "Curve printing only shows first defining equation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7953",
    "user": "wjp"
}
```
Assignee: AlexGhitza

Reported by Ronald van Luijk:

The `print C` below only prints the first defining equation.


```
sage: # problem printing
sage: A.<x,y,z>=AffineSpace(QQ,3)
sage: C=Curve([x-y,2-z])
sage: print C
Affine Space Curve over Rational Field defined by x - y
sage: print C.defining_ideal()
Ideal (x - y, -z + 2) of Multivariate Polynomial Ring in x, y, z over Rational Field
```


Issue created by migration from https://trac.sagemath.org/ticket/7953





---

archive/issue_comments_069394.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-16T23:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7953#issuecomment-69394",
    "user": "wjp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069395.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-17T03:50:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7953#issuecomment-69395",
    "user": "wjp"
}
```

Attachment



---

archive/issue_comments_069396.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T22:39:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7953#issuecomment-69396",
    "user": "AlexGhitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069397.json:
```json
{
    "body": "Looks good.  Thanks, Willem and Ronald!",
    "created_at": "2010-01-17T22:39:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7953#issuecomment-69397",
    "user": "AlexGhitza"
}
```

Looks good.  Thanks, Willem and Ronald!



---

archive/issue_comments_069398.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-18T01:36:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7953#issuecomment-69398",
    "user": "wjp"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_069399.json:
```json
{
    "body": "After discussing with William (see also #7954), I'll move the non-plane curve code out of the plane_curves directory first, and rebase this patch on top of that afterwards.",
    "created_at": "2010-01-18T01:36:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7953#issuecomment-69399",
    "user": "wjp"
}
```

After discussing with William (see also #7954), I'll move the non-plane curve code out of the plane_curves directory first, and rebase this patch on top of that afterwards.



---

archive/issue_comments_069400.json:
```json
{
    "body": "TABs replaced with spaces",
    "created_at": "2010-10-23T21:56:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7953#issuecomment-69400",
    "user": "novoselt"
}
```

TABs replaced with spaces



---

archive/issue_comments_069401.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-10-23T21:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7953#issuecomment-69401",
    "user": "novoselt"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_069402.json:
```json
{
    "body": "Attachment\n\nI'll take the liberty to switch this patch back to positive review, since it does solve the problem described in the ticket (which is bad - Sage gives wrong answers) and there was no work done in a \"better direction\" for 9 month neither here nor on #7954.\n\nThe original patch uses TABs, so I changed them to spaces leaving the rest the same. Applies cleanly and passes all tests on sage-4.6.rc0.",
    "created_at": "2010-10-23T21:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7953#issuecomment-69402",
    "user": "novoselt"
}
```

Attachment

I'll take the liberty to switch this patch back to positive review, since it does solve the problem described in the ticket (which is bad - Sage gives wrong answers) and there was no work done in a "better direction" for 9 month neither here nor on #7954.

The original patch uses TABs, so I changed them to spaces leaving the rest the same. Applies cleanly and passes all tests on sage-4.6.rc0.



---

archive/issue_comments_069403.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-01T10:05:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7953#issuecomment-69403",
    "user": "jdemeyer"
}
```

Resolution: fixed
