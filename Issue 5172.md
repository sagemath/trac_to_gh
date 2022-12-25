# Issue 5172: Sage 3.3.a5: more numerical noise in sage/calculus/calculus.py

archive/issues_005172.json:
```json
{
    "body": "Assignee: mabshoff\n\nSee on cicero:\n\n```\nsage -t -long \"devel/sage/sage/calculus/calculus.py\"        \n**********************************************************************\nFile \"/home/mabshoff/build-3.3.alpha5/sage-3.3.alpha5-cicero/devel/sage/sage/calculus/calculus.py\", line 3206:\n    sage: f.roots(ring=CC)\nExpected:\n    [(-0.0588115223184495, 1), (-1.331099917875... - 1.52241655183732*I, 1), (-1.33109991787579 + 1.52241655183732*I, 1), (1.36050567903502 - 1.51880872209965*I, 1), (1.36050567903502 + 1.51880872209965*I, 1)]\nGot:\n    [(-0.0588115223184495, 1), (-1.33109991787580 - 1.52241655183732*I, 1), (-1.33109991787580 + 1.52241655183732*I, 1), (1.36050567903502 - 1.51880872209965*I, 1), (1.36050567903502 + 1.51880872209965*I, 1)]\n**********************************************************************\nFile \"/home/mabshoff/build-3.3.alpha5/sage-3.3.alpha5-cicero/devel/sage/sage/calculus/calculus.py\", line 3210:\n    sage: f.roots(ring=CC, multiplicities=False)\nExpected:\n    [-0.0588115223184495, -1.331099917875... - 1.52241655183732*I, -1.33109991787579 + 1.52241655183732*I, 1.36050567903502 - 1.51880872209965*I, 1.36050567903502 + 1.51880872209965*I]\nGot:\n    [-0.0588115223184495, -1.33109991787580 - 1.52241655183732*I, -1.33109991787580 + 1.52241655183732*I, 1.36050567903502 - 1.51880872209965*I, 1.36050567903502 + 1.51880872209965*I]\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5172\n\n",
    "created_at": "2009-02-04T14:09:25Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Sage 3.3.a5: more numerical noise in sage/calculus/calculus.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5172",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

See on cicero:

```
sage -t -long "devel/sage/sage/calculus/calculus.py"        
**********************************************************************
File "/home/mabshoff/build-3.3.alpha5/sage-3.3.alpha5-cicero/devel/sage/sage/calculus/calculus.py", line 3206:
    sage: f.roots(ring=CC)
Expected:
    [(-0.0588115223184495, 1), (-1.331099917875... - 1.52241655183732*I, 1), (-1.33109991787579 + 1.52241655183732*I, 1), (1.36050567903502 - 1.51880872209965*I, 1), (1.36050567903502 + 1.51880872209965*I, 1)]
Got:
    [(-0.0588115223184495, 1), (-1.33109991787580 - 1.52241655183732*I, 1), (-1.33109991787580 + 1.52241655183732*I, 1), (1.36050567903502 - 1.51880872209965*I, 1), (1.36050567903502 + 1.51880872209965*I, 1)]
**********************************************************************
File "/home/mabshoff/build-3.3.alpha5/sage-3.3.alpha5-cicero/devel/sage/sage/calculus/calculus.py", line 3210:
    sage: f.roots(ring=CC, multiplicities=False)
Expected:
    [-0.0588115223184495, -1.331099917875... - 1.52241655183732*I, -1.33109991787579 + 1.52241655183732*I, 1.36050567903502 - 1.51880872209965*I, 1.36050567903502 + 1.51880872209965*I]
Got:
    [-0.0588115223184495, -1.33109991787580 - 1.52241655183732*I, -1.33109991787580 + 1.52241655183732*I, 1.36050567903502 - 1.51880872209965*I, 1.36050567903502 + 1.51880872209965*I]
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/5172





---

archive/issue_comments_039549.json:
```json
{
    "body": "Attachment [trac_5172.patch](tarball://root/attachments/some-uuid/ticket5172/trac_5172.patch) by mabshoff created at 2009-02-05 13:24:07",
    "created_at": "2009-02-05T13:24:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5172#issuecomment-39549",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5172.patch](tarball://root/attachments/some-uuid/ticket5172/trac_5172.patch) by mabshoff created at 2009-02-05 13:24:07



---

archive/issue_comments_039550.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-05T13:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5172#issuecomment-39550",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039551.json:
```json
{
    "body": "After applying the patch:\n\n\n```\nsage -t  \"devel/sage/sage/calculus/calculus.py\"             \n\t [276.2 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 276.2 seconds\n[jaap@paix sage-3.3.alpha4]$ \n\n```\n\n\nWorks for me on Fedora 9, 32 bits\n\nJaap",
    "created_at": "2009-02-05T15:01:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5172#issuecomment-39551",
    "user": "https://github.com/jaapspies"
}
```

After applying the patch:


```
sage -t  "devel/sage/sage/calculus/calculus.py"             
	 [276.2 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 276.2 seconds
[jaap@paix sage-3.3.alpha4]$ 

```


Works for me on Fedora 9, 32 bits

Jaap



---

archive/issue_comments_039552.json:
```json
{
    "body": "Merged in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-05T23:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5172#issuecomment-39552",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha6.

Cheers,

Michael



---

archive/issue_comments_039553.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-05T23:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5172#issuecomment-39553",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_011969.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-05T23:40:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5172",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5172#event-11969"
}
```
