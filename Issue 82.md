# Issue 82: bug in eigenvalues over a number field

archive/issues_000082.json:
```json
{
    "body": "Assignee: @williamstein\n\nsage: M = MatrixSpace(RationalField(),2,2)\n\nsage: A = M([1,-4,1, -1])\n\nsage: p = A.charpoly()\n\nsage: K = NumberField(p,'alpha')\n\nsage: M = MatrixSpace(K,2,2)\n\nsage: A = M([1,-4,1, -1])\n\nsage: A.eigenvectors()\n\nfails at the last step. However, \n\nsage: M = MatrixSpace(RationalField(),2,2)\n\nsage: A = M([1,-4,1, -1])\n\nsage: A.eigenvectors()\n\n [(1, a - 1)]\n\nworks, though \"a\" is undefined.\n\nIssue created by migration from https://trac.sagemath.org/ticket/82\n\n",
    "created_at": "2006-09-24T19:43:16Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "title": "bug in eigenvalues over a number field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/82",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: @williamstein

sage: M = MatrixSpace(RationalField(),2,2)

sage: A = M([1,-4,1, -1])

sage: p = A.charpoly()

sage: K = NumberField(p,'alpha')

sage: M = MatrixSpace(K,2,2)

sage: A = M([1,-4,1, -1])

sage: A.eigenvectors()

fails at the last step. However, 

sage: M = MatrixSpace(RationalField(),2,2)

sage: A = M([1,-4,1, -1])

sage: A.eigenvectors()

 [(1, a - 1)]

works, though "a" is undefined.

Issue created by migration from https://trac.sagemath.org/ticket/82





---

archive/issue_comments_000414.json:
```json
{
    "body": "Note.  In the second example a is not undefined.  It's the print representation of the generator\nof a number field.  It's not supposed to suddenly be injected into the current scope. \n\n```\nsage: V =A.eigenvectors()\nsage: V[0][1].parent()\n Number Field in a with defining polynomial x^2 + 3\n```\n",
    "created_at": "2006-09-25T23:12:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/82",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/82#issuecomment-414",
    "user": "https://github.com/williamstein"
}
```

Note.  In the second example a is not undefined.  It's the print representation of the generator
of a number field.  It's not supposed to suddenly be injected into the current scope. 

```
sage: V =A.eigenvectors()
sage: V[0][1].parent()
 Number Field in a with defining polynomial x^2 + 3
```




---

archive/issue_comments_000415.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-12T22:20:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/82",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/82#issuecomment-415",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_000416.json:
```json
{
    "body": "It now works (though notation slightly different now):\n\n```\nsage: M = MatrixSpace(RationalField(),2,2)\nsage: A = M([1,-4,1, -1])\nsage: p = A.charpoly()\nsage: K = NumberField(p,'alpha')\nsage: M = MatrixSpace(K,2,2)\nsage: A = M([1,-4,1, -1])\nsage: A.eigenspaces()\n[\n(alpha, [\n(1, alpha - 1)\n]),\n(-alpha, [\n(1, -alpha - 1)\n])\n]\n```\n",
    "created_at": "2007-01-12T22:20:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/82",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/82#issuecomment-416",
    "user": "https://github.com/williamstein"
}
```

It now works (though notation slightly different now):

```
sage: M = MatrixSpace(RationalField(),2,2)
sage: A = M([1,-4,1, -1])
sage: p = A.charpoly()
sage: K = NumberField(p,'alpha')
sage: M = MatrixSpace(K,2,2)
sage: A = M([1,-4,1, -1])
sage: A.eigenspaces()
[
(alpha, [
(1, alpha - 1)
]),
(-alpha, [
(1, -alpha - 1)
])
]
```




---

archive/issue_events_000082.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-01-12T22:20:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/82",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/82#event-82"
}
```
