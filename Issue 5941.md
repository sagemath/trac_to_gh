# Issue 5941: [with patch, positive review] transitive_close returns a graph with the same name even though it is a totally different graph!

archive/issues_005941.json:
```json
{
    "body": "Assignee: @rlmill\n\n```\nsage: g = graphs.KrackhardtKiteGraph()\nsage: h = g.transitive_closure()\nsage: h       # oops -- h says it is Krackhardt Kite but it isn't\nKrackhardt Kite Graph: Graph on 10 vertices\nsage: h == g\nFalse\nsage: h.is_isomorphic(g)\nFalse\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5941\n\n",
    "closed_at": "2009-07-19T13:31:43Z",
    "created_at": "2009-04-29T17:18:14Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "[with patch, positive review] transitive_close returns a graph with the same name even though it is a totally different graph!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5941",
    "user": "https://github.com/williamstein"
}
```
Assignee: @rlmill

```
sage: g = graphs.KrackhardtKiteGraph()
sage: h = g.transitive_closure()
sage: h       # oops -- h says it is Krackhardt Kite but it isn't
Krackhardt Kite Graph: Graph on 10 vertices
sage: h == g
False
sage: h.is_isomorphic(g)
False
```

Issue created by migration from https://trac.sagemath.org/ticket/5941





---

archive/issue_comments_046874.json:
```json
{
    "body": "Attachment [trac_5941.patch](tarball://root/attachments/some-uuid/ticket5941/trac_5941.patch) by @rlmill created at 2009-07-16 22:33:00",
    "created_at": "2009-07-16T22:33:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5941#issuecomment-46874",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_5941.patch](tarball://root/attachments/some-uuid/ticket5941/trac_5941.patch) by @rlmill created at 2009-07-16 22:33:00



---

archive/issue_comments_046875.json:
```json
{
    "body": "Nice!",
    "created_at": "2009-07-18T23:49:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5941#issuecomment-46875",
    "user": "https://trac.sagemath.org/admin/accounts/users/ekirkman"
}
```

Nice!



---

archive/issue_comments_046876.json:
```json
{
    "body": "Looks like I simultaneously reviewed this.  Positive review from me too.",
    "created_at": "2009-07-18T23:54:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5941#issuecomment-46876",
    "user": "https://github.com/jasongrout"
}
```

Looks like I simultaneously reviewed this.  Positive review from me too.



---

archive/issue_events_013919.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-19T13:31:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5941",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5941#event-13919"
}
```



---

archive/issue_comments_046877.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-19T13:31:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5941#issuecomment-46877",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
