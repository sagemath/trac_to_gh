# Issue 7600: Vertex cover

Issue created by migration from https://trac.sagemath.org/ticket/7600

Original creator: ncohen

Original creation time: 2009-12-04 07:49:59

Assignee: rlm

CC:  kevin.stueve

As the title says, this patch implements Graph.vertex_cover.


---

Comment by ncohen created at 2009-12-04 07:51:14

Changing status from new to needs_review.


---

Comment by kevin.stueve created at 2009-12-09 04:48:31

I've never reviewed a patch before.

We were just talking about vertex cover in my algorithms class the other day.

The three problems:


1) Does G have a clique of size m or more?


2) Is there a vertex cover of size m or less for G?


3) Does G contain an independent set of size m or more?



are all polynomially reducible to each other.

exercise 9, p 403, The Design and Analysis of Algorithms, 2nd Edition

I'm not aware if those other problems are implemented in Sage.  If not, maybe a ticket should be created.

3048	          As vertex cover is a `NP`-complete problem

IMO, would be better with the word "an" in place of "a".

Kevin Stueve


---

Comment by ncohen created at 2009-12-09 08:11:14

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2009-12-09 08:11:14

Hello !!!!

You are right, these three are reducible to each other ! Actually, Sage already has an algorithm for 1) and 3) through Cliquer, which is way more efficient that LinearProgramming... I will immediately add several lines to the patch to let it use Cliquer by default, and use LP if the users wants it ( and this way we can control the respective values of the two algorithms ) :-)

Thank you very much for your remark, this should speed up the algorithm amazingly ! :-)

Nathann


---

Comment by ncohen created at 2009-12-09 08:33:35

Done ! Thank you very much for your help ! :-)
Besides, as the algorithm Cliquer does not require GLPK or CBC, there is a way for everybody to compute a vertex cover now :-)

Nathann


---

Comment by ncohen created at 2009-12-09 08:33:35

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2009-12-15 17:52:38

oops:

```
sage: vc2 = g.vertex_cover(algorithm="Cliquer")
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)

/Users/rlmill/.sage/temp/rlm_book.local/98560/_Users_rlmill__sage_init_sage_0.py in <module>()

/Users/rlmill/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/graphs/graph.pyc in vertex_cover(self, algorithm, value_only, log)
   3325                 return self.order()-len(independent)
   3326             else:
-> 3327                 return set(g.vertices()).difference(set(independent))
   3328 
   3329         elif algorithm=="MILP":

UnboundLocalError: local variable 'g' referenced before assignment
```



---

Comment by rlm created at 2009-12-15 17:52:38

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by ncohen created at 2009-12-16 01:27:26

fixed !


---

Comment by ncohen created at 2009-12-16 01:27:26

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2009-12-16 03:26:24

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-19 19:59:11

Resolution: fixed
