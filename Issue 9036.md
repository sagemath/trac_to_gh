# Issue 9036: Graph.canonical_label(certify=True, edge_labels=True) returns a name error

archive/issues_009036.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nKeywords: labelled graph isomorphism\n\nThe method canonical_label() for Graph and DiGraph does not take the parameters 'certify=True' and 'edge_labels=True' at the same time:\n\n```\nsage: g = Graph()                                      \nsage: g.canonical_label()\nGraph on 0 vertices\nsage: g.canonical_label(certify=True)\n(Graph on 0 vertices, {})\nsage: g.canonical_label(edge_labels=True)\nGraph on 0 vertices\nsage: g.canonical_label(certify=True, edge_labels=True)\n\n...\n\nNameError: global name 'relabeling' is not defined\n}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/9036\n\n",
    "closed_at": "2010-06-29T16:47:57Z",
    "created_at": "2010-05-24T14:29:39Z",
    "labels": [
        "component: graph theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Graph.canonical_label(certify=True, edge_labels=True) returns a name error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9036",
    "user": "https://trac.sagemath.org/admin/accounts/users/stumpc5"
}
```
Assignee: jason, ncohen, rlm

Keywords: labelled graph isomorphism

The method canonical_label() for Graph and DiGraph does not take the parameters 'certify=True' and 'edge_labels=True' at the same time:

```
sage: g = Graph()                                      
sage: g.canonical_label()
Graph on 0 vertices
sage: g.canonical_label(certify=True)
(Graph on 0 vertices, {})
sage: g.canonical_label(edge_labels=True)
Graph on 0 vertices
sage: g.canonical_label(certify=True, edge_labels=True)

...

NameError: global name 'relabeling' is not defined
}}

Issue created by migration from https://trac.sagemath.org/ticket/9036





---

archive/issue_comments_083515.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-02T00:47:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9036#issuecomment-83515",
    "user": "https://trac.sagemath.org/admin/accounts/users/stumpc5"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083516.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-06-13T18:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9036#issuecomment-83516",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_083517.json:
```json
{
    "body": "Hmmm... I am reaallyyyyy sorry but I do not have the slightest idea of what the function \"canonical_label\" exactly does... Could I ask that your patch also improves its documentation ? :-/\n\nNathann",
    "created_at": "2010-06-13T18:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9036#issuecomment-83517",
    "user": "https://github.com/nathanncohen"
}
```

Hmmm... I am reaallyyyyy sorry but I do not have the slightest idea of what the function "canonical_label" exactly does... Could I ask that your patch also improves its documentation ? :-/

Nathann



---

archive/issue_comments_083518.json:
```json
{
    "body": "fixed bug in GenericGraph.canonical_label() and updated documentation",
    "created_at": "2010-06-15T13:26:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9036#issuecomment-83518",
    "user": "https://trac.sagemath.org/admin/accounts/users/stumpc5"
}
```

fixed bug in GenericGraph.canonical_label() and updated documentation



---

archive/issue_comments_083519.json:
```json
{
    "body": "Attachment [trac_9036_canonical_label.patch](tarball://root/attachments/some-uuid/ticket9036/trac_9036_canonical_label.patch) by stumpc5 created at 2010-06-15 13:30:19\n\nDone... I hope it is more understandable now.\n\nChristian",
    "created_at": "2010-06-15T13:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9036#issuecomment-83519",
    "user": "https://trac.sagemath.org/admin/accounts/users/stumpc5"
}
```

Attachment [trac_9036_canonical_label.patch](tarball://root/attachments/some-uuid/ticket9036/trac_9036_canonical_label.patch) by stumpc5 created at 2010-06-15 13:30:19

Done... I hope it is more understandable now.

Christian



---

archive/issue_comments_083520.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-06-15T13:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9036#issuecomment-83520",
    "user": "https://trac.sagemath.org/admin/accounts/users/stumpc5"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_083521.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-15T14:14:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9036#issuecomment-83521",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083522.json:
```json
{
    "body": "Positive review ! I can now see it was a natural thing to do, but I really didn't feel safe without understanding the function's purpose... :-)\n\nThank you again !\n\nNathann",
    "created_at": "2010-06-15T14:14:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9036#issuecomment-83522",
    "user": "https://github.com/nathanncohen"
}
```

Positive review ! I can now see it was a natural thing to do, but I really didn't feel safe without understanding the function's purpose... :-)

Thank you again !

Nathann



---

archive/issue_events_022122.json:
```json
{
    "actor": "https://github.com/loefflerd",
    "created_at": "2010-06-29T08:00:04Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9036",
    "milestone": "sage-4.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9036#event-22122"
}
```



---

archive/issue_comments_083523.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-29T16:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9036#issuecomment-83523",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_022123.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-06-29T16:47:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9036",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9036#event-22123"
}
```
