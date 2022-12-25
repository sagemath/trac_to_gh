# Issue 9013: Fix graph.loops() to not return all edges

archive/issues_009013.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\n```\nsage: G = graphs.PetersenGraph()\nsage: G.loops()\n[(0, 1, None), (0, 4, None), (0, 5, None), (0, 1, None), (1, 2, None),\n(1, 6, None), (1, 2, None), (2, 3, None), (2, 7, None), (2, 3, None),\n(3, 4, None), (3, 8, None), (0, 4, None), (3, 4, None), (4, 9, None),\n(0, 5, None), (5, 7, None), (5, 8, None), (1, 6, None), (6, 8, None),\n(6, 9, None), (2, 7, None), (5, 7, None), (7, 9, None), (3, 8, None),\n(5, 8, None), (6, 8, None), (4, 9, None), (6, 9, None), (7, 9, None)]\n```\n\n...but... the Petersen graph is loop free...\n\nIssue created by migration from https://trac.sagemath.org/ticket/9013\n\n",
    "closed_at": "2010-06-06T07:05:29Z",
    "created_at": "2010-05-21T21:19:23Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Fix graph.loops() to not return all edges",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9013",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
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

archive/issue_comments_083233.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-21T21:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83233",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083234.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-21T21:39:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83234",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_083235.json:
```json
{
    "body": "No new doctests... please add some that verify that the problem has been fixed.",
    "created_at": "2010-05-21T21:39:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83235",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

No new doctests... please add some that verify that the problem has been fixed.



---

archive/issue_comments_083236.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-21T21:44:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83236",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083237.json:
```json
{
    "body": "Attachment [out](tarball://root/attachments/some-uuid/ticket9013/out) by boothby created at 2010-05-22 04:52:57",
    "created_at": "2010-05-22T04:52:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83237",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [out](tarball://root/attachments/some-uuid/ticket9013/out) by boothby created at 2010-05-22 04:52:57



---

archive/issue_comments_083238.json:
```json
{
    "body": "Several doctest failures when applied against 4.4.2 in attachment \"out\".",
    "created_at": "2010-05-22T04:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83238",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Several doctest failures when applied against 4.4.2 in attachment "out".



---

archive/issue_comments_083239.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-22T04:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83239",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_083240.json:
```json
{
    "body": "Attachment [trac_9013.patch](tarball://root/attachments/some-uuid/ticket9013/trac_9013.patch) by @rlmill created at 2010-05-25 23:44:59",
    "created_at": "2010-05-25T23:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83240",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_9013.patch](tarball://root/attachments/some-uuid/ticket9013/trac_9013.patch) by @rlmill created at 2010-05-25 23:44:59



---

archive/issue_comments_083241.json:
```json
{
    "body": "Try this one.",
    "created_at": "2010-05-25T23:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83241",
    "user": "https://github.com/rlmill"
}
```

Try this one.



---

archive/issue_comments_083242.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-25T23:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83242",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083243.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-26T22:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83243",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083244.json:
```json
{
    "body": "Works for me.",
    "created_at": "2010-05-26T22:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83244",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Works for me.



---

archive/issue_comments_083245.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T07:05:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9013#issuecomment-83245",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_022052.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-06T07:05:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9013",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9013#event-22052"
}
```
