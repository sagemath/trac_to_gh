# Issue 8781: Overfull graph (and a bug in edge_coloring)

archive/issues_008781.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nThis patch defines the (very short) function is_overfull (http://en.wikipedia.org/wiki/Overfull_graph), and updates the edge_coloring function to support it. \n\nI also fixed a mistake in this code : I had mixed g.order() with max(g.degree()) for complete graphs ^^;\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/8781\n\n",
    "created_at": "2010-04-27T12:11:34Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "Overfull graph (and a bug in edge_coloring)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8781",
    "user": "ncohen"
}
```
Assignee: jason, ncohen, rlm

This patch defines the (very short) function is_overfull (http://en.wikipedia.org/wiki/Overfull_graph), and updates the edge_coloring function to support it. 

I also fixed a mistake in this code : I had mixed g.order() with max(g.degree()) for complete graphs ^^;

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/8781





---

archive/issue_comments_080374.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-04-27T12:15:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8781#issuecomment-80374",
    "user": "ncohen"
}
```

Attachment



---

archive/issue_comments_080375.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-27T12:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8781#issuecomment-80375",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080376.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-05-10T07:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8781#issuecomment-80376",
    "user": "mvngu"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_080377.json:
```json
{
    "body": "For the patch [trac_8781.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8781/trac_8781.patch), I'm OK with the part dealing with defining the new method `is_overfull()`. I have attached reviewer patch that adds some more doctests to that method, fixes some formatting styles, and adds a comment about optimizing that method for speed. \n\n\n\nNow to the part I don't like about [trac_8781.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8781/trac_8781.patch). It's the part of that patch that deals with the module `sage/graphs/graph_coloring.py`. While testing that part of ncohen's patch, I came across this failure:\n\n\n```sh\nsage: from sage.graphs.graph_coloring import edge_coloring\nsage: g = graphs.ClawGraph()\nsage: edge_coloring(g, value_only=True)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-8781-overfull/<ipython console> in <module>()\n\n/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-8781-overfull/local/lib/python2.6/site-packages/sage/graphs/graph_coloring.pyc in edge_coloring(g, value_only, vizing, hex_colors, log)\n    564             sum([color[R(e)][i] for e in g.edges_incident(v)]), max=1)\n    565                 for v in g.vertex_iterator()\n--> 566                     for i in xrange(k)]\n    567     # an edge must have a color\n\n    568     [p.add_constraint(sum([color[R(e)][i] for i in xrange(k)]), max=1, min=1)\n\n/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-8781-overfull/local/lib/python2.6/site-packages/sage/numerical/mip.so in sage.numerical.mip.MIPVariable.__getitem__ (sage/numerical/mip.c:9202)()\n\nTypeError: unhashable type: 'dict'\n```\n\n\nThis also came up even though I had installed the optional GLPK spkg. One possibility here is to split off the part of the patch that deals with edge coloring and put that part in another ticket. That ticket could also be about resolving the failure I reported above. Other possibility is to resolve the above failure in the current ticket.",
    "created_at": "2010-05-10T07:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8781#issuecomment-80377",
    "user": "mvngu"
}
```

For the patch [trac_8781.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8781/trac_8781.patch), I'm OK with the part dealing with defining the new method `is_overfull()`. I have attached reviewer patch that adds some more doctests to that method, fixes some formatting styles, and adds a comment about optimizing that method for speed. 



Now to the part I don't like about [trac_8781.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8781/trac_8781.patch). It's the part of that patch that deals with the module `sage/graphs/graph_coloring.py`. While testing that part of ncohen's patch, I came across this failure:


```sh
sage: from sage.graphs.graph_coloring import edge_coloring
sage: g = graphs.ClawGraph()
sage: edge_coloring(g, value_only=True)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-8781-overfull/<ipython console> in <module>()

/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-8781-overfull/local/lib/python2.6/site-packages/sage/graphs/graph_coloring.pyc in edge_coloring(g, value_only, vizing, hex_colors, log)
    564             sum([color[R(e)][i] for e in g.edges_incident(v)]), max=1)
    565                 for v in g.vertex_iterator()
--> 566                     for i in xrange(k)]
    567     # an edge must have a color

    568     [p.add_constraint(sum([color[R(e)][i] for i in xrange(k)]), max=1, min=1)

/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-8781-overfull/local/lib/python2.6/site-packages/sage/numerical/mip.so in sage.numerical.mip.MIPVariable.__getitem__ (sage/numerical/mip.c:9202)()

TypeError: unhashable type: 'dict'
```


This also came up even though I had installed the optional GLPK spkg. One possibility here is to split off the part of the patch that deals with edge coloring and put that part in another ticket. That ticket could also be about resolving the failure I reported above. Other possibility is to resolve the above failure in the current ticket.



---

archive/issue_comments_080378.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-05-10T17:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8781#issuecomment-80378",
    "user": "ncohen"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_080379.json:
```json
{
    "body": "Oops.... That's totally unrelated, and is caused by the recent upgrade of NetworkX. The default graphs from NetworkX (of which ClawGraph() is an example) now have {} instead of None as default edge labels... And as {} is not hashable, Sage does not like to find it as part of a dictionary key ;-)\n\nThere was already a patch waiting for review to fix it, which is #8892, but I had forgotten this file and only fixed generic_graph and graph... Well, I updated that patch, which is now a dependency of this very one, and fixes the bug you found.\n\nThank you very much Minh, and sorry again for that :-)\n\nNathann",
    "created_at": "2010-05-10T17:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8781#issuecomment-80379",
    "user": "ncohen"
}
```

Oops.... That's totally unrelated, and is caused by the recent upgrade of NetworkX. The default graphs from NetworkX (of which ClawGraph() is an example) now have {} instead of None as default edge labels... And as {} is not hashable, Sage does not like to find it as part of a dictionary key ;-)

There was already a patch waiting for review to fix it, which is #8892, but I had forgotten this file and only fixed generic_graph and graph... Well, I updated that patch, which is now a dependency of this very one, and fixes the bug you found.

Thank you very much Minh, and sorry again for that :-)

Nathann



---

archive/issue_comments_080380.json:
```json
{
    "body": "Replying to [comment:3 ncohen]:\n> There was already a patch waiting for review to fix it, which is #8892, but I had forgotten this file and only fixed generic_graph and graph...\n\nI have updated my reviewer patch to include the doctest that resulted in the failure I reported above. We better make sure it doesn't happen again. Anyone for a final review of the whole ticket?",
    "created_at": "2010-05-21T16:54:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8781#issuecomment-80380",
    "user": "mvngu"
}
```

Replying to [comment:3 ncohen]:
> There was already a patch waiting for review to fix it, which is #8892, but I had forgotten this file and only fixed generic_graph and graph...

I have updated my reviewer patch to include the doctest that resulted in the failure I reported above. We better make sure it doesn't happen again. Anyone for a final review of the whole ticket?



---

archive/issue_comments_080381.json:
```json
{
    "body": "It's ok for me !! I thought for a time it also needed to be rebased, but I has just forgotten to apply my patch before yours ;-)\n\nI noticed an error in the docstrings though... so positive review to your patch, and this ticket is still waiting for review because of mine.\n\nand by the way... It's a bit odd that I did not notice this problem before, and I'm afraid tis may come from the fact I used CPLEX as a default solver before, while only GLPK is installed on my current copy of Sage O_o\n\nNathann",
    "created_at": "2010-05-24T17:45:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8781#issuecomment-80381",
    "user": "ncohen"
}
```

It's ok for me !! I thought for a time it also needed to be rebased, but I has just forgotten to apply my patch before yours ;-)

I noticed an error in the docstrings though... so positive review to your patch, and this ticket is still waiting for review because of mine.

and by the way... It's a bit odd that I did not notice this problem before, and I'm afraid tis may come from the fact I used CPLEX as a default solver before, while only GLPK is installed on my current copy of Sage O_o

Nathann



---

archive/issue_comments_080382.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-05-25T01:09:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8781#issuecomment-80382",
    "user": "mvngu"
}
```

Attachment



---

archive/issue_comments_080383.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:5 ncohen]:\n> I noticed an error in the docstrings though... so positive review to your patch, and this ticket is still waiting for review because of mine.\n\nYour fix is OK by me. However, note that it requires GLPK or CBC. (I have only tested with those two spkg's.) Without any of those packages installed, I got the following failure:\n\n```sh\nsage -t -long \"devel/sage-main/sage/graphs/generic_graph.py\"\n**********************************************************************\nFile \"/dev/shm/mvngu/sandbox/sage-4.4.2.sandbox.6/devel/sage-main/sage/graphs/generic_graph.py\", line 1845:\n    sage: edge_coloring(g, value_only=True)\nExpected:\n    3\nGot:\n    4\n**********************************************************************\nFile \"/dev/shm/mvngu/sandbox/sage-4.4.2.sandbox.6/devel/sage-main/sage/graphs/generic_graph.py\", line 4027:\n    sage: g.matching(algorithm=\"LP\", value_only=True)\nException raised:\n    Traceback (most recent call last):\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.2.sandbox.6/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.2.sandbox.6/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.2.sandbox.6/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_69[5]>\", line 1, in <module>\n        g.matching(algorithm=\"LP\", value_only=True)###line 4027:\n    sage: g.matching(algorithm=\"LP\", value_only=True)\n      File \"/dev/shm/mvngu/sandbox/sage-4.4.2.sandbox.6/local/lib/python/site-packages/sage/graphs/generic_graph.py\", line 4078, in matching\n        return p.solve(objective_only=True, solver=solver, log=verbose)\n      File \"mip.pyx\", line 1051, in sage.numerical.mip.MixedIntegerLinearProgram.solve (sage/numerical/mip.c:7884)\n    ValueError: There does not seem to be any (Mixed) Integer Linear Program solver installed. Please visit http://www.sagemath.org/doc/constructions/linear_programming.html to learn more about the solvers available.\n**********************************************************************\n```\n\nSo I have made the doctest optional. And as I said before: Anyone for a final review of the whole ticket? :-) See the ticket description for instructions on how to apply patches.",
    "created_at": "2010-05-25T01:14:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8781#issuecomment-80383",
    "user": "mvngu"
}
```

Attachment

Replying to [comment:5 ncohen]:
> I noticed an error in the docstrings though... so positive review to your patch, and this ticket is still waiting for review because of mine.

Your fix is OK by me. However, note that it requires GLPK or CBC. (I have only tested with those two spkg's.) Without any of those packages installed, I got the following failure:

```sh
sage -t -long "devel/sage-main/sage/graphs/generic_graph.py"
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.4.2.sandbox.6/devel/sage-main/sage/graphs/generic_graph.py", line 1845:
    sage: edge_coloring(g, value_only=True)
Expected:
    3
Got:
    4
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.4.2.sandbox.6/devel/sage-main/sage/graphs/generic_graph.py", line 4027:
    sage: g.matching(algorithm="LP", value_only=True)
Exception raised:
    Traceback (most recent call last):
      File "/dev/shm/mvngu/sandbox/sage-4.4.2.sandbox.6/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.2.sandbox.6/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.2.sandbox.6/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_69[5]>", line 1, in <module>
        g.matching(algorithm="LP", value_only=True)###line 4027:
    sage: g.matching(algorithm="LP", value_only=True)
      File "/dev/shm/mvngu/sandbox/sage-4.4.2.sandbox.6/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 4078, in matching
        return p.solve(objective_only=True, solver=solver, log=verbose)
      File "mip.pyx", line 1051, in sage.numerical.mip.MixedIntegerLinearProgram.solve (sage/numerical/mip.c:7884)
    ValueError: There does not seem to be any (Mixed) Integer Linear Program solver installed. Please visit http://www.sagemath.org/doc/constructions/linear_programming.html to learn more about the solvers available.
**********************************************************************
```

So I have made the doctest optional. And as I said before: Anyone for a final review of the whole ticket? :-) See the ticket description for instructions on how to apply patches.



---

archive/issue_comments_080384.json:
```json
{
    "body": "Hem... So in the end, with your \"optional\" keyword and the 3 instead of 4, there is no error returned from the doctests when no solver is installed. The problem is that when a user who does not have any solver installed uses the edge_coloring method, he gets wrong results because the function, when noticing that the solve command raises an exception (because no solver is installed) incorrectly deduces that the problem has no solution, and answers Delta+1. This is just because I wrote except: instead of except MIPSolverException:, and it is (I hope) my last mistake. :-)\n\nWith this other 1-line patch, this should be fixed.... God I'm eager to see all those dependencies merged into Sage, I'm getting tired of applying them all each time I want to test something !!\n\nNathann",
    "created_at": "2010-05-25T17:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8781#issuecomment-80384",
    "user": "ncohen"
}
```

Hem... So in the end, with your "optional" keyword and the 3 instead of 4, there is no error returned from the doctests when no solver is installed. The problem is that when a user who does not have any solver installed uses the edge_coloring method, he gets wrong results because the function, when noticing that the solve command raises an exception (because no solver is installed) incorrectly deduces that the problem has no solution, and answers Delta+1. This is just because I wrote except: instead of except MIPSolverException:, and it is (I hope) my last mistake. :-)

With this other 1-line patch, this should be fixed.... God I'm eager to see all those dependencies merged into Sage, I'm getting tired of applying them all each time I want to test something !!

Nathann



---

archive/issue_comments_080385.json:
```json
{
    "body": "Attachment\n\nI'm OK with `trac_8781.patch` and `trac_8781-fix2.patch`. We now need final approval for my reviewer patch `trac_8781-reviewer.patch`.",
    "created_at": "2010-06-12T08:10:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8781#issuecomment-80385",
    "user": "mvngu"
}
```

Attachment

I'm OK with `trac_8781.patch` and `trac_8781-fix2.patch`. We now need final approval for my reviewer patch `trac_8781-reviewer.patch`.



---

archive/issue_comments_080386.json:
```json
{
    "body": "Fine without any LP solver, fine with GLPK, fine with CPLEX :-)\n\nPositive review... But I noticed lots of failures because of the travelling_salesman_problem, still due to default {} labels... This function was under review when the patch fixing it was merged, so I'll create another one for this :-/\n\nNathann",
    "created_at": "2010-06-12T22:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8781#issuecomment-80386",
    "user": "ncohen"
}
```

Fine without any LP solver, fine with GLPK, fine with CPLEX :-)

Positive review... But I noticed lots of failures because of the travelling_salesman_problem, still due to default {} labels... This function was under review when the patch fixing it was merged, so I'll create another one for this :-/

Nathann



---

archive/issue_comments_080387.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-12T22:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8781#issuecomment-80387",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080388.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-29T16:44:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8781#issuecomment-80388",
    "user": "rlm"
}
```

Resolution: fixed
