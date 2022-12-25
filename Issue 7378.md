# Issue 7378: Subdivide edges in a graph

archive/issues_007378.json:
```json
{
    "body": "Assignee: @rlmill\n\nIt is often useful to subdivide the edges of a graph, so there should be a function in Sage for this.\n\nWhen an edge e between u and v is subdivided in a DiGraph, perhaps the best thing to do would be to name the new vertices as (e, 0), (e, 1), (e, 2), etc ...\n\nWe are left with a similar problem concerning the Graphs and here I have to admit I do not know which name to use without inducing some orientation..\n\nThis being said, it has to be done ! :-)\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/7378\n\n",
    "created_at": "2009-11-03T09:26:13Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Subdivide edges in a graph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7378",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

It is often useful to subdivide the edges of a graph, so there should be a function in Sage for this.

When an edge e between u and v is subdivided in a DiGraph, perhaps the best thing to do would be to name the new vertices as (e, 0), (e, 1), (e, 2), etc ...

We are left with a similar problem concerning the Graphs and here I have to admit I do not know which name to use without inducing some orientation..

This being said, it has to be done ! :-)

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/7378





---

archive/issue_comments_061913.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-04T15:15:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61913",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061914.json:
```json
{
    "body": "Here it is !!!\n\nNathann",
    "created_at": "2010-04-04T15:15:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61914",
    "user": "https://github.com/nathanncohen"
}
```

Here it is !!!

Nathann



---

archive/issue_comments_061915.json:
```json
{
    "body": "In the docs, you say that the following are valid forms:\n\nG.add_edge( 1, 2, 8 )\n\nG.add_edge( (1, 2), 8 )\n\nHowever, reading the code seems to indicate that it should be subdivide_edge, not add_edge.",
    "created_at": "2010-04-20T04:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61915",
    "user": "https://github.com/jasongrout"
}
```

In the docs, you say that the following are valid forms:

G.add_edge( 1, 2, 8 )

G.add_edge( (1, 2), 8 )

However, reading the code seems to indicate that it should be subdivide_edge, not add_edge.



---

archive/issue_comments_061916.json:
```json
{
    "body": "Changing assignee from @rlmill to @jasongrout.",
    "created_at": "2010-04-20T04:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61916",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @rlmill to @jasongrout.



---

archive/issue_comments_061917.json:
```json
{
    "body": "Indeed. Fixed :-)\n\nNathann",
    "created_at": "2010-04-20T07:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61917",
    "user": "https://github.com/nathanncohen"
}
```

Indeed. Fixed :-)

Nathann



---

archive/issue_comments_061918.json:
```json
{
    "body": "I just applied this patch on top of #7608, and there was nothing wrong to report :-)",
    "created_at": "2010-04-23T11:43:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61918",
    "user": "https://github.com/nathanncohen"
}
```

I just applied this patch on top of #7608, and there was nothing wrong to report :-)



---

archive/issue_comments_061919.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-17T20:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61919",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061920.json:
```json
{
    "body": "\"If the given edge is labelled with `l`, all the edges created by the subdivision will have the same label.\"\n\n... You should also specify what happens to labels when `l` is not given. In addition, you should have all these cases doctested.",
    "created_at": "2010-06-17T20:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61920",
    "user": "https://github.com/rlmill"
}
```

"If the given edge is labelled with `l`, all the edges created by the subdivision will have the same label."

... You should also specify what happens to labels when `l` is not given. In addition, you should have all these cases doctested.



---

archive/issue_comments_061921.json:
```json
{
    "body": "> ... You should also specify what happens to labels when `l` is not given. In addition, you should have all these cases doctested.\n\n\nThat said, all tests pass. So once the above is addressed, I'll probably be happy.",
    "created_at": "2010-06-17T20:53:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61921",
    "user": "https://github.com/rlmill"
}
```

> ... You should also specify what happens to labels when `l` is not given. In addition, you should have all these cases doctested.


That said, all tests pass. So once the above is addressed, I'll probably be happy.



---

archive/issue_comments_061922.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-18T11:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61922",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061923.json:
```json
{
    "body": "What about this ? :-)\n\nNathann",
    "created_at": "2010-06-18T11:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61923",
    "user": "https://github.com/nathanncohen"
}
```

What about this ? :-)

Nathann



---

archive/issue_comments_061924.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-18T15:20:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61924",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061925.json:
```json
{
    "body": "I don't think this quite works as advertised. If I have edge `(u, v, 1)` and I do `G.subdivide_edge((u, v, 2), 5)`, then the edge `(u, v, 1)` is never deleted.\n\nIs the input label the new label, or the label of the existing edge?\n\nMaybe there should be a `new_label` argument instead? I'm not sure the best way to approach this, and I'm interested in your opinion.",
    "created_at": "2010-06-18T15:20:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61925",
    "user": "https://github.com/rlmill"
}
```

I don't think this quite works as advertised. If I have edge `(u, v, 1)` and I do `G.subdivide_edge((u, v, 2), 5)`, then the edge `(u, v, 1)` is never deleted.

Is the input label the new label, or the label of the existing edge?

Maybe there should be a `new_label` argument instead? I'm not sure the best way to approach this, and I'm interested in your opinion.



---

archive/issue_comments_061926.json:
```json
{
    "body": "Oh... The behaviour I had in mind was rather to raise an ValueError excetion saying : edge(u,v,2) does not exist. I really think of this as a topological method, so the user is expected to relabel his edges later if there is any need of it. I really wanted the edge to be \"split\" into several parts, all bearing the same label. \n\nWhat would you think about it ? I'll update the patch to match this behaviour, just because it is easy to do so, though if you don't like it we can still remove it ! :-)\n\nNathann",
    "created_at": "2010-06-20T17:51:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61926",
    "user": "https://github.com/nathanncohen"
}
```

Oh... The behaviour I had in mind was rather to raise an ValueError excetion saying : edge(u,v,2) does not exist. I really think of this as a topological method, so the user is expected to relabel his edges later if there is any need of it. I really wanted the edge to be "split" into several parts, all bearing the same label. 

What would you think about it ? I'll update the patch to match this behaviour, just because it is easy to do so, though if you don't like it we can still remove it ! :-)

Nathann



---

archive/issue_comments_061927.json:
```json
{
    "body": "Attachment [trac_7378.patch](tarball://root/attachments/some-uuid/ticket7378/trac_7378.patch) by @nathanncohen created at 2010-06-20 18:04:14",
    "created_at": "2010-06-20T18:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61927",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_7378.patch](tarball://root/attachments/some-uuid/ticket7378/trac_7378.patch) by @nathanncohen created at 2010-06-20 18:04:14



---

archive/issue_comments_061928.json:
```json
{
    "body": "Apply after trac_7378.patch",
    "created_at": "2010-06-21T17:38:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61928",
    "user": "https://github.com/rlmill"
}
```

Apply after trac_7378.patch



---

archive/issue_comments_061929.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-21T17:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61929",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061930.json:
```json
{
    "body": "Attachment [trac_7378-ref.patch](tarball://root/attachments/some-uuid/ticket7378/trac_7378-ref.patch) by @rlmill created at 2010-06-21 17:40:17\n\nReplying to [comment:10 ncohen]:\n> I really wanted the edge to be \"split\" into several parts, all bearing the same label. \n\n\nThanks for clarifying. I've tried to make this clear in the documentation. If you approve of my referee patch, please set the ticket to positive review.",
    "created_at": "2010-06-21T17:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61930",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_7378-ref.patch](tarball://root/attachments/some-uuid/ticket7378/trac_7378-ref.patch) by @rlmill created at 2010-06-21 17:40:17

Replying to [comment:10 ncohen]:
> I really wanted the edge to be "split" into several parts, all bearing the same label. 


Thanks for clarifying. I've tried to make this clear in the documentation. If you approve of my referee patch, please set the ticket to positive review.



---

archive/issue_comments_061931.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-21T20:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61931",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061932.json:
```json
{
    "body": "Thank youuuuuuuuuuu !!! :-)\n\nNathann",
    "created_at": "2010-06-21T20:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61932",
    "user": "https://github.com/nathanncohen"
}
```

Thank youuuuuuuuuuu !!! :-)

Nathann



---

archive/issue_comments_061933.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-06-21T20:17:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61933",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_061934.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-21T20:17:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61934",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061935.json:
```json
{
    "body": "wrong alert, positive review ! :-)\n\nNathann",
    "created_at": "2010-06-21T20:30:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61935",
    "user": "https://github.com/nathanncohen"
}
```

wrong alert, positive review ! :-)

Nathann



---

archive/issue_comments_061936.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-21T20:30:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61936",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061937.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-29T16:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7378#issuecomment-61937",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_017445.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-06-29T16:43:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7378",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7378#event-17445"
}
```
