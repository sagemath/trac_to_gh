# Issue 7724: breadth/depth first search for c_graphs

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-12-17 17:46:37

Assignee: rlm

CC:  rlm

Some improvement on this side, and so for ther functions like connected components, strongly connected components, etc...


```
sage: g= graphs.RandomGNP(1000,.01)
sage: h=g.copy(implementation="c_graph")
sage: timeit("list(g.depth_first_search(0))")
25 loops, best of 3: 10.9 ms per loop
sage: timeit("list(h.depth_first_search(0))")
125 loops, best of 3: 2.03 ms per loop
```


Nathann


---

Comment by ncohen created at 2009-12-18 14:46:11

Changing status from new to needs_review.


---

Comment by ncohen created at 2009-12-18 15:24:55

( small bug fixed : I had forgotten bitset_set_first_n which was quite problematic in a few cases :-) )


---

Comment by rlm created at 2009-12-18 22:00:26

There's a merging conflict:

```
-        ALGORITHM: 8.3.8 in [1]. Notice that the termination condition on 
-        line (23) of the algorithm uses "p[v] == 0" which in the book 
-        means that the parent is undefined; in this case, v must be the 
+        ALGORITHM: 8.3.8 in [Jungnickel2005]_. Notice that the termination 
+        condition on line (23) of the algorithm uses "p[v] == 0" which in
+        the book means that the parent is undefined; in this case, v must be the 
         root s.  Since our vertex names start with 0, we substitute instead
         the condition "v == s".  This is the terminating condition used 
         in the general Depth First Search tree in Algorithm 8.2.1.
         
         REFERENCE:
 
-        - [1] D. Jungnickel, Graphs, Networks and Algorithms,
+        .. [Jungnickel2005] D. Jungnickel, Graphs, Networks and Algorithms,
```


This change already made it into 4.3.rc1, I believe, in #7314. Can you rebase on top of that patch?


---

Comment by rlm created at 2009-12-18 22:00:26

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2009-12-19 08:29:23

I'm not at home and won't be able to do it today... I should be able to produce it tomorrow morning though :-)


---

Comment by ncohen created at 2009-12-20 16:35:15

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2009-12-20 16:35:15

Hello !!

I could not reproduce your merging conflict, though as I had applied the patch I use the occasion to add a few other things... You will find in this new version of the patch

    * A function beadth_dirst_search ( with optional arguments ``reverse`` and ``ignore_direction``
    * A function ``depth_first_search`` with the same paremeters
    * A function ``is_connected``
    * A function ``is_strongly_connected``
    * I needed to know inside the graph backend whether the graph was directed or not : I thought for some time about it, and ended up adding to the constructors of ``Graph`` and ``DiGraph`` a line ``self._backend.directed = True/False`` according to the situation.
    * I also modified graph.py so that it would use the functions defined in c_graph whenever possible, and NetworkX otherwise

And with this, we should be another step closer.. :-)

Nathann


---

Comment by ylchapuy created at 2009-12-21 00:27:52

The actual breadth/depth_first_search are generator objects but your new ones are plain lists. Is it a design choice?


---

Comment by ncohen created at 2009-12-21 06:46:15

There is no "yield" command available at the moment in Cython... :-)


---

Comment by ncohen created at 2009-12-21 07:01:32

Now using bitset_first to find a vertex in the graph :-)

Nathann


---

Comment by ylchapuy created at 2009-12-21 11:25:25

Replying to [comment:7 ncohen]:
> There is no "yield" command available at the moment in Cython... :-)

But you can still define a iterator class.

The following patch is based on your work, and defines an iterator. You can choose which one you prefer.


---

Comment by ncohen created at 2009-12-21 11:43:21

Well, actually until now Robert Miller just typed : return iter(value)) which was good too... If you prefer to return an iterator instead of alist, perhaps this would be better :-)


---

Comment by ylchapuy created at 2009-12-21 11:46:26

The way I did it, I don't copy the data, the big list doesn't exist, this can be an advantage. But I let you do the choice, I won't use big graphs anyway.


---

Comment by ncohen created at 2009-12-21 11:49:35

Well, my view was that if just waiting can prevent us from writing lines of codes that could be replaced by a "yield" once it will be available, why not ? :-)

Let's see what Robert thinks about it if he is finally reviewing this ticket .. And thank you again for your help ! :-)

Nathann


---

Comment by ylchapuy created at 2009-12-21 15:45:26

slight update:
use extend instead of append improves performance


---

Attachment


---

Comment by rlm created at 2010-01-02 16:18:24

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-02 16:18:24

1. The iterator patch is preferable, since there are actual speed gains when a loop is terminated early. I've rebased the patch against sage-4.3.

2. There is some confusion as to the function `get_vertex`. This should go from Python objects to ints, and in several places it is used the other way around. The function `vertex_label` will go from int to Python object, and I've switched these in the appropriate places (see `trac_7724-ref.patch`). I've also added an example where the vertex labels aren't integers.

3. I've tested this with #7634 applied, and everything looks good with the fixes mentioned above.


---

Attachment


---

Comment by mhansen created at 2010-01-03 22:13:00

Resolution: fixed
