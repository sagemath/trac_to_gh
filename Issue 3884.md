# Issue 3884: change banner in "sage -advanced"

archive/issues_003884.json:
```json
{
    "body": "Assignee: cwitty\n\nFrom Ralf Hemmecke:\n\n\n```\nwoodpecker:~/scratch/SAGE>./sage -advanced\n-----------------------------------------------------------\n-----------------------------------------------------------\n| SAGE: Software for Algebra and Geometry Experimentation |\nDidn't I hear you saying at ISSAC that SAGE is no longer an abbreviation?\n```\n\n\nIt should be the normal Sage banner. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3884\n\n",
    "created_at": "2008-08-17T19:40:27Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "change banner in \"sage -advanced\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3884",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty

From Ralf Hemmecke:


```
woodpecker:~/scratch/SAGE>./sage -advanced
-----------------------------------------------------------
-----------------------------------------------------------
| SAGE: Software for Algebra and Geometry Experimentation |
Didn't I hear you saying at ISSAC that SAGE is no longer an abbreviation?
```


It should be the normal Sage banner. 

Issue created by migration from https://trac.sagemath.org/ticket/3884





---

archive/issue_comments_027653.json:
```json
{
    "body": "Attachment [trac_3884.patch](tarball://root/attachments/some-uuid/ticket3884/trac_3884.patch) by mabshoff created at 2008-08-22 22:14:26\n\nThis patch changes the banner printed to something very similar at the startup of Sage.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-22T22:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3884#issuecomment-27653",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_3884.patch](tarball://root/attachments/some-uuid/ticket3884/trac_3884.patch) by mabshoff created at 2008-08-22 22:14:26

This patch changes the banner printed to something very similar at the startup of Sage.

Cheers,

Michael



---

archive/issue_comments_027654.json:
```json
{
    "body": "With the patch applied we now get:\n{{\nmabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.1$ ./sage -h\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n Optional arguments:\n<SNIP>\n}}}\n| SAGE Version 3.1.1, Release Date: 2008-08-17                       |\nCheers,\n\nMichael",
    "created_at": "2008-08-22T23:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3884#issuecomment-27654",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With the patch applied we now get:
{{
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.1$ ./sage -h
----------------------------------------------------------------------
----------------------------------------------------------------------
 Optional arguments:
<SNIP>
}}}
| SAGE Version 3.1.1, Release Date: 2008-08-17                       |
Cheers,

Michael



---

archive/issue_comments_027655.json:
```json
{
    "body": "With the patch we now get (better formatting):\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.1$ ./sage -h\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n Optional arguments:\n<SNIP>\n```\n",
    "created_at": "2008-08-22T23:40:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3884#issuecomment-27655",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With the patch we now get (better formatting):

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.1$ ./sage -h
----------------------------------------------------------------------
----------------------------------------------------------------------
 Optional arguments:
<SNIP>
```




---

archive/issue_comments_027656.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha0",
    "created_at": "2008-08-23T00:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3884#issuecomment-27656",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha0



---

archive/issue_events_004109.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-08-23T00:06:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3884",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3884#event-4109"
}
```



---

archive/issue_comments_027657.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-23T00:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3884#issuecomment-27657",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
