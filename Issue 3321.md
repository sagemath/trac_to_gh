# Issue 3321: Matrix.visualize_structure is too dark/messed up

archive/issues_003321.json:
```json
{
    "body": "Assignee: cwitty\n\nConsider this example\n\n```\nsage: A = MatrixSpace(GF(2),2000,2000)(1)\nsage: A.visualize_structure()\n```\n\n\nI've attached the output to this ticket (hint: the scaling is to blame) Somehow I believe Tom Boothby would have an easy time to fix this so I CC him :-)\n\nIssue created by migration from https://trac.sagemath.org/ticket/3321\n\n",
    "created_at": "2008-05-28T13:38:50Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "Matrix.visualize_structure is too dark/messed up",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3321",
    "user": "malb"
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

archive/issue_comments_023026.json:
```json
{
    "body": "png output which is way too dark (it should be white)",
    "created_at": "2008-05-28T13:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3321#issuecomment-23026",
    "user": "malb"
}
```

png output which is way too dark (it should be white)



---

archive/issue_comments_023027.json:
```json
{
    "body": "Attachment [3321_visualize_structure.patch](tarball://root/attachments/some-uuid/ticket3321/3321_visualize_structure.patch) by malb created at 2009-01-22 07:37:15",
    "created_at": "2009-01-22T07:37:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3321#issuecomment-23027",
    "user": "malb"
}
```

Attachment [3321_visualize_structure.patch](tarball://root/attachments/some-uuid/ticket3321/3321_visualize_structure.patch) by malb created at 2009-01-22 07:37:15



---

archive/issue_comments_023028.json:
```json
{
    "body": "Attachment [sage0.2.png](tarball://root/attachments/some-uuid/ticket3321/sage0.2.png) by malb created at 2009-01-22 07:37:50\n\nshows that the bug was indeed fixed",
    "created_at": "2009-01-22T07:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3321#issuecomment-23028",
    "user": "malb"
}
```

Attachment [sage0.2.png](tarball://root/attachments/some-uuid/ticket3321/sage0.2.png) by malb created at 2009-01-22 07:37:50

shows that the bug was indeed fixed



---

archive/issue_comments_023029.json:
```json
{
    "body": "This fixes the bug and the code is fine, but in the docstring I have a minor quibble: you remove a warning about libpng problems on OS X. If those problems haven't been fixed, we should leave the warning in the docstring. I'll give this a positive review if you put the little warning back (or show that the problem was fixed!)",
    "created_at": "2009-01-22T08:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3321#issuecomment-23029",
    "user": "ddrake"
}
```

This fixes the bug and the code is fine, but in the docstring I have a minor quibble: you remove a warning about libpng problems on OS X. If those problems haven't been fixed, we should leave the warning in the docstring. I'll give this a positive review if you put the little warning back (or show that the problem was fixed!)



---

archive/issue_comments_023030.json:
```json
{
    "body": "Replying to [comment:2 ddrake]:\n> This fixes the bug and the code is fine, but in the docstring I have a minor quibble: you remove a warning about libpng problems on OS X. If those problems haven't been fixed, we should leave the warning in the docstring. I'll give this a positive review if you put the little warning back (or show that the problem was fixed!)\n\nThe problem has been fixed, which is the reason the libpng.dylib problem pops up with various external packages. It was the tradeoff between the Sage library passing doctests and external code working, so I chose Sage. Hence this is positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-22T10:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3321#issuecomment-23030",
    "user": "mabshoff"
}
```

Replying to [comment:2 ddrake]:
> This fixes the bug and the code is fine, but in the docstring I have a minor quibble: you remove a warning about libpng problems on OS X. If those problems haven't been fixed, we should leave the warning in the docstring. I'll give this a positive review if you put the little warning back (or show that the problem was fixed!)

The problem has been fixed, which is the reason the libpng.dylib problem pops up with various external packages. It was the tradeoff between the Sage library passing doctests and external code working, so I chose Sage. Hence this is positive review.

Cheers,

Michael



---

archive/issue_comments_023031.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T08:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3321#issuecomment-23031",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha1



---

archive/issue_comments_023032.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T08:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3321#issuecomment-23032",
    "user": "mabshoff"
}
```

Resolution: fixed
