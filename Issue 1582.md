# Issue 1582: 2.9.1.alph2: doctest failure in sage/graphs/graph.py with x86 Linux

archive/issues_001582.json:
```json
{
    "body": "Assignee: @rlmill\n\nJaap reported:\n\n```\nsage -t  devel/sage-main/sage/graphs/graph.py\n**********************************************************************\nFile \"graph.py\", line 4150:\n     sage: E[1][0]\nExpected:\n     Vector space of degree 5 and dimension 1 over Real Double Field\n     User basis matrix:\n     [ 0.632455532034 -0.632455532034   -0.4472135955 -0.013900198608 0.0738411279702]\nGot:\n     Vector space of degree 5 and dimension 1 over Real Double Field\n     User basis matrix:\n     [  0.632455532034  -0.632455532034    -0.4472135955   0.047561829961 -0.0797092534371]\n********************************************************************** \n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1582\n\n",
    "created_at": "2007-12-21T12:27:52Z",
    "labels": [
        "doctest coverage",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.1",
    "title": "2.9.1.alph2: doctest failure in sage/graphs/graph.py with x86 Linux",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1582",
    "user": "mabshoff"
}
```
Assignee: @rlmill

Jaap reported:

```
sage -t  devel/sage-main/sage/graphs/graph.py
**********************************************************************
File "graph.py", line 4150:
     sage: E[1][0]
Expected:
     Vector space of degree 5 and dimension 1 over Real Double Field
     User basis matrix:
     [ 0.632455532034 -0.632455532034   -0.4472135955 -0.013900198608 0.0738411279702]
Got:
     Vector space of degree 5 and dimension 1 over Real Double Field
     User basis matrix:
     [  0.632455532034  -0.632455532034    -0.4472135955   0.047561829961 -0.0797092534371]
********************************************************************** 
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1582





---

archive/issue_comments_010079.json:
```json
{
    "body": "\n```\n[4:44pm] wstein-924: Regarding the graph.py example, I would just put\n[4:44pm] wstein-924: sage: E[1][0]    # eigenspace computation is somewhat random.\n[4:45pm] rlm-1584: +1\n```\n\n\nMerged in 2.9.1 alpha3",
    "created_at": "2007-12-21T22:13:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1582#issuecomment-10079",
    "user": "@rlmill"
}
```


```
[4:44pm] wstein-924: Regarding the graph.py example, I would just put
[4:44pm] wstein-924: sage: E[1][0]    # eigenspace computation is somewhat random.
[4:45pm] rlm-1584: +1
```


Merged in 2.9.1 alpha3



---

archive/issue_comments_010080.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-21T22:13:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1582#issuecomment-10080",
    "user": "@rlmill"
}
```

Resolution: fixed
