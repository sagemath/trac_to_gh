# Issue 5167: Sage 3.3.a4 on OSX: doctest failure in sage/calculus/calculus.py due to changed order of roots

archive/issues_005167.json:
```json
{
    "body": "Assignee: mabshoff\n\nNote that this problem is different from #5129, but has also been observed on other platforms:\n\n```\nsage -t -long \"devel/sage/sage/calculus/calculus.py\"        \n**********************************************************************\nFile \"/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/calculus/calculus.py\", line 3206:\n    sage: f.roots(ring=CC)\nExpected:\n    [(-0.0588115223184495, 1), (1.36050567903502 + 1.51880872209965*I, 1), (-1.33109991787579 + 1.52241655183732*I, 1), (1.360505\n67903502 - 1.51880872209965*I, 1), (-1.33109991787580 - 1.52241655183732*I, 1)]\nGot:\n    [(-0.0588115223184495, 1), (-1.33109991787579 + 1.52241655183732*I, 1), (1.36050567903502 + 1.51880872209965*I, 1), (-1.33109\n991787579 - 1.52241655183732*I, 1), (1.36050567903502 - 1.51880872209965*I, 1)]\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/calculus/calculus.py\", line 3210:\n    sage: f.roots(ring=CC, multiplicities=False)\nExpected:\n    [-0.0588115223184495, 1.36050567903502 + 1.51880872209965*I, -1.33109991787579 + 1.52241655183732*I, 1.36050567903502 - 1.518\n80872209965*I, -1.33109991787580 - 1.52241655183732*I]\nGot:\n    [-0.0588115223184495, -1.33109991787579 + 1.52241655183732*I, 1.36050567903502 + 1.51880872209965*I, -1.33109991787579 - 1.52\n241655183732*I, 1.36050567903502 - 1.51880872209965*I]\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/calculus/calculus.py\", line 3214:\n    sage: f.roots(ring=QQbar, multiplicities=False)\nExpected:\n    [-0.05881152231844944?, 1.360505679035020? + 1.518808722099650?*I, -1.331099917875796? + 1.522416551837318?*I, 1.360505679035\n020? - 1.518808722099650?*I, -1.331099917875796? - 1.522416551837318?*I]\nGot:\n    [-0.05881152231844944?, -1.331099917875796? + 1.522416551837318?*I, 1.360505679035020? + 1.518808722099650?*I, -1.33109991787\n5796? - 1.522416551837318?*I, 1.360505679035020? - 1.518808722099650?*I]\n**********************************************************************\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5167\n\n",
    "created_at": "2009-02-03T18:12:12Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Sage 3.3.a4 on OSX: doctest failure in sage/calculus/calculus.py due to changed order of roots",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5167",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Note that this problem is different from #5129, but has also been observed on other platforms:

```
sage -t -long "devel/sage/sage/calculus/calculus.py"        
**********************************************************************
File "/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/calculus/calculus.py", line 3206:
    sage: f.roots(ring=CC)
Expected:
    [(-0.0588115223184495, 1), (1.36050567903502 + 1.51880872209965*I, 1), (-1.33109991787579 + 1.52241655183732*I, 1), (1.360505
67903502 - 1.51880872209965*I, 1), (-1.33109991787580 - 1.52241655183732*I, 1)]
Got:
    [(-0.0588115223184495, 1), (-1.33109991787579 + 1.52241655183732*I, 1), (1.36050567903502 + 1.51880872209965*I, 1), (-1.33109
991787579 - 1.52241655183732*I, 1), (1.36050567903502 - 1.51880872209965*I, 1)]
**********************************************************************
File "/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/calculus/calculus.py", line 3210:
    sage: f.roots(ring=CC, multiplicities=False)
Expected:
    [-0.0588115223184495, 1.36050567903502 + 1.51880872209965*I, -1.33109991787579 + 1.52241655183732*I, 1.36050567903502 - 1.518
80872209965*I, -1.33109991787580 - 1.52241655183732*I]
Got:
    [-0.0588115223184495, -1.33109991787579 + 1.52241655183732*I, 1.36050567903502 + 1.51880872209965*I, -1.33109991787579 - 1.52
241655183732*I, 1.36050567903502 - 1.51880872209965*I]
**********************************************************************
File "/Users/mabshoff/sage-3.3.alpha4/devel/sage/sage/calculus/calculus.py", line 3214:
    sage: f.roots(ring=QQbar, multiplicities=False)
Expected:
    [-0.05881152231844944?, 1.360505679035020? + 1.518808722099650?*I, -1.331099917875796? + 1.522416551837318?*I, 1.360505679035
020? - 1.518808722099650?*I, -1.331099917875796? - 1.522416551837318?*I]
Got:
    [-0.05881152231844944?, -1.331099917875796? + 1.522416551837318?*I, 1.360505679035020? + 1.518808722099650?*I, -1.33109991787
5796? - 1.522416551837318?*I, 1.360505679035020? - 1.518808722099650?*I]
**********************************************************************
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5167





---

archive/issue_comments_039515.json:
```json
{
    "body": "#4544 ought to resolve this issue.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-03T18:34:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5167#issuecomment-39515",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

#4544 ought to resolve this issue.

Cheers,

Michael



---

archive/issue_comments_039516.json:
```json
{
    "body": "Fixed via merging the reviewer patch at #4544.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-03T20:11:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5167#issuecomment-39516",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed via merging the reviewer patch at #4544.

Cheers,

Michael



---

archive/issue_comments_039517.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-03T20:11:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5167#issuecomment-39517",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_011962.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-03T20:11:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5167",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5167#event-11962"
}
```
