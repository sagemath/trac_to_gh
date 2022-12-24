# Issue 2793: Bug in the sage preparser!  "\"Yes,\" he said."

archive/issues_002793.json:
```json
{
    "body": "Assignee: cwitty\n\nIn the Python tutorial (http://docs.python.org/tut/node5.html#SECTION005120000000000000000)\n there's an example of making a string:\n\n```\n>>> \"\\\"Yes,\\\" he said.\"\n'\"Yes,\" he said.'\n```\n\n\nThis fails in Sage because of the preparser!\n\n\n```\nsage: \"\\\"Yes,\\\" he said.\"\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\n     \"\\\"Yes,._backslash_()\" he said.\"\n                             ^\n<type 'exceptions.SyntaxError'>: invalid syntax\n```\n\n\nThis is obviously a bug in the _backslash_ or \"in quotes\" part of the preparser.  So it's almost certainly my fault.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2793\n\n",
    "created_at": "2008-04-04T00:44:28Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Bug in the sage preparser!  \"\\\"Yes,\\\" he said.\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2793",
    "user": "was"
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

archive/issue_comments_019178.json:
```json
{
    "body": "Attachment [sage-2793.2.patch](tarball://root/attachments/some-uuid/ticket2793/sage-2793.2.patch) by was created at 2008-04-04 01:09:42",
    "created_at": "2008-04-04T01:09:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2793#issuecomment-19178",
    "user": "was"
}
```

Attachment [sage-2793.2.patch](tarball://root/attachments/some-uuid/ticket2793/sage-2793.2.patch) by was created at 2008-04-04 01:09:42



---

archive/issue_comments_019179.json:
```json
{
    "body": "Breaks on `s = \"\\\\\"`.",
    "created_at": "2008-04-04T07:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2793#issuecomment-19179",
    "user": "robertwb"
}
```

Breaks on `s = "\\"`.



---

archive/issue_comments_019180.json:
```json
{
    "body": "Attachment [sage-2793-part2.patch](tarball://root/attachments/some-uuid/ticket2793/sage-2793-part2.patch) by was created at 2008-04-04 19:00:33",
    "created_at": "2008-04-04T19:00:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2793#issuecomment-19180",
    "user": "was"
}
```

Attachment [sage-2793-part2.patch](tarball://root/attachments/some-uuid/ticket2793/sage-2793-part2.patch) by was created at 2008-04-04 19:00:33



---

archive/issue_comments_019181.json:
```json
{
    "body": "I've attached a part 2 patch which addresses the referee's (nick's) comments.",
    "created_at": "2008-04-04T19:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2793#issuecomment-19181",
    "user": "was"
}
```

I've attached a part 2 patch which addresses the referee's (nick's) comments.



---

archive/issue_comments_019182.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-04T19:23:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2793#issuecomment-19182",
    "user": "robertwb"
}
```

Looks good to me.



---

archive/issue_comments_019183.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-04T21:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2793#issuecomment-19183",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019184.json:
```json
{
    "body": "Merged both patches in Sage 3.0.alpha1",
    "created_at": "2008-04-04T21:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2793#issuecomment-19184",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.0.alpha1
