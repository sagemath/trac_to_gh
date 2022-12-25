# Issue 3043: The SPKG.txt  of the gfan spkg does not specify license exactly

archive/issues_003043.json:
```json
{
    "body": "Assignee: @malb\n\nThe gfan SPKG.txt says:\n\n## License\n* GPL\n\nit does not say which version of the GPL it is.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3043\n\n",
    "created_at": "2008-04-27T12:58:06Z",
    "labels": [
        "component: commutative algebra",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "The SPKG.txt  of the gfan spkg does not specify license exactly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3043",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```
Assignee: @malb

The gfan SPKG.txt says:

## License
* GPL

it does not say which version of the GPL it is.


Issue created by migration from https://trac.sagemath.org/ticket/3043





---

archive/issue_comments_020911.json:
```json
{
    "body": "Well, the gfan code base is rather sloppy in this regard:\n\n* it never specifies the license other than GPL\n* zero files have a copyright statement in them\n\nSo in conclusion this must be solved upstream by the author. The FSF read on this is if you include a version of the GPL Version X then your software is licensed under GPL Version X+\n\nCheers,\n\nMichael",
    "created_at": "2008-04-29T06:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3043",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3043#issuecomment-20911",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Well, the gfan code base is rather sloppy in this regard:

* it never specifies the license other than GPL
* zero files have a copyright statement in them

So in conclusion this must be solved upstream by the author. The FSF read on this is if you include a version of the GPL Version X then your software is licensed under GPL Version X+

Cheers,

Michael



---

archive/issue_comments_020912.json:
```json
{
    "body": "Remove assignee @malb.",
    "created_at": "2008-06-03T14:16:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3043",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3043#issuecomment-20912",
    "user": "https://github.com/malb"
}
```

Remove assignee @malb.



---

archive/issue_comments_020913.json:
```json
{
    "body": "Both the version of gfan that's currently in Sage (0.3) and the latest version (0.4plus) have a file COPYING which is just the text of GPL version 2.  I would say that's pretty clear, and it should be in the file SPKG.txt.",
    "created_at": "2010-01-02T13:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3043",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3043#issuecomment-20913",
    "user": "https://github.com/aghitza"
}
```

Both the version of gfan that's currently in Sage (0.3) and the latest version (0.4plus) have a file COPYING which is just the text of GPL version 2.  I would say that's pretty clear, and it should be in the file SPKG.txt.



---

archive/issue_comments_020914.json:
```json
{
    "body": "Close as fixed by #7820.",
    "created_at": "2010-01-25T14:13:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3043",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3043#issuecomment-20914",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Close as fixed by #7820.



---

archive/issue_comments_020915.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T14:13:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3043",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3043#issuecomment-20915",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_003250.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-25T14:13:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3043",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3043#event-3250"
}
```
