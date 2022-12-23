# Issue 7305: Implement the Higman-Sims graph

archive/issues_007305.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  ncohen\n\nAdd the Higman-Sims graph to the graph generators collection.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7305\n\n",
    "created_at": "2009-10-26T04:14:49Z",
    "labels": [
        "graph theory",
        "minor",
        "enhancement"
    ],
    "title": "Implement the Higman-Sims graph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7305",
    "user": "rbeezer"
}
```
Assignee: rlm

CC:  ncohen

Add the Higman-Sims graph to the graph generators collection.

Issue created by migration from https://trac.sagemath.org/ticket/7305





---

archive/issue_comments_061008.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-10-26T04:18:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7305#issuecomment-61008",
    "user": "rbeezer"
}
```

Attachment



---

archive/issue_comments_061009.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-26T04:18:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7305#issuecomment-61009",
    "user": "rbeezer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061010.json:
```json
{
    "body": "Two remarks :\n* In my memory there are two different lists of graphs in the file graph_generator.py, and you only added yours once\n* I would have written \n  {{{\n  relabel - default: True.\n  }}}\n      \n  as \n\n  {{{\n  ``relabel`` - default: ``True``.\n  }}}",
    "created_at": "2009-11-07T16:33:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7305#issuecomment-61010",
    "user": "ncohen"
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

archive/issue_comments_061011.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-07T16:33:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7305#issuecomment-61011",
    "user": "ncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061012.json:
```json
{
    "body": "Attachment\n\nHi Nathann,\n\nNice catch, on both counts.  Thanks for the review.\n\nThe \"_2\" patch is self-contained (ie apply just the single revised patch on a fresh install) and addresses both your comments.\n\nRob",
    "created_at": "2009-11-08T22:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7305#issuecomment-61012",
    "user": "rbeezer"
}
```

Attachment

Hi Nathann,

Nice catch, on both counts.  Thanks for the review.

The "_2" patch is self-contained (ie apply just the single revised patch on a fresh install) and addresses both your comments.

Rob



---

archive/issue_comments_061013.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-08T22:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7305#issuecomment-61013",
    "user": "rbeezer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061014.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-09T16:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7305#issuecomment-61014",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061015.json:
```json
{
    "body": "Then I can swear I never saw any cleaner patch.... Thanks for this addition ! :-)\n\nNathann",
    "created_at": "2009-11-09T16:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7305#issuecomment-61015",
    "user": "ncohen"
}
```

Then I can swear I never saw any cleaner patch.... Thanks for this addition ! :-)

Nathann



---

archive/issue_comments_061016.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-12T08:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7305#issuecomment-61016",
    "user": "mhansen"
}
```

Resolution: fixed
