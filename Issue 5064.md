# Issue 5064: Steenrod algebras are non-unique

archive/issues_005064.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @jhpalmieri\n\n\n```\nsage: A = SteenrodAlgebra(17)\nsage: A(0).parent() is A\nFalse\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5064\n\n",
    "created_at": "2009-01-23T02:16:15Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Steenrod algebras are non-unique",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5064",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: tbd

CC:  @jhpalmieri


```
sage: A = SteenrodAlgebra(17)
sage: A(0).parent() is A
False
```


Issue created by migration from https://trac.sagemath.org/ticket/5064





---

archive/issue_comments_038500.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-01-23T02:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5064#issuecomment-38500",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing priority from major to minor.



---

archive/issue_comments_038501.json:
```json
{
    "body": "Changing component from algebra to commutative algebra.",
    "created_at": "2009-01-23T02:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5064#issuecomment-38501",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing component from algebra to commutative algebra.



---

archive/issue_comments_038502.json:
```json
{
    "body": "Changing assignee from tbd to @malb.",
    "created_at": "2009-01-23T02:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5064#issuecomment-38502",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing assignee from tbd to @malb.



---

archive/issue_comments_038503.json:
```json
{
    "body": "Changing component from commutative algebra to algebra.",
    "created_at": "2009-01-23T02:17:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5064#issuecomment-38503",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing component from commutative algebra to algebra.



---

archive/issue_comments_038504.json:
```json
{
    "body": "Changing assignee from @malb to tbd.",
    "created_at": "2009-01-23T02:17:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5064#issuecomment-38504",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing assignee from @malb to tbd.



---

archive/issue_comments_038505.json:
```json
{
    "body": "Attachment [5064-unique-steenrod.patch](tarball://root/attachments/some-uuid/ticket5064/5064-unique-steenrod.patch) by boothby created at 2009-01-24 10:09:02",
    "created_at": "2009-01-24T10:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5064#issuecomment-38505",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [5064-unique-steenrod.patch](tarball://root/attachments/some-uuid/ticket5064/5064-unique-steenrod.patch) by boothby created at 2009-01-24 10:09:02



---

archive/issue_comments_038506.json:
```json
{
    "body": "tried the patch, it doesn't work for me.",
    "created_at": "2009-01-24T11:42:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5064#issuecomment-38506",
    "user": "https://trac.sagemath.org/admin/accounts/users/shumow"
}
```

tried the patch, it doesn't work for me.



---

archive/issue_comments_038507.json:
```json
{
    "body": "My bad.  I screwed up the test.  It works for me now.\nI ran the tests and looked the code over, but I don't know enough about Steenrod Algebras to feel comfortable refereeing this.",
    "created_at": "2009-01-24T11:49:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5064#issuecomment-38507",
    "user": "https://trac.sagemath.org/admin/accounts/users/shumow"
}
```

My bad.  I screwed up the test.  It works for me now.
I ran the tests and looked the code over, but I don't know enough about Steenrod Algebras to feel comfortable refereeing this.



---

archive/issue_comments_038508.json:
```json
{
    "body": "On closer explanation from boothby, I feel I can give this a positive review.",
    "created_at": "2009-01-24T12:02:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5064#issuecomment-38508",
    "user": "https://trac.sagemath.org/admin/accounts/users/shumow"
}
```

On closer explanation from boothby, I feel I can give this a positive review.



---

archive/issue_comments_038509.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T16:28:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5064#issuecomment-38509",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha2



---

archive/issue_comments_038510.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T16:28:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5064#issuecomment-38510",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
