# Issue 9714: Graph(..., format='incidence_matrix') doesn't work with graphs that have loops, but G.incidence_matrix() does.  So?

archive/issues_009714.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nWe have\n\n```\nsage: M = matrix(3, [1,2,0, 0,2,0, 0,0,1])\nsage: g = Graph(M, format='adjacency_matrix')\nsage: I = g.incidence_matrix(); I\n[-1 -1  0  0  0  1]\n[ 1  1  0  1  1  0]\n[ 0  0  1  0  0  0]\n```\nBut then:\n\n```\nsage: Graph(I, format='incidence_matrix').show(graph_border=True)\nkaboom!\n```\n\nEither the first .incidence_matrix() should fail, or the second Graph(...) should work.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9714\n\n",
    "created_at": "2010-08-10T00:16:47Z",
    "labels": [
        "component: graph theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "Graph(..., format='incidence_matrix') doesn't work with graphs that have loops, but G.incidence_matrix() does.  So?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9714",
    "user": "https://github.com/williamstein"
}
```
Assignee: jason, ncohen, rlm

We have

```
sage: M = matrix(3, [1,2,0, 0,2,0, 0,0,1])
sage: g = Graph(M, format='adjacency_matrix')
sage: I = g.incidence_matrix(); I
[-1 -1  0  0  0  1]
[ 1  1  0  1  1  0]
[ 0  0  1  0  0  0]
```
But then:

```
sage: Graph(I, format='incidence_matrix').show(graph_border=True)
kaboom!
```

Either the first .incidence_matrix() should fail, or the second Graph(...) should work.

Issue created by migration from https://trac.sagemath.org/ticket/9714





---

archive/issue_comments_094613.json:
```json
{
    "body": "Easy to fix, just replace (on line 944 of `graph.py`)\n\n```\nif len(NZ) != 2:\n    msg += \"There must be two nonzero entries (-1 & 1) per column.\"\n    assert False\n```\nwith something like\n\n```\nif len(NZ) == 1:\n    if loops is None:\n        loops = True\n    elif not loops:\n        msg += \"There must be two nonzero entries (-1 & 1) per column.\"\n        assert False\nelif len(NZ) != 2:\n    msg += \"There must be two nonzero entries (-1 & 1) per column.\"\n    assert False\n```",
    "created_at": "2010-08-10T00:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9714#issuecomment-94613",
    "user": "https://github.com/rlmill"
}
```

Easy to fix, just replace (on line 944 of `graph.py`)

```
if len(NZ) != 2:
    msg += "There must be two nonzero entries (-1 & 1) per column."
    assert False
```
with something like

```
if len(NZ) == 1:
    if loops is None:
        loops = True
    elif not loops:
        msg += "There must be two nonzero entries (-1 & 1) per column."
        assert False
elif len(NZ) != 2:
    msg += "There must be two nonzero entries (-1 & 1) per column."
    assert False
```



---

archive/issue_comments_094614.json:
```json
{
    "body": "Attachment [trac_9714_incidence_checking.patch](tarball://root/attachments/some-uuid/ticket9714/trac_9714_incidence_checking.patch) by brunellus created at 2012-01-23 19:53:08",
    "created_at": "2012-01-23T19:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9714#issuecomment-94614",
    "user": "https://trac.sagemath.org/admin/accounts/users/brunellus"
}
```

Attachment [trac_9714_incidence_checking.patch](tarball://root/attachments/some-uuid/ticket9714/trac_9714_incidence_checking.patch) by brunellus created at 2012-01-23 19:53:08



---

archive/issue_comments_094615.json:
```json
{
    "body": "Then there is another problem: checking forgets possibility that there are only two vertices defined. I tried to fix that: see the second doctest.",
    "created_at": "2012-01-23T19:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9714#issuecomment-94615",
    "user": "https://trac.sagemath.org/admin/accounts/users/brunellus"
}
```

Then there is another problem: checking forgets possibility that there are only two vertices defined. I tried to fix that: see the second doctest.



---

archive/issue_comments_094616.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-23T19:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9714#issuecomment-94616",
    "user": "https://trac.sagemath.org/admin/accounts/users/brunellus"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_094617.json:
```json
{
    "body": "Helloooooooooooooooo !!!\n\nI find a bit weird that this code deals with -1 and 1 entries for *undirected* graphs, but well... `^^;`\n\nAnyway, here is a very small patch that just avoid some unnecessary computations. \n\nI give a positive review to your patch, and you can review mine if you have some time `:-)`\n\nNathann",
    "created_at": "2012-01-29T19:04:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9714#issuecomment-94617",
    "user": "https://github.com/nathanncohen"
}
```

Helloooooooooooooooo !!!

I find a bit weird that this code deals with -1 and 1 entries for *undirected* graphs, but well... `^^;`

Anyway, here is a very small patch that just avoid some unnecessary computations. 

I give a positive review to your patch, and you can review mine if you have some time `:-)`

Nathann



---

archive/issue_comments_094618.json:
```json
{
    "body": "Hi, thanks for the review. You are certainly right that -1 is weird thing in this context and constructor should accept a normal incidence matrix with two ones in each column. I'll start another ticket for this.\n\nI'll set positive review as soon as the tests pass.",
    "created_at": "2012-01-31T11:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9714#issuecomment-94618",
    "user": "https://trac.sagemath.org/admin/accounts/users/brunellus"
}
```

Hi, thanks for the review. You are certainly right that -1 is weird thing in this context and constructor should accept a normal incidence matrix with two ones in each column. I'll start another ticket for this.

I'll set positive review as soon as the tests pass.



---

archive/issue_comments_094619.json:
```json
{
    "body": "What do you say to this adjustment? :-)\n\nLuk\u00e1\u0161.",
    "created_at": "2012-01-31T15:20:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9714#issuecomment-94619",
    "user": "https://trac.sagemath.org/admin/accounts/users/brunellus"
}
```

What do you say to this adjustment? :-)

Lukáš.



---

archive/issue_comments_094620.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-01-31T17:40:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9714#issuecomment-94620",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094621.json:
```json
{
    "body": "> What do you say to this adjustment? :-)\n\n\n\"Stupid me\"\n\nOk, now it's good to go `:-)`\n\nNathann",
    "created_at": "2012-01-31T17:40:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9714#issuecomment-94621",
    "user": "https://github.com/nathanncohen"
}
```

> What do you say to this adjustment? :-)


"Stupid me"

Ok, now it's good to go `:-)`

Nathann



---

archive/issue_comments_094622.json:
```json
{
    "body": "Please state clearly which patches have to be applied.",
    "created_at": "2012-02-03T11:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9714#issuecomment-94622",
    "user": "https://github.com/jdemeyer"
}
```

Please state clearly which patches have to be applied.



---

archive/issue_comments_094623.json:
```json
{
    "body": "Oh, sorry. :-)",
    "created_at": "2012-02-06T09:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9714#issuecomment-94623",
    "user": "https://trac.sagemath.org/admin/accounts/users/brunellus"
}
```

Oh, sorry. :-)



---

archive/issue_comments_094624.json:
```json
{
    "body": "(Just adding a proper commit message.)",
    "created_at": "2012-02-06T10:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9714#issuecomment-94624",
    "user": "https://trac.sagemath.org/admin/accounts/users/brunellus"
}
```

(Just adding a proper commit message.)



---

archive/issue_comments_094625.json:
```json
{
    "body": "The last two patches have one annoyingly long line as commit message.  Could you please shorten the line length.  Multiple lines are allowed, but the first line should make sense by itself.",
    "created_at": "2012-02-15T10:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9714#issuecomment-94625",
    "user": "https://github.com/jdemeyer"
}
```

The last two patches have one annoyingly long line as commit message.  Could you please shorten the line length.  Multiple lines are allowed, but the first line should make sense by itself.



---

archive/issue_comments_094626.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-02-15T10:05:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9714#issuecomment-94626",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_094627.json:
```json
{
    "body": "Attachment [trac_9714_review.patch](tarball://root/attachments/some-uuid/ticket9714/trac_9714_review.patch) by @nathanncohen created at 2012-02-15 10:59:27",
    "created_at": "2012-02-15T10:59:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9714#issuecomment-94627",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_9714_review.patch](tarball://root/attachments/some-uuid/ticket9714/trac_9714_review.patch) by @nathanncohen created at 2012-02-15 10:59:27



---

archive/issue_comments_094628.json:
```json
{
    "body": "Attachment [trac_9714_review_review.patch](tarball://root/attachments/some-uuid/ticket9714/trac_9714_review_review.patch) by @nathanncohen created at 2012-02-15 10:59:53\n\nFixed too `:-)`\n\nNathann",
    "created_at": "2012-02-15T10:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9714#issuecomment-94628",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_9714_review_review.patch](tarball://root/attachments/some-uuid/ticket9714/trac_9714_review_review.patch) by @nathanncohen created at 2012-02-15 10:59:53

Fixed too `:-)`

Nathann



---

archive/issue_comments_094629.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-02-15T10:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9714#issuecomment-94629",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_094630.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-02-22T10:44:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9714#issuecomment-94630",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_024296.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-02-22T10:44:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9714",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9714#event-24296"
}
```
