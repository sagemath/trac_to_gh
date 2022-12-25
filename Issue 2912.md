# Issue 2912: M4RI should be built with -O3

archive/issues_002912.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: speed, build system\n\n* it is fairly straight forward C so it shouldn't break under `-O3`\n* it makes a noticeable speed difference. To echelonise a random 10<sup>4</sup> x 10<sup>4</sup> matrix takes ~ 8 seconds with `-O2` and ~ 6 seconds with `-O3`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2912\n\n",
    "created_at": "2008-04-13T21:05:11Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "M4RI should be built with -O3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2912",
    "user": "https://github.com/malb"
}
```
Assignee: @williamstein

Keywords: speed, build system

* it is fairly straight forward C so it shouldn't break under `-O3`
* it makes a noticeable speed difference. To echelonise a random 10<sup>4</sup> x 10<sup>4</sup> matrix takes ~ 8 seconds with `-O2` and ~ 6 seconds with `-O3`.

Issue created by migration from https://trac.sagemath.org/ticket/2912





---

archive/issue_comments_020019.json:
```json
{
    "body": "New SPKG up at:\n\n   http://sage.math.washington.edu/home/malb/libm4ri-20071224.p2.spkg",
    "created_at": "2008-04-13T21:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2912#issuecomment-20019",
    "user": "https://github.com/malb"
}
```

New SPKG up at:

   http://sage.math.washington.edu/home/malb/libm4ri-20071224.p2.spkg



---

archive/issue_comments_020020.json:
```json
{
    "body": "Spkg looks good to me. Changes are minimal. We still need an SPKG.txt, but that can be done down the road. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-13T23:41:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2912#issuecomment-20020",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Spkg looks good to me. Changes are minimal. We still need an SPKG.txt, but that can be done down the road. Positive review.

Cheers,

Michael



---

archive/issue_events_006671.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-13T23:41:50Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2912",
    "milestone": "sage-3.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2912#event-6671"
}
```



---

archive/issue_comments_020021.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-13T23:42:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2912#issuecomment-20021",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006672.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-13T23:42:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2912",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2912#event-6672"
}
```



---

archive/issue_comments_020022.json:
```json
{
    "body": "Merged in Sage 3.0.alpha5",
    "created_at": "2008-04-13T23:42:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2912#issuecomment-20022",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha5
