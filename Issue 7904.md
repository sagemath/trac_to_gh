# Issue 7904: is_gallai_tree

archive/issues_007904.json:
```json
{
    "body": "Assignee: @rlmill\n\nFrom the docstring : \nA graph is a Gallai tree if and only if it is connected and its `2`-connected components are all isomorphic to complete graphs or odd cycles.\n\nThis patch also slightly touches the function is_clique, which was unnecessarily copying the whole graph 2 times :\n* Firstly, using the subgraph method\n* Secondly, using the to_simple method\n\nIssue created by migration from https://trac.sagemath.org/ticket/7904\n\n",
    "created_at": "2010-01-12T08:16:07Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "is_gallai_tree",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7904",
    "user": "@nathanncohen"
}
```
Assignee: @rlmill

From the docstring : 
A graph is a Gallai tree if and only if it is connected and its `2`-connected components are all isomorphic to complete graphs or odd cycles.

This patch also slightly touches the function is_clique, which was unnecessarily copying the whole graph 2 times :
* Firstly, using the subgraph method
* Secondly, using the to_simple method

Issue created by migration from https://trac.sagemath.org/ticket/7904





---

archive/issue_comments_068728.json:
```json
{
    "body": "Attachment [trac_7904.patch](tarball://root/attachments/some-uuid/ticket7904/trac_7904.patch) by @nathanncohen created at 2010-01-12 08:16:42",
    "created_at": "2010-01-12T08:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7904#issuecomment-68728",
    "user": "@nathanncohen"
}
```

Attachment [trac_7904.patch](tarball://root/attachments/some-uuid/ticket7904/trac_7904.patch) by @nathanncohen created at 2010-01-12 08:16:42



---

archive/issue_comments_068729.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-12T08:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7904#issuecomment-68729",
    "user": "@nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068730.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-03-17T05:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7904#issuecomment-68730",
    "user": "@jasongrout"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_068731.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-05-20T20:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7904#issuecomment-68731",
    "user": "@nathanncohen"
}
```

Changing priority from major to minor.



---

archive/issue_comments_068732.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-18T23:56:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7904#issuecomment-68732",
    "user": "@rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068733.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-29T16:46:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7904#issuecomment-68733",
    "user": "@rlmill"
}
```

Resolution: fixed
