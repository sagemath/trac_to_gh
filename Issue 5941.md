# Issue 5941: transitive_close returns a graph with the same name even though it is a totally different graph!

archive/issues_005941.json:
```json
{
    "body": "Assignee: rlm\n\n\n```\nsage: g = graphs.KrackhardtKiteGraph()\nsage: h = g.transitive_closure()\nsage: h       # oops -- h says it is Krackhardt Kite but it isn't\nKrackhardt Kite Graph: Graph on 10 vertices\nsage: h == g\nFalse\nsage: h.is_isomorphic(g)\nFalse\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5941\n\n",
    "created_at": "2009-04-29T17:18:14Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "transitive_close returns a graph with the same name even though it is a totally different graph!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5941",
    "user": "was"
}
```
Assignee: rlm


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

archive/issue_comments_046963.json:
```json
{
    "body": "Attachment [trac_5941.patch](tarball://root/attachments/some-uuid/ticket5941/trac_5941.patch) by rlm created at 2009-07-16 22:33:00",
    "created_at": "2009-07-16T22:33:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5941#issuecomment-46963",
    "user": "rlm"
}
```

Attachment [trac_5941.patch](tarball://root/attachments/some-uuid/ticket5941/trac_5941.patch) by rlm created at 2009-07-16 22:33:00



---

archive/issue_comments_046964.json:
```json
{
    "body": "Nice!",
    "created_at": "2009-07-18T23:49:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5941#issuecomment-46964",
    "user": "ekirkman"
}
```

Nice!



---

archive/issue_comments_046965.json:
```json
{
    "body": "Looks like I simultaneously reviewed this.  Positive review from me too.",
    "created_at": "2009-07-18T23:54:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5941#issuecomment-46965",
    "user": "jason"
}
```

Looks like I simultaneously reviewed this.  Positive review from me too.



---

archive/issue_comments_046966.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-19T13:31:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5941#issuecomment-46966",
    "user": "mvngu"
}
```

Resolution: fixed
