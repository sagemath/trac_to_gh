# Issue 1858: plot.py coverage is crap -- get it to 100%

archive/issues_001858.json:
```json
{
    "body": "Assignee: @williamstein\n\nRight now:\n\n```\n$ sage -coverage plot.py\n----------------------------------------------------------------------\nplot.py\nERROR: Please define a s == loads(dumps(s)) doctest.\nSCORE plot.py: 13% (25 of 185)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1858\n\n",
    "created_at": "2008-01-20T00:33:52Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "plot.py coverage is crap -- get it to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1858",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Right now:

```
$ sage -coverage plot.py
----------------------------------------------------------------------
plot.py
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE plot.py: 13% (25 of 185)
```



Issue created by migration from https://trac.sagemath.org/ticket/1858





---

archive/issue_comments_011724.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-20T01:29:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1858#issuecomment-11724",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011725.json:
```json
{
    "body": "after:\n\n```\nteragon:plot was$ sage -coverage plot.py|more\n----------------------------------------------------------------------\nplot.py\nSCORE plot.py: 35% (64 of 180)\n```\n\n\nIt's a start at least.",
    "created_at": "2008-01-20T04:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1858#issuecomment-11725",
    "user": "https://github.com/williamstein"
}
```

after:

```
teragon:plot was$ sage -coverage plot.py|more
----------------------------------------------------------------------
plot.py
SCORE plot.py: 35% (64 of 180)
```


It's a start at least.



---

archive/issue_comments_011726.json:
```json
{
    "body": "Attachment [trac-1858.patch](tarball://root/attachments/some-uuid/ticket1858/trac-1858.patch) by @williamstein created at 2008-01-20 04:49:54",
    "created_at": "2008-01-20T04:49:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1858#issuecomment-11726",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1858.patch](tarball://root/attachments/some-uuid/ticket1858/trac-1858.patch) by @williamstein created at 2008-01-20 04:49:54



---

archive/issue_comments_011727.json:
```json
{
    "body": "The following docstring is probably wrong -- each entry is probably a float between 0 and 1, inclusive.\n\n\n```\n467\t        INPUT: \n468\t            c -- an rgb color 3-tuple, where each tuple entry is an \n469\t                 integer between 0 and 1 \n```\n\n\nBut I think this should be applied.",
    "created_at": "2008-01-20T21:41:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1858#issuecomment-11727",
    "user": "https://github.com/ncalexan"
}
```

The following docstring is probably wrong -- each entry is probably a float between 0 and 1, inclusive.


```
467	        INPUT: 
468	            c -- an rgb color 3-tuple, where each tuple entry is an 
469	                 integer between 0 and 1 
```


But I think this should be applied.



---

archive/issue_comments_011728.json:
```json
{
    "body": "fixes the typo nick pointed out",
    "created_at": "2008-01-20T21:44:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1858#issuecomment-11728",
    "user": "https://github.com/williamstein"
}
```

fixes the typo nick pointed out



---

archive/issue_comments_011729.json:
```json
{
    "body": "Attachment [trac-1858-part2.patch](tarball://root/attachments/some-uuid/ticket1858/trac-1858-part2.patch) by mabshoff created at 2008-01-21 02:12:46\n\nOk, since was fixed the issue this looks good to merge now.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-21T02:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1858#issuecomment-11729",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac-1858-part2.patch](tarball://root/attachments/some-uuid/ticket1858/trac-1858-part2.patch) by mabshoff created at 2008-01-21 02:12:46

Ok, since was fixed the issue this looks good to merge now.

Cheers,

Michael



---

archive/issue_comments_011730.json:
```json
{
    "body": "These two patches seem to depend on at least 1508 to be applied - maybe more.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-21T02:16:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1858#issuecomment-11730",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

These two patches seem to depend on at least 1508 to be applied - maybe more.

Cheers,

Michael



---

archive/issue_comments_011731.json:
```json
{
    "body": "This patch also clashes with #1859, so I applied two hunks manually.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-21T03:52:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1858#issuecomment-11731",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch also clashes with #1859, so I applied two hunks manually.

Cheers,

Michael



---

archive/issue_events_002016.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-01-21T03:52:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1858",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1858#event-2016"
}
```



---

archive/issue_comments_011732.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T03:52:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1858#issuecomment-11732",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011733.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-21T03:52:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1858#issuecomment-11733",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha1
