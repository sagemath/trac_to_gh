# Issue 7365: Petersen's 2-factor theorem

archive/issues_007365.json:
```json
{
    "body": "Assignee: @rlmill\n\nImplement a function corresponding to Petersen's theorem on 2-factors.\n\nThis theorem says that any 2r-regular graphs can be decomposed in 2-factors. If the graph is not regular and is of maximum degree Delta, then it can be decomposed as an union of Delta/2 disjoints (<=2)-factors.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7365\n\n",
    "created_at": "2009-10-31T20:53:35Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Petersen's 2-factor theorem",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7365",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

Implement a function corresponding to Petersen's theorem on 2-factors.

This theorem says that any 2r-regular graphs can be decomposed in 2-factors. If the graph is not regular and is of maximum degree Delta, then it can be decomposed as an union of Delta/2 disjoints (<=2)-factors.

Issue created by migration from https://trac.sagemath.org/ticket/7365





---

archive/issue_comments_061608.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-18T18:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7365#issuecomment-61608",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061609.json:
```json
{
    "body": "If you're introducing a new module in sage.graphs, the header of the file should be much more descriptive of what the module is for, etc... Take a look at some of the other files for examples.\n\nI'm (personally) very curious about what else you plan on including in `graph_decompositions`...\n\nThe patch applies cleanly, and the code looks good. Once again, I'd like to see a little more examples in the documentation.",
    "created_at": "2009-12-15T17:27:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7365#issuecomment-61609",
    "user": "https://github.com/rlmill"
}
```

If you're introducing a new module in sage.graphs, the header of the file should be much more descriptive of what the module is for, etc... Take a look at some of the other files for examples.

I'm (personally) very curious about what else you plan on including in `graph_decompositions`...

The patch applies cleanly, and the code looks good. Once again, I'd like to see a little more examples in the documentation.



---

archive/issue_comments_061610.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-15T17:27:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7365#issuecomment-61610",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061611.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-18T08:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7365#issuecomment-61611",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061612.json:
```json
{
    "body": "Hello !!!\n\nAs mentionned, I moved this function toward graph.py, and will patiently wait for the splitting of graph.py to begin creating new files.. :-)\n\n(please do not forget to install GLPK or CBC before testing it because of #7734)\n\nNathann",
    "created_at": "2009-12-18T08:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7365#issuecomment-61612",
    "user": "https://github.com/nathanncohen"
}
```

Hello !!!

As mentionned, I moved this function toward graph.py, and will patiently wait for the splitting of graph.py to begin creating new files.. :-)

(please do not forget to install GLPK or CBC before testing it because of #7734)

Nathann



---

archive/issue_comments_061613.json:
```json
{
    "body": "Attachment [trac_7365.patch](tarball://root/attachments/some-uuid/ticket7365/trac_7365.patch) by @nathanncohen created at 2009-12-18 08:54:06\n\nI tried to find another example, but could not find any interesting/funny one (the theorem and its proof by themselves are enough to make me laugh :-) ). If you can think of a good one, just tell me and I'll add it :-)\n\nNathann",
    "created_at": "2009-12-18T08:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7365#issuecomment-61613",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_7365.patch](tarball://root/attachments/some-uuid/ticket7365/trac_7365.patch) by @nathanncohen created at 2009-12-18 08:54:06

I tried to find another example, but could not find any interesting/funny one (the theorem and its proof by themselves are enough to make me laugh :-) ). If you can think of a good one, just tell me and I'll add it :-)

Nathann



---

archive/issue_comments_061614.json:
```json
{
    "body": "Attachment [tmp_4.png](tarball://root/attachments/some-uuid/ticket7365/tmp_4.png) by @rlmill created at 2009-12-18 19:21:29",
    "created_at": "2009-12-18T19:21:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7365#issuecomment-61614",
    "user": "https://github.com/rlmill"
}
```

Attachment [tmp_4.png](tarball://root/attachments/some-uuid/ticket7365/tmp_4.png) by @rlmill created at 2009-12-18 19:21:29



---

archive/issue_comments_061615.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-18T19:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7365#issuecomment-61615",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061616.json:
```json
{
    "body": "Attachment [trac_7365-doctest.patch](tarball://root/attachments/some-uuid/ticket7365/trac_7365-doctest.patch) by @rlmill created at 2009-12-18 19:22:58",
    "created_at": "2009-12-18T19:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7365#issuecomment-61616",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_7365-doctest.patch](tarball://root/attachments/some-uuid/ticket7365/trac_7365-doctest.patch) by @rlmill created at 2009-12-18 19:22:58



---

archive/issue_events_007588.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-12-19T22:59:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7365",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7365#event-7588"
}
```



---

archive/issue_comments_061617.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-19T22:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7365#issuecomment-61617",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
