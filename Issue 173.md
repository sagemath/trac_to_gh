# Issue 173: mathematica raises matrices / QQ to large powers much more quickly than SAGE

archive/issues_000173.json:
```json
{
    "body": "Assignee: somebody\n\nIf you make a messy 3x3 matrix over QQ and raise it to a large power\nin SAGE it is WAY faster in Mathematica. \n\n\n\n```\nsage: time m = matrix(QQ,3,range(9)); m[0,0] =20; n=m^(-1)\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.05\nsage: time k=n^20000\nCPU times: user 0.56 s, sys: 0.00 s, total: 0.56 s\nWall time: 0.57\nsage: nm = magma(n)\nsage: time l=nm^20000\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.40\nsage: nm = mathematica(n)\nsage: time a=nm^20000\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.03\n```\n\n\nSAGE should do whatever mathematica is doing...\n\nIssue created by migration from https://trac.sagemath.org/ticket/173\n\n",
    "created_at": "2006-12-01T01:08:37Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "mathematica raises matrices / QQ to large powers much more quickly than SAGE",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/173",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

If you make a messy 3x3 matrix over QQ and raise it to a large power
in SAGE it is WAY faster in Mathematica. 



```
sage: time m = matrix(QQ,3,range(9)); m[0,0] =20; n=m^(-1)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.05
sage: time k=n^20000
CPU times: user 0.56 s, sys: 0.00 s, total: 0.56 s
Wall time: 0.57
sage: nm = magma(n)
sage: time l=nm^20000
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.40
sage: nm = mathematica(n)
sage: time a=nm^20000
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.03
```


SAGE should do whatever mathematica is doing...

Issue created by migration from https://trac.sagemath.org/ticket/173





---

archive/issue_comments_000790.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2006-12-01T01:08:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/173#issuecomment-790",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to minor.



---

archive/issue_events_000320.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-11T02:14:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/173",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/173#event-320"
}
```



---

archive/issue_events_000321.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-12-03T18:35:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/173",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/173#event-321"
}
```



---

archive/issue_comments_000791.json:
```json
{
    "body": "It turns out that this is invalid.  I was misusing Mathematica.  See\nthis thread\n\n http://groups.google.com/group/sage-devel/browse_thread/thread/27d0cde4628cac48",
    "created_at": "2007-12-03T18:35:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/173#issuecomment-791",
    "user": "https://github.com/williamstein"
}
```

It turns out that this is invalid.  I was misusing Mathematica.  See
this thread

 http://groups.google.com/group/sage-devel/browse_thread/thread/27d0cde4628cac48



---

archive/issue_comments_000792.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-12-03T18:35:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/173#issuecomment-792",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid



---

archive/issue_comments_000793.json:
```json
{
    "body": "\n```\n\"The computer allows you to make mistakes faster than any other invention, with the possible exception of handguns and tequila.\"\n```\n",
    "created_at": "2007-12-03T19:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/173#issuecomment-793",
    "user": "https://github.com/williamstein"
}
```


```
"The computer allows you to make mistakes faster than any other invention, with the possible exception of handguns and tequila."
```




---

archive/issue_events_000322.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-12-03T19:04:55Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/173",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/173#event-322"
}
```



---

archive/issue_events_000323.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-12-03T19:04:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/173",
    "milestone": "sage-2.8.15",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/173#event-323"
}
```



---

archive/issue_comments_000794.json:
```json
{
    "body": "\"The computer allows you to make mistakes faster than any other invention, with the possible exception of handguns and tequila.\"",
    "created_at": "2007-12-03T19:05:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/173#issuecomment-794",
    "user": "https://github.com/williamstein"
}
```

"The computer allows you to make mistakes faster than any other invention, with the possible exception of handguns and tequila."
