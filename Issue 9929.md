# Issue 9929: Additional test in is_even_hole_free

archive/issues_009929.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nThis bug has been reported in #9925, and fixed by #9420. We just want to make sure it does not appear again ! `:-)`\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9930\n\n",
    "created_at": "2010-09-17T08:08:52Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Additional test in is_even_hole_free",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9929",
    "user": "ncohen"
}
```
Assignee: jason, ncohen, rlm

This bug has been reported in #9925, and fixed by #9420. We just want to make sure it does not appear again ! `:-)`

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/9930





---

archive/issue_comments_098876.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-17T08:16:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9929#issuecomment-98876",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098877.json:
```json
{
    "body": "Attachment [trac_9930.patch](tarball://root/attachments/some-uuid/ticket9930/trac_9930.patch) by ncohen created at 2010-09-17 08:16:22",
    "created_at": "2010-09-17T08:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9929#issuecomment-98877",
    "user": "ncohen"
}
```

Attachment [trac_9930.patch](tarball://root/attachments/some-uuid/ticket9930/trac_9930.patch) by ncohen created at 2010-09-17 08:16:22



---

archive/issue_comments_098878.json:
```json
{
    "body": "I tried the loop included in this patch with 100 000 instead of 100, and it still works.... Sounds like we are safe on this side `:-)`\n\nNathann",
    "created_at": "2010-09-17T08:48:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9929#issuecomment-98878",
    "user": "ncohen"
}
```

I tried the loop included in this patch with 100 000 instead of 100, and it still works.... Sounds like we are safe on this side `:-)`

Nathann



---

archive/issue_comments_098879.json:
```json
{
    "body": "Replying to [comment:3 ncohen]:\n> I tried the loop included in this patch with 100 000 instead of 100, and it still works.... Sounds like we are safe on this side `:-)`\n> \n> Nathann\n\nunless there is a probabilistic argument that with high probability we run into the cases we are interested in testing here,\nthis won't fly... Random tests don't prove much otherwise. And here you don't even know what to look for, right?",
    "created_at": "2010-09-19T08:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9929#issuecomment-98879",
    "user": "dimpase"
}
```

Replying to [comment:3 ncohen]:
> I tried the loop included in this patch with 100 000 instead of 100, and it still works.... Sounds like we are safe on this side `:-)`
> 
> Nathann

unless there is a probabilistic argument that with high probability we run into the cases we are interested in testing here,
this won't fly... Random tests don't prove much otherwise. And here you don't even know what to look for, right?



---

archive/issue_comments_098880.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-09-19T08:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9929#issuecomment-98880",
    "user": "dimpase"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_098881.json:
```json
{
    "body": "> unless there is a probabilistic argument that with high probability we run into the cases we are interested in testing here,\n> this won't fly... Random tests don't prove much otherwise. And here you don't even know what to look for, right?\n\nWell, there is a practical argument saying that the mistake appeared with a probability of 1%, as my comments on #9925 indicated (and which I tried on even longer sequences of tests). Besides, the graph I create from its sparse6_string is known to create a mistake on the current version of Sage. What do you think we could do besides that ?\n\nNathann",
    "created_at": "2010-09-19T08:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9929#issuecomment-98881",
    "user": "ncohen"
}
```

> unless there is a probabilistic argument that with high probability we run into the cases we are interested in testing here,
> this won't fly... Random tests don't prove much otherwise. And here you don't even know what to look for, right?

Well, there is a practical argument saying that the mistake appeared with a probability of 1%, as my comments on #9925 indicated (and which I tried on even longer sequences of tests). Besides, the graph I create from its sparse6_string is known to create a mistake on the current version of Sage. What do you think we could do besides that ?

Nathann



---

archive/issue_comments_098882.json:
```json
{
    "body": "\n```\nthe graph I create from its sparse6_string is known to create a mistake on the current version of Sage. \n```\n\nOK, this is fair enough. I'll give it a positive review as soon as it is marked as \"needs review\"",
    "created_at": "2010-09-19T08:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9929#issuecomment-98882",
    "user": "dimpase"
}
```


```
the graph I create from its sparse6_string is known to create a mistake on the current version of Sage. 
```

OK, this is fair enough. I'll give it a positive review as soon as it is marked as "needs review"



---

archive/issue_comments_098883.json:
```json
{
    "body": "> OK, this is fair enough. I'll give it a positive review as soon as it is marked as \"needs review\" \n\nThen let it be ! `:-)`\n\nNathann",
    "created_at": "2010-09-19T09:00:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9929#issuecomment-98883",
    "user": "ncohen"
}
```

> OK, this is fair enough. I'll give it a positive review as soon as it is marked as "needs review" 

Then let it be ! `:-)`

Nathann



---

archive/issue_comments_098884.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-09-19T09:00:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9929#issuecomment-98884",
    "user": "ncohen"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_098885.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-19T09:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9929#issuecomment-98885",
    "user": "dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098886.json:
```json
{
    "body": "Thanksssssss !! And many other thanks for the review of subgraph_search `:-)`\n\nNathann",
    "created_at": "2010-09-19T09:04:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9929#issuecomment-98886",
    "user": "ncohen"
}
```

Thanksssssss !! And many other thanks for the review of subgraph_search `:-)`

Nathann



---

archive/issue_comments_098887.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T08:39:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9929#issuecomment-98887",
    "user": "mpatel"
}
```

Resolution: fixed
