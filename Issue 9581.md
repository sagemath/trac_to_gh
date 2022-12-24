# Issue 9581: edge_incident bug in generic_graph.py

archive/issues_009581.json:
```json
{
    "body": "Assignee: @videlec\n\nCC:  @nathanncohen rmiller\n\nKeywords: graph\n\nCurrently, the edge_incident method of generic graph calls edge_boundary which first take a lot of time and secondly does not work\n\n\n```\nsage: G = Graph(loops=True)\nsage: G.add_edge(0,0)\nsage: G.edges()\n[(0, 0, None)]\nsage: list(G.edge_iterator(0))\n[(0, 0, None)]\nsage: G.edges_incident(0)\n[]\n```\n\n\nThe ticket also aims to reduce multiple calls (edge_boundary does not call directly vertex_iterator as it should).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9581\n\n",
    "created_at": "2010-07-23T07:13:18Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "edge_incident bug in generic_graph.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9581",
    "user": "@videlec"
}
```
Assignee: @videlec

CC:  @nathanncohen rmiller

Keywords: graph

Currently, the edge_incident method of generic graph calls edge_boundary which first take a lot of time and secondly does not work


```
sage: G = Graph(loops=True)
sage: G.add_edge(0,0)
sage: G.edges()
[(0, 0, None)]
sage: list(G.edge_iterator(0))
[(0, 0, None)]
sage: G.edges_incident(0)
[]
```


The ticket also aims to reduce multiple calls (edge_boundary does not call directly vertex_iterator as it should).

Issue created by migration from https://trac.sagemath.org/ticket/9581





---

archive/issue_comments_092537.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-23T10:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9581#issuecomment-92537",
    "user": "@nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092538.json:
```json
{
    "body": "Excellent ! Thank youuuuuuuuuuuuuu !!\n\nYour patch is very nice, applies fine and everything.. I would just like to append a short line, because of a missing \"if\". If you agree with this, let's say this ticket is positively reviewed ! :-)\n\nNathann",
    "created_at": "2010-07-23T10:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9581#issuecomment-92538",
    "user": "@nathanncohen"
}
```

Excellent ! Thank youuuuuuuuuuuuuu !!

Your patch is very nice, applies fine and everything.. I would just like to append a short line, because of a missing "if". If you agree with this, let's say this ticket is positively reviewed ! :-)

Nathann



---

archive/issue_comments_092539.json:
```json
{
    "body": "Attachment [trac_9581-fix.patch](tarball://root/attachments/some-uuid/ticket9581/trac_9581-fix.patch) by @videlec created at 2010-07-23 23:27:42\n\nNathan, Why did you put this ticket as needs_review? It seems to be important to be a lot more explicit in the definition of each function of generic_graph and implement all the cases in examples... perhaps it is the matter of another ticket...",
    "created_at": "2010-07-23T23:27:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9581#issuecomment-92539",
    "user": "@videlec"
}
```

Attachment [trac_9581-fix.patch](tarball://root/attachments/some-uuid/ticket9581/trac_9581-fix.patch) by @videlec created at 2010-07-23 23:27:42

Nathan, Why did you put this ticket as needs_review? It seems to be important to be a lot more explicit in the definition of each function of generic_graph and implement all the cases in examples... perhaps it is the matter of another ticket...



---

archive/issue_comments_092540.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-24T02:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9581#issuecomment-92540",
    "user": "@nathanncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_092541.json:
```json
{
    "body": "Hello ! Well, if you think it needs more documenation or tests, this ticket certainly is the one that should contain it...  I thought the behaviour of these functions did not change that much, only \"internal modifications\", so... But I'm sorry for this, all you just said is better done here ! :-)",
    "created_at": "2010-07-24T02:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9581#issuecomment-92541",
    "user": "@nathanncohen"
}
```

Hello ! Well, if you think it needs more documenation or tests, this ticket certainly is the one that should contain it...  I thought the behaviour of these functions did not change that much, only "internal modifications", so... But I'm sorry for this, all you just said is better done here ! :-)



---

archive/issue_comments_092542.json:
```json
{
    "body": "apply only this patch which takes care of Nathan remark",
    "created_at": "2010-10-10T10:20:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9581#issuecomment-92542",
    "user": "@videlec"
}
```

apply only this patch which takes care of Nathan remark



---

archive/issue_comments_092543.json:
```json
{
    "body": "Attachment [trac_9581-edge_incident.patch](tarball://root/attachments/some-uuid/ticket9581/trac_9581-edge_incident.patch) by @videlec created at 2010-10-10 10:20:24",
    "created_at": "2010-10-10T10:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9581#issuecomment-92543",
    "user": "@videlec"
}
```

Attachment [trac_9581-edge_incident.patch](tarball://root/attachments/some-uuid/ticket9581/trac_9581-edge_incident.patch) by @videlec created at 2010-10-10 10:20:24



---

archive/issue_comments_092544.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-10T10:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9581#issuecomment-92544",
    "user": "@videlec"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_092545.json:
```json
{
    "body": "Hello !!! I can not apply this patch on 4.6.alpha3, looks like it needs to be rebased `^^;`\n\nNathann",
    "created_at": "2010-10-10T17:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9581#issuecomment-92545",
    "user": "@nathanncohen"
}
```

Hello !!! I can not apply this patch on 4.6.alpha3, looks like it needs to be rebased `^^;`

Nathann



---

archive/issue_comments_092546.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-10-10T17:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9581#issuecomment-92546",
    "user": "@nathanncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_092547.json:
```json
{
    "body": "Attachment [trac_9581-edge_incident.2.patch](tarball://root/attachments/some-uuid/ticket9581/trac_9581-edge_incident.2.patch) by @videlec created at 2010-10-11 08:02:00\n\nrebased version (apply only this one)",
    "created_at": "2010-10-11T08:02:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9581#issuecomment-92547",
    "user": "@videlec"
}
```

Attachment [trac_9581-edge_incident.2.patch](tarball://root/attachments/some-uuid/ticket9581/trac_9581-edge_incident.2.patch) by @videlec created at 2010-10-11 08:02:00

rebased version (apply only this one)



---

archive/issue_comments_092548.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-11T08:02:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9581#issuecomment-92548",
    "user": "@videlec"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_092549.json:
```json
{
    "body": "Positive review to this rebased version `:-)`\n\nNathann",
    "created_at": "2010-10-11T12:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9581#issuecomment-92549",
    "user": "@nathanncohen"
}
```

Positive review to this rebased version `:-)`

Nathann



---

archive/issue_comments_092550.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-11T12:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9581#issuecomment-92550",
    "user": "@nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092551.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-01T10:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9581#issuecomment-92551",
    "user": "@jdemeyer"
}
```

Resolution: fixed
