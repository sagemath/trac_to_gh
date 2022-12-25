# Issue 6434: [with patch, needs review] make a latex.py doctest more robust

archive/issues_006434.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nThere are a pair of doctests in latex.py whose output contains the entire latex preamble, which means that any time anyone changes the preamble (for example in #6417), it screws up the doctest.  This patch replaces most of the preamble with \"...\".\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6434\n\n",
    "created_at": "2009-06-27T17:35:01Z",
    "labels": [
        "component: misc",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "[with patch, needs review] make a latex.py doctest more robust",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6434",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

There are a pair of doctests in latex.py whose output contains the entire latex preamble, which means that any time anyone changes the preamble (for example in #6417), it screws up the doctest.  This patch replaces most of the preamble with "...".


Issue created by migration from https://trac.sagemath.org/ticket/6434





---

archive/issue_comments_051563.json:
```json
{
    "body": "Attachment [latex_6434.patch](tarball://root/attachments/some-uuid/ticket6434/latex_6434.patch) by @jhpalmieri created at 2009-06-27 17:35:25",
    "created_at": "2009-06-27T17:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6434#issuecomment-51563",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [latex_6434.patch](tarball://root/attachments/some-uuid/ticket6434/latex_6434.patch) by @jhpalmieri created at 2009-06-27 17:35:25



---

archive/issue_comments_051564.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-04T00:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6434#issuecomment-51564",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_006675.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-07-04T00:53:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6434",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6434#event-6675"
}
```
