# Issue 7593: Matching using LP

Issue created by migration from https://trac.sagemath.org/ticket/7593

Original creator: ncohen

Original creation time: 2009-12-03 14:46:04

Assignee: rlm

As the title says, this patch implements a function solving the maximum weight matching problem.


---

Comment by ncohen created at 2009-12-03 15:18:22

Changing status from new to needs_review.


---

Comment by wdj created at 2009-12-14 17:52:38

Changing status from needs_review to needs_work.


---

Comment by wdj created at 2009-12-14 17:52:38

I could not get this to apply to sage 4.3.rc0 with glpk installed.

Do you need to rebase this?


---

Comment by ncohen created at 2009-12-14 17:55:17

Well, I need to rebase it each time there is a new version of Sage, and this until it finally gets reviewed... I'll rebase it just now !

Nathann


---

Comment by ncohen created at 2009-12-14 18:00:17

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2009-12-14 18:00:17

here it is !!! This may  well be the tenth version of this function which has been written 6 months ago :p

Nathann


---

Comment by wdj created at 2009-12-15 02:03:17

Changing status from needs_review to needs_info.


---

Comment by wdj created at 2009-12-15 02:03:17

Replying to [comment:5 ncohen]:
> here it is !!! This may  well be the tenth version of this function which has been 
> written 6 months ago :p
> 
> Nathann

Sorry for the long delay in refereeing. 

It applies okay to 4.3.rc0 on ubuntu 9.04 32 bit, and passes 
sage -testall except for the failures that I got without the 
patch installed (in calculus and nf_introduction). The documentation also
looks satisfactory to me. The optional test


```
sage -t -optional "devel/sage/sage/graphs/graph.py
```

gave rise to (in particular) the following failure

```
wdj@wdj-virtualbox:~/sagefiles/sage-4.3.rc0$ ./sage -t -optional "devel/sage/sage/graphs/graph.py"
sage -t -optional "devel/sage/sage/graphs/graph.py"         
sh: kpsewhich: not found
sh: kpsewhich: not found
sh: kpsewhich: not found
sh: kpsewhich: not found
**********************************************************************
File "/home/wdj/sagefiles/sage-4.3.rc0/devel/sage/sage/graphs/graph.py", line 3293:
    sage: g.matching(value_only=True) # optional - requires Glpk or COIN-OR/CBC
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-4.3.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/wdj/sagefiles/sage-4.3.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/wdj/sagefiles/sage-4.3.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_59[3]>", line 1, in <module>
        g.matching(value_only=True) # optional - requires Glpk or COIN-OR/CBC###line 3293:
    sage: g.matching(value_only=True) # optional - requires Glpk or COIN-OR/CBC
      File "/home/wdj/sagefiles/sage-4.3.rc0/local/lib/python/site-packages/sage/graphs/graph.py", line 3316, in matching
        return p.solve(objective_only=True)
      File "mip.pyx", line 945, in sage.numerical.mip.MixedIntegerLinearProgram.solve (sage/numerical/mip.c:7177)
    ValueError: There does not seem to be any solver installed. Please visit http://www.sagemath.org/doc/tutorial/tour_LP.html for more informations.
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_59
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wdj/.sage//tmp/.doctest_graph.py
	 [74.3 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -optional "devel/sage/sage/graphs/graph.py"
```


Does this seem related to your patch? glpk is installed, to the error message
("solver not installed") seems wrong, or at least is unexpected by me.


---

Comment by ncohen created at 2009-12-15 08:36:25

This is indeed related to my patch, but I have a question : when you say that glpk is installed, do you mean that you installed it in the same branche where you applied the patch ? If you installed it when you were using a different branch, then switched to another one to test this patch, it will not be detected.. You need to install it in every branch where you need to use it :-)

This comes from the fact that during the installation of the procedure, the file mipGlpk.pyx is compiled and only accessible by the "current" branch. You the probably need to switch to the branch which uses matching, then to sage -f GLPK ( as it needs to be forced ) :-)

Hope this will solve it ! :-)

Nathann


---

Comment by wdj created at 2009-12-15 12:46:16

Agreed.  Thanks. Very useful patch.


---

Comment by wdj created at 2009-12-15 12:46:16

Changing status from needs_info to needs_review.


---

Comment by wdj created at 2009-12-15 12:47:08

Changing status from needs_review to positive_review.


---

Comment by wdj created at 2009-12-15 12:47:08

Applies and tests fine on sage 4.3.rc0 and ubuntu 9.04 32 bit.


---

Comment by ncohen created at 2009-12-15 13:49:17

Yeppeeeeeeeeeee !! :-)

Thank you veeeeeeeeeeeeeeeeeeeeeeeeeeryyyyyyyyyyyyyyy much :-)

Nathann


---

Comment by mhansen created at 2009-12-15 16:07:27

The patch needs a little touching up.

It should be `.. math::` instead of `.. MATH::`.  Also, it would be good to follow PEP 8 rules http://www.python.org/dev/peps/pep-0008/ regarding spacing -- http://www.python.org/dev/peps/pep-0008/ .


---

Attachment

I just updated the path to replace MATH by math :-)


---

Comment by mhansen created at 2009-12-19 21:06:30

Resolution: fixed
