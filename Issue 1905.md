# Issue 1905: elliptic curves -- both E.Lseries and E.L_series are defined.  Just define one of them, say E.Lseries. (trivial to fix)

archive/issues_001905.json:
```json
{
    "body": "Assignee: was\n\nThere is no good reason to have both.  That would be like having KroneckerSymbol and kronecker_symbol. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1905\n\n",
    "created_at": "2008-01-24T03:09:02Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "elliptic curves -- both E.Lseries and E.L_series are defined.  Just define one of them, say E.Lseries. (trivial to fix)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1905",
    "user": "was"
}
```
Assignee: was

There is no good reason to have both.  That would be like having KroneckerSymbol and kronecker_symbol. 

Issue created by migration from https://trac.sagemath.org/ticket/1905





---

archive/issue_comments_012067.json:
```json
{
    "body": "Attachment [1905-kill-L_series.patch](tarball://root/attachments/some-uuid/ticket1905/1905-kill-L_series.patch) by AlexGhitza created at 2008-01-24 09:23:14",
    "created_at": "2008-01-24T09:23:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1905#issuecomment-12067",
    "user": "AlexGhitza"
}
```

Attachment [1905-kill-L_series.patch](tarball://root/attachments/some-uuid/ticket1905/1905-kill-L_series.patch) by AlexGhitza created at 2008-01-24 09:23:14



---

archive/issue_comments_012068.json:
```json
{
    "body": "See the attached patch for the trivial fix.  The duplicate L_series() appeared only in two files: ell_rational_field.py and padics.py.  Removed it from the first file, and replaced all occurrences in the second file by Lseries().  Also ran sage -t * in schemes/elliptic_curves to make sure nothing got screwed in the process.",
    "created_at": "2008-01-24T09:24:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1905#issuecomment-12068",
    "user": "AlexGhitza"
}
```

See the attached patch for the trivial fix.  The duplicate L_series() appeared only in two files: ell_rational_field.py and padics.py.  Removed it from the first file, and replaced all occurrences in the second file by Lseries().  Also ran sage -t * in schemes/elliptic_curves to make sure nothing got screwed in the process.



---

archive/issue_comments_012069.json:
```json
{
    "body": "Looks good to me.  Thanks Alex!",
    "created_at": "2008-01-24T16:19:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1905#issuecomment-12069",
    "user": "was"
}
```

Looks good to me.  Thanks Alex!



---

archive/issue_comments_012070.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-24T20:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1905#issuecomment-12070",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha2



---

archive/issue_comments_012071.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-24T20:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1905#issuecomment-12071",
    "user": "mabshoff"
}
```

Resolution: fixed
