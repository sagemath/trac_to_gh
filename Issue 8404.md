# Issue 8404: Computing a H-minor

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-02-28 18:45:33

Assignee: rlm

This patch is a linear program to compute a H minor of a graph... I hope you will like it ! :-)

We say that a graph `G` has a `H`-minor (or that it has a graph isomorphic to `H` as a minor), if for all `h\in H`, there exist disjoint sets `S_h \subseteq V(G)` such that once the vertices of each `S_h` have been merged to create a new graph `G'`, this new graph contains `H` as a subgraph.

For more information of minor theory, see http://en.wikipedia.org/wiki/Minor_(graph_theory)

Nathann



---

Comment by ncohen created at 2010-02-28 18:46:46

Changing status from new to needs_review.


---

Comment by jason created at 2010-03-01 12:19:13

This is awesome to have something like this in Sage.  I noticed in the patch a misspelling: "exaclty" -> "exactly".

Do you have a reference for the translation of the minor problem into a linear programming problem?  Can you put that into the docstring?


---

Comment by ncohen created at 2010-03-01 15:32:26

No, that's mine. Or at least I did not read it anywhere, as I can not claim no one thought about it before. I recently talked with someone who should have known it if it existed, and who did not.

Note that it can be very slow, though, even if there is no alternative that I know of.

I will fix the typo in a minute :-)

Nathann


---

Comment by jason created at 2010-03-01 16:08:29

Well, congratulations!  I think it would be interesting to see a short writeup of it, maybe posted on arxiv.org?  Are there any other linear program graph functions that aren't in the literature that you've already incorporated into Sage?  It would make an interesting "Survey of using linear programming to solve graph problems".


---

Comment by ncohen created at 2010-03-01 16:18:44

Not really... The only way for me to use LP is through Sage, so most of what I write ends up as a patch. I recently sent a patch for two variations of graph coloring that interest me #8405.

Actually, my recent patches of LP formulations :

 * #2203 Traveling Salesman Problem
 * #7476 Edge-disjoint spanning trees
 * #7529 Maximum average Degree
 * #8403 Steiner Tree
 * #8405 Linear arboricity / Acyclic edge coloring
 * This very patch

All have the same thing in common : there is an easy way that I ignored until very recently to write "acyclicity" without using column generation. It may be a bit slower, but I do not have to write column generation to define them, at least :p

Knowing how to say "acyclicity" enables one to say "connectedness". And once you know how to say "connectedness", you can say Minor, Steiner Tree, TSP, etc :-)

What would you like to find in such a document ? A list of formulations, plus explanations ?

Nathann


---

Comment by jason created at 2010-03-01 16:40:58

Replying to [comment:5 ncohen]:


> What would you like to find in such a document ? A list of formulations, plus explanations ?


Yes, I think that would be great.  It's also a way for your Sage work to get more traditional credit in academics, especially if you are formulating things that aren't in a standard reference and might be less than straightforward.  And thirdly, it's a way for people like me, who have a minimal understanding of linear programming, to check your code :).


---

Comment by wdj created at 2010-03-01 21:39:17

Nathann: Please do write up the paper Jason suggests. I would also be very interested.


---

Comment by ncohen created at 2010-03-04 14:31:27

Here it is ! 

http://www-sop.inria.fr/members/Nathann.Cohen/LP_formulations.pdf

Nathann


---

Comment by ncohen created at 2010-03-04 14:31:27

Changing assignee from rlm to ncohen.


---

Comment by ncohen created at 2010-03-04 14:31:44

Changing assignee from ncohen to rlm.


---

Comment by dimpase created at 2010-03-05 04:16:44

Replying to [comment:7 wdj]:
> Nathann: Please do write up the paper Jason suggests. I would also be very interested.

Nathann, you seem to be systematically writing LP where it should be ILP, or MILP, right?
Please fix this.

As well, you need to include meaningful examples: e.g. showing how to use your code to show that some well-known graph (say, Petersen) is not planar by finding a Kuratowski minor. It's not obvious that your code can handle this in reasonable time (I have had my share of using ILP for seemingly small problems, with very limited success).
And, apart from planarity (planarity is easy algorithmically, so it has only theoretical interest here), few other real problems involving graph minors. 
And if the code cannot  do anything useful, it should not be included in Sage (not in the standard or optional part, anyway) 

I therefore change the status to "needs work"... (I wish we had anonymous reviewing, like in journals :-))

Dmitrii


---

Comment by dimpase created at 2010-03-05 04:16:44

Changing status from needs_review to needs_work.


---

Comment by jason created at 2010-03-05 11:26:09

Replying to [comment:10 dimpase]:

> And, apart from planarity (planarity is easy algorithmically, so it has only theoretical interest here), few other real problems involving graph minors. 
> And if the code cannot  do anything useful, it should not be included in Sage (not in the standard or optional part, anyway) 
> 


*I'm* interested in it.  In some of my research in graph parameters (minimum rank of graphs), there are some nice bounds written in terms of the minors of a graph.  Even if it only works for graphs up to 20 vertices, it would be interesting to me and others working in this area (minimum rank of graphs) so that we could quickly compute small examples.


---

Comment by ncohen created at 2010-03-05 11:58:59

Hello !!!

Here is a new version of the patch with the examples you requested. 

I mever tried to make a mystery that this method is slow. It was one on my first comments about this patch. The thing is that there is no alternative that I know of. Minor theory is not what I should work on, but it is an interesting thing and I tried to find practical algorithms to solve it, and failed most of the time. I sent messages to people who claimed to have one and received no answer... And as for every LP algorithm written in Sage, I consider this one as a quick and lazy way to have some feature available, and the function as bound to be rewritten as soon as someone will want to spend time on it.

I would like very much to send a patch soon to be able to compute the treewidth of a graph, and even heuristics for it.. I would have to ask this code from a researcher who may be kind enough to share it, but those would still remain very slow algorithms. I can not stand the very idea of a heuristic as a mathematician, but sometimes you just have no other alternative...

As for anonymous reviewing, research has still to learn from Free Software that we are working together, not competing, and most of the time just doing the best we can.

Nathann


---

Comment by ncohen created at 2010-03-05 11:58:59

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-03-05 12:03:22

Oh, and I set the test of K5 and K33 minors in Petersen Graph as both optional and long... It takes on my computer something like 4 seconds for K5 and 2 for K33 with Cbc.. With a bit of luck it will be faster soon enough : the next package for Cbc can handle multithreading and Cplex seems ti be giving free licenses to researchers and students.

( #8171 and #8172 are still waiting for review, btw :-)  )

Nathann


---

Comment by ncohen created at 2010-03-06 10:01:57

By the way... I just retried to solve this problem using CPLEX instead of Coin.. Result :


```
sage: time graphs.PetersenGraph().minor(graphs.CompleteGraph(5))
Wall time: 0.22 s
{0: [3, 8], 1: [5, 7], 2: [1, 2], 3: [0, 4], 4: [6, 9]}
```



```
sage: time graphs.PetersenGraph().minor(graphs.CompleteBipartiteGraph(3,3))
Wall time: 0.18 s
{0: [4, 9], 1: [5], 2: [1, 2], 3: [3, 8], 4: [0], 5: [7]}
```


So it seems it is not that bad after all :-)

Nathann


---

Comment by dimpase created at 2010-03-06 11:34:02

Replying to [comment:14 ncohen]:
> By the way... I just retried to solve this problem using CPLEX instead of Coin.. Result :
> 
> {{{
> sage: time graphs.PetersenGraph().minor(graphs.CompleteGraph(5))
> Wall time: 0.22 s
> {0: [3, 8], 1: [5, 7], 2: [1, 2], 3: [0, 4], 4: [6, 9]}
> }}}
> 
> {{{
> sage: time graphs.PetersenGraph().minor(graphs.CompleteBipartiteGraph(3,3))
> Wall time: 0.18 s
> {0: [4, 9], 1: [5], 2: [1, 2], 3: [3, 8], 4: [0], 5: [7]}
> }}}
> 
> So it seems it is not that bad after all :-)

I wonder how does it scale when the number of vertices of G grows.

Regarding CPLEX I would not be that optimistic - they did not say whether
they give that free licences for unlimited time.


> 
> Nathann


---

Comment by ncohen created at 2010-03-06 11:43:46

I expect it not to scale ;-)

Nathann


---

Comment by dimpase created at 2010-03-06 11:50:24

Replying to [comment:16 ncohen]:
> I expect it not to scale ;-)

yeah - can you try some 20-25 vertex examples?

(by the way, "no K_4-minor" is equivalent to "treewidth at most 2", so you can write
another short function to test fro just this...)


---

Comment by ncohen created at 2010-03-06 12:17:47

> yeah - can you try some 20-25 vertex examples?
> 
> (by the way, "no K_4-minor" is equivalent to "treewidth at most 2", so you can write
> another short function to test fro just this...)

I would be glad to review your patch if you were to write one :-D

(Sorry, but I really do not have much time available these days....)

Nathann


---

Comment by dimpase created at 2010-03-06 12:24:33

Replying to [comment:18 ncohen]:
> > yeah - can you try some 20-25 vertex examples?
> > 
> > (by the way, "no K_4-minor" is equivalent to "treewidth at most 2", so you can write
> > another short function to test fro just this...)
> 
> I would be glad to review your patch if you were to write one :-D
> 
> (Sorry, but I really do not have much time available these days....)

nobody has any time :)

well, you still should change "Linear Programming" to "(Mixed) Integer Linear Programming", at least 
in your patch and in other docs.

> 
> Nathann


---

Comment by ncohen created at 2010-03-08 18:00:55

now with *Mixed Integer* linear program


---

Comment by dimpase created at 2010-03-09 02:52:24

Changing status from needs_review to positive_review.


---

Comment by dimpase created at 2010-03-09 02:52:24

Replying to [comment:20 ncohen]:
> now with *Mixed Integer* linear program
OK, but please also fix

```
ALGORITHM

Mixed Integer Linear Program
```

it must be "Programming", not "Program" here.

I also notice similar misuses of "Linear Program/Programming" (instead of (M)ILP) on
http://www.sagemath.org/doc/reference/sage/numerical/mip.html

and another tutorial-like thing you wrote 
(in the latter you also forget to mention that max. matching problem in a graph
can be solved in polynomial time, using LP (or otherwise), so that the MILP formulation is far from the best possible)

Please fix these too some time soon, please...


---

Comment by ncohen created at 2010-03-09 10:04:14

This patch has been updated to program*ming*.

I you feel anything else in Sage needs to be fixed, please create the corresponding ticket and -- if possible -- write a patch for it.

You have set this ticket to "positive review". Have you actually tested it, docstring and documentation ?

Nathann


---

Comment by dimpase created at 2010-03-09 11:14:48

Replying to [comment:22 ncohen]:
> This patch has been updated to program*ming*.
> 
> I you feel anything else in Sage needs to be fixed, please create the corresponding ticket and -- if possible -- write a patch for it.

well, I do not know how to patch that writeup on linear programming --- Minh
does not seem to know this, either.

> 
> You have set this ticket to "positive review". Have you actually tested it, docstring and documentation ?

I applied the patch, to sage-4.3.3 on boxen (so this is a 64-bit intel linux)
and did sage -t -optional on graphs/graph.py
and it all passed (I also did some minor computations at sage prompt, just to make sure there is no screwup anywhere :))

I do not know how to *test* documentation, never heard of --- is there a way?

Oh, by the way, there is still a fix needed:

you should add # optional on the line 1951 of the file, otherwise 
sage -t (no -optional) will complain about undefined gg.

Please fix this, otherwise I'll have to revert to "needs work" :)
(I wish I had such an efficient means to make my students work hard :))

PS. I do not seem to be able to find out which MILP solver I am actually using --- is there a way to find this out without uninstalling several optional packages?

Dima


---

Comment by ncohen created at 2010-03-09 11:43:37

The difference being that I am not your student, nor do I have any intention of standing your rudeness and the way you give me orders for very long.

I write these patches, even though they require *a lot* of time, because I think people may be interested in them. If you are not (you had the kindness to mention earlier that it should be thrown away as useless), I do not need you here.

This is the last time I edit the patch, I can not afford to update it each time you change your mind about what needs to be done.

Nathann


---

Attachment

Replying to [comment:24 ncohen]:
> The difference being that I am not your student, nor do I have any intention of standing your rudeness and the way you give me orders for very long.
> 

Please point me out to a place where I was rude to you.
I apologize in advance, if you like, anyway.

By the way, I am considerably older than you, so please also forgive me slipping
into patronizing.

> I write these patches, even though they require *a lot* of time, because I think people may be interested in them. If you are not (you had the kindness to mention earlier that it should be thrown away as useless), I do not need you here.
> 

I just want your, and others, patches to be useful to people, this is all.
I never said that your work should be thrown away, regardless. I said it should be thrown away if it does not work as advertised, and I asked you to provide few more examples to demonstrate the usefulness of them. This is downright normal reviewing process, believe me. 

In fact, I am very patient with you. Many would have said "meshugene genz, meshugene grivn", and stopped dealing with you and your patches all together.  

And this is exactly the point when I wondered aloud whether it would be better
to have anonymous reviewers. :-)

> This is the last time I edit the patch, I can not afford to update it each time you change your mind about what needs to be done.
>

It's not that I change my mind, that is I see a way to improve it. It's normal process of work. I am only human after all.

Dima   

> Nathann


---

Comment by ncohen created at 2010-03-13 08:06:44

Where the conversation moved : 

http://groups.google.com/group/sage-devel/browse_thread/thread/cd4e971043773fd3

Nathann


---

Comment by ncohen created at 2010-03-16 02:06:33

With the new (and free) cplex, it takes 120 seconds to prove there is no K5 in a 4x4 grid. Finding a K4 is instantaneous.

Nathann


---

Comment by jhpalmieri created at 2010-04-15 23:45:51

Merged "trac_8404.patch" into 4.4.alpha0.


---

Comment by jhpalmieri created at 2010-04-15 23:45:51

Resolution: fixed
