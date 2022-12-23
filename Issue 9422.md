# Issue 9422: Slightly improving is_forest

Issue created by migration from https://trac.sagemath.org/ticket/9422

Original creator: ncohen

Original creation time: 2010-07-04 11:45:46

Assignee: jason, ncohen, rlm

CC:  rlm mvngu

As it is implemented at the moment, the method is_forest creates a new graph for each connected component of the graph, then calls the is_tree method for each of them, which checks again that the connected components are....connected !

We can do it a bit faster :-)

Nathann


---

Attachment


---

Comment by ncohen created at 2010-07-04 11:46:59

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-07-04 11:55:54

Creating a large forest : 


```
g = graphs.RandomGNP(300,.1)
g = g.subgraph(edges=g.min_spanning_tree())
g.delete_edges([e for e in g.edges() if random()<.5])
sage: g.sparse6_string()
':~?Ck_O?gF?MAo?_??W@_AC?D`G?oE_I@GU?EE??`s@GCa??gb?[CWQa[BW?ak?wp@AEGt?m@GE_IM_?_A?g?`Y@WA_aOoAcSDHH?QAgGc{CwI`AEgPdS?HW?QCWC_IVOCeCCXc@yAW@e_Axn?U[_DfOAhu?M]?\\fgDX}@y_??`e?Ga_m`o?ggIG@`EGGY_AcOBhK?IT?Ye?I_uAGNhwCwRiC?WGiO?Yf?A?g?ikEIl?]AGAjC@Ir@alOJ_YAwJ_AAGAk?AgF_I?W@\
kW?g@kk@JL?QroN_A?zX?U?WFlw@WAmG@GD`q@Zf?M{?G_y{oa_Q|oO_E~?IoC@KGBfA_@osEw@p??wF_BD?L_rE_?poCk]?NGoCqW?[h?aAWE'
```


Then using two different versions of is_forest 


```
sage: %timeit g.is_forest()
125 loops, best of 3: 5.06 ms per loop

sage: %timeit g.is_forest()
5 loops, best of 3: 43.8 ms per loop
```


Short and useful... All I love ! :-)

Nathann


---

Comment by mpatel created at 2010-10-05 21:51:13

See [comment:ticket:9925:20 comment 20ff] at #9925 for a flaky doctest that #9422 and #10067 should fix.


---

Comment by mpatel created at 2010-10-06 04:28:13

Replying to [comment:3 mpatel]:
> See [comment:ticket:9925:20 comment 20ff] at #9925 for a flaky doctest that #9422 and #10067 should fix.

I've opened #10081 for this failure.


---

Comment by lsampaio created at 2010-10-12 08:15:52

"Short and useful..." 
... and quite easy to review :P


---

Comment by lsampaio created at 2010-10-12 08:15:52

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-10-12 08:18:12

Thanks !!!

Nathann


---

Comment by mpatel created at 2010-10-21 08:31:16

Resolution: fixed
