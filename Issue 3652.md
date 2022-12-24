# Issue 3652: [with patch, needs review] FreeModule(ZZ, 2000).random_element() is far slower than it should be

archive/issues_003652.json:
```json
{
    "body": "Assignee: was\n\nCurrently, random_element on a `FreeModule` constructs a basis, even if we know the basis is trivial.  The attached patch fixes this for `FreeModule_ambient` and subclasses.\n\nBefore:\n\n```\nsage: K = FreeModule(ZZ, 2000)\nsage: get_memory_usage()\n118.60546875\nsage: %time _ = K.random_element()\nCPU times: user 1.45 s, sys: 0.12 s, total: 1.57 s\nWall time: 1.57 s\nsage: get_memory_usage()\n225.56640625\n```\n\n\nAfter:\n\n```\nsage: K = FreeModule(ZZ, 2000)\nsage: get_memory_usage()\n118.60546875\nsage: %time _ = K.random_element()\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\nsage: get_memory_usage()\n118.60546875\nsage: timeit('K.random_element()')\n125 loops, best of 3: 2.32 ms per loop\n```\n\n\nA 600-fold speedup.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3652\n\n",
    "created_at": "2008-07-13T22:19:27Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with patch, needs review] FreeModule(ZZ, 2000).random_element() is far slower than it should be",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3652",
    "user": "cwitty"
}
```
Assignee: was

Currently, random_element on a `FreeModule` constructs a basis, even if we know the basis is trivial.  The attached patch fixes this for `FreeModule_ambient` and subclasses.

Before:

```
sage: K = FreeModule(ZZ, 2000)
sage: get_memory_usage()
118.60546875
sage: %time _ = K.random_element()
CPU times: user 1.45 s, sys: 0.12 s, total: 1.57 s
Wall time: 1.57 s
sage: get_memory_usage()
225.56640625
```


After:

```
sage: K = FreeModule(ZZ, 2000)
sage: get_memory_usage()
118.60546875
sage: %time _ = K.random_element()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: get_memory_usage()
118.60546875
sage: timeit('K.random_element()')
125 loops, best of 3: 2.32 ms per loop
```


A 600-fold speedup.

Issue created by migration from https://trac.sagemath.org/ticket/3652





---

archive/issue_comments_025827.json:
```json
{
    "body": "Attachment [trac3652-free-module-random-speedup.patch](tarball://root/attachments/some-uuid/ticket3652/trac3652-free-module-random-speedup.patch) by ncalexan created at 2008-08-10 20:14:46\n\nApplies nicely and does speed up the operation on my system.",
    "created_at": "2008-08-10T20:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3652#issuecomment-25827",
    "user": "ncalexan"
}
```

Attachment [trac3652-free-module-random-speedup.patch](tarball://root/attachments/some-uuid/ticket3652/trac3652-free-module-random-speedup.patch) by ncalexan created at 2008-08-10 20:14:46

Applies nicely and does speed up the operation on my system.



---

archive/issue_comments_025828.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-10T22:52:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3652#issuecomment-25828",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025829.json:
```json
{
    "body": "Merged in Sage 3.1.alpha1",
    "created_at": "2008-08-10T22:52:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3652#issuecomment-25829",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha1
