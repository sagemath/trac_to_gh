# Issue 9861: Reimplementation of IntervalGraph to handle repeated vertices.

archive/issues_009861.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nKeywords: interval graph\n\nThis is a reimplementation of the `IntervalGraph()` constructor to allow repeated intervals in the list of intervals. The input is a list of intervals. The output is a graph whose vertices are numbered 0 through n-1 (where n is the length of the list). Vertices u and v are adjacent iff the u'th and v'th intervals in the input list intersect. The intervals associated with these vertices are saved with the graph using `set_vertex` and can be retrieved later using `get_vertex` or `get_vertices`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9862\n\n",
    "created_at": "2010-09-06T18:53:29Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "Reimplementation of IntervalGraph to handle repeated vertices.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9861",
    "user": "edward.scheinerman"
}
```
Assignee: jason, ncohen, rlm

Keywords: interval graph

This is a reimplementation of the `IntervalGraph()` constructor to allow repeated intervals in the list of intervals. The input is a list of intervals. The output is a graph whose vertices are numbered 0 through n-1 (where n is the length of the list). Vertices u and v are adjacent iff the u'th and v'th intervals in the input list intersect. The intervals associated with these vertices are saved with the graph using `set_vertex` and can be retrieved later using `get_vertex` or `get_vertices`.

Issue created by migration from https://trac.sagemath.org/ticket/9862





---

archive/issue_comments_097363.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-09-06T18:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9861#issuecomment-97363",
    "user": "edward.scheinerman"
}
```

Attachment



---

archive/issue_comments_097364.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-06T18:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9861#issuecomment-97364",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097365.json:
```json
{
    "body": "Two short modifications in the docstring... One to use the \".. NOTE\" environment, and another one to propagate the warnings to RandomInterval `:-)`\n\nAs usual, positive review to your patch ! It's left to you to judge mine `:-)`\n\nNathann",
    "created_at": "2010-09-06T19:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9861#issuecomment-97365",
    "user": "ncohen"
}
```

Two short modifications in the docstring... One to use the ".. NOTE" environment, and another one to propagate the warnings to RandomInterval `:-)`

As usual, positive review to your patch ! It's left to you to judge mine `:-)`

Nathann



---

archive/issue_comments_097366.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-09-06T19:25:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9861#issuecomment-97366",
    "user": "ncohen"
}
```

Attachment



---

archive/issue_comments_097367.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-06T19:59:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9861#issuecomment-97367",
    "user": "edward.scheinerman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097368.json:
```json
{
    "body": "Doc string changes are fine. Thanks, Nathann.",
    "created_at": "2010-09-06T19:59:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9861#issuecomment-97368",
    "user": "edward.scheinerman"
}
```

Doc string changes are fine. Thanks, Nathann.



---

archive/issue_comments_097369.json:
```json
{
    "body": "I'm glad to see this IntervalGraph issue settled at last.... and this easily :-)\n\nNathann",
    "created_at": "2010-09-06T20:09:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9861#issuecomment-97369",
    "user": "ncohen"
}
```

I'm glad to see this IntervalGraph issue settled at last.... and this easily :-)

Nathann



---

archive/issue_comments_097370.json:
```json
{
    "body": "Remember to fill in the \"Author(s)\" and \"Reviewer(s)\" fields.  We use these to generate release notes.",
    "created_at": "2010-09-15T22:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9861#issuecomment-97370",
    "user": "mpatel"
}
```

Remember to fill in the "Author(s)" and "Reviewer(s)" fields.  We use these to generate release notes.



---

archive/issue_comments_097371.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T22:52:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9861#issuecomment-97371",
    "user": "mpatel"
}
```

Resolution: fixed
