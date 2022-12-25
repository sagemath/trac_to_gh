# Issue 8403: Steiner Tree

archive/issues_008403.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @jasongrout\n\nHere is a patch containing the function Graph.steiner_tree.\n\nIt consists in finding in a graph, given a set S of vertices, a tree in G of minimum weight/cardinality containing the vertices from S. \n\nEverything is explained in the docstrings anyway :-)\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/8403\n\n",
    "created_at": "2010-02-28T17:57:45Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Steiner Tree",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8403",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

CC:  @jasongrout

Here is a patch containing the function Graph.steiner_tree.

It consists in finding in a graph, given a set S of vertices, a tree in G of minimum weight/cardinality containing the vertices from S. 

Everything is explained in the docstrings anyway :-)

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/8403





---

archive/issue_comments_075133.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-28T17:58:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75133",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075134.json:
```json
{
    "body": "For an explanation of the Linear Program used to solve this problem, see the LP chapter from : http://code.google.com/p/graph-theory-algorithms-book/\n\nNathann",
    "created_at": "2010-04-08T21:21:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75134",
    "user": "https://github.com/nathanncohen"
}
```

For an explanation of the Linear Program used to solve this problem, see the LP chapter from : http://code.google.com/p/graph-theory-algorithms-book/

Nathann



---

archive/issue_comments_075135.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-17T21:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75135",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075136.json:
```json
{
    "body": "I don't think that, as you claim, minimum spanning trees can be computed in linear time.",
    "created_at": "2010-06-17T21:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75136",
    "user": "https://github.com/rlmill"
}
```

I don't think that, as you claim, minimum spanning trees can be computed in linear time.



---

archive/issue_comments_075137.json:
```json
{
    "body": "And you are right. I was thinking about spanning trees, as I usually do not care about weights, but min spanning trees require a bit longer. nlog(n) is enough , even if better can be achieved, by first sorting the edges according to their weights, then greedily building a spanning tree..",
    "created_at": "2010-06-18T11:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75137",
    "user": "https://github.com/nathanncohen"
}
```

And you are right. I was thinking about spanning trees, as I usually do not care about weights, but min spanning trees require a bit longer. nlog(n) is enough , even if better can be achieved, by first sorting the edges according to their weights, then greedily building a spanning tree..



---

archive/issue_comments_075138.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-18T11:14:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75138",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075139.json:
```json
{
    "body": "Here it is !\n\nNathann",
    "created_at": "2010-06-18T11:14:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75139",
    "user": "https://github.com/nathanncohen"
}
```

Here it is !

Nathann



---

archive/issue_comments_075140.json:
```json
{
    "body": "Attachment [trac_8403.patch](tarball://root/attachments/some-uuid/ticket8403/trac_8403.patch) by @rlmill created at 2010-06-18 15:04:22\n\nReplying to [comment:5 ncohen]:\n> And you are right. I was thinking about spanning trees, as I usually do not care about weights...\n\nI don't think spanning tree is linear: the standard method is a BFS/DFS, which is still worst case quadratic. I know this is no longer relevant here, but I want to make sure I have this right. If you do know of a linear time spanning tree algorithm, I'm curious about it.",
    "created_at": "2010-06-18T15:04:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75140",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_8403.patch](tarball://root/attachments/some-uuid/ticket8403/trac_8403.patch) by @rlmill created at 2010-06-18 15:04:22

Replying to [comment:5 ncohen]:
> And you are right. I was thinking about spanning trees, as I usually do not care about weights...

I don't think spanning tree is linear: the standard method is a BFS/DFS, which is still worst case quadratic. I know this is no longer relevant here, but I want to make sure I have this right. If you do know of a linear time spanning tree algorithm, I'm curious about it.



---

archive/issue_comments_075141.json:
```json
{
    "body": "That's what I call linear -- not according to the the number of vertices, but according to the size of the input : n+m :-)\n\nNathann",
    "created_at": "2010-06-18T19:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75141",
    "user": "https://github.com/nathanncohen"
}
```

That's what I call linear -- not according to the the number of vertices, but according to the size of the input : n+m :-)

Nathann



---

archive/issue_comments_075142.json:
```json
{
    "body": "Replying to [comment:8 ncohen]:\n> That's what I call linear -- not according to the the number of vertices, but according to the size of the input : n+m :-)\n\nAha, thanks for clarifying. If you approve of my part2, set the ticket to positive-- all looks good to me!",
    "created_at": "2010-06-19T00:06:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75142",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:8 ncohen]:
> That's what I call linear -- not according to the the number of vertices, but according to the size of the input : n+m :-)

Aha, thanks for clarifying. If you approve of my part2, set the ticket to positive-- all looks good to me!



---

archive/issue_comments_075143.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-20T17:46:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75143",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075144.json:
```json
{
    "body": "Attachment [trac_8403-part2.patch](tarball://root/attachments/some-uuid/ticket8403/trac_8403-part2.patch) by @nathanncohen created at 2010-06-20 17:46:59\n\nThank you again ! :-)\n\nNathann",
    "created_at": "2010-06-20T17:46:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75144",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_8403-part2.patch](tarball://root/attachments/some-uuid/ticket8403/trac_8403-part2.patch) by @nathanncohen created at 2010-06-20 17:46:59

Thank you again ! :-)

Nathann



---

archive/issue_comments_075145.json:
```json
{
    "body": "apply before part 2",
    "created_at": "2010-06-28T18:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75145",
    "user": "https://github.com/rlmill"
}
```

apply before part 2



---

archive/issue_comments_075146.json:
```json
{
    "body": "Attachment [trac_8403-rebased.patch](tarball://root/attachments/some-uuid/ticket8403/trac_8403-rebased.patch) by @rlmill created at 2010-06-29 16:49:24",
    "created_at": "2010-06-29T16:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75146",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_8403-rebased.patch](tarball://root/attachments/some-uuid/ticket8403/trac_8403-rebased.patch) by @rlmill created at 2010-06-29 16:49:24



---

archive/issue_events_008588.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-06-29T16:49:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8403#event-8588"
}
```



---

archive/issue_comments_075147.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-29T16:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75147",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
