# Issue 5421: Speedup is_isomorphic

archive/issues_005421.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  mhansen\n\nBased on the thread at\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/1e3928bc2bffe9a6?pli=1\n\nseveral speedups have been implemented:\n\n1. Graphs which can be switched to `c_graph` are automatically switched before isomorphism testing (see thread).\n\n2. Several cheap imports have been moved to module level.\n\n3. One unnecessary step was removed.\n\nBenchmark: Take a list of all isomorphism classes of graphs on 7 vertices. Take one representative from each, and test each unordered pair for isomorphism. With underlying `c_graph` implementation, previously was 31.11 seconds, is now 10.71 seconds.\n\nThis patch also enables the `implementation` syntax in the graph generators.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5421\n\n",
    "created_at": "2009-03-02T18:36:52Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "Speedup is_isomorphic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5421",
    "user": "rlm"
}
```
Assignee: rlm

CC:  mhansen

Based on the thread at

http://groups.google.com/group/sage-devel/browse_thread/thread/1e3928bc2bffe9a6?pli=1

several speedups have been implemented:

1. Graphs which can be switched to `c_graph` are automatically switched before isomorphism testing (see thread).

2. Several cheap imports have been moved to module level.

3. One unnecessary step was removed.

Benchmark: Take a list of all isomorphism classes of graphs on 7 vertices. Take one representative from each, and test each unordered pair for isomorphism. With underlying `c_graph` implementation, previously was 31.11 seconds, is now 10.71 seconds.

This patch also enables the `implementation` syntax in the graph generators.

Issue created by migration from https://trac.sagemath.org/ticket/5421





---

archive/issue_comments_041937.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-02T18:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5421#issuecomment-41937",
    "user": "rlm"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041938.json:
```json
{
    "body": "One comment: note the deletion of the step checking whether the sorted degree sequences are the same. This is now an intrinsic part of the algorithm used for isomorphism checking, so this is redundant effort.",
    "created_at": "2009-03-02T18:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5421#issuecomment-41938",
    "user": "rlm"
}
```

One comment: note the deletion of the step checking whether the sorted degree sequences are the same. This is now an intrinsic part of the algorithm used for isomorphism checking, so this is redundant effort.



---

archive/issue_comments_041939.json:
```json
{
    "body": "Note: this is a patch based on Sage-3.3, so the documentation is still pre-reST",
    "created_at": "2009-03-02T19:27:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5421#issuecomment-41939",
    "user": "rlm"
}
```

Note: this is a patch based on Sage-3.3, so the documentation is still pre-reST



---

archive/issue_comments_041940.json:
```json
{
    "body": "Yep, the patch definitely needs a rebase:\n\n```\nmabshoff@sage:/scratch/mabshoff/sage-3.4.alpha1/devel/sage$ patch -p1 --dry-run < trac_5421.patch \npatching file sage/graphs/graph.py\nHunk #1 succeeded at 335 (offset 70 lines).\nHunk #2 succeeded at 7587 (offset 664 lines).\npatching file sage/graphs/graph_generators.py\nHunk #1 FAILED at 242.\nHunk #2 FAILED at 258.\nHunk #3 succeeded at 3111 with fuzz 2 (offset 308 lines).\nHunk #4 FAILED at 3143.\nHunk #5 succeeded at 3199 (offset 325 lines).\nHunk #6 FAILED at 3324.\nHunk #7 FAILED at 3338.\nHunk #8 succeeded at 3660 with fuzz 2 (offset 386 lines).\nHunk #9 FAILED at 3686.\nHunk #10 succeeded at 3739 with fuzz 1 (offset 403 lines).\nHunk #11 succeeded at 3870 (offset 419 lines).\nHunk #12 succeeded at 3894 (offset 419 lines).\nHunk #13 succeeded at 3907 (offset 419 lines).\nHunk #14 succeeded at 3952 with fuzz 1 (offset 421 lines).\nHunk #15 succeeded at 4092 (offset 434 lines).\nHunk #16 succeeded at 4111 (offset 434 lines).\n6 out of 16 hunks FAILED -- saving rejects to file sage/graphs/graph_generators.py.rej\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T19:59:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5421#issuecomment-41940",
    "user": "mabshoff"
}
```

Yep, the patch definitely needs a rebase:

```
mabshoff@sage:/scratch/mabshoff/sage-3.4.alpha1/devel/sage$ patch -p1 --dry-run < trac_5421.patch 
patching file sage/graphs/graph.py
Hunk #1 succeeded at 335 (offset 70 lines).
Hunk #2 succeeded at 7587 (offset 664 lines).
patching file sage/graphs/graph_generators.py
Hunk #1 FAILED at 242.
Hunk #2 FAILED at 258.
Hunk #3 succeeded at 3111 with fuzz 2 (offset 308 lines).
Hunk #4 FAILED at 3143.
Hunk #5 succeeded at 3199 (offset 325 lines).
Hunk #6 FAILED at 3324.
Hunk #7 FAILED at 3338.
Hunk #8 succeeded at 3660 with fuzz 2 (offset 386 lines).
Hunk #9 FAILED at 3686.
Hunk #10 succeeded at 3739 with fuzz 1 (offset 403 lines).
Hunk #11 succeeded at 3870 (offset 419 lines).
Hunk #12 succeeded at 3894 (offset 419 lines).
Hunk #13 succeeded at 3907 (offset 419 lines).
Hunk #14 succeeded at 3952 with fuzz 1 (offset 421 lines).
Hunk #15 succeeded at 4092 (offset 434 lines).
Hunk #16 succeeded at 4111 (offset 434 lines).
6 out of 16 hunks FAILED -- saving rejects to file sage/graphs/graph_generators.py.rej
```


Cheers,

Michael



---

archive/issue_comments_041941.json:
```json
{
    "body": "Attachment [trac_5421.patch](tarball://root/attachments/some-uuid/ticket5421/trac_5421.patch) by rlm created at 2009-03-02 20:18:49\n\nI rebased the patch to 3.4.alpha0, but I don't have a built copy yet, so I couldn't test. But I'm pretty sure it should work. What could go wrong?",
    "created_at": "2009-03-02T20:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5421#issuecomment-41941",
    "user": "rlm"
}
```

Attachment [trac_5421.patch](tarball://root/attachments/some-uuid/ticket5421/trac_5421.patch) by rlm created at 2009-03-02 20:18:49

I rebased the patch to 3.4.alpha0, but I don't have a built copy yet, so I couldn't test. But I'm pretty sure it should work. What could go wrong?



---

archive/issue_comments_041942.json:
```json
{
    "body": "One doctest failure:\n\n```\nmabshoff@sage:/scratch/mabshoff/sage-3.4.alpha1$ ./sage -t -long devel/sage/sage/combinat/words/suffix_trees.py\nsage -t -long \"devel/sage/sage/combinat/words/suffix_trees.py\"\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.alpha1/devel/sage/sage/combinat/words/suffix_trees.py\", line 1263:\n    sage: t.uncompactify().is_isomorphic(s.to_digraph())\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-3.4.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.4.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.4.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_38[6]>\", line 1, in <module>\n        t.uncompactify().is_isomorphic(s.to_digraph())###line 1263:\n    sage: t.uncompactify().is_isomorphic(s.to_digraph())\n      File \"/scratch/mabshoff/sage-3.4.alpha1/local/lib/python2.5/site-packages/sage/graphs/graph.py\", line 7631, in is_isomorphic\n        G2 = G2.copy(implementation='c_graph')\n      File \"/scratch/mabshoff/sage-3.4.alpha1/local/lib/python2.5/site-packages/sage/graphs/graph.py\", line 707, in copy\n        G = DiGraph(self, name=self.name(), pos=copy(self._pos), boundary=copy(self._boundary), implementation=implementation, sparse=sparse)\n      File \"/scratch/mabshoff/sage-3.4.alpha1/local/lib/python2.5/site-packages/sage/graphs/graph.py\", line 9859, in __init__\n        self._backend.add_edge(u,v,l,True)\n      File \"sparse_graph.pyx\", line 1171, in sage.graphs.base.sparse_graph.SparseGraphBackend.add_edge (sage/graphs/base/sparse_graph.c:9597)\n      File \"sparse_graph.pyx\", line 515, in sage.graphs.base.sparse_graph.SparseGraph.add_arc_label (sage/graphs/base/sparse_graph.c:3980)\n    TypeError: an integer is required\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_38\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/sage-3.4.alpha1/tmp/.doctest_suffix_trees.py\n         [2.9 s]\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T23:24:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5421#issuecomment-41942",
    "user": "mabshoff"
}
```

One doctest failure:

```
mabshoff@sage:/scratch/mabshoff/sage-3.4.alpha1$ ./sage -t -long devel/sage/sage/combinat/words/suffix_trees.py
sage -t -long "devel/sage/sage/combinat/words/suffix_trees.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.alpha1/devel/sage/sage/combinat/words/suffix_trees.py", line 1263:
    sage: t.uncompactify().is_isomorphic(s.to_digraph())
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.4.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_38[6]>", line 1, in <module>
        t.uncompactify().is_isomorphic(s.to_digraph())###line 1263:
    sage: t.uncompactify().is_isomorphic(s.to_digraph())
      File "/scratch/mabshoff/sage-3.4.alpha1/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 7631, in is_isomorphic
        G2 = G2.copy(implementation='c_graph')
      File "/scratch/mabshoff/sage-3.4.alpha1/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 707, in copy
        G = DiGraph(self, name=self.name(), pos=copy(self._pos), boundary=copy(self._boundary), implementation=implementation, sparse=sparse)
      File "/scratch/mabshoff/sage-3.4.alpha1/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 9859, in __init__
        self._backend.add_edge(u,v,l,True)
      File "sparse_graph.pyx", line 1171, in sage.graphs.base.sparse_graph.SparseGraphBackend.add_edge (sage/graphs/base/sparse_graph.c:9597)
      File "sparse_graph.pyx", line 515, in sage.graphs.base.sparse_graph.SparseGraph.add_arc_label (sage/graphs/base/sparse_graph.c:3980)
    TypeError: an integer is required
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_38
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/sage-3.4.alpha1/tmp/.doctest_suffix_trees.py
         [2.9 s]
```


Cheers,

Michael



---

archive/issue_comments_041943.json:
```json
{
    "body": "Looks like that second patch is not ready yet...",
    "created_at": "2009-03-03T07:23:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5421#issuecomment-41943",
    "user": "rlm"
}
```

Looks like that second patch is not ready yet...



---

archive/issue_comments_041944.json:
```json
{
    "body": "Attachment [trac_5421-b.patch](tarball://root/attachments/some-uuid/ticket5421/trac_5421-b.patch) by rlm created at 2009-03-04 20:02:41",
    "created_at": "2009-03-04T20:02:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5421#issuecomment-41944",
    "user": "rlm"
}
```

Attachment [trac_5421-b.patch](tarball://root/attachments/some-uuid/ticket5421/trac_5421-b.patch) by rlm created at 2009-03-04 20:02:41



---

archive/issue_comments_041945.json:
```json
{
    "body": "I forgot one line in patch b, now all is well.",
    "created_at": "2009-03-04T20:03:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5421#issuecomment-41945",
    "user": "rlm"
}
```

I forgot one line in patch b, now all is well.



---

archive/issue_comments_041946.json:
```json
{
    "body": "Mike: Can you give this patch a review? \n\nCheers,\n\nMichael",
    "created_at": "2009-03-08T05:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5421#issuecomment-41946",
    "user": "mabshoff"
}
```

Mike: Can you give this patch a review? 

Cheers,

Michael



---

archive/issue_comments_041947.json:
```json
{
    "body": "mabshoff has doctested.  I can't guarantee this speeds up {all,any} cases and I have only read over the modified code -- this is so deeply nested that I can only give a 3/4 thumbs up.",
    "created_at": "2009-03-08T06:35:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5421#issuecomment-41947",
    "user": "ncalexan"
}
```

mabshoff has doctested.  I can't guarantee this speeds up {all,any} cases and I have only read over the modified code -- this is so deeply nested that I can only give a 3/4 thumbs up.



---

archive/issue_comments_041948.json:
```json
{
    "body": "Merged both patches in Sage 3.4.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-08T06:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5421#issuecomment-41948",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.4.rc1.

Cheers,

Michael



---

archive/issue_comments_041949.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-08T06:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5421#issuecomment-41949",
    "user": "mabshoff"
}
```

Resolution: fixed
