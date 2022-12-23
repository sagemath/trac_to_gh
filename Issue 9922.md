# Issue 9922: Minimum Feedback Arc/Edge set through constraint generation

Issue created by migration from https://trac.sagemath.org/ticket/9923

Original creator: ncohen

Original creation time: 2010-09-16 20:25:16

Assignee: jason, ncohen, rlm

CC:  abmasse mvngu

Because of the friend who made me work on Feedback Arc Set and is already the cause of #9911, I implemented another LP formulation of this problem using constraint generation. The performances are....... IMPROVED `:-)`

If you have any question while reviewing this, please do not hesitate. As usual, I tried my best to make the code understandable `:-)`

Require #9911

Nathann


---

Comment by ncohen created at 2010-09-16 20:26:25

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-09-23 15:44:13

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-09-30 23:00:48

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-10-23 16:53:53

Rebased on top of #9911 and its dependencies.

Nathann


---

Attachment


---

Comment by rlm created at 2011-01-12 03:38:12

Nathann,

Can you say more about the difference between the two patches? Why should we merge the slower patch? I'm a bit confused over this....


---

Comment by gbe created at 2011-01-12 03:44:07

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2011-01-12 09:13:52

Changing status from needs_work to needs_info.


---

Comment by ncohen created at 2011-01-12 09:13:52

Hello Robert !!!

> Can you say more about the difference between the two patches? Why should we merge the slower patch? I'm a bit confused over this....

Of course ! I should have been way more explicit when I replaced the former patch by the new one `^^;`

This patch is about finding a smallest (cardinality) subset of vertices (or edges, but let's just talk about vertices) in a digraph whose removal makes it acyclic. It is solved by a LP in a following way : 
give me the set of vertices you have now, and I will tell you if you did not forget any circuit. If you forgot a circuit, I give it to you (the LP), and you compute again a *smallest set of vertices such that each circuit your know is cut by at least a vertex*.

The LP solver does not know the whole graph. Is just knows a small list of circuits. With this information, it computes a possible set of vertices, and cycles are added if the given set is not sufficient.

So, there are three parts in this method : the first one is a loop doing what I said just above : getting the current solution, checking whether is it acyclic, adding a constraint (the cycle) if it is not. The second one is the LP itself, of course (knowing a list of circuits, find the set -- the hard part), and a routine checking whether the digraph without the vertices returned by the solver is acyclic.

In the first patch, everything was written in Cython. I was worried it wouldn't be as clear as Python, plus it was again defining a function somewhere, this function being called dy digraph.py, and most importantly, I thought it would be easier/faster to review this way `^^;`. Besides, I was redefining a function checking whether the graph is acyclic in a funny way : optimised for my use, while the standard one present in Sage was still using NetworkX. In #10432, the method checking whether the digraph is acyclic has been rewritten in Cython, so even though my version was a tad more optimised for my use, it is still way faster than using NetworkX.

With the new patch, the loop (is this set good?) is in Python, the LP is still solved by C libraries, and the routine checking the solution is in Cython (not so bad) because of #10432. My tricks avoided to make a copy of the graph at each loop, which is clearly nice, but I wondered whether this was reason enough to keep a looong copy of the routine optimised for my needs, and Cython code instead of Python when it is not really needed (this part is not really bad. The only problem is the graph copy).

Considering this version is already infinitely better than what we already have, I thought it would not be so bad to waste a few milliseconds, when the size of the problems we solve now would have made any computer crash out of memory previously.

(patch updated, still being debated) `:-)`

Nathann


---

Attachment

Thanks for explaining Nathann, that greatly clarifies things.


---

Comment by ncohen created at 2011-01-12 21:54:02

Changing status from needs_info to needs_review.


---

Comment by rlm created at 2011-01-16 04:40:50

Ran tests with the following applied:

```
rlmill@geom:/scratch/rlmill/sage-4.6.1.rc0/devel/sage-main$ hg qap
trac_9911.patch
9911_fix.patch
trac_10435.patch
trac_10432.patch
trac_9923-python.patch
```


Looks good!


---

Comment by rlm created at 2011-01-16 04:40:50

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-26 22:26:46

Resolution: fixed
