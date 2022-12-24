# Issue 7302: Nowhere wero flow

archive/issues_007302.json:
```json
{
    "body": "Assignee: @rlmill\n\nAs we will soon have a Flow function in Sage, the next step could be to write a Nowhere Zero flow function !\n\nMore informations there : http://en.wikipedia.org/wiki/Nowhere-zero_flow\n\nIssue created by migration from https://trac.sagemath.org/ticket/7302\n\n",
    "created_at": "2009-10-25T19:46:14Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.2",
    "title": "Nowhere wero flow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7302",
    "user": "@nathanncohen"
}
```
Assignee: @rlmill

As we will soon have a Flow function in Sage, the next step could be to write a Nowhere Zero flow function !

More informations there : http://en.wikipedia.org/wiki/Nowhere-zero_flow

Issue created by migration from https://trac.sagemath.org/ticket/7302





---

archive/issue_comments_060891.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-06T10:59:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7302#issuecomment-60891",
    "user": "@nathanncohen"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_060892.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2017-10-22T12:04:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7302#issuecomment-60892",
    "user": "@dcoudert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060893.json:
```json
{
    "body": "I propose a MIP formulation that answers this long standing request. I'm not aware of alternative/faster methods. It works for any bridgeless (di)graphs with loops or multiple edges.\n----\nNew commits:",
    "created_at": "2017-10-22T12:04:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7302#issuecomment-60893",
    "user": "@dcoudert"
}
```

I propose a MIP formulation that answers this long standing request. I'm not aware of alternative/faster methods. It works for any bridgeless (di)graphs with loops or multiple edges.
----
New commits:



---

archive/issue_comments_060894.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-10-22T21:05:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7302#issuecomment-60894",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060895.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-12-09T18:47:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7302#issuecomment-60895",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060896.json:
```json
{
    "body": "Overall it looks good. I made some documentation tweaks. However, I do have a question about graphs with a single vertex. Should the nowhere zero flow correspond to an empty digraph? If so, then positive review. Otherwise a fix will be needed.\n----\nNew commits:",
    "created_at": "2017-12-11T08:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7302#issuecomment-60896",
    "user": "@tscrim"
}
```

Overall it looks good. I made some documentation tweaks. However, I do have a question about graphs with a single vertex. Should the nowhere zero flow correspond to an empty digraph? If so, then positive review. Otherwise a fix will be needed.
----
New commits:



---

archive/issue_comments_060897.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2017-12-11T08:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7302#issuecomment-60897",
    "user": "@tscrim"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_060898.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-12-11T09:43:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7302#issuecomment-60898",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060899.json:
```json
{
    "body": "You are right, the returned digraph must be on the same vertex set.\nI have pushed required changes.\n\nHowever, the current solution does not pass test due to an issue in `orientations`:\n\n```\nsage: G = Graph(1)\nsage: next(G.orientations())\nDigraph on 0 vertices\n```\n\nI'm opening a ticket to fix that and put a dependency on ticket #24366. So we have to wait before finalizing this ticket.",
    "created_at": "2017-12-11T09:50:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7302#issuecomment-60899",
    "user": "@dcoudert"
}
```

You are right, the returned digraph must be on the same vertex set.
I have pushed required changes.

However, the current solution does not pass test due to an issue in `orientations`:

```
sage: G = Graph(1)
sage: next(G.orientations())
Digraph on 0 vertices
```

I'm opening a ticket to fix that and put a dependency on ticket #24366. So we have to wait before finalizing this ticket.



---

archive/issue_comments_060900.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-12-16T01:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7302#issuecomment-60900",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060901.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2017-12-16T01:34:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7302#issuecomment-60901",
    "user": "@tscrim"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_060902.json:
```json
{
    "body": "Replying to [comment:14 dcoudert]:\n> So we have to wait before finalizing this ticket.\n\nWhy? I don't see the point of waiting for the beta with the dependency to be released. I just merge in the branch, and let us continue with the review here.\n\nI made a few more small tweaks. If my changes look good, then positive review.",
    "created_at": "2017-12-16T01:34:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7302#issuecomment-60902",
    "user": "@tscrim"
}
```

Replying to [comment:14 dcoudert]:
> So we have to wait before finalizing this ticket.

Why? I don't see the point of waiting for the beta with the dependency to be released. I just merge in the branch, and let us continue with the review here.

I made a few more small tweaks. If my changes look good, then positive review.



---

archive/issue_comments_060903.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-12-16T10:02:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7302#issuecomment-60903",
    "user": "@dcoudert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060904.json:
```json
{
    "body": "Thank you Travis. LGTM.",
    "created_at": "2017-12-16T10:02:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7302#issuecomment-60904",
    "user": "@dcoudert"
}
```

Thank you Travis. LGTM.



---

archive/issue_comments_060905.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2017-12-17T14:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7302#issuecomment-60905",
    "user": "@vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_060906.json:
```json
{
    "body": "PDF docs fail (hint: \u2212 is not a minus sign)",
    "created_at": "2017-12-17T14:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7302#issuecomment-60906",
    "user": "@vbraun"
}
```

PDF docs fail (hint: − is not a minus sign)



---

archive/issue_comments_060907.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-12-17T19:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7302#issuecomment-60907",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060908.json:
```json
{
    "body": "Sorry for that.",
    "created_at": "2017-12-17T19:03:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7302#issuecomment-60908",
    "user": "@dcoudert"
}
```

Sorry for that.



---

archive/issue_comments_060909.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2017-12-17T19:03:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7302#issuecomment-60909",
    "user": "@dcoudert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060910.json:
```json
{
    "body": "Thanks to both.",
    "created_at": "2017-12-17T21:11:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7302#issuecomment-60910",
    "user": "@tscrim"
}
```

Thanks to both.



---

archive/issue_comments_060911.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-12-17T21:11:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7302#issuecomment-60911",
    "user": "@tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060912.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2017-12-22T23:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7302#issuecomment-60912",
    "user": "@vbraun"
}
```

Resolution: fixed
