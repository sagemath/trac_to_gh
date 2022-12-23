# Issue 352: error in matrix creation options

archive/issues_000352.json:
```json
{
    "body": "Assignee: was\n\n\n```\n> After trying some things, I've noticed that it is possible to coerce a\n> flat list into a sparse matrix but not a list of lists.\n> \n> E.G.\n> sage: B = MatrixSpace(ZZ,5,5)\n> sage: v = [0 for i in range(25)]\n> sage: u = [[0 for i in range(5)] for j in range(5)]\n> sage: B(v)\n> [0 0 0 0 0]\n> [0 0 0 0 0]\n> [0 0 0 0 0]\n> [0 0 0 0 0]\n> [0 0 0 0 0]\n> \n> sage: B(u) ---> results in the same error as before.\n> Is there a conceptual reason that a flat list works, but a list of\n\nThat looks like just a mistake on our paper.  We should make\nit so both cases work. \n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/352\n\n",
    "created_at": "2007-04-19T21:15:46Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "title": "error in matrix creation options",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/352",
    "user": "was"
}
```
Assignee: was


```
> After trying some things, I've noticed that it is possible to coerce a
> flat list into a sparse matrix but not a list of lists.
> 
> E.G.
> sage: B = MatrixSpace(ZZ,5,5)
> sage: v = [0 for i in range(25)]
> sage: u = [[0 for i in range(5)] for j in range(5)]
> sage: B(v)
> [0 0 0 0 0]
> [0 0 0 0 0]
> [0 0 0 0 0]
> [0 0 0 0 0]
> [0 0 0 0 0]
> 
> sage: B(u) ---> results in the same error as before.
> Is there a conceptual reason that a flat list works, but a list of

That looks like just a mistake on our paper.  We should make
it so both cases work. 
```



Issue created by migration from https://trac.sagemath.org/ticket/352





---

archive/issue_comments_001709.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-18T23:53:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/352#issuecomment-1709",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_001710.json:
```json
{
    "body": "This work since at least Sage 2.8.1\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.1, Release Date: 2007-08-18                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: B = MatrixSpace(ZZ,5,5)\nsage: v = [0 for i in range(25)]\nsage: u = [[0 for i in range(5)] for j in range(5)]\nsage: B(u)\n\n[0 0 0 0 0]\n[0 0 0 0 0]\n[0 0 0 0 0]\n[0 0 0 0 0]\n[0 0 0 0 0]\nsage: B(v)\n\n[0 0 0 0 0]\n[0 0 0 0 0]\n[0 0 0 0 0]\n[0 0 0 0 0]\n[0 0 0 0 0]\n```\n",
    "created_at": "2007-08-18T23:53:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/352#issuecomment-1710",
    "user": "mabshoff"
}
```

This work since at least Sage 2.8.1


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.1, Release Date: 2007-08-18                       |
| Type notebook() for the GUI, and license() for information.        |
sage: B = MatrixSpace(ZZ,5,5)
sage: v = [0 for i in range(25)]
sage: u = [[0 for i in range(5)] for j in range(5)]
sage: B(u)

[0 0 0 0 0]
[0 0 0 0 0]
[0 0 0 0 0]
[0 0 0 0 0]
[0 0 0 0 0]
sage: B(v)

[0 0 0 0 0]
[0 0 0 0 0]
[0 0 0 0 0]
[0 0 0 0 0]
[0 0 0 0 0]
```

