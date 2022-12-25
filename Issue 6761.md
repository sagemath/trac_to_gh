# Issue 6761: solve_left on a vector returns a matrix

archive/issues_006761.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jasongrout\n\nThis is inconsistent with solve_right and contrary to the documentation. \n\n```\nsage: A = random_matrix(ZZ, 5)\nsage: b = vector(ZZ, range(5))\nsage: A.solve_left(b)\n[    47/630  -233/1170       2/65     34/819 -5269/8190]\nsage: A.solve_left(b).parent()\nFull MatrixSpace of 1 by 5 dense matrices over Rational Field\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6761\n\n",
    "created_at": "2009-08-16T09:13:10Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "solve_left on a vector returns a matrix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6761",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein

CC:  @jasongrout

This is inconsistent with solve_right and contrary to the documentation. 

```
sage: A = random_matrix(ZZ, 5)
sage: b = vector(ZZ, range(5))
sage: A.solve_left(b)
[    47/630  -233/1170       2/65     34/819 -5269/8190]
sage: A.solve_left(b).parent()
Full MatrixSpace of 1 by 5 dense matrices over Rational Field
```

Issue created by migration from https://trac.sagemath.org/ticket/6761





---

archive/issue_comments_055565.json:
```json
{
    "body": "Attachment [trac_6761.patch](tarball://root/attachments/some-uuid/ticket6761/trac_6761.patch) by @kwankyu created at 2009-11-06 08:13:07",
    "created_at": "2009-11-06T08:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6761#issuecomment-55565",
    "user": "https://github.com/kwankyu"
}
```

Attachment [trac_6761.patch](tarball://root/attachments/some-uuid/ticket6761/trac_6761.patch) by @kwankyu created at 2009-11-06 08:13:07



---

archive/issue_comments_055566.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-06T08:19:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6761#issuecomment-55566",
    "user": "https://github.com/kwankyu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_055567.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-06T20:06:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6761#issuecomment-55567",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_055568.json:
```json
{
    "body": "Thanks!",
    "created_at": "2009-11-06T20:06:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6761#issuecomment-55568",
    "user": "https://github.com/robertwb"
}
```

Thanks!



---

archive/issue_events_015938.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-07T04:59:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6761",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6761#event-15938"
}
```



---

archive/issue_comments_055569.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-07T04:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6761#issuecomment-55569",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
