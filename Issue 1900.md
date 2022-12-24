# Issue 1900: [with patch, needs review] Clean up adjacency matrix functions for graphs

archive/issues_001900.json:
```json
{
    "body": "Assignee: rlm\n\nThere were several options available to graphs but not digraphs, so I factored the code out to generic graphs, and made sure all functionality was available there.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1900\n\n",
    "created_at": "2008-01-24T00:25:27Z",
    "labels": [
        "graph theory",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] Clean up adjacency matrix functions for graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1900",
    "user": "rlm"
}
```
Assignee: rlm

There were several options available to graphs but not digraphs, so I factored the code out to generic graphs, and made sure all functionality was available there.

Issue created by migration from https://trac.sagemath.org/ticket/1900





---

archive/issue_comments_012021.json:
```json
{
    "body": "Attachment [graph_am-updated.patch](tarball://root/attachments/some-uuid/ticket1900/graph_am-updated.patch) by jason created at 2008-01-24 05:44:07",
    "created_at": "2008-01-24T05:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1900#issuecomment-12021",
    "user": "jason"
}
```

Attachment [graph_am-updated.patch](tarball://root/attachments/some-uuid/ticket1900/graph_am-updated.patch) by jason created at 2008-01-24 05:44:07



---

archive/issue_comments_012022.json:
```json
{
    "body": "I further cleaned up the code a bit and hopefully made it a tad faster as well in graph_am-updated.patch, which should be applied instead of graph_am.patch.\n\nAlso, pending the outcome of the discussion on sage-devel, graph_am-over_integers.patch should be applied after graph_am-updated.patch in order to delete the over_integers parameter.\n\nReviews of my modifications would be appreciated.",
    "created_at": "2008-01-24T05:46:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1900#issuecomment-12022",
    "user": "jason"
}
```

I further cleaned up the code a bit and hopefully made it a tad faster as well in graph_am-updated.patch, which should be applied instead of graph_am.patch.

Also, pending the outcome of the discussion on sage-devel, graph_am-over_integers.patch should be applied after graph_am-updated.patch in order to delete the over_integers parameter.

Reviews of my modifications would be appreciated.



---

archive/issue_comments_012023.json:
```json
{
    "body": "Updated patch fixes doctests and calls to adjacency_matrix",
    "created_at": "2008-01-24T06:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1900#issuecomment-12023",
    "user": "jason"
}
```

Updated patch fixes doctests and calls to adjacency_matrix



---

archive/issue_comments_012024.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2008-01-24T06:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1900#issuecomment-12024",
    "user": "jason"
}
```

Changing priority from minor to major.



---

archive/issue_comments_012025.json:
```json
{
    "body": "Attachment [graph_am-over_integers.patch](tarball://root/attachments/some-uuid/ticket1900/graph_am-over_integers.patch) by jason created at 2008-01-24 06:22:49",
    "created_at": "2008-01-24T06:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1900#issuecomment-12025",
    "user": "jason"
}
```

Attachment [graph_am-over_integers.patch](tarball://root/attachments/some-uuid/ticket1900/graph_am-over_integers.patch) by jason created at 2008-01-24 06:22:49



---

archive/issue_comments_012026.json:
```json
{
    "body": "Priority changed since the default of returning an adjacency matrix over GF(2) made the characteristic polynomial function completely *wrong*.",
    "created_at": "2008-01-24T06:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1900#issuecomment-12026",
    "user": "jason"
}
```

Priority changed since the default of returning an adjacency matrix over GF(2) made the characteristic polynomial function completely *wrong*.



---

archive/issue_comments_012027.json:
```json
{
    "body": "Robert, where did your original patch go?  I don't want to take all the credit---you did the initial work here.  I'm not sure how to change the patch to include both of us as authors...",
    "created_at": "2008-01-24T18:58:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1900#issuecomment-12027",
    "user": "jason"
}
```

Robert, where did your original patch go?  I don't want to take all the credit---you did the initial work here.  I'm not sure how to change the patch to include both of us as authors...



---

archive/issue_comments_012028.json:
```json
{
    "body": "I deleted it to avoid merge conflict. Don't worry about it.",
    "created_at": "2008-01-24T20:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1900#issuecomment-12028",
    "user": "rlm"
}
```

I deleted it to avoid merge conflict. Don't worry about it.



---

archive/issue_comments_012029.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-24T21:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1900#issuecomment-12029",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012030.json:
```json
{
    "body": "Both patches merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-24T21:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1900#issuecomment-12030",
    "user": "mabshoff"
}
```

Both patches merged in Sage 2.10.1.alpha2
