# Issue 1361: reimplement graph generation

archive/issues_001361.json:
```json
{
    "body": "Assignee: mhansen\n\nKeywords: graphs\n\nChanges:\n1. Redefine order to be number of edges.\n2. Start with empty graph.\n3. Augment by adding 1 edge.\n4. Cython-ize.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1361\n\n",
    "created_at": "2007-12-02T04:39:43Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "reimplement graph generation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1361",
    "user": "rlm"
}
```
Assignee: mhansen

Keywords: graphs

Changes:
1. Redefine order to be number of edges.
2. Start with empty graph.
3. Augment by adding 1 edge.
4. Cython-ize.

Issue created by migration from https://trac.sagemath.org/ticket/1361





---

archive/issue_comments_008719.json:
```json
{
    "body": "Changing assignee from mhansen to rlm.",
    "created_at": "2007-12-02T04:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1361#issuecomment-8719",
    "user": "rlm"
}
```

Changing assignee from mhansen to rlm.



---

archive/issue_comments_008720.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-02T04:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1361#issuecomment-8720",
    "user": "rlm"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008721.json:
```json
{
    "body": "Attachment [graph_gen.hg](tarball://root/attachments/some-uuid/ticket1361/graph_gen.hg) by rlm created at 2007-12-02 07:31:11",
    "created_at": "2007-12-02T07:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1361#issuecomment-8721",
    "user": "rlm"
}
```

Attachment [graph_gen.hg](tarball://root/attachments/some-uuid/ticket1361/graph_gen.hg) by rlm created at 2007-12-02 07:31:11



---

archive/issue_comments_008722.json:
```json
{
    "body": "Implementing in Cython should have little effect, since what is in Python is certainly not the bottleneck.",
    "created_at": "2007-12-02T07:31:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1361#issuecomment-8722",
    "user": "rlm"
}
```

Implementing in Cython should have little effect, since what is in Python is certainly not the bottleneck.



---

archive/issue_comments_008723.json:
```json
{
    "body": "Looks good to me.  (Code looks reasonable, doctests pass in sage/graphs/.)",
    "created_at": "2007-12-02T07:49:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1361#issuecomment-8723",
    "user": "cwitty"
}
```

Looks good to me.  (Code looks reasonable, doctests pass in sage/graphs/.)



---

archive/issue_comments_008724.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T08:09:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1361#issuecomment-8724",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_008725.json:
```json
{
    "body": "Merged in 2.8.15.alpha2.",
    "created_at": "2007-12-02T08:09:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1361#issuecomment-8725",
    "user": "mabshoff"
}
```

Merged in 2.8.15.alpha2.
