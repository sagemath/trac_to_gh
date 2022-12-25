# Issue 5440: Failure to restart %magma in notebook.

archive/issues_005440.json:
```json
{
    "body": "Assignee: boothby\n\nIn the notebook, if one does:\n\n  %magma \n  quit;\n\nthen\n\n  %magma\n  1+1\n\none gets an error (the terminated magma process \napparently does not get restarted).\n\nIt works fine in the shell.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5440\n\n",
    "created_at": "2009-03-05T16:26:39Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Failure to restart %magma in notebook.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5440",
    "user": "https://trac.sagemath.org/admin/accounts/users/kohel"
}
```
Assignee: boothby

In the notebook, if one does:

  %magma 
  quit;

then

  %magma
  1+1

one gets an error (the terminated magma process 
apparently does not get restarted).

It works fine in the shell.

Issue created by migration from https://trac.sagemath.org/ticket/5440





---

archive/issue_comments_041999.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5440#issuecomment-41999",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Resolution: invalid



---

archive/issue_comments_042000.json:
```json
{
    "body": "Closing deprecated notebook tickets",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5440#issuecomment-42000",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Closing deprecated notebook tickets
