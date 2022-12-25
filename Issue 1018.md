# Issue 1018: Change prod() to used balanced tree

archive/issues_001018.json:
```json
{
    "body": "Assignee: somebody\n\nComputing a*b*c*d as (a*b)*(c*d) rather than ((a*b)*c)*d can take better advantage of asymptotically fast multiplication. On the other hand the latter can take better advantage of inplace operators and has less overhead. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1018\n\n",
    "created_at": "2007-10-28T08:09:45Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.10",
    "title": "Change prod() to used balanced tree",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1018",
    "user": "https://github.com/robertwb"
}
```
Assignee: somebody

Computing a*b*c*d as (a*b)*(c*d) rather than ((a*b)*c)*d can take better advantage of asymptotically fast multiplication. On the other hand the latter can take better advantage of inplace operators and has less overhead. 

Issue created by migration from https://trac.sagemath.org/ticket/1018





---

archive/issue_comments_006222.json:
```json
{
    "body": "Changing assignee from somebody to @robertwb.",
    "created_at": "2007-10-28T08:16:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1018#issuecomment-6222",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from somebody to @robertwb.



---

archive/issue_comments_006223.json:
```json
{
    "body": "This patch computes the product in a balanced way down to a certain level (default 5) and can be much faster. Only associativity (not commutativity) is assumed. \n\n\n```\nsage: time a = prod([1..50000])\nCPU times: user 0.08 s, sys: 0.01 s, total: 0.08 s\nWall time: 0.08\nsage: time L = [1..50000]\nCPU times: user 0.02 s, sys: 0.00 s, total: 0.03 s\nWall time: 0.03\n\n```\n\n\nvs a generator (which is multiplied in order)\n\n\n```\nsage: time a = prod(1..50000)\nCPU times: user 1.11 s, sys: 0.00 s, total: 1.12 s\nWall time: 1.12\nsage: time L = list(1..50000)\nCPU times: user 0.18 s, sys: 0.00 s, total: 0.19 s\nWall time: 0.19\n```\n\n\nThere is also a class sage.misc.misc_c.NonAssociative to see the exact product tree. \n\n```\nsage: from sage.misc.misc_c import NonAssociative\nsage: L = [NonAssociative(label) for label in 'abcdef']\nsage: prod(L)\n(((a*b)*c)*((d*e)*f))\n```\n",
    "created_at": "2007-10-28T08:16:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1018#issuecomment-6223",
    "user": "https://github.com/robertwb"
}
```

This patch computes the product in a balanced way down to a certain level (default 5) and can be much faster. Only associativity (not commutativity) is assumed. 


```
sage: time a = prod([1..50000])
CPU times: user 0.08 s, sys: 0.01 s, total: 0.08 s
Wall time: 0.08
sage: time L = [1..50000]
CPU times: user 0.02 s, sys: 0.00 s, total: 0.03 s
Wall time: 0.03

```


vs a generator (which is multiplied in order)


```
sage: time a = prod(1..50000)
CPU times: user 1.11 s, sys: 0.00 s, total: 1.12 s
Wall time: 1.12
sage: time L = list(1..50000)
CPU times: user 0.18 s, sys: 0.00 s, total: 0.19 s
Wall time: 0.19
```


There is also a class sage.misc.misc_c.NonAssociative to see the exact product tree. 

```
sage: from sage.misc.misc_c import NonAssociative
sage: L = [NonAssociative(label) for label in 'abcdef']
sage: prod(L)
(((a*b)*c)*((d*e)*f))
```




---

archive/issue_comments_006224.json:
```json
{
    "body": "Attachment [balanced-prod-1018.patch](tarball://root/attachments/some-uuid/ticket1018/balanced-prod-1018.patch) by @robertwb created at 2007-10-28 08:18:13",
    "created_at": "2007-10-28T08:18:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1018#issuecomment-6224",
    "user": "https://github.com/robertwb"
}
```

Attachment [balanced-prod-1018.patch](tarball://root/attachments/some-uuid/ticket1018/balanced-prod-1018.patch) by @robertwb created at 2007-10-28 08:18:13



---

archive/issue_events_001142.json:
```json
{
    "actor": "cwitty",
    "created_at": "2007-10-28T18:08:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1018",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1018#event-1142"
}
```



---

archive/issue_comments_006225.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-28T18:08:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1018#issuecomment-6225",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Resolution: fixed
