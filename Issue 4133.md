# Issue 4133: [with spkg, positive review] sage.math - sage 3.1.2.rc4 doctest failure in interfaces/maxima.py

archive/issues_004133.json:
```json
{
    "body": "Assignee: mabshoff\n\n```\n********************************************************************** \nFile \"/home/was/build/sage-3.1.2.rc4/tmp/maxima.py\", line 791: \n    sage: 'gcd' in t \nExpected: \n    True \nGot: \n    False \n********************************************************************** \nFile \"/home/was/build/sage-3.1.2.rc4/tmp/maxima.py\", line 1849: \n    sage: 'gcd' in m.trait_names() \nExpected: \n    True \nGot: \n    False \n********************************************************************** \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4133\n\n",
    "closed_at": "2008-09-17T01:17:59Z",
    "created_at": "2008-09-16T05:26:28Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with spkg, positive review] sage.math - sage 3.1.2.rc4 doctest failure in interfaces/maxima.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4133",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

```
********************************************************************** 
File "/home/was/build/sage-3.1.2.rc4/tmp/maxima.py", line 791: 
    sage: 'gcd' in t 
Expected: 
    True 
Got: 
    False 
********************************************************************** 
File "/home/was/build/sage-3.1.2.rc4/tmp/maxima.py", line 1849: 
    sage: 'gcd' in m.trait_names() 
Expected: 
    True 
Got: 
    False 
********************************************************************** 
```

Issue created by migration from https://trac.sagemath.org/ticket/4133





---

archive/issue_comments_029919.json:
```json
{
    "body": "This is due to a stale maxima_commandlist_cache.sobj in the DOT_SAGE directory.  It was fixed by doing\n\nrm ~/.sage/maxima_commandlist_cache.sobj",
    "created_at": "2008-09-17T00:43:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4133#issuecomment-29919",
    "user": "https://github.com/mwhansen"
}
```

This is due to a stale maxima_commandlist_cache.sobj in the DOT_SAGE directory.  It was fixed by doing

rm ~/.sage/maxima_commandlist_cache.sobj



---

archive/issue_comments_029920.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-17T01:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4133#issuecomment-29920",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_029921.json:
```json
{
    "body": "The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc5/maxima-5.16.2.p0.spkg\n\nfixes the problem.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-17T01:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4133#issuecomment-29921",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc5/maxima-5.16.2.p0.spkg

fixes the problem.

Cheers,

Michael



---

archive/issue_comments_029922.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc5",
    "created_at": "2008-09-17T01:17:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4133#issuecomment-29922",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc5



---

archive/issue_comments_029923.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-17T01:17:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4133#issuecomment-29923",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_009414.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-17T01:17:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4133",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4133#event-9414"
}
```
