# Issue 4002: raise coverage of sage.graphs to 100%

archive/issues_004002.json:
```json
{
    "body": "Assignee: rlm\n\nIn progress...\n\nIssue created by migration from https://trac.sagemath.org/ticket/4002\n\n",
    "created_at": "2008-08-30T17:43:32Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "raise coverage of sage.graphs to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4002",
    "user": "rlm"
}
```
Assignee: rlm

In progress...

Issue created by migration from https://trac.sagemath.org/ticket/4002





---

archive/issue_comments_028903.json:
```json
{
    "body": "Attachment [trac_4002.patch](tarball://root/attachments/some-uuid/ticket4002/trac_4002.patch) by rlm created at 2008-08-30 18:59:47\n\nmhansen will finish `linearextensions.py`, I am now working on the few missing doctests in `graph_generators.py`",
    "created_at": "2008-08-30T18:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4002#issuecomment-28903",
    "user": "rlm"
}
```

Attachment [trac_4002.patch](tarball://root/attachments/some-uuid/ticket4002/trac_4002.patch) by rlm created at 2008-08-30 18:59:47

mhansen will finish `linearextensions.py`, I am now working on the few missing doctests in `graph_generators.py`



---

archive/issue_comments_028904.json:
```json
{
    "body": "Attachment [trac_4002-ggen.patch](tarball://root/attachments/some-uuid/ticket4002/trac_4002-ggen.patch) by rlm created at 2008-08-30 19:08:01",
    "created_at": "2008-08-30T19:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4002#issuecomment-28904",
    "user": "rlm"
}
```

Attachment [trac_4002-ggen.patch](tarball://root/attachments/some-uuid/ticket4002/trac_4002-ggen.patch) by rlm created at 2008-08-30 19:08:01



---

archive/issue_comments_028905.json:
```json
{
    "body": "Attachment [trac_4002-3.patch](tarball://root/attachments/some-uuid/ticket4002/trac_4002-3.patch) by mhansen created at 2008-08-31 03:30:59",
    "created_at": "2008-08-31T03:30:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4002#issuecomment-28905",
    "user": "mhansen"
}
```

Attachment [trac_4002-3.patch](tarball://root/attachments/some-uuid/ticket4002/trac_4002-3.patch) by mhansen created at 2008-08-31 03:30:59



---

archive/issue_comments_028906.json:
```json
{
    "body": "These three patches apply in order to 3.1.2.alpha2, running `sage -t` all tests pass in `sage/graphs`, and afterwards we have:\n\n```\n./sage -coverageall /sage/graphs\nbase/c_graph.pyx: 100% (15 of 15)\nbase/sparse_graph.pyx: 100% (28 of 28)\nbase/graph_backends.py: 100% (51 of 51)\nbase/dense_graph.pyx: 100% (21 of 21)\nbipartite_graph.py: 100% (10 of 10)\nchrompoly.pyx: 100% (1 of 1)\ngraph_bundle.py: 100% (5 of 5)\ngraph_coloring.py: 100% (5 of 5)\ngraph_database.py: 100% (18 of 18)\ngraph_fast.pyx: 100% (8 of 8)\ngraph_generators.py: 100% (65 of 65)\ngraph_isom.pyx: 100% (27 of 27)\ngraph_list.py: 100% (7 of 7)\ngraph.py: 100% (193 of 193)\nlinearextensions.py: 100% (7 of 7)\nplanarity.pyx: 100% (1 of 1)\nprint_graphs.py: 100% (5 of 5)\nschnyder.py: 100% (8 of 8)\n\nOverall weighted coverage score:  100.0%\nTotal number of functions:  475\n```\n",
    "created_at": "2008-08-31T03:38:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4002#issuecomment-28906",
    "user": "rlm"
}
```

These three patches apply in order to 3.1.2.alpha2, running `sage -t` all tests pass in `sage/graphs`, and afterwards we have:

```
./sage -coverageall /sage/graphs
base/c_graph.pyx: 100% (15 of 15)
base/sparse_graph.pyx: 100% (28 of 28)
base/graph_backends.py: 100% (51 of 51)
base/dense_graph.pyx: 100% (21 of 21)
bipartite_graph.py: 100% (10 of 10)
chrompoly.pyx: 100% (1 of 1)
graph_bundle.py: 100% (5 of 5)
graph_coloring.py: 100% (5 of 5)
graph_database.py: 100% (18 of 18)
graph_fast.pyx: 100% (8 of 8)
graph_generators.py: 100% (65 of 65)
graph_isom.pyx: 100% (27 of 27)
graph_list.py: 100% (7 of 7)
graph.py: 100% (193 of 193)
linearextensions.py: 100% (7 of 7)
planarity.pyx: 100% (1 of 1)
print_graphs.py: 100% (5 of 5)
schnyder.py: 100% (8 of 8)

Overall weighted coverage score:  100.0%
Total number of functions:  475
```




---

archive/issue_comments_028907.json:
```json
{
    "body": "Positive review on Robert's first two patches.",
    "created_at": "2008-08-31T03:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4002#issuecomment-28907",
    "user": "mhansen"
}
```

Positive review on Robert's first two patches.



---

archive/issue_comments_028908.json:
```json
{
    "body": "Merged all three patches in Sage 3.1.2.alpha3",
    "created_at": "2008-08-31T04:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4002#issuecomment-28908",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 3.1.2.alpha3



---

archive/issue_comments_028909.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-31T04:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4002#issuecomment-28909",
    "user": "mabshoff"
}
```

Resolution: fixed
