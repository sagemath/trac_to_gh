# Issue 4005: [with patch, needs review] sage-coverage screws up with lambda functions as default arguments

archive/issues_004005.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4005\n\n",
    "created_at": "2008-08-30T18:53:14Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] sage-coverage screws up with lambda functions as default arguments",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4005",
    "user": "https://github.com/rlmill"
}
```
Assignee: mabshoff



Issue created by migration from https://trac.sagemath.org/ticket/4005





---

archive/issue_comments_028862.json:
```json
{
    "body": "Apply to scripts repo.",
    "created_at": "2008-08-30T18:54:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4005#issuecomment-28862",
    "user": "https://github.com/rlmill"
}
```

Apply to scripts repo.



---

archive/issue_comments_028863.json:
```json
{
    "body": "Attachment [trac_4005_sage-coverage.patch](tarball://root/attachments/some-uuid/ticket4005/trac_4005_sage-coverage.patch) by mabshoff created at 2008-08-30 23:55:37\n\nThis patch is motivated by\n\n```\n    def min_spanning_tree(self, weight_function=lambda e: 1,\n                          algorithm='Kruskal',\n                          starting_vertex=None ):\n```\n\nfrom sage/graphs/graph.py.\n\nPositive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-30T23:55:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4005#issuecomment-28863",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4005_sage-coverage.patch](tarball://root/attachments/some-uuid/ticket4005/trac_4005_sage-coverage.patch) by mabshoff created at 2008-08-30 23:55:37

This patch is motivated by

```
    def min_spanning_tree(self, weight_function=lambda e: 1,
                          algorithm='Kruskal',
                          starting_vertex=None ):
```

from sage/graphs/graph.py.

Positive review.

Cheers,

Michael



---

archive/issue_comments_028864.json:
```json
{
    "body": "rlm points out that this is not perfect, but it fixes this one specific issue. \n\nCheers,\n\nMichael",
    "created_at": "2008-08-30T23:57:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4005#issuecomment-28864",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

rlm points out that this is not perfect, but it fixes this one specific issue. 

Cheers,

Michael



---

archive/issue_comments_028865.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-30T23:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4005#issuecomment-28865",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028866.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha3",
    "created_at": "2008-08-30T23:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4005#issuecomment-28866",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha3
