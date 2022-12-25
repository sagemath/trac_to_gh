# Issue 9700: Export check_edge_label from sparse_graph.pyx

archive/issues_009700.json:
```json
{
    "body": "Assignee: @rhinton\n\nCC:  @rlmill @nathanncohen\n\nKeywords: graphs, Cython, sparse\n\nThe current `sparse_graph.pxd` does not export `check_edge_label`, which is necessary to translate Python object edge labels to the internal integer indices.  Exporting this function call enables writing Cython code based on the fast sparse graph implementation.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9700\n\n",
    "created_at": "2010-08-06T19:38:52Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "Export check_edge_label from sparse_graph.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9700",
    "user": "https://github.com/rhinton"
}
```
Assignee: @rhinton

CC:  @rlmill @nathanncohen

Keywords: graphs, Cython, sparse

The current `sparse_graph.pxd` does not export `check_edge_label`, which is necessary to translate Python object edge labels to the internal integer indices.  Exporting this function call enables writing Cython code based on the fast sparse graph implementation.


Issue created by migration from https://trac.sagemath.org/ticket/9700





---

archive/issue_comments_094171.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-06T20:43:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9700#issuecomment-94171",
    "user": "https://github.com/rhinton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_094172.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-07T02:12:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9700#issuecomment-94172",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094173.json:
```json
{
    "body": "One line.... Positively reviewed :-)\n\nNathann",
    "created_at": "2010-08-07T02:12:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9700#issuecomment-94173",
    "user": "https://github.com/nathanncohen"
}
```

One line.... Positively reviewed :-)

Nathann



---

archive/issue_comments_094174.json:
```json
{
    "body": "Agreed!",
    "created_at": "2010-08-07T03:29:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9700#issuecomment-94174",
    "user": "https://github.com/rlmill"
}
```

Agreed!



---

archive/issue_comments_094175.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-08-07T05:08:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9700#issuecomment-94175",
    "user": "https://github.com/qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_094176.json:
```json
{
    "body": "Can someone prepend the ticket number to the patch commit string?",
    "created_at": "2010-08-07T05:08:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9700#issuecomment-94176",
    "user": "https://github.com/qed777"
}
```

Can someone prepend the ticket number to the patch commit string?



---

archive/issue_comments_094177.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-08-07T06:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9700#issuecomment-94177",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_094178.json:
```json
{
    "body": "Attachment [trac-9700-sparse_graph-export-check_edge_label.patch](tarball://root/attachments/some-uuid/ticket9700/trac-9700-sparse_graph-export-check_edge_label.patch) by @mwhansen created at 2010-08-07 06:35:27\n\nDone.",
    "created_at": "2010-08-07T06:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9700#issuecomment-94178",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac-9700-sparse_graph-export-check_edge_label.patch](tarball://root/attachments/some-uuid/ticket9700/trac-9700-sparse_graph-export-check_edge_label.patch) by @mwhansen created at 2010-08-07 06:35:27

Done.



---

archive/issue_events_009834.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-09T09:49:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9700",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9700#event-9834"
}
```



---

archive/issue_comments_094179.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9700",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9700#issuecomment-94179",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
