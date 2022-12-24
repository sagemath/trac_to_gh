# Issue 3429: New linbox 1.1.6 spkg

archive/issues_003429.json:
```json
{
    "body": "Assignee: cpernet\n\nUpgrade linbox to 1.1.6 release.\nThe new release includes the sage interface, so the new spkg should shave out the old linbox_wrap.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3429\n\n",
    "created_at": "2008-06-15T20:13:43Z",
    "labels": [
        "linbox",
        "major",
        "enhancement"
    ],
    "title": "New linbox 1.1.6 spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3429",
    "user": "cpernet"
}
```
Assignee: cpernet

Upgrade linbox to 1.1.6 release.
The new release includes the sage interface, so the new spkg should shave out the old linbox_wrap.


Issue created by migration from https://trac.sagemath.org/ticket/3429





---

archive/issue_comments_024164.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-15T20:16:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3429#issuecomment-24164",
    "user": "cpernet"
}
```

Changing status from new to assigned.



---

archive/issue_comments_024165.json:
```json
{
    "body": "The proposed new linbox spkg is available at\nhttp:/sage.math.washington.edu/home/pernet/linbox-1.1.6rc0.spkg",
    "created_at": "2008-06-15T20:16:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3429#issuecomment-24165",
    "user": "cpernet"
}
```

The proposed new linbox spkg is available at
http:/sage.math.washington.edu/home/pernet/linbox-1.1.6rc0.spkg



---

archive/issue_comments_024166.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mabshoff\".",
    "created_at": "2008-06-15T21:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3429#issuecomment-24166",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_mabshoff".



---

archive/issue_comments_024167.json:
```json
{
    "body": "The spkg builds fine for me on OSX and Linux x86-64 and doctests fine. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-26T03:44:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3429#issuecomment-24167",
    "user": "mabshoff"
}
```

The spkg builds fine for me on OSX and Linux x86-64 and doctests fine. Positive review.

Cheers,

Michael



---

archive/issue_comments_024168.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-26T03:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3429#issuecomment-24168",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024169.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-26T03:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3429#issuecomment-24169",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha1



---

archive/issue_comments_024170.json:
```json
{
    "body": "Attachment [update_new_linbox_interface.patch](tarball://root/attachments/some-uuid/ticket3429/update_new_linbox_interface.patch) by cpernet created at 2008-06-27 21:14:54\n\nFix the new naming convention (include files and libraries) for linbox-1.1.6rc0",
    "created_at": "2008-06-27T21:14:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3429#issuecomment-24170",
    "user": "cpernet"
}
```

Attachment [update_new_linbox_interface.patch](tarball://root/attachments/some-uuid/ticket3429/update_new_linbox_interface.patch) by cpernet created at 2008-06-27 21:14:54

Fix the new naming convention (include files and libraries) for linbox-1.1.6rc0



---

archive/issue_comments_024171.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-06-27T21:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3429#issuecomment-24171",
    "user": "cpernet"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_024172.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2008-06-27T21:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3429#issuecomment-24172",
    "user": "cpernet"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_024173.json:
```json
{
    "body": "Reopening this ticket, since I forgot to update the sage hooks on the linbox library.\nEverything went well on installations that had the previous library installed. So the problem only proped up when doing a fresh install.\nSee [http://groups.google.fr/group/sage-devel/browse_thread/thread/a7067a9a6c9464fc](http://groups.google.fr/group/sage-devel/browse_thread/thread/a7067a9a6c9464fc)\n\nI am attaching a patch fixing this.",
    "created_at": "2008-06-27T21:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3429#issuecomment-24173",
    "user": "cpernet"
}
```

Reopening this ticket, since I forgot to update the sage hooks on the linbox library.
Everything went well on installations that had the previous library installed. So the problem only proped up when doing a fresh install.
See [http://groups.google.fr/group/sage-devel/browse_thread/thread/a7067a9a6c9464fc](http://groups.google.fr/group/sage-devel/browse_thread/thread/a7067a9a6c9464fc)

I am attaching a patch fixing this.



---

archive/issue_comments_024174.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-06-27T21:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3429#issuecomment-24174",
    "user": "cpernet"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_024175.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-06-27T21:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3429#issuecomment-24175",
    "user": "cpernet"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_024176.json:
```json
{
    "body": "Positive review on update_new_linbox_interface.patch. After applying to a fresh build of 3.0.4.alpha1 the Sage library builds and passes doctests.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-30T04:58:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3429#issuecomment-24176",
    "user": "mabshoff"
}
```

Positive review on update_new_linbox_interface.patch. After applying to a fresh build of 3.0.4.alpha1 the Sage library builds and passes doctests.

Cheers,

Michael



---

archive/issue_comments_024177.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-30T04:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3429#issuecomment-24177",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024178.json:
```json
{
    "body": "Merged update_new_linbox_interface.patch in Sage 3.0.4.alpha2",
    "created_at": "2008-06-30T04:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3429#issuecomment-24178",
    "user": "mabshoff"
}
```

Merged update_new_linbox_interface.patch in Sage 3.0.4.alpha2
