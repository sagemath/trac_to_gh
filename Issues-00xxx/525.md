# Issue 525: Get Pete Chvany's build notes into the SAGE docs.

archive/issues_000525.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/525\n\n",
    "closed_at": "2008-09-26T19:08:39Z",
    "created_at": "2007-08-30T03:06:42Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Get Pete Chvany's build notes into the SAGE docs.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/525",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff



Issue created by migration from https://trac.sagemath.org/ticket/525





---

archive/issue_comments_002652.json:
```json
{
    "body": "Attachment [SAGEbuild.rtf](tarball://root/attachments/some-uuid/ticket525/SAGEbuild.rtf) by @williamstein created at 2007-08-30 03:06:58\n\nSAGe build notes",
    "created_at": "2007-08-30T03:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/525#issuecomment-2652",
    "user": "https://github.com/williamstein"
}
```

Attachment [SAGEbuild.rtf](tarball://root/attachments/some-uuid/ticket525/SAGEbuild.rtf) by @williamstein created at 2007-08-30 03:06:58

SAGe build notes



---

archive/issue_comments_002653.json:
```json
{
    "body": "From Section 10:\n\n```\nThe call to bison will probably go away in future versions of SAGE, but at present (version 2.7.3, version 2.8) it is helpful to force install bison as part of preparing the ground for later packages.\n```\nThis issue has been resolved.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-30T10:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/525#issuecomment-2653",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

From Section 10:

```
The call to bison will probably go away in future versions of SAGE, but at present (version 2.7.3, version 2.8) it is helpful to force install bison as part of preparing the ground for later packages.
```
This issue has been resolved.

Cheers,

Michael



---

archive/issue_comments_002654.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-20T06:55:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/525#issuecomment-2654",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002655.json:
```json
{
    "body": "Changing assignee from tba to mabshoff.",
    "created_at": "2008-04-20T06:55:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/525#issuecomment-2655",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from tba to mabshoff.



---

archive/issue_comments_002656.json:
```json
{
    "body": "Is this ticket still relevant? If so, can someone explain its purpose to me? Who is the target audience for the attached document?\n\nFor example, the document says 'These instructions assume a basic level of Unix command-line fluency.' But in this case, how much of this needs to be explained?\n\nFor another example, it seems like a bad idea (items 3 and 4) to delete the old copy of sage, at least not until you're sure that the new one doesn't break things (the way the notebook was somewhat broken for a few releases). If we want instructions like this somewhere (in the installation guide, I suppose), I would not include them as is...",
    "created_at": "2008-09-26T18:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/525#issuecomment-2656",
    "user": "https://github.com/jhpalmieri"
}
```

Is this ticket still relevant? If so, can someone explain its purpose to me? Who is the target audience for the attached document?

For example, the document says 'These instructions assume a basic level of Unix command-line fluency.' But in this case, how much of this needs to be explained?

For another example, it seems like a bad idea (items 3 and 4) to delete the old copy of sage, at least not until you're sure that the new one doesn't break things (the way the notebook was somewhat broken for a few releases). If we want instructions like this somewhere (in the installation guide, I suppose), I would not include them as is...



---

archive/issue_comments_002657.json:
```json
{
    "body": "Replying to [comment:3 jhpalmieri]:\n\nHi John,\n\n> Is this ticket still relevant? If so, can someone explain its purpose to me? Who is the target audience for the attached document?\n\n\nI don't think so.\n\n> For example, the document says 'These instructions assume a basic level of Unix command-line fluency.' But in this case, how much of this needs to be explained?\n> \n> For another example, it seems like a bad idea (items 3 and 4) to delete the old copy of sage, at least not until you're sure that the new one doesn't break things (the way the notebook was somewhat broken for a few releases). If we want instructions like this somewhere (in the installation guide, I suppose), I would not include them as is...\n\n\nThey do suggest outright bad things like building Sage with sudo privileges. It is much, much better to build Sage as a user, -bdist and then move the result into a user accessible location. Another bad thing it to give the sage script an absolute patch since these days the location of a link is automatically resolved.\n\nConsequently: closed as wontfix.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T19:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/525#issuecomment-2657",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:3 jhpalmieri]:

Hi John,

> Is this ticket still relevant? If so, can someone explain its purpose to me? Who is the target audience for the attached document?


I don't think so.

> For example, the document says 'These instructions assume a basic level of Unix command-line fluency.' But in this case, how much of this needs to be explained?
> 
> For another example, it seems like a bad idea (items 3 and 4) to delete the old copy of sage, at least not until you're sure that the new one doesn't break things (the way the notebook was somewhat broken for a few releases). If we want instructions like this somewhere (in the installation guide, I suppose), I would not include them as is...


They do suggest outright bad things like building Sage with sudo privileges. It is much, much better to build Sage as a user, -bdist and then move the result into a user accessible location. Another bad thing it to give the sage script an absolute patch since these days the location of a link is automatically resolved.

Consequently: closed as wontfix.

Cheers,

Michael



---

archive/issue_comments_002658.json:
```json
{
    "body": "wontfix as explained above.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T19:08:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/525#issuecomment-2658",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

wontfix as explained above.

Cheers,

Michael



---

archive/issue_events_001349.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-26T19:08:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/525",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/525#event-1349"
}
```



---

archive/issue_comments_002659.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-09-26T19:08:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/525#issuecomment-2659",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: wontfix
