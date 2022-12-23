# Issue 8878: Use Dijkstra to discover shortest coercion path

archive/issues_008878.json:
```json
{
    "body": "Assignee: robertwb\n\nCC:  sage-combinat\n\nKeywords: coercion, morphism\n\nIn #7420, it was discussed that the current coercion model is using depth first search to find for coercion paths between different parents, and that it would be better to use breath-first / Dijkstra to get a shortest coercion path. For example, we obtained once a coercion path of length 20 among symmetric functions.\n\nPatch under development on the Sage-Combinat server.\n\nNote: the following issue is probably related:\n\n```\nA = CombinatorialFreeModule(QQ, ZZ, prefix = \"A\")\nB = CombinatorialFreeModule(QQ, ZZ, prefix = \"B\")\nC = CombinatorialFreeModule(QQ, ZZ, prefix = \"C\")\nD = CombinatorialFreeModule(QQ, ZZ, prefix = \"D\")\n\ndef make_morph(X, Y):\n    X.module_morphism(Y.monomial).register_as_coercion()\n\nmake_morph(A,B)\nmake_morph(B,A)\n\nmake_morph(C,A)\n\nmake_morph(D,C)\n\nd = D.monomial(1)\n\nA(d)\nB(d)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8878\n\n",
    "created_at": "2010-05-04T23:35:06Z",
    "labels": [
        "coercion",
        "major",
        "bug"
    ],
    "title": "Use Dijkstra to discover shortest coercion path",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8878",
    "user": "nthiery"
}
```
Assignee: robertwb

CC:  sage-combinat

Keywords: coercion, morphism

In #7420, it was discussed that the current coercion model is using depth first search to find for coercion paths between different parents, and that it would be better to use breath-first / Dijkstra to get a shortest coercion path. For example, we obtained once a coercion path of length 20 among symmetric functions.

Patch under development on the Sage-Combinat server.

Note: the following issue is probably related:

```
A = CombinatorialFreeModule(QQ, ZZ, prefix = "A")
B = CombinatorialFreeModule(QQ, ZZ, prefix = "B")
C = CombinatorialFreeModule(QQ, ZZ, prefix = "C")
D = CombinatorialFreeModule(QQ, ZZ, prefix = "D")

def make_morph(X, Y):
    X.module_morphism(Y.monomial).register_as_coercion()

make_morph(A,B)
make_morph(B,A)

make_morph(C,A)

make_morph(D,C)

d = D.monomial(1)

A(d)
B(d)
```


Issue created by migration from https://trac.sagemath.org/ticket/8878





---

archive/issue_comments_081584.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-05-04T23:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8878#issuecomment-81584",
    "user": "nthiery"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_081585.json:
```json
{
    "body": "The link to sage-combinat is dead.\n\n(Posting this mainly to get a CC on this ticket.)",
    "created_at": "2013-06-22T23:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8878#issuecomment-81585",
    "user": "darij"
}
```

The link to sage-combinat is dead.

(Posting this mainly to get a CC on this ticket.)
