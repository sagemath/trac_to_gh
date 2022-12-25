# Issue 5394: [with patch, needs review] Remove the remnants of the docs from sage-ptest and make it ignore the devel/sage/build directory

archive/issues_005394.json:
```json
{
    "body": "Assignee: cwitty\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5394\n\n",
    "created_at": "2009-02-27T17:14:13Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "[with patch, needs review] Remove the remnants of the docs from sage-ptest and make it ignore the devel/sage/build directory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5394",
    "user": "https://github.com/mwhansen"
}
```
Assignee: cwitty



Issue created by migration from https://trac.sagemath.org/ticket/5394





---

archive/issue_comments_041459.json:
```json
{
    "body": "Attachment [trac_5394.patch](tarball://root/attachments/some-uuid/ticket5394/trac_5394.patch) by mabshoff created at 2009-02-27 21:03:32\n\nExcellent, couldn't have done it better myself :)\n\nCheers,\n\nMichael",
    "created_at": "2009-02-27T21:03:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5394#issuecomment-41459",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5394.patch](tarball://root/attachments/some-uuid/ticket5394/trac_5394.patch) by mabshoff created at 2009-02-27 21:03:32

Excellent, couldn't have done it better myself :)

Cheers,

Michael



---

archive/issue_comments_041460.json:
```json
{
    "body": "Merged in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-27T23:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5394#issuecomment-41460",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.rc0.

Cheers,

Michael



---

archive/issue_events_012570.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-27T23:07:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5394",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5394#event-12570"
}
```



---

archive/issue_comments_041461.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-27T23:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5394#issuecomment-41461",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041462.json:
```json
{
    "body": "This patch actually does not ignore the bits in build and I am not quite sure why the patch doesn't work.\n\nMike: Thoughts?\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T12:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5394#issuecomment-41462",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch actually does not ignore the bits in build and I am not quite sure why the patch doesn't work.

Mike: Thoughts?

Cheers,

Michael



---

archive/issue_comments_041463.json:
```json
{
    "body": "Ok, figured it out - reviewer patch coming up.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T12:35:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5394#issuecomment-41463",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, figured it out - reviewer patch coming up.

Cheers,

Michael



---

archive/issue_comments_041464.json:
```json
{
    "body": "Attachment [trac_5394-reviewer.patch](tarball://root/attachments/some-uuid/ticket5394/trac_5394-reviewer.patch) by mabshoff created at 2009-02-28 15:50:50\n\nOops, the reviewer patch had some debug output in it. I removed that in the tree and did another checkin.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T15:50:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5394#issuecomment-41464",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5394-reviewer.patch](tarball://root/attachments/some-uuid/ticket5394/trac_5394-reviewer.patch) by mabshoff created at 2009-02-28 15:50:50

Oops, the reviewer patch had some debug output in it. I removed that in the tree and did another checkin.

Cheers,

Michael
