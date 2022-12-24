# Issue 701: port srange to Cython for speed

archive/issues_000701.json:
```json
{
    "body": "Assignee: somebody\n\nWilliam complained about srange being slow several times now. Let's fix it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/701\n\n",
    "created_at": "2007-09-20T10:31:27Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "title": "port srange to Cython for speed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/701",
    "user": "malb"
}
```
Assignee: somebody

William complained about srange being slow several times now. Let's fix it.

Issue created by migration from https://trac.sagemath.org/ticket/701





---

archive/issue_comments_003674.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-21T00:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/701#issuecomment-3674",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_003675.json:
```json
{
    "body": "Attachment [srange.hg](tarball://root/attachments/some-uuid/ticket701/srange.hg) by was created at 2007-09-21 00:00:58",
    "created_at": "2007-09-21T00:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/701#issuecomment-3675",
    "user": "was"
}
```

Attachment [srange.hg](tarball://root/attachments/some-uuid/ticket701/srange.hg) by was created at 2007-09-21 00:00:58



---

archive/issue_comments_003676.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-09-21T14:28:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/701#issuecomment-3676",
    "user": "jsp"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_003677.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-09-21T14:28:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/701#issuecomment-3677",
    "user": "jsp"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_003678.json:
```json
{
    "body": "The srange function with include_endpoint=True\ndoes not include the endpoint in some cases:\n\nsage: srange(1.0, 5.0, include_endpoint=True)\n\n[1.00000000000000, 2.00000000000000, 3.00000000000000, 4.00000000000000]",
    "created_at": "2007-09-21T14:28:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/701#issuecomment-3678",
    "user": "jsp"
}
```

The srange function with include_endpoint=True
does not include the endpoint in some cases:

sage: srange(1.0, 5.0, include_endpoint=True)

[1.00000000000000, 2.00000000000000, 3.00000000000000, 4.00000000000000]



---

archive/issue_comments_003679.json:
```json
{
    "body": "Attachment [srange-fixes.hg](tarball://root/attachments/some-uuid/ticket701/srange-fixes.hg) by robertwb created at 2007-09-21 18:46:07",
    "created_at": "2007-09-21T18:46:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/701#issuecomment-3679",
    "user": "robertwb"
}
```

Attachment [srange-fixes.hg](tarball://root/attachments/some-uuid/ticket701/srange-fixes.hg) by robertwb created at 2007-09-21 18:46:07



---

archive/issue_comments_003680.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-04T03:16:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/701#issuecomment-3680",
    "user": "was"
}
```

Resolution: fixed
