# Issue 7304: [With patch, needs review] Contract edge in graph

Issue created by migration from Trac.

Original creator: AJonsson

Original creation time: 2009-10-25 20:04:34

Assignee: rlm

CC:  brunellus lkeough dcoudert tscrim stefan yomcat

This patch contract an edge (u,v) in a graph. In the resulting graph vertex u is merged into vertex v.

The variables u and v can be passed as variables, a tuple (u,v) or a 3-tuple (u,v,'label'). The last allows us to use an element from G.edges() for contraction.


---

Attachment

Initial patch for review


---

Comment by AJonsson created at 2009-10-25 20:12:56

Changing type from defect to enhancement.


---

Comment by AJonsson created at 2009-10-25 20:12:56

Changing status from new to needs_review.


---

Comment by AJonsson created at 2009-10-25 21:05:23

Resolution: duplicate


---

Comment by AJonsson created at 2009-10-25 21:05:23

Duplicate of #7159 . That ticket is about vertex merging, but it is basically the same thing.


---

Comment by AJonsson created at 2009-10-27 18:19:01

Resolution changed from duplicate to 


---

Comment by AJonsson created at 2009-10-27 18:19:01

On second thought, reopening.

Merging vertices gives a slightly different result for certain cases that are important in deletion-contraction algorithms, so this function has a place to fill as well.

Example of case that contract_edge() handles differently:

If we have two vertices A, B, with two parallel edges between them, a merging of A and B results in a single vertex with no edge or loops. If we instead choose to contract one of the two parallel edges (and allow loops), we will end up with a single vertex which has a loop.


---

Comment by AJonsson created at 2009-10-27 18:19:01

Changing status from closed to new.


---

Comment by AJonsson created at 2009-10-27 18:19:19

Changing status from new to needs_review.


---

Comment by mvngu created at 2009-10-28 12:30:08

Replying to [comment:2 AJonsson]:
> Duplicate of #7159 . That ticket is about vertex merging, but it is basically the same thing.
Anders, please don't close tickets. That's the job of the release manager. See [this section](http://www.sagemath.org/doc/developer/trac.html#closing-tickets) of the Developer's Guide for conventions on closing tickets.


---

Comment by AJonsson created at 2009-10-28 19:43:56

Replying to [comment:6 mvngu]:
> Anders, please don't close tickets. That's the job of the release manager. See [this section](http://www.sagemath.org/doc/developer/trac.html#closing-tickets) of the Developer's Guide for conventions on closing tickets.

Whoops. Hadn't seen that section. Won't happen again.


---

Comment by ncohen created at 2009-10-31 20:39:25

I understand your point, but do you think it useful to have 2 different functions to merge vertices, instead of having just one with more options ? It could be a bit confusing...

Nathann


---

Comment by ncohen created at 2009-10-31 20:39:32

Changing status from needs_review to needs_info.


---

Comment by AJonsson created at 2009-11-01 09:52:01

Replying to [comment:8 ncohen]:
> I understand your point, but do you think it useful to have 2 different functions to merge vertices, instead of having just one with more options ? It could be a bit confusing...
> 
> Nathann

I don't feel too strongly about it. As long as full functionality exists, it matters little to me if it is in one or two functions.


---

Comment by ncohen created at 2009-11-01 09:57:18

My advice exactly ! 

Could you then write a patch to modify #7159 as soon as it will be merged ? You could also directly modify the trac ticket as it is not merged yet, but then we would be looking for someone else to review it, as for #7814...

As you said, I do not mind as long as the two behaviours exist.. If you think your version of merging should be the default one, it's up to you ! :-)


---

Comment by AJonsson created at 2009-11-01 10:06:54

Ok, will look closer into a modification of #7159 to be added after that ticket has been merged to Sage.


---

Comment by AJonsson created at 2009-11-01 10:06:54

Changing status from needs_info to needs_work.


---

Comment by ncohen created at 2009-12-05 09:05:17

should we keep this ticket open, or close it and open a new one with your modification of #7159 ?


---

Comment by AJonsson created at 2009-12-07 00:28:06

Replying to [comment:13 ncohen]:
> should we keep this ticket open, or close it and open a new one with your modification of #7159 ?

Let's keep it open, otherwise we would just open an almost identical ticket. I will see if I get the time to finish the function sometime next week.


---

Comment by bascorp created at 2010-04-30 14:33:13

[куплю мобильный телефон](http://forum.mobile-shop.kiev.ua/)


---

Comment by Stefan created at 2011-04-11 15:03:04

There's a spam link above here that needs removing.

As a matroid theorist, I look at deletion and contraction a bit differently. It bothers me that I cannot write something along the lines of

H = G.delete((1,2)).contract([(3,5),(6,7)])

without modifying G.


---

Comment by ncohen created at 2011-04-11 15:18:46

What would your code do ? Are your pairs edges or vertices ? Right now your have a merge_vertices commands in Graph that lets you contract any set of vertices.

Nathann


---

Comment by Stefan created at 2011-04-11 19:19:26

My pairs would be edges. In an even more ideal world, I would refer to them by their labels. For comparison, if M is a matroid with elements 'e', 'f', 'g', I currently have some experimental code allowing me to write

N = M / ['e'] \ ['f', 'g']

resulting in the matroid with e contracted and f,g deleted. From a matroid-theoretic point of view, if you contract an edge, all edges parallel to it should turn into loops. The current merge_vertices doesn't do that, even if I call G.allow_loops(True) first. With this behavior, contracting a loop should probably equal deleting a loop.

Anyway, my main point is that I feel there should be methods for deletion and contraction that return a new graph, rather than modifying the graph itself.

Real use case: the other day I was wondering about maximal planar subgraphs of a small graph G. In that case you want to explore: first delete edge 'e', then delete edge 'f', then 'f' and 'g', then 'f' and 'h', and finally only edge 'h'. The current implementation makes such exploration of minors a bit cumbersome: you frequently make copies of G, which you then modify.


---

Comment by ncohen created at 2011-04-12 19:08:57

> Anyway, my main point is that I feel there should be methods for deletion and contraction that return a new graph, rather than modifying the graph itself.

Would you be interested in mixing the two ? Like sometimes calling a delete_edge function which returns a graph, and some other times a method which modifies the graph ?

The current behaviour is necessary for many functions, and replacing it would mean a huge loss in efficiency. It is possible to add a keyword to all those methods so that a graph will be returned instead of modifying the current graph. I don't quite like this, as it would mean some additional tests for each of all those very fundamental functions, but then again...
On the other hand, if you are not interested in mixing the two type of operations, perhaps the best is to work on an immutable graph class. Many people have asked this already, and when working on an immutable graph class having a default behaviour of "returning an immutable copy of the graph modified as requested" does not seem too unnatural. What about this then ? `:-)`

Nathann


---

Comment by Stefan created at 2011-04-19 15:06:38

I'm not at all in favor of having two different behaviors encoded in one function. One option would be to implement the __div__ and _backslash_ operators to do, respectively, contraction and deletion without changing the object.


---

Comment by ncohen created at 2011-04-19 15:09:53

> I'm not at all in favor of having two different behaviors encoded in one function. One option would be to implement the __div__ and _backslash_ operators to do, respectively, contraction and deletion without changing the object.

Got it !

This being said, I understand that's how matroid theory is written "on the paper", but do you think it would be possible to write useful code using only those symbols when any of them means copying the whole structure ? But perhaps I do not know how you intend to code it, and how much such operations could cost in memory and time ...

Nathann


---

Comment by rlm created at 2011-04-19 18:18:11

Replying to [comment:20 Stefan]:
> I'm not at all in favor of having two different behaviors encoded in one function.

This is often the case. For example many graph functions in Sage have an `inplace` option, which provides exactly this choice.


---

Comment by Stefan created at 2011-04-20 07:30:14

Replying to [comment:22 rlm]:
> Replying to [comment:20 Stefan]:
> > I'm not at all in favor of having two different behaviors encoded in one function.
> 
> This is often the case. For example many graph functions in Sage have an `inplace` option, which provides exactly this choice.

Indeed it does! I'm not sure that this happens often, but so far I found subgraph() and relabel(). The former defaults to inplace=False; the latter defaults to inplace=True.

In that case it would be preferable not to have extra methods (the list is quite long enough as it stands). Defining the forward and backslashes might still be a neat addition.

Nathann, typical work with matroids is on relatively small ground sets. I don't expect intensive calculations on graphs with more than, say, a few dozen edges. We would wrap the graph in a GraphicMatroid object anyway, so it's easy to compensate for any functionality in the graph code that is not entirely fit for our purpose. So you need not worry about our needs for the time being.

What remains is the question of contracting one edge from a parallel pair (see above).


---

Comment by brunellus created at 2012-01-31 14:48:16

So, what do you say to my patch? It provides

 1. loops handling (see #9807)
 1. ``contract_edge`` option
 1. ``inplace`` option


---

Comment by brunellus created at 2012-01-31 14:48:16

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2012-03-10 13:00:31

Apply trac_7304_contract_edge.patch

(for patchbot)


---

Comment by boothby created at 2012-03-21 20:48:35

Brunellus,

This isn't quite there, and you haven't tested everything.

Graphs have a copy method -- `g = g.copy()` is faster than `g=copy(g)`.  There are two problems with the block


```
        if vertices and vertices[0] is None: 
	    vertices[0] = g.add_vertex()
```


first off, this assumes that `g.add_vertex()` returns the label of the added vertex.  It does not.  Second, it modifies `vertices` for no good reason (what if the users passes in a tuple, set, or generator?)


---

Comment by boothby created at 2012-03-21 21:07:52

Changing status from needs_review to needs_work.


---

Comment by boothby created at 2012-03-21 22:21:21

Ah, I see that g.add_vertex() indeed returns the label for the current alpha of 5.0.  Please update this to not modify the users's input with


```
    vertices = list(vertices)
```


and use `g.copy()` instead of copy, and I'll give this a positive review.


---

Comment by brunellus created at 2012-05-16 09:00:02

Thanks for the review! I will update the patch right now.


---

Attachment


---

Comment by brunellus created at 2012-05-16 10:35:17

Changing status from needs_work to needs_review.


---

Comment by lkeough created at 2012-07-15 21:25:42

I have been working on getting the Tutte polynomial into Sage (#1314).  The Tutte polynomial needs contraction with keeping any resulting multiedges and loops (but removing the edge you contracted).  It seems your code does this if you allow multiedges and loops and use the contract_edge feature.

I think they may have had this discussion above, but I can't tell what was concluded:  Would adding an option like "simplegraph = True" be a reasonable thing to do?


---

Comment by jdemeyer created at 2012-07-27 20:43:02

Please fill in your real name as Author.


---

Comment by ncohen created at 2012-11-26 10:32:39

Changing status from needs_review to needs_info.


---

Comment by ncohen created at 2012-11-26 10:32:39

Ok.... Which is the patch that needs to be reviewed ? Is it [attachment:trac_7304_contract_edge.patch] ?

Nathann


---

Comment by zgershkoff created at 2017-06-22 00:58:28

Changing status from needs_info to needs_review.


---

Comment by zgershkoff created at 2017-06-22 00:58:28

I ended up writing some new methods for edge contraction. I didn't use either patch here. The first one didn't seem to respect edge labels, and `allow_loops_multiedges` seems redundant since these are intrinsic to the graph, and the second one seemed too complicated to disentangle from `merge_vertices`. I also didn't include an `inplace` option for consistency with `delete_edge`.

The `contract_edges()` method was tough because if the user inputs a list of edges, the vertices need to be updated dynamically as the contractions occur and vertices are lost. I ended up using nested while loops to accomplish this. Maybe there's a faster way?
----
New commits:


---

Comment by git created at 2017-06-22 00:59:53

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-06-22 01:31:39

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-06-22 01:33:13

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by zgershkoff created at 2017-06-22 01:59:18

Let's wait until I speed up `contract_edges()`.


---

Comment by zgershkoff created at 2017-06-22 01:59:18

Changing status from needs_review to needs_work.


---

Comment by git created at 2017-06-22 05:22:03

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-06-22 17:02:48

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by zgershkoff created at 2017-06-22 17:06:23

Changing status from needs_work to needs_review.


---

Comment by zgershkoff created at 2017-06-22 17:06:23

For the sake of not having two implementations for the same thing, I adapted brunellus's earlier patch and rewrote `contract_edge()` to use `merge_vertices()`. This depends on #23290 to resolve a defect in `merge_vertices()`.


---

Comment by git created at 2017-06-23 07:02:44

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by dcoudert created at 2017-06-23 08:25:15

Some comments for `contract_edges`:
* instead of dropping non-edges, it is better to not add such edge to the list
* construct the list of vertices at the same time to add edges to the list
* Instead of implementing your own disjoint set methods, you can use `DisjointSet`
* If you use `DS = DisjointSet(...)`, you can use `DS.root_to_elements_dict()` instead of `vertices = [v for v in vertices if v!= destination[v]]`


---

Comment by git created at 2017-06-25 18:52:27

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by zgershkoff created at 2017-06-25 18:57:32

Replying to [comment:52 dcoudert]:
> Some comments for `contract_edges`:
> * instead of dropping non-edges, it is better to not add such edge to the list
> * construct the list of vertices at the same time to add edges to the list
Done.
> * Instead of implementing your own disjoint set methods, you can use `DisjointSet`
> * If you use `DS = DisjointSet(...)`, you can use `DS.root_to_elements_dict()` instead of `vertices = [v for v in vertices if v!= destination[v]]`
It's nice that sage already has an implementation of this algorithm, but I find it lacking. If I want a list of non-roots, I can do `vertices = [v for v in vertices if (v not in DS.root_to_elements_dict() )]`, but there doesn't seem to be an analog to my `root()` method. So at the end, when I need to know what the root of a vertex is, I don't see any easy way to do that if I'm using `DisjointSet`.


---

Comment by zgershkoff created at 2017-06-25 19:01:57

There's another issue I've been considering: if a user has loops on but multiedges off, then iterated contraction with `contract_edge()` will never create loops, but giving the same input as a list to `contract_edges()` could create loops because it will bypass when the edges are in parallel. On one hand, it seems like it should be consistent, but on the other hand, if a user has loops on and multiedges off, I don't know what business they have contracting edges, so I don't know what their desired output would be.


---

Comment by dcoudert created at 2017-06-25 19:06:38

> It's nice that sage already has an implementation of this algorithm, but I find it lacking. If I want a list of non-roots, I can do `vertices = [v for v in vertices if (v not in DS.root_to_elements_dict() )]`, but there doesn't seem to be an analog to my `root()` method. So at the end, when I need to know what the root of a vertex is, I don't see any easy way to do that if I'm using `DisjointSet`.

`vertices = [v for v in vertices if v != DS.find(v)]` should give you non-roots, no?


---

Comment by git created at 2017-06-25 19:22:09

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by zgershkoff created at 2017-06-25 19:22:38

Ah, right. I misread the description of that method.


---

Comment by dcoudert created at 2017-06-26 06:40:20

Replying to [comment:55 zgershkoff]:
> There's another issue I've been considering: if a user has loops on but multiedges off, then iterated contraction with `contract_edge()` will never create loops, but giving the same input as a list to `contract_edges()` could create loops because it will bypass when the edges are in parallel. On one hand, it seems like it should be consistent, but on the other hand, if a user has loops on and multiedges off, I don't know what business they have contracting edges, so I don't know what their desired output would be.

This is the main difficulty with such method: what's the good answer? what is the user expected ? It is really application dependent. For instance, in some cases you want to contract an edge unless it creates a loop.\\
I would say that as long as the behavior is clearly documented, it's fine. If the user wants something else, he can code his own method.

 

One remark. You could use `edges_incident.extend( self.outgoing_edges(v) )` instead of `out_edges=self.edge_boundary([v])`. You can also use `self.incoming_edges(v)`.


---

Comment by zgershkoff created at 2017-06-26 20:48:21

Thanks for the comments. I think if I use both `self.incoming_edges(v)` and `self.outgoing_edges(v)` then I will get loops on `v` twice, so I'm leaving `out_edges=self.edge_boundary([v])` as it is, but I will extend `edges_incident` by `self.incoming_edges(v)`.


---

Comment by git created at 2017-06-26 21:33:11

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-06-26 21:34:20

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by dcoudert created at 2017-06-27 06:46:12

Another round of comments. 

In method `contract_edge`
- in the `INPUT` block, some lines are for `contract_edges` and so should be removed from here.
- remove the `OUTPUT` block. It is useless here
- If I call `G.contract_edge( (u, v) )` and that the graph has edge `(u, v, 'label')`, then the method will do nothing. Is this the behavior you expect? If so, it should be documented.
- you may replace `for e in self.edges_incident(v):` with `for x,y,l in self.edges_incident(v):`. I don't know which option is the best.

In method `contract_edges`:
- The first line is too long. Usually, the first line is short, and followed with a longer description
- Again the `OUTPUT` block is useless
- in the `TESTS` block, you have an indentation problem
- If we pass a list of 2-tuples but that all edges of the graph have non `None` labels, nothing will happen. If it's expected behavior, it should be documented
- after the `for e in edges:` loop, you should add a termination test like `if not edge_list: return` or `if not edge_list or not vertices: return`
- `out_edges=self.edge_boundary([v])` -> `out_edges = self.edge_boundary([v])`
- `edges_incident = edges_incident + self.edges_incident(v)` -> `edges_incident.extend(self.edges_incident(v))`
- `for (u, v, label) in edges_incident:` -> `for u, v, label in edges_incident:`.


---

Comment by zgershkoff created at 2017-06-27 20:11:44

Replying to [comment:63 dcoudert]:
> Another round of comments. 
> 
> In method `contract_edge`
> - in the `INPUT` block, some lines are for `contract_edges` and so should be removed from here.
> - remove the `OUTPUT` block. It is useless here
> - If I call `G.contract_edge( (u, v) )` and that the graph has edge `(u, v, 'label')`, then the method will do nothing. Is this the behavior you expect? If so, it should be documented.

I can't reproduce this. `self.has_edge(u,v)` works the same as `self.has_edge(u,v,None)`. It seems though the last edge it has in memory between `u` and `v` gets contracted.

```
sage: edgelist = [(0,1,0), (0,1,9), (0,1,2), (0,2,2), (1,2,3)]
sage: G = Graph(edgelist, loops=True, multiedges=True)
sage: G.contract_edge(0,1); G.edges()
[(0, 0, 0), (0, 0, 9), (0, 2, 2), (0, 2, 3)]
sage: edgelist = [(0,1,0), (0,1,2), (0,1,9), (0,2,2), (1,2,3)]
sage: G = Graph(edgelist, loops=True, multiedges=True)
sage: G.contract_edge(0,1); G.edges()
[(0, 0, 0), (0, 0, 2), (0, 2, 2), (0, 2, 3)]
```


> - you may replace `for e in self.edges_incident(v):` with `for x,y,l in self.edges_incident(v):`. I don't know which option is the best.

I changed it to `x,y,l` for consistency.

Why is `x,y,l` preferred over `(x,y,l)`? I don't see anything about this in PEP8, but I've been using the parentheses around the tuple a lot because I think it's easier to read that way.


---

Comment by git created at 2017-06-27 20:31:51

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by zgershkoff created at 2017-06-27 20:48:41

I have a few more questions.

- Is `return` preferred over `return None`? I've changed them to just `return`.
- Where is the indentation error in `contract_edges()`? Is it the space in front of some of the edges in the output? That matches the output, and it makes the html display correctly.
- I've noticed that there are problems for `contract_edges()` if the input is a mix of 2-tuples and 3-tuples as the example below shows, but this is kind of a GIGO situation and I don't know if I should bother addressing it.


```
sage: edgelist = [(0,1,0), (0,1,1), (0,1,2)]
sage: G = Graph(edgelist, loops=True, multiedges=True)
sage: G.contract_edges([(0,1,2), (0,1)]); G.edges()
[(0, 0, 0)]
sage: G = Graph(edgelist, loops=True, multiedges=True)
sage: G.contract_edges([(0,1), (0,1,2)]); G.edges()
[(0, 0, 0), (0, 0, 1)]
```



---

Comment by git created at 2017-06-27 21:01:51

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by dcoudert created at 2017-06-28 07:15:10

Something has changed in the tests for method `contract_edge`. Now we are loosing loops. I don't know why

```
sage: edgelist = [(0,0,'a'), (0,1,'b'), (1,1,'c')]
sage: G = Graph(edgelist, loops=True, multiedges=True)
sage: G.contract_edge(0,1,'b'); G.edges()
[(0, 0, 'a')]
sage: D = DiGraph(edgelist, loops=True, multiedges=True)
sage: D.contract_edge(0,1,'b'); D.edges()
[(0, 0, 'a')]
```


In `contract_edges`:
*`if not edges:` -> `if not edge_list:`
* indentation of tests `With loops in a digraph::`


---

Comment by zgershkoff created at 2017-06-28 07:42:57

Replying to [comment:68 dcoudert]:
> Something has changed in the tests for method `contract_edge`. Now we are loosing loops. I don't know why

I think I put those tests in before I rewrote `contract_edge` to use `merge_vertices`. Maybe it's irrelevant to have those tests there now. Now that uses `merge_vertices`, it's dependent on #23290 to keep the loops. I should have been clearer about that, sorry.

> In `contract_edges`:
> *`if not edges:` -> `if not edge_list:`
> * indentation of tests `With loops in a digraph::`

Yes, I see it now. I'll fix those shortly.


---

Comment by git created at 2017-06-28 17:58:39

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by zgershkoff created at 2017-06-28 18:00:52

I took the liberty of moving #23290 into this since it's closed. All tests pass now.


---

Comment by dcoudert created at 2017-06-28 20:13:03

Right, better to rebase on top of #23290.

In method `contract_edge`, I suggest the following change. Do you agree ?

```
       if self.allows_loops() and (not self.has_edge(u, u) or self.allows_multiple_edges()):
           # add loops
           for (x, y, l) in self.edges_incident(v):
               if set([x, y]) == set([u, v]):
                   self.add_edge(u, u, l)
```


In method `contract_edges`
- the test `if len(set([len(e) for e in edges])) > 1:` is fun ;)
- `if self.has_edge((u, v, label)):` -> `if self.has_edge(u, v, label):`. This is to avoid guessing the format in method `has_edge`.


---

Comment by zgershkoff created at 2017-06-28 20:51:43

Replying to [comment:72 dcoudert]:
> Right, better to rebase on top of #23290.
> 
> In method `contract_edge`, I suggest the following change. Do you agree ?
> {{{
>        if self.allows_loops() and (not self.has_edge(u, u) or self.allows_multiple_edges()):
>            # add loops
>            for (x, y, l) in self.edges_incident(v):
>                if set([x, y]) == set([u, v]):
>                    self.add_edge(u, u, l)
> }}}
I think sage will fail silently if multiedges are off, but it makes sense in principle to check first. I changed the order of the tests because I figured checking a boolean with `self.allows_multiple_edges()` is probably faster than looking for an edge.
> In method `contract_edges`
> - the test `if len(set([len(e) for e in edges])) > 1:` is fun ;)
> - `if self.has_edge((u, v, label)):` -> `if self.has_edge(u, v, label):`. This is to avoid guessing the format in method `has_edge`.
That also makes sense.


---

Comment by git created at 2017-06-28 20:52:05

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by zgershkoff created at 2017-06-29 04:30:08

It occurs to me that in `contract_edge`, loops will never be created unless there are already multiedges. Thus we only need to check if multiedges are allowed once when adding loops.


---

Comment by zgershkoff created at 2017-06-29 04:44:11

Nevermind. A digraph can have two arcs in different directions between a pair of vertices and still have multiedges disabled, so contraction can create a loop. I suppose it's better like it is, since if there's already a loop at `u`, it will always be kept with its original label now.


---

Comment by dcoudert created at 2017-06-29 11:12:26

The patch looks good to me, but I'm wondering if we have taken all cases into account (functionality and/or tests)


---

Comment by git created at 2017-06-29 23:26:31

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-06-29 23:34:36

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by zgershkoff created at 2017-06-29 23:36:15

I added tests for labeled edges, and for attempting to contract non-edges. I think that covers it.


---

Comment by dcoudert created at 2017-07-01 19:59:53

Final comments (sorry for that).

For method `contract_edge`:
- at the top of the `generic_graph.py` file, could you ensure that the description of `contract_edge` is the same as in the method. I propose to put: `Contract an edge from `u` to `v``. Note that I use `Contract` and not `Contracts`.
- Then in the method, split the first line to `Contract an edge from `u` to `v`` and then have a next paragraph with `This method returns silently if the edge does not exist.`

For method `contract_edges`:
- at the top of the `generic_graph.py` file, for `contract_edges`: use `Contract` instead of `Contracts`
- improve the alignment of paragraph `If `e` is an edge that is...`
- In the `INPUT` block, `- ``edges`` - a list...` -> `- ``edges`` -- a list...`. You will certainly have to put the last word (edges) on the next line to be in 80 columns format.
- In the `TESTS:` block, just before `With loops in a digraph::`, remove the empty `::` block. I was not able to build the documentation and it took me a while to understand that it was caused by this `::` stuff.
- I'm not sure the empty line `....:` is useful. You can remove it.

I hope it's the last round of corrections ;)


---

Comment by git created at 2017-07-02 23:14:38

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-07-02 23:16:26

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by zgershkoff created at 2017-07-02 23:16:50

Done. Thanks for walking me through it.


---

Comment by dcoudert created at 2017-07-02 23:46:10

You have used `from 'u' to 'v'` with `'` instead of ```. I think that ``` is more appropriate. It is nicer in the documentation and it avoids confusion with string.

You have to do the correction both at the top of the file and at the beginning of `contract_edge`.

After that you can set the ticket to positive review (or I will do it later).

Best,


---

Comment by git created at 2017-07-03 00:04:13

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by zgershkoff created at 2017-07-03 00:39:40

Changing status from needs_review to positive_review.


---

Comment by zgershkoff created at 2017-07-03 00:39:40

I can't personally verify that the documentation builds correctly (perhaps an error with the beta I have installed), but doctests pass, so I'll take your word for it. Thanks for the review.


---

Comment by dcoudert created at 2017-07-03 03:17:50

I checked and the documentation looks good. So we are done.


---

Comment by vbraun created at 2017-08-14 22:39:39

If you depend on a pre-git ticket then the release script will never figure out that the dependencies are merged FYI


---

Comment by vbraun created at 2017-08-16 18:46:08

Resolution: fixed
