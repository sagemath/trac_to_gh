# Issue 243: two permutation group bugs: __contains__ hangs.

archive/issues_000243.json:
```json
{
    "body": "Assignee: somebody\n\nFrom David Kohel\n\n```\nsage: G = SymmetricGroup(16)\nsage: g = G.random() # note random_element doesn't exist which seems to be the SAGE preference\nsage: parent(g) is G\nTrue\nsage: parent(g) == G\nTrue\nsage: g in G # hangs despite the above...not sure where it goes wrong\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/243\n\n",
    "created_at": "2007-02-04T22:51:48Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "two permutation group bugs: __contains__ hangs.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/243",
    "user": "@williamstein"
}
```
Assignee: somebody

From David Kohel

```
sage: G = SymmetricGroup(16)
sage: g = G.random() # note random_element doesn't exist which seems to be the SAGE preference
sage: parent(g) is G
True
sage: parent(g) == G
True
sage: g in G # hangs despite the above...not sure where it goes wrong
```


Issue created by migration from https://trac.sagemath.org/ticket/243





---

archive/issue_comments_001078.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-02-05T07:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/243#issuecomment-1078",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_001079.json:
```json
{
    "body": "David Kohel fixed this.",
    "created_at": "2007-02-05T07:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/243#issuecomment-1079",
    "user": "@williamstein"
}
```

David Kohel fixed this.
