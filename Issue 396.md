# Issue 396: vector-vector produc ts

archive/issues_000396.json:
```json
{
    "body": "Assignee: @williamstein\n\nMultiplying a mix of vectors and matrices is allowed presently in sage, but it is not associative:\n\n```\nv=vector([1,2,3])\nM=matrix([[1,0],[0,1],[1,1]])\nw=vector([1,2])\n\nprint v*M*w\nprint (v*M)*w\nprint v*(M*w)\n///\n(4, 10)\n(4, 10)\n(1, 4, 9)\n```\nIt is a combination of vectors not knowing whether they are row- or column vectors (probably good)\nand that v * w has the odd meaning of doing a component-wise multiplication. Perhaps it inherits the method from lists or something? It would be safest to explicitly cast an error if one tries to multiply vectors.\n\nIssue created by migration from https://trac.sagemath.org/ticket/396\n\n",
    "created_at": "2007-06-28T23:46:25Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "vector-vector produc ts",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/396",
    "user": "https://github.com/nbruin"
}
```
Assignee: @williamstein

Multiplying a mix of vectors and matrices is allowed presently in sage, but it is not associative:

```
v=vector([1,2,3])
M=matrix([[1,0],[0,1],[1,1]])
w=vector([1,2])

print v*M*w
print (v*M)*w
print v*(M*w)
///
(4, 10)
(4, 10)
(1, 4, 9)
```
It is a combination of vectors not knowing whether they are row- or column vectors (probably good)
and that v * w has the odd meaning of doing a component-wise multiplication. Perhaps it inherits the method from lists or something? It would be safest to explicitly cast an error if one tries to multiply vectors.

Issue created by migration from https://trac.sagemath.org/ticket/396





---

archive/issue_events_000950.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-08-23T14:08:02Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/396",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/396#event-950"
}
```



---

archive/issue_comments_001940.json:
```json
{
    "body": "The multiplication comes from FreeModule:\n\nsage: F = FreeModule(QQ, 3)\nsage: a = F([1,2,3])\nsage: b = F([1,2,3])\nsage: a*b\n(1, 4, 9)\n\nI think that this is wrong.",
    "created_at": "2007-09-06T17:31:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/396#issuecomment-1940",
    "user": "https://github.com/mwhansen"
}
```

The multiplication comes from FreeModule:

sage: F = FreeModule(QQ, 3)
sage: a = F([1,2,3])
sage: b = F([1,2,3])
sage: a*b
(1, 4, 9)

I think that this is wrong.



---

archive/issue_events_000951.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-06T20:59:27Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/396",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/396#event-951"
}
```



---

archive/issue_events_000952.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-06T20:59:27Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/396",
    "milestone": "sage-2.8.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/396#event-952"
}
```



---

archive/issue_comments_001941.json:
```json
{
    "body": "Changing component from algebraic geometry to linear algebra.",
    "created_at": "2007-09-06T20:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/396#issuecomment-1941",
    "user": "https://github.com/williamstein"
}
```

Changing component from algebraic geometry to linear algebra.



---

archive/issue_comments_001942.json:
```json
{
    "body": "Attachment [396.patch](tarball://root/attachments/some-uuid/ticket396/396.patch) by @mwhansen created at 2007-09-06 23:02:48",
    "created_at": "2007-09-06T23:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/396#issuecomment-1942",
    "user": "https://github.com/mwhansen"
}
```

Attachment [396.patch](tarball://root/attachments/some-uuid/ticket396/396.patch) by @mwhansen created at 2007-09-06 23:02:48



---

archive/issue_events_000953.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-07T00:04:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/396",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/396#event-953"
}
```



---

archive/issue_comments_001943.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-07T00:04:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/396#issuecomment-1943",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
