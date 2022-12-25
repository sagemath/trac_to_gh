# Issue 3933: Set iteration is broken over sets created with iterators

archive/issues_003933.json:
```json
{
    "body": "Assignee: cwitty\n\nThis works:\n\nsage: list(Set([1, 2, 3, 4, 5]))\n[1, 2, 3, 4, 5]\n\nBut this doesn't:\n\nsage: list(Set(iter([1, 2, 3, 4, 5])))\n[]\n\nBasically Set makes a Set_object() out of it and Set_object is really not prepared to deal with an iterator.  I glanced over the code and did find an obvious solution.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3933\n\n",
    "created_at": "2008-08-22T19:12:05Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Set iteration is broken over sets created with iterators",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3933",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```
Assignee: cwitty

This works:

sage: list(Set([1, 2, 3, 4, 5]))
[1, 2, 3, 4, 5]

But this doesn't:

sage: list(Set(iter([1, 2, 3, 4, 5])))
[]

Basically Set makes a Set_object() out of it and Set_object is really not prepared to deal with an iterator.  I glanced over the code and did find an obvious solution.

Issue created by migration from https://trac.sagemath.org/ticket/3933





---

archive/issue_comments_028117.json:
```json
{
    "body": "The examples should read\n\n\n```\nsage: list(Set([1, 2, 3, 4, 5]))\n[1, 2, 3, 4, 5]\n```\n\n\nand \n\n\n```\nsage: list(Set(iter([1, 2, 3, 4, 5])))\n[]\n```\n",
    "created_at": "2008-08-22T19:13:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3933#issuecomment-28117",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

The examples should read


```
sage: list(Set([1, 2, 3, 4, 5]))
[1, 2, 3, 4, 5]
```


and 


```
sage: list(Set(iter([1, 2, 3, 4, 5])))
[]
```




---

archive/issue_comments_028118.json:
```json
{
    "body": "amusingly:\n\n\n```\nsage: list(Set(iter([1, 2, 3, 4, 5])))\n[]\nsage: list(Set(set(iter([1, 2, 3, 4, 5]))))\n[1, 2, 3, 4, 5]\n```\n",
    "created_at": "2009-01-23T14:00:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3933#issuecomment-28118",
    "user": "https://github.com/rlmill"
}
```

amusingly:


```
sage: list(Set(iter([1, 2, 3, 4, 5])))
[]
sage: list(Set(set(iter([1, 2, 3, 4, 5]))))
[1, 2, 3, 4, 5]
```




---

archive/issue_comments_028119.json:
```json
{
    "body": "Also, I was worried about giving it an infinite iterator, but it seems Python is happy to shoot itself in the foot:\n\n\n```\nsage: set(Primes())\n<wait approximately forever for nothing to happen>\n```\n",
    "created_at": "2009-01-23T14:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3933#issuecomment-28119",
    "user": "https://github.com/rlmill"
}
```

Also, I was worried about giving it an infinite iterator, but it seems Python is happy to shoot itself in the foot:


```
sage: set(Primes())
<wait approximately forever for nothing to happen>
```




---

archive/issue_comments_028120.json:
```json
{
    "body": "Attachment [trac-3933.patch](tarball://root/attachments/some-uuid/ticket3933/trac-3933.patch) by @rlmill created at 2009-01-23 14:13:26",
    "created_at": "2009-01-23T14:13:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3933#issuecomment-28120",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac-3933.patch](tarball://root/attachments/some-uuid/ticket3933/trac-3933.patch) by @rlmill created at 2009-01-23 14:13:26



---

archive/issue_comments_028121.json:
```json
{
    "body": "This works and passes tests.  So I give it a positive review.",
    "created_at": "2009-01-24T03:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3933#issuecomment-28121",
    "user": "https://trac.sagemath.org/admin/accounts/users/abergeron"
}
```

This works and passes tests.  So I give it a positive review.



---

archive/issue_comments_028122.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-25T20:59:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3933#issuecomment-28122",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028123.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3",
    "created_at": "2009-01-25T20:59:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3933#issuecomment-28123",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha3



---

archive/issue_events_004162.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-25T20:59:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3933",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3933#event-4162"
}
```
