# Issue 1305: incidence structures

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-11-28 19:50:39

Assignee: mhansen

CC:  sage-combinat

Original from Chris Godsil's wishlist, with reply by Jason Grout and second reply by Robert Miller.


```
>>> (d) Bipartite graphs: We will need to deal with some incidence structures,
>>> and these can be encoded as bipartite graphs. We want to get the point
>>> graphs and line graphs of incidence structures. If we have a procedure to
>>> convert a graph G to an incidence structure of vertices and edges, then
>>> the line graph of the incidence structure is the line graph of G.
>> Do we have a way to represent and work with incidence structures in Sage
>> natively?
> Graphs and codes are implemented, but I don't think designs are.
> Ultimately, there should be an incidence structure class which they
> inherit from etc etc etc. Definitely a wishlist ticket, and likely a
> good coding sprint idea for Sage Days 7.
```



---

Comment by jason created at 2007-11-28 20:21:15

Also from Chris Godsil (hrm, with :


```
>>> It would be very useful to be able to form incidence structures from
>>> differ-
>>> ence sets. Here the input would be a group G and some subsets S_1 , . .
>>> . , S_m ;
>>> the point set of the incidence structure would be G, and the blocks would
>>> be the translates S^g_i for i = 1, . . . , m and g in G. Even just the
>>> case G = Z^d_m
>>> would be a good start.
```



---

Comment by mhansen created at 2008-12-02 10:15:08

Resolution: invalid


---

Comment by mhansen created at 2008-12-02 10:15:08

I think we can close this ticket as it is very vague.  Additionally, there is now a class for incidence structures which can be found at http://www.sagemath.org/hg/sage-main/file/5be1d5ad8339/sage/combinat/designs/incidence_structures.py .
