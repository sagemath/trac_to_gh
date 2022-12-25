# Issue 717: sage -t timeout stuff works poorly

archive/issues_000717.json:
```json
{
    "body": "Assignee: failure\n\nIssues:\n1. I can't actually find anywhere in sage-doctest right now where the two alarm codes are actually used, so SAGE should never timeout.  Weird.\n2. It should be easy for users to adjust the timeout, e.g., on slow systems.\n3. \"sage --long\" should automatically have a much longer timeout.\n\nIssue created by migration from https://trac.sagemath.org/ticket/717\n\n",
    "created_at": "2007-09-20T20:07:28Z",
    "labels": [
        "component: doctest coverage"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "sage -t timeout stuff works poorly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/717",
    "user": "https://github.com/williamstein"
}
```
Assignee: failure

Issues:
1. I can't actually find anywhere in sage-doctest right now where the two alarm codes are actually used, so SAGE should never timeout.  Weird.
2. It should be easy for users to adjust the timeout, e.g., on slow systems.
3. "sage --long" should automatically have a much longer timeout.

Issue created by migration from https://trac.sagemath.org/ticket/717





---

archive/issue_comments_004159.json:
```json
{
    "body": "This has annoyed me on regular occasions, so let's fix this.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-04T14:17:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/717#issuecomment-4159",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This has annoyed me on regular occasions, so let's fix this.

Cheers,

Michael



---

archive/issue_comments_004160.json:
```json
{
    "body": "The third part of the ticket, i.e. 'sage --long\" should automatically have a much longer timeout' is  now now #2029.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-02T04:31:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/717#issuecomment-4160",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The third part of the ticket, i.e. 'sage --long" should automatically have a much longer timeout' is  now now #2029.

Cheers,

Michael



---

archive/issue_comments_004161.json:
```json
{
    "body": "FYI, but this is probably orthogonal to the doctesting and more has to do with signal delivery.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-05T05:20:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/717#issuecomment-4161",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

FYI, but this is probably orthogonal to the doctesting and more has to do with signal delivery.

Cheers,

Michael



---

archive/issue_comments_004162.json:
```json
{
    "body": "Attachment [trac_717_bin.patch](tarball://root/attachments/some-uuid/ticket717/trac_717_bin.patch) by @garyfurnish created at 2008-12-05 06:24:56\n\nThis code enables timeouts.",
    "created_at": "2008-12-05T06:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/717#issuecomment-4162",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_717_bin.patch](tarball://root/attachments/some-uuid/ticket717/trac_717_bin.patch) by @garyfurnish created at 2008-12-05 06:24:56

This code enables timeouts.



---

archive/issue_comments_004163.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-05T06:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/717#issuecomment-4163",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_004164.json:
```json
{
    "body": "Changing assignee from failure to @garyfurnish.",
    "created_at": "2008-12-05T06:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/717#issuecomment-4164",
    "user": "https://github.com/garyfurnish"
}
```

Changing assignee from failure to @garyfurnish.



---

archive/issue_comments_004165.json:
```json
{
    "body": "Patch looks with one tiny exception:\n\n```\n[10:25pm] mab|ds9: one suggestions: raise the sleep period to 1 second: time.sleep(.1)\n[10:25pm] gfurnish: feel free to make the modification\n[10:25pm] mab|ds9: I think we can live with that.\n[10:25pm] mab|ds9: mk\n```\n\nI will move item (2) to its own ticket since it is not addressed here.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-05T06:33:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/717#issuecomment-4165",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks with one tiny exception:

```
[10:25pm] mab|ds9: one suggestions: raise the sleep period to 1 second: time.sleep(.1)
[10:25pm] gfurnish: feel free to make the modification
[10:25pm] mab|ds9: I think we can live with that.
[10:25pm] mab|ds9: mk
```

I will move item (2) to its own ticket since it is not addressed here.

Cheers,

Michael



---

archive/issue_comments_004166.json:
```json
{
    "body": "This works very nicely. Positive review. \n\n(2) has been moved to #4712.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-05T07:38:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/717#issuecomment-4166",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This works very nicely. Positive review. 

(2) has been moved to #4712.

Cheers,

Michael



---

archive/issue_events_000796.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-12-05T07:38:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/717",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/717#event-796"
}
```



---

archive/issue_comments_004167.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha0",
    "created_at": "2008-12-05T07:38:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/717#issuecomment-4167",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.2.alpha0



---

archive/issue_comments_004168.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-05T07:38:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/717#issuecomment-4168",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
