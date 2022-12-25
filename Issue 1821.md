# Issue 1821: Update FLINT to 1.0.6

archive/issues_001821.json:
```json
{
    "body": "Assignee: mabshoff\n\n```\nFLINT 1.0.6 fixes the issue on the teragrid machine. It's just a\nworkaround. I've no idea what was really wrong. It might be that when\nthey implemented the builtin they forgot about arithmetic shift\nissues. At any rate it seems to be broken only when you ask for the\nnumber of bits of 0. The patch just treats this as a special case. The\ntests now pass on that machine, and still pass on sage.math.\n\nAt first I thought it had to do with the fact that the builtin returns\nan int, which is 32 bits, whilst a long is 64 bits. But I was unable\nto fix it under this assumption.\n\nhttp://www.flintlib.org/\n\nBill.\n```\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1821\n\n",
    "created_at": "2008-01-18T01:04:04Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "Update FLINT to 1.0.6",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1821",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

```
FLINT 1.0.6 fixes the issue on the teragrid machine. It's just a
workaround. I've no idea what was really wrong. It might be that when
they implemented the builtin they forgot about arithmetic shift
issues. At any rate it seems to be broken only when you ask for the
number of bits of 0. The patch just treats this as a special case. The
tests now pass on that machine, and still pass on sage.math.

At first I thought it had to do with the fact that the builtin returns
an int, which is 32 bits, whilst a long is 64 bits. But I was unable
to fix it under this assumption.

http://www.flintlib.org/

Bill.
```

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1821





---

archive/issue_comments_011493.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-18T01:04:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1821#issuecomment-11493",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011494.json:
```json
{
    "body": "The updated spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha0/flint-1.06.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-01-19T18:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1821#issuecomment-11494",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha0/flint-1.06.spkg

Cheers,

Michael



---

archive/issue_comments_011495.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-19T19:52:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1821#issuecomment-11495",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004430.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-19T19:52:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1821",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1821#event-4430"
}
```



---

archive/issue_comments_011496.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha0",
    "created_at": "2008-01-19T19:52:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1821#issuecomment-11496",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha0
