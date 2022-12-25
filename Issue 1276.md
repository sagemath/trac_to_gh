# Issue 1276: incorporate willem's doctest timing code into sage

archive/issues_001276.json:
```json
{
    "body": "Assignee: failure\n\nCC:  @wjp\n\n\n```\n> Send me your doctest timing code :-)  I'm looking forward to playing with it.\n\nHere you go. It's a patch to local/bin/sage-doctest and a file timing.py\nthat I had put in sage/misc .\n\nIt adds a --time option to sage-doctest that makes it append the timings\nit generates as a dict indexed by hash to the (cpickled) file\n.doctest/timings.sobj .  There's no infrastructure yet to automatically\ndelete that file when appropriate, though.\n\nI also attached two very basic scripts that show or compare the contents\nof timings.sobj files.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1276\n\n",
    "created_at": "2007-11-26T04:18:09Z",
    "labels": [
        "component: doctest coverage"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "incorporate willem's doctest timing code into sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1276",
    "user": "https://github.com/williamstein"
}
```
Assignee: failure

CC:  @wjp


```
> Send me your doctest timing code :-)  I'm looking forward to playing with it.

Here you go. It's a patch to local/bin/sage-doctest and a file timing.py
that I had put in sage/misc .

It adds a --time option to sage-doctest that makes it append the timings
it generates as a dict indexed by hash to the (cpickled) file
.doctest/timings.sobj .  There's no infrastructure yet to automatically
delete that file when appropriate, though.

I also attached two very basic scripts that show or compare the contents
of timings.sobj files.
```


Issue created by migration from https://trac.sagemath.org/ticket/1276





---

archive/issue_comments_007971.json:
```json
{
    "body": "Attachment [recodefordoctesttiming.zip](tarball://root/attachments/some-uuid/ticket1276/recodefordoctesttiming.zip) by @williamstein created at 2007-11-26 04:19:12",
    "created_at": "2007-11-26T04:19:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-7971",
    "user": "https://github.com/williamstein"
}
```

Attachment [recodefordoctesttiming.zip](tarball://root/attachments/some-uuid/ticket1276/recodefordoctesttiming.zip) by @williamstein created at 2007-11-26 04:19:12



---

archive/issue_comments_007972.json:
```json
{
    "body": "Changing assignee from failure to @williamstein.",
    "created_at": "2007-11-26T04:19:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-7972",
    "user": "https://github.com/williamstein"
}
```

Changing assignee from failure to @williamstein.



---

archive/issue_comments_007973.json:
```json
{
    "body": "This ought to get merged.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-29T17:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-7973",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This ought to get merged.

Cheers,

Michael



---

archive/issue_comments_007974.json:
```json
{
    "body": "Changing assignee from @williamstein to @ncalexan.",
    "created_at": "2008-01-20T03:38:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-7974",
    "user": "https://github.com/ncalexan"
}
```

Changing assignee from @williamstein to @ncalexan.



---

archive/issue_comments_007975.json:
```json
{
    "body": "This code looks good, and I'm working in this area so I'll update it and ready it for merging.",
    "created_at": "2008-01-20T03:38:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-7975",
    "user": "https://github.com/ncalexan"
}
```

This code looks good, and I'm working in this area so I'll update it and ready it for merging.



---

archive/issue_comments_007976.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-04-18T20:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-7976",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_007977.json:
```json
{
    "body": "Attachment [trac_1276.patch](tarball://root/attachments/some-uuid/ticket1276/trac_1276.patch) by @garyfurnish created at 2008-05-24 22:42:44\n\nrebased & fixed devel repo patch for this.",
    "created_at": "2008-05-24T22:42:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-7977",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_1276.patch](tarball://root/attachments/some-uuid/ticket1276/trac_1276.patch) by @garyfurnish created at 2008-05-24 22:42:44

rebased & fixed devel repo patch for this.



---

archive/issue_comments_007978.json:
```json
{
    "body": "rebased & fixed scripts repo patch for this.",
    "created_at": "2008-05-24T22:42:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-7978",
    "user": "https://github.com/garyfurnish"
}
```

rebased & fixed scripts repo patch for this.



---

archive/issue_comments_007979.json:
```json
{
    "body": "Attachment [trac_1276_scripts.patch](tarball://root/attachments/some-uuid/ticket1276/trac_1276_scripts.patch) by @garyfurnish created at 2008-05-24 22:45:05",
    "created_at": "2008-05-24T22:45:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-7979",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_1276_scripts.patch](tarball://root/attachments/some-uuid/ticket1276/trac_1276_scripts.patch) by @garyfurnish created at 2008-05-24 22:45:05



---

archive/issue_comments_007980.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-24T22:45:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-7980",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007981.json:
```json
{
    "body": "Changing assignee from @ncalexan to @garyfurnish.",
    "created_at": "2008-05-24T22:45:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-7981",
    "user": "https://github.com/garyfurnish"
}
```

Changing assignee from @ncalexan to @garyfurnish.



---

archive/issue_comments_007982.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mabshoff\".",
    "created_at": "2008-06-15T21:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-7982",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "" to "editor_mabshoff".



---

archive/issue_comments_007983.json:
```json
{
    "body": "I think that ticket #3476 does the actual \"write time info to file\" better than this patch, but the viewing scripts here are useful and should be kept.\n\nI suggest basing this ticket on #3476.",
    "created_at": "2008-08-12T01:11:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-7983",
    "user": "https://github.com/ncalexan"
}
```

I think that ticket #3476 does the actual "write time info to file" better than this patch, but the viewing scripts here are useful and should be kept.

I suggest basing this ticket on #3476.



---

archive/issue_comments_007984.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-09-06T23:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-7984",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: wontfix



---

archive/issue_events_001420.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-09-06T23:14:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1276#event-1420"
}
```



---

archive/issue_comments_007985.json:
```json
{
    "body": "This superseded by #3476, so let's close this. \n\nCheers,\n\nMichael",
    "created_at": "2008-09-06T23:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-7985",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This superseded by #3476, so let's close this. 

Cheers,

Michael
