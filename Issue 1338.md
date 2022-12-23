# Issue 1338: Symmetrica crashes on big-endian machines

archive/issues_001338.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\nIt seems that symmetrica doesn't do too well on big endian machines. On Sparc as well as PPC under Linux the sfa doctest segfaults or shows bad things happening under valgrind. Mike Hanson said that there will be a new upstream version of symmetrica soon, so let's see if those fix the issue.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1338\n\n",
    "created_at": "2007-11-29T09:53:13Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "Symmetrica crashes on big-endian machines",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1338",
    "user": "mabshoff"
}
```
Assignee: mhansen

CC:  sage-combinat

It seems that symmetrica doesn't do too well on big endian machines. On Sparc as well as PPC under Linux the sfa doctest segfaults or shows bad things happening under valgrind. Mike Hanson said that there will be a new upstream version of symmetrica soon, so let's see if those fix the issue.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1338





---

archive/issue_comments_008573.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-08T03:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8573",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008574.json:
```json
{
    "body": "I think this might have been fixed with the upgrade to symmetrica-2.0?  See #1417 .",
    "created_at": "2007-12-08T03:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8574",
    "user": "mhansen"
}
```

I think this might have been fixed with the upgrade to symmetrica-2.0?  See #1417 .



---

archive/issue_comments_008575.json:
```json
{
    "body": "This bug is not invalid, since it is probably fixed by #1417. But only when we can confirm that we will close the bug as fixed.\n\nWe do not invalidate bugs because they were fixed by another ticket.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-09T09:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8575",
    "user": "mabshoff"
}
```

This bug is not invalid, since it is probably fixed by #1417. But only when we can confirm that we will close the bug as fixed.

We do not invalidate bugs because they were fixed by another ticket.

Cheers,

Michael



---

archive/issue_comments_008576.json:
```json
{
    "body": "The new symmetrica does not fix the issue and it still dumps core during various doctests. While something else might still be involved (libSingular) the ticket should remain open until we sort this all out.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-15T23:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8576",
    "user": "mabshoff"
}
```

The new symmetrica does not fix the issue and it still dumps core during various doctests. While something else might still be involved (libSingular) the ticket should remain open until we sort this all out.

Cheers,

Michael



---

archive/issue_comments_008577.json:
```json
{
    "body": "Unfortunately this is still an issue :(\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T15:32:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8577",
    "user": "mabshoff"
}
```

Unfortunately this is still an issue :(

Cheers,

Michael



---

archive/issue_comments_008578.json:
```json
{
    "body": "The spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/alpha0/symmetrica-2.0.p3.spkg\n\nThe patch posted makes the symmetrica extension depends on def.h, so it gets rebuild when symmetrica is being updated.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-15T11:37:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8578",
    "user": "mabshoff"
}
```

The spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/alpha0/symmetrica-2.0.p3.spkg

The patch posted makes the symmetrica extension depends on def.h, so it gets rebuild when symmetrica is being updated.

Cheers,

Michael



---

archive/issue_comments_008579.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-05-15T11:41:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8579",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_008580.json:
```json
{
    "body": "Reassigned to 4.0.\n\nAnd this is my ticket now :)\n\nCheers,\n\nMichael",
    "created_at": "2009-05-15T11:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8580",
    "user": "mabshoff"
}
```

Reassigned to 4.0.

And this is my ticket now :)

Cheers,

Michael



---

archive/issue_comments_008581.json:
```json
{
    "body": "Changing assignee from mhansen to mabshoff.",
    "created_at": "2009-05-15T11:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8581",
    "user": "mabshoff"
}
```

Changing assignee from mhansen to mabshoff.



---

archive/issue_comments_008582.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2009-05-15T11:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8582",
    "user": "mabshoff"
}
```

Changing status from assigned to new.



---

archive/issue_comments_008583.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-15T11:41:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8583",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008584.json:
```json
{
    "body": "New spkg here with some trivial referee typo fixes:\n\nhttp://sage.math.washington.edu/home/wstein/patches/symmetrica-2.0.p4.spkg",
    "created_at": "2009-05-15T12:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8584",
    "user": "was"
}
```

New spkg here with some trivial referee typo fixes:

http://sage.math.washington.edu/home/wstein/patches/symmetrica-2.0.p4.spkg



---

archive/issue_comments_008585.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-15T14:22:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8585",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_008586.json:
```json
{
    "body": "Merged spkg and patch into Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-15T14:22:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1338#issuecomment-8586",
    "user": "mabshoff"
}
```

Merged spkg and patch into Sage 4.0.alpha0.

Cheers,

Michael
