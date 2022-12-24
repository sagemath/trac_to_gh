# Issue 8403: Steiner Tree

archive/issues_008403.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @jasongrout\n\nHere is a patch containing the function Graph.steiner_tree.\n\nIt consists in finding in a graph, given a set S of vertices, a tree in G of minimum weight/cardinality containing the vertices from S. \n\nEverything is explained in the docstrings anyway :-)\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/8403\n\n",
    "created_at": "2010-02-28T17:57:45Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Steiner Tree",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8403",
    "user": "@nathanncohen"
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

archive/issue_comments_075257.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-28T17:58:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75257",
    "user": "@nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075258.json:
```json
{
    "body": "For an explanation of the Linear Program used to solve this problem, see the LP chapter from : http://code.google.com/p/graph-theory-algorithms-book/\n\nNathann",
    "created_at": "2010-04-08T21:21:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75258",
    "user": "@nathanncohen"
}
```

For an explanation of the Linear Program used to solve this problem, see the LP chapter from : http://code.google.com/p/graph-theory-algorithms-book/

Nathann



---

archive/issue_comments_075259.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-17T21:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75259",
    "user": "@rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075260.json:
```json
{
    "body": "I don't think that, as you claim, minimum spanning trees can be computed in linear time.",
    "created_at": "2010-06-17T21:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75260",
    "user": "@rlmill"
}
```

I don't think that, as you claim, minimum spanning trees can be computed in linear time.



---

archive/issue_comments_075261.json:
```json
{
    "body": "And you are right. I was thinking about spanning trees, as I usually do not care about weights, but min spanning trees require a bit longer. nlog(n) is enough , even if better can be achieved, by first sorting the edges according to their weights, then greedily building a spanning tree..",
    "created_at": "2010-06-18T11:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75261",
    "user": "@nathanncohen"
}
```

And you are right. I was thinking about spanning trees, as I usually do not care about weights, but min spanning trees require a bit longer. nlog(n) is enough , even if better can be achieved, by first sorting the edges according to their weights, then greedily building a spanning tree..



---

archive/issue_comments_075262.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-18T11:14:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75262",
    "user": "@nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075263.json:
```json
{
    "body": "Here it is !\n\nNathann",
    "created_at": "2010-06-18T11:14:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75263",
    "user": "@nathanncohen"
}
```

Here it is !

Nathann



---

archive/issue_comments_075264.json:
```json
{
    "body": "Attachment [trac_8403.patch](tarball://root/attachments/some-uuid/ticket8403/trac_8403.patch) by @rlmill created at 2010-06-18 15:04:22\n\nReplying to [comment:5 ncohen]:\n> And you are right. I was thinking about spanning trees, as I usually do not care about weights...\n\nI don't think spanning tree is linear: the standard method is a BFS/DFS, which is still worst case quadratic. I know this is no longer relevant here, but I want to make sure I have this right. If you do know of a linear time spanning tree algorithm, I'm curious about it.",
    "created_at": "2010-06-18T15:04:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75264",
    "user": "@rlmill"
}
```

Attachment [trac_8403.patch](tarball://root/attachments/some-uuid/ticket8403/trac_8403.patch) by @rlmill created at 2010-06-18 15:04:22

Replying to [comment:5 ncohen]:
> And you are right. I was thinking about spanning trees, as I usually do not care about weights...

I don't think spanning tree is linear: the standard method is a BFS/DFS, which is still worst case quadratic. I know this is no longer relevant here, but I want to make sure I have this right. If you do know of a linear time spanning tree algorithm, I'm curious about it.



---

archive/issue_comments_075265.json:
```json
{
    "body": "That's what I call linear -- not according to the the number of vertices, but according to the size of the input : n+m :-)\n\nNathann",
    "created_at": "2010-06-18T19:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75265",
    "user": "@nathanncohen"
}
```

That's what I call linear -- not according to the the number of vertices, but according to the size of the input : n+m :-)

Nathann



---

archive/issue_comments_075266.json:
```json
{
    "body": "Replying to [comment:8 ncohen]:\n> That's what I call linear -- not according to the the number of vertices, but according to the size of the input : n+m :-)\n\nAha, thanks for clarifying. If you approve of my part2, set the ticket to positive-- all looks good to me!",
    "created_at": "2010-06-19T00:06:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75266",
    "user": "@rlmill"
}
```

Replying to [comment:8 ncohen]:
> That's what I call linear -- not according to the the number of vertices, but according to the size of the input : n+m :-)

Aha, thanks for clarifying. If you approve of my part2, set the ticket to positive-- all looks good to me!



---

archive/issue_comments_075267.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-20T17:46:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75267",
    "user": "@nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075268.json:
```json
{
    "body": "Attachment [trac_8403-part2.patch](tarball://root/attachments/some-uuid/ticket8403/trac_8403-part2.patch) by @nathanncohen created at 2010-06-20 17:46:59\n\nThank you again ! :-)\n\nNathann",
    "created_at": "2010-06-20T17:46:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75268",
    "user": "@nathanncohen"
}
```

Attachment [trac_8403-part2.patch](tarball://root/attachments/some-uuid/ticket8403/trac_8403-part2.patch) by @nathanncohen created at 2010-06-20 17:46:59

Thank you again ! :-)

Nathann



---

archive/issue_comments_075269.json:
```json
{
    "body": "apply before part 2",
    "created_at": "2010-06-28T18:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75269",
    "user": "@rlmill"
}
```

apply before part 2



---

archive/issue_comments_075270.json:
```json
{
    "body": "Attachment [trac_8403-rebased.patch](tarball://root/attachments/some-uuid/ticket8403/trac_8403-rebased.patch) by @rlmill created at 2010-06-29 16:49:24",
    "created_at": "2010-06-29T16:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75270",
    "user": "@rlmill"
}
```

Attachment [trac_8403-rebased.patch](tarball://root/attachments/some-uuid/ticket8403/trac_8403-rebased.patch) by @rlmill created at 2010-06-29 16:49:24



---

archive/issue_comments_075271.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-29T16:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8403#issuecomment-75271",
    "user": "@rlmill"
}
```

Resolution: fixed
