# Issue 3040: [with patch; needs review] make it so magma(A) works for matrices over cyclotomic number fields

archive/issues_003040.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @ncalexan\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3040\n\n",
    "created_at": "2008-04-27T03:21:07Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "[with patch; needs review] make it so magma(A) works for matrices over cyclotomic number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3040",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @ncalexan



Issue created by migration from https://trac.sagemath.org/ticket/3040





---

archive/issue_comments_020872.json:
```json
{
    "body": "Attachment [sage-3040.patch](tarball://root/attachments/some-uuid/ticket3040/sage-3040.patch) by mabshoff created at 2008-04-27 03:32:04\n\nWhoever reviews this also ought to review #2171\n\nCheers,\n\nMichael",
    "created_at": "2008-04-27T03:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3040#issuecomment-20872",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [sage-3040.patch](tarball://root/attachments/some-uuid/ticket3040/sage-3040.patch) by mabshoff created at 2008-04-27 03:32:04

Whoever reviews this also ought to review #2171

Cheers,

Michael



---

archive/issue_comments_020873.json:
```json
{
    "body": "As written, this does not work.  Was it the wrong version of the patch?\n\nHere's a potential doctest, it fails because magma(K) does not work.\n\n\n```\n        We coerce a matrix over a cyclotomic field, where the\n        generator must be named during the coercion.\n            sage: K.<z> = CyclotomicField(12)\n            sage: A = matrix(K, 2, 3, [z, 1+z, z^7 - z + 10/3, 1, 0, z^2 + z + 9*z^11])\n            sage: B = magma(A); B                       # optional\n            sage: B.Type()                              # optional\n            ModMatFldElt\n            sage: B.Parent()                            # optional\n            Full KMatrixSpace of 2 by 3 matrices over XXX\n```\n",
    "created_at": "2008-05-05T18:39:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3040#issuecomment-20873",
    "user": "https://github.com/ncalexan"
}
```

As written, this does not work.  Was it the wrong version of the patch?

Here's a potential doctest, it fails because magma(K) does not work.


```
        We coerce a matrix over a cyclotomic field, where the
        generator must be named during the coercion.
            sage: K.<z> = CyclotomicField(12)
            sage: A = matrix(K, 2, 3, [z, 1+z, z^7 - z + 10/3, 1, 0, z^2 + z + 9*z^11])
            sage: B = magma(A); B                       # optional
            sage: B.Type()                              # optional
            ModMatFldElt
            sage: B.Parent()                            # optional
            Full KMatrixSpace of 2 by 3 matrices over XXX
```




---

archive/issue_comments_020874.json:
```json
{
    "body": "This works fine -- assuming you have the first patch from #3042 applied. Once that's in place, this is awesome.",
    "created_at": "2008-05-10T10:44:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3040#issuecomment-20874",
    "user": "https://github.com/craigcitro"
}
```

This works fine -- assuming you have the first patch from #3042 applied. Once that's in place, this is awesome.



---

archive/issue_comments_020875.json:
```json
{
    "body": "Oh, and I noticed that this patch didn't have a doctest. I mistakenly let it through -- so I'm adding one, and attaching a patch.",
    "created_at": "2008-05-10T11:00:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3040#issuecomment-20875",
    "user": "https://github.com/craigcitro"
}
```

Oh, and I noticed that this patch didn't have a doctest. I mistakenly let it through -- so I'm adding one, and attaching a patch.



---

archive/issue_comments_020876.json:
```json
{
    "body": "Attachment [trac-3040-doctest.patch](tarball://root/attachments/some-uuid/ticket3040/trac-3040-doctest.patch) by mabshoff created at 2008-06-08 22:53:02\n\nsage-3040.patch no longer applies cleanly. Please rebase.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-08T22:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3040#issuecomment-20876",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac-3040-doctest.patch](tarball://root/attachments/some-uuid/ticket3040/trac-3040-doctest.patch) by mabshoff created at 2008-06-08 22:53:02

sage-3040.patch no longer applies cleanly. Please rebase.

Cheers,

Michael



---

archive/issue_comments_020877.json:
```json
{
    "body": "Attachment [sage-3040-doctest-rebase.patch](tarball://root/attachments/some-uuid/ticket3040/sage-3040-doctest-rebase.patch) by @williamstein created at 2008-06-09 07:25:44",
    "created_at": "2008-06-09T07:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3040#issuecomment-20877",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3040-doctest-rebase.patch](tarball://root/attachments/some-uuid/ticket3040/sage-3040-doctest-rebase.patch) by @williamstein created at 2008-06-09 07:25:44



---

archive/issue_comments_020878.json:
```json
{
    "body": "Merged sage-3040-rebase.patch and sage-3040-doctest-rebase.patch in Sage 3.0.3.alpha2",
    "created_at": "2008-06-09T07:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3040#issuecomment-20878",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged sage-3040-rebase.patch and sage-3040-doctest-rebase.patch in Sage 3.0.3.alpha2



---

archive/issue_events_006889.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-09T07:42:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3040",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3040#event-6889"
}
```



---

archive/issue_comments_020879.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-09T07:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3040#issuecomment-20879",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020880.json:
```json
{
    "body": "The patches have been rebased, so correct the \"Summary\".\n\nCheers,\n\nMichael",
    "created_at": "2008-06-09T07:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3040#issuecomment-20880",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patches have been rebased, so correct the "Summary".

Cheers,

Michael
