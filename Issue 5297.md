# Issue 5297: [with patch, positive review] sparse vectors and free module elements: pairwise_product is broken

archive/issues_005297.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\n```\nsage: v = vector({1: 1, 3: -2})  \nsage: w = vector({3: 3})       \nsage: v\n(0, 1, 0, -2)\nsage: w\n(0, 0, 0, 3)\nsage: v.pairwise_product(w)\n(0, 1, 0, -6)\nsage: v.dense_vector().pairwise_product(w)\n(0, 0, 0, -6)\n```\n(The last line illustrates that dense vectors seem to work okay.)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5297\n\n",
    "closed_at": "2009-02-18T00:17:17Z",
    "created_at": "2009-02-17T20:55:05Z",
    "labels": [
        "component: linear algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, positive review] sparse vectors and free module elements: pairwise_product is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5297",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

```
sage: v = vector({1: 1, 3: -2})  
sage: w = vector({3: 3})       
sage: v
(0, 1, 0, -2)
sage: w
(0, 0, 0, 3)
sage: v.pairwise_product(w)
(0, 1, 0, -6)
sage: v.dense_vector().pairwise_product(w)
(0, 0, 0, -6)
```
(The last line illustrates that dense vectors seem to work okay.)


Issue created by migration from https://trac.sagemath.org/ticket/5297





---

archive/issue_comments_040684.json:
```json
{
    "body": "Attachment [5297.patch](tarball://root/attachments/some-uuid/ticket5297/5297.patch) by @jhpalmieri created at 2009-02-17 20:56:16",
    "created_at": "2009-02-17T20:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5297#issuecomment-40684",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [5297.patch](tarball://root/attachments/some-uuid/ticket5297/5297.patch) by @jhpalmieri created at 2009-02-17 20:56:16



---

archive/issue_comments_040685.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-02-18T00:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5297#issuecomment-40685",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_events_012317.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-18T00:17:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5297",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5297#event-12317"
}
```



---

archive/issue_comments_040686.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-18T00:17:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5297#issuecomment-40686",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040687.json:
```json
{
    "body": "Merged in Sage 3.3.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-18T00:17:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5297#issuecomment-40687",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.rc2.

Cheers,

Michael



---

archive/issue_events_012318.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-18T00:17:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5297",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5297#event-12318"
}
```
