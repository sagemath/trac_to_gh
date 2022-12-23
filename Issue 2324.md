# Issue 2324: RealNumber->QQ coercion fails for NaN, infinity

archive/issues_002324.json:
```json
{
    "body": "Assignee: somebody\n\nBoth of these should raise an exception immediately.  Instead, the former crashes, and the latter takes a long time to do something (I haven't tracked down what yet).\n\n\n```\nsage: QQ(RR(0.0/0.0))\n/home/cwitty/sage/local/bin/sage-sage: line 212:  5344 Segmentation fault      sage-ipython -wthread -c \"$SAGE_STARTUP_COMMAND;\" \"$@\"\n```\n\n\n\n```\nsage: QQ(RR(1.0/0.0))\n... infinite loop?\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2324\n\n",
    "created_at": "2008-02-26T20:27:06Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "RealNumber->QQ coercion fails for NaN, infinity",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2324",
    "user": "cwitty"
}
```
Assignee: somebody

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

archive/issue_comments_015460.json:
```json
{
    "body": "Changing assignee from somebody to cwitty.",
    "created_at": "2008-02-26T20:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2324#issuecomment-15460",
    "user": "cwitty"
}
```

Changing assignee from somebody to cwitty.



---

archive/issue_comments_015461.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-26T20:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2324#issuecomment-15461",
    "user": "cwitty"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015462.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-27T03:17:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2324#issuecomment-15462",
    "user": "cwitty"
}
```

Attachment



---

archive/issue_comments_015463.json:
```json
{
    "body": "After a long build, this works for me against 2.10.3.alpha0",
    "created_at": "2008-02-27T19:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2324#issuecomment-15463",
    "user": "mhansen"
}
```

After a long build, this works for me against 2.10.3.alpha0



---

archive/issue_comments_015464.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-27T23:59:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2324#issuecomment-15464",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015465.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc0",
    "created_at": "2008-02-27T23:59:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2324#issuecomment-15465",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc0
