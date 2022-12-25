# Issue 5907: [with patch; needs review] incorrect fast_float evaluation of constant polynomials

archive/issues_005907.json:
```json
{
    "body": "Assignee: @tornaria\n\nKeywords: fast_float\n\nA constant polynomial `a` is incorrectly `_fast_float_`- evaluated as `a*x`:\n\n```\nsage: R.<t> = QQ[]\nsage: f = t + 2 - t\nsage: ff = f._fast_float_()\nsage: ff(3)\n6.0\nsage: list(ff)\n['load 0', 'push 2.0', 'mul']\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5907\n\n",
    "created_at": "2009-04-27T01:10:19Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch; needs review] incorrect fast_float evaluation of constant polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5907",
    "user": "https://github.com/tornaria"
}
```
Assignee: @tornaria

Keywords: fast_float

A constant polynomial `a` is incorrectly `_fast_float_`- evaluated as `a*x`:

```
sage: R.<t> = QQ[]
sage: f = t + 2 - t
sage: ff = f._fast_float_()
sage: ff(3)
6.0
sage: list(ff)
['load 0', 'push 2.0', 'mul']
```

Issue created by migration from https://trac.sagemath.org/ticket/5907





---

archive/issue_comments_046600.json:
```json
{
    "body": "Fix fast_float evaluation of constant polynomials",
    "created_at": "2009-04-27T01:13:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5907#issuecomment-46600",
    "user": "https://github.com/tornaria"
}
```

Fix fast_float evaluation of constant polynomials



---

archive/issue_comments_046601.json:
```json
{
    "body": "Attachment [trac_5907.patch](tarball://root/attachments/some-uuid/ticket5907/trac_5907.patch) by cwitty created at 2009-04-27 16:45:15",
    "created_at": "2009-04-27T16:45:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5907#issuecomment-46601",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac_5907.patch](tarball://root/attachments/some-uuid/ticket5907/trac_5907.patch) by cwitty created at 2009-04-27 16:45:15



---

archive/issue_comments_046602.json:
```json
{
    "body": "Attachment [trac5907-part2-fast-callable.patch](tarball://root/attachments/some-uuid/ticket5907/trac5907-part2-fast-callable.patch) by cwitty created at 2009-04-27 16:47:29\n\nPositive review for the original patch (code looks good, doctests pass).  Unfortunately _fast_callable_ copied the buggy code; seems like we might as well fix both bugs on the same ticket, so I've added a second patch to fix the _fast_callable_ bug.  (So this second patch needs review.)",
    "created_at": "2009-04-27T16:47:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5907#issuecomment-46602",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac5907-part2-fast-callable.patch](tarball://root/attachments/some-uuid/ticket5907/trac5907-part2-fast-callable.patch) by cwitty created at 2009-04-27 16:47:29

Positive review for the original patch (code looks good, doctests pass).  Unfortunately _fast_callable_ copied the buggy code; seems like we might as well fix both bugs on the same ticket, so I've added a second patch to fix the _fast_callable_ bug.  (So this second patch needs review.)



---

archive/issue_comments_046603.json:
```json
{
    "body": "Positive review for cwitty's change.",
    "created_at": "2009-05-19T05:04:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5907#issuecomment-46603",
    "user": "https://github.com/mwhansen"
}
```

Positive review for cwitty's change.



---

archive/issue_events_013857.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-19T19:08:19Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5907",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5907#event-13857"
}
```



---

archive/issue_comments_046604.json:
```json
{
    "body": "Merged both patches in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T19:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5907#issuecomment-46604",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_events_013858.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-19T19:08:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5907",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5907#event-13858"
}
```



---

archive/issue_comments_046605.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-19T19:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5907#issuecomment-46605",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
