# Issue 4661: clean up module_list.py

archive/issues_004661.json:
```json
{
    "body": "Assignee: @craigcitro\n\nThere were a few duplicate entries in  `module_list.py`, which didn't cause any trouble, but caused sage to build some extensions (like `sage/structure/sage_object.pyx`) multiple times during the build. The attached patch alphabetizes the module list, and removes duplicates.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4661\n\n",
    "created_at": "2008-11-30T09:00:21Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "clean up module_list.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4661",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

There were a few duplicate entries in  `module_list.py`, which didn't cause any trouble, but caused sage to build some extensions (like `sage/structure/sage_object.pyx`) multiple times during the build. The attached patch alphabetizes the module list, and removes duplicates.

Issue created by migration from https://trac.sagemath.org/ticket/4661





---

archive/issue_comments_035032.json:
```json
{
    "body": "Attachment [trac_4661.patch](tarball://root/attachments/some-uuid/ticket4661/trac_4661.patch) by mabshoff created at 2008-11-30 10:11:22\n\nI just posted Craig's patch that he gave to me off-trac. I did nuke the build directory and a sage -ba followed by a -t -long passed, so positive review.\n\nSome commented out extensions might have to be nuked, but that ought to get taken care of via the followup ticket #4663.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-30T10:11:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4661#issuecomment-35032",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4661.patch](tarball://root/attachments/some-uuid/ticket4661/trac_4661.patch) by mabshoff created at 2008-11-30 10:11:22

I just posted Craig's patch that he gave to me off-trac. I did nuke the build directory and a sage -ba followed by a -t -long passed, so positive review.

Some commented out extensions might have to be nuked, but that ought to get taken care of via the followup ticket #4663.

Cheers,

Michael



---

archive/issue_events_004909.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-11-30T10:11:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4661",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4661#event-4909"
}
```



---

archive/issue_comments_035033.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-30T10:11:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4661#issuecomment-35033",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035034.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc1",
    "created_at": "2008-11-30T10:11:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4661#issuecomment-35034",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.rc1
