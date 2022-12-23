# Issue 9350: Python max flow method

Issue created by migration from https://trac.sagemath.org/ticket/9350

Original creator: ncohen

Original creation time: 2010-06-27 10:19:03

Assignee: jason, mvngu, ncohen, rlm

Implementation of a max-flow algorithm which does not use Linear Programming.

I will update it right after #8870 is merged

Nathann


---

Comment by ncohen created at 2010-07-08 12:41:35

Updated, and now needs review :-)


---

Comment by ncohen created at 2010-07-08 12:41:35

Changing status from new to needs_review.


---

Comment by wdj created at 2010-07-29 13:13:40

Changing status from needs_review to needs_info.


---

Comment by wdj created at 2010-07-29 13:13:40

This applies okay to 4.5.2.a1 and seems to pass all tests, except for some unrelated failures. However, there are no examples in edge_cut with vertices=True, eg


```
sage: g = graphs.PetersenGraph()
sage: g.edge_cut(0, 3, method="FF", vertices=True)
[3, [(0, 1, None), (0, 4, None), (0, 5, None)], [[0], [1, 2, 3, 4, 5, 6, 7, 8, 9]]]
```

Why is this?


---

Comment by ncohen created at 2010-07-29 14:08:37

> Why is this?
 
What do you think of line 3652 of the generic_graph.py file ? `:-)`


```
sage: value,edges,[set1,set2] = g.edge_cut(0, 14, use_edge_labels=True, vertices=True) 
```


Nathann


---

Comment by wdj created at 2010-07-29 16:48:12

Replying to [comment:4 ncohen]:
> > Why is this?
>  
> What do you think of line 3652 of the generic_graph.py file ? `:-)`
> 
> {{{
> sage: value,edges,[set1,set2] = g.edge_cut(0, 14, use_edge_labels=True, vertices=True) 
> }}}
> 
> Nathann

The value isn't returned, so the potential user cannot see examples of how the output changes for different choices of the input. I'm just wondering if there was a good reason for omitting the edges in the output. An example with value_only=False would be equally nice. Finally, to be extremely picky, the description


```
``vertices`` -- boolean (default: ``False``). When set to ``True``,
          also returns the two sets of vertices that are disconnected by
          the cut. Implies ``value_only=False``.
```

should probably read

```
``vertices`` -- boolean (default: ``False``). When set to ``True``,
          returns a list of edges in the edge cut and the two 
          sets of vertices that are disconnected by the cut. 
          Note: ``vertices=True`` implies ``value_only=False``.
```


Does this seem reasonable?


---

Attachment


---

Comment by ncohen created at 2010-07-29 17:04:06

It does ! I just updated the patch with you example and the corrected docstring `:-)`

There was, indeed, a reason for never showing directly the output of all these methods : it formerly used Linear Programming, and the results of LP, eve though correct, can vary depending on the time of the day and the solver used. So showing it is asking for trouble, though one can perfectly check some relations... But this Python implementation being deterministic, it's fine now !

Nathann


---

Comment by ncohen created at 2010-07-29 17:04:06

Changing status from needs_info to needs_review.


---

Comment by wdj created at 2010-07-29 22:52:41

Replying to [comment:6 ncohen]:
> It does ! I just updated the patch with you example and the corrected docstring `:-)`
> 
> There was, indeed, a reason for never showing directly the output of all these 
> methods : it formerly used Linear Programming, and the results of LP, even 
> though correct, can vary depending on the time of the day and the solver used. 
> So showing it is asking for trouble, though one can perfectly check some 
> relations... But this Python implementation being deterministic, it's fine now !
> 
> Nathann

Excellent. Passed tested for me (except for unrelated doctest failures on a mac 10.6.4).

Thanks Nathann!!


---

Comment by dimpase created at 2010-09-04 05:57:26

Changing status from needs_review to positive_review.


---

Comment by dimpase created at 2010-09-04 05:57:26

I also tested this, and it looks OK. 
Wdj, have you forgotten to give it positive review?

Dima


---

Comment by ncohen created at 2010-09-04 06:23:10

Thanksssss ! :-)


---

Comment by mpatel created at 2010-09-15 22:29:15

Please remember to fill in the "Author(s)" and "Reviewer(s)" fields.


---

Comment by mpatel created at 2010-09-15 22:52:26

Resolution: fixed
