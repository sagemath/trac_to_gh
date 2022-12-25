# Issue 7733: Graph(g) and DiGraph(g) do not keep the embedding !

archive/issues_007733.json:
```json
{
    "body": "Assignee: @rlmill\n\nJust try ::\n\n```\nsage: g = graphs.PetersenGraph()\nsage: g.show()\nsage: Graph(g).show()\nsage: DiGraph(g).show()\n```\n\nThe positions are not kept.... Why isn't Graph(g) equivalent to copy(g) ?\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/7733\n\n",
    "closed_at": "2010-03-08T20:57:27Z",
    "created_at": "2009-12-18T08:25:18Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Graph(g) and DiGraph(g) do not keep the embedding !",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7733",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

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

archive/issue_comments_066324.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-22T18:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66324",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066325.json:
```json
{
    "body": "Two lines !\n\nNathann",
    "created_at": "2010-02-22T18:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66325",
    "user": "https://github.com/nathanncohen"
}
```

Two lines !

Nathann



---

archive/issue_comments_066326.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-02T03:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66326",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066327.json:
```json
{
    "body": "You must provide doctests in both directions.",
    "created_at": "2010-03-02T03:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66327",
    "user": "https://github.com/rlmill"
}
```

You must provide doctests in both directions.



---

archive/issue_comments_066328.json:
```json
{
    "body": "Done !",
    "created_at": "2010-03-02T13:17:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66328",
    "user": "https://github.com/nathanncohen"
}
```

Done !



---

archive/issue_comments_066329.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-02T13:17:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66329",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066330.json:
```json
{
    "body": "Attachment [trac_7733.patch](tarball://root/attachments/some-uuid/ticket7733/trac_7733.patch) by @nathanncohen created at 2010-03-02 13:18:19",
    "created_at": "2010-03-02T13:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66330",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_7733.patch](tarball://root/attachments/some-uuid/ticket7733/trac_7733.patch) by @nathanncohen created at 2010-03-02 13:18:19



---

archive/issue_comments_066331.json:
```json
{
    "body": "There is one case which is untested, going from a `Graph` to a `DiGraph`.",
    "created_at": "2010-03-06T22:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66331",
    "user": "https://github.com/rlmill"
}
```

There is one case which is untested, going from a `Graph` to a `DiGraph`.



---

archive/issue_comments_066332.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-06T22:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66332",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066333.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-03-07T17:04:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66333",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_066334.json:
```json
{
    "body": "What do you think of line 300 ?\n\n```\nsage: g = DiGraph(graphs.PetersenGraph()) \n```\n\nWould you like to see an independent test for it ?\n\nNathann",
    "created_at": "2010-03-07T17:04:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66334",
    "user": "https://github.com/nathanncohen"
}
```

What do you think of line 300 ?

```
sage: g = DiGraph(graphs.PetersenGraph()) 
```

Would you like to see an independent test for it ?

Nathann



---

archive/issue_comments_066335.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-03-07T17:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66335",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_066336.json:
```json
{
    "body": "Sorry, I must have missed that!",
    "created_at": "2010-03-07T17:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66336",
    "user": "https://github.com/rlmill"
}
```

Sorry, I must have missed that!



---

archive/issue_comments_066337.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-07T18:02:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66337",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066338.json:
```json
{
    "body": "Thanks :-)",
    "created_at": "2010-03-07T18:04:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66338",
    "user": "https://github.com/nathanncohen"
}
```

Thanks :-)



---

archive/issue_events_018491.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-03-08T20:57:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7733#event-18491"
}
```



---

archive/issue_comments_066339.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-08T20:57:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7733#issuecomment-66339",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
