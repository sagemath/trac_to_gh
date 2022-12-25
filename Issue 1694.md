# Issue 1694: Update FLINT to 1.04 release

archive/issues_001694.json:
```json
{
    "body": "Assignee: mabshoff\n\nTo quote Bill Hart:\n\n```\nHi Michael,\n\nI see you are the release manager for the next release of SAGE and\nthat updating spkg's is a priority.\n\nThere are a handful of bug fixes in FLINT 1.0.4 which should probably\nmake their way into SAGE. Some of the fixes repair bugs which affected\ntest code on some 32 bit machines, though the bugs are actually in the\ntest code itself.\n\nThe other bug fixes are in code that doesn't affect SAGE at all, since\nit is not used by SAGE. So this is not an urgent update, but something\nwhich should be done eventually I guess.\n\nBill\n```\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1694\n\n",
    "created_at": "2008-01-05T20:47:42Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "Update FLINT to 1.04 release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1694",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

To quote Bill Hart:

```
Hi Michael,

I see you are the release manager for the next release of SAGE and
that updating spkg's is a priority.

There are a handful of bug fixes in FLINT 1.0.4 which should probably
make their way into SAGE. Some of the fixes repair bugs which affected
test code on some 32 bit machines, though the bugs are actually in the
test code itself.

The other bug fixes are in code that doesn't affect SAGE at all, since
it is not used by SAGE. So this is not an urgent update, but something
which should be done eventually I guess.

Bill
```

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1694





---

archive/issue_comments_010730.json:
```json
{
    "body": "Oops,\n\n```\nHi Michael,\n\nSorry to do this to you, but David Harvey and I just fixed some build\nissues for machines running Darwin and certain versions of gcc. The\nnew release is FLINT 1.0.5\n\nhttp://www.flintlib.org/\n\nIt might save you some troubles down the track as some of these issues\nwould also be a problem for building within SAGE.\n\nBill.\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-01-06T20:25:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1694#issuecomment-10730",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Oops,

```
Hi Michael,

Sorry to do this to you, but David Harvey and I just fixed some build
issues for machines running Darwin and certain versions of gcc. The
new release is FLINT 1.0.5

http://www.flintlib.org/

It might save you some troubles down the track as some of these issues
would also be a problem for building within SAGE.

Bill.
```

Cheers,

Michael



---

archive/issue_comments_010731.json:
```json
{
    "body": "The udpated spkg is at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha0/flint-1.05.spkg\n\nI have turned the mandatory check on for now.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-08T01:28:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1694#issuecomment-10731",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The udpated spkg is at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha0/flint-1.05.spkg

I have turned the mandatory check on for now.

Cheers,

Michael



---

archive/issue_comments_010732.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-08T01:28:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1694#issuecomment-10732",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004147.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-08T01:28:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1694",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1694#event-4147"
}
```
