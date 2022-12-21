# Issue 9698: Hamiltonian cycles in undirected graphs - backtracking algorithm.

Issue created by migration from Trac.

Original creator: fidelbarrera

Original creation time: 2010-08-06 19:17:39

Assignee: jason, ncohen, rlm

CC:  rlm boothby ncohen

Randomized backtracking for finding hamiltonian cycles.

A path P is maintained during the execution of the algorithm. Initially the path will contain an edge of the graph. Every 10 iterations the path is reversed. Every ``reset_bound`` iterations the path will be cleared and procedure is restarted. Every ``backtrack_bound`` steps we discard the last five vertices and continue with the procedure. The total number of steps in the algorithm is controlled by ``max_iter``. If a hamiltonian cycle is found it is returned. If the number of steps reaches ``max_iter`` 
then a longest path is returned. See OUTPUT for more details.


---

Attachment


---

Comment by fidelbarrera created at 2010-08-06 19:26:49

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-08-07 02:07:01

Changing status from needs_review to needs_info.


---

Comment by ncohen created at 2010-08-07 02:07:01

Wow !!! This sounds great !! I promise I will give this patch a look as soon as possible ! :-)

I have a few questions already...

 * I noticed you mentionned in the doc that the backtrack algorithm may not return an optimal hamiltonian path, but don't you think it may be better to create another function for it, rather than having a method whose answer may be exact or not depending on the algorithm used ?
 * If your algorithm is fast enough, could it be interesting to check when calling is_hamiltonian the answer given by your algorithm before solving the actual tsp problem (which is sometimes veeeeeery long) ?
 * Main question : as it is a backtracking algorithm, and this may require a lot of computational work... What would you think of making it a Cython function, to give t more energy ? :-)

Thaaaanksssssssss ! :-)

Nathann


---

Comment by fidelbarrera created at 2010-08-08 03:29:27

Replying to [comment:2 ncohen]:
> Wow !!! This sounds great !! I promise I will give this patch a look as soon as possible ! :-)
> 
> I have a few questions already...
> 
>  * I noticed you mentionned in the doc that the backtrack algorithm may not return an optimal hamiltonian path, but don't you think it may be better to create another function for it, rather than having a method whose answer may be exact or not depending on the algorithm used ?

Yes, this sounds OK. Would you think it is OK to call it `hamilton_cycle_heuristic`? Please let me know if you have a better suggestion for the name.

>  * If your algorithm is fast enough, could it be interesting to check when calling is_hamiltonian the answer given by your algorithm before solving the actual tsp problem (which is sometimes veeeeeery long) ?

I am not sure about this. I believe the algorithm is pretty fast on hamiltonian graphs whose vertices have low degree. But if not, the amount of time spent searching depends on `max_iter`. For the current default value of `max_iter`, it takes more than 20 seconds to stop searching for a hamilton cycle in the Petersen graph. Trying with the tsp algorithm it takes only 1/100 of a second.

>  * Main question : as it is a backtracking algorithm, and this may require a lot of computational work... What would you think of making it a Cython function, to give t more energy ? :-)

This sounds great! I have never implemented anything in Cython, but I'll give it a try. :)


> 
> Thaaaanksssssssss ! :-)
> 
> Nathann

Cheers,
Fidel


---

Comment by ncohen created at 2010-08-08 03:48:08

> Yes, this sounds OK. Would you think it is OK to call it `hamilton_cycle_heuristic`? Please let me know if you have a better suggestion for the name.

Hmm.. I was about to answer "yes" when I noticed that your algorithm, even though it may return an hamiltonian cycle when it finds one, will return the longest path it found otherwise.. Hence, here is a proposition : 

there is a file named graphs/generic_graph_pyx.pyx (which is a Cython file), into which you could add your algorithm (using Cython to optimize it if possible). The methods added to this class are not directly accessible through the Graph class, which means that if you add your algorithm there, it will not appear as methods of the graphs objects. What you could do then, is add a method hamilton_cycle_heuristic and longest_path_heuristic to the generic_graph class (unifying both directed and undirected graphs), which would call your algorithm. The hamilton_cycle_heuristic would call this algorithm and return the hamiltonian path if found, and nothing otherwise. The hamiltonian_path method would call your algorithm, and return its result as the longest path found. 

This, because otherwise people may not notice your hamiltonian_cycle_heuristic can also be useful to find longest paths...

Well, this may be quite some work, but if I can help you at any step, please tell me :-)

> I am not sure about this. I believe the algorithm is pretty fast on hamiltonian graphs whose vertices have low degree. But if not, the amount of time spent searching depends on `max_iter`. For the current default value of `max_iter`, it takes more than 20 seconds to stop searching for a hamilton cycle in the Petersen graph. Trying with the tsp algorithm it takes only 1/100 of a second.

Hmmm... I hope this could be very different after the algorithm is rewritten using Cython :-)

> This sounds great! I have never implemented anything in Cython, but I'll give it a try. :)

Well, if you know C, then Cython iss "just" a wonderful way to write C instructions among Python code.. And the C parts are.. FAST :-D

I wrote an enumerative algorithm to find a given induced subgraph in a large graph. If you want to give a look to its source code, it is located in graphs/generic_graph_pyx.pyx. You will find there other examples of Cython code, but it is mainly that : you can write C code in Python file. Here again, send me an email if you think I can be of any assistance. Or you can post on sage-devel, to obtain answers from more knowledgeable developpers.

Nathann


---

Comment by rlm created at 2010-08-09 18:19:19

Replying to [comment:5 ncohen]:
> there is a file named graphs/generic_graph_pyx.pyx (which is a Cython file), into which you could add your algorithm (using Cython to optimize it if possible).

`generic_graph` and `generic_graph_pyx` are for methods which are common to `Graph` and `DiGraph`. This algorithm is just for undirected graphs. What there needs to be are `graph_pyx` and `digraph_pyx` files, which there currently are not.*

> The methods added to this class are not directly accessible through the Graph class

This is just plain wrong. Any methods you add to the *class* `GenericGraph_pyx` are inherited by `GenericGraph`, which are then inherited by `Graph` and `DiGraph`.

> Well, this may be quite some work, but if I can help you at any step, please tell me :-)

* - I'm not sure whether Cython supports multiple inheritance or not. It would be harder to have `graph_pyx` and `digraph_pyx` if not, because (I think) Cython cdef classes cannot inherit from Python classes...


---

Comment by ncohen created at 2010-08-10 03:28:56

Replying to [comment:6 rlm]:

> `generic_graph` and `generic_graph_pyx` are for methods which are common to `Graph` and `DiGraph`. This algorithm is just for undirected graphs. What there needs to be are `graph_pyx` and `digraph_pyx` files, which there currently are not.*

Oh... I didn't notice that... Both longest path and hamiltonian cycle make sense in both settings though, and with some luck writing a version handling both does not require too much work.

> This is just plain wrong. Any methods you add to the *class* `GenericGraph_pyx` are inherited by `GenericGraph`, which are then inherited by `Graph` and `DiGraph`.

After giving it a look, it is indeed plainly wrong. It just shows I added methods to the file -- and not to the class --  when I edited the file... Sorryyyyy !! `^^;`

Nathann


---

Attachment

Please apply instead of trac_9698.patch.


---

Comment by fidelbarrera created at 2010-09-02 19:44:01

Changing status from needs_info to needs_review.


---

Comment by fidelbarrera created at 2010-09-02 19:44:01

Replying to [comment:5 ncohen]:

> Hmmm... I hope this could be very different after the algorithm is rewritten using Cython :-)

Quite amazed, it takes less than 2 seconds now, against 25s in Python :-O! 

> Well, if you know C, then Cython iss "just" a wonderful way to write C instructions among Python code.. And the C parts are.. FAST :-D

Still a bit unsure about my Cython style (first timer), I would appreciate any comments you have about it.

> I wrote an enumerative algorithm to find a given induced subgraph in a large graph. If you want to give a look to its source code, it is located in graphs/generic_graph_pyx.pyx. You will find there other examples of Cython code, but it is mainly that : you can write C code in Python file. Here again, send me an email if you think I can be of any assistance. Or you can post on sage-devel, to obtain answers from more knowledgeable developpers.

This one and the source code for Sparse and Dense graphs really helped. Thanks!

Please apply trac_9698_2.patch instead of trac_9698.patch.

Fidel


---

Comment by rlm created at 2010-09-02 19:48:40

Fidel,

May I suggest to put this code into `generic_graph.pyx` instead of creating a new Cython file for just this one function?


---

Comment by fidelbarrera created at 2010-09-02 20:11:07

Please apply instead of trac_9698.patch and trac_9698_2.patch.


---

Attachment

Replying to [comment:9 rlm]:

> Fidel, May I suggest to put this code into `generic_graph.pyx` instead of creating a new Cython file for just this one function?

Sure, please use trac_9698_3.patch instead of the previous ones.

Fidel


---

Comment by ncohen created at 2010-09-04 13:31:59

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-09-04 13:31:59

Hello Fidel !!

Well, first let me say that I am very glad to see you rewrote this piece of code in Cython, to find out it greatly improved its performances `:-)`

I have been spending some time reading your code. I began by fixing one or two typo, then ended up having more important remarks, so I will list them as they sometimes need your answers :

    * Your doctest is "too" indented. The normal text should be aligned with the initial `"""` as for the other methods

    * Your explanation of the algorithm would deserve to follow a ``ALGORITHM:`` line, as in ``subgraph_search``

    * we are used to write ``OUTPUT:`` then its contents on the following lines, and not as you do on the same line. There is no good reason behind, that's just to keep the whole syntax in the whole code

    * If you have time, it would be nice to give several comments along with the examples `:-)`

    * it may be nice to cache the list of vertices instead of calling ``g.verts()`` very often. A 
      {{{
      cdef list vertices = g.verts()
      }}}
      is all it requires, and it lets you replace ``g.verts()`` by ``vertices`` elsewhere in the code
    * I do not get why you list the possible extensions this way :
      {{{
      for u in g.out_neighbors( path[ length-1 ] ):
      }}}

      I expected the algorithm to pick a random neighbor which is not already in the path at this step. Why don't you first build the list of such elements, then pick one if there exists any ? As it is written, you algorithm may ignore some paths, as it always picks the "first one" as returned by the list of neighbors.

    * I understand the usefulness of path reversing, or resetting, or removing the last 5 vertices, but there is something else I do not understand in your code : let us imagine that your algorithm, at each loop, is increasing the current path from one element at each time for a long period. At some point, your algorithm will reset it, or remove the last vertices, even while it may still be possible to extend the path. Why so ? A way around :

      Given a current "path", there could be a method named "greedily_extend" which, for as long as there exists a possible extension of the path (a neighbor of the last vertex not already in the path), picks one randomly and adds it to the path. This method ends when it is not possible to greedily extend the path anymore. It is not a very costly method, and at each iteration of it increases the current path's legngth, which is good. Your counters could then be "when this method has been called 100 times, remove the last 5", or reset, etc, etc... It would be a way to avoid the path to be increased while it is possible because of the counters (which are useful -- I do not deny this !). This would also avoid the following :

    * Each time a new vertex is added to the longest path, it is copied to be remembered. It is nice, but if your algorithm begins by building a path of length 20, you copy it 20 times ! By having a method like the previous one, you would call it just once, when the path can not be extended anymore. 

    * If your code finds a hamiltonian path whith is not a cycle, it ends anyway.

    * About 
      {{{
      for row in G.adjacency_matrix():
      }}}

      Why don't you prefer to list G's edges ?

      The answer to that one may have to do with the following :

    * Here is what happens when the vertices of your graph are not integers :

      {{{
       sage: from sage.graphs.generic_graph_pyx import find_hamiltonian as fh
       sage: fh(graphs.Grid2dGraph(5,5))
       ERROR: An unexpected error occurred while tokenizing input
       The following traceback may be corrupted or invalid
       The error message is: ('EOF in multi-line statement', (636, 0))
      
       ERROR: An unexpected error occurred while tokenizing input
       The following traceback may be corrupted or invalid
       The error message is: ('EOF in multi-line statement', (555, 0))
       
       ---------------------------------------------------------------------------
       TypeError                                 Traceback (most recent call last)
       
       /home/ncohen/<ipython console> in <module>()
       
       /home/ncohen/.Sage/local/lib/python2.6/site-packages/sage/graphs/generic_graph_pyx.so in sage.graphs.generic_graph_pyx.find_hamiltonian (sage/graphs/generic_graph_pyx.c:9109)()
       
      /home/ncohen/.Sage/local/lib/python2.6/site-packages/sage/graphs/generic_graph_pyx.so in sage.graphs.generic_graph_pyx.find_hamiltonian (sage/graphs/generic_graph_pyx.c:7609)()
      
      TypeError: an integer is required
      }}}

      I have been told this an incredible amount of times myself `^^;`

Overall, I stll do not understand why you call it an heuristic to find a hamiltonian cycle ! What you have written in a heuristic to find a hamiltonian path, which tries to return a hamiltonian cycle. What about renaming all of it accordingly ? What about writing a ``longest_path`` method ? I could write such a LP as an exact solver, and you could add your heuristic to it, exactly as you did for hamiltonian_cycle. You method is not only useful for hamiltonian cycle, but also for hamiltonian/longest paths ! Please give me your advice on this.

Ok, this was a long review... Sorry for the time it requires... `^^;`. I was away for one month and a half, but I should be more reactive now, and by email too if necessary... Thank you very much for your work, though `:-)` 

Nathann


---

Comment by fidelbarrera created at 2010-09-12 20:49:09

Please apply instead of previous patches.


---

Attachment

Replying to [comment:11 ncohen]:

Hello Nathann,

> I have been spending some time reading your code. I began by fixing one or two typo, then ended up having more important remarks, so I will list them as they sometimes need your answers :

Thanks!

I have fixed the doctest indentation, added an ALGORITHM: line and fixed the OUTPUT: line.

The vertices are now cached in !``vertices!``. And every vertex is picked randomly, not as before, where the first available vertex was chosen.

> * I understand the usefulness of path reversing, or resetting, or removing the last 5 vertices, but there is something else I do not understand in your code : let us imagine that your algorithm, at each loop, is increasing the current path from one element at each time for a long period. At some point, your algorithm will reset it, or remove the last vertices, even while it may still be possible to extend the path. Why so ? A way around :

Here we rely on the !``backtrack_bound!`` and !``reset_bound!``, we should give "appropriate" values.

> * Each time a new vertex is added to the longest path, it is copied to be remembered. It is nice, but if your algorithm begins by building a path of length 20, you copy it 20 times ! By having a method like the previous one, you would call it just once, when the path can not be extended anymore.

Now, the longest path is only updated if the path cannot be extended anymore.

> * If your code finds a hamiltonian path whith is not a cycle, it ends anyway.

I think that when a hamiltonian path is found, we check if the two ends are adjacent, if so, then it ends. The test is done in:


```
            done = g.has_arc( path[n-1], path[0] )
```

It also takes longer with non hamiltonian graphs, e.g. the Petersen graph, i.e. it stops until it hits the max_iter bound.

I think the problem with the vertices not being integers is fixed now Although I did not get error messages as yours, I just got as output a list of integer vertices.

I think I have removed the word heuristic. It would be great to write the longest_path method. The function is almost exactly the same as the one that is written, in fact it might be possible to adapt this one to do both ;)

Thanks, 

Fidel


---

Comment by fidelbarrera created at 2010-09-12 21:21:41

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-09-14 19:22:36

``longest_path`` written in #9910 `:-)`

Nathann


---

Comment by fidelbarrera created at 2010-10-10 22:39:15

Please apply instead of previous patches.


---

Attachment

Replying to [comment:13 ncohen]:
> ``longest_path`` written in #9910 `:-)`
> 
> Nathann

Hello Nathann,

I have modified the function so it can obtain longest paths as well. Please let me know what you think, about it.

Thanks,
Fidel


---

Comment by ncohen created at 2010-10-11 07:56:33

Hello !!!

It looks like you patch can not be applied on the brand-new 4.6.alpha3... As it is the second time in two days a patch does not apply on this release, I tried #10043 to notice it did no apply either -- it was THE patch I did not want to rebase :-/

Nathann


---

Comment by ncohen created at 2010-10-11 07:56:33

Changing status from needs_review to needs_work.


---

Comment by fidelbarrera created at 2010-10-17 04:40:25

Rebased version of trac_9698_5.patch


---

Attachment

Hello Nathann,

> It looks like you patch can not be applied on the brand-new 4.6.alpha3... 
I have rebased the patch, please see trac_9698_6.patch I hope it works now :)

Best,
Fidel


---

Comment by fidelbarrera created at 2010-10-17 04:42:43

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-10-17 13:27:03

Then I guess this is it ! I am adding a small patch with unimportant modifications, like adding backquotes, lists for enumerations, or changing the length of some lines. I also added a doctest, just in case. Whatever happens, I do not fear anything wrong from this method as it tests its output before returning it... Positive review to your patch ! Could you review mine ? `:-)`

Thanksssssss !!

Nathann


---

Comment by fidelbarrera created at 2010-10-18 16:16:23

Changing status from needs_review to positive_review.


---

Attachment

Your modifications look good. All doctests passed. Changing to positive review.

Thanks,
Fidel


---

Attachment

same as trac_9698 - smallfixes.patch


---

Comment by jdemeyer created at 2010-10-23 12:10:18

Please don't put spaces in patch filenames


---

Comment by jdemeyer created at 2010-11-01 10:10:09

Resolution: fixed


---

Comment by eviatarbach created at 2011-01-05 04:30:48

Great patch! I was hoping for these functions. There are some spelling problems, though (these are all in the docstrings):

1. All instances of "hamiltonian" should be changed to "Hamiltonian". This is because Hamilton is a proper noun, and the capitalization transfers to the term (see here: http://mathworld.wolfram.com/HamiltonianCycle.html). "hypohamiltonian" should be left lower-case, though.
2. "neccesary" should be "necessary"
3. "non hamiltonian" should be "non-Hamiltonian" (note the dash)
4. "Dodecahedral" should not be capitalized; "dodecahedral"
5. "Running the algorithm on random instances, just to make sure the answers are still satisfiable path". Should be "paths".
6. "ajacent" should be "adjacent"
7. "Now, we try the algorithm on a non hamiltonian graph, the Petersen graph" should be "graph: the".
8. "another known hypohamiltonian graph, the generalized Petersen" should be "graph: the"

Sorry for having to reopen!


---

Comment by eviatarbach created at 2011-01-05 04:30:48

Changing status from closed to needs_work.


---

Comment by jdemeyer created at 2011-01-05 08:19:13

I created a new ticket for this: #10561
