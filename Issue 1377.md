# Issue 1377: [with patch] technically incorrect code in integer_mod.pyx

archive/issues_001377.json:
```json
{
    "body": "Assignee: @williamstein\n\nThere is code in integer_mod.pyx that coerces a Python int into an int_fast32_t.  This is wrong, since a Python int can hold a C long; so this might truncate if sizeof(int_fast32_t) < sizeof(long).\n\nHowever, the bug has little or no practical effect, since:\n1) on 64-bit x86 Linux, sizeof(int_fast32_t) == sizeof(long);\n2) the problem only occurs if you call `IntegerMod_int` directly (which nobody should); it looks like all the wrappers do the modulo before they create the `IntegerMod_int`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1377\n\n",
    "created_at": "2007-12-03T00:02:29Z",
    "labels": [
        "component: algebraic geometry",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "[with patch] technically incorrect code in integer_mod.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1377",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

There is code in integer_mod.pyx that coerces a Python int into an int_fast32_t.  This is wrong, since a Python int can hold a C long; so this might truncate if sizeof(int_fast32_t) < sizeof(long).

However, the bug has little or no practical effect, since:
1) on 64-bit x86 Linux, sizeof(int_fast32_t) == sizeof(long);
2) the problem only occurs if you call `IntegerMod_int` directly (which nobody should); it looks like all the wrappers do the modulo before they create the `IntegerMod_int`.

Issue created by migration from https://trac.sagemath.org/ticket/1377





---

archive/issue_comments_008809.json:
```json
{
    "body": "Attachment [1377.patch](tarball://root/attachments/some-uuid/ticket1377/1377.patch) by cwitty created at 2007-12-03 00:03:44",
    "created_at": "2007-12-03T00:03:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1377#issuecomment-8809",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [1377.patch](tarball://root/attachments/some-uuid/ticket1377/1377.patch) by cwitty created at 2007-12-03 00:03:44



---

archive/issue_comments_008810.json:
```json
{
    "body": "Changing assignee from @williamstein to somebody.",
    "created_at": "2007-12-04T08:13:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1377#issuecomment-8810",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from @williamstein to somebody.



---

archive/issue_comments_008811.json:
```json
{
    "body": "Changing component from algebraic geometry to basic arithmetic.",
    "created_at": "2007-12-04T08:13:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1377#issuecomment-8811",
    "user": "https://github.com/robertwb"
}
```

Changing component from algebraic geometry to basic arithmetic.



---

archive/issue_comments_008812.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2007-12-04T08:13:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1377#issuecomment-8812",
    "user": "https://github.com/robertwb"
}
```

Looks good to me.



---

archive/issue_comments_008813.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-06T02:15:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1377#issuecomment-8813",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_008814.json:
```json
{
    "body": "Merged in 2.9.alpha0.",
    "created_at": "2007-12-06T02:15:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1377#issuecomment-8814",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.alpha0.



---

archive/issue_events_003558.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-06T02:15:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1377",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1377#event-3558"
}
```
