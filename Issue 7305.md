# Issue 7305: Implement the Higman-Sims graph

archive/issues_007305.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @nathanncohen\n\nAdd the Higman-Sims graph to the graph generators collection.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7305\n\n",
    "created_at": "2009-10-26T04:14:49Z",
    "labels": [
        "component: graph theory",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "Implement the Higman-Sims graph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7305",
    "user": "https://github.com/rbeezer"
}
```
Assignee: @rlmill

CC:  @nathanncohen

Add the Higman-Sims graph to the graph generators collection.

Issue created by migration from https://trac.sagemath.org/ticket/7305





---

archive/issue_comments_060895.json:
```json
{
    "body": "Attachment [trac_7305_higman_sims_graph.patch](tarball://root/attachments/some-uuid/ticket7305/trac_7305_higman_sims_graph.patch) by @rbeezer created at 2009-10-26 04:18:36",
    "created_at": "2009-10-26T04:18:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7305#issuecomment-60895",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_7305_higman_sims_graph.patch](tarball://root/attachments/some-uuid/ticket7305/trac_7305_higman_sims_graph.patch) by @rbeezer created at 2009-10-26 04:18:36



---

archive/issue_comments_060896.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-26T04:18:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7305#issuecomment-60896",
    "user": "https://github.com/rbeezer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060897.json:
```json
{
    "body": "Two remarks :\n* In my memory there are two different lists of graphs in the file graph_generator.py, and you only added yours once\n* I would have written \n  {{{\n  relabel - default: True.\n  }}}\n      \n  as \n\n  {{{\n  ``relabel`` - default: ``True``.\n  }}}",
    "created_at": "2009-11-07T16:33:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7305#issuecomment-60897",
    "user": "https://github.com/nathanncohen"
}
```

Two remarks :
* In my memory there are two different lists of graphs in the file graph_generator.py, and you only added yours once
* I would have written 
  {{{
  relabel - default: True.
  }}}
      
  as 

  {{{
  ``relabel`` - default: ``True``.
  }}}



---

archive/issue_comments_060898.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-07T16:33:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7305#issuecomment-60898",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060899.json:
```json
{
    "body": "Attachment [trac_7305_higman_sims_graph_2.patch](tarball://root/attachments/some-uuid/ticket7305/trac_7305_higman_sims_graph_2.patch) by @rbeezer created at 2009-11-08 22:21:14\n\nHi Nathann,\n\nNice catch, on both counts.  Thanks for the review.\n\nThe \"_2\" patch is self-contained (ie apply just the single revised patch on a fresh install) and addresses both your comments.\n\nRob",
    "created_at": "2009-11-08T22:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7305#issuecomment-60899",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_7305_higman_sims_graph_2.patch](tarball://root/attachments/some-uuid/ticket7305/trac_7305_higman_sims_graph_2.patch) by @rbeezer created at 2009-11-08 22:21:14

Hi Nathann,

Nice catch, on both counts.  Thanks for the review.

The "_2" patch is self-contained (ie apply just the single revised patch on a fresh install) and addresses both your comments.

Rob



---

archive/issue_comments_060900.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-08T22:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7305#issuecomment-60900",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060901.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-09T16:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7305#issuecomment-60901",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060902.json:
```json
{
    "body": "Then I can swear I never saw any cleaner patch.... Thanks for this addition ! :-)\n\nNathann",
    "created_at": "2009-11-09T16:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7305#issuecomment-60902",
    "user": "https://github.com/nathanncohen"
}
```

Then I can swear I never saw any cleaner patch.... Thanks for this addition ! :-)

Nathann



---

archive/issue_events_007528.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-12T08:14:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7305",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7305#event-7528"
}
```



---

archive/issue_comments_060903.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-12T08:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7305#issuecomment-60903",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
