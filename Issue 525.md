# Issue 525: Get Pete Chvany's build notes into the SAGE docs.

archive/issues_000525.json:
```json
{
    "body": "Assignee: tba\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/525\n\n",
    "created_at": "2007-08-30T03:06:42Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "Get Pete Chvany's build notes into the SAGE docs.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/525",
    "user": "was"
}
```
Assignee: tba



Issue created by migration from https://trac.sagemath.org/ticket/525





---

archive/issue_comments_002664.json:
```json
{
    "body": "Attachment [SAGEbuild.rtf](tarball://root/attachments/some-uuid/ticket525/SAGEbuild.rtf) by was created at 2007-08-30 03:06:58\n\nSAGe build notes",
    "created_at": "2007-08-30T03:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/525#issuecomment-2664",
    "user": "was"
}
```

Attachment [SAGEbuild.rtf](tarball://root/attachments/some-uuid/ticket525/SAGEbuild.rtf) by was created at 2007-08-30 03:06:58

SAGe build notes



---

archive/issue_comments_002665.json:
```json
{
    "body": "From Section 10:\n\n```\nThe call to bison will probably go away in future versions of SAGE, but at present (version 2.7.3, version 2.8) it is helpful to force install bison as part of preparing the ground for later packages.\n```\n\nThis issue has been resolved.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-30T10:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/525#issuecomment-2665",
    "user": "mabshoff"
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

archive/issue_comments_002666.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-20T06:55:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/525#issuecomment-2666",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002667.json:
```json
{
    "body": "Changing assignee from tba to mabshoff.",
    "created_at": "2008-04-20T06:55:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/525#issuecomment-2667",
    "user": "mabshoff"
}
```

Changing assignee from tba to mabshoff.



---

archive/issue_comments_002668.json:
```json
{
    "body": "Is this ticket still relevant? If so, can someone explain its purpose to me? Who is the target audience for the attached document?\n\nFor example, the document says 'These instructions assume a basic level of Unix command-line fluency.' But in this case, how much of this needs to be explained?\n\nFor another example, it seems like a bad idea (items 3 and 4) to delete the old copy of sage, at least not until you're sure that the new one doesn't break things (the way the notebook was somewhat broken for a few releases). If we want instructions like this somewhere (in the installation guide, I suppose), I would not include them as is...",
    "created_at": "2008-09-26T18:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/525#issuecomment-2668",
    "user": "jhpalmieri"
}
```

Is this ticket still relevant? If so, can someone explain its purpose to me? Who is the target audience for the attached document?

For example, the document says 'These instructions assume a basic level of Unix command-line fluency.' But in this case, how much of this needs to be explained?

For another example, it seems like a bad idea (items 3 and 4) to delete the old copy of sage, at least not until you're sure that the new one doesn't break things (the way the notebook was somewhat broken for a few releases). If we want instructions like this somewhere (in the installation guide, I suppose), I would not include them as is...



---

archive/issue_comments_002669.json:
```json
{
    "body": "Replying to [comment:3 jhpalmieri]:\n\nHi John,\n\n> Is this ticket still relevant? If so, can someone explain its purpose to me? Who is the target audience for the attached document?\n\nI don't think so.\n\n> For example, the document says 'These instructions assume a basic level of Unix command-line fluency.' But in this case, how much of this needs to be explained?\n> \n> For another example, it seems like a bad idea (items 3 and 4) to delete the old copy of sage, at least not until you're sure that the new one doesn't break things (the way the notebook was somewhat broken for a few releases). If we want instructions like this somewhere (in the installation guide, I suppose), I would not include them as is...\n\nThey do suggest outright bad things like building Sage with sudo privileges. It is much, much better to build Sage as a user, -bdist and then move the result into a user accessible location. Another bad thing it to give the sage script an absolute patch since these days the location of a link is automatically resolved.\n\nConsequently: closed as wontfix.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T19:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/525#issuecomment-2669",
    "user": "mabshoff"
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

archive/issue_comments_002670.json:
```json
{
    "body": "wontfix as explained above.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T19:08:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/525#issuecomment-2670",
    "user": "mabshoff"
}
```

wontfix as explained above.

Cheers,

Michael



---

archive/issue_comments_002671.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-09-26T19:08:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/525#issuecomment-2671",
    "user": "mabshoff"
}
```

Resolution: wontfix
