# Issue 4760: [with patch, needs review] dsage_interface doctests broken

archive/issues_004760.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nThe doctests in dsage_interface are disabled and do not work properly when enabled.  This patch fixes these issues.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/4760\n\n",
    "created_at": "2008-12-11T14:51:54Z",
    "labels": [
        "component: dsage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "[with patch, needs review] dsage_interface doctests broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4760",
    "user": "https://github.com/garyfurnish"
}
```
Assignee: @garyfurnish

The doctests in dsage_interface are disabled and do not work properly when enabled.  This patch fixes these issues.  

Issue created by migration from https://trac.sagemath.org/ticket/4760





---

archive/issue_comments_036003.json:
```json
{
    "body": "Attachment [trac_4760.patch](tarball://root/attachments/some-uuid/ticket4760/trac_4760.patch) by @garyfurnish created at 2008-12-11 14:53:26",
    "created_at": "2008-12-11T14:53:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4760#issuecomment-36003",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_4760.patch](tarball://root/attachments/some-uuid/ticket4760/trac_4760.patch) by @garyfurnish created at 2008-12-11 14:53:26



---

archive/issue_comments_036004.json:
```json
{
    "body": "All tests pass for me after #4745 and this patch.  I think the doctests should still be rewritten to use start_all since that should be the preferred way to do things.",
    "created_at": "2008-12-11T15:03:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4760#issuecomment-36004",
    "user": "https://github.com/mwhansen"
}
```

All tests pass for me after #4745 and this patch.  I think the doctests should still be rewritten to use start_all since that should be the preferred way to do things.



---

archive/issue_comments_036005.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-11T15:04:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4760#issuecomment-36005",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036006.json:
```json
{
    "body": "The following comment in the file should definitely be deleted:\n\n```\n3\t3\tDoctesting of this file is disabled because it fails in so many ways it is even funny. \n4\t4\tSee http://trac.sagemath.org/sage_trac/ticket/3593 for two of the four ways I've\n<SNIP> \n```\n\nI will do so via a referee patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-11T15:47:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4760#issuecomment-36006",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The following comment in the file should definitely be deleted:

```
3	3	Doctesting of this file is disabled because it fails in so many ways it is even funny. 
4	4	See http://trac.sagemath.org/sage_trac/ticket/3593 for two of the four ways I've
<SNIP> 
```

I will do so via a referee patch.

Cheers,

Michael



---

archive/issue_comments_036007.json:
```json
{
    "body": "Attachment [trac_4760-referee.patch](tarball://root/attachments/some-uuid/ticket4760/trac_4760-referee.patch) by mabshoff created at 2008-12-11 15:55:18",
    "created_at": "2008-12-11T15:55:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4760#issuecomment-36007",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4760-referee.patch](tarball://root/attachments/some-uuid/ticket4760/trac_4760-referee.patch) by mabshoff created at 2008-12-11 15:55:18



---

archive/issue_comments_036008.json:
```json
{
    "body": "Merged both patches in Sage 3.2.2.alpha2",
    "created_at": "2008-12-11T15:55:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4760#issuecomment-36008",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.2.2.alpha2



---

archive/issue_events_010888.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-11T15:55:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4760",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4760#event-10888"
}
```



---

archive/issue_comments_036009.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-11T15:55:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4760#issuecomment-36009",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
