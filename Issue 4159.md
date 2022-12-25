# Issue 4159: sage -bdist fails on osx 10.5 ppc with libpng errors

archive/issues_004159.json:
```json
{
    "body": "Assignee: mabshoff\n\nWith sage-3.1.2 if you try to do sage -bdist it fails with weird libpng linking errors\nand missing symbols.  This is when it tries to make a dmg. \n\nFor the 3.1.2 binary, I'm just using tar for now until this is fixed.  The fix will\nprobably be to unset some dynamic library paths right before running the commands\nin the sage-bdist script that create the dmg. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4159\n\n",
    "created_at": "2008-09-20T15:47:42Z",
    "labels": [
        "component: distribution",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "sage -bdist fails on osx 10.5 ppc with libpng errors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4159",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

With sage-3.1.2 if you try to do sage -bdist it fails with weird libpng linking errors
and missing symbols.  This is when it tries to make a dmg. 

For the 3.1.2 binary, I'm just using tar for now until this is fixed.  The fix will
probably be to unset some dynamic library paths right before running the commands
in the sage-bdist script that create the dmg. 

Issue created by migration from https://trac.sagemath.org/ticket/4159





---

archive/issue_comments_030127.json:
```json
{
    "body": "What are the errors? Is this on varro?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-20T20:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4159#issuecomment-30127",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

What are the errors? Is this on varro?

Cheers,

Michael



---

archive/issue_comments_030128.json:
```json
{
    "body": "It turns out that this happens on *all* OS X machines, both 10.5 and 10.4 on both ppc and intel.  Basically \"sage -bdist\" is completely broken in sage-3.1.2 on OS X.",
    "created_at": "2008-09-21T13:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4159#issuecomment-30128",
    "user": "https://github.com/williamstein"
}
```

It turns out that this happens on *all* OS X machines, both 10.5 and 10.4 on both ppc and intel.  Basically "sage -bdist" is completely broken in sage-3.1.2 on OS X.



---

archive/issue_comments_030129.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-09-21T13:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4159#issuecomment-30129",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_030130.json:
```json
{
    "body": "Yeah, I agree that the fix will be to unset DYLD_LIBRARY_PATH right before actually calling hdiutil in sage-bdist. Very odd that a command line utility pulls in libpng symbols. Oh well.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-21T17:57:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4159#issuecomment-30130",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Yeah, I agree that the fix will be to unset DYLD_LIBRARY_PATH right before actually calling hdiutil in sage-bdist. Very odd that a command line utility pulls in libpng symbols. Oh well.

Cheers,

Michael



---

archive/issue_comments_030131.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-30T17:43:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4159#issuecomment-30131",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030132.json:
```json
{
    "body": "Patch coming up.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-30T17:43:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4159#issuecomment-30132",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch coming up.

Cheers,

Michael



---

archive/issue_comments_030133.json:
```json
{
    "body": "Attachment [trac_4159.patch](tarball://root/attachments/some-uuid/ticket4159/trac_4159.patch) by @mwhansen created at 2008-10-12 23:30:27",
    "created_at": "2008-10-12T23:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4159#issuecomment-30133",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4159.patch](tarball://root/attachments/some-uuid/ticket4159/trac_4159.patch) by @mwhansen created at 2008-10-12 23:30:27



---

archive/issue_comments_030134.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-10-12T23:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4159#issuecomment-30134",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_030135.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-12T23:39:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4159#issuecomment-30135",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030136.json:
```json
{
    "body": "Merged in Sage 3.1.3.rc0",
    "created_at": "2008-10-12T23:39:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4159#issuecomment-30136",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.rc0
