# Issue 2587: [with 2-line patch, needs review] subgroup of a permutation group is so slow it's silly

archive/issues_002587.json:
```json
{
    "body": "Assignee: joyner\n\nThe setup:\n\n```\nsage: C = QuadraticResidueCode(7, GF(2))\nsage: G = C.permutation_automorphism_group()\nsage: G.order()\n168\n```\n\nBefore:\n\n```\nsage: time SG = G.subgroup(list(G.gens()[:3]))\nCPU times: user 0.86 s, sys: 0.34 s, total: 1.20 s\nWall time: 1.24\n```\n\nAfter:\n\n```\nsage: time SG = G.subgroup(list(G.gens()[:3]))\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2587\n\n",
    "created_at": "2008-03-18T17:07:41Z",
    "labels": [
        "component: group theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with 2-line patch, needs review] subgroup of a permutation group is so slow it's silly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2587",
    "user": "https://github.com/rlmill"
}
```
Assignee: joyner

The setup:

```
sage: C = QuadraticResidueCode(7, GF(2))
sage: G = C.permutation_automorphism_group()
sage: G.order()
168
```

Before:

```
sage: time SG = G.subgroup(list(G.gens()[:3]))
CPU times: user 0.86 s, sys: 0.34 s, total: 1.20 s
Wall time: 1.24
```

After:

```
sage: time SG = G.subgroup(list(G.gens()[:3]))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
```


Issue created by migration from https://trac.sagemath.org/ticket/2587





---

archive/issue_comments_017670.json:
```json
{
    "body": "Attachment [2587-subgroups-are-slow.patch](tarball://root/attachments/some-uuid/ticket2587/2587-subgroups-are-slow.patch) by @mwhansen created at 2008-03-18 22:38:55\n\nThis looks good and works for me.",
    "created_at": "2008-03-18T22:38:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2587#issuecomment-17670",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2587-subgroups-are-slow.patch](tarball://root/attachments/some-uuid/ticket2587/2587-subgroups-are-slow.patch) by @mwhansen created at 2008-03-18 22:38:55

This looks good and works for me.



---

archive/issue_comments_017671.json:
```json
{
    "body": "Merged in Sage 2.11.alpha0",
    "created_at": "2008-03-19T00:29:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2587#issuecomment-17671",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha0



---

archive/issue_events_002776.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-19T00:29:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2587",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2587#event-2776"
}
```



---

archive/issue_comments_017672.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-19T00:29:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2587#issuecomment-17672",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
