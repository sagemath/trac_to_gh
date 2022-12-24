# Issue 3502: modular symbols -- implement apply_sparse, which is needed for fast eigenvalue computation

archive/issues_003502.json:
```json
{
    "body": "Assignee: craigcitro\n\nImplement applying Hecke operator to a single sparse vector, an operation that is needed for quick computation of systems of Hecke eigenvalues.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3502\n\n",
    "created_at": "2008-06-24T15:40:11Z",
    "labels": [
        "modular forms",
        "major",
        "enhancement"
    ],
    "title": "modular symbols -- implement apply_sparse, which is needed for fast eigenvalue computation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3502",
    "user": "was"
}
```
Assignee: craigcitro

Implement applying Hecke operator to a single sparse vector, an operation that is needed for quick computation of systems of Hecke eigenvalues.

Issue created by migration from https://trac.sagemath.org/ticket/3502





---

archive/issue_comments_024697.json:
```json
{
    "body": "So I looked over the code, and everything looks good. There were a handful of small touch-ups needed, missing doctests, etc., so I went ahead and took care of all of that. Someone should look over the additional patch I've posted, but after that, this looks ready to go. \n\nI'm also cleaning up the ticket by deleting the 12 individual patches and posting William's complete bundle (from the URL he added above), and adding my patch.",
    "created_at": "2008-09-11T09:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3502#issuecomment-24697",
    "user": "craigcitro"
}
```

So I looked over the code, and everything looks good. There were a handful of small touch-ups needed, missing doctests, etc., so I went ahead and took care of all of that. Someone should look over the additional patch I've posted, but after that, this looks ready to go. 

I'm also cleaning up the ticket by deleting the 12 individual patches and posting William's complete bundle (from the URL he added above), and adding my patch.



---

archive/issue_comments_024698.json:
```json
{
    "body": "William's bundle with all patches",
    "created_at": "2008-09-11T09:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3502#issuecomment-24698",
    "user": "craigcitro"
}
```

William's bundle with all patches



---

archive/issue_comments_024699.json:
```json
{
    "body": "Attachment [3502.hg](tarball://root/attachments/some-uuid/ticket3502/3502.hg) by craigcitro created at 2008-09-11 09:21:23",
    "created_at": "2008-09-11T09:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3502#issuecomment-24699",
    "user": "craigcitro"
}
```

Attachment [3502.hg](tarball://root/attachments/some-uuid/ticket3502/3502.hg) by craigcitro created at 2008-09-11 09:21:23



---

archive/issue_comments_024700.json:
```json
{
    "body": "Attachment [trac-3502-addl.patch](tarball://root/attachments/some-uuid/ticket3502/trac-3502-addl.patch) by craigcitro created at 2008-09-12 06:54:26\n\n(This doesn't need to go into 3.1.2, so I'm moving it to 3.1.3.)",
    "created_at": "2008-09-12T06:54:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3502#issuecomment-24700",
    "user": "craigcitro"
}
```

Attachment [trac-3502-addl.patch](tarball://root/attachments/some-uuid/ticket3502/trac-3502-addl.patch) by craigcitro created at 2008-09-12 06:54:26

(This doesn't need to go into 3.1.2, so I'm moving it to 3.1.3.)



---

archive/issue_comments_024701.json:
```json
{
    "body": "I read through the additional patch, applied it, doctested it, and I'm happy across the board.  It's very good for increasing doctest coverage.\n Thanks Craig!!",
    "created_at": "2008-09-20T04:50:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3502#issuecomment-24701",
    "user": "was"
}
```

I read through the additional patch, applied it, doctested it, and I'm happy across the board.  It's very good for increasing doctest coverage.
 Thanks Craig!!



---

archive/issue_comments_024702.json:
```json
{
    "body": "Merged 3502.hg and trac-3502-addl.patch in Sage 3.1.3.alpha1",
    "created_at": "2008-09-20T21:59:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3502#issuecomment-24702",
    "user": "mabshoff"
}
```

Merged 3502.hg and trac-3502-addl.patch in Sage 3.1.3.alpha1



---

archive/issue_comments_024703.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-20T21:59:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3502#issuecomment-24703",
    "user": "mabshoff"
}
```

Resolution: fixed
