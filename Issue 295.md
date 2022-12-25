# Issue 295: '??' doesn't always print last line of last function in file

archive/issues_000295.json:
```json
{
    "body": "Assignee: @williamstein\n\nA file with this content (w/o the \"===\"'s) shows the problem:\n\n\n```\ndef Foo(x)\n    x = 1\n```\n\n\nAfter load/attaching this file, typing \"??Foo\" prints only the 'def' line.\n\nIf the file looks like this (i.e., with an 'extra' blank line):\n\n\n```\ndef Foo(x)\n    x = 1\n\n```\n\n\nthen '??' works properly.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/295\n\n",
    "created_at": "2007-02-25T18:49:28Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "title": "'??' doesn't always print last line of last function in file",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/295",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```
Assignee: @williamstein

A file with this content (w/o the "==="'s) shows the problem:


```
def Foo(x)
    x = 1
```


After load/attaching this file, typing "??Foo" prints only the 'def' line.

If the file looks like this (i.e., with an 'extra' blank line):


```
def Foo(x)
    x = 1

```


then '??' works properly.


Issue created by migration from https://trac.sagemath.org/ticket/295





---

archive/issue_comments_001392.json:
```json
{
    "body": "Ignore the \"===\"s part; forgot to remove this after fiddling with formatting.",
    "created_at": "2007-02-25T18:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/295",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/295#issuecomment-1392",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

Ignore the "==="s part; forgot to remove this after fiddling with formatting.



---

archive/issue_comments_001393.json:
```json
{
    "body": "Changing assignee from @williamstein to Nick Alexander.",
    "created_at": "2007-02-25T19:15:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/295",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/295#issuecomment-1393",
    "user": "https://github.com/williamstein"
}
```

Changing assignee from @williamstein to Nick Alexander.



---

archive/issue_comments_001394.json:
```json
{
    "body": "Changing assignee from Nick Alexander to @ncalexan.",
    "created_at": "2007-02-28T20:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/295",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/295#issuecomment-1394",
    "user": "https://github.com/ncalexan"
}
```

Changing assignee from Nick Alexander to @ncalexan.



---

archive/issue_comments_001395.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-02-28T20:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/295",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/295#issuecomment-1395",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed



---

archive/issue_comments_001396.json:
```json
{
    "body": "Fixed in ncalexan's local tree by 34c022ed2482.\n\nThis requires the doctest.ELLIPSIS option be added to local/bin/sage-doctest, so I haven't sent it upstream yet.  When I finish touching the testing infrastructure, I'll send it along, or ask for it :)",
    "created_at": "2007-02-28T20:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/295",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/295#issuecomment-1396",
    "user": "https://github.com/ncalexan"
}
```

Fixed in ncalexan's local tree by 34c022ed2482.

This requires the doctest.ELLIPSIS option be added to local/bin/sage-doctest, so I haven't sent it upstream yet.  When I finish touching the testing infrastructure, I'll send it along, or ask for it :)



---

archive/issue_events_000312.json:
```json
{
    "actor": "https://github.com/ncalexan",
    "created_at": "2007-02-28T20:33:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/295",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/295#event-312"
}
```
