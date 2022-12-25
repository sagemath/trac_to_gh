# Issue 3502: modular symbols -- implement apply_sparse, which is needed for fast eigenvalue computation

archive/issues_003502.json:
```json
{
    "body": "Assignee: @craigcitro\n\nImplement applying Hecke operator to a single sparse vector, an operation that is needed for quick computation of systems of Hecke eigenvalues.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3502\n\n",
    "created_at": "2008-06-24T15:40:11Z",
    "labels": [
        "component: modular forms"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "modular symbols -- implement apply_sparse, which is needed for fast eigenvalue computation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3502",
    "user": "https://github.com/williamstein"
}
```
Assignee: @craigcitro

Implement applying Hecke operator to a single sparse vector, an operation that is needed for quick computation of systems of Hecke eigenvalues.

Issue created by migration from https://trac.sagemath.org/ticket/3502





---

archive/issue_comments_024648.json:
```json
{
    "body": "So I looked over the code, and everything looks good. There were a handful of small touch-ups needed, missing doctests, etc., so I went ahead and took care of all of that. Someone should look over the additional patch I've posted, but after that, this looks ready to go. \n\nI'm also cleaning up the ticket by deleting the 12 individual patches and posting William's complete bundle (from the URL he added above), and adding my patch.",
    "created_at": "2008-09-11T09:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3502#issuecomment-24648",
    "user": "https://github.com/craigcitro"
}
```

So I looked over the code, and everything looks good. There were a handful of small touch-ups needed, missing doctests, etc., so I went ahead and took care of all of that. Someone should look over the additional patch I've posted, but after that, this looks ready to go. 

I'm also cleaning up the ticket by deleting the 12 individual patches and posting William's complete bundle (from the URL he added above), and adding my patch.



---

archive/issue_comments_024649.json:
```json
{
    "body": "William's bundle with all patches",
    "created_at": "2008-09-11T09:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3502#issuecomment-24649",
    "user": "https://github.com/craigcitro"
}
```

William's bundle with all patches



---

archive/issue_comments_024650.json:
```json
{
    "body": "Attachment [3502.hg](tarball://root/attachments/some-uuid/ticket3502/3502.hg) by @craigcitro created at 2008-09-11 09:21:23",
    "created_at": "2008-09-11T09:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3502#issuecomment-24650",
    "user": "https://github.com/craigcitro"
}
```

Attachment [3502.hg](tarball://root/attachments/some-uuid/ticket3502/3502.hg) by @craigcitro created at 2008-09-11 09:21:23



---

archive/issue_comments_024651.json:
```json
{
    "body": "Attachment [trac-3502-addl.patch](tarball://root/attachments/some-uuid/ticket3502/trac-3502-addl.patch) by @craigcitro created at 2008-09-12 06:54:26\n\n(This doesn't need to go into 3.1.2, so I'm moving it to 3.1.3.)",
    "created_at": "2008-09-12T06:54:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3502#issuecomment-24651",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-3502-addl.patch](tarball://root/attachments/some-uuid/ticket3502/trac-3502-addl.patch) by @craigcitro created at 2008-09-12 06:54:26

(This doesn't need to go into 3.1.2, so I'm moving it to 3.1.3.)



---

archive/issue_comments_024652.json:
```json
{
    "body": "I read through the additional patch, applied it, doctested it, and I'm happy across the board.  It's very good for increasing doctest coverage.\n Thanks Craig!!",
    "created_at": "2008-09-20T04:50:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3502#issuecomment-24652",
    "user": "https://github.com/williamstein"
}
```

I read through the additional patch, applied it, doctested it, and I'm happy across the board.  It's very good for increasing doctest coverage.
 Thanks Craig!!



---

archive/issue_events_003722.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-09-20T21:59:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3502",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3502#event-3722"
}
```



---

archive/issue_comments_024653.json:
```json
{
    "body": "Merged 3502.hg and trac-3502-addl.patch in Sage 3.1.3.alpha1",
    "created_at": "2008-09-20T21:59:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3502#issuecomment-24653",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 3502.hg and trac-3502-addl.patch in Sage 3.1.3.alpha1



---

archive/issue_comments_024654.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-20T21:59:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3502#issuecomment-24654",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
