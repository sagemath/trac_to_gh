# Issue 6962: [with patch, needs review] Feedback vertex set, Feedback arc set

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-09-19 18:45:45

Assignee: rlm

Adds the functions :
* DiGraph.feedback_arc_set
* DiGraph.feedback_vertex_set

You will find a full description of the problem in the docstrings, or there :
* http://en.wikipedia.org/wiki/Feedback_vertex_set
* http://en.wikipedia.org/wiki/Feedback_arc_set

The functions use Linear Programming, which needs one of the two optional packages GLPK 
{{{ 
sage: install_package('cbc')
}}}
or CBC 

```
sage: install_package('glpk') 
```

installed. You will find a helpful documentation about the construction of the Linear Program in the docstring.

One of the docstrings uses the function min_vertex_cover from #6680.

Nathann


---

Comment by jason created at 2009-09-20 06:05:01

We've used the terminology "edge" with a DiGraph, with the understanding that direction matters when you have a DiGraph.  Is it a possibility to change "feedback_arc_set" to "feedback_edge_set"?


---

Comment by ncohen created at 2009-09-20 07:32:06

I mix them up myself sometimes, this distinction can almost always be deduced from the context, even outside of Sage... And anyway the word "feedback" is enough for anybody interested in the function to read its documentation, so I think it is OK. We can write "feedback arc set" in the documentation in case someones looks for this special string, besides !

The thing is that I will be going for one week in something like 10 minutes and will not have any access to any computer during this time. Could a reviewer fix this while reviewing the whole patch ? If this patch is not reviewed when I get back, I will do it myself, though... And I will remember that you already settled this question :-)

Nathann


---

Comment by ncohen created at 2009-09-29 11:55:52

Done ! :-)

( the patch now is written according to the changes brought to class MIP in #7012 )


---

Comment by rlm created at 2009-12-15 16:49:02

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2009-12-15 16:49:02

This patch still applies ok, but none of the doctests work:

```
sage: cycle=graphs.CycleGraph(5)
sage: dcycle=DiGraph(cycle)
sage: cycle.size()
5
sage: dcycle.feedback_edge_set(value_only=True)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/rlmill/.sage/temp/rlm_book.local/96266/_Users_rlmill__sage_init_sage_0.py in <module>()

/Users/rlmill/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/graphs/graph.pyc in feedback_edge_set(self, value_only)
  12540         from sage.numerical.mip import MixedIntegerLinearProgram
  12541         
> 12542         p=MixedIntegerLinearProgram(sense=-1)
  12543         
  12544         b=p.new_variable()

/Users/rlmill/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/numerical/mip.so in sage.numerical.mip.MixedIntegerLinearProgram.__init__ (sage/numerical/mip.c:866)()

TypeError: __init__() got an unexpected keyword argument 'sense'
sage: cycle.min_vertex_cover()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/Users/rlmill/.sage/temp/rlm_book.local/96266/_Users_rlmill__sage_init_sage_0.py in <module>()

AttributeError: 'Graph' object has no attribute 'min_vertex_cover'
sage: dcycle.feedback_vertex_set(value_only=True)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/rlmill/.sage/temp/rlm_book.local/96266/_Users_rlmill__sage_init_sage_0.py in <module>()

/Users/rlmill/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/graphs/graph.pyc in feedback_vertex_set(self, value_only)
  12632         from sage.numerical.mip import MixedIntegerLinearProgram
  12633         
> 12634         p=MixedIntegerLinearProgram(sense=-1)
  12635         
  12636         b=p.new_variable()

/Users/rlmill/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/numerical/mip.so in sage.numerical.mip.MixedIntegerLinearProgram.__init__ (sage/numerical/mip.c:866)()

TypeError: __init__() got an unexpected keyword argument 'sense'
```


There are two issues:

1. `__init__() got an unexpected keyword argument 'sense'`

2. `'Graph' object has no attribute 'min_vertex_cover'`


---

Comment by ncohen created at 2009-12-16 11:36:54

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2009-12-16 11:37:22

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2009-12-17 13:06:40

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2009-12-17 13:06:40

Updated !


---

Attachment


---

Comment by rlm created at 2009-12-17 21:51:33

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-19 20:06:08

Resolution: fixed
