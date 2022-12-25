# Issue 2324: [with patch, positive review] RealNumber->QQ coercion fails for NaN, infinity

archive/issues_002324.json:
```json
{
    "body": "Assignee: cwitty\n\nBoth of these should raise an exception immediately.  Instead, the former crashes, and the latter takes a long time to do something (I haven't tracked down what yet).\n\n```\nsage: QQ(RR(0.0/0.0))\n/home/cwitty/sage/local/bin/sage-sage: line 212:  5344 Segmentation fault      sage-ipython -wthread -c \"$SAGE_STARTUP_COMMAND;\" \"$@\"\n```\n\n```\nsage: QQ(RR(1.0/0.0))\n... infinite loop?\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2324\n\n",
    "closed_at": "2008-02-27T23:59:16Z",
    "created_at": "2008-02-26T20:27:06Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "[with patch, positive review] RealNumber->QQ coercion fails for NaN, infinity",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2324",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: cwitty

Both of these should raise an exception immediately.  Instead, the former crashes, and the latter takes a long time to do something (I haven't tracked down what yet).

```
sage: QQ(RR(0.0/0.0))
/home/cwitty/sage/local/bin/sage-sage: line 212:  5344 Segmentation fault      sage-ipython -wthread -c "$SAGE_STARTUP_COMMAND;" "$@"
```

```
sage: QQ(RR(1.0/0.0))
... infinite loop?
```


Issue created by migration from https://trac.sagemath.org/ticket/2324





---

archive/issue_comments_015426.json:
```json
{
    "body": "Changing assignee from somebody to cwitty.",
    "created_at": "2008-02-26T20:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2324#issuecomment-15426",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing assignee from somebody to cwitty.



---

archive/issue_comments_015427.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-26T20:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2324#issuecomment-15427",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015428.json:
```json
{
    "body": "Attachment [rr-qq-coercion-crash.patch](tarball://root/attachments/some-uuid/ticket2324/rr-qq-coercion-crash.patch) by cwitty created at 2008-02-27 03:17:10",
    "created_at": "2008-02-27T03:17:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2324#issuecomment-15428",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [rr-qq-coercion-crash.patch](tarball://root/attachments/some-uuid/ticket2324/rr-qq-coercion-crash.patch) by cwitty created at 2008-02-27 03:17:10



---

archive/issue_comments_015429.json:
```json
{
    "body": "After a long build, this works for me against 2.10.3.alpha0",
    "created_at": "2008-02-27T19:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2324#issuecomment-15429",
    "user": "https://github.com/mwhansen"
}
```

After a long build, this works for me against 2.10.3.alpha0



---

archive/issue_comments_015430.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-27T23:59:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2324#issuecomment-15430",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005472.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-27T23:59:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2324",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2324#event-5472"
}
```



---

archive/issue_comments_015431.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc0",
    "created_at": "2008-02-27T23:59:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2324#issuecomment-15431",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc0
