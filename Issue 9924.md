# Issue 9924: Doctest error in sage/graphs/graph.py

archive/issues_009924.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @dimpase edward.scheinerman @jasongrout @kcrisman mvngu @nathanncohen\n\nI get this doctest error with a trial 4.6.alpha1 on sage.math and many other Sage cluster and Skynet machines:\n\n```python\nsage -t -long  devel/sage/sage/graphs/graph.py\n**********************************************************************\nFile \"/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/devel/sage-main/sage/graphs/graph.py\", line 1347:\n    sage: cycle.order() % 2 == 0\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[9]>\", line 1, in <module>\n        cycle.order() % Integer(2) == Integer(0)###line 1347:\n    sage: cycle.order() % 2 == 0\n    AttributeError: 'bool' object has no attribute 'order'\n**********************************************************************\nFile \"/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/devel/sage-main/sage/graphs/graph.py\", line 1349:\n    sage: cycle.is_isomorphic(graphs.CycleGraph(cycle.order()))\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[10]>\", line 1, in <module>\n        cycle.is_isomorphic(graphs.CycleGraph(cycle.order()))###line 1349:\n    sage: cycle.is_isomorphic(graphs.CycleGraph(cycle.order()))\n    AttributeError: 'bool' object has no attribute 'is_isomorphic'\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9925\n\n",
    "created_at": "2010-09-16T23:56:40Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Doctest error in sage/graphs/graph.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9924",
    "user": "@qed777"
}
```
Assignee: mvngu

CC:  @dimpase edward.scheinerman @jasongrout @kcrisman mvngu @nathanncohen

I get this doctest error with a trial 4.6.alpha1 on sage.math and many other Sage cluster and Skynet machines:

```python
sage -t -long  devel/sage/sage/graphs/graph.py
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/devel/sage-main/sage/graphs/graph.py", line 1347:
    sage: cycle.order() % 2 == 0
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[9]>", line 1, in <module>
        cycle.order() % Integer(2) == Integer(0)###line 1347:
    sage: cycle.order() % 2 == 0
    AttributeError: 'bool' object has no attribute 'order'
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/devel/sage-main/sage/graphs/graph.py", line 1349:
    sage: cycle.is_isomorphic(graphs.CycleGraph(cycle.order()))
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[10]>", line 1, in <module>
        cycle.is_isomorphic(graphs.CycleGraph(cycle.order()))###line 1349:
    sage: cycle.is_isomorphic(graphs.CycleGraph(cycle.order()))
    AttributeError: 'bool' object has no attribute 'is_isomorphic'
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/9925





---

archive/issue_comments_098798.json:
```json
{
    "body": "If it's feasible to create a patch now, I can merge it into 4.6.alpha1, while I wait for a response to a build error at #4000. \n\nEdward, could you add yourself to the [account name-real name map](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames)?",
    "created_at": "2010-09-16T23:58:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98798",
    "user": "@qed777"
}
```

If it's feasible to create a patch now, I can merge it into 4.6.alpha1, while I wait for a response to a build error at #4000. 

Edward, could you add yourself to the [account name-real name map](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames)?



---

archive/issue_comments_098799.json:
```json
{
    "body": "Is this repeatable?  I think I've seen this before, but it's always passed on the second try.",
    "created_at": "2010-09-17T00:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98799",
    "user": "@jhpalmieri"
}
```

Is this repeatable?  I think I've seen this before, but it's always passed on the second try.



---

archive/issue_comments_098800.json:
```json
{
    "body": "Oops.  You're right.  I confused this with a different error.  I got error above only on sage.math and cicero.skynet (x86-Linux-pentium4-fc) and it's not reproducible.\n\nI apologize for the noise.  Does anyone know why this test might be \"flaky\"?",
    "created_at": "2010-09-17T00:36:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98800",
    "user": "@qed777"
}
```

Oops.  You're right.  I confused this with a different error.  I got error above only on sage.math and cicero.skynet (x86-Linux-pentium4-fc) and it's not reproducible.

I apologize for the noise.  Does anyone know why this test might be "flaky"?



---

archive/issue_comments_098801.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2010-09-17T00:37:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98801",
    "user": "@qed777"
}
```

Resolution: worksforme



---

archive/issue_comments_098802.json:
```json
{
    "body": "Hmmm..... If ``cycle`` is a boolean, it means it is equal to True (the method called returns \"True\", or a certificate that it is not true otherwise -- a graph object). I have already seen this method to return wrong answers (and this is fixed in #9420), but the code *IS* deterministic and in this case I do not understand why you would not get an error at the previous docstring :\n\n\n```\n            sage: g.is_even_hole_free()      \n            True\n```\n\n\nwhich uses the same graph. Of course, this doctest is another one of the kind I'm trying to get rid off these days : it theoretically fails with a probability of 1/9999999999999999.... which means that it \"can happen\"... But once again, this would mean an error at the previous docstring too `O_o`\n\nif you are finding yourself on one of the machines on which you have seen it failing, could you give this a try ?\n\n\n```\n    sage: all( isinstance(graphs.RandomBipartite(10, 10, .5).is_even_hole_free(certificate = True), \"Graph\") for i in range(10000) )\n```\n\n\nNathann",
    "created_at": "2010-09-17T05:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98802",
    "user": "@nathanncohen"
}
```

Hmmm..... If ``cycle`` is a boolean, it means it is equal to True (the method called returns "True", or a certificate that it is not true otherwise -- a graph object). I have already seen this method to return wrong answers (and this is fixed in #9420), but the code *IS* deterministic and in this case I do not understand why you would not get an error at the previous docstring :


```
            sage: g.is_even_hole_free()      
            True
```


which uses the same graph. Of course, this doctest is another one of the kind I'm trying to get rid off these days : it theoretically fails with a probability of 1/9999999999999999.... which means that it "can happen"... But once again, this would mean an error at the previous docstring too `O_o`

if you are finding yourself on one of the machines on which you have seen it failing, could you give this a try ?


```
    sage: all( isinstance(graphs.RandomBipartite(10, 10, .5).is_even_hole_free(certificate = True), "Graph") for i in range(10000) )
```


Nathann



---

archive/issue_comments_098803.json:
```json
{
    "body": "Hmmm.... It looks like it's not --so-- rare O_o\n\n\n```\nsage: sum( not isinstance(graphs.RandomBipartite(10, 10, .5).is_even_hole_free(certificate = True), Graph) for i in range(10000) )\n96\n```\n\n\nsomething like 1%...`:-/`\n\nAnd with this :\n\n\n```\nsage: t = lambda x: Graph(x).is_forest() or isinstance(x.is_even_hole_free(certificate = True), Graph)\nsage: sum( not t(graphs.RandomBipartite(10, 10, .5)) for i in range(10000) )\n111\n```\n\n\nWhich means it comes from .... the bug in the method subgraph_search, and not from the theoretical probability `:-/`\n\nWith the patch applied :\n\n\n```\nsage: sage: t = lambda x: Graph(x).is_forest() or isinstance(x.is_even_hole_free(certificate = True), Graph)\nsage: sage: sum( not t(graphs.RandomBipartite(10, 10, .5)) for i in range(10000) )\n0\n```\n\n\nWhich **relieved** me. I should post a patch to add this is_forest condition anyway. Can I put it on this ticket ?\n\nNathann",
    "created_at": "2010-09-17T06:12:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98803",
    "user": "@nathanncohen"
}
```

Hmmm.... It looks like it's not --so-- rare O_o


```
sage: sum( not isinstance(graphs.RandomBipartite(10, 10, .5).is_even_hole_free(certificate = True), Graph) for i in range(10000) )
96
```


something like 1%...`:-/`

And with this :


```
sage: t = lambda x: Graph(x).is_forest() or isinstance(x.is_even_hole_free(certificate = True), Graph)
sage: sum( not t(graphs.RandomBipartite(10, 10, .5)) for i in range(10000) )
111
```


Which means it comes from .... the bug in the method subgraph_search, and not from the theoretical probability `:-/`

With the patch applied :


```
sage: sage: t = lambda x: Graph(x).is_forest() or isinstance(x.is_even_hole_free(certificate = True), Graph)
sage: sage: sum( not t(graphs.RandomBipartite(10, 10, .5)) for i in range(10000) )
0
```


Which **relieved** me. I should post a patch to add this is_forest condition anyway. Can I put it on this ticket ?

Nathann



---

archive/issue_comments_098804.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2010-09-17T06:19:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98804",
    "user": "@dimpase"
}
```

Changing status from closed to needs_work.



---

archive/issue_comments_098805.json:
```json
{
    "body": "go ahead, Nathann, add the patch...",
    "created_at": "2010-09-17T06:19:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98805",
    "user": "@dimpase"
}
```

go ahead, Nathann, add the patch...



---

archive/issue_comments_098806.json:
```json
{
    "body": "Nathann, could you also add a doctest that does *boom* to the unpatched code?",
    "created_at": "2010-09-17T06:21:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98806",
    "user": "@dimpase"
}
```

Nathann, could you also add a doctest that does *boom* to the unpatched code?



---

archive/issue_comments_098807.json:
```json
{
    "body": "I can do that, but this patch will require #9925 to be applied first... Here is the explanation : for the moment, the docstring works by generating a random bipartite graph, and looking for a cycle inside it. With a (very small) probability, this graph can be a forest, which means there is no cycle --> the doctest fails. This is not checked right now, and means that even though veeeery unlikely, it may fail because the generated graph is a forest. I can write a patch for this, and it will be available here in a second. The problem now, is that even if the graph is not a forest, a bug in subgraph_search may appear during the doctests (and does, with a probability of 1%). Even when the patch checking whether the graph is a forest will be applied, these errors will *STILL* appear until #9420 is applied.\n\nI will then add a patch right now to test for forests, just in case, and another patch based upon #9420, to check this never appears again :-)\n\nNathann",
    "created_at": "2010-09-17T07:48:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98807",
    "user": "@nathanncohen"
}
```

I can do that, but this patch will require #9925 to be applied first... Here is the explanation : for the moment, the docstring works by generating a random bipartite graph, and looking for a cycle inside it. With a (very small) probability, this graph can be a forest, which means there is no cycle --> the doctest fails. This is not checked right now, and means that even though veeeery unlikely, it may fail because the generated graph is a forest. I can write a patch for this, and it will be available here in a second. The problem now, is that even if the graph is not a forest, a bug in subgraph_search may appear during the doctests (and does, with a probability of 1%). Even when the patch checking whether the graph is a forest will be applied, these errors will *STILL* appear until #9420 is applied.

I will then add a patch right now to test for forests, just in case, and another patch based upon #9420, to check this never appears again :-)

Nathann



---

archive/issue_comments_098808.json:
```json
{
    "body": "Attachment [trac_9925.patch](tarball://root/attachments/some-uuid/ticket9925/trac_9925.patch) by @nathanncohen created at 2010-09-17 08:17:38\n\nThere is now one ticket to be reviewed here, and the patch Dima requested is also waiting for review at #9930 (though it depends on #9420 too)..\n\nSorry for all that !!! `^^;`\n\nNathann",
    "created_at": "2010-09-17T08:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98808",
    "user": "@nathanncohen"
}
```

Attachment [trac_9925.patch](tarball://root/attachments/some-uuid/ticket9925/trac_9925.patch) by @nathanncohen created at 2010-09-17 08:17:38

There is now one ticket to be reviewed here, and the patch Dima requested is also waiting for review at #9930 (though it depends on #9420 too)..

Sorry for all that !!! `^^;`

Nathann



---

archive/issue_comments_098809.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-17T08:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98809",
    "user": "@nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_098810.json:
```json
{
    "body": "Changing priority from blocker to major.",
    "created_at": "2010-09-19T06:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98810",
    "user": "@qed777"
}
```

Changing priority from blocker to major.



---

archive/issue_comments_098811.json:
```json
{
    "body": "I don't get how these lines in the doctest test anything.\n\n```\n... \n \t1354\t            sage: print \"Everything is Fine !\" \n \t1355\t            Everything is Fine ! \n```\n\nUnless I am mistaken, they only indicate that the coder was in a jolly good mood while writing them :-)",
    "created_at": "2010-09-19T08:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98811",
    "user": "@dimpase"
}
```

I don't get how these lines in the doctest test anything.

```
... 
 	1354	            sage: print "Everything is Fine !" 
 	1355	            Everything is Fine ! 
```

Unless I am mistaken, they only indicate that the coder was in a jolly good mood while writing them :-)



---

archive/issue_comments_098812.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-19T08:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98812",
    "user": "@dimpase"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_098813.json:
```json
{
    "body": "First, you are right, then it was also to avoid having a docstring returning nothing on success, and returning \"Error\" on failure... It is just meant to say \"this section has been run\", and check that it was not bypassed for some reason.. Do you prefer it without this part ?\n\nIf so, tell me and I update it.\n\nBut I consider it a very pertinent information that Sage developpers have fun writing docstring, and the user may like to know it `:-D`\n\nNathann",
    "created_at": "2010-09-19T08:34:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98813",
    "user": "@nathanncohen"
}
```

First, you are right, then it was also to avoid having a docstring returning nothing on success, and returning "Error" on failure... It is just meant to say "this section has been run", and check that it was not bypassed for some reason.. Do you prefer it without this part ?

If so, tell me and I update it.

But I consider it a very pertinent information that Sage developpers have fun writing docstring, and the user may like to know it `:-D`

Nathann



---

archive/issue_comments_098814.json:
```json
{
    "body": "Nathan, you do not *return* error, you just *print* \"Error\"!\nAll that print stuff gets lost when running \"sage -t\", imho...",
    "created_at": "2010-09-19T08:59:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98814",
    "user": "@dimpase"
}
```

Nathan, you do not *return* error, you just *print* "Error"!
All that print stuff gets lost when running "sage -t", imho...



---

archive/issue_comments_098815.json:
```json
{
    "body": "> Nathan, you do not *return* error, you just *print* \"Error\"!\n> All that print stuff gets lost when running \"sage -t\", imho...\n\nYes, but if the message \"Error\" is printed and the docstring doesn't expect it, an error will reported, won't it ? `O_o`\n\nIn case of failure, this piece of code will print :\n\nError !\nEverything is fine !\n\nWhile the code only expects to find \"Everything is fine !\".\n\nNathann",
    "created_at": "2010-09-19T09:03:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98815",
    "user": "@nathanncohen"
}
```

> Nathan, you do not *return* error, you just *print* "Error"!
> All that print stuff gets lost when running "sage -t", imho...

Yes, but if the message "Error" is printed and the docstring doesn't expect it, an error will reported, won't it ? `O_o`

In case of failure, this piece of code will print :

Error !
Everything is fine !

While the code only expects to find "Everything is fine !".

Nathann



---

archive/issue_comments_098816.json:
```json
{
    "body": "OK, my bad...",
    "created_at": "2010-09-19T09:04:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98816",
    "user": "@dimpase"
}
```

OK, my bad...



---

archive/issue_comments_098817.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-09-19T09:04:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98817",
    "user": "@dimpase"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_098818.json:
```json
{
    "body": "Typo, my apologies.",
    "created_at": "2010-09-27T09:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98818",
    "user": "@loefflerd"
}
```

Typo, my apologies.



---

archive/issue_comments_098819.json:
```json
{
    "body": "Resolution changed from worksforme to fixed",
    "created_at": "2010-09-29T08:39:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98819",
    "user": "@qed777"
}
```

Resolution changed from worksforme to fixed



---

archive/issue_comments_098820.json:
```json
{
    "body": "Karl-Dieter Crisman reported this error on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/6bb037c1f4a1ace9/baa93cd5c1dc489f#baa93cd5c1dc489f):\n\n```python\nOn OS X 10.4 PPC, I get a variant on #10042 (I put this on the ticket)\nand the toric divisor one, and a known Maxima timeout due to tab-\ncompletion.  I also got the following non-repeating failure:\n\nFile \"/Users/student/Desktop/sage-4.6.alpha2/devel/sage/sage/graphs/graph.py\", line 1346:\n    sage: if not g.is_forest():\n         cycle = g.is_even_hole_free(certificate = True)\n         if cycle.order() % Integer(2) == Integer(1):\n             print \"Error !\"\n         if not cycle.is_isomorphic(\n                graphs.CycleGraph(cycle.order())):\n             print \"Error !\"\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/student/Desktop/sage-4.6.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/student/Desktop/sage-4.6.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/student/Desktop/sage-4.6.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[8]>\", line 1, in <module>\n        if not g.is_forest():###line 1346:\n    sage: if not g.is_forest():\n      File \"/Users/student/Desktop/sage-4.6.alpha2/local/lib/python/site-packages/sage/graphs/generic_graph.py\", line 1823, in is_forest\n        for g in self.connected_components_subgraphs():\n      File \"/Users/student/Desktop/sage-4.6.alpha2/local/lib/python/site-packages/sage/graphs/generic_graph.py\", line 3136, in connected_components_subgraphs\n        list.append(self.subgraph(c, inplace=False))\n      File \"/Users/student/Desktop/sage-4.6.alpha2/local/lib/python/site-packages/sage/graphs/generic_graph.py\", line 8170, in subgraph\n        edge_property=edge_property)\n      File \"/Users/student/Desktop/sage-4.6.alpha2/local/lib/python/site-packages/sage/graphs/generic_graph.py\", line 8279, in _subgraph_by_adding\n        G.add_vertices(vertices)\n      File \"/Users/student/Desktop/sage-4.6.alpha2/local/lib/python/site-packages/sage/graphs/bipartite_graph.py\", line 534, in add_vertices\n        raise RuntimeError(\"Partition must be specified (e.g. left=True).\")\n    RuntimeError: Partition must be specified (e.g. left=True).\n```\n\nDima and Nathann, could you look into this?  If it's a new problem, please open a new 4.6 blocker with this in the description.",
    "created_at": "2010-10-04T21:40:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98820",
    "user": "@qed777"
}
```

Karl-Dieter Crisman reported this error on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/6bb037c1f4a1ace9/baa93cd5c1dc489f#baa93cd5c1dc489f):

```python
On OS X 10.4 PPC, I get a variant on #10042 (I put this on the ticket)
and the toric divisor one, and a known Maxima timeout due to tab-
completion.  I also got the following non-repeating failure:

File "/Users/student/Desktop/sage-4.6.alpha2/devel/sage/sage/graphs/graph.py", line 1346:
    sage: if not g.is_forest():
         cycle = g.is_even_hole_free(certificate = True)
         if cycle.order() % Integer(2) == Integer(1):
             print "Error !"
         if not cycle.is_isomorphic(
                graphs.CycleGraph(cycle.order())):
             print "Error !"
Exception raised:
    Traceback (most recent call last):
      File "/Users/student/Desktop/sage-4.6.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/student/Desktop/sage-4.6.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/student/Desktop/sage-4.6.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[8]>", line 1, in <module>
        if not g.is_forest():###line 1346:
    sage: if not g.is_forest():
      File "/Users/student/Desktop/sage-4.6.alpha2/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 1823, in is_forest
        for g in self.connected_components_subgraphs():
      File "/Users/student/Desktop/sage-4.6.alpha2/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 3136, in connected_components_subgraphs
        list.append(self.subgraph(c, inplace=False))
      File "/Users/student/Desktop/sage-4.6.alpha2/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 8170, in subgraph
        edge_property=edge_property)
      File "/Users/student/Desktop/sage-4.6.alpha2/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 8279, in _subgraph_by_adding
        G.add_vertices(vertices)
      File "/Users/student/Desktop/sage-4.6.alpha2/local/lib/python/site-packages/sage/graphs/bipartite_graph.py", line 534, in add_vertices
        raise RuntimeError("Partition must be specified (e.g. left=True).")
    RuntimeError: Partition must be specified (e.g. left=True).
```

Dima and Nathann, could you look into this?  If it's a new problem, please open a new 4.6 blocker with this in the description.



---

archive/issue_comments_098821.json:
```json
{
    "body": "It's another of this SERGHLIGHLWIEUGH BipartiteGraph-related errors --> they overload methods like add-edge to stay compatible. Usually wrapping the graph inside Graph(g) to cast it toward a regular graph is enough, but I'll give it a look only tomorrow. I have far too much of this wonderful red wine in the brain at the moment. You'll have a patch tomorrow -- sorry for that !\n\nNathann",
    "created_at": "2010-10-04T21:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98821",
    "user": "@nathanncohen"
}
```

It's another of this SERGHLIGHLWIEUGH BipartiteGraph-related errors --> they overload methods like add-edge to stay compatible. Usually wrapping the graph inside Graph(g) to cast it toward a regular graph is enough, but I'll give it a look only tomorrow. I have far too much of this wonderful red wine in the brain at the moment. You'll have a patch tomorrow -- sorry for that !

Nathann



---

archive/issue_comments_098822.json:
```json
{
    "body": "Replying to [comment:20 mpatel]:\n> Karl-Dieter Crisman reported this error on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/6bb037c1f4a1ace9/baa93cd5c1dc489f#baa93cd5c1dc489f):\n\nI saw the same non-repeating error on Skynet's fulvia (x86_64-SunOS-core2).  The full log is [here](http://build.sagemath.org/sage/builders/fulvia%20full/builds/1/steps/shell_5/logs/stdio).",
    "created_at": "2010-10-05T03:43:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98822",
    "user": "@qed777"
}
```

Replying to [comment:20 mpatel]:
> Karl-Dieter Crisman reported this error on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/6bb037c1f4a1ace9/baa93cd5c1dc489f#baa93cd5c1dc489f):

I saw the same non-repeating error on Skynet's fulvia (x86_64-SunOS-core2).  The full log is [here](http://build.sagemath.org/sage/builders/fulvia%20full/builds/1/steps/shell_5/logs/stdio).



---

archive/issue_comments_098823.json:
```json
{
    "body": "This is fixed by both #10067 and #9422",
    "created_at": "2010-10-05T08:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98823",
    "user": "@nathanncohen"
}
```

This is fixed by both #10067 and #9422



---

archive/issue_comments_098824.json:
```json
{
    "body": "Replying to [comment:23 ncohen]:\n> This is fixed by both #10067 and #9422\n\nCould you give before-after example(s) here analogous to those in [comment:6 comment 6], that show statistically, at least, that the new patches fix the problem?  Is it practical to use one of these examples as a long doctest?",
    "created_at": "2010-10-05T08:55:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98824",
    "user": "@qed777"
}
```

Replying to [comment:23 ncohen]:
> This is fixed by both #10067 and #9422

Could you give before-after example(s) here analogous to those in [comment:6 comment 6], that show statistically, at least, that the new patches fix the problem?  Is it practical to use one of these examples as a long doctest?



---

archive/issue_comments_098825.json:
```json
{
    "body": "To be honest I have no idea at all of the probability in this case. I just followed the path of the code, and saw where it can only have happened. With patch #9422, the method is_forest does not call connected_components_subgraphs anymore, which clearly avoids the bug (caused by the subgraph method. adding edges in a BipartiteGraph can lead to such exceptions). With #10067, the BipartiteGraph class is not used anymore, which means that these checks when adding edges (creating the failure) are not done anymore.\n\nMy previous checks were all about being sure there was no mistake in subgraph_search, which is some not-so-trivial Cython code. In this case, the cause of the error is crystal clear `:-)`\n\nNathann",
    "created_at": "2010-10-05T09:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98825",
    "user": "@nathanncohen"
}
```

To be honest I have no idea at all of the probability in this case. I just followed the path of the code, and saw where it can only have happened. With patch #9422, the method is_forest does not call connected_components_subgraphs anymore, which clearly avoids the bug (caused by the subgraph method. adding edges in a BipartiteGraph can lead to such exceptions). With #10067, the BipartiteGraph class is not used anymore, which means that these checks when adding edges (creating the failure) are not done anymore.

My previous checks were all about being sure there was no mistake in subgraph_search, which is some not-so-trivial Cython code. In this case, the cause of the error is crystal clear `:-)`

Nathann



---

archive/issue_comments_098826.json:
```json
{
    "body": "I don't have time to apply the patches, but without them, the code:\n\n```python\ndef example(verbose=False):\n    try:\n        g = graphs.RandomBipartite(10, 10, .5)\n        g.is_even_hole_free() and not g.is_forest()\n        if not g.is_forest():\n            cycle = g.is_even_hole_free(certificate = True)\n            if cycle.order() % 2 == 1:\n                print \"Error !\"\n            if not cycle.is_isomorphic(graphs.CycleGraph(cycle.order())):\n                print \"Error !\"\n        error = False\n    except RuntimeError as exc:\n        error = True\n        if verbose:\n            print exc\n    return error\n\ndef runner(n=1000):\n    fail = 0\n    for i in xrange(n):\n        fail += example()\n    return fail\n\nrunner()\n```\n\ngives 20 or so failures.  Could you check your patches against this or a similar statistical diagnostic?",
    "created_at": "2010-10-05T21:49:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98826",
    "user": "@qed777"
}
```

I don't have time to apply the patches, but without them, the code:

```python
def example(verbose=False):
    try:
        g = graphs.RandomBipartite(10, 10, .5)
        g.is_even_hole_free() and not g.is_forest()
        if not g.is_forest():
            cycle = g.is_even_hole_free(certificate = True)
            if cycle.order() % 2 == 1:
                print "Error !"
            if not cycle.is_isomorphic(graphs.CycleGraph(cycle.order())):
                print "Error !"
        error = False
    except RuntimeError as exc:
        error = True
        if verbose:
            print exc
    return error

def runner(n=1000):
    fail = 0
    for i in xrange(n):
        fail += example()
    return fail

runner()
```

gives 20 or so failures.  Could you check your patches against this or a similar statistical diagnostic?



---

archive/issue_comments_098827.json:
```json
{
    "body": "You could also try, e.g.,\n\n\n```sh\nenv SAGE_TEST_ITER=100 ./sage -tp -long devel/sage/sage/graphs/graph.py \n```\n\non various files.  I believe this will \"break\" on the first failure in a file.  There's also `SAGE_TEST_GLOBAL_ITER`.  For this, I recommend capturing the output in a file and checking later for failures.  Note: `sage -tp` uses these variables, but `sage -t` does not.",
    "created_at": "2010-10-05T22:08:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98827",
    "user": "@qed777"
}
```

You could also try, e.g.,


```sh
env SAGE_TEST_ITER=100 ./sage -tp -long devel/sage/sage/graphs/graph.py 
```

on various files.  I believe this will "break" on the first failure in a file.  There's also `SAGE_TEST_GLOBAL_ITER`.  For this, I recommend capturing the output in a file and checking later for failures.  Note: `sage -tp` uses these variables, but `sage -t` does not.



---

archive/issue_comments_098828.json:
```json
{
    "body": "I've opened #10081 as a 4.6 blocker for the problem in [comment:20 comment 20].",
    "created_at": "2010-10-06T04:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98828",
    "user": "@qed777"
}
```

I've opened #10081 as a 4.6 blocker for the problem in [comment:20 comment 20].



---

archive/issue_comments_098829.json:
```json
{
    "body": "Well, as you had taken the time to write this testing function, I tested it against the patches (with n = 10 000, as I was working on a sheet of paper at the same time and did not mind forgetting it for several minutes `:-D`) :\n\nWith #9422 applied :\n\n```python\nsage: runner(10000)\n0\n```\n\n\nWith no patch applied, but with \n\n```python\ng = graphs.RandomBipartite(10, 10, .5)\n```\n\nreplaced by \n\n```python\ng = Graph(graphs.RandomBipartite(10, 10, .5))\n```\n\n\nin your code (which is exactly what the docstring in #10067 does) :\n\n\n```python\nsage: runner(10000)\n0\n```\n\n\nBe sure that this is not just a statistical proof : #9422 \"disconnects\" the call to the ``is_subgraph`` command, so there is really no path left leading to this exception from BipartiteGraph !\n\nNathann\n\nP.S. : Thank you for this ``#!python`` trick ! Very nice `;-)`",
    "created_at": "2010-10-06T12:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9924#issuecomment-98829",
    "user": "@nathanncohen"
}
```

Well, as you had taken the time to write this testing function, I tested it against the patches (with n = 10 000, as I was working on a sheet of paper at the same time and did not mind forgetting it for several minutes `:-D`) :

With #9422 applied :

```python
sage: runner(10000)
0
```


With no patch applied, but with 

```python
g = graphs.RandomBipartite(10, 10, .5)
```

replaced by 

```python
g = Graph(graphs.RandomBipartite(10, 10, .5))
```


in your code (which is exactly what the docstring in #10067 does) :


```python
sage: runner(10000)
0
```


Be sure that this is not just a statistical proof : #9422 "disconnects" the call to the ``is_subgraph`` command, so there is really no path left leading to this exception from BipartiteGraph !

Nathann

P.S. : Thank you for this ``#!python`` trick ! Very nice `;-)`
