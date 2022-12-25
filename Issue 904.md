# Issue 904: [with patch] graphs: clique-testing

archive/issues_000904.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: graphs\n\nThis adds is_clique and is_indendent_set functions to undirected graphs.\n\nIssue created by migration from https://trac.sagemath.org/ticket/904\n\n",
    "created_at": "2007-10-15T22:19:21Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.9",
    "title": "[with patch] graphs: clique-testing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/904",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

Keywords: graphs

This adds is_clique and is_indendent_set functions to undirected graphs.

Issue created by migration from https://trac.sagemath.org/ticket/904





---

archive/issue_comments_005548.json:
```json
{
    "body": "Attachment [clique_ind_set.patch](tarball://root/attachments/some-uuid/ticket904/clique_ind_set.patch) by @jasongrout created at 2007-10-15 22:19:30",
    "created_at": "2007-10-15T22:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/904#issuecomment-5548",
    "user": "https://github.com/jasongrout"
}
```

Attachment [clique_ind_set.patch](tarball://root/attachments/some-uuid/ticket904/clique_ind_set.patch) by @jasongrout created at 2007-10-15 22:19:30



---

archive/issue_comments_005549.json:
```json
{
    "body": "Updated patch clique_ind_set-2.patch.  Apply this instead of the first patch.\n\nThis adds an option to the is_clique to check if it is a directed clique (i.e., edges in each direction exist) in the case the graph is a directed graph.  This patch also puts both functions into GeneralGraph to make them available to directed graphs.  It also deletes the (now redundant) independent_set function in GeneralGraph.\n\nThis functionality now gives us the Combinatorica EmptyQ and CompleteQ functions, as well as the CliqueQ and IndependentSetQ functions.",
    "created_at": "2007-10-17T16:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/904#issuecomment-5549",
    "user": "https://github.com/jasongrout"
}
```

Updated patch clique_ind_set-2.patch.  Apply this instead of the first patch.

This adds an option to the is_clique to check if it is a directed clique (i.e., edges in each direction exist) in the case the graph is a directed graph.  This patch also puts both functions into GeneralGraph to make them available to directed graphs.  It also deletes the (now redundant) independent_set function in GeneralGraph.

This functionality now gives us the Combinatorica EmptyQ and CompleteQ functions, as well as the CliqueQ and IndependentSetQ functions.



---

archive/issue_comments_005550.json:
```json
{
    "body": "Attachment [clique_ind_set-2.patch](tarball://root/attachments/some-uuid/ticket904/clique_ind_set-2.patch) by @jasongrout created at 2007-10-17 16:12:06\n\nReplaces the first patch above.",
    "created_at": "2007-10-17T16:12:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/904#issuecomment-5550",
    "user": "https://github.com/jasongrout"
}
```

Attachment [clique_ind_set-2.patch](tarball://root/attachments/some-uuid/ticket904/clique_ind_set-2.patch) by @jasongrout created at 2007-10-17 16:12:06

Replaces the first patch above.



---

archive/issue_comments_005551.json:
```json
{
    "body": "This patch looks ready for inclusion. Jason -- do you notice any other functions that could be moved to GeneralGraph?",
    "created_at": "2007-10-21T04:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/904#issuecomment-5551",
    "user": "https://github.com/rlmill"
}
```

This patch looks ready for inclusion. Jason -- do you notice any other functions that could be moved to GeneralGraph?



---

archive/issue_events_001020.json:
```json
{
    "actor": "@malb",
    "created_at": "2007-10-23T22:17:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/904",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/904#event-1020"
}
```



---

archive/issue_comments_005552.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-23T22:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/904#issuecomment-5552",
    "user": "https://github.com/malb"
}
```

Resolution: fixed



---

archive/issue_comments_005553.json:
```json
{
    "body": "merged into 2.8.9.alpha0",
    "created_at": "2007-10-23T22:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/904#issuecomment-5553",
    "user": "https://github.com/malb"
}
```

merged into 2.8.9.alpha0
