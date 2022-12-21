# Issue 2203: Integrate concorde in Sage

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-02-18 15:37:09

Assignee: rlm

Concorde is a state-of-the-art traveling salesman problem solver and it's GPL! :)

http://www.tsp.gatech.edu/concorde/index.html

I have a student that might be interested in implementing an interface, so email me if you plan on working on this and I'll forward it to him.


---

Comment by jason created at 2008-02-18 18:01:27

I take that back, concorde is *not* GPL.  From the readme:

  The code is written
in the ANSI C programming language and it is available for academic
research use; for other uses, contact bico`@`isye.gatech.edu for
licensing options.

So maybe it could be a optional package unless we can get a GPL version.


---

Comment by rlm created at 2008-08-30 21:51:57

Changing assignee from rlm to jason.


---

Comment by jason created at 2008-12-01 16:33:05

Another option for a Traveling Salesman Problem solver is the code here:

http://www.cs.utoronto.ca/~neto/

Specifically, http://www.cs.utoronto.ca/~neto/research/lk/

It is GPL.


---

Comment by jason created at 2008-12-01 16:34:07

Also, the student referenced above does not currently have the time to work on this, so if you want to work on it, go right ahead.


---

Comment by ncohen created at 2009-04-18 09:30:44

This package of algorithms seems to be very famous in the world of TSP solvers :
http://www.cs.sunysb.edu/~algorith/implement/tsp/distrib/tsp_solve/tsp_solve-1.3.6.tar.gz
It contains both exact and heuristical solvers.. The thing is that I read nowhere it was licensed under the GPL license, but the beginning of the README file contains :
TspSolve -- Copyright(c) 1994 Free Software Foundation

Still< i do not knwo what it means ;-)


---

Comment by wdj created at 2009-04-18 11:04:07

The README file also has the distribution license, near the
bottom of the file. It appears to be GPL-compatible 
but slightly stronger than the modified BSD.

I agree that "Copyright(c) 1994 Free Software Foundation" at the top of the file is odd!


---

Comment by ncohen created at 2009-04-18 11:17:07

I tried to send an email to the author but his mail address seems to be outdated.... I found another and was not luckier.. In the end, is it SAGE-Compatible ? ;-)

Nathann


---

Comment by wdj created at 2009-04-18 11:28:16

I just sent an email to the author. (It seems he has just used a commercial spam filter so you have to jump through a few hoops to get his email to be actually delivered to his inbox.)

Yes, the license is GPL-compatible, hence Sage-compatible. 
I pointed out in my email to his that IANAL but it seems
to me that he (the author) cannot both assign the 
copyright to someone else and also issue a distribution license of *his* own choosing.


---

Comment by ncohen created at 2010-02-05 09:05:25

I'm pretty glad to have found a way to write this as a linear programs without having to define too many constraints, and without having to use column generation... So here are the long-awaited functions ! :-))))))))

If anyone is interested in steiner trees, they should not be hard to write either...

Well, clearly Concorde is miles above this function, but I have attempted to interface it 3 times so far, and each time I left my office cursing their (abscence of) documentation... :p

Nathann


---

Comment by ncohen created at 2010-02-05 09:05:25

Changing status from new to needs_review.


---

Comment by jason created at 2010-02-05 09:19:18

Nice!

A small comment: I think "is_*" functions should return either True or False.  We have is_hamiltonian() returning False or an object.  I think it would be more consistent to have a hamiltonian_cycle() function that returns a TSP or False, and maybe also an is_hamiltonian function that just returns True and False.


---

Comment by ncohen created at 2010-02-05 09:22:48

Here is my dilemma : I first thought of having an argument cycle=True in is_hamiltonian to make it return the cycle whenever possible, then noticed that if Graph() would work well anyway, so it wouldn't matter in the end. The thing is that a hamiltonian_cycle function would be a complete alias of travelling_salesman_problem, and also that I always feel bad talking about "cycles" when this function returns a "circuit" (in a digraph). So from my point of view, hamiltonian_cycle is not meant to be applied to directed graphs....

Well, if you can find your way through all this... :-)

Nathann


---

Comment by ncohen created at 2010-02-07 07:41:14

( ... after some email ... )

Ok, ok, I got it !! Here is the new version of this patch ! ;-)

Nathann


---

Comment by wdj created at 2010-02-07 22:09:55

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

Comment by ncohen created at 2010-02-08 02:40:37

No, it is not. This comes from something internal to MixedIntegerLinearProgram, which has been corrected somewhere already... It could be #7311 though I am not sure. The point is that I have seen it for some time, and I stopped worrying a while ago. So this is bound to mean I already fixed it :-)

Nathann


---

Comment by wdj created at 2010-02-08 03:09:49

Changing status from needs_review to needs_work.


---

Comment by wdj created at 2010-02-08 03:09:49

Although I am not really competent in this area, I am changing this back to needs work since it does not have an example where the graph is weighted (other than all weights being equal to 1). Since this is a parameter option, it really should be tested. It would be nice to have an example where there is a choice of circuits (eg, with the hypercube graph) but only one which is cheapest.


---

Comment by ncohen created at 2010-02-08 12:29:18

With a brand new example ! ;-)

Nathann


---

Comment by ncohen created at 2010-02-08 12:29:18

Changing status from needs_work to needs_review.


---

Comment by wdj created at 2010-02-08 16:22:07

This had the same (unrelated?) failures as before. The docstrings look much better now and the added functionalit is very nice!

It looks good to me but I prefer to let Jason Grout have the final say.


---

Comment by jason created at 2010-02-08 18:40:24

A couple of somewhat picky notes from just reading through the code:

 * "traveling" is spelled with one 'l' in American English.  See [Oxford English Dictionary](http://dictionary.oed.com/cgi/entry/50256805?query_type=word&queryword=travel&first=1&max_to_show=10&sort_type=alpha&search_id=CNCH-0vTuPN-10331&result_place=2), "Derivatives, as travelled, -er, -ing, etc. are usually spelt with ll in Gr. Britain, with single l in America."  With no offense to those across the Great Pond, it seems that we've standardized on American English for spelling.

 * I don't think there is a need for the "is_hamiltonian" note in the TSP function.

 * If these functions require an optional package, it should probably mention that as a note or warning in the documentation.

I'll try applying this patch soon to have a more thorough review.  It looks really nice!


---

Comment by ncohen created at 2010-02-09 09:24:34

This new patch is now written in american, even though it hurts (I so love english people). I also removed the comment from the TSP function.

Concerning the note in the docstrings about optional packages, well.. My opinion is that we may consider LP to be optional, but that many recent patches added very useful functionalities requiring the user to install at least one LP solver, so to be honest these packages, one can less and less do without these packages, which are to be named "optional" because of license incompatibilities... 

If you feel it is really necessary, though, it looks like we should "normalize" the Graph class and add comments to each function which uses LP or depends on it :-)

Nathann


---

Comment by ncohen created at 2010-02-09 11:05:53

I added a few lines to support multigraphs.... Before this, the problem failed if you added to each edge a paralell one, while it should only help ;-)

Nathann


---

Attachment


---

Comment by wdj created at 2010-02-10 15:31:21

Replying to [comment:24 ncohen]:
> I added a few lines to support multigraphs.... Before this, the problem failed if you added to each edge a paralell one, while it should only help ;-)
> 
> Nathann


This new patch passes the same tests as before.

Again, I leave it to Jason to give the final okay.


---

Comment by ncohen created at 2010-04-08 21:20:20

Changing assignee from jason to ncohen.


---

Comment by ncohen created at 2010-04-08 21:20:20

For an explanation of the Linear Program used to solve this problem, see the LP chapter from : http://code.google.com/p/graph-theory-algorithms-book/

Nathann


---

Comment by wdj created at 2010-05-12 17:29:14

Changing status from needs_review to positive_review.


---

Comment by wdj created at 2010-05-12 17:29:14

I retested this on 4.4.2.a0. Looks good to me.


---

Attachment

rebase of previous patch


---

Comment by mvngu created at 2010-05-22 10:31:42

I got a hunk failure when applying the patch on top of #8364 and #8166 in that order:


```
[mvngu`@`sage sage-main]$ hg tip
changeset:   14321:1451c00a8d44
tag:         tip
user:        Minh Van Nguyen <nguyenminh2`@`gmail.com>
date:        Wed May 19 00:55:29 2010 -0700
summary:     4.4.2

[mvngu`@`sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8364/trac_8364.patch && hg qpush 
adding trac_8364.patch to series file
applying trac_8364.patch
now at: trac_8364.patch
[mvngu`@`sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8364/trac_8364-reviewer.patch && hg qpush 
adding trac_8364-reviewer.patch to series file
applying trac_8364-reviewer.patch
now at: trac_8364-reviewer.patch
[mvngu`@`sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8166/trac_8166-rebase.patch && hg qpush 
adding trac_8166-rebase.patch to series file
applying trac_8166-rebase.patch
now at: trac_8166-rebase.patch
[mvngu`@`sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/2203/trac_2203.patch && hg qpush 
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

Comment by mvngu created at 2010-05-22 10:31:42

Changing status from positive_review to needs_work.


---

Comment by mvngu created at 2010-05-22 10:31:58

Changing status from needs_work to needs_review.


---

Comment by wdj created at 2010-05-23 22:41:46

Is this rebase to work on top of 4.4.2? I can't even get the first patch to apply. I assume only the last patch of 8364 
is to be applied first. If not, please list exactly which patches and in what order to test this.


---

Comment by ncohen created at 2010-05-24 17:31:39

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-05-24 17:31:39

It applies nicely on my 4.4.2 using Minh's commnds.. I did not even know hg accepted urls instead of files ;-)

Positive review !

Nathann


---

Comment by mhansen created at 2010-06-06 07:08:48

Resolution: fixed
