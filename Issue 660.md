# Issue 660: allow reverse order if converting GF(p^n) element to GF(p)^n element [with patch]

archive/issues_000660.json:
```json
{
    "body": "Assignee: somebody\n\nLet $e \\in GF(q)$. Then `e.vector()` is implemented in little endian ordering in SAGE. This patch allows to reverse this order.\n\nIssue created by migration from https://trac.sagemath.org/ticket/660\n\n",
    "created_at": "2007-09-15T13:10:14Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.5",
    "title": "allow reverse order if converting GF(p^n) element to GF(p)^n element [with patch]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/660",
    "user": "https://github.com/malb"
}
```
Assignee: somebody

Let $e \in GF(q)$. Then `e.vector()` is implemented in little endian ordering in SAGE. This patch allows to reverse this order.

Issue created by migration from https://trac.sagemath.org/ticket/660





---

archive/issue_comments_003419.json:
```json
{
    "body": "Attachment [gfqvectorreverse.patch](tarball://root/attachments/some-uuid/ticket660/gfqvectorreverse.patch) by @malb created at 2007-09-15 13:10:21",
    "created_at": "2007-09-15T13:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/660#issuecomment-3419",
    "user": "https://github.com/malb"
}
```

Attachment [gfqvectorreverse.patch](tarball://root/attachments/some-uuid/ticket660/gfqvectorreverse.patch) by @malb created at 2007-09-15 13:10:21



---

archive/issue_comments_003420.json:
```json
{
    "body": "could use doctests.",
    "created_at": "2007-09-21T02:37:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/660#issuecomment-3420",
    "user": "https://github.com/williamstein"
}
```

could use doctests.



---

archive/issue_comments_003421.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-21T02:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/660#issuecomment-3421",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_001772.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-21T02:39:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/660",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/660#event-1772"
}
```



---

archive/issue_comments_003422.json:
```json
{
    "body": "i added doctests to official repo.",
    "created_at": "2007-09-21T02:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/660#issuecomment-3422",
    "user": "https://github.com/williamstein"
}
```

i added doctests to official repo.
