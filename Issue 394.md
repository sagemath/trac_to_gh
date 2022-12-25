# Issue 394: flatten command for nested lists

archive/issues_000394.json:
```json
{
    "body": "Assignee: mhampton\n\nKeywords: lists, flatten\n\nThe attached file has a candidate function for a flatten command. The default types to flatten are lists and tuples, but more can be added.  Here are the examples from my EXAMPLES section:\n\n\n```\nEXAMPLES:\n        sage: flatten([[1,1],[1],2])\n        [1, 1, 1, 2]\n        sage: flatten((['Hi',2,vector(QQ,[1,2,3])],(4,5,6)))\n        ['Hi', 2, (1, 2, 3), 4, 5, 6]\n        sage: flatten((['Hi',2,vector(QQ,[1,2,3])],(4,5,6)),ltypes=(list, tuple, sage.modules.vector_rational_dense.Vector_rational_dense))\n        ['Hi', 2, 1, 2, 3, 4, 5, 6]\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/394\n\n",
    "created_at": "2007-06-28T16:04:21Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "title": "flatten command for nested lists",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/394",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: mhampton

Keywords: lists, flatten

The attached file has a candidate function for a flatten command. The default types to flatten are lists and tuples, but more can be added.  Here are the examples from my EXAMPLES section:


```
EXAMPLES:
        sage: flatten([[1,1],[1],2])
        [1, 1, 1, 2]
        sage: flatten((['Hi',2,vector(QQ,[1,2,3])],(4,5,6)))
        ['Hi', 2, (1, 2, 3), 4, 5, 6]
        sage: flatten((['Hi',2,vector(QQ,[1,2,3])],(4,5,6)),ltypes=(list, tuple, sage.modules.vector_rational_dense.Vector_rational_dense))
        ['Hi', 2, 1, 2, 3, 4, 5, 6]
```



Issue created by migration from https://trac.sagemath.org/ticket/394





---

archive/issue_comments_001923.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2007-06-28T16:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/394#issuecomment-1923",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Resolution: duplicate



---

archive/issue_events_000416.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mhampton",
    "created_at": "2007-06-28T16:07:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/394",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/394#event-416"
}
```
