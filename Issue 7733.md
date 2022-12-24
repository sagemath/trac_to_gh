# Issue 7733: Graph(g) and DiGraph(g) do not keep the embedding !

archive/issues_007733.json:
```json
{
    "body": "Assignee: rlm\n\nJust try ::\n\n\n```\nsage: g = graphs.PetersenGraph()\nsage: g.show()\nsage: Graph(g).show()\nsage: DiGraph(g).show()\n```\n\n\nThe positions are not kept.... Why isn't Graph(g) equivalent to copy(g) ?\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/7733\n\n",
    "created_at": "2009-12-18T08:25:18Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Graph(g) and DiGraph(g) do not keep the embedding !",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7733",
    "user": "ncohen"
}
```
Assignee: rlm

Just try ::


```
sage: g = graphs.PetersenGraph()
sage: g.show()
sage: Graph(g).show()
sage: DiGraph(g).show()
```


The positions are not kept.... Why isn't Graph(g) equivalent to copy(g) ?

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/7733





---

archive/issue_comments_066440.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-22T18:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66440",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066441.json:
```json
{
    "body": "Two lines !\n\nNathann",
    "created_at": "2010-02-22T18:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66441",
    "user": "ncohen"
}
```

Two lines !

Nathann



---

archive/issue_comments_066442.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-02T03:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66442",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066443.json:
```json
{
    "body": "You must provide doctests in both directions.",
    "created_at": "2010-03-02T03:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66443",
    "user": "rlm"
}
```

You must provide doctests in both directions.



---

archive/issue_comments_066444.json:
```json
{
    "body": "Done !",
    "created_at": "2010-03-02T13:17:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66444",
    "user": "ncohen"
}
```

Done !



---

archive/issue_comments_066445.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-02T13:17:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66445",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066446.json:
```json
{
    "body": "Attachment [trac_7733.patch](tarball://root/attachments/some-uuid/ticket7733/trac_7733.patch) by ncohen created at 2010-03-02 13:18:19",
    "created_at": "2010-03-02T13:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66446",
    "user": "ncohen"
}
```

Attachment [trac_7733.patch](tarball://root/attachments/some-uuid/ticket7733/trac_7733.patch) by ncohen created at 2010-03-02 13:18:19



---

archive/issue_comments_066447.json:
```json
{
    "body": "There is one case which is untested, going from a `Graph` to a `DiGraph`.",
    "created_at": "2010-03-06T22:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66447",
    "user": "rlm"
}
```

There is one case which is untested, going from a `Graph` to a `DiGraph`.



---

archive/issue_comments_066448.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-06T22:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66448",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066449.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-03-07T17:04:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66449",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_066450.json:
```json
{
    "body": "What do you think of line 300 ?\n\n\n```\nsage: g = DiGraph(graphs.PetersenGraph()) \n```\n\n\nWould you like to see an independent test for it ?\n\nNathann",
    "created_at": "2010-03-07T17:04:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66450",
    "user": "ncohen"
}
```

What do you think of line 300 ?


```
sage: g = DiGraph(graphs.PetersenGraph()) 
```


Would you like to see an independent test for it ?

Nathann



---

archive/issue_comments_066451.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-03-07T17:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66451",
    "user": "rlm"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_066452.json:
```json
{
    "body": "Sorry, I must have missed that!",
    "created_at": "2010-03-07T17:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66452",
    "user": "rlm"
}
```

Sorry, I must have missed that!



---

archive/issue_comments_066453.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-07T18:02:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66453",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066454.json:
```json
{
    "body": "Thanks :-)",
    "created_at": "2010-03-07T18:04:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66454",
    "user": "ncohen"
}
```

Thanks :-)



---

archive/issue_comments_066455.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-08T20:57:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66455",
    "user": "mhansen"
}
```

Resolution: fixed
