# Issue 2793: [with patch; with positive review] Bug in the sage preparser!  "\"Yes,\" he said."

archive/issues_002793.json:
```json
{
    "body": "Assignee: cwitty\n\nIn the Python tutorial (http://docs.python.org/tut/node5.html#SECTION005120000000000000000)\n there's an example of making a string:\n\n```\n>>> \"\\\"Yes,\\\" he said.\"\n'\"Yes,\" he said.'\n```\n\nThis fails in Sage because of the preparser!\n\n```\nsage: \"\\\"Yes,\\\" he said.\"\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\n     \"\\\"Yes,._backslash_()\" he said.\"\n                             ^\n<type 'exceptions.SyntaxError'>: invalid syntax\n```\n\nThis is obviously a bug in the _backslash_ or \"in quotes\" part of the preparser.  So it's almost certainly my fault.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2793\n\n",
    "closed_at": "2008-04-04T21:27:04Z",
    "created_at": "2008-04-04T00:44:28Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch; with positive review] Bug in the sage preparser!  \"\\\"Yes,\\\" he said.\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2793",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty

In the Python tutorial (http://docs.python.org/tut/node5.html#SECTION005120000000000000000)
 there's an example of making a string:

```
>>> "\"Yes,\" he said."
'"Yes," he said.'
```

This fails in Sage because of the preparser!

```
sage: "\"Yes,\" he said."
------------------------------------------------------------
   File "<ipython console>", line 1
     "\"Yes,._backslash_()" he said."
                             ^
<type 'exceptions.SyntaxError'>: invalid syntax
```

This is obviously a bug in the _backslash_ or "in quotes" part of the preparser.  So it's almost certainly my fault.


Issue created by migration from https://trac.sagemath.org/ticket/2793





---

archive/issue_comments_019137.json:
```json
{
    "body": "Attachment [sage-2793.2.patch](tarball://root/attachments/some-uuid/ticket2793/sage-2793.2.patch) by @williamstein created at 2008-04-04 01:09:42",
    "created_at": "2008-04-04T01:09:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2793#issuecomment-19137",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2793.2.patch](tarball://root/attachments/some-uuid/ticket2793/sage-2793.2.patch) by @williamstein created at 2008-04-04 01:09:42



---

archive/issue_comments_019138.json:
```json
{
    "body": "Breaks on `s = \"\\\\\"`.",
    "created_at": "2008-04-04T07:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2793#issuecomment-19138",
    "user": "https://github.com/robertwb"
}
```

Breaks on `s = "\\"`.



---

archive/issue_comments_019139.json:
```json
{
    "body": "Attachment [sage-2793-part2.patch](tarball://root/attachments/some-uuid/ticket2793/sage-2793-part2.patch) by @williamstein created at 2008-04-04 19:00:33",
    "created_at": "2008-04-04T19:00:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2793#issuecomment-19139",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2793-part2.patch](tarball://root/attachments/some-uuid/ticket2793/sage-2793-part2.patch) by @williamstein created at 2008-04-04 19:00:33



---

archive/issue_comments_019140.json:
```json
{
    "body": "I've attached a part 2 patch which addresses the referee's (nick's) comments.",
    "created_at": "2008-04-04T19:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2793#issuecomment-19140",
    "user": "https://github.com/williamstein"
}
```

I've attached a part 2 patch which addresses the referee's (nick's) comments.



---

archive/issue_comments_019141.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-04T19:23:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2793#issuecomment-19141",
    "user": "https://github.com/robertwb"
}
```

Looks good to me.



---

archive/issue_comments_019142.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-04T21:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2793#issuecomment-19142",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006447.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-04T21:27:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2793",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2793#event-6447"
}
```



---

archive/issue_comments_019143.json:
```json
{
    "body": "Merged both patches in Sage 3.0.alpha1",
    "created_at": "2008-04-04T21:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2793#issuecomment-19143",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.0.alpha1
