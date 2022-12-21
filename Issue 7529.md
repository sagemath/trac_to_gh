# Issue 7529: Maximum Average Degree of a graph

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-11-25 09:57:52

Assignee: rlm

The maximum average degree of a graph is the maximum, over all subgraphs H of a graph G, of average_degree(H).

This can be computed in polynomial time ( though I do not know of any practical way to do it ) and could be used, for example, as a certificate for negative answers in #7528.

Nathann


---

Comment by ncohen created at 2010-01-28 11:08:47

After some thinking, is was easy to write it through Linear Programming :-)

I also wrote a pretty elementary average_degree function, that I had been missing for some time !

Nathann


---

Comment by ncohen created at 2010-01-28 11:08:47

Changing status from new to needs_review.


---

Attachment


---

Comment by ncohen created at 2010-04-08 21:21:05

For an explanation of the Linear Program used to solve this problem, see the LP chapter from : http://code.google.com/p/graph-theory-algorithms-book/

Nathann


---

Comment by wdj created at 2010-05-12 12:58:22

Changing status from needs_review to positive_review.


---

Comment by wdj created at 2010-05-12 12:58:22

This installs fine on 4.4.2.a0, passes sage -testall both before and after installing glpk (except for unrelated failures).

Also, the docs look good and I tested it on other examples and it works as claimed:


```
sage: g = graphs.RandomGNP(20,.3) 
sage: h = graphs.RandomGNP(20,.2) 
sage: j = g+h
sage: j.density()
49/390
sage: h.density()
3/19
sage: g.density()
34/95
sage: RR(g.density())
0.357894736842105
sage: RR(h.density())
0.157894736842105
sage: j.maximum_average_degree()
34/5
sage: h.average_degree()
3
sage: g.average_degree()
34/5
```



---

Comment by ncohen created at 2010-05-12 14:49:27

Thaaaaaaank you so much !!! The other LP tickets are just applications of the following thing : if a graph has maximum average degree strictly less than 2 ( so 2-epsilon in the code, or 1-epsilon as it is sometimes divided) then it is acyclic -> a forest !!

So this ticket really is they key to all others ! When I found how to solve this one I knew how to write the others, so there shouldn't be any surprise in them :-)

Thank you again !!

Nathann


---

Comment by bascorp2 created at 2010-05-26 08:40:07

[print pictures](http://like-search.info/)


---

Comment by wdj created at 2010-05-26 10:36:19

Replying to [comment:6 bascorp2]:
> [print pictures](http://like-search.info/)

This looks like spam but I didn't try the link.


---

Comment by mhansen created at 2010-06-06 07:11:09

Resolution: fixed
