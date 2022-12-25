# Issue 5983: [with patch, positive review] cmp related doctest failure in sage/schemes/jacobians/abstract_jacobian.py

archive/issues_005983.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  alexghitza\n\nThis says it all and fails on occasion due to memory layout, etc. Writing a doctest this way is **wrong**:\n\n```\nsage -t -long \"devel/sage/sage/schemes/jacobians/abstract_jacobian.py\"\n**********************************************************************\nFile \"/home/mabshoff/build-3.4.2/sage-3.4.2-eno-gcc-4.3.3/devel/sage/sage/schemes/jacobians/abstract_jacobian.py\", line 118:\n    sage: J1 < P2\nExpected:\n    False\nGot:\n    True\n**********************************************************************\nFile \"/home/mabshoff/build-3.4.2/sage-3.4.2-eno-gcc-4.3.3/devel/sage/sage/schemes/jacobians/abstract_jacobian.py\", line 120:\n    sage: J1 > P2\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n```\nI am CCing Alex since I believe he wrote this doctest :)\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5983\n\n",
    "closed_at": "2009-05-05T04:21:02Z",
    "created_at": "2009-05-05T03:39:23Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "[with patch, positive review] cmp related doctest failure in sage/schemes/jacobians/abstract_jacobian.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5983",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  alexghitza

This says it all and fails on occasion due to memory layout, etc. Writing a doctest this way is **wrong**:

```
sage -t -long "devel/sage/sage/schemes/jacobians/abstract_jacobian.py"
**********************************************************************
File "/home/mabshoff/build-3.4.2/sage-3.4.2-eno-gcc-4.3.3/devel/sage/sage/schemes/jacobians/abstract_jacobian.py", line 118:
    sage: J1 < P2
Expected:
    False
Got:
    True
**********************************************************************
File "/home/mabshoff/build-3.4.2/sage-3.4.2-eno-gcc-4.3.3/devel/sage/sage/schemes/jacobians/abstract_jacobian.py", line 120:
    sage: J1 > P2
Expected:
    True
Got:
    False
**********************************************************************
```
I am CCing Alex since I believe he wrote this doctest :)

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5983





---

archive/issue_comments_047447.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-05T03:39:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5983#issuecomment-47447",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_events_014037.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-05T03:39:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5983",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5983#event-14037"
}
```



---

archive/issue_comments_047448.json:
```json
{
    "body": "Attachment [trac_5983.patch](tarball://root/attachments/some-uuid/ticket5983/trac_5983.patch) by @williamstein created at 2009-05-05 03:59:04",
    "created_at": "2009-05-05T03:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5983#issuecomment-47448",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5983.patch](tarball://root/attachments/some-uuid/ticket5983/trac_5983.patch) by @williamstein created at 2009-05-05 03:59:04



---

archive/issue_comments_047449.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-05T04:21:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5983#issuecomment-47449",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_014038.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-05T04:21:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5983",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5983#event-14038"
}
```



---

archive/issue_comments_047450.json:
```json
{
    "body": "Merged in Sage 3.4.2.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-05T04:21:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5983#issuecomment-47450",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.2.

Cheers,

Michael



---

archive/issue_comments_047451.json:
```json
{
    "body": "Replying to [ticket:5983 mabshoff]:\n> I am CCing Alex since I believe he wrote this doctest :)\n\n\nYes, sorry about that.  It won't happen again (the bad cmp test, not writing doctest in general :)",
    "created_at": "2009-05-05T06:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5983#issuecomment-47451",
    "user": "https://github.com/aghitza"
}
```

Replying to [ticket:5983 mabshoff]:
> I am CCing Alex since I believe he wrote this doctest :)


Yes, sorry about that.  It won't happen again (the bad cmp test, not writing doctest in general :)



---

archive/issue_comments_047452.json:
```json
{
    "body": "Replying to [comment:5 AlexGhitza]:\n\n> Yes, sorry about that.  It won't happen again (the bad cmp test, not writing doctest in general :)\n\n\nHehe, I didn't catch this issue while running doctests dozens if not hundred of times on sage.math and many other systems, but it just triggered once on a SkyNet box. I also found an analog problem in other places, so you aren't the only one.\n\nKeep the doctests coming ;)\n\nCheers,\n\nMichael",
    "created_at": "2009-05-05T06:33:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5983#issuecomment-47452",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:5 AlexGhitza]:

> Yes, sorry about that.  It won't happen again (the bad cmp test, not writing doctest in general :)


Hehe, I didn't catch this issue while running doctests dozens if not hundred of times on sage.math and many other systems, but it just triggered once on a SkyNet box. I also found an analog problem in other places, so you aren't the only one.

Keep the doctests coming ;)

Cheers,

Michael
