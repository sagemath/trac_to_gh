# Issue 9036: Graph.canonical_label(certify=True, edge_labels=True) returns a name error

archive/issues_009036.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nKeywords: labelled graph isomorphism\n\nThe method canonical_label() for Graph and DiGraph does not take the parameters 'certify=True' and 'edge_labels=True' at the same time:\n\n\n```\nsage: g = Graph()                                      \nsage: g.canonical_label()\nGraph on 0 vertices\nsage: g.canonical_label(certify=True)\n(Graph on 0 vertices, {})\nsage: g.canonical_label(edge_labels=True)\nGraph on 0 vertices\nsage: g.canonical_label(certify=True, edge_labels=True)\n\n...\n\nNameError: global name 'relabeling' is not defined\n}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/9036\n\n",
    "created_at": "2010-05-24T14:29:39Z",
    "labels": [
        "graph theory",
        "minor",
        "bug"
    ],
    "title": "Graph.canonical_label(certify=True, edge_labels=True) returns a name error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9036",
    "user": "stumpc5"
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

archive/issue_comments_083651.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-02T00:47:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9036#issuecomment-83651",
    "user": "stumpc5"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083652.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-06-13T18:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9036#issuecomment-83652",
    "user": "ncohen"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_083653.json:
```json
{
    "body": "Hmmm... I am reaallyyyyy sorry but I do not have the slightest idea of what the function \"canonical_label\" exactly does... Could I ask that your patch also improves its documentation ? :-/\n\nNathann",
    "created_at": "2010-06-13T18:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9036#issuecomment-83653",
    "user": "ncohen"
}
```

Hmmm... I am reaallyyyyy sorry but I do not have the slightest idea of what the function "canonical_label" exactly does... Could I ask that your patch also improves its documentation ? :-/

Nathann



---

archive/issue_comments_083654.json:
```json
{
    "body": "fixed bug in GenericGraph.canonical_label() and updated documentation",
    "created_at": "2010-06-15T13:26:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9036#issuecomment-83654",
    "user": "stumpc5"
}
```

fixed bug in GenericGraph.canonical_label() and updated documentation



---

archive/issue_comments_083655.json:
```json
{
    "body": "Attachment [trac_9036_canonical_label.patch](tarball://root/attachments/some-uuid/ticket9036/trac_9036_canonical_label.patch) by stumpc5 created at 2010-06-15 13:30:19\n\nDone... I hope it is more understandable now.\n\nChristian",
    "created_at": "2010-06-15T13:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9036#issuecomment-83655",
    "user": "stumpc5"
}
```

Attachment [trac_9036_canonical_label.patch](tarball://root/attachments/some-uuid/ticket9036/trac_9036_canonical_label.patch) by stumpc5 created at 2010-06-15 13:30:19

Done... I hope it is more understandable now.

Christian



---

archive/issue_comments_083656.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-06-15T13:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9036#issuecomment-83656",
    "user": "stumpc5"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_083657.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-15T14:14:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9036#issuecomment-83657",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083658.json:
```json
{
    "body": "Positive review ! I can now see it was a natural thing to do, but I really didn't feel safe without understanding the function's purpose... :-)\n\nThank you again !\n\nNathann",
    "created_at": "2010-06-15T14:14:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9036#issuecomment-83658",
    "user": "ncohen"
}
```

Positive review ! I can now see it was a natural thing to do, but I really didn't feel safe without understanding the function's purpose... :-)

Thank you again !

Nathann



---

archive/issue_comments_083659.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-29T16:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9036#issuecomment-83659",
    "user": "rlm"
}
```

Resolution: fixed
