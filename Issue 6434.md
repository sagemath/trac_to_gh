# Issue 6434: [with patch, needs review] make a latex.py doctest more robust

archive/issues_006434.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nThere are a pair of doctests in latex.py whose output contains the entire latex preamble, which means that any time anyone changes the preamble (for example in #6417), it screws up the doctest.  This patch replaces most of the preamble with \"...\".\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6434\n\n",
    "created_at": "2009-06-27T17:35:01Z",
    "labels": [
        "misc",
        "minor",
        "enhancement"
    ],
    "title": "[with patch, needs review] make a latex.py doctest more robust",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6434",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

There are a pair of doctests in latex.py whose output contains the entire latex preamble, which means that any time anyone changes the preamble (for example in #6417), it screws up the doctest.  This patch replaces most of the preamble with "...".


Issue created by migration from https://trac.sagemath.org/ticket/6434





---

archive/issue_comments_051660.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-06-27T17:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6434#issuecomment-51660",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_051661.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-04T00:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6434#issuecomment-51661",
    "user": "rlm"
}
```

Resolution: fixed
