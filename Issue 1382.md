# Issue 1382: conversion of sage matrices to mathematica is just completely totally broken

archive/issues_001382.json:
```json
{
    "body": "Assignee: @williamstein\n\nWe have\n\n```\nsage: n = matrix(QQ, 3, range(9))\nsage: n._mathematica_init_()\n'{{0},{1},{2},{3},{4},{5},{6},{7},{8}}'\n```\n\nbut we should have\n\n```\nsage: n = matrix(QQ, 3, range(9))\nsage: n._mathematica_init_()\n'{{0,1,2},{3,4,5},{6,7,8}}'\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1382\n\n",
    "created_at": "2007-12-03T17:09:37Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "conversion of sage matrices to mathematica is just completely totally broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1382",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

We have

```
sage: n = matrix(QQ, 3, range(9))
sage: n._mathematica_init_()
'{{0},{1},{2},{3},{4},{5},{6},{7},{8}}'
```

but we should have

```
sage: n = matrix(QQ, 3, range(9))
sage: n._mathematica_init_()
'{{0,1,2},{3,4,5},{6,7,8}}'
```




Issue created by migration from https://trac.sagemath.org/ticket/1382





---

archive/issue_events_003573.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-22T12:19:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1382",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1382#event-3573"
}
```



---

archive/issue_comments_008835.json:
```json
{
    "body": "Attachment [ticket_1382.patch](tarball://root/attachments/some-uuid/ticket1382/ticket_1382.patch) by mabshoff created at 2008-02-16 23:29:25",
    "created_at": "2008-02-16T23:29:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1382#issuecomment-8835",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [ticket_1382.patch](tarball://root/attachments/some-uuid/ticket1382/ticket_1382.patch) by mabshoff created at 2008-02-16 23:29:25



---

archive/issue_comments_008836.json:
```json
{
    "body": "Attachment [task_1832_2.patch](tarball://root/attachments/some-uuid/ticket1382/task_1832_2.patch) by TimothyClemans created at 2008-02-16 23:58:50",
    "created_at": "2008-02-16T23:58:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1382#issuecomment-8836",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [task_1832_2.patch](tarball://root/attachments/some-uuid/ticket1382/task_1832_2.patch) by TimothyClemans created at 2008-02-16 23:58:50



---

archive/issue_comments_008837.json:
```json
{
    "body": "Attachment [task_1832_3.patch](tarball://root/attachments/some-uuid/ticket1382/task_1832_3.patch) by TimothyClemans created at 2008-02-17 00:01:17",
    "created_at": "2008-02-17T00:01:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1382#issuecomment-8837",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [task_1832_3.patch](tarball://root/attachments/some-uuid/ticket1382/task_1832_3.patch) by TimothyClemans created at 2008-02-17 00:01:17



---

archive/issue_comments_008838.json:
```json
{
    "body": "Attachment [task_1382_4.patch](tarball://root/attachments/some-uuid/ticket1382/task_1382_4.patch) by TimothyClemans created at 2008-02-17 00:21:09",
    "created_at": "2008-02-17T00:21:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1382#issuecomment-8838",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [task_1382_4.patch](tarball://root/attachments/some-uuid/ticket1382/task_1382_4.patch) by TimothyClemans created at 2008-02-17 00:21:09



---

archive/issue_comments_008839.json:
```json
{
    "body": "Changing assignee from @williamstein to TimothyClemans.",
    "created_at": "2008-02-17T00:31:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1382#issuecomment-8839",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Changing assignee from @williamstein to TimothyClemans.



---

archive/issue_comments_008840.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-17T00:31:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1382#issuecomment-8840",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008841.json:
```json
{
    "body": "Attachment [combined_1382.patch](tarball://root/attachments/some-uuid/ticket1382/combined_1382.patch) by TimothyClemans created at 2008-02-17 01:13:19",
    "created_at": "2008-02-17T01:13:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1382#issuecomment-8841",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [combined_1382.patch](tarball://root/attachments/some-uuid/ticket1382/combined_1382.patch) by TimothyClemans created at 2008-02-17 01:13:19



---

archive/issue_comments_008842.json:
```json
{
    "body": "This will not work, since it does not appear to be recursive.  For example:\n\n```\nsage: var('x, y, z, b')\n(x, y, z, b)\nsage: f = sin(x^2) + y^z\nsage: f\ny^z + sin(x^2)\nsage: f._mathematica_init_()\n'(Sin[(x) ^ (2)]) + ((y) ^ (z))'\nsage: M = matrix(1, 2, [f, f^2]); M\n[    y^z + sin(x^2) (y^z + sin(x^2))^2]\n```\n\nAlso, please post a unified patch making it easy to see just the total changes.",
    "created_at": "2008-02-17T01:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1382#issuecomment-8842",
    "user": "https://github.com/ncalexan"
}
```

This will not work, since it does not appear to be recursive.  For example:

```
sage: var('x, y, z, b')
(x, y, z, b)
sage: f = sin(x^2) + y^z
sage: f
y^z + sin(x^2)
sage: f._mathematica_init_()
'(Sin[(x) ^ (2)]) + ((y) ^ (z))'
sage: M = matrix(1, 2, [f, f^2]); M
[    y^z + sin(x^2) (y^z + sin(x^2))^2]
```

Also, please post a unified patch making it easy to see just the total changes.



---

archive/issue_comments_008843.json:
```json
{
    "body": "Attachment [1382_5.patch](tarball://root/attachments/some-uuid/ticket1382/1382_5.patch) by @williamstein created at 2008-02-23 00:57:10\n\n(this one by William and Timothy) apply this patch right after applying 1382_2.patch",
    "created_at": "2008-02-23T00:57:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1382#issuecomment-8843",
    "user": "https://github.com/williamstein"
}
```

Attachment [1382_5.patch](tarball://root/attachments/some-uuid/ticket1382/1382_5.patch) by @williamstein created at 2008-02-23 00:57:10

(this one by William and Timothy) apply this patch right after applying 1382_2.patch



---

archive/issue_comments_008844.json:
```json
{
    "body": "Attachment [1382_5-part2of2.patch](tarball://root/attachments/some-uuid/ticket1382/1382_5-part2of2.patch) by @williamstein created at 2008-02-23 00:57:26",
    "created_at": "2008-02-23T00:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1382#issuecomment-8844",
    "user": "https://github.com/williamstein"
}
```

Attachment [1382_5-part2of2.patch](tarball://root/attachments/some-uuid/ticket1382/1382_5-part2of2.patch) by @williamstein created at 2008-02-23 00:57:26



---

archive/issue_comments_008845.json:
```json
{
    "body": "Patch looks good, I say apply.\n\nIs _mathematica_init_ guaranteed not to require Mathematica?  If not, some more doctests need to be declared optional.  Otherwise, looks good.",
    "created_at": "2008-02-23T01:04:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1382#issuecomment-8845",
    "user": "https://github.com/ncalexan"
}
```

Patch looks good, I say apply.

Is _mathematica_init_ guaranteed not to require Mathematica?  If not, some more doctests need to be declared optional.  Otherwise, looks good.



---

archive/issue_comments_008846.json:
```json
{
    "body": "> Is _mathematica_init_ guaranteed not to require Mathematica? \n\n\nYes.  It returns a string is must not call Mathematica. \n\nWilliam",
    "created_at": "2008-02-23T01:06:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1382#issuecomment-8846",
    "user": "https://github.com/williamstein"
}
```

> Is _mathematica_init_ guaranteed not to require Mathematica? 


Yes.  It returns a string is must not call Mathematica. 

William



---

archive/issue_comments_008847.json:
```json
{
    "body": "Somebody ought to clue be in \n\n* which patches to apply in which order (the comments are unclear)\n* if all problems regarding optional doctests are solved, i.e. the last comment by William\n\nCheers,\n\nMichael",
    "created_at": "2008-02-24T19:59:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1382#issuecomment-8847",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Somebody ought to clue be in 

* which patches to apply in which order (the comments are unclear)
* if all problems regarding optional doctests are solved, i.e. the last comment by William

Cheers,

Michael



---

archive/issue_comments_008848.json:
```json
{
    "body": "Michael.  Apply 1382_2.patch then 1382_5-part2of2.patch.  And the comment about optional is not applicable since _mathematica_init_ should never depend on mathematica.",
    "created_at": "2008-02-24T20:39:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1382#issuecomment-8848",
    "user": "https://github.com/williamstein"
}
```

Michael.  Apply 1382_2.patch then 1382_5-part2of2.patch.  And the comment about optional is not applicable since _mathematica_init_ should never depend on mathematica.



---

archive/issue_comments_008849.json:
```json
{
    "body": "William's patch seems to be editing 1382_5.patch. task_1832_2.patch depends on ticket_1382.patch and it doesn't have lines like \"return mathematica.mathematica(tuple(self))\" which are in 1382_5.patch and show up in red on http://trac.sagemath.org/sage_trac/attachment/ticket/1382/1382_5-part2of2.patch",
    "created_at": "2008-02-24T20:48:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1382#issuecomment-8849",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

William's patch seems to be editing 1382_5.patch. task_1832_2.patch depends on ticket_1382.patch and it doesn't have lines like "return mathematica.mathematica(tuple(self))" which are in 1382_5.patch and show up in red on http://trac.sagemath.org/sage_trac/attachment/ticket/1382/1382_5-part2of2.patch



---

archive/issue_comments_008850.json:
```json
{
    "body": "The patches at this ticket are a mess either way: For task_1832_2.patch I need to ticket_1382.patch. But at that point 1382_5-part2of2.patch doesn't apply cleanly. So, in conclusion: Please post a single patch that has all the changes and that applies cleanly against 2.10.2. To do that merge the fixes back by hand, do not just post a bundle with all patches applied. \n\nCheers,\n\nMichael",
    "created_at": "2008-02-24T21:05:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1382#issuecomment-8850",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patches at this ticket are a mess either way: For task_1832_2.patch I need to ticket_1382.patch. But at that point 1382_5-part2of2.patch doesn't apply cleanly. So, in conclusion: Please post a single patch that has all the changes and that applies cleanly against 2.10.2. To do that merge the fixes back by hand, do not just post a bundle with all patches applied. 

Cheers,

Michael



---

archive/issue_comments_008851.json:
```json
{
    "body": "I made a typo.  Simply apply \n\n* 1382_5.patch\n* 1382_5-part2of2.patch. \n\nThat's it.  2 patches.   They should not be flattened. \n\nWilliam",
    "created_at": "2008-02-24T21:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1382#issuecomment-8851",
    "user": "https://github.com/williamstein"
}
```

I made a typo.  Simply apply 

* 1382_5.patch
* 1382_5-part2of2.patch. 

That's it.  2 patches.   They should not be flattened. 

William



---

archive/issue_comments_008852.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-24T21:25:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1382#issuecomment-8852",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_008853.json:
```json
{
    "body": "Merged 1382_5.patch and 1382_5-part2of2.patch in Sage 2.10.3.alpha0. Thanks William for the clarification.",
    "created_at": "2008-02-24T21:25:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1382#issuecomment-8853",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 1382_5.patch and 1382_5-part2of2.patch in Sage 2.10.3.alpha0. Thanks William for the clarification.



---

archive/issue_events_003574.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-24T21:25:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1382",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1382#event-3574"
}
```
