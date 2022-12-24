# Issue 7274: graphs: Maximum flow algorithms

archive/issues_007274.json:
```json
{
    "body": "Assignee: @rlmill\n\nThis is work from Sage Days 16 in Barcelona.\n\nFirst patch implements Edmonds-Karp and Dinic algorithm for DiGraph. Second one uses this implementation to find maximum matching in bipartite graphs.\n\nI also include worksheet with simple usage example.\n\nPlease review. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7274\n\n",
    "created_at": "2009-10-23T21:15:13Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "graphs: Maximum flow algorithms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7274",
    "user": "tombuc"
}
```
Assignee: @rlmill

This is work from Sage Days 16 in Barcelona.

First patch implements Edmonds-Karp and Dinic algorithm for DiGraph. Second one uses this implementation to find maximum matching in bipartite graphs.

I also include worksheet with simple usage example.

Please review. 

Issue created by migration from https://trac.sagemath.org/ticket/7274





---

archive/issue_comments_060529.json:
```json
{
    "body": "Attachment [maxflowsolver.patch](tarball://root/attachments/some-uuid/ticket7274/maxflowsolver.patch) by tombuc created at 2009-10-23 21:15:50\n\nMaximum flow algorithms",
    "created_at": "2009-10-23T21:15:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7274#issuecomment-60529",
    "user": "tombuc"
}
```

Attachment [maxflowsolver.patch](tarball://root/attachments/some-uuid/ticket7274/maxflowsolver.patch) by tombuc created at 2009-10-23 21:15:50

Maximum flow algorithms



---

archive/issue_comments_060530.json:
```json
{
    "body": "Attachment [marriage.patch](tarball://root/attachments/some-uuid/ticket7274/marriage.patch) by tombuc created at 2009-10-23 21:16:27\n\nMaximum matching in bipartite graphs",
    "created_at": "2009-10-23T21:16:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7274#issuecomment-60530",
    "user": "tombuc"
}
```

Attachment [marriage.patch](tarball://root/attachments/some-uuid/ticket7274/marriage.patch) by tombuc created at 2009-10-23 21:16:27

Maximum matching in bipartite graphs



---

archive/issue_comments_060531.json:
```json
{
    "body": "Attachment [MaxflowTest.sws](tarball://root/attachments/some-uuid/ticket7274/MaxflowTest.sws) by tombuc created at 2009-10-23 21:17:00\n\nExample usage",
    "created_at": "2009-10-23T21:17:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7274#issuecomment-60531",
    "user": "tombuc"
}
```

Attachment [MaxflowTest.sws](tarball://root/attachments/some-uuid/ticket7274/MaxflowTest.sws) by tombuc created at 2009-10-23 21:17:00

Example usage



---

archive/issue_comments_060532.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-23T21:27:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7274#issuecomment-60532",
    "user": "tombuc"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060533.json:
```json
{
    "body": "I wrote a patch at ticket #6680 including flows and (possibly weighted) matchings ( in the general case ). This patch still hasn't been reviewed, but it could be interesting to compare the performances before merging any of them :-)",
    "created_at": "2009-10-24T00:06:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7274#issuecomment-60533",
    "user": "@nathanncohen"
}
```

I wrote a patch at ticket #6680 including flows and (possibly weighted) matchings ( in the general case ). This patch still hasn't been reviewed, but it could be interesting to compare the performances before merging any of them :-)



---

archive/issue_comments_060534.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-15T18:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7274#issuecomment-60534",
    "user": "@rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060535.json:
```json
{
    "body": "Patch applies cleanly and passes tests, and I'm ready to approve except for:\n\n1. `def path_iterator(P)` This function needs a docstring. The 100% rule applies here too. Just a simple sentence saying what it does and an example or two will do.",
    "created_at": "2009-12-15T18:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7274#issuecomment-60535",
    "user": "@rlmill"
}
```

Patch applies cleanly and passes tests, and I'm ready to approve except for:

1. `def path_iterator(P)` This function needs a docstring. The 100% rule applies here too. Just a simple sentence saying what it does and an example or two will do.



---

archive/issue_comments_060536.json:
```json
{
    "body": "As #7592 and #7593 just got reviewed, this patch can not be directly added to sage : there are now functions Graph.flow and Graph.matching available in Sage ( well, in the next version.. )\n\nThe problem with these functions is that they still depend on GLPK or CBC, two optional packages that can not be made standard are their licenses are not compatible, so it would be good to have pure Python equivalent.\n\nSeveral remarks\n\n* In #7600 and in Graph.coloring, the user can chose which algorithm he would like to use to solve the problem. Maybe the best way is to copy this behaviour in the case of flows and matching to have the two algorithms available.\n* It could be very useful to know how these algorithms compare in terms of performances. This will be much easier to test when flow and matching will be natively in Sage\n* #7634 may not be ready, but time could come soon : with this update the efficiency of the shortest_path method will be improved, and the speed of this implementation too.\n* Somwhere in the code, I saw a call to \n\n```\npath = R.shortest_path(source, sink,by_weight=False, bidirectional=False)\n```\n\n      I wondered why you chosed not to use the bidirectional version of the algorithm, as it is expected to be faster.. :-)\n\nThank you for your work !!!",
    "created_at": "2009-12-16T19:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7274#issuecomment-60536",
    "user": "@nathanncohen"
}
```

As #7592 and #7593 just got reviewed, this patch can not be directly added to sage : there are now functions Graph.flow and Graph.matching available in Sage ( well, in the next version.. )

The problem with these functions is that they still depend on GLPK or CBC, two optional packages that can not be made standard are their licenses are not compatible, so it would be good to have pure Python equivalent.

Several remarks

* In #7600 and in Graph.coloring, the user can chose which algorithm he would like to use to solve the problem. Maybe the best way is to copy this behaviour in the case of flows and matching to have the two algorithms available.
* It could be very useful to know how these algorithms compare in terms of performances. This will be much easier to test when flow and matching will be natively in Sage
* #7634 may not be ready, but time could come soon : with this update the efficiency of the shortest_path method will be improved, and the speed of this implementation too.
* Somwhere in the code, I saw a call to 

```
path = R.shortest_path(source, sink,by_weight=False, bidirectional=False)
```

      I wondered why you chosed not to use the bidirectional version of the algorithm, as it is expected to be faster.. :-)

Thank you for your work !!!



---

archive/issue_comments_060537.json:
```json
{
    "body": "Apparently #3930 should be closed when this is merged.",
    "created_at": "2009-12-18T17:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7274#issuecomment-60537",
    "user": "@jasongrout"
}
```

Apparently #3930 should be closed when this is merged.



---

archive/issue_comments_060538.json:
```json
{
    "body": "We have a Python version for max flow through #9350 ... So as this ticket has been here for 10 months now..\n\nNathann",
    "created_at": "2010-10-09T08:29:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7274#issuecomment-60538",
    "user": "@nathanncohen"
}
```

We have a Python version for max flow through #9350 ... So as this ticket has been here for 10 months now..

Nathann



---

archive/issue_comments_060539.json:
```json
{
    "body": "Close as duplicate of #9350.",
    "created_at": "2010-10-09T08:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7274#issuecomment-60539",
    "user": "mvngu"
}
```

Close as duplicate of #9350.



---

archive/issue_comments_060540.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-10-09T08:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7274#issuecomment-60540",
    "user": "mvngu"
}
```

Resolution: duplicate
