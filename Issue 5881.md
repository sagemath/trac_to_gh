# Issue 5881: __cmp__ is random-ish in root_system/type_dual.py also (analog to #5811)

archive/issues_005881.json:
```json
{
    "body": "Assignee: @mwhansen\n\nThis is happening with gcc 4.3.3:\n\n```\nsage -t  \"devel/sage/sage/combinat/root_system/type_dual.py\"\n**********************************************************************\nFile \"/home/mariah/sage/sage-3.4.1-x86_64-Linux-fc/devel/sage/sage/combinat/root\n_system/type_dual.py\", line 43:\n   sage: [[x.__cmp__(y) for x in ct] for y in ct]\nExpected:\n   [[0, 1, -1], [-1, 0, -1], [1, 1, 0]]\nGot:\n   [[0, 1, 1], [-1, 0, 1], [1, 1, 0]]\n**********************************************************************\nFile \"/home/mariah/sage/sage-3.4.1-x86_64-Linux-fc/devel/sage/sage/combinat/root\n_system/type_dual.py\", line 45:\n   sage: sorted(ct)\nExpected:\n   [['A', 4], A1xB2, B2xA1]\nGot:\n   [A1xB2, B2xA1, ['A', 4]]\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5881\n\n",
    "created_at": "2009-04-23T21:10:28Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "__cmp__ is random-ish in root_system/type_dual.py also (analog to #5811)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5881",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @mwhansen

This is happening with gcc 4.3.3:

```
sage -t  "devel/sage/sage/combinat/root_system/type_dual.py"
**********************************************************************
File "/home/mariah/sage/sage-3.4.1-x86_64-Linux-fc/devel/sage/sage/combinat/root
_system/type_dual.py", line 43:
   sage: [[x.__cmp__(y) for x in ct] for y in ct]
Expected:
   [[0, 1, -1], [-1, 0, -1], [1, 1, 0]]
Got:
   [[0, 1, 1], [-1, 0, 1], [1, 1, 0]]
**********************************************************************
File "/home/mariah/sage/sage-3.4.1-x86_64-Linux-fc/devel/sage/sage/combinat/root
_system/type_dual.py", line 45:
   sage: sorted(ct)
Expected:
   [['A', 4], A1xB2, B2xA1]
Got:
   [A1xB2, B2xA1, ['A', 4]]
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/5881





---

archive/issue_comments_046382.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-30T07:52:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5881#issuecomment-46382",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046383.json:
```json
{
    "body": "Attachment [trac_5881.patch](tarball://root/attachments/some-uuid/ticket5881/trac_5881.patch) by @mwhansen created at 2009-04-30 07:52:32",
    "created_at": "2009-04-30T07:52:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5881#issuecomment-46383",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_5881.patch](tarball://root/attachments/some-uuid/ticket5881/trac_5881.patch) by @mwhansen created at 2009-04-30 07:52:32



---

archive/issue_comments_046384.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T09:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5881#issuecomment-46384",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_046385.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-30T09:43:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5881#issuecomment-46385",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006137.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-04-30T09:43:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5881",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5881#event-6137"
}
```



---

archive/issue_comments_046386.json:
```json
{
    "body": "Mrged in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T09:43:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5881#issuecomment-46386",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Mrged in Sage 3.4.2.rc0.

Cheers,

Michael
