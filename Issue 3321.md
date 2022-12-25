# Issue 3321: Matrix.visualize_structure is too dark/messed up

archive/issues_003321.json:
```json
{
    "body": "Assignee: cwitty\n\nConsider this example\n\n```\nsage: A = MatrixSpace(GF(2),2000,2000)(1)\nsage: A.visualize_structure()\n```\n\n\nI've attached the output to this ticket (hint: the scaling is to blame) Somehow I believe Tom Boothby would have an easy time to fix this so I CC him :-)\n\nIssue created by migration from https://trac.sagemath.org/ticket/3321\n\n",
    "created_at": "2008-05-28T13:38:50Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Matrix.visualize_structure is too dark/messed up",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3321",
    "user": "https://github.com/malb"
}
```
Assignee: cwitty

Consider this example

```
sage: A = MatrixSpace(GF(2),2000,2000)(1)
sage: A.visualize_structure()
```


I've attached the output to this ticket (hint: the scaling is to blame) Somehow I believe Tom Boothby would have an easy time to fix this so I CC him :-)

Issue created by migration from https://trac.sagemath.org/ticket/3321





---

archive/issue_comments_022978.json:
```json
{
    "body": "png output which is way too dark (it should be white)",
    "created_at": "2008-05-28T13:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3321#issuecomment-22978",
    "user": "https://github.com/malb"
}
```

png output which is way too dark (it should be white)



---

archive/issue_comments_022979.json:
```json
{
    "body": "Attachment [3321_visualize_structure.patch](tarball://root/attachments/some-uuid/ticket3321/3321_visualize_structure.patch) by @malb created at 2009-01-22 07:37:15",
    "created_at": "2009-01-22T07:37:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3321#issuecomment-22979",
    "user": "https://github.com/malb"
}
```

Attachment [3321_visualize_structure.patch](tarball://root/attachments/some-uuid/ticket3321/3321_visualize_structure.patch) by @malb created at 2009-01-22 07:37:15



---

archive/issue_comments_022980.json:
```json
{
    "body": "Attachment [sage0.2.png](tarball://root/attachments/some-uuid/ticket3321/sage0.2.png) by @malb created at 2009-01-22 07:37:50\n\nshows that the bug was indeed fixed",
    "created_at": "2009-01-22T07:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3321#issuecomment-22980",
    "user": "https://github.com/malb"
}
```

Attachment [sage0.2.png](tarball://root/attachments/some-uuid/ticket3321/sage0.2.png) by @malb created at 2009-01-22 07:37:50

shows that the bug was indeed fixed



---

archive/issue_comments_022981.json:
```json
{
    "body": "This fixes the bug and the code is fine, but in the docstring I have a minor quibble: you remove a warning about libpng problems on OS X. If those problems haven't been fixed, we should leave the warning in the docstring. I'll give this a positive review if you put the little warning back (or show that the problem was fixed!)",
    "created_at": "2009-01-22T08:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3321#issuecomment-22981",
    "user": "https://github.com/dandrake"
}
```

This fixes the bug and the code is fine, but in the docstring I have a minor quibble: you remove a warning about libpng problems on OS X. If those problems haven't been fixed, we should leave the warning in the docstring. I'll give this a positive review if you put the little warning back (or show that the problem was fixed!)



---

archive/issue_comments_022982.json:
```json
{
    "body": "Replying to [comment:2 ddrake]:\n> This fixes the bug and the code is fine, but in the docstring I have a minor quibble: you remove a warning about libpng problems on OS X. If those problems haven't been fixed, we should leave the warning in the docstring. I'll give this a positive review if you put the little warning back (or show that the problem was fixed!)\n\nThe problem has been fixed, which is the reason the libpng.dylib problem pops up with various external packages. It was the tradeoff between the Sage library passing doctests and external code working, so I chose Sage. Hence this is positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-22T10:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3321#issuecomment-22982",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:2 ddrake]:
> This fixes the bug and the code is fine, but in the docstring I have a minor quibble: you remove a warning about libpng problems on OS X. If those problems haven't been fixed, we should leave the warning in the docstring. I'll give this a positive review if you put the little warning back (or show that the problem was fixed!)

The problem has been fixed, which is the reason the libpng.dylib problem pops up with various external packages. It was the tradeoff between the Sage library passing doctests and external code working, so I chose Sage. Hence this is positive review.

Cheers,

Michael



---

archive/issue_comments_022983.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T08:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3321#issuecomment-22983",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha1



---

archive/issue_comments_022984.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T08:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3321#issuecomment-22984",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
