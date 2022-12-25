# Issue 2774: [with patch, needs review] conversion from PolyBoRi to Singular

archive/issues_002774.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @burcin\n\nKeywords: polybori\n\n\n```\nsage: B.<x,y> = BooleanPolynomialRing(2)\nsage: B._singular_()\n//   characteristic : 2\n//   number of vars : 2\n//        block   1 : ordering lp\n//                  : names    x y\n//        block   2 : ordering C\n// quotient ring from ideal\n_[1]=x2+x\n_[2]=y2+y\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2774\n\n",
    "created_at": "2008-04-02T16:09:06Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, needs review] conversion from PolyBoRi to Singular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2774",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @burcin

Keywords: polybori


```
sage: B.<x,y> = BooleanPolynomialRing(2)
sage: B._singular_()
//   characteristic : 2
//   number of vars : 2
//        block   1 : ordering lp
//                  : names    x y
//        block   2 : ordering C
// quotient ring from ideal
_[1]=x2+x
_[2]=y2+y
```


Issue created by migration from https://trac.sagemath.org/ticket/2774





---

archive/issue_comments_019019.json:
```json
{
    "body": "Attachment [polybori_to_singular.patch](tarball://root/attachments/some-uuid/ticket2774/polybori_to_singular.patch) by @mwhansen created at 2008-04-04 21:32:54\n\nLooks good to me.",
    "created_at": "2008-04-04T21:32:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2774#issuecomment-19019",
    "user": "https://github.com/mwhansen"
}
```

Attachment [polybori_to_singular.patch](tarball://root/attachments/some-uuid/ticket2774/polybori_to_singular.patch) by @mwhansen created at 2008-04-04 21:32:54

Looks good to me.



---

archive/issue_comments_019020.json:
```json
{
    "body": "Merged in Sage 3.0.alpha1",
    "created_at": "2008-04-04T22:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2774#issuecomment-19020",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha1



---

archive/issue_comments_019021.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-04T22:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2774#issuecomment-19021",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006410.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-04T22:15:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2774",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2774#event-6410"
}
```
