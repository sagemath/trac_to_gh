# Issue 4118: [with patch, needs review] fix various Pari-related issues

archive/issues_004118.json:
```json
{
    "body": "Assignee: craigcitro\n\nThis patch fixes two things:\n\n1. In various places, we used something like `x.type() == 't_INT'` in Cython code, and with Pari already linked in. In this case, it's much faster to use `typ(x.g) == t_INT`. \n2. Several `_sig_on`s were missing, so I've gone through and added the ones I saw missing. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4118\n\n",
    "created_at": "2008-09-14T11:49:11Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] fix various Pari-related issues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4118",
    "user": "craigcitro"
}
```
Assignee: craigcitro

This patch fixes two things:

1. In various places, we used something like `x.type() == 't_INT'` in Cython code, and with Pari already linked in. In this case, it's much faster to use `typ(x.g) == t_INT`. 
2. Several `_sig_on`s were missing, so I've gone through and added the ones I saw missing. 



Issue created by migration from https://trac.sagemath.org/ticket/4118





---

archive/issue_comments_029817.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-09-14T11:49:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4118#issuecomment-29817",
    "user": "craigcitro"
}
```

Attachment



---

archive/issue_comments_029818.json:
```json
{
    "body": "Nice patch. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-14T11:58:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4118#issuecomment-29818",
    "user": "mabshoff"
}
```

Nice patch. Positive review.

Cheers,

Michael



---

archive/issue_comments_029819.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc3",
    "created_at": "2008-09-14T13:32:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4118#issuecomment-29819",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc3



---

archive/issue_comments_029820.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-14T13:32:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4118#issuecomment-29820",
    "user": "mabshoff"
}
```

Resolution: fixed
