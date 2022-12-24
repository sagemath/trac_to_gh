# Issue 8748: Linear Arboricity, Acyclic edge coloring

archive/issues_008748.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nThis patch implements LP formulations of Linear Arboricity and Acyclic edge coloring\n\nNathann Thank you.I got it.\n\nThis ticket is the same as #8405. The latter got spam content and the spammer closed the ticket. It would be more trouble and result in confusion to reopen the ticket. So I have moved the ticket over to this one.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8748\n\n",
    "created_at": "2010-04-23T01:04:32Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Linear Arboricity, Acyclic edge coloring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8748",
    "user": "@nathanncohen"
}
```
Assignee: jason, ncohen, rlm

This patch implements LP formulations of Linear Arboricity and Acyclic edge coloring

Nathann Thank you.I got it.

This ticket is the same as #8405. The latter got spam content and the spammer closed the ticket. It would be more trouble and result in confusion to reopen the ticket. So I have moved the ticket over to this one.

Issue created by migration from https://trac.sagemath.org/ticket/8748





---

archive/issue_comments_080034.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-23T01:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8748#issuecomment-80034",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080035.json:
```json
{
    "body": "For an explanation of the Linear Program used to solve this problem, see the LP chapter from :  http://code.google.com/p/graph-theory-algorithms-book/\n\nNathann",
    "created_at": "2010-04-23T01:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8748#issuecomment-80035",
    "user": "mvngu"
}
```

For an explanation of the Linear Program used to solve this problem, see the LP chapter from :  http://code.google.com/p/graph-theory-algorithms-book/

Nathann



---

archive/issue_comments_080036.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-21T21:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8748#issuecomment-80036",
    "user": "@rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_080037.json:
```json
{
    "body": "Failures:\n\n```\nsage -t -only-optional=glpk,cbc \"devel/sage-main/sage/graphs/graph_coloring.py\"\n**********************************************************************\nFile \"/Users/rlmill/sage-4.4.4.alpha0-cbc/devel/sage-main/sage/graphs/graph_coloring.py\", line 749:\n    sage: all([g1.has_edge(e) or g2.has_edge(e) for e in g.edges()])  # optional - GLPK, CBC\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/Users/rlmill/sage-4.4.4.alpha0-cbc/devel/sage-main/sage/graphs/graph_coloring.py\", line 922:\n    sage: all([ any([gg.has_edge(e) for gg in colors]) for e in g.edges()])     # optional - GLPK, CBC\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n```\n",
    "created_at": "2010-06-21T21:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8748#issuecomment-80037",
    "user": "@rlmill"
}
```

Failures:

```
sage -t -only-optional=glpk,cbc "devel/sage-main/sage/graphs/graph_coloring.py"
**********************************************************************
File "/Users/rlmill/sage-4.4.4.alpha0-cbc/devel/sage-main/sage/graphs/graph_coloring.py", line 749:
    sage: all([g1.has_edge(e) or g2.has_edge(e) for e in g.edges()])  # optional - GLPK, CBC
Expected:
    True
Got:
    False
**********************************************************************
File "/Users/rlmill/sage-4.4.4.alpha0-cbc/devel/sage-main/sage/graphs/graph_coloring.py", line 922:
    sage: all([ any([gg.has_edge(e) for gg in colors]) for e in g.edges()])     # optional - GLPK, CBC
Expected:
    True
Got:
    False
**********************************************************************
```




---

archive/issue_comments_080038.json:
```json
{
    "body": "Yet another graph constructor from networkx, with {} instead of None as labels. A g.edges(labels = False) did the trick :-)\n\nSorry abou that !\n\nNathann",
    "created_at": "2010-06-21T21:14:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8748#issuecomment-80038",
    "user": "@nathanncohen"
}
```

Yet another graph constructor from networkx, with {} instead of None as labels. A g.edges(labels = False) did the trick :-)

Sorry abou that !

Nathann



---

archive/issue_comments_080039.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-21T21:14:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8748#issuecomment-80039",
    "user": "@nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080040.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-21T21:57:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8748#issuecomment-80040",
    "user": "@rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080041.json:
```json
{
    "body": "Attachment [trac_8748.2.patch](tarball://root/attachments/some-uuid/ticket8748/trac_8748.2.patch) by @rlmill created at 2010-06-21 21:57:09",
    "created_at": "2010-06-21T21:57:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8748#issuecomment-80041",
    "user": "@rlmill"
}
```

Attachment [trac_8748.2.patch](tarball://root/attachments/some-uuid/ticket8748/trac_8748.2.patch) by @rlmill created at 2010-06-21 21:57:09



---

archive/issue_comments_080042.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-29T16:44:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8748#issuecomment-80042",
    "user": "@rlmill"
}
```

Resolution: fixed
