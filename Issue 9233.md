# Issue 9233: maxima --> sage conversion error

archive/issues_009233.json:
```json
{
    "body": "Assignee: burcin\n\n\n```\n\nsage: var('n')\nn\nsage: sum((4/(8*n+1)-2/(8*n+4)-1/(8*n+5)-1/(16*n+12)-1/(16*n+14)), n, 0,oo)\n...\n\nTypeError: unable to make sense of Maxima expression '-(22*log(2)-2*psi[0](7/8)-4*psi[0](5/8)+16*psi[0](1/8)-pi+10*euler_gamma)/32' in Sage\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9233\n\n",
    "created_at": "2010-06-13T23:36:31Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "maxima --> sage conversion error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9233",
    "user": "was"
}
```
Assignee: burcin


```

sage: var('n')
n
sage: sum((4/(8*n+1)-2/(8*n+4)-1/(8*n+5)-1/(16*n+12)-1/(16*n+14)), n, 0,oo)
...

TypeError: unable to make sense of Maxima expression '-(22*log(2)-2*psi[0](7/8)-4*psi[0](5/8)+16*psi[0](1/8)-pi+10*euler_gamma)/32' in Sage
```


Issue created by migration from https://trac.sagemath.org/ticket/9233





---

archive/issue_comments_086673.json:
```json
{
    "body": "This is probably a duplicate of #9217.",
    "created_at": "2010-06-13T23:43:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9233#issuecomment-86673",
    "user": "burcin"
}
```

This is probably a duplicate of #9217.



---

archive/issue_comments_086674.json:
```json
{
    "body": "Indeed it is.\n\n\n```\n\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: var('n')\nn\nsage: sum((4/(8*n+1)-2/(8*n+4)-1/(8*n+5)-1/(16*n+12)-1/(16*n+14)), n, 0,oo)\n1/32*pi - 5/16*euler_gamma - 1/2*psi(1/8) + 1/8*psi(5/8) + 1/16*psi(7/8) - 11/16*log(2)\n```\n",
    "created_at": "2010-06-14T00:21:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9233#issuecomment-86674",
    "user": "mhansen"
}
```

Indeed it is.


```

----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: var('n')
n
sage: sum((4/(8*n+1)-2/(8*n+4)-1/(8*n+5)-1/(16*n+12)-1/(16*n+14)), n, 0,oo)
1/32*pi - 5/16*euler_gamma - 1/2*psi(1/8) + 1/8*psi(5/8) + 1/16*psi(7/8) - 11/16*log(2)
```




---

archive/issue_comments_086675.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-06-14T00:21:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9233#issuecomment-86675",
    "user": "mhansen"
}
```

Resolution: duplicate
