# Issue 3648: [with patch, needs review] complex(pari(...)) fails

archive/issues_003648.json:
```json
{
    "body": "Assignee: somebody\n\nPari gen objects should have a `__complex__` method, so that complex(...) works on them.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3648\n\n",
    "created_at": "2008-07-12T16:23:14Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.6",
    "title": "[with patch, needs review] complex(pari(...)) fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3648",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: somebody

Pari gen objects should have a `__complex__` method, so that complex(...) works on them.

Issue created by migration from https://trac.sagemath.org/ticket/3648





---

archive/issue_comments_025746.json:
```json
{
    "body": "Attachment [trac3648-gen-complex.patch](tarball://root/attachments/some-uuid/ticket3648/trac3648-gen-complex.patch) by dmharvey created at 2008-07-14 04:44:34",
    "created_at": "2008-07-14T04:44:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3648#issuecomment-25746",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [trac3648-gen-complex.patch](tarball://root/attachments/some-uuid/ticket3648/trac3648-gen-complex.patch) by dmharvey created at 2008-07-14 04:44:34



---

archive/issue_comments_025747.json:
```json
{
    "body": "Attachment [trac3648-gen-complex-2.patch](tarball://root/attachments/some-uuid/ticket3648/trac3648-gen-complex-2.patch) by dmharvey created at 2008-07-14 04:54:28",
    "created_at": "2008-07-14T04:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3648#issuecomment-25747",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [trac3648-gen-complex-2.patch](tarball://root/attachments/some-uuid/ticket3648/trac3648-gen-complex-2.patch) by dmharvey created at 2008-07-14 04:54:28



---

archive/issue_comments_025748.json:
```json
{
    "body": "I've added a further doctest to cover the case when \"complex\" doesn't make sense.\n\ncwitty: if you're happy with that, this has a positive review from me.",
    "created_at": "2008-07-14T04:55:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3648#issuecomment-25748",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

I've added a further doctest to cover the case when "complex" doesn't make sense.

cwitty: if you're happy with that, this has a positive review from me.



---

archive/issue_comments_025749.json:
```json
{
    "body": "dmharvey's patch looks good to me, and doctests pass in sage/libs/pari.",
    "created_at": "2008-07-16T04:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3648#issuecomment-25749",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

dmharvey's patch looks good to me, and doctests pass in sage/libs/pari.



---

archive/issue_comments_025750.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-16T04:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3648#issuecomment-25750",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025751.json:
```json
{
    "body": "Merged in Sage 3.0.6.alpha0",
    "created_at": "2008-07-16T04:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3648#issuecomment-25751",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.6.alpha0
