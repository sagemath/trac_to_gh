# Issue 8273: Enumeration of cycles in directed graphs

Issue created by migration from https://trac.sagemath.org/ticket/8273

Original creator: abmasse

Original creation time: 2010-02-15 14:43:20

Assignee: rlm

CC:  ncohen rlm sage-combinat

Keywords: cycle, enumeration

In many graph-theoretical problems, it is important to understand the cycles structure of undirected graphs as well as directed ones. Therefore, I suggest three functions that allow one to iterate over all cycles of a directed graph (I might be interested in writing some functions for undirected graphs, but I prefer to have these ones validated before I do so).



The first and main function is called `cycles_iterator(...)` and allows one to iterate over all cycles satisfying conditions according to the following parameters:

- `simple` (a boolean). When set to True, only the starting and ending vertex may be repeated in the cycle

- `distinct` (also a boolean). When set to True, then all equivalent cycles are merged into one cycle. Equivalent cycles are cycles differing only from their starting vertex, such as `[0,1,2,0]` and `[1,2,0,1]`.

- `initial_vertices` (an iterable). Specify the only allowed starting vertices of the cycles.

- `max_length` (an integer). The maximum length of cycles. Useful especially when a graph contains a very large number of cycles and one wants to compute smaller ones.

The two other function are merely calling `cycles_iterator(...)` with some of the above parameters fixed.


---

Comment by abmasse created at 2010-02-15 14:56:54

Will add the patch soon.


---

Comment by abmasse created at 2010-02-15 15:12:19

As you may see in the patch file, I added the digraph.py and generic_graph.py files so that it appear in the generated documentation. However, there are a lot of warnings... What should we do about it? Correct it in that ticket?


---

Comment by abmasse created at 2010-02-15 15:12:19

Changing status from new to needs_review.


---

Comment by abmasse created at 2010-02-15 22:22:29

Changing type from defect to enhancement.


---

Comment by abmasse created at 2010-02-15 22:22:29

Changing status from needs_review to needs_work.


---

Comment by abmasse created at 2010-02-15 22:22:29

Nathann Cohen wrote:

  Hello !!!

  I just took a quick look at your patch :

  - Don't you think it may still be interesting to first check whether
  the given is/is not in any cycle ? It just amounts to check the
  strongly connected component containing this vertex is a singleton. I
  wrote is_strongly_connected in c_graph.pyx, so it is in Cython and
  very efficient... strongly_connected_component_containing_vertex is
  still to be written, but it should take at most 6 lines, which are a
  pure copy of is_strongly_connected :-)
  Of course if this function is recursive, it is totallty different as
  it may mean many different calls :-)

  - I see you wrote many comments in the code, which is nice, but some
  loops are not commented at all... Do you think the algorithm can be
  easily understood reading it ? :-)

       1530            if len(sccs) == 0: raise StopIteration

  This condition shouldn't ever happen, as the list of strongly
  connected components is a list of list.. In the "worst" case, the
  returned list has a singleton per item :

  [ [0], [1], .... ], and in this case len(sccs) == self.order()

Thank you for your comments ! I will indeed add some comments in the code so that everyone can understand what it does. As for the first comment, I think it is better not to compute the strongly connected components in the private function `_cycles_iterator_vertex(...)` since it will be computed for every starting vertices (i.e. it will be quadratic in the worst case). As for the remark for trivial cycles, it is a good remark: I think I will add another parameter to choose if one wants to include trivial cycles or not. What do you think?


---

Comment by ncohen created at 2010-02-16 17:26:25

Hello !!!

It would be good to get (cheaply) rid of this "bug" happening when the vertices are in no non-trivial strongly connected components... Perhaps some other parameter meant to be used only internally, in this case too... But this would mean a lot of them in the end :-)

I continued to read some parts of your code, and have some other remarks :

 * you write :
   {{{
        sccs = self.strongly_connected_components()
        from operator import add
        vertices = reduce(add, sccs)
        edges = reduce(add, [self.subgraph(scc).edges() for scc in sccs])
        h = self.subgraph(vertices, edges)
   }}}
   Well, you seem trying to get rid of "bridges" -- edges whose removal disconnect the graph. Obviously, there will be no cycle going through them. Doing so, you create a lot of copies of the graph (the subgraph() command), which could be costly... Here is another way to do it :

   First, create the list of strongly connected components
   {{{
        sccs = self.strongly_connected_components()
   }}}

   Then, associate to each vertex the id of its connected component :

   {{{
        d = {}
        for id, component in enumerate(sccs):
            for v in component:
 	        d[v] = id
   }}}

   Once it is done, create a copy of your first graph using the copy command (these commands are low-level, written in Cython). Then remove the bad edges :

   {{{
        h = self.copy()
	h.delete_edges([ e for e in g.edge_iterator() if d[e[0]] != d[e[1]] ])
   }}}

   This way most of the work is done using dictionaries, and no heavy structure like graphs.

 * How is this :

   {{{
        vertices = reduce(add, sccs)
   }}}

   different from setting

   {{{
	vertices = self.vertices() 
   }}}

   I think it comes from the same fact that you will have in sccs some connected components equal to singletons.

  * You write :
  
    {{{
        for vi in vertex_iterators.values():
            try:
                cycles.append(vi.next())
            except(StopIteration):
                pass
    }}}

    I do not know much about iterators, but... Well, the values of vertex_iterators are iterators, so 

    {{{
        for vi in vertex_iterators.values():
	     cycles.extend(list(vi))
    }}}

    should work, shouldn't it ?

 * This :

   {{{
        while len(cycles) > 0:
   }}}
   
   Can be replaced by 

   {{{
        while cycles:
   }}}

 * In this situation :
   {{{
            for i in range(len(cycles)):
                if len(cycles[i]) < len(shortest_cycle):
                    shortest_cycle = cycles[i]
                    imin = i
   }}}

   You can write 

   {{{
            for i, cycle_i in enumerate(cycles):
                if len(cycle_i) < len(shortest_cycle):
                    shortest_cycle = cycle_i
                    imin = i
   }}}

   I have been told about this "enumerate" trick when working on Cython files... This command is optimized in Cython, so writing Python code this way will help if we are to Cythonize it later :-)

   For example :

   {{{
   a = ['pie', 'cake', 'coffee']
   list(enumerate(a))
   [(0, 'pie'), (1, 'cake'), (2, 'coffee')]
   }}}

   Anyway, if you are trying to get the minimum element of such a list, you could have also written :

   {{{
   i_min, cycle_min = min( enumerate(cycles), key = lambda x: len(x[1]) )
   }}}

I'll give a look again at your next version of the patch... Each time I get more used to what it does :-)

Nathann


---

Comment by abmasse created at 2010-02-23 13:36:22

Hello, Nathann !
I corrected my patch according to your remarks. I agree with all of them except the following one

  I do not know much about iterators, but...
  Well, the values of vertex_iterators are iterators,
  so


```
for vi in vertex_iterators.values():
    cycles.extend(list(vi))
```


For two reasons: (1) I want to iterate cycles with increasing length and what you propose breaks this property. (2) There is no guarantee that ``list(vi)`` will ever terminate, since the number of cycles (when ``simple`` is set to False) may be infinite !

I also added three functions which iterate over paths. Note that the code is almost the same, but for sake of efficienty, it seems better to me not to intersect it. The main reason is that when you want to enumerate unrooted cycles, there is a very fast way to verify that (just check that the starting vertex of the current path is the smallest in the path). Therefore, I prefered to separate the two functions.

Thank you for the useful comments !

Also, if you prefer me to break the patch into two smaller ones, just tell me, I'll do it. I'll upload the patch in a short while.


---

Attachment

New patch taking into account Nathann's comments


---

Comment by abmasse created at 2010-02-23 14:03:10

The patch has been uploaded. I removed doc reference changes since some warnings occurred and I believe it should be done in another patch. My modifications seemed correct concerning the documentation. Now needing review !


---

Comment by abmasse created at 2010-02-23 14:03:10

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-02-24 17:41:22

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-02-24 17:41:22

Several comments :

 * I do not understand the comment "First, we handle the trivial paths if needed" at line 1519 of digraph.py. What you do just afterwards is initialize the list of paths, which is nicely done regardless of the value of "trivial".

 * I did not notice it before, but you are maintaining a list of values to which you append things, while only removing the smallest element. This is clearly a heap !! By using them (see http://docs.python.org/library/heapq.html), you could *theoretically* reduce the complexity of your computations. Well, I think you patch is fixe as it is now, but if you need your computations to speed up a bit, this is definitely worth a try !

 * Instead, when starting_vertices = None, of setting it to self.vertices(), you can also set it to just "self". When, later on, you write "for v in starting_vertices", it will use the iterator over the vertices from "self", which can be slightly better. Well, you algorithm is not meant to be used on graphs with a large number of vertices anyway, so it's not a problem in the present case.

 * in all_simple_paths, you both have a "vertex" argument and a "starting vertex" argument. Besides, in the documentation, you say that vertex is the starting vertex of the cycle. What I understand is : the cycles you enumerate will ALL contain "vertex", but the first vertices of each cycle you will return will belong to starting_vertices. Is this right ? :-)

 * line 1706 : I understand your comment as "If cycles are NOT rooted", which is what your code does and appears more correct. Besides, is "rooted" is documented in all_cycles_iterator, it is not in _all_cycles_iterator

 * You remove the bad edges in _all_simple_cycles if the correct flag is set, though you never use it in your own code... As you remove them manually in all_simple_cycles, perhaps you can just remove this option in _all_simple_cycles ?

 
Short of this, your patch is fine... Next update will definitely be a positive review ! I did not update the patch myself as there were several questions I did not know how to solve myself, so sorry if some comments are clearly minor ones... :-)

Have fuuuuuuun !

Nathann


---

Comment by abmasse created at 2010-02-25 17:50:50

Hello, Nathann !

Don't say sorry, your comments are very welcome and are clearly pertinent !

Several comments :

    * I do not understand the comment "First, we handle the trivial paths if needed" at line 1519 of digraph.py. What you do just afterwards is initialize the list of paths, which is nicely done regardless of the value of "trivial". 

Done. It was an old comment I forgot to delete.

    * I did not notice it before, but you are maintaining a list of values to which you append things, while only removing the smallest element. This is clearly a heap !! By using them (see  http://docs.python.org/library/heapq.html), you could *theoretically* reduce the complexity of your computations. Well, I think you patch is fixe as it is now, but if you need your computations to speed up a bit, this is definitely worth a try ! 

Done. I noticed it while writing the code, but I was too lazy to do it. It turned out to be very simple, so I'm glad you mentionned it.

    * Instead, when starting_vertices = None, of setting it to self.vertices(), you can also set it to just "self". When, later on, you write "for v in starting_vertices", it will use the iterator over the vertices from "self", which can be slightly better. Well, you algorithm is not meant to be used on graphs with a large number of vertices anyway, so it's not a problem in the present case. 

Done. Thanks for the information !

    * in all_simple_paths, you both have a "vertex" argument and a "starting vertex" argument. Besides, in the documentation, you say that vertex is the starting vertex of the cycle. What I understand is : the cycles you enumerate will ALL contain "vertex", but the first vertices of each cycle you will return will belong to starting_vertices. Is this right ? :-) 

There is no argument vertex in `all_simple_paths`, unless I'm mistaken. I guess you mean `_all_cycles_iterator_vertex` ? But your understanding is correct. It seems odd to have the arguments `vertex` and `starting_vertices`: the reason I do that is that I need to know what are the allowed initial vertices so that I return only one cycle among `[0,1,0]` and `[1,0,1]` when `rooted=False`. An efficient and simple way to control equivalent rooted cycles is to return the one with smallest starting vertex.

    * line 1706 : I understand your comment as "If cycles are NOT rooted", which is what your code does and appears more correct. Besides, is "rooted" is documented in all_cycles_iterator, it is not in _all_cycles_iterator 

Done. You are right. The meaning of `rooted` is now documented in `_all_cycles_iterator`.

    * You remove the bad edges in _all_simple_cycles if the correct flag is set, though you never use it in your own code... As you remove them manually in all_simple_cycles, perhaps you can just remove this option in _all_simple_cycles ? 

The reason I put this flag is that I want the function `_all_simple_cycles_iterator_vertex` not to cycle infinitely if one uses it directly. So, yes, I don't use it directly in my code, but this allows me to remove the warning about infinite cycle there was before.

I'll upload a patch in a short while.


---

Comment by abmasse created at 2010-02-25 17:54:36

Apply on top of the main patch


---

Attachment

I uploaded another patch that include your comments. Needs review !


---

Comment by abmasse created at 2010-02-25 17:55:26

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-02-26 09:42:50

It just needs merging now... Very nice work ! :-)

Nathann


---

Comment by ncohen created at 2010-02-26 09:42:50

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-03 14:23:40

Resolution: fixed


---

Comment by mvngu created at 2010-03-03 14:23:40

Merged in this order:

 1. [trac_8273_digraphs_cycles_enumerations-abm.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8273/trac_8273_digraphs_cycles_enumerations-abm.patch)
 1. [trac_8273_with_heap-abm.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8273/trac_8273_with_heap-abm.patch)

Alexandre: you should place a sensible commit message in your patch together with the ticket number.


---

Comment by abmasse created at 2010-03-03 14:40:46

Yes, thank you, Minh, you're right !

Someone made me notice it some time ago and I thought I had done it for all my patchs, but it looks like I forgot some. It won't happen again I hope.
