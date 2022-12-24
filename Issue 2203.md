# Issue 2203: Integrate concorde in Sage

archive/issues_002203.json:
```json
{
    "body": "Assignee: rlm\n\nConcorde is a state-of-the-art traveling salesman problem solver and it's GPL! :)\n\nhttp://www.tsp.gatech.edu/concorde/index.html\n\nI have a student that might be interested in implementing an interface, so email me if you plan on working on this and I'll forward it to him.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2203\n\n",
    "created_at": "2008-02-18T15:37:09Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Integrate concorde in Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2203",
    "user": "jason"
}
```
Assignee: rlm

Concorde is a state-of-the-art traveling salesman problem solver and it's GPL! :)

http://www.tsp.gatech.edu/concorde/index.html

I have a student that might be interested in implementing an interface, so email me if you plan on working on this and I'll forward it to him.

Issue created by migration from https://trac.sagemath.org/ticket/2203





---

archive/issue_comments_014500.json:
```json
{
    "body": "I take that back, concorde is *not* GPL.  From the readme:\n\n  The code is written\nin the ANSI C programming language and it is available for academic\nresearch use; for other uses, contact bico`@`isye.gatech.edu for\nlicensing options.\n\nSo maybe it could be a optional package unless we can get a GPL version.",
    "created_at": "2008-02-18T18:01:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14500",
    "user": "jason"
}
```

I take that back, concorde is *not* GPL.  From the readme:

  The code is written
in the ANSI C programming language and it is available for academic
research use; for other uses, contact bico`@`isye.gatech.edu for
licensing options.

So maybe it could be a optional package unless we can get a GPL version.



---

archive/issue_comments_014501.json:
```json
{
    "body": "Changing assignee from rlm to jason.",
    "created_at": "2008-08-30T21:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14501",
    "user": "rlm"
}
```

Changing assignee from rlm to jason.



---

archive/issue_comments_014502.json:
```json
{
    "body": "Another option for a Traveling Salesman Problem solver is the code here:\n\nhttp://www.cs.utoronto.ca/~neto/\n\nSpecifically, http://www.cs.utoronto.ca/~neto/research/lk/\n\nIt is GPL.",
    "created_at": "2008-12-01T16:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14502",
    "user": "jason"
}
```

Another option for a Traveling Salesman Problem solver is the code here:

http://www.cs.utoronto.ca/~neto/

Specifically, http://www.cs.utoronto.ca/~neto/research/lk/

It is GPL.



---

archive/issue_comments_014503.json:
```json
{
    "body": "Also, the student referenced above does not currently have the time to work on this, so if you want to work on it, go right ahead.",
    "created_at": "2008-12-01T16:34:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14503",
    "user": "jason"
}
```

Also, the student referenced above does not currently have the time to work on this, so if you want to work on it, go right ahead.



---

archive/issue_comments_014504.json:
```json
{
    "body": "This package of algorithms seems to be very famous in the world of TSP solvers :\nhttp://www.cs.sunysb.edu/~algorith/implement/tsp/distrib/tsp_solve/tsp_solve-1.3.6.tar.gz\nIt contains both exact and heuristical solvers.. The thing is that I read nowhere it was licensed under the GPL license, but the beginning of the README file contains :\nTspSolve -- Copyright(c) 1994 Free Software Foundation\n\nStill< i do not knwo what it means ;-)",
    "created_at": "2009-04-18T09:30:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14504",
    "user": "ncohen"
}
```

This package of algorithms seems to be very famous in the world of TSP solvers :
http://www.cs.sunysb.edu/~algorith/implement/tsp/distrib/tsp_solve/tsp_solve-1.3.6.tar.gz
It contains both exact and heuristical solvers.. The thing is that I read nowhere it was licensed under the GPL license, but the beginning of the README file contains :
TspSolve -- Copyright(c) 1994 Free Software Foundation

Still< i do not knwo what it means ;-)



---

archive/issue_comments_014505.json:
```json
{
    "body": "The README file also has the distribution license, near the\nbottom of the file. It appears to be GPL-compatible \nbut slightly stronger than the modified BSD.\n\nI agree that \"Copyright(c) 1994 Free Software Foundation\" at the top of the file is odd!",
    "created_at": "2009-04-18T11:04:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14505",
    "user": "wdj"
}
```

The README file also has the distribution license, near the
bottom of the file. It appears to be GPL-compatible 
but slightly stronger than the modified BSD.

I agree that "Copyright(c) 1994 Free Software Foundation" at the top of the file is odd!



---

archive/issue_comments_014506.json:
```json
{
    "body": "I tried to send an email to the author but his mail address seems to be outdated.... I found another and was not luckier.. In the end, is it SAGE-Compatible ? ;-)\n\nNathann",
    "created_at": "2009-04-18T11:17:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14506",
    "user": "ncohen"
}
```

I tried to send an email to the author but his mail address seems to be outdated.... I found another and was not luckier.. In the end, is it SAGE-Compatible ? ;-)

Nathann



---

archive/issue_comments_014507.json:
```json
{
    "body": "I just sent an email to the author. (It seems he has just used a commercial spam filter so you have to jump through a few hoops to get his email to be actually delivered to his inbox.)\n\nYes, the license is GPL-compatible, hence Sage-compatible. \nI pointed out in my email to his that IANAL but it seems\nto me that he (the author) cannot both assign the \ncopyright to someone else and also issue a distribution license of *his* own choosing.",
    "created_at": "2009-04-18T11:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14507",
    "user": "wdj"
}
```

I just sent an email to the author. (It seems he has just used a commercial spam filter so you have to jump through a few hoops to get his email to be actually delivered to his inbox.)

Yes, the license is GPL-compatible, hence Sage-compatible. 
I pointed out in my email to his that IANAL but it seems
to me that he (the author) cannot both assign the 
copyright to someone else and also issue a distribution license of *his* own choosing.



---

archive/issue_comments_014508.json:
```json
{
    "body": "I'm pretty glad to have found a way to write this as a linear programs without having to define too many constraints, and without having to use column generation... So here are the long-awaited functions ! :-))))))))\n\nIf anyone is interested in steiner trees, they should not be hard to write either...\n\nWell, clearly Concorde is miles above this function, but I have attempted to interface it 3 times so far, and each time I left my office cursing their (abscence of) documentation... :p\n\nNathann",
    "created_at": "2010-02-05T09:05:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14508",
    "user": "ncohen"
}
```

I'm pretty glad to have found a way to write this as a linear programs without having to define too many constraints, and without having to use column generation... So here are the long-awaited functions ! :-))))))))

If anyone is interested in steiner trees, they should not be hard to write either...

Well, clearly Concorde is miles above this function, but I have attempted to interface it 3 times so far, and each time I left my office cursing their (abscence of) documentation... :p

Nathann



---

archive/issue_comments_014509.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-05T09:05:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14509",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_014510.json:
```json
{
    "body": "Nice!\n\nA small comment: I think \"is_*\" functions should return either True or False.  We have is_hamiltonian() returning False or an object.  I think it would be more consistent to have a hamiltonian_cycle() function that returns a TSP or False, and maybe also an is_hamiltonian function that just returns True and False.",
    "created_at": "2010-02-05T09:19:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14510",
    "user": "jason"
}
```

Nice!

A small comment: I think "is_*" functions should return either True or False.  We have is_hamiltonian() returning False or an object.  I think it would be more consistent to have a hamiltonian_cycle() function that returns a TSP or False, and maybe also an is_hamiltonian function that just returns True and False.



---

archive/issue_comments_014511.json:
```json
{
    "body": "Here is my dilemma : I first thought of having an argument cycle=True in is_hamiltonian to make it return the cycle whenever possible, then noticed that if Graph() would work well anyway, so it wouldn't matter in the end. The thing is that a hamiltonian_cycle function would be a complete alias of travelling_salesman_problem, and also that I always feel bad talking about \"cycles\" when this function returns a \"circuit\" (in a digraph). So from my point of view, hamiltonian_cycle is not meant to be applied to directed graphs....\n\nWell, if you can find your way through all this... :-)\n\nNathann",
    "created_at": "2010-02-05T09:22:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14511",
    "user": "ncohen"
}
```

Here is my dilemma : I first thought of having an argument cycle=True in is_hamiltonian to make it return the cycle whenever possible, then noticed that if Graph() would work well anyway, so it wouldn't matter in the end. The thing is that a hamiltonian_cycle function would be a complete alias of travelling_salesman_problem, and also that I always feel bad talking about "cycles" when this function returns a "circuit" (in a digraph). So from my point of view, hamiltonian_cycle is not meant to be applied to directed graphs....

Well, if you can find your way through all this... :-)

Nathann



---

archive/issue_comments_014512.json:
```json
{
    "body": "( ... after some email ... )\n\nOk, ok, I got it !! Here is the new version of this patch ! ;-)\n\nNathann",
    "created_at": "2010-02-07T07:41:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14512",
    "user": "ncohen"
}
```

( ... after some email ... )

Ok, ok, I got it !! Here is the new version of this patch ! ;-)

Nathann



---

archive/issue_comments_014513.json:
```json
{
    "body": "I installed it and ran sage -testall. No Failures.\n\nThen I installed glpk and ran sage -testall --optional and got (among \nlots of other failures which are presumably unrelated) this:\n\n\n```\njeeves:sage-4.3.2 wdj$ ./sage -t  --optional \"devel/sage/sage/graphs/generic_graph.py\"\nsage -t --optional \"devel/sage/sage/graphs/generic_graph.py\"\n**********************************************************************\nFile \"/Users/wdj/sagefiles/sage-4.3.2/devel/sage/sage/graphs/generic_graph.py\", line 4097:\n    sage: g.vertex_disjoint_paths(0,1) # optional - requires GLPK or CBC\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/wdj/sagefiles/sage-4.3.2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/wdj/sagefiles/sage-4.3.2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/wdj/sagefiles/sage-4.3.2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_69[3]>\", line 1, in <module>\n        g.vertex_disjoint_paths(Integer(0),Integer(1)) # optional - requires GLPK or CBC###line 4097:\n    sage: g.vertex_disjoint_paths(0,1) # optional - requires GLPK or CBC\n      File \"/Users/wdj/sagefiles/sage-4.3.2/local/lib/python/site-packages/sage/graphs/generic_graph.py\", line 4101, in vertex_disjoint_paths\n        [obj, flow_graph] = self.flow(s,t,value_only=False, integer=True, use_edge_labels=False, vertex_bound=True)\n      File \"/Users/wdj/sagefiles/sage-4.3.2/local/lib/python/site-packages/sage/graphs/generic_graph.py\", line 3986, in flow\n        [p.add_constraint([flow[X][v] for X in g[v]],max=1) for v in g if v!=x and v!=y]\n      File \"mip.pyx\", line 670, in sage.numerical.mip.MixedIntegerLinearProgram.add_constraint (sage/numerical/mip.c:5462)\n    AttributeError: 'list' object has no attribute 'f'\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_69\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /Users/wdj/.sage//tmp/.doctest_generic_graph.py\n         [29.4 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t --optional \"devel/sage/sage/graphs/generic_graph.py\"\n```\n\n\nIs this a related failure?",
    "created_at": "2010-02-07T22:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14513",
    "user": "wdj"
}
```

I installed it and ran sage -testall. No Failures.

Then I installed glpk and ran sage -testall --optional and got (among 
lots of other failures which are presumably unrelated) this:


```
jeeves:sage-4.3.2 wdj$ ./sage -t  --optional "devel/sage/sage/graphs/generic_graph.py"
sage -t --optional "devel/sage/sage/graphs/generic_graph.py"
**********************************************************************
File "/Users/wdj/sagefiles/sage-4.3.2/devel/sage/sage/graphs/generic_graph.py", line 4097:
    sage: g.vertex_disjoint_paths(0,1) # optional - requires GLPK or CBC
Exception raised:
    Traceback (most recent call last):
      File "/Users/wdj/sagefiles/sage-4.3.2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/wdj/sagefiles/sage-4.3.2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/wdj/sagefiles/sage-4.3.2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_69[3]>", line 1, in <module>
        g.vertex_disjoint_paths(Integer(0),Integer(1)) # optional - requires GLPK or CBC###line 4097:
    sage: g.vertex_disjoint_paths(0,1) # optional - requires GLPK or CBC
      File "/Users/wdj/sagefiles/sage-4.3.2/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 4101, in vertex_disjoint_paths
        [obj, flow_graph] = self.flow(s,t,value_only=False, integer=True, use_edge_labels=False, vertex_bound=True)
      File "/Users/wdj/sagefiles/sage-4.3.2/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 3986, in flow
        [p.add_constraint([flow[X][v] for X in g[v]],max=1) for v in g if v!=x and v!=y]
      File "mip.pyx", line 670, in sage.numerical.mip.MixedIntegerLinearProgram.add_constraint (sage/numerical/mip.c:5462)
    AttributeError: 'list' object has no attribute 'f'
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_69
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/wdj/.sage//tmp/.doctest_generic_graph.py
         [29.4 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t --optional "devel/sage/sage/graphs/generic_graph.py"
```


Is this a related failure?



---

archive/issue_comments_014514.json:
```json
{
    "body": "No, it is not. This comes from something internal to MixedIntegerLinearProgram, which has been corrected somewhere already... It could be #7311 though I am not sure. The point is that I have seen it for some time, and I stopped worrying a while ago. So this is bound to mean I already fixed it :-)\n\nNathann",
    "created_at": "2010-02-08T02:40:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14514",
    "user": "ncohen"
}
```

No, it is not. This comes from something internal to MixedIntegerLinearProgram, which has been corrected somewhere already... It could be #7311 though I am not sure. The point is that I have seen it for some time, and I stopped worrying a while ago. So this is bound to mean I already fixed it :-)

Nathann



---

archive/issue_comments_014515.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-08T03:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14515",
    "user": "wdj"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_014516.json:
```json
{
    "body": "Although I am not really competent in this area, I am changing this back to needs work since it does not have an example where the graph is weighted (other than all weights being equal to 1). Since this is a parameter option, it really should be tested. It would be nice to have an example where there is a choice of circuits (eg, with the hypercube graph) but only one which is cheapest.",
    "created_at": "2010-02-08T03:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14516",
    "user": "wdj"
}
```

Although I am not really competent in this area, I am changing this back to needs work since it does not have an example where the graph is weighted (other than all weights being equal to 1). Since this is a parameter option, it really should be tested. It would be nice to have an example where there is a choice of circuits (eg, with the hypercube graph) but only one which is cheapest.



---

archive/issue_comments_014517.json:
```json
{
    "body": "With a brand new example ! ;-)\n\nNathann",
    "created_at": "2010-02-08T12:29:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14517",
    "user": "ncohen"
}
```

With a brand new example ! ;-)

Nathann



---

archive/issue_comments_014518.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-08T12:29:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14518",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_014519.json:
```json
{
    "body": "This had the same (unrelated?) failures as before. The docstrings look much better now and the added functionalit is very nice!\n\nIt looks good to me but I prefer to let Jason Grout have the final say.",
    "created_at": "2010-02-08T16:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14519",
    "user": "wdj"
}
```

This had the same (unrelated?) failures as before. The docstrings look much better now and the added functionalit is very nice!

It looks good to me but I prefer to let Jason Grout have the final say.



---

archive/issue_comments_014520.json:
```json
{
    "body": "A couple of somewhat picky notes from just reading through the code:\n\n* \"traveling\" is spelled with one 'l' in American English.  See [Oxford English Dictionary](http://dictionary.oed.com/cgi/entry/50256805?query_type=word&queryword=travel&first=1&max_to_show=10&sort_type=alpha&search_id=CNCH-0vTuPN-10331&result_place=2), \"Derivatives, as travelled, -er, -ing, etc. are usually spelt with ll in Gr. Britain, with single l in America.\"  With no offense to those across the Great Pond, it seems that we've standardized on American English for spelling.\n\n* I don't think there is a need for the \"is_hamiltonian\" note in the TSP function.\n\n* If these functions require an optional package, it should probably mention that as a note or warning in the documentation.\n\nI'll try applying this patch soon to have a more thorough review.  It looks really nice!",
    "created_at": "2010-02-08T18:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14520",
    "user": "jason"
}
```

A couple of somewhat picky notes from just reading through the code:

* "traveling" is spelled with one 'l' in American English.  See [Oxford English Dictionary](http://dictionary.oed.com/cgi/entry/50256805?query_type=word&queryword=travel&first=1&max_to_show=10&sort_type=alpha&search_id=CNCH-0vTuPN-10331&result_place=2), "Derivatives, as travelled, -er, -ing, etc. are usually spelt with ll in Gr. Britain, with single l in America."  With no offense to those across the Great Pond, it seems that we've standardized on American English for spelling.

* I don't think there is a need for the "is_hamiltonian" note in the TSP function.

* If these functions require an optional package, it should probably mention that as a note or warning in the documentation.

I'll try applying this patch soon to have a more thorough review.  It looks really nice!



---

archive/issue_comments_014521.json:
```json
{
    "body": "This new patch is now written in american, even though it hurts (I so love english people). I also removed the comment from the TSP function.\n\nConcerning the note in the docstrings about optional packages, well.. My opinion is that we may consider LP to be optional, but that many recent patches added very useful functionalities requiring the user to install at least one LP solver, so to be honest these packages, one can less and less do without these packages, which are to be named \"optional\" because of license incompatibilities... \n\nIf you feel it is really necessary, though, it looks like we should \"normalize\" the Graph class and add comments to each function which uses LP or depends on it :-)\n\nNathann",
    "created_at": "2010-02-09T09:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14521",
    "user": "ncohen"
}
```

This new patch is now written in american, even though it hurts (I so love english people). I also removed the comment from the TSP function.

Concerning the note in the docstrings about optional packages, well.. My opinion is that we may consider LP to be optional, but that many recent patches added very useful functionalities requiring the user to install at least one LP solver, so to be honest these packages, one can less and less do without these packages, which are to be named "optional" because of license incompatibilities... 

If you feel it is really necessary, though, it looks like we should "normalize" the Graph class and add comments to each function which uses LP or depends on it :-)

Nathann



---

archive/issue_comments_014522.json:
```json
{
    "body": "I added a few lines to support multigraphs.... Before this, the problem failed if you added to each edge a paralell one, while it should only help ;-)\n\nNathann",
    "created_at": "2010-02-09T11:05:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14522",
    "user": "ncohen"
}
```

I added a few lines to support multigraphs.... Before this, the problem failed if you added to each edge a paralell one, while it should only help ;-)

Nathann



---

archive/issue_comments_014523.json:
```json
{
    "body": "Attachment [trac_2203.patch](tarball://root/attachments/some-uuid/ticket2203/trac_2203.patch) by ncohen created at 2010-02-09 11:06:10",
    "created_at": "2010-02-09T11:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14523",
    "user": "ncohen"
}
```

Attachment [trac_2203.patch](tarball://root/attachments/some-uuid/ticket2203/trac_2203.patch) by ncohen created at 2010-02-09 11:06:10



---

archive/issue_comments_014524.json:
```json
{
    "body": "Replying to [comment:24 ncohen]:\n> I added a few lines to support multigraphs.... Before this, the problem failed if you added to each edge a paralell one, while it should only help ;-)\n> \n> Nathann\n\n\nThis new patch passes the same tests as before.\n\nAgain, I leave it to Jason to give the final okay.",
    "created_at": "2010-02-10T15:31:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14524",
    "user": "wdj"
}
```

Replying to [comment:24 ncohen]:
> I added a few lines to support multigraphs.... Before this, the problem failed if you added to each edge a paralell one, while it should only help ;-)
> 
> Nathann


This new patch passes the same tests as before.

Again, I leave it to Jason to give the final okay.



---

archive/issue_comments_014525.json:
```json
{
    "body": "Changing assignee from jason to ncohen.",
    "created_at": "2010-04-08T21:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14525",
    "user": "ncohen"
}
```

Changing assignee from jason to ncohen.



---

archive/issue_comments_014526.json:
```json
{
    "body": "For an explanation of the Linear Program used to solve this problem, see the LP chapter from : http://code.google.com/p/graph-theory-algorithms-book/\n\nNathann",
    "created_at": "2010-04-08T21:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14526",
    "user": "ncohen"
}
```

For an explanation of the Linear Program used to solve this problem, see the LP chapter from : http://code.google.com/p/graph-theory-algorithms-book/

Nathann



---

archive/issue_comments_014527.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-12T17:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14527",
    "user": "wdj"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_014528.json:
```json
{
    "body": "I retested this on 4.4.2.a0. Looks good to me.",
    "created_at": "2010-05-12T17:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14528",
    "user": "wdj"
}
```

I retested this on 4.4.2.a0. Looks good to me.



---

archive/issue_comments_014529.json:
```json
{
    "body": "Attachment [trac_2203-rebase.patch](tarball://root/attachments/some-uuid/ticket2203/trac_2203-rebase.patch) by mvngu created at 2010-05-22 10:23:20\n\nrebase of previous patch",
    "created_at": "2010-05-22T10:23:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14529",
    "user": "mvngu"
}
```

Attachment [trac_2203-rebase.patch](tarball://root/attachments/some-uuid/ticket2203/trac_2203-rebase.patch) by mvngu created at 2010-05-22 10:23:20

rebase of previous patch



---

archive/issue_comments_014530.json:
```json
{
    "body": "I got a hunk failure when applying the patch on top of #8364 and #8166 in that order:\n\n\n```\n[mvngu@sage sage-main]$ hg tip\nchangeset:   14321:1451c00a8d44\ntag:         tip\nuser:        Minh Van Nguyen <nguyenminh2@gmail.com>\ndate:        Wed May 19 00:55:29 2010 -0700\nsummary:     4.4.2\n\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8364/trac_8364.patch && hg qpush \nadding trac_8364.patch to series file\napplying trac_8364.patch\nnow at: trac_8364.patch\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8364/trac_8364-reviewer.patch && hg qpush \nadding trac_8364-reviewer.patch to series file\napplying trac_8364-reviewer.patch\nnow at: trac_8364-reviewer.patch\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8166/trac_8166-rebase.patch && hg qpush \nadding trac_8166-rebase.patch to series file\napplying trac_8166-rebase.patch\nnow at: trac_8166-rebase.patch\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/2203/trac_2203.patch && hg qpush \nadding trac_2203.patch to series file\napplying trac_2203.patch\npatching file sage/graphs/generic_graph.py\nHunk #1 FAILED at 3637\n1 out of 2 hunks FAILED -- saving rejects to file sage/graphs/generic_graph.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_2203.patch\n```\n\n\nI have rebased ncohen's patch on top of #8364 and #8166. See the ticket description for instructions on how to apply the rebased patch. Someone other than myself needs to have a look through my rebase patch to make sure I didn't mess up anything. Because of this, I'm putting the ticket in \"needs review\". The code introduced by ncohen's patch (equivalently the code in the rebased patch) needs some clean-ups, but I won't do that here.",
    "created_at": "2010-05-22T10:31:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14530",
    "user": "mvngu"
}
```

I got a hunk failure when applying the patch on top of #8364 and #8166 in that order:


```
[mvngu@sage sage-main]$ hg tip
changeset:   14321:1451c00a8d44
tag:         tip
user:        Minh Van Nguyen <nguyenminh2@gmail.com>
date:        Wed May 19 00:55:29 2010 -0700
summary:     4.4.2

[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8364/trac_8364.patch && hg qpush 
adding trac_8364.patch to series file
applying trac_8364.patch
now at: trac_8364.patch
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8364/trac_8364-reviewer.patch && hg qpush 
adding trac_8364-reviewer.patch to series file
applying trac_8364-reviewer.patch
now at: trac_8364-reviewer.patch
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8166/trac_8166-rebase.patch && hg qpush 
adding trac_8166-rebase.patch to series file
applying trac_8166-rebase.patch
now at: trac_8166-rebase.patch
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/2203/trac_2203.patch && hg qpush 
adding trac_2203.patch to series file
applying trac_2203.patch
patching file sage/graphs/generic_graph.py
Hunk #1 FAILED at 3637
1 out of 2 hunks FAILED -- saving rejects to file sage/graphs/generic_graph.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_2203.patch
```


I have rebased ncohen's patch on top of #8364 and #8166. See the ticket description for instructions on how to apply the rebased patch. Someone other than myself needs to have a look through my rebase patch to make sure I didn't mess up anything. Because of this, I'm putting the ticket in "needs review". The code introduced by ncohen's patch (equivalently the code in the rebased patch) needs some clean-ups, but I won't do that here.



---

archive/issue_comments_014531.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-05-22T10:31:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14531",
    "user": "mvngu"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_014532.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-22T10:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14532",
    "user": "mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_014533.json:
```json
{
    "body": "Is this rebase to work on top of 4.4.2? I can't even get the first patch to apply. I assume only the last patch of 8364 \nis to be applied first. If not, please list exactly which patches and in what order to test this.",
    "created_at": "2010-05-23T22:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14533",
    "user": "wdj"
}
```

Is this rebase to work on top of 4.4.2? I can't even get the first patch to apply. I assume only the last patch of 8364 
is to be applied first. If not, please list exactly which patches and in what order to test this.



---

archive/issue_comments_014534.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-24T17:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14534",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_014535.json:
```json
{
    "body": "It applies nicely on my 4.4.2 using Minh's commnds.. I did not even know hg accepted urls instead of files ;-)\n\nPositive review !\n\nNathann",
    "created_at": "2010-05-24T17:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14535",
    "user": "ncohen"
}
```

It applies nicely on my 4.4.2 using Minh's commnds.. I did not even know hg accepted urls instead of files ;-)

Positive review !

Nathann



---

archive/issue_comments_014536.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T07:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2203#issuecomment-14536",
    "user": "mhansen"
}
```

Resolution: fixed
