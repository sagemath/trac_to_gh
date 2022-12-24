# Issue 3648: [with patch, needs review] complex(pari(...)) fails

archive/issues_003648.json:
```json
{
    "body": "Assignee: somebody\n\nPari gen objects should have a `__complex__` method, so that complex(...) works on them.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3648\n\n",
    "created_at": "2008-07-12T16:23:14Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.6",
    "title": "[with patch, needs review] complex(pari(...)) fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3648",
    "user": "cwitty"
}
```
Assignee: somebody

Pari gen objects should have a `__complex__` method, so that complex(...) works on them.

Issue created by migration from https://trac.sagemath.org/ticket/3648





---

archive/issue_comments_025800.json:
```json
{
    "body": "Attachment [trac3648-gen-complex.patch](tarball://root/attachments/some-uuid/ticket3648/trac3648-gen-complex.patch) by dmharvey created at 2008-07-14 04:44:34",
    "created_at": "2008-07-14T04:44:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3648#issuecomment-25800",
    "user": "dmharvey"
}
```

Attachment [trac3648-gen-complex.patch](tarball://root/attachments/some-uuid/ticket3648/trac3648-gen-complex.patch) by dmharvey created at 2008-07-14 04:44:34



---

archive/issue_comments_025801.json:
```json
{
    "body": "Attachment [trac3648-gen-complex-2.patch](tarball://root/attachments/some-uuid/ticket3648/trac3648-gen-complex-2.patch) by dmharvey created at 2008-07-14 04:54:28",
    "created_at": "2008-07-14T04:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3648#issuecomment-25801",
    "user": "dmharvey"
}
```

Attachment [trac3648-gen-complex-2.patch](tarball://root/attachments/some-uuid/ticket3648/trac3648-gen-complex-2.patch) by dmharvey created at 2008-07-14 04:54:28



---

archive/issue_comments_025802.json:
```json
{
    "body": "I've added a further doctest to cover the case when \"complex\" doesn't make sense.\n\ncwitty: if you're happy with that, this has a positive review from me.",
    "created_at": "2008-07-14T04:55:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3648#issuecomment-25802",
    "user": "dmharvey"
}
```

I've added a further doctest to cover the case when "complex" doesn't make sense.

cwitty: if you're happy with that, this has a positive review from me.



---

archive/issue_comments_025803.json:
```json
{
    "body": "dmharvey's patch looks good to me, and doctests pass in sage/libs/pari.",
    "created_at": "2008-07-16T04:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3648#issuecomment-25803",
    "user": "cwitty"
}
```

dmharvey's patch looks good to me, and doctests pass in sage/libs/pari.



---

archive/issue_comments_025804.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-16T04:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3648#issuecomment-25804",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025805.json:
```json
{
    "body": "Merged in Sage 3.0.6.alpha0",
    "created_at": "2008-07-16T04:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3648#issuecomment-25805",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.6.alpha0
