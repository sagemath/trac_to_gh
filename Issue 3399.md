# Issue 3399: [with patch, needs review] sage build scripts should be moved to devel

archive/issues_003399.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nThe sage build files that use pbuild should be moved to the devel repo while the pbuild files should stay in extcode.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3399\n\n",
    "created_at": "2008-06-11T15:00:38Z",
    "labels": [
        "component: pbuild",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch, needs review] sage build scripts should be moved to devel",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3399",
    "user": "https://github.com/garyfurnish"
}
```
Assignee: @garyfurnish

The sage build files that use pbuild should be moved to the devel repo while the pbuild files should stay in extcode.

Issue created by migration from https://trac.sagemath.org/ticket/3399





---

archive/issue_comments_023753.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-11T15:03:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3399#issuecomment-23753",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_023754.json:
```json
{
    "body": "Good in principle, but as discussed with you in person this does not work as is due to circular dependency issues.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-11T20:50:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3399#issuecomment-23754",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Good in principle, but as discussed with you in person this does not work as is due to circular dependency issues.

Cheers,

Michael



---

archive/issue_comments_023755.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mabshoff\".",
    "created_at": "2008-06-20T05:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3399#issuecomment-23755",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "" to "editor_mabshoff".



---

archive/issue_comments_023756.json:
```json
{
    "body": "Attachment [trac_3399_2.patch](tarball://root/attachments/some-uuid/ticket3399/trac_3399_2.patch) by @garyfurnish created at 2008-07-01 16:47:03",
    "created_at": "2008-07-01T16:47:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3399#issuecomment-23756",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_3399_2.patch](tarball://root/attachments/some-uuid/ticket3399/trac_3399_2.patch) by @garyfurnish created at 2008-07-01 16:47:03



---

archive/issue_comments_023757.json:
```json
{
    "body": "Attachment [trac_3399_2_extcode.patch](tarball://root/attachments/some-uuid/ticket3399/trac_3399_2_extcode.patch) by @garyfurnish created at 2008-07-01 16:47:19",
    "created_at": "2008-07-01T16:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3399#issuecomment-23757",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_3399_2_extcode.patch](tarball://root/attachments/some-uuid/ticket3399/trac_3399_2_extcode.patch) by @garyfurnish created at 2008-07-01 16:47:19



---

archive/issue_comments_023758.json:
```json
{
    "body": "Attachment [trac_3399_2_scripts.patch](tarball://root/attachments/some-uuid/ticket3399/trac_3399_2_scripts.patch) by @garyfurnish created at 2008-07-01 16:48:14\n\nPlease remove the old patches, apply the new patches, and rereview.  This patch also adds documentation on how to add files to pbuild: see devel/sage/sagebuild.py",
    "created_at": "2008-07-01T16:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3399#issuecomment-23758",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_3399_2_scripts.patch](tarball://root/attachments/some-uuid/ticket3399/trac_3399_2_scripts.patch) by @garyfurnish created at 2008-07-01 16:48:14

Please remove the old patches, apply the new patches, and rereview.  This patch also adds documentation on how to add files to pbuild: see devel/sage/sagebuild.py



---

archive/issue_comments_023759.json:
```json
{
    "body": "Patch looks good to me and applies cleanly. Positive review. We might have to think about names and locations of those files in the long term, but for now this does the right thing.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-06T09:05:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3399#issuecomment-23759",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me and applies cleanly. Positive review. We might have to think about names and locations of those files in the long term, but for now this does the right thing.

Cheers,

Michael



---

archive/issue_comments_023760.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-06T09:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3399#issuecomment-23760",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023761.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha2",
    "created_at": "2008-07-06T09:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3399#issuecomment-23761",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha2
