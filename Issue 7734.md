# Issue 7734: edge_coloring ( and possibly vertex_coloring ) loop forever when GLPK is not installed

archive/issues_007734.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  rlm\n\nAs the title says... :-)\n\nIssue created by migration from https://trac.sagemath.org/ticket/7734\n\n",
    "created_at": "2009-12-18T08:45:30Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "edge_coloring ( and possibly vertex_coloring ) loop forever when GLPK is not installed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7734",
    "user": "ncohen"
}
```
Assignee: rlm

CC:  rlm

As the title says... :-)

Issue created by migration from https://trac.sagemath.org/ticket/7734





---

archive/issue_comments_066456.json:
```json
{
    "body": "Attachment [trac_7734.patch](tarball://root/attachments/some-uuid/ticket7734/trac_7734.patch) by ncohen created at 2009-12-18 09:02:34",
    "created_at": "2009-12-18T09:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7734#issuecomment-66456",
    "user": "ncohen"
}
```

Attachment [trac_7734.patch](tarball://root/attachments/some-uuid/ticket7734/trac_7734.patch) by ncohen created at 2009-12-18 09:02:34



---

archive/issue_comments_066457.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-18T09:03:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7734#issuecomment-66457",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066458.json:
```json
{
    "body": "1. There should always be an example of the bug you are fixing in the patch, always always always. We need a mug shot, so the bug doesn't show its face again :) I added this, as well as several other tests, which have exposed other corner case bugs, such as:\n\n```\nsage: g = Graph(20)\nsage: vertex_coloring(g, hex_colors=True)\n{'#ff0000': 0}\n```\n\nI've fixed these.\n\n2. It seems to take some time to add constraints to the problem, which is pointless if no solver is installed. Can you add a patch that runs a trivial test before setting up the problem, to see if it is installed?",
    "created_at": "2009-12-18T21:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7734#issuecomment-66458",
    "user": "rlm"
}
```

1. There should always be an example of the bug you are fixing in the patch, always always always. We need a mug shot, so the bug doesn't show its face again :) I added this, as well as several other tests, which have exposed other corner case bugs, such as:

```
sage: g = Graph(20)
sage: vertex_coloring(g, hex_colors=True)
{'#ff0000': 0}
```

I've fixed these.

2. It seems to take some time to add constraints to the problem, which is pointless if no solver is installed. Can you add a patch that runs a trivial test before setting up the problem, to see if it is installed?



---

archive/issue_comments_066459.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-18T21:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7734#issuecomment-66459",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066460.json:
```json
{
    "body": "Attachment [trac_7734-edit.patch](tarball://root/attachments/some-uuid/ticket7734/trac_7734-edit.patch) by rlm created at 2009-12-18 21:24:09",
    "created_at": "2009-12-18T21:24:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7734#issuecomment-66460",
    "user": "rlm"
}
```

Attachment [trac_7734-edit.patch](tarball://root/attachments/some-uuid/ticket7734/trac_7734-edit.patch) by rlm created at 2009-12-18 21:24:09



---

archive/issue_comments_066461.json:
```json
{
    "body": "Thank you for your help !!!\n\nConcerning your second point : do you have an example for which it takes some time ? I would also like to try to improve it a bit :-)",
    "created_at": "2009-12-19T08:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7734#issuecomment-66461",
    "user": "ncohen"
}
```

Thank you for your help !!!

Concerning your second point : do you have an example for which it takes some time ? I would also like to try to improve it a bit :-)



---

archive/issue_comments_066462.json:
```json
{
    "body": "Replying to [comment:5 ncohen]:\n> Thank you for your help !!!\n> \n> do you have an example for which it takes some time ? I would also like to try to improve it a bit :-)\n> \n\n\n```\nsage: from sage.graphs.graph_coloring import vertex_coloring\nsage: g = graphs.CirculantGraph(120, [2,3,5,7])\nsage: vertex_coloring(g)\n```\n\nIt takes longer to set up the constraint than to solve the problem, on my laptop.",
    "created_at": "2009-12-19T08:39:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7734#issuecomment-66462",
    "user": "rlm"
}
```

Replying to [comment:5 ncohen]:
> Thank you for your help !!!
> 
> do you have an example for which it takes some time ? I would also like to try to improve it a bit :-)
> 


```
sage: from sage.graphs.graph_coloring import vertex_coloring
sage: g = graphs.CirculantGraph(120, [2,3,5,7])
sage: vertex_coloring(g)
```

It takes longer to set up the constraint than to solve the problem, on my laptop.



---

archive/issue_comments_066463.json:
```json
{
    "body": "I just created #7740 to deal with the problem of speed. What would you advise for the detection of the solver ? At the moment, only the \"solve\" command requires an optional package to be installed, do you think it would be worth changing this and make the whole class depend on GLPK or CBC ?\n\nNathann",
    "created_at": "2009-12-19T08:49:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7734#issuecomment-66463",
    "user": "ncohen"
}
```

I just created #7740 to deal with the problem of speed. What would you advise for the detection of the solver ? At the moment, only the "solve" command requires an optional package to be installed, do you think it would be worth changing this and make the whole class depend on GLPK or CBC ?

Nathann



---

archive/issue_comments_066464.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-19T20:13:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7734",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7734#issuecomment-66464",
    "user": "mhansen"
}
```

Resolution: fixed
