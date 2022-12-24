# Issue 442: RDF roots() function gives imprecise results

archive/issues_000442.json:
```json
{
    "body": "Assignee: rlm\n\nFor example:\n\nsage: x = polygen(RDF)\nsage: f = (x-1)^3\nsage: f.roots()\n\n[1.00000859959,\n 0.999995700205 + 7.44736245561e-06*I,\n 0.999995700205 - 7.44736245561e-06*I]\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/442\n\n",
    "created_at": "2007-08-18T19:17:27Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.2",
    "title": "RDF roots() function gives imprecise results",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/442",
    "user": "rlm"
}
```
Assignee: rlm

For example:

sage: x = polygen(RDF)
sage: f = (x-1)^3
sage: f.roots()

[1.00000859959,
 0.999995700205 + 7.44736245561e-06*I,
 0.999995700205 - 7.44736245561e-06*I]


Issue created by migration from https://trac.sagemath.org/ticket/442





---

archive/issue_comments_002209.json:
```json
{
    "body": "in sage-2.8.1/local/lib/python2.5/site-packages/numpy/lib/polynomial.py,\nline 116 appears to be casting whatever float type is given to just float.",
    "created_at": "2007-08-18T19:44:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/442#issuecomment-2209",
    "user": "rlm"
}
```

in sage-2.8.1/local/lib/python2.5/site-packages/numpy/lib/polynomial.py,
line 116 appears to be casting whatever float type is given to just float.



---

archive/issue_comments_002210.json:
```json
{
    "body": "This is just as much an issue for eigen_left and eigen_right:\n \nsage: g = Matrix(RDF, [[0, -9],[1,6]]); g\n[ 0.0 -9.0]\n[ 1.0  6.0]\nsage: g.eigen_left()\n([3.00000003183, 2.99999996817], .....",
    "created_at": "2007-08-18T20:24:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/442#issuecomment-2210",
    "user": "rlm"
}
```

This is just as much an issue for eigen_left and eigen_right:
 
sage: g = Matrix(RDF, [[0, -9],[1,6]]); g
[ 0.0 -9.0]
[ 1.0  6.0]
sage: g.eigen_left()
([3.00000003183, 2.99999996817], .....



---

archive/issue_comments_002211.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2007-08-18T20:33:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/442#issuecomment-2211",
    "user": "rlm"
}
```

Resolution: duplicate



---

archive/issue_comments_002212.json:
```json
{
    "body": "See ticket #211.",
    "created_at": "2007-08-18T20:33:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/442#issuecomment-2212",
    "user": "rlm"
}
```

See ticket #211.
