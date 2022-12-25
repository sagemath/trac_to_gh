# Issue 4118: [with patch, needs review] fix various Pari-related issues

archive/issues_004118.json:
```json
{
    "body": "Assignee: @craigcitro\n\nThis patch fixes two things:\n\n1. In various places, we used something like `x.type() == 't_INT'` in Cython code, and with Pari already linked in. In this case, it's much faster to use `typ(x.g) == t_INT`. \n2. Several `_sig_on`s were missing, so I've gone through and added the ones I saw missing. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4118\n\n",
    "created_at": "2008-09-14T11:49:11Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] fix various Pari-related issues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4118",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

This patch fixes two things:

1. In various places, we used something like `x.type() == 't_INT'` in Cython code, and with Pari already linked in. In this case, it's much faster to use `typ(x.g) == t_INT`. 
2. Several `_sig_on`s were missing, so I've gone through and added the ones I saw missing. 



Issue created by migration from https://trac.sagemath.org/ticket/4118





---

archive/issue_comments_029758.json:
```json
{
    "body": "Attachment [trac-4118.patch](tarball://root/attachments/some-uuid/ticket4118/trac-4118.patch) by @craigcitro created at 2008-09-14 11:49:45",
    "created_at": "2008-09-14T11:49:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4118#issuecomment-29758",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-4118.patch](tarball://root/attachments/some-uuid/ticket4118/trac-4118.patch) by @craigcitro created at 2008-09-14 11:49:45



---

archive/issue_comments_029759.json:
```json
{
    "body": "Nice patch. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-14T11:58:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4118#issuecomment-29759",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nice patch. Positive review.

Cheers,

Michael



---

archive/issue_comments_029760.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc3",
    "created_at": "2008-09-14T13:32:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4118#issuecomment-29760",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc3



---

archive/issue_events_009374.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-14T13:32:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4118",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4118#event-9374"
}
```



---

archive/issue_comments_029761.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-14T13:32:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4118#issuecomment-29761",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
