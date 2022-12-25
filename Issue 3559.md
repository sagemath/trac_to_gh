# Issue 3559: [with patch; needs review] sage timeup script

archive/issues_003559.json:
```json
{
    "body": "Assignee: tbd\n\nCredit goes to Andrew Dalke, Mike Hansen, and William Stein (a little)\n\nIssue created by migration from https://trac.sagemath.org/ticket/3559\n\n",
    "created_at": "2008-07-06T08:20:37Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch; needs review] sage timeup script",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3559",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

Credit goes to Andrew Dalke, Mike Hansen, and William Stein (a little)

Issue created by migration from https://trac.sagemath.org/ticket/3559





---

archive/issue_comments_025105.json:
```json
{
    "body": "Attachment [scripts-3559.patch](tarball://root/attachments/some-uuid/ticket3559/scripts-3559.patch) by @williamstein created at 2008-07-06 08:21:14",
    "created_at": "2008-07-06T08:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3559#issuecomment-25105",
    "user": "https://github.com/williamstein"
}
```

Attachment [scripts-3559.patch](tarball://root/attachments/some-uuid/ticket3559/scripts-3559.patch) by @williamstein created at 2008-07-06 08:21:14



---

archive/issue_comments_025106.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mhansen\".",
    "created_at": "2008-07-06T10:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3559#issuecomment-25106",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing keywords from "" to "editor_mhansen".



---

archive/issue_comments_025107.json:
```json
{
    "body": "Since Mike is getting the author's permission so we can include this I am making him editor. Feel free to decline :)\n\nCheers,\n\nMichael",
    "created_at": "2008-07-06T10:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3559#issuecomment-25107",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Since Mike is getting the author's permission so we can include this I am making him editor. Feel free to decline :)

Cheers,

Michael



---

archive/issue_comments_025108.json:
```json
{
    "body": "\n```\n    I was wondering if you'd be\n    willing to release your code under a GPL compatible license so that we\n    can include it with Sage to do regression testing with every release.\n\n\nCertainly.\n\nIf you believe that\n\n This work written by Andrew Dalke and released into the public domain\n in 2008.  No copyright protection is asserted.\n\nis sufficient then there you go.  Else\n\n Copyright Andrew Dalke, 2008. This software is provided 'as-is', without\n any express or implied warranty. In no event will the author be held\n liable for any damages arising from the use of this software.\n\n Permission is granted to anyone to use this software for any purpose,\n including commercial applications, and to alter it and redistribute it\n freely, subject to no restriction.\n\nI honestly think that the code needs enough modifications to be usable in SAGE or another tool that nothing of my code will remain.\n\nNow if had access to the code I wrote for a client, that would be much cooler.  It saved the imports to a format that kcachegrind could visualize.  :)\n\nCheers,\n\n\n                               Andrew\n                               dalke@dalkescientific.com\n```\n",
    "created_at": "2008-07-06T17:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3559#issuecomment-25108",
    "user": "https://github.com/mwhansen"
}
```


```
    I was wondering if you'd be
    willing to release your code under a GPL compatible license so that we
    can include it with Sage to do regression testing with every release.


Certainly.

If you believe that

 This work written by Andrew Dalke and released into the public domain
 in 2008.  No copyright protection is asserted.

is sufficient then there you go.  Else

 Copyright Andrew Dalke, 2008. This software is provided 'as-is', without
 any express or implied warranty. In no event will the author be held
 liable for any damages arising from the use of this software.

 Permission is granted to anyone to use this software for any purpose,
 including commercial applications, and to alter it and redistribute it
 freely, subject to no restriction.

I honestly think that the code needs enough modifications to be usable in SAGE or another tool that nothing of my code will remain.

Now if had access to the code I wrote for a client, that would be much cooler.  It saved the imports to a format that kcachegrind could visualize.  :)

Cheers,


                               Andrew
                               dalke@dalkescientific.com
```




---

archive/issue_comments_025109.json:
```json
{
    "body": "Attachment [scripts-3559-part2.patch](tarball://root/attachments/some-uuid/ticket3559/scripts-3559-part2.patch) by @williamstein created at 2008-07-06 17:15:51",
    "created_at": "2008-07-06T17:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3559#issuecomment-25109",
    "user": "https://github.com/williamstein"
}
```

Attachment [scripts-3559-part2.patch](tarball://root/attachments/some-uuid/ticket3559/scripts-3559-part2.patch) by @williamstein created at 2008-07-06 17:15:51



---

archive/issue_comments_025110.json:
```json
{
    "body": "Positive review. I think this is a nice start and will greatly help to keep the import time down.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-06T17:18:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3559#issuecomment-25110",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review. I think this is a nice start and will greatly help to keep the import time down.

Cheers,

Michael



---

archive/issue_comments_025111.json:
```json
{
    "body": "Merged both patches in Sage 3.0.4.alpha2",
    "created_at": "2008-07-06T18:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3559#issuecomment-25111",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.0.4.alpha2



---

archive/issue_comments_025112.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-06T18:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3559#issuecomment-25112",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003777.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-07-06T18:11:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3559",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3559#event-3777"
}
```
