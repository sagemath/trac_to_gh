# Issue 1900: [with patch, needs review] Clean up adjacency matrix functions for graphs

archive/issues_001900.json:
```json
{
    "body": "Assignee: @rlmill\n\nThere were several options available to graphs but not digraphs, so I factored the code out to generic graphs, and made sure all functionality was available there.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1900\n\n",
    "created_at": "2008-01-24T00:25:27Z",
    "labels": [
        "component: graph theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch, needs review] Clean up adjacency matrix functions for graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1900",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill

There were several options available to graphs but not digraphs, so I factored the code out to generic graphs, and made sure all functionality was available there.

Issue created by migration from https://trac.sagemath.org/ticket/1900





---

archive/issue_comments_011992.json:
```json
{
    "body": "Attachment [graph_am-updated.patch](tarball://root/attachments/some-uuid/ticket1900/graph_am-updated.patch) by @jasongrout created at 2008-01-24 05:44:07",
    "created_at": "2008-01-24T05:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1900#issuecomment-11992",
    "user": "https://github.com/jasongrout"
}
```

Attachment [graph_am-updated.patch](tarball://root/attachments/some-uuid/ticket1900/graph_am-updated.patch) by @jasongrout created at 2008-01-24 05:44:07



---

archive/issue_comments_011993.json:
```json
{
    "body": "I further cleaned up the code a bit and hopefully made it a tad faster as well in graph_am-updated.patch, which should be applied instead of graph_am.patch.\n\nAlso, pending the outcome of the discussion on sage-devel, graph_am-over_integers.patch should be applied after graph_am-updated.patch in order to delete the over_integers parameter.\n\nReviews of my modifications would be appreciated.",
    "created_at": "2008-01-24T05:46:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1900#issuecomment-11993",
    "user": "https://github.com/jasongrout"
}
```

I further cleaned up the code a bit and hopefully made it a tad faster as well in graph_am-updated.patch, which should be applied instead of graph_am.patch.

Also, pending the outcome of the discussion on sage-devel, graph_am-over_integers.patch should be applied after graph_am-updated.patch in order to delete the over_integers parameter.

Reviews of my modifications would be appreciated.



---

archive/issue_comments_011994.json:
```json
{
    "body": "Updated patch fixes doctests and calls to adjacency_matrix",
    "created_at": "2008-01-24T06:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1900#issuecomment-11994",
    "user": "https://github.com/jasongrout"
}
```

Updated patch fixes doctests and calls to adjacency_matrix



---

archive/issue_comments_011995.json:
```json
{
    "body": "Attachment [graph_am-over_integers.patch](tarball://root/attachments/some-uuid/ticket1900/graph_am-over_integers.patch) by @jasongrout created at 2008-01-24 06:22:49",
    "created_at": "2008-01-24T06:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1900#issuecomment-11995",
    "user": "https://github.com/jasongrout"
}
```

Attachment [graph_am-over_integers.patch](tarball://root/attachments/some-uuid/ticket1900/graph_am-over_integers.patch) by @jasongrout created at 2008-01-24 06:22:49



---

archive/issue_comments_011996.json:
```json
{
    "body": "Priority changed since the default of returning an adjacency matrix over GF(2) made the characteristic polynomial function completely *wrong*.",
    "created_at": "2008-01-24T06:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1900#issuecomment-11996",
    "user": "https://github.com/jasongrout"
}
```

Priority changed since the default of returning an adjacency matrix over GF(2) made the characteristic polynomial function completely *wrong*.



---

archive/issue_comments_011997.json:
```json
{
    "body": "Robert, where did your original patch go?  I don't want to take all the credit---you did the initial work here.  I'm not sure how to change the patch to include both of us as authors...",
    "created_at": "2008-01-24T18:58:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1900#issuecomment-11997",
    "user": "https://github.com/jasongrout"
}
```

Robert, where did your original patch go?  I don't want to take all the credit---you did the initial work here.  I'm not sure how to change the patch to include both of us as authors...



---

archive/issue_comments_011998.json:
```json
{
    "body": "I deleted it to avoid merge conflict. Don't worry about it.",
    "created_at": "2008-01-24T20:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1900#issuecomment-11998",
    "user": "https://github.com/rlmill"
}
```

I deleted it to avoid merge conflict. Don't worry about it.



---

archive/issue_comments_011999.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-24T21:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1900#issuecomment-11999",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012000.json:
```json
{
    "body": "Both patches merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-24T21:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1900#issuecomment-12000",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Both patches merged in Sage 2.10.1.alpha2
