# Issue 9861: Reimplementation of IntervalGraph to handle repeated vertices.

archive/issues_009861.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nKeywords: interval graph\n\nThis is a reimplementation of the `IntervalGraph()` constructor to allow repeated intervals in the list of intervals. The input is a list of intervals. The output is a graph whose vertices are numbered 0 through n-1 (where n is the length of the list). Vertices u and v are adjacent iff the u'th and v'th intervals in the input list intersect. The intervals associated with these vertices are saved with the graph using `set_vertex` and can be retrieved later using `get_vertex` or `get_vertices`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9862\n\n",
    "created_at": "2010-09-06T18:53:29Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Reimplementation of IntervalGraph to handle repeated vertices.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9861",
    "user": "https://trac.sagemath.org/admin/accounts/users/edward.scheinerman"
}
```
Assignee: jason, ncohen, rlm

Keywords: interval graph

This is a reimplementation of the `IntervalGraph()` constructor to allow repeated intervals in the list of intervals. The input is a list of intervals. The output is a graph whose vertices are numbered 0 through n-1 (where n is the length of the list). Vertices u and v are adjacent iff the u'th and v'th intervals in the input list intersect. The intervals associated with these vertices are saved with the graph using `set_vertex` and can be retrieved later using `get_vertex` or `get_vertices`.

Issue created by migration from https://trac.sagemath.org/ticket/9862





---

archive/issue_comments_097204.json:
```json
{
    "body": "Attachment [trac_9862.patch](tarball://root/attachments/some-uuid/ticket9862/trac_9862.patch) by edward.scheinerman created at 2010-09-06 18:54:32",
    "created_at": "2010-09-06T18:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9861#issuecomment-97204",
    "user": "https://trac.sagemath.org/admin/accounts/users/edward.scheinerman"
}
```

Attachment [trac_9862.patch](tarball://root/attachments/some-uuid/ticket9862/trac_9862.patch) by edward.scheinerman created at 2010-09-06 18:54:32



---

archive/issue_comments_097205.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-06T18:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9861#issuecomment-97205",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097206.json:
```json
{
    "body": "Two short modifications in the docstring... One to use the \".. NOTE\" environment, and another one to propagate the warnings to RandomInterval `:-)`\n\nAs usual, positive review to your patch ! It's left to you to judge mine `:-)`\n\nNathann",
    "created_at": "2010-09-06T19:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9861#issuecomment-97206",
    "user": "https://github.com/nathanncohen"
}
```

Two short modifications in the docstring... One to use the ".. NOTE" environment, and another one to propagate the warnings to RandomInterval `:-)`

As usual, positive review to your patch ! It's left to you to judge mine `:-)`

Nathann



---

archive/issue_comments_097207.json:
```json
{
    "body": "Attachment [trac_9862 - small docstring fixes.patch](tarball://root/attachments/some-uuid/ticket9862/trac_9862 - small docstring fixes.patch) by @nathanncohen created at 2010-09-06 19:25:08",
    "created_at": "2010-09-06T19:25:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9861#issuecomment-97207",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_9862 - small docstring fixes.patch](tarball://root/attachments/some-uuid/ticket9862/trac_9862 - small docstring fixes.patch) by @nathanncohen created at 2010-09-06 19:25:08



---

archive/issue_comments_097208.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-06T19:59:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9861#issuecomment-97208",
    "user": "https://trac.sagemath.org/admin/accounts/users/edward.scheinerman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097209.json:
```json
{
    "body": "Doc string changes are fine. Thanks, Nathann.",
    "created_at": "2010-09-06T19:59:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9861#issuecomment-97209",
    "user": "https://trac.sagemath.org/admin/accounts/users/edward.scheinerman"
}
```

Doc string changes are fine. Thanks, Nathann.



---

archive/issue_comments_097210.json:
```json
{
    "body": "I'm glad to see this IntervalGraph issue settled at last.... and this easily :-)\n\nNathann",
    "created_at": "2010-09-06T20:09:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9861#issuecomment-97210",
    "user": "https://github.com/nathanncohen"
}
```

I'm glad to see this IntervalGraph issue settled at last.... and this easily :-)

Nathann



---

archive/issue_comments_097211.json:
```json
{
    "body": "Remember to fill in the \"Author(s)\" and \"Reviewer(s)\" fields.  We use these to generate release notes.",
    "created_at": "2010-09-15T22:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9861#issuecomment-97211",
    "user": "https://github.com/qed777"
}
```

Remember to fill in the "Author(s)" and "Reviewer(s)" fields.  We use these to generate release notes.



---

archive/issue_events_009991.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-09-15T22:52:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9861",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9861#event-9991"
}
```



---

archive/issue_comments_097212.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T22:52:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9861#issuecomment-97212",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
