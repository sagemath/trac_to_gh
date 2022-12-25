# Issue 1338: [with spkg, positive review] Solaris: Symmetrica 2.0 crashes due to linker issues

archive/issues_001338.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  sage-combinat\n\nIt seems that symmetrica doesn't do too well on big endian machines. On Sparc as well as PPC under Linux the sfa doctest segfaults or shows bad things happening under valgrind. Mike Hanson said that there will be a new upstream version of symmetrica soon, so let's see if those fix the issue.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1338\n\n",
    "closed_at": "2009-05-15T14:22:05Z",
    "created_at": "2007-11-29T09:53:13Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with spkg, positive review] Solaris: Symmetrica 2.0 crashes due to linker issues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1338",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  sage-combinat

It seems that symmetrica doesn't do too well on big endian machines. On Sparc as well as PPC under Linux the sfa doctest segfaults or shows bad things happening under valgrind. Mike Hanson said that there will be a new upstream version of symmetrica soon, so let's see if those fix the issue.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1338





---

archive/issue_events_003474.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2007-12-08T03:29:04Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1338#event-3474"
}
```



---

archive/issue_comments_008549.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-08T03:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8549",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008550.json:
```json
{
    "body": "I think this might have been fixed with the upgrade to symmetrica-2.0?  See #1417 .",
    "created_at": "2007-12-08T03:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8550",
    "user": "https://github.com/mwhansen"
}
```

I think this might have been fixed with the upgrade to symmetrica-2.0?  See #1417 .



---

archive/issue_comments_008551.json:
```json
{
    "body": "This bug is not invalid, since it is probably fixed by #1417. But only when we can confirm that we will close the bug as fixed.\n\nWe do not invalidate bugs because they were fixed by another ticket.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-09T09:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8551",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This bug is not invalid, since it is probably fixed by #1417. But only when we can confirm that we will close the bug as fixed.

We do not invalidate bugs because they were fixed by another ticket.

Cheers,

Michael



---

archive/issue_comments_008552.json:
```json
{
    "body": "The new symmetrica does not fix the issue and it still dumps core during various doctests. While something else might still be involved (libSingular) the ticket should remain open until we sort this all out.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-15T23:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8552",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The new symmetrica does not fix the issue and it still dumps core during various doctests. While something else might still be involved (libSingular) the ticket should remain open until we sort this all out.

Cheers,

Michael



---

archive/issue_comments_008553.json:
```json
{
    "body": "Unfortunately this is still an issue :(\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T15:32:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8553",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Unfortunately this is still an issue :(

Cheers,

Michael



---

archive/issue_comments_008554.json:
```json
{
    "body": "The spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/alpha0/symmetrica-2.0.p3.spkg\n\nThe patch posted makes the symmetrica extension depends on def.h, so it gets rebuild when symmetrica is being updated.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-15T11:37:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8554",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/alpha0/symmetrica-2.0.p3.spkg

The patch posted makes the symmetrica extension depends on def.h, so it gets rebuild when symmetrica is being updated.

Cheers,

Michael



---

archive/issue_comments_008555.json:
```json
{
    "body": "Attachment [trac_1338.patch](tarball://root/attachments/some-uuid/ticket1338/trac_1338.patch) by mabshoff created at 2009-05-15 11:41:16",
    "created_at": "2009-05-15T11:41:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8555",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_1338.patch](tarball://root/attachments/some-uuid/ticket1338/trac_1338.patch) by mabshoff created at 2009-05-15 11:41:16



---

archive/issue_comments_008556.json:
```json
{
    "body": "Reassigned to 4.0.\n\nAnd this is my ticket now :)\n\nCheers,\n\nMichael",
    "created_at": "2009-05-15T11:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8556",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Reassigned to 4.0.

And this is my ticket now :)

Cheers,

Michael



---

archive/issue_comments_008557.json:
```json
{
    "body": "Changing assignee from @mwhansen to mabshoff.",
    "created_at": "2009-05-15T11:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8557",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @mwhansen to mabshoff.



---

archive/issue_events_003475.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-15T11:41:42Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1338#event-3475"
}
```



---

archive/issue_events_003476.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-15T11:41:42Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1338#event-3476"
}
```



---

archive/issue_comments_008558.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2009-05-15T11:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8558",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from assigned to new.



---

archive/issue_comments_008559.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-15T11:41:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8559",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008560.json:
```json
{
    "body": "New spkg here with some trivial referee typo fixes:\n\nhttp://sage.math.washington.edu/home/wstein/patches/symmetrica-2.0.p4.spkg",
    "created_at": "2009-05-15T12:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8560",
    "user": "https://github.com/williamstein"
}
```

New spkg here with some trivial referee typo fixes:

http://sage.math.washington.edu/home/wstein/patches/symmetrica-2.0.p4.spkg



---

archive/issue_comments_008561.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-15T14:22:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8561",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003477.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-15T14:22:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1338#event-3477"
}
```



---

archive/issue_comments_008562.json:
```json
{
    "body": "Merged spkg and patch into Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-15T14:22:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8562",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged spkg and patch into Sage 4.0.alpha0.

Cheers,

Michael
