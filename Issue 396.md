# Issue 396: vector-vector produc ts

archive/issues_000396.json:
```json
{
    "body": "Assignee: was\n\nMultiplying a mix of vectors and matrices is allowed presently in sage, but it is not associative:\n\n```\nv=vector([1,2,3])\nM=matrix([[1,0],[0,1],[1,1]])\nw=vector([1,2])\n\nprint v*M*w\nprint (v*M)*w\nprint v*(M*w)\n///\n(4, 10)\n(4, 10)\n(1, 4, 9)\n```\n\nIt is a combination of vectors not knowing whether they are row- or column vectors (probably good)\nand that v * w has the odd meaning of doing a component-wise multiplication. Perhaps it inherits the method from lists or something? It would be safest to explicitly cast an error if one tries to multiply vectors.\n\nIssue created by migration from https://trac.sagemath.org/ticket/396\n\n",
    "created_at": "2007-06-28T23:46:25Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "vector-vector produc ts",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/396",
    "user": "nbruin"
}
```
Assignee: was

Multiplying a mix of vectors and matrices is allowed presently in sage, but it is not associative:

```
v=vector([1,2,3])
M=matrix([[1,0],[0,1],[1,1]])
w=vector([1,2])

print v*M*w
print (v*M)*w
print v*(M*w)
///
(4, 10)
(4, 10)
(1, 4, 9)
```

It is a combination of vectors not knowing whether they are row- or column vectors (probably good)
and that v * w has the odd meaning of doing a component-wise multiplication. Perhaps it inherits the method from lists or something? It would be safest to explicitly cast an error if one tries to multiply vectors.

Issue created by migration from https://trac.sagemath.org/ticket/396





---

archive/issue_comments_001949.json:
```json
{
    "body": "The multiplication comes from FreeModule:\n\nsage: F = FreeModule(QQ, 3)\nsage: a = F([1,2,3])\nsage: b = F([1,2,3])\nsage: a*b\n(1, 4, 9)\n\nI think that this is wrong.",
    "created_at": "2007-09-06T17:31:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/396#issuecomment-1949",
    "user": "mhansen"
}
```

The multiplication comes from FreeModule:

sage: F = FreeModule(QQ, 3)
sage: a = F([1,2,3])
sage: b = F([1,2,3])
sage: a*b
(1, 4, 9)

I think that this is wrong.



---

archive/issue_comments_001950.json:
```json
{
    "body": "Changing component from algebraic geometry to linear algebra.",
    "created_at": "2007-09-06T20:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/396#issuecomment-1950",
    "user": "was"
}
```

Changing component from algebraic geometry to linear algebra.



---

archive/issue_comments_001951.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-09-06T23:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/396#issuecomment-1951",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_001952.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-07T00:04:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/396#issuecomment-1952",
    "user": "was"
}
```

Resolution: fixed
