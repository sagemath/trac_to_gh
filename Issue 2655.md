# Issue 2655: [with patch, needs review] Cython circular cdef imports

archive/issues_002655.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nCC:  @robertwb\n\nThis patch allows circular cdef imports in Cython.\nIt also modifies cython exceptions to also print the line number in the C code.\nFurthermore the patch begins modifications to seperate module creation from module global execution, which will potentially be useful as Cython starts to employ more optimizations.   \nThis patch is required for the symbolics overhaul.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2655\n\n",
    "created_at": "2008-03-23T16:09:37Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, needs review] Cython circular cdef imports",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2655",
    "user": "https://github.com/garyfurnish"
}
```
Assignee: @garyfurnish

CC:  @robertwb

This patch allows circular cdef imports in Cython.
It also modifies cython exceptions to also print the line number in the C code.
Furthermore the patch begins modifications to seperate module creation from module global execution, which will potentially be useful as Cython starts to employ more optimizations.   
This patch is required for the symbolics overhaul.

Issue created by migration from https://trac.sagemath.org/ticket/2655





---

archive/issue_comments_018225.json:
```json
{
    "body": "Attachment [trac_2655_cython_9612.patch](tarball://root/attachments/some-uuid/ticket2655/trac_2655_cython_9612.patch) by @garyfurnish created at 2008-03-23 16:10:46",
    "created_at": "2008-03-23T16:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2655#issuecomment-18225",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_2655_cython_9612.patch](tarball://root/attachments/some-uuid/ticket2655/trac_2655_cython_9612.patch) by @garyfurnish created at 2008-03-23 16:10:46



---

archive/issue_comments_018226.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-23T16:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2655#issuecomment-18226",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_018227.json:
```json
{
    "body": "Attachment [trac_2655_cython_9612.2.patch](tarball://root/attachments/some-uuid/ticket2655/trac_2655_cython_9612.2.patch) by @garyfurnish created at 2008-03-23 16:15:20\n\nDo not apply 9612.patch, apply 9612.2 patch instead.  It removed several debug printf statements.",
    "created_at": "2008-03-23T16:15:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2655#issuecomment-18227",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_2655_cython_9612.2.patch](tarball://root/attachments/some-uuid/ticket2655/trac_2655_cython_9612.2.patch) by @garyfurnish created at 2008-03-23 16:15:20

Do not apply 9612.patch, apply 9612.2 patch instead.  It removed several debug printf statements.



---

archive/issue_comments_018228.json:
```json
{
    "body": "Attachment [trac_2655_cython_9612.3.patch](tarball://root/attachments/some-uuid/ticket2655/trac_2655_cython_9612.3.patch) by @garyfurnish created at 2008-03-23 16:19:13\n\nNew patch, apply this one *only*.  Removes more commented code.",
    "created_at": "2008-03-23T16:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2655#issuecomment-18228",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_2655_cython_9612.3.patch](tarball://root/attachments/some-uuid/ticket2655/trac_2655_cython_9612.3.patch) by @garyfurnish created at 2008-03-23 16:19:13

New patch, apply this one *only*.  Removes more commented code.



---

archive/issue_comments_018229.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-03-23T18:38:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2655#issuecomment-18229",
    "user": "https://github.com/garyfurnish"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_018230.json:
```json
{
    "body": "Mhh, shouldn't this go to the Cython mailing list?\n\nCheers,\n\nMichael",
    "created_at": "2008-03-23T19:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2655#issuecomment-18230",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Mhh, shouldn't this go to the Cython mailing list?

Cheers,

Michael



---

archive/issue_comments_018231.json:
```json
{
    "body": "I am looking into this, but so far it looks good.",
    "created_at": "2008-03-26T11:19:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2655#issuecomment-18231",
    "user": "https://github.com/robertwb"
}
```

I am looking into this, but so far it looks good.



---

archive/issue_comments_018232.json:
```json
{
    "body": "Could you post some samples here that don't work with Cython now, but do with your patch applied?",
    "created_at": "2008-03-28T06:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2655#issuecomment-18232",
    "user": "https://github.com/williamstein"
}
```

Could you post some samples here that don't work with Cython now, but do with your patch applied?



---

archive/issue_comments_018233.json:
```json
{
    "body": "This wasn't near as scary of a patch as I had first supposed, good work. I merged it into Cython.",
    "created_at": "2008-03-30T11:11:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2655#issuecomment-18233",
    "user": "https://github.com/robertwb"
}
```

This wasn't near as scary of a patch as I had first supposed, good work. I merged it into Cython.



---

archive/issue_comments_018234.json:
```json
{
    "body": "Attachment [trac_2655_cython_9612_4.patch](tarball://root/attachments/some-uuid/ticket2655/trac_2655_cython_9612_4.patch) by @garyfurnish created at 2008-04-04 01:22:33\n\nFix for clear.pyx issue",
    "created_at": "2008-04-04T01:22:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2655#issuecomment-18234",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_2655_cython_9612_4.patch](tarball://root/attachments/some-uuid/ticket2655/trac_2655_cython_9612_4.patch) by @garyfurnish created at 2008-04-04 01:22:33

Fix for clear.pyx issue



---

archive/issue_comments_018235.json:
```json
{
    "body": "Merged upstream.",
    "created_at": "2008-04-04T05:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2655#issuecomment-18235",
    "user": "https://github.com/robertwb"
}
```

Merged upstream.



---

archive/issue_comments_018236.json:
```json
{
    "body": "Fixes doctests for cython 0.9.6.13",
    "created_at": "2008-04-04T19:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2655#issuecomment-18236",
    "user": "https://github.com/garyfurnish"
}
```

Fixes doctests for cython 0.9.6.13



---

archive/issue_comments_018237.json:
```json
{
    "body": "Attachment [trac_2655_devel_1.patch](tarball://root/attachments/some-uuid/ticket2655/trac_2655_devel_1.patch) by @garyfurnish created at 2008-04-04 19:35:09\n\n\n```\nThis has the new repository hierarchy, so you won't be able to pull\nfrom the online -devel ones. If no one reports any bugs in then I\nwill release tomorrow.\n\nhttp://sage.math.washington.edu/home/robertwb/cython/\n\n- Robert\n```\n",
    "created_at": "2008-04-04T19:35:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2655#issuecomment-18237",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_2655_devel_1.patch](tarball://root/attachments/some-uuid/ticket2655/trac_2655_devel_1.patch) by @garyfurnish created at 2008-04-04 19:35:09


```
This has the new repository hierarchy, so you won't be able to pull
from the online -devel ones. If no one reports any bugs in then I
will release tomorrow.

http://sage.math.washington.edu/home/robertwb/cython/

- Robert
```




---

archive/issue_comments_018238.json:
```json
{
    "body": "The spkg at\n\nhttp://sage.math.washington.edu/home/robertwb/cython/cython-0.9.6.13.spkg\n\ncontains a BUILD directory. I removed it and got the size down to about 100kb over 0.9.6.12.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-04T20:28:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2655#issuecomment-18238",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg at

http://sage.math.washington.edu/home/robertwb/cython/cython-0.9.6.13.spkg

contains a BUILD directory. I removed it and got the size down to about 100kb over 0.9.6.12.

Cheers,

Michael



---

archive/issue_comments_018239.json:
```json
{
    "body": "Thanks. This will be removed before the final release.",
    "created_at": "2008-04-04T20:32:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2655#issuecomment-18239",
    "user": "https://github.com/robertwb"
}
```

Thanks. This will be removed before the final release.



---

archive/issue_events_002846.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-04T21:24:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2655",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2655#event-2846"
}
```



---

archive/issue_comments_018240.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-04T21:24:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2655#issuecomment-18240",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018241.json:
```json
{
    "body": "Merged in Sage 3.0.alpha1",
    "created_at": "2008-04-04T21:24:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2655#issuecomment-18241",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha1



---

archive/issue_comments_018242.json:
```json
{
    "body": "Just to confirm, does this mean in the cython-0.9.6.13.spkg from above (minus the build directory) so I needn't make a separate ticket for the new Cython?",
    "created_at": "2008-04-04T22:43:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2655#issuecomment-18242",
    "user": "https://github.com/robertwb"
}
```

Just to confirm, does this mean in the cython-0.9.6.13.spkg from above (minus the build directory) so I needn't make a separate ticket for the new Cython?



---

archive/issue_comments_018243.json:
```json
{
    "body": "Replying to [comment:15 robertwb]:\n> Just to confirm, does this mean in the cython-0.9.6.13.spkg from above (minus the build directory) so I needn't make a separate ticket for the new Cython? \n\nCorrect. The ticket's credit and description reflects this.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-04T22:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2655#issuecomment-18243",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:15 robertwb]:
> Just to confirm, does this mean in the cython-0.9.6.13.spkg from above (minus the build directory) so I needn't make a separate ticket for the new Cython? 

Correct. The ticket's credit and description reflects this.

Cheers,

Michael



---

archive/issue_comments_018244.json:
```json
{
    "body": "The spkg up at \n\nhttp://sage.math.washington.edu/home/robertwb/cython/\n\nturns c line numbers back on, and has a minor fix for external class declarations (which didn't show up in the Sage codebase, but did for other poeple).",
    "created_at": "2008-04-08T08:48:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2655#issuecomment-18244",
    "user": "https://github.com/robertwb"
}
```

The spkg up at 

http://sage.math.washington.edu/home/robertwb/cython/

turns c line numbers back on, and has a minor fix for external class declarations (which didn't show up in the Sage codebase, but did for other poeple).



---

archive/issue_comments_018245.json:
```json
{
    "body": "Hi Robert,\n\nI have merged the latest (April 8th) cython.spkg. I saw the message on the Cython mailing list, so I am not surprised that it did come. But I would recommend opening [or reopening] a ticket and also bumping the version number to p0 to reflect this change.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-08T09:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2655#issuecomment-18245",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Robert,

I have merged the latest (April 8th) cython.spkg. I saw the message on the Cython mailing list, so I am not surprised that it did come. But I would recommend opening [or reopening] a ticket and also bumping the version number to p0 to reflect this change.

Cheers,

Michael
