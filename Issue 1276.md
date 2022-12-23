# Issue 1276: incorporate willem's doctest timing code into sage

archive/issues_001276.json:
```json
{
    "body": "Assignee: failure\n\nCC:  wjp\n\n\n```\n> Send me your doctest timing code :-)  I'm looking forward to playing with it.\n\nHere you go. It's a patch to local/bin/sage-doctest and a file timing.py\nthat I had put in sage/misc .\n\nIt adds a --time option to sage-doctest that makes it append the timings\nit generates as a dict indexed by hash to the (cpickled) file\n.doctest/timings.sobj .  There's no infrastructure yet to automatically\ndelete that file when appropriate, though.\n\nI also attached two very basic scripts that show or compare the contents\nof timings.sobj files.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1276\n\n",
    "created_at": "2007-11-26T04:18:09Z",
    "labels": [
        "doctest coverage",
        "major",
        "enhancement"
    ],
    "title": "incorporate willem's doctest timing code into sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1276",
    "user": "was"
}
```
Assignee: failure

CC:  wjp


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

archive/issue_comments_007994.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-11-26T04:19:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-7994",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_007995.json:
```json
{
    "body": "Changing assignee from failure to was.",
    "created_at": "2007-11-26T04:19:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-7995",
    "user": "was"
}
```

Changing assignee from failure to was.



---

archive/issue_comments_007996.json:
```json
{
    "body": "This ought to get merged.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-29T17:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-7996",
    "user": "mabshoff"
}
```

This ought to get merged.

Cheers,

Michael



---

archive/issue_comments_007997.json:
```json
{
    "body": "Changing assignee from was to ncalexan.",
    "created_at": "2008-01-20T03:38:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-7997",
    "user": "ncalexan"
}
```

Changing assignee from was to ncalexan.



---

archive/issue_comments_007998.json:
```json
{
    "body": "This code looks good, and I'm working in this area so I'll update it and ready it for merging.",
    "created_at": "2008-01-20T03:38:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-7998",
    "user": "ncalexan"
}
```

This code looks good, and I'm working in this area so I'll update it and ready it for merging.



---

archive/issue_comments_007999.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-04-18T20:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-7999",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_008000.json:
```json
{
    "body": "Attachment\n\nrebased & fixed devel repo patch for this.",
    "created_at": "2008-05-24T22:42:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-8000",
    "user": "gfurnish"
}
```

Attachment

rebased & fixed devel repo patch for this.



---

archive/issue_comments_008001.json:
```json
{
    "body": "rebased & fixed scripts repo patch for this.",
    "created_at": "2008-05-24T22:42:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-8001",
    "user": "gfurnish"
}
```

rebased & fixed scripts repo patch for this.



---

archive/issue_comments_008002.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-05-24T22:45:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-8002",
    "user": "gfurnish"
}
```

Attachment



---

archive/issue_comments_008003.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-24T22:45:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-8003",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008004.json:
```json
{
    "body": "Changing assignee from ncalexan to gfurnish.",
    "created_at": "2008-05-24T22:45:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-8004",
    "user": "gfurnish"
}
```

Changing assignee from ncalexan to gfurnish.



---

archive/issue_comments_008005.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mabshoff\".",
    "created_at": "2008-06-15T21:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-8005",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_mabshoff".



---

archive/issue_comments_008006.json:
```json
{
    "body": "I think that ticket #3476 does the actual \"write time info to file\" better than this patch, but the viewing scripts here are useful and should be kept.\n\nI suggest basing this ticket on #3476.",
    "created_at": "2008-08-12T01:11:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-8006",
    "user": "ncalexan"
}
```

I think that ticket #3476 does the actual "write time info to file" better than this patch, but the viewing scripts here are useful and should be kept.

I suggest basing this ticket on #3476.



---

archive/issue_comments_008007.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-09-06T23:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-8007",
    "user": "mabshoff"
}
```

Resolution: wontfix



---

archive/issue_comments_008008.json:
```json
{
    "body": "This superseded by #3476, so let's close this. \n\nCheers,\n\nMichael",
    "created_at": "2008-09-06T23:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1276#issuecomment-8008",
    "user": "mabshoff"
}
```

This superseded by #3476, so let's close this. 

Cheers,

Michael
