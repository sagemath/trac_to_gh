# Issue 9013: Fix graph.loops() to not return all edges

archive/issues_009013.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\n\n```\nsage: G = graphs.PetersenGraph()\nsage: G.loops()\n[(0, 1, None), (0, 4, None), (0, 5, None), (0, 1, None), (1, 2, None),\n(1, 6, None), (1, 2, None), (2, 3, None), (2, 7, None), (2, 3, None),\n(3, 4, None), (3, 8, None), (0, 4, None), (3, 4, None), (4, 9, None),\n(0, 5, None), (5, 7, None), (5, 8, None), (1, 6, None), (6, 8, None),\n(6, 9, None), (2, 7, None), (5, 7, None), (7, 9, None), (3, 8, None),\n(5, 8, None), (6, 8, None), (4, 9, None), (6, 9, None), (7, 9, None)]\n```\n\n\n...but... the Petersen graph is loop free...\n\nIssue created by migration from https://trac.sagemath.org/ticket/9013\n\n",
    "created_at": "2010-05-21T21:19:23Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "Fix graph.loops() to not return all edges",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9013",
    "user": "boothby"
}
```
Assignee: jason, ncohen, rlm


```
sage: G = graphs.PetersenGraph()
sage: G.loops()
[(0, 1, None), (0, 4, None), (0, 5, None), (0, 1, None), (1, 2, None),
(1, 6, None), (1, 2, None), (2, 3, None), (2, 7, None), (2, 3, None),
(3, 4, None), (3, 8, None), (0, 4, None), (3, 4, None), (4, 9, None),
(0, 5, None), (5, 7, None), (5, 8, None), (1, 6, None), (6, 8, None),
(6, 9, None), (2, 7, None), (5, 7, None), (7, 9, None), (3, 8, None),
(5, 8, None), (6, 8, None), (4, 9, None), (6, 9, None), (7, 9, None)]
```


...but... the Petersen graph is loop free...

Issue created by migration from https://trac.sagemath.org/ticket/9013





---

archive/issue_comments_083369.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-21T21:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83369",
    "user": "rlm"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083370.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-21T21:39:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83370",
    "user": "boothby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_083371.json:
```json
{
    "body": "No new doctests... please add some that verify that the problem has been fixed.",
    "created_at": "2010-05-21T21:39:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83371",
    "user": "boothby"
}
```

No new doctests... please add some that verify that the problem has been fixed.



---

archive/issue_comments_083372.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-21T21:44:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83372",
    "user": "rlm"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083373.json:
```json
{
    "body": "Attachment [out](tarball://root/attachments/some-uuid/ticket9013/out) by boothby created at 2010-05-22 04:52:57",
    "created_at": "2010-05-22T04:52:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83373",
    "user": "boothby"
}
```

Attachment [out](tarball://root/attachments/some-uuid/ticket9013/out) by boothby created at 2010-05-22 04:52:57



---

archive/issue_comments_083374.json:
```json
{
    "body": "Several doctest failures when applied against 4.4.2 in attachment \"out\".",
    "created_at": "2010-05-22T04:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83374",
    "user": "boothby"
}
```

Several doctest failures when applied against 4.4.2 in attachment "out".



---

archive/issue_comments_083375.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-22T04:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83375",
    "user": "boothby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_083376.json:
```json
{
    "body": "Attachment [trac_9013.patch](tarball://root/attachments/some-uuid/ticket9013/trac_9013.patch) by rlm created at 2010-05-25 23:44:59",
    "created_at": "2010-05-25T23:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83376",
    "user": "rlm"
}
```

Attachment [trac_9013.patch](tarball://root/attachments/some-uuid/ticket9013/trac_9013.patch) by rlm created at 2010-05-25 23:44:59



---

archive/issue_comments_083377.json:
```json
{
    "body": "Try this one.",
    "created_at": "2010-05-25T23:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83377",
    "user": "rlm"
}
```

Try this one.



---

archive/issue_comments_083378.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-25T23:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83378",
    "user": "rlm"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083379.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-26T22:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83379",
    "user": "boothby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083380.json:
```json
{
    "body": "Works for me.",
    "created_at": "2010-05-26T22:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83380",
    "user": "boothby"
}
```

Works for me.



---

archive/issue_comments_083381.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T07:05:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83381",
    "user": "mhansen"
}
```

Resolution: fixed
