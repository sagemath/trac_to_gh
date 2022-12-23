# Issue 2345: negative indicies in vectors

archive/issues_002345.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: vector(RR,range(3))[2]\n 2.00000000000000\n\nsage: vector(RR,range(3))[-1]\n----------------------------------------------------\n\n/home/dfdeshom/custom/sage/devel/sage-gcd2/<ipython\nconsole> in <module>()\n\n/home/dfdeshom/custom/sage/devel/sage-gcd2/free_modu\nle_element.pyx in sage.modules.free_module_element.F\nreeModuleElement_generic_dense.__getitem__()\n\n<type 'exceptions.IndexError'>: index (i=-1) must be\n between 0 and 2\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2345\n\n",
    "created_at": "2008-02-28T08:47:58Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "negative indicies in vectors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2345",
    "user": "mhansen"
}
```
Assignee: was


```
sage: vector(RR,range(3))[2]
 2.00000000000000

sage: vector(RR,range(3))[-1]
----------------------------------------------------

/home/dfdeshom/custom/sage/devel/sage-gcd2/<ipython
console> in <module>()

/home/dfdeshom/custom/sage/devel/sage-gcd2/free_modu
le_element.pyx in sage.modules.free_module_element.F
reeModuleElement_generic_dense.__getitem__()

<type 'exceptions.IndexError'>: index (i=-1) must be
 between 0 and 2
```


Issue created by migration from https://trac.sagemath.org/ticket/2345





---

archive/issue_comments_015703.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2008-02-28T09:36:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2345#issuecomment-15703",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_015704.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-28T09:36:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2345#issuecomment-15704",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_015705.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-28T09:36:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2345#issuecomment-15705",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015706.json:
```json
{
    "body": "The patch looks great, thanks!",
    "created_at": "2008-02-28T14:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2345#issuecomment-15706",
    "user": "dfdeshom"
}
```

The patch looks great, thanks!



---

archive/issue_comments_015707.json:
```json
{
    "body": "There was a long discussion about it and in the end the patch was voted in in the thread:\n\nhttps://groups.google.com/group/sage-devel/browse_thread/thread/0aadcca5557ea45a/80148bb28bec02d1#80148bb28bec02d1\n\nCheers,\n\nMichael",
    "created_at": "2008-03-03T02:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2345#issuecomment-15707",
    "user": "mabshoff"
}
```

There was a long discussion about it and in the end the patch was voted in in the thread:

https://groups.google.com/group/sage-devel/browse_thread/thread/0aadcca5557ea45a/80148bb28bec02d1#80148bb28bec02d1

Cheers,

Michael



---

archive/issue_comments_015708.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-03T02:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2345#issuecomment-15708",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015709.json:
```json
{
    "body": "Merged in 2.10.3.rc1.",
    "created_at": "2008-03-03T03:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2345#issuecomment-15709",
    "user": "mhansen"
}
```

Merged in 2.10.3.rc1.
