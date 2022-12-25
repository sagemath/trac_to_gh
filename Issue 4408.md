# Issue 4408: magma interface -- change _magma_init_ to take non-optional magma argument

archive/issues_004408.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis patch touches a lot of files in a trivial automatic way.  They main point is it changes the _magma_init_ signature from \n\n_magma_init_(self)\n\nto \n\n_magma_init_(self, magma)\n\nwhere magma is a magma interface.  Also, it introduces some caching for the magma interface itself.  This means that _magma_init_ has access to and can impact the full state of the magma interpreter.   This makes creating a string representation of an element valid for that interpreter dramatically more powerful and flexible, is conceptually very easy to understand, and works.  The caching helps mediate potential efficiency issues. \n\nNote, whether caching should be on or off by default is unclear, and I think can only be answered by implementing a lot more of this framework and doing some profiling. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4408\n\n",
    "created_at": "2008-10-31T01:50:04Z",
    "labels": [
        "component: interfaces"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "magma interface -- change _magma_init_ to take non-optional magma argument",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4408",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

This patch touches a lot of files in a trivial automatic way.  They main point is it changes the _magma_init_ signature from 

_magma_init_(self)

to 

_magma_init_(self, magma)

where magma is a magma interface.  Also, it introduces some caching for the magma interface itself.  This means that _magma_init_ has access to and can impact the full state of the magma interpreter.   This makes creating a string representation of an element valid for that interpreter dramatically more powerful and flexible, is conceptually very easy to understand, and works.  The caching helps mediate potential efficiency issues. 

Note, whether caching should be on or off by default is unclear, and I think can only be answered by implementing a lot more of this framework and doing some profiling. 

Issue created by migration from https://trac.sagemath.org/ticket/4408





---

archive/issue_comments_032349.json:
```json
{
    "body": "Attachment [sage-4408.patch](tarball://root/attachments/some-uuid/ticket4408/sage-4408.patch) by mabshoff created at 2008-10-31 04:08:23",
    "created_at": "2008-10-31T04:08:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4408#issuecomment-32349",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [sage-4408.patch](tarball://root/attachments/some-uuid/ticket4408/sage-4408.patch) by mabshoff created at 2008-10-31 04:08:23



---

archive/issue_comments_032350.json:
```json
{
    "body": "I've decided caching is not the default, since I don't want to blatantly introduce memory leaks. The second patch implements this change (one line change), plus changes all _magma_init_()'s to appropriate _magma_init_(magma).",
    "created_at": "2008-11-04T05:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4408#issuecomment-32350",
    "user": "https://github.com/williamstein"
}
```

I've decided caching is not the default, since I don't want to blatantly introduce memory leaks. The second patch implements this change (one line change), plus changes all _magma_init_()'s to appropriate _magma_init_(magma).



---

archive/issue_comments_032351.json:
```json
{
    "body": "Attachment [sage-4408-part2.patch](tarball://root/attachments/some-uuid/ticket4408/sage-4408-part2.patch) by @williamstein created at 2008-11-04 05:33:02",
    "created_at": "2008-11-04T05:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4408#issuecomment-32351",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-4408-part2.patch](tarball://root/attachments/some-uuid/ticket4408/sage-4408-part2.patch) by @williamstein created at 2008-11-04 05:33:02



---

archive/issue_comments_032352.json:
```json
{
    "body": "Attachment [sage-4408-part3.patch](tarball://root/attachments/some-uuid/ticket4408/sage-4408-part3.patch) by @williamstein created at 2008-11-14 00:53:32",
    "created_at": "2008-11-14T00:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4408#issuecomment-32352",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-4408-part3.patch](tarball://root/attachments/some-uuid/ticket4408/sage-4408-part3.patch) by @williamstein created at 2008-11-14 00:53:32



---

archive/issue_comments_032353.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-11-24T03:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4408#issuecomment-32353",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid



---

archive/issue_comments_032354.json:
```json
{
    "body": "I've decided this approach with caching is the wrong design since it would introduce memory leaks.  I'm closing this ticket/approach as invalid, and opening a new one, which\nimplements related ideas and gets it right.  See #4601.",
    "created_at": "2008-11-24T03:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4408#issuecomment-32354",
    "user": "https://github.com/williamstein"
}
```

I've decided this approach with caching is the wrong design since it would introduce memory leaks.  I'm closing this ticket/approach as invalid, and opening a new one, which
implements related ideas and gets it right.  See #4601.
