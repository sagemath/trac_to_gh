# Issue 6552: bug in depth-first searching

archive/issues_006552.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @rlmill\n\nHere is a bug in the depth-first searching of a graph:\n\n\n```\n\nsage: D = DiGraph( { 0: [1,2,3], 1: [4,5], 2: [5], 3: [6], 5: [7], 6: [7], 7: [0]})\nsage: list(D.depth_first_search(0, ignore_direction=True))                         \n[0, 7, 6, 5, 3, 2, 1, 4]\n```\n\n\nIt should be `[0, 7, 6, 3, 5, 2, 1, 4]`.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6552\n\n",
    "created_at": "2009-07-18T10:28:04Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "bug in depth-first searching",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6552",
    "user": "@jasongrout"
}
```
Assignee: @rlmill

CC:  @rlmill

Here is a bug in the depth-first searching of a graph:


```

sage: D = DiGraph( { 0: [1,2,3], 1: [4,5], 2: [5], 3: [6], 5: [7], 6: [7], 7: [0]})
sage: list(D.depth_first_search(0, ignore_direction=True))                         
[0, 7, 6, 5, 3, 2, 1, 4]
```


It should be `[0, 7, 6, 3, 5, 2, 1, 4]`.



Issue created by migration from https://trac.sagemath.org/ticket/6552





---

archive/issue_comments_053431.json:
```json
{
    "body": "I also added a bunch of features to the graph traversal functions and put in a lot more doctests.",
    "created_at": "2009-07-18T10:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6552#issuecomment-53431",
    "user": "@jasongrout"
}
```

I also added a bunch of features to the graph traversal functions and put in a lot more doctests.



---

archive/issue_comments_053432.json:
```json
{
    "body": "I say you remove the\n\n```\n#        for v,d in queue: \n#            seen.add(v) \n```\n\nin `depth_first_search` and everything looks good!",
    "created_at": "2009-07-18T18:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6552#issuecomment-53432",
    "user": "@rlmill"
}
```

I say you remove the

```
#        for v,d in queue: 
#            seen.add(v) 
```

in `depth_first_search` and everything looks good!



---

archive/issue_comments_053433.json:
```json
{
    "body": "Attachment [trac-6552-graph-traversal.patch](tarball://root/attachments/some-uuid/ticket6552/trac-6552-graph-traversal.patch) by @jasongrout created at 2009-07-18 19:15:39",
    "created_at": "2009-07-18T19:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6552#issuecomment-53433",
    "user": "@jasongrout"
}
```

Attachment [trac-6552-graph-traversal.patch](tarball://root/attachments/some-uuid/ticket6552/trac-6552-graph-traversal.patch) by @jasongrout created at 2009-07-18 19:15:39



---

archive/issue_comments_053434.json:
```json
{
    "body": "Good catch!  I deleted those two lines and posted an updated patch.  Thanks for reviewing this so fast!",
    "created_at": "2009-07-18T19:16:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6552#issuecomment-53434",
    "user": "@jasongrout"
}
```

Good catch!  I deleted those two lines and posted an updated patch.  Thanks for reviewing this so fast!



---

archive/issue_comments_053435.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-20T17:24:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6552#issuecomment-53435",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_053436.json:
```json
{
    "body": "This will have to wait for Sage 4.1.1.alpha1. Apparently, I accidentally closed this as being merged in 4.1.1.alpha0.",
    "created_at": "2009-07-20T17:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6552#issuecomment-53436",
    "user": "mvngu"
}
```

This will have to wait for Sage 4.1.1.alpha1. Apparently, I accidentally closed this as being merged in 4.1.1.alpha0.



---

archive/issue_comments_053437.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-07-20T17:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6552#issuecomment-53437",
    "user": "mvngu"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_053438.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-07-20T17:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6552#issuecomment-53438",
    "user": "mvngu"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_053439.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-23T03:37:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6552#issuecomment-53439",
    "user": "mvngu"
}
```

Resolution: fixed
