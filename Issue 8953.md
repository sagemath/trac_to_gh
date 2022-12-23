# Issue 8953: Perfect graph recognition algorithm

Issue created by migration from https://trac.sagemath.org/ticket/8953

Original creator: ncohen

Original creation time: 2010-05-12 01:38:44

Assignee: jason, ncohen, rlm

CC:  rhinton

Costly, but nice enough for small graphs :-)


---

Comment by ncohen created at 2010-05-12 21:56:24

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-05-12 21:56:24

New version dealing with BipartiteGraph graphs. Sorry for the two versions, they are identical ;-)

Nathann


---

Comment by ncohen created at 2010-05-20 20:03:47

Changing priority from major to minor.


---

Comment by rlm created at 2010-06-17 20:48:23

Doctests fail:

```
sage -t  "devel/sage-main/sage/graphs/graph.py"             
**********************************************************************
File "/Users/rlmill/sage-4.4.4.alpha0/devel/sage-main/sage/graphs/graph.py", line 1458:
    sage: g.is_perfect()
Exception raised:
    Traceback (most recent call last):
      File "/Users/rlmill/sage-4.4.4.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.4.4.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.4.4.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_9[5]>", line 1, in <module>
        g.is_perfect()###line 1458:
    sage: g.is_perfect()
      File "/Users/rlmill/sage-4.4.4.alpha0/local/lib/python/site-packages/sage/graphs/graph.py", line 1516, in is_perfect
        counter_example = self.induced_subgraph_search(graphs.CycleGraph(i))
    AttributeError: 'Graph' object has no attribute 'induced_subgraph_search'
**********************************************************************
```

for example. Also, you should explain what a perfect graph is in the docstring, before quoting the theorem.


---

Comment by rlm created at 2010-06-17 20:48:23

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-06-18 10:59:15

Sorryyyyy !! This method has been renamed during the review of the corresponding ticket, and I didn't update this patch... I'll send one in a second !

Nathann


---

Comment by ncohen created at 2010-06-18 10:59:15

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-06-18 14:49:04

Your new patch applies fine (without #8927 even) and passes all doctests in `sage/graphs`. If you approve of the editing changes in my referee's patch, then set this ticket to positive review!


---

Comment by ncohen created at 2010-06-18 15:02:35

Agreed ! :-)

Thanksssssssss !

Nathann


---

Comment by ncohen created at 2010-06-18 15:02:35

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-29 00:00:09

Changing status from positive_review to needs_work.


---

Comment by rlm created at 2010-06-29 00:00:09

After sage-4.5.alpha1 is released, this will lead to a failed doctest:


```
**********************************************************************
File "/scratch/rlmill/release/sage-4.5.alpha1/devel/sage-main/sage/graphs/graph.py", line 1629:
    sage: g.is_perfect()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/rlmill/release/sage-4.5.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/rlmill/release/sage-4.5.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/rlmill/release/sage-4.5.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_11[5]>", line 1, in <module>
        g.is_perfect()###line 1629:
    sage: g.is_perfect()
      File "/scratch/rlmill/release/sage-4.5.alpha1/local/lib/python/site-packages/sage/graphs/graph.py", line 1702, in is_perfect
        counter_example = self.subgraph_search(graphs.CycleGraph(i), induced = True).complement()
    AttributeError: 'NoneType' object has no attribute 'complement'  
**********************************************************************
```



---

Comment by ncohen created at 2010-06-29 07:44:06

1) Sorryyyyyyyyy !!!
2) Fixed :-)

Nathann


---

Comment by ncohen created at 2010-06-29 07:44:06

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-07-18 09:38:34

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-07-19 01:50:37

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-07-19 01:50:37

Hello !!! 

My patch applied fine on sage-4.5, though I just updated it... 

It also contains your modifications :-)

Nathann


---

Attachment

It was probably the other patch causing conflict.


---

Comment by rlm created at 2010-07-19 08:34:02

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-21 02:49:18

Resolution: fixed
