# Issue 4854: represent paths as lists of edges

archive/issues_004854.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  brunellus\n\nFrom sage-devel:\n\n```\nWhile trying to model deterministic finite automata over Sage\n(multi-)graphs,\nI've run into the following: paths are represented as lists of vertices,\nregardless\nof edges. Superficial investigation shows that both sage.graph and\nnetworkx are somewhat grounded on this notion of path.\n\nBut! For finite automata and other word-accepting machines to be correctly\nrepresented paths should be considered as sequences of labeled edges, not\nvertices, as far as two vertices may be connected by differently labeled\nedges, and that is essential. \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4854\n\n",
    "created_at": "2008-12-22T19:24:26Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "represent paths as lists of edges",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4854",
    "user": "rlm"
}
```
Assignee: rlm

CC:  brunellus

From sage-devel:

```
While trying to model deterministic finite automata over Sage
(multi-)graphs,
I've run into the following: paths are represented as lists of vertices,
regardless
of edges. Superficial investigation shows that both sage.graph and
networkx are somewhat grounded on this notion of path.

But! For finite automata and other word-accepting machines to be correctly
represented paths should be considered as sequences of labeled edges, not
vertices, as far as two vertices may be connected by differently labeled
edges, and that is essential. 
```


Issue created by migration from https://trac.sagemath.org/ticket/4854





---

archive/issue_comments_036801.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4854#issuecomment-36801",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_036802.json:
```json
{
    "body": "Hmmmm... As I have not met any Patch class in Sage, I assume you are using functions on graphs returning paths, which are not encoded as you may like.... Could you tell me which functions you are talking about, in case I made no mistake ? :-)",
    "created_at": "2009-08-14T16:05:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4854#issuecomment-36802",
    "user": "ncohen"
}
```

Hmmmm... As I have not met any Patch class in Sage, I assume you are using functions on graphs returning paths, which are not encoded as you may like.... Could you tell me which functions you are talking about, in case I made no mistake ? :-)



---

archive/issue_comments_036803.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-02-22T21:33:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4854#issuecomment-36803",
    "user": "ncohen"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_036804.json:
```json
{
    "body": "What might be required is a keyword such as \"as_edge\" for methods that return paths. So if \"as_edge=True\", return the path as a list of edges. If \"as_edge=False\" (which is default), return the path as a list of vertices.",
    "created_at": "2010-04-19T03:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4854#issuecomment-36804",
    "user": "mvngu"
}
```

What might be required is a keyword such as "as_edge" for methods that return paths. So if "as_edge=True", return the path as a list of edges. If "as_edge=False" (which is default), return the path as a list of vertices.
