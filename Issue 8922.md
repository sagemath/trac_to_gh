# Issue 8922: induced subgraph search

archive/issues_008922.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nThis patch add to Sage the method Graph.induced_subgraph_search which looks for a given graph as an induced subgraph of \"self\".\n\nThis is done through exhaustive search, using a very basic new graph class hand-made to efficiently stand such repetitive operations !\n\nI tried to document the code so that it could be somewhat easy to review, but feel free to ask any question about it ! :-)\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/8922\n\n",
    "created_at": "2010-05-07T18:58:33Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "induced subgraph search",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8922",
    "user": "ncohen"
}
```
Assignee: jason, ncohen, rlm

This patch add to Sage the method Graph.induced_subgraph_search which looks for a given graph as an induced subgraph of "self".

This is done through exhaustive search, using a very basic new graph class hand-made to efficiently stand such repetitive operations !

I tried to document the code so that it could be somewhat easy to review, but feel free to ask any question about it ! :-)

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/8922





---

archive/issue_comments_082188.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-07T19:01:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8922#issuecomment-82188",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082189.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2010-05-20T20:06:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8922#issuecomment-82189",
    "user": "ncohen"
}
```

Changing priority from major to critical.



---

archive/issue_comments_082190.json:
```json
{
    "body": "Updated ! Changes :\n\n* it took me some time, but I tested the new graph classes StaticDenseGraph this patch introduced against the already implemented DenseGraph.... Which turned out to be more efficient.. So this new class has disappeared, and the new code is now written into the usual Sage files instead of new ones\n\n* a -- very nasty -- memory leak -- now fixed\n\n* add functions to test for induced as well as non-induced subgraphs, as it is the same.. Also works with DiGraphs, by the way !\n\nAnd once this patch will be merged into Sage... I will have many other things to write on top of it :-)\n\nNathann",
    "created_at": "2010-05-25T23:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8922#issuecomment-82190",
    "user": "ncohen"
}
```

Updated ! Changes :

* it took me some time, but I tested the new graph classes StaticDenseGraph this patch introduced against the already implemented DenseGraph.... Which turned out to be more efficient.. So this new class has disappeared, and the new code is now written into the usual Sage files instead of new ones

* a -- very nasty -- memory leak -- now fixed

* add functions to test for induced as well as non-induced subgraphs, as it is the same.. Also works with DiGraphs, by the way !

And once this patch will be merged into Sage... I will have many other things to write on top of it :-)

Nathann



---

archive/issue_comments_082191.json:
```json
{
    "body": "Replying to [comment:3 ncohen]:\n>     * it took me some time, but I tested the new graph classes StaticDenseGraph this patch introduced against the already implemented DenseGraph.... Which turned out to be more efficient.. So this new class has disappeared, and the new code is now written into the usual Sage files instead of new ones\n\nI have been reviewing your previous patch for over two days and went the same route as you have done in your current patch. That is, I rewrote your StaticDenseGraph to use the C graph based DenseGraph class, as it is very efficient in terms of storage. The reason why I have not uploaded my reviewer patch is that I was thinking about and playing with how to make the method `adjacency_list` more efficient in terms of storage. An array of ints is wasteful for the intended purpose, when a bitset is more suited to the purpose. What has been bugging me is trying to get my bitset implementation of `adjacency_list` to compile and work.\n\n\n\n\n>     * a -- very nasty -- memory leak -- now fixed\n\nAgain, I went the same route in my reviewer patch.\n\n\n\n\n\n>     * add functions to test for induced as well as non-induced subgraphs, as it is the same.. Also works with DiGraphs, by the way !\n\nAgain, I went the same route in my reviewer patch.\n\n\n\n\nSeems like you anticipated my changes. Anyway, I'll have a careful look at your updated patch.",
    "created_at": "2010-05-26T00:05:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8922#issuecomment-82191",
    "user": "mvngu"
}
```

Replying to [comment:3 ncohen]:
>     * it took me some time, but I tested the new graph classes StaticDenseGraph this patch introduced against the already implemented DenseGraph.... Which turned out to be more efficient.. So this new class has disappeared, and the new code is now written into the usual Sage files instead of new ones

I have been reviewing your previous patch for over two days and went the same route as you have done in your current patch. That is, I rewrote your StaticDenseGraph to use the C graph based DenseGraph class, as it is very efficient in terms of storage. The reason why I have not uploaded my reviewer patch is that I was thinking about and playing with how to make the method `adjacency_list` more efficient in terms of storage. An array of ints is wasteful for the intended purpose, when a bitset is more suited to the purpose. What has been bugging me is trying to get my bitset implementation of `adjacency_list` to compile and work.




>     * a -- very nasty -- memory leak -- now fixed

Again, I went the same route in my reviewer patch.





>     * add functions to test for induced as well as non-induced subgraphs, as it is the same.. Also works with DiGraphs, by the way !

Again, I went the same route in my reviewer patch.




Seems like you anticipated my changes. Anyway, I'll have a careful look at your updated patch.



---

archive/issue_comments_082192.json:
```json
{
    "body": "Hello !!\n\nWell, first thank you for your work on this patch... I know it's a bit heavy all at once, and I hope the comments were clear enough :-)\n\nAbout the ``adjacency_list`` method : I was more worried about speed than storage, but anyway DenseGraph were faster than my matrix of integers..  Don't you think working on integers as it is done inside of DenseGraph could be more efficient than it currently is ? I have never used operations such as << and >> as it is done in DenseGraph, but I thought it would be the next step if one wanted to improve the speed for a bit. I'll trust you on this one !\n\nI also took some notes for future improvements... For example several tricks to reduce the number of attempts, or the initial graph, but I intended to wait for this patch to be merged before adding them. It will be easier to read in another one anyway :-)\n\nThank you again\n\nNathann",
    "created_at": "2010-05-26T04:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8922#issuecomment-82192",
    "user": "ncohen"
}
```

Hello !!

Well, first thank you for your work on this patch... I know it's a bit heavy all at once, and I hope the comments were clear enough :-)

About the ``adjacency_list`` method : I was more worried about speed than storage, but anyway DenseGraph were faster than my matrix of integers..  Don't you think working on integers as it is done inside of DenseGraph could be more efficient than it currently is ? I have never used operations such as << and >> as it is done in DenseGraph, but I thought it would be the next step if one wanted to improve the speed for a bit. I'll trust you on this one !

I also took some notes for future improvements... For example several tricks to reduce the number of attempts, or the initial graph, but I intended to wait for this patch to be merged before adding them. It will be easier to read in another one anyway :-)

Thank you again

Nathann



---

archive/issue_comments_082193.json:
```json
{
    "body": "I applied patches in the order suggested in the ticket description. Running doctests on the whole graph theory module resulted in these failures. This failure results from ncohen's updated patch, which does not update the doctests:\n\n```\nsage -t -long \"devel/sage-main/sage/graphs/generic_graph_pyx.pyx\"\n**********************************************************************\nFile \"/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/devel/sage-main/sage/graphs/generic_graph_pyx.pyx\", line 491:\n    sage: from sage.graphs.induced_subgraphs.induced_subgraphs import find_induced\nException raised:\n    Traceback (most recent call last):\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_10[2]>\", line 1, in <module>\n        from sage.graphs.induced_subgraphs.induced_subgraphs import find_induced###line 491:\n    sage: from sage.graphs.induced_subgraphs.induced_subgraphs import find_induced\n    ImportError: No module named induced_subgraphs.induced_subgraphs\n**********************************************************************\nFile \"/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/devel/sage-main/sage/graphs/generic_graph_pyx.pyx\", line 492:\n    sage: find_induced(graphs.PetersenGraph(), graphs.PathGraph(5))\nException raised:\n    Traceback (most recent call last):\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_10[3]>\", line 1, in <module>\n        find_induced(graphs.PetersenGraph(), graphs.PathGraph(Integer(5)))###line 492:\n    sage: find_induced(graphs.PetersenGraph(), graphs.PathGraph(5))\n    NameError: name 'find_induced' is not defined\n**********************************************************************\nFile \"/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/devel/sage-main/sage/graphs/generic_graph_pyx.pyx\", line 497:\n    sage: find_induced(graphs.PetersenGraph(), graphs.ClawGraph())\nException raised:\n    Traceback (most recent call last):\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_10[4]>\", line 1, in <module>\n        find_induced(graphs.PetersenGraph(), graphs.ClawGraph())###line 497:\n    sage: find_induced(graphs.PetersenGraph(), graphs.ClawGraph())\n    NameError: name 'find_induced' is not defined\n**********************************************************************\nFile \"/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/devel/sage-main/sage/graphs/generic_graph_pyx.pyx\", line 502:\n    sage: find_induced(graphs.PetersenGraph(), graphs.PathGraph(6))\nException raised:\n    Traceback (most recent call last):\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_10[5]>\", line 1, in <module>\n        find_induced(graphs.PetersenGraph(), graphs.PathGraph(Integer(6)))###line 502:\n    sage: find_induced(graphs.PetersenGraph(), graphs.PathGraph(6))\n    NameError: name 'find_induced' is not defined\n```\n\n\nThis is a known failure:\n\n```\nsage -t -long \"devel/sage-main/sage/graphs/generic_graph.py\"\n**********************************************************************\nFile \"/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/devel/sage-main/sage/graphs/generic_graph.py\", line 10754:\n    sage: print G.graphviz_string(labels=\"latex\",edge_labels=True)\nExpected:\n    digraph {\n      node [shape=\"plaintext\"];\n      \"2/3\" [label=\" \", texlbl=\"$\\frac{2}{3}$\"];\n      \"1/3\" [label=\" \", texlbl=\"$\\frac{1}{3}$\"];\n      \"1/2\" [label=\" \", texlbl=\"$\\frac{1}{2}$\"];\n      \"1\" [label=\" \", texlbl=\"$1$\"];\n      \"1/4\" [label=\" \", texlbl=\"$\\frac{1}{4}$\"];\n      \"4/5\" [label=\" \", texlbl=\"$\\frac{4}{5}$\"];\n      \"-4\" [label=\" \", texlbl=\"$-4$\"];\n      \"2\" [label=\" \", texlbl=\"$2$\"];\n      \"-2\" [label=\" \", texlbl=\"$-2$\"];\n      \"-1/2\" [label=\" \", texlbl=\"$-\\frac{1}{2}$\"];\n      \"-1\" [label=\" \", texlbl=\"$-1$\"];\n    <BLANKLINE>\n      \"1/2\" -> \"-2\" [label=\" \", texlbl=\"$x \\ {\\mapsto}\\ \\frac{-1}{x}$\"];\n      \"1/2\" -> \"2/3\" [label=\" \", texlbl=\"$x \\ {\\mapsto}\\ \\frac{1}{x + 1}$\"];\n      \"1\" -> \"-1\" [label=\" \", texlbl=\"$x \\ {\\mapsto}\\ \\frac{-1}{x}$\"];\n      \"1\" -> \"1/2\" [label=\" \", texlbl=\"$x \\ {\\mapsto}\\ \\frac{1}{x + 1}$\"];\n      \"1/4\" -> \"-4\" [label=\" \", texlbl=\"$x \\ {\\mapsto}\\ \\frac{-1}{x}$\"];\n      \"1/4\" -> \"4/5\" [label=\" \", texlbl=\"$x \\ {\\mapsto}\\ \\frac{1}{x + 1}$\"];\n      \"2\" -> \"-1/2\" [label=\" \", texlbl=\"$x \\ {\\mapsto}\\ \\frac{-1}{x}$\"];\n      \"2\" -> \"1/3\" [label=\" \", texlbl=\"$x \\ {\\mapsto}\\ \\frac{1}{x + 1}$\"];\n    }\nGot:\n    digraph {\n      node [shape=\"plaintext\"];\n      \"2/3\" [label=\" \", texlbl=\"$\\frac{2}{3}$\"];\n      \"1/3\" [label=\" \", texlbl=\"$\\frac{1}{3}$\"];\n      \"1/2\" [label=\" \", texlbl=\"$\\frac{1}{2}$\"];\n      \"1\" [label=\" \", texlbl=\"$1$\"];\n      \"1/4\" [label=\" \", texlbl=\"$\\frac{1}{4}$\"];\n      \"4/5\" [label=\" \", texlbl=\"$\\frac{4}{5}$\"];\n      \"-4\" [label=\" \", texlbl=\"$-4$\"];\n      \"2\" [label=\" \", texlbl=\"$2$\"];\n      \"-2\" [label=\" \", texlbl=\"$-2$\"];\n      \"-1/2\" [label=\" \", texlbl=\"$-\\frac{1}{2}$\"];\n      \"-1\" [label=\" \", texlbl=\"$-1$\"];\n    <BLANKLINE>\n      \"1/2\" -> \"-2\" [label=\" \", texlbl=\"$x \\ {\\mapsto}\\ \\frac{1}{x}$\"];\n      \"1/2\" -> \"2/3\" [label=\" \", texlbl=\"$x \\ {\\mapsto}\\ \\frac{1}{x + 1}$\"];\n      \"1\" -> \"-1\" [label=\" \", texlbl=\"$x \\ {\\mapsto}\\ \\frac{1}{x}$\"];\n      \"1\" -> \"1/2\" [label=\" \", texlbl=\"$x \\ {\\mapsto}\\ \\frac{1}{x + 1}$\"];\n      \"1/4\" -> \"-4\" [label=\" \", texlbl=\"$x \\ {\\mapsto}\\ \\frac{1}{x}$\"];\n      \"1/4\" -> \"4/5\" [label=\" \", texlbl=\"$x \\ {\\mapsto}\\ \\frac{1}{x + 1}$\"];\n      \"2\" -> \"-1/2\" [label=\" \", texlbl=\"$x \\ {\\mapsto}\\ \\frac{1}{x}$\"];\n      \"2\" -> \"1/3\" [label=\" \", texlbl=\"$x \\ {\\mapsto}\\ \\frac{1}{x + 1}$\"];\n    }\n```\n\n\nThis one should be optional, I think, and results from #8166:\n\n```\nFile \"/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/devel/sage-main/sage/graphs/generic_graph.py\", line 4213:\n    sage: g.matching(algorithm=\"LP\", value_only=True)\nException raised:\n    Traceback (most recent call last):\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_70[5]>\", line 1, in <module>\n        g.matching(algorithm=\"LP\", value_only=True)###line 4213:\n    sage: g.matching(algorithm=\"LP\", value_only=True)\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/lib/python/site-packages/sage/graphs/generic_graph.py\", line 4264, in matching\n        return p.solve(objective_only=True, solver=solver, log=verbose)\n      File \"mip.pyx\", line 1051, in sage.numerical.mip.MixedIntegerLinearProgram.solve (sage/numerical/mip.c:7884)\n    ValueError: There does not seem to be any (Mixed) Integer Linear Program solver installed. Please visit http://www.sagemath.org/doc/constructions/linear_programming.html to learn more about the solvers available.\n```\n",
    "created_at": "2010-06-01T18:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8922#issuecomment-82193",
    "user": "mvngu"
}
```

I applied patches in the order suggested in the ticket description. Running doctests on the whole graph theory module resulted in these failures. This failure results from ncohen's updated patch, which does not update the doctests:

```
sage -t -long "devel/sage-main/sage/graphs/generic_graph_pyx.pyx"
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/devel/sage-main/sage/graphs/generic_graph_pyx.pyx", line 491:
    sage: from sage.graphs.induced_subgraphs.induced_subgraphs import find_induced
Exception raised:
    Traceback (most recent call last):
      File "/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[2]>", line 1, in <module>
        from sage.graphs.induced_subgraphs.induced_subgraphs import find_induced###line 491:
    sage: from sage.graphs.induced_subgraphs.induced_subgraphs import find_induced
    ImportError: No module named induced_subgraphs.induced_subgraphs
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/devel/sage-main/sage/graphs/generic_graph_pyx.pyx", line 492:
    sage: find_induced(graphs.PetersenGraph(), graphs.PathGraph(5))
Exception raised:
    Traceback (most recent call last):
      File "/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[3]>", line 1, in <module>
        find_induced(graphs.PetersenGraph(), graphs.PathGraph(Integer(5)))###line 492:
    sage: find_induced(graphs.PetersenGraph(), graphs.PathGraph(5))
    NameError: name 'find_induced' is not defined
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/devel/sage-main/sage/graphs/generic_graph_pyx.pyx", line 497:
    sage: find_induced(graphs.PetersenGraph(), graphs.ClawGraph())
Exception raised:
    Traceback (most recent call last):
      File "/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[4]>", line 1, in <module>
        find_induced(graphs.PetersenGraph(), graphs.ClawGraph())###line 497:
    sage: find_induced(graphs.PetersenGraph(), graphs.ClawGraph())
    NameError: name 'find_induced' is not defined
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/devel/sage-main/sage/graphs/generic_graph_pyx.pyx", line 502:
    sage: find_induced(graphs.PetersenGraph(), graphs.PathGraph(6))
Exception raised:
    Traceback (most recent call last):
      File "/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[5]>", line 1, in <module>
        find_induced(graphs.PetersenGraph(), graphs.PathGraph(Integer(6)))###line 502:
    sage: find_induced(graphs.PetersenGraph(), graphs.PathGraph(6))
    NameError: name 'find_induced' is not defined
```


This is a known failure:

```
sage -t -long "devel/sage-main/sage/graphs/generic_graph.py"
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/devel/sage-main/sage/graphs/generic_graph.py", line 10754:
    sage: print G.graphviz_string(labels="latex",edge_labels=True)
Expected:
    digraph {
      node [shape="plaintext"];
      "2/3" [label=" ", texlbl="$\frac{2}{3}$"];
      "1/3" [label=" ", texlbl="$\frac{1}{3}$"];
      "1/2" [label=" ", texlbl="$\frac{1}{2}$"];
      "1" [label=" ", texlbl="$1$"];
      "1/4" [label=" ", texlbl="$\frac{1}{4}$"];
      "4/5" [label=" ", texlbl="$\frac{4}{5}$"];
      "-4" [label=" ", texlbl="$-4$"];
      "2" [label=" ", texlbl="$2$"];
      "-2" [label=" ", texlbl="$-2$"];
      "-1/2" [label=" ", texlbl="$-\frac{1}{2}$"];
      "-1" [label=" ", texlbl="$-1$"];
    <BLANKLINE>
      "1/2" -> "-2" [label=" ", texlbl="$x \ {\mapsto}\ \frac{-1}{x}$"];
      "1/2" -> "2/3" [label=" ", texlbl="$x \ {\mapsto}\ \frac{1}{x + 1}$"];
      "1" -> "-1" [label=" ", texlbl="$x \ {\mapsto}\ \frac{-1}{x}$"];
      "1" -> "1/2" [label=" ", texlbl="$x \ {\mapsto}\ \frac{1}{x + 1}$"];
      "1/4" -> "-4" [label=" ", texlbl="$x \ {\mapsto}\ \frac{-1}{x}$"];
      "1/4" -> "4/5" [label=" ", texlbl="$x \ {\mapsto}\ \frac{1}{x + 1}$"];
      "2" -> "-1/2" [label=" ", texlbl="$x \ {\mapsto}\ \frac{-1}{x}$"];
      "2" -> "1/3" [label=" ", texlbl="$x \ {\mapsto}\ \frac{1}{x + 1}$"];
    }
Got:
    digraph {
      node [shape="plaintext"];
      "2/3" [label=" ", texlbl="$\frac{2}{3}$"];
      "1/3" [label=" ", texlbl="$\frac{1}{3}$"];
      "1/2" [label=" ", texlbl="$\frac{1}{2}$"];
      "1" [label=" ", texlbl="$1$"];
      "1/4" [label=" ", texlbl="$\frac{1}{4}$"];
      "4/5" [label=" ", texlbl="$\frac{4}{5}$"];
      "-4" [label=" ", texlbl="$-4$"];
      "2" [label=" ", texlbl="$2$"];
      "-2" [label=" ", texlbl="$-2$"];
      "-1/2" [label=" ", texlbl="$-\frac{1}{2}$"];
      "-1" [label=" ", texlbl="$-1$"];
    <BLANKLINE>
      "1/2" -> "-2" [label=" ", texlbl="$x \ {\mapsto}\ \frac{1}{x}$"];
      "1/2" -> "2/3" [label=" ", texlbl="$x \ {\mapsto}\ \frac{1}{x + 1}$"];
      "1" -> "-1" [label=" ", texlbl="$x \ {\mapsto}\ \frac{1}{x}$"];
      "1" -> "1/2" [label=" ", texlbl="$x \ {\mapsto}\ \frac{1}{x + 1}$"];
      "1/4" -> "-4" [label=" ", texlbl="$x \ {\mapsto}\ \frac{1}{x}$"];
      "1/4" -> "4/5" [label=" ", texlbl="$x \ {\mapsto}\ \frac{1}{x + 1}$"];
      "2" -> "-1/2" [label=" ", texlbl="$x \ {\mapsto}\ \frac{1}{x}$"];
      "2" -> "1/3" [label=" ", texlbl="$x \ {\mapsto}\ \frac{1}{x + 1}$"];
    }
```


This one should be optional, I think, and results from #8166:

```
File "/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/devel/sage-main/sage/graphs/generic_graph.py", line 4213:
    sage: g.matching(algorithm="LP", value_only=True)
Exception raised:
    Traceback (most recent call last):
      File "/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_70[5]>", line 1, in <module>
        g.matching(algorithm="LP", value_only=True)###line 4213:
    sage: g.matching(algorithm="LP", value_only=True)
      File "/dev/shm/mvngu/sandbox/sage-4.4.3.alpha0.sandbox0/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 4264, in matching
        return p.solve(objective_only=True, solver=solver, log=verbose)
      File "mip.pyx", line 1051, in sage.numerical.mip.MixedIntegerLinearProgram.solve (sage/numerical/mip.c:7884)
    ValueError: There does not seem to be any (Mixed) Integer Linear Program solver installed. Please visit http://www.sagemath.org/doc/constructions/linear_programming.html to learn more about the solvers available.
```




---

archive/issue_comments_082194.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-01T18:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8922#issuecomment-82194",
    "user": "mvngu"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082195.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-01T19:11:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8922#issuecomment-82195",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082196.json:
```json
{
    "body": "Sorry for that Minh :-/\n\nHere is an updated patch... God, I'm eager to have all these dependencies merged into Sage !\n\nNathann",
    "created_at": "2010-06-01T19:11:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8922#issuecomment-82196",
    "user": "ncohen"
}
```

Sorry for that Minh :-/

Here is an updated patch... God, I'm eager to have all these dependencies merged into Sage !

Nathann



---

archive/issue_comments_082197.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-06-01T19:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8922#issuecomment-82197",
    "user": "ncohen"
}
```

Attachment



---

archive/issue_comments_082198.json:
```json
{
    "body": "It looks like everything in the dependencies except this patch is now reviewed.  Minh, are you reviewing this patch as well?",
    "created_at": "2010-06-04T21:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8922#issuecomment-82198",
    "user": "jason"
}
```

It looks like everything in the dependencies except this patch is now reviewed.  Minh, are you reviewing this patch as well?



---

archive/issue_comments_082199.json:
```json
{
    "body": "Replying to [comment:9 jason]:\n> Minh, are you reviewing this patch as well?\n\nYes. I'm finalizing a reviewer patch.",
    "created_at": "2010-06-04T21:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8922#issuecomment-82199",
    "user": "mvngu"
}
```

Replying to [comment:9 jason]:
> Minh, are you reviewing this patch as well?

Yes. I'm finalizing a reviewer patch.



---

archive/issue_comments_082200.json:
```json
{
    "body": "Attachment\n\nChanges in reviewer patch:\n\n* Move the method `adjacency_sequence()` to the class `CGraph`, as I think that method is useful for both dense and sparse graphs.\n* Clean-up coding style in accordance with PEP 008.\n* In describing the algorithm used in `subgraph_search()` of the module `generic_graph_pyx.pyx`, you have the formula:\n {{{\n`\\binom k!{|V(G)|}{k}`\n }}}\n That won't typeset in LaTeX as you expected. Do you mean this?\n {{{\n`k! \\binom{|V(G)|}{k}`\n }}}\n I have used the latter formula in my reviewer patch. Please correct me if I'm wrong.\n* Unit tests for the `cdef` functions `vectors_equal()` and `vectors_inferior()`, and the method `adjacency_sequence()`. These functions/methods are defined using `cdef` and the doctest coverage script don't pick them up in its analysis. However, I still think it's important to provide unit tests for such functions/methods.\n* Amalgamate the methods `induced_subgraph_search()` and `subgraph_search()`. Their definitions are almost identical, except for the keyword `induced`. The combined method is defined to take the boolean keyword `induced` and pass it on to the relevant method.\n\nAnother pair of eyes is needed to look over my reviewer patch.",
    "created_at": "2010-06-05T01:16:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8922#issuecomment-82200",
    "user": "mvngu"
}
```

Attachment

Changes in reviewer patch:

* Move the method `adjacency_sequence()` to the class `CGraph`, as I think that method is useful for both dense and sparse graphs.
* Clean-up coding style in accordance with PEP 008.
* In describing the algorithm used in `subgraph_search()` of the module `generic_graph_pyx.pyx`, you have the formula:
 {{{
`\binom k!{|V(G)|}{k}`
 }}}
 That won't typeset in LaTeX as you expected. Do you mean this?
 {{{
`k! \binom{|V(G)|}{k}`
 }}}
 I have used the latter formula in my reviewer patch. Please correct me if I'm wrong.
* Unit tests for the `cdef` functions `vectors_equal()` and `vectors_inferior()`, and the method `adjacency_sequence()`. These functions/methods are defined using `cdef` and the doctest coverage script don't pick them up in its analysis. However, I still think it's important to provide unit tests for such functions/methods.
* Amalgamate the methods `induced_subgraph_search()` and `subgraph_search()`. Their definitions are almost identical, except for the keyword `induced`. The combined method is defined to take the boolean keyword `induced` and pass it on to the relevant method.

Another pair of eyes is needed to look over my reviewer patch.



---

archive/issue_comments_082201.json:
```json
{
    "body": "Wow, your reviewer patch is twice the size of the original patch!",
    "created_at": "2010-06-05T02:16:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8922#issuecomment-82201",
    "user": "jason"
}
```

Wow, your reviewer patch is twice the size of the original patch!



---

archive/issue_comments_082202.json:
```json
{
    "body": "Hello !!\n\nFirst, I want to thank you for the amount of time your must have spent on this :-)\n\n>  * Move the method `adjacency_sequence()` to the class `CGraph`, as I think that method is useful for both dense and sparse graphs.\n\nIt can be, though systematically testing adjacencies (and most importantly -- non-adjacencies) in sparse graph can be a problem... Perhaps we will have to split this function in two copies, one for each class, one day or another. I have been talking with Alexandre Blondin Masse who could need such a feature for Sparse graphs :-)\n\n>  * In describing the algorithm used in `subgraph_search()` of the module `generic_graph_pyx.pyx`, you have the formula:\n>  {{{\n> `\\binom k!{|V(G)|}{k}`\n>  }}}\n>  That won't typeset in LaTeX as you expected. Do you mean this?\n>  {{{\n> `k! \\binom{|V(G)|}{k}`\n>  }}}\n\nIndeed\n\n>  I have used the latter formula in my reviewer patch. Please correct me if I'm wrong.\n\nYou almost never are :-)\n\n>  * Unit tests for the `cdef` functions `vectors_equal()` and `vectors_inferior()`, and the method `adjacency_sequence()`. These functions/methods are defined using `cdef` and the doctest coverage script don't pick them up in its analysis. However, I still think it's important to provide unit tests for such functions/methods.\n\nWell, if there is anything wrong in these functions your tests will show it, though given their length I wouldn't have thought necessary to add such tests.... Are you doubting Cython itself ? :-)\n\n>  * Amalgamate the methods `induced_subgraph_search()` and `subgraph_search()`. Their definitions are almost identical, except for the keyword `induced`. The combined method is defined to take the boolean keyword `induced` and pass it on to the relevant method.\n\nI was thinking of someone working on induced subgraphs, and not seeing any occurence of this word among the functions.... But he will get interested in subgraph search sooner or later ;-)\n\n> Another pair of eyes is needed to look over my reviewer patch.\n\nI already spent some time over it, and agreed with what I saw.... Considering its length, I may do this once or twice again before setting it to \"positive review\". and... Thank you again :-)\n\nNathann",
    "created_at": "2010-06-05T09:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8922#issuecomment-82202",
    "user": "ncohen"
}
```

Hello !!

First, I want to thank you for the amount of time your must have spent on this :-)

>  * Move the method `adjacency_sequence()` to the class `CGraph`, as I think that method is useful for both dense and sparse graphs.

It can be, though systematically testing adjacencies (and most importantly -- non-adjacencies) in sparse graph can be a problem... Perhaps we will have to split this function in two copies, one for each class, one day or another. I have been talking with Alexandre Blondin Masse who could need such a feature for Sparse graphs :-)

>  * In describing the algorithm used in `subgraph_search()` of the module `generic_graph_pyx.pyx`, you have the formula:
>  {{{
> `\binom k!{|V(G)|}{k}`
>  }}}
>  That won't typeset in LaTeX as you expected. Do you mean this?
>  {{{
> `k! \binom{|V(G)|}{k}`
>  }}}

Indeed

>  I have used the latter formula in my reviewer patch. Please correct me if I'm wrong.

You almost never are :-)

>  * Unit tests for the `cdef` functions `vectors_equal()` and `vectors_inferior()`, and the method `adjacency_sequence()`. These functions/methods are defined using `cdef` and the doctest coverage script don't pick them up in its analysis. However, I still think it's important to provide unit tests for such functions/methods.

Well, if there is anything wrong in these functions your tests will show it, though given their length I wouldn't have thought necessary to add such tests.... Are you doubting Cython itself ? :-)

>  * Amalgamate the methods `induced_subgraph_search()` and `subgraph_search()`. Their definitions are almost identical, except for the keyword `induced`. The combined method is defined to take the boolean keyword `induced` and pass it on to the relevant method.

I was thinking of someone working on induced subgraphs, and not seeing any occurence of this word among the functions.... But he will get interested in subgraph search sooner or later ;-)

> Another pair of eyes is needed to look over my reviewer patch.

I already spent some time over it, and agreed with what I saw.... Considering its length, I may do this once or twice again before setting it to "positive review". and... Thank you again :-)

Nathann



---

archive/issue_comments_082203.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-05T10:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8922#issuecomment-82203",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082204.json:
```json
{
    "body": "Agreeeeeeed !! I expect this function to receive a lot of improvements in future patches :-)\n\nNathann",
    "created_at": "2010-06-05T10:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8922#issuecomment-82204",
    "user": "ncohen"
}
```

Agreeeeeeed !! I expect this function to receive a lot of improvements in future patches :-)

Nathann



---

archive/issue_comments_082205.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T07:14:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8922#issuecomment-82205",
    "user": "mhansen"
}
```

Resolution: fixed
