# Issue 3110: [with patch, needs review] rare pbuild dependency bug

archive/issues_003110.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nKeywords: pbuild\n\nThis patch corrects a bug in pbuild dependency checking that does not correctly register the pxd file dependency for a pyx file if no other files cimport the file (rare).\n\nIssue created by migration from https://trac.sagemath.org/ticket/3110\n\n",
    "created_at": "2008-05-06T04:33:11Z",
    "labels": [
        "component: pbuild",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "[with patch, needs review] rare pbuild dependency bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3110",
    "user": "https://github.com/garyfurnish"
}
```
Assignee: @garyfurnish

Keywords: pbuild

This patch corrects a bug in pbuild dependency checking that does not correctly register the pxd file dependency for a pyx file if no other files cimport the file (rare).

Issue created by migration from https://trac.sagemath.org/ticket/3110





---

archive/issue_comments_021452.json:
```json
{
    "body": "Attachment [trac_extcode_3110.patch](tarball://root/attachments/some-uuid/ticket3110/trac_extcode_3110.patch) by @garyfurnish created at 2008-05-06 04:34:54",
    "created_at": "2008-05-06T04:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3110#issuecomment-21452",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_extcode_3110.patch](tarball://root/attachments/some-uuid/ticket3110/trac_extcode_3110.patch) by @garyfurnish created at 2008-05-06 04:34:54



---

archive/issue_comments_021453.json:
```json
{
    "body": "This patch also modifies -ba to clean the build directory.",
    "created_at": "2008-05-06T04:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3110#issuecomment-21453",
    "user": "https://github.com/garyfurnish"
}
```

This patch also modifies -ba to clean the build directory.



---

archive/issue_comments_021454.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-06T04:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3110#issuecomment-21454",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021455.json:
```json
{
    "body": "Path looks good to me. One thing: This patch also contains unrelated changes [besides the clean option] which are uncontroversial. I would suggest that you also add some release number that you increment on changes so we do not end up having to poke around for the exact version of pbuild when we need to debug some problem remotely.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-06T20:01:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3110#issuecomment-21455",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Path looks good to me. One thing: This patch also contains unrelated changes [besides the clean option] which are uncontroversial. I would suggest that you also add some release number that you increment on changes so we do not end up having to poke around for the exact version of pbuild when we need to debug some problem remotely.

Cheers,

Michael



---

archive/issue_comments_021456.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha0",
    "created_at": "2008-05-06T20:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3110#issuecomment-21456",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.alpha0



---

archive/issue_events_007026.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-06T20:02:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3110",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3110#event-7026"
}
```



---

archive/issue_comments_021457.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-06T20:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3110#issuecomment-21457",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
