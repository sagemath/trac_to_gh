# Issue 2083: [with patch, needs review] Make number_field .galois_closure require a name and .galois_conjugates take an explicit field.

archive/issues_002083.json:
```json
{
    "body": "Assignee: was\n\nKeywords: number field galois closure names\n\n`.galois_closure` used to guess a variable name, which is not very Sage-like.  This and a related issue with `.galois_conjugates` are fixed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2083\n\n",
    "created_at": "2008-02-07T08:57:01Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with patch, needs review] Make number_field .galois_closure require a name and .galois_conjugates take an explicit field.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2083",
    "user": "ncalexan"
}
```
Assignee: was

Keywords: number field galois closure names

`.galois_closure` used to guess a variable name, which is not very Sage-like.  This and a related issue with `.galois_conjugates` are fixed.

Issue created by migration from https://trac.sagemath.org/ticket/2083





---

archive/issue_comments_013483.json:
```json
{
    "body": "Attachment [ncalexan-nf-galois-closure.patch](tarball://root/attachments/some-uuid/ticket2083/ncalexan-nf-galois-closure.patch) by ncalexan created at 2008-02-07 08:57:45",
    "created_at": "2008-02-07T08:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2083#issuecomment-13483",
    "user": "ncalexan"
}
```

Attachment [ncalexan-nf-galois-closure.patch](tarball://root/attachments/some-uuid/ticket2083/ncalexan-nf-galois-closure.patch) by ncalexan created at 2008-02-07 08:57:45



---

archive/issue_comments_013484.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-02-07T10:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2083#issuecomment-13484",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_013485.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-07T10:33:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2083#issuecomment-13485",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013486.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-07T10:33:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2083#issuecomment-13486",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha0
