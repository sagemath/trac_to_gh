# Issue 701: port srange to Cython for speed

archive/issues_000701.json:
```json
{
    "body": "Assignee: somebody\n\nWilliam complained about srange being slow several times now. Let's fix it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/701\n\n",
    "created_at": "2007-09-20T10:31:27Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.6",
    "title": "port srange to Cython for speed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/701",
    "user": "https://github.com/malb"
}
```
Assignee: somebody

William complained about srange being slow several times now. Let's fix it.

Issue created by migration from https://trac.sagemath.org/ticket/701





---

archive/issue_comments_003661.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-21T00:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/701#issuecomment-3661",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000769.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-09-21T00:00:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/701",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/701#event-769"
}
```



---

archive/issue_comments_003662.json:
```json
{
    "body": "Attachment [srange.hg](tarball://root/attachments/some-uuid/ticket701/srange.hg) by @williamstein created at 2007-09-21 00:00:58",
    "created_at": "2007-09-21T00:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/701#issuecomment-3662",
    "user": "https://github.com/williamstein"
}
```

Attachment [srange.hg](tarball://root/attachments/some-uuid/ticket701/srange.hg) by @williamstein created at 2007-09-21 00:00:58



---

archive/issue_comments_003663.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-09-21T14:28:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/701#issuecomment-3663",
    "user": "https://github.com/jaapspies"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_003664.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-09-21T14:28:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/701#issuecomment-3664",
    "user": "https://github.com/jaapspies"
}
```

Changing status from closed to reopened.



---

archive/issue_events_000770.json:
```json
{
    "actor": "@jaapspies",
    "created_at": "2007-09-21T14:28:13Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/701",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/701#event-770"
}
```



---

archive/issue_comments_003665.json:
```json
{
    "body": "The srange function with include_endpoint=True\ndoes not include the endpoint in some cases:\n\nsage: srange(1.0, 5.0, include_endpoint=True)\n\n[1.00000000000000, 2.00000000000000, 3.00000000000000, 4.00000000000000]",
    "created_at": "2007-09-21T14:28:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/701#issuecomment-3665",
    "user": "https://github.com/jaapspies"
}
```

The srange function with include_endpoint=True
does not include the endpoint in some cases:

sage: srange(1.0, 5.0, include_endpoint=True)

[1.00000000000000, 2.00000000000000, 3.00000000000000, 4.00000000000000]



---

archive/issue_comments_003666.json:
```json
{
    "body": "Attachment [srange-fixes.hg](tarball://root/attachments/some-uuid/ticket701/srange-fixes.hg) by @robertwb created at 2007-09-21 18:46:07",
    "created_at": "2007-09-21T18:46:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/701#issuecomment-3666",
    "user": "https://github.com/robertwb"
}
```

Attachment [srange-fixes.hg](tarball://root/attachments/some-uuid/ticket701/srange-fixes.hg) by @robertwb created at 2007-09-21 18:46:07



---

archive/issue_comments_003667.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-04T03:16:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/701#issuecomment-3667",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000771.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-10-04T03:16:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/701",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/701#event-771"
}
```
