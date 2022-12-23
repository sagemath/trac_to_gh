# Issue 2049: symbolic matrix exp (easy to implement)

archive/issues_002049.json:
```json
{
    "body": "Assignee: was\n\n\n```\n\n> On a related issue: is there a command corresponding to Mathematica's\n> MatrixExp? For example,\n> \n> sage: var('t')\n> sage: M=matrix(SR,2,[0,t,-t,0])\n> sage: M.matrix_exp()\n> \n> [cos(t), sin(t)]\n> [-sin(t), cos(t)]\n> \n\nThere is no such command in Sage, really.  Maxima\ndoes have such a command, so it would be\npossible to implement something easily:\n\nsage: t = var('t')\nsage: M = matrix(SR,2,[0,t,-t,0])\nsage: mm = maxima(M)\nsage: mm.matrixexp()\nmatrix([%e^-(%i*t)*(%e^(2*%i*t)+1)/2,-%e^-(%i*t)*(%i*%e^(2*%i*t)-%i)/2],[%e^-(%i*t)*(%i*%e^(2*%i*t)-%i)/2,%e^-(%i*t)*(%e^(2*%i*t)+1)/2])\n\nSo there will be an M.exp() function in some future version\nof Sage. \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2049\n\n",
    "created_at": "2008-02-05T04:55:07Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "title": "symbolic matrix exp (easy to implement)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2049",
    "user": "was"
}
```
Assignee: was


```

> On a related issue: is there a command corresponding to Mathematica's
> MatrixExp? For example,
> 
> sage: var('t')
> sage: M=matrix(SR,2,[0,t,-t,0])
> sage: M.matrix_exp()
> 
> [cos(t), sin(t)]
> [-sin(t), cos(t)]
> 

There is no such command in Sage, really.  Maxima
does have such a command, so it would be
possible to implement something easily:

sage: t = var('t')
sage: M = matrix(SR,2,[0,t,-t,0])
sage: mm = maxima(M)
sage: mm.matrixexp()
matrix([%e^-(%i*t)*(%e^(2*%i*t)+1)/2,-%e^-(%i*t)*(%i*%e^(2*%i*t)-%i)/2],[%e^-(%i*t)*(%i*%e^(2*%i*t)-%i)/2,%e^-(%i*t)*(%e^(2*%i*t)+1)/2])

So there will be an M.exp() function in some future version
of Sage. 
```


Issue created by migration from https://trac.sagemath.org/ticket/2049





---

archive/issue_comments_013270.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-05T05:15:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2049#issuecomment-13270",
    "user": "was"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013271.json:
```json
{
    "body": "Attachment\n\nThis patch has already been merged (checked in 2.10.2.rc0).",
    "created_at": "2008-02-23T01:23:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2049#issuecomment-13271",
    "user": "AlexGhitza"
}
```

Attachment

This patch has already been merged (checked in 2.10.2.rc0).



---

archive/issue_comments_013272.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-23T01:23:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2049#issuecomment-13272",
    "user": "AlexGhitza"
}
```

Resolution: fixed



---

archive/issue_comments_013273.json:
```json
{
    "body": "This one snuck in via one of the bundles from #174 or #2190. Bundles are bad.\n\nIt would be nice if anybody could give this a proper review, despite the fact that it already is in 2.10.2.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-23T01:27:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2049#issuecomment-13273",
    "user": "mabshoff"
}
```

This one snuck in via one of the bundles from #174 or #2190. Bundles are bad.

It would be nice if anybody could give this a proper review, despite the fact that it already is in 2.10.2.

Cheers,

Michael



---

archive/issue_comments_013274.json:
```json
{
    "body": "Oh, yes, I looked at it, thought it looked good, tried to import the patch and got a bunch of rejects, noticed that it had already been merged.\n\nConclusion: it's good, should be applied, and was applied.",
    "created_at": "2008-02-23T01:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2049#issuecomment-13274",
    "user": "AlexGhitza"
}
```

Oh, yes, I looked at it, thought it looked good, tried to import the patch and got a bunch of rejects, noticed that it had already been merged.

Conclusion: it's good, should be applied, and was applied.
