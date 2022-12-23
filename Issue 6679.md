# Issue 6679: [with patch, needs review] Vertex Coloring, Edge Coloring (uses Linear Programming)

Issue created by migration from https://trac.sagemath.org/ticket/6679

Original creator: ncohen

Original creation time: 2009-08-06 15:10:42

Assignee: rlm

Hello everybody !!!

Here are two new functions for the Graph class in Sage : vertex_coloring and edge_coloring.

Those new functions both use Linear programming, so to use them you will have to install the patches MIP-1 to MIP-5 in #6502 along with the package GLPK :

http://trac.sagemath.org/sage_trac/ticket/6502

If you want them to be ever more efficient, you can also install COIN-OR/CBC ( from #6603 ) with this line :

sage -f http://www-sop.inria.fr/members/Nathann.Cohen/cbc-2.3.spkg

I hope I learned what I had to with my previous patch, as I hope you will find those functions sufficiently and correctly documented. These functions should be ---way--- more efficient than the previous ones, regardless of the Linear Solver you chose to use.

( I have to add that I will be absent next week, but even though I will be able to answer any of your questions and to post fixes until tomorrow evening. I chosed to post these two functions now hoping they could be integrated with the patch for LP into the next release of Sage )


---

Comment by ncohen created at 2009-08-06 15:11:43

First patch !


---

Attachment

First patch !


---

Comment by ncohen created at 2009-08-06 15:13:01

Hmmm... The two patches coloring-1 and coloring-1.2 are exactly identical, but I do not know how to remove the second one ^^;


---

Comment by ncohen created at 2009-08-31 15:54:54

As the functions dealing with LP have not been reviewed, I prefer to rewrite the MIP class for Sage to make it easier to use. I will post a new version of the MIP patch as soon as possible, along with all the patches for functions using it.

Sorry for the trouble, I'll try to make it quick !

Nathann


---

Comment by ncohen created at 2009-09-03 17:05:38

Even shorter, even better, even more efficient... Here is the new version of these two functions, now using the symbolic version of MIP from #6869 !!!!


---

Attachment


---

Comment by kcrisman created at 2009-10-21 16:23:53

I have a question.  What is the relation to the already existing methods .chromatic_number() and .coloring()?

```
sage: G = graphs.PetersenGraph()
sage: G.coloring()
[[1, 3, 5, 9], [0, 2, 6], [4, 7, 8]]
sage: G.chromatic_number()
3
```

At the very least it seems reasonable to modify .coloring() rather than add a new function, and perhaps keep the previous algorithm if that is useful.  I can't speak to which one is better, unfortunately, but it can be good to avoid a surfeit of methods.


---

Comment by kcrisman created at 2009-10-21 16:23:53

Changing status from needs_review to needs_info.


---

Comment by ncohen created at 2009-10-24 14:38:47

Changing status from needs_info to needs_review.


---

Comment by ncohen created at 2009-10-24 14:38:47

Hello !!!!

I wrote this patch some time ago, and it needed an update because of some changes in class numerical.mip. Besides, your sound remark needs an answer :-)

Here is what this new version of the patch does :

    * It creates two functions vertex_coloring and edge_coloring in the graph_coloring module.
    * I noticed there were methods defined in the graph_coloring module which were not used in the Graph class, even though they
      were built just for that ! For example, the function Graph.chromatic_number computes the chromatic number through computing the whole Chromatic Polynomial (honestly, I do not know any worse way to compute it !), even though there is a chromnatic_number function in the graph_coloring module computing the same parameter with a different method. I updated the Graph.chromatic_number method to let the user chose one of the (now three) different ways to compute the chromatic polynomial. I set it to MILP by default ( so that it uses the new vertex_coloring method which is defined in this patch ) as I expect it to be the most efficient.
    * The same thing occured in the Graph.coloring() function. This method used a slower version of what was already available in the graph_coloring module.  It now uses the graph_coloring.first_coloring method, or the newly defined vertex_coloring method.
    * Functions graph_coloring.chromatic_number and graph_coloring.first_coloring compute things that can also be computed through the use of the newly created graph_coloring.vertex_coloring method. I think the way they compute their results is far too slow, as they compute ALL the colorings to return one, and so should be removed ( the function all_graph_colorings, which they all use, must obvously be kept ) some months from now, while they should be kept some time to compare their results with graph_coloring.vertex_coloring ( both speed and exactness )
    * Several docstring fixes, when I noticed them

Nathann


---

Comment by ncohen created at 2009-11-10 09:20:15

Added round_robin, and a more efficient coloring for complete graphs


---

Comment by mvngu created at 2009-11-25 04:35:09

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2009-11-25 04:35:09

I assume that the patch `trac_6679.patch` is the one to review, so here goes. Here are some issues:

 1. For the function `chromatic_number()`, it's a bad idea to make "MILP" the default algorithm choice because that algorithm requires the installation of an optional package. Imagine the surprise (and confusion) when one uses the function `chromatic_number()` with the default value, but neither GLPK nor CBC is installed. You can make some algorithm a default choice provided that it's in a standard package or in the Sage library. If you have another algorithm that uses an optional package, you could still provide an interface to that algorithm and document uses of that algorithm in the docstring. So between "CP" and "DLX", choose one and make that algorithm the default choice. You have clearly documented how to use the "MILP" algorithm, which is good for those who want a better algorithm.
 1. You don't need to put spaces between the sign "=" if it occurs as part of assigning a value to an argument in a function call, like in `chromatic_number(algorithm="MILP")`. To follow coding conventions, you should put spaces between operators. So instead of doing `algorithm=="CP"`, you should do `algorithm == "CP"`. You can read more about Python coding conventions in [PEP 8](http://www.python.org/dev/peps/pep-0008/).
 1. Use the style of raising exceptions that is compatible with Python 3.x. For example, the following is not recommended for being compatible with Python 3.x:
 {{{
raise ValueError, "The `algorithm` variable must be set to either `DLX`, `MILP` or `CP`."
 }}}
 However, the following style is compatible with Python 3.x:
 {{{
raise ValueError("The `algorithm` variable must be set to either `DLX`, `MILP` or `CP`.")
 }}}
 Lots of code in the Sage library still uses the old style of raising exceptions. This will come back to haunt us when the time comes to switch to Python 3.x.
 1. The formatting of docstring is inconsistent.


---

Comment by ncohen created at 2009-11-25 08:16:03

Patch updated ! I also noticed I had forgotten one "optional" tag in the docstrings, and I rewrote all the ValueError I was able to find in the whole file.

I have a question though : I build the reference to check the docstrings and noticed the file graph_colouring.pyx was not included in them : should we change it ?

There are still many "test" functions in this file that may not be of interest to the user, though.... 

In any case, thank you very much for your help :-)

Nathann


---

Comment by mvngu created at 2009-11-25 08:25:09

Changing status from needs_work to needs_review.


---

Attachment

Replying to [comment:14 ncohen]:
> I have a question though : I build the reference to check the docstrings and noticed the file graph_colouring.pyx was not included in them : should we change it ?
An ultimate goal is to include all documentation of the Sage library in the reference manual. So, yes to your suggestion. Please open another ticket to include the file `sage/graph/graph_coloring.py` in the reference manual.


---

Comment by mvngu created at 2009-12-01 18:15:37

based on trac_6679.patch


---

Attachment

The patch `trac_6679.patch` applies OK against Sage 4.3.alpha0. All doctests pass with the options `-t -long`, apart from the following known doctest failure:

```
sage -t -long devel/sage/sage/interfaces/maxima.py # 1 doctests failed
```

The doctests also pass with the optional packages `cbc-2.3.p0` and `glpk-4.38.p2`, again with the above failure. In the function `first_coloring`(), the function signature states that `hex_colors=True`, which means that `hex_colors` is `True` by default. Yet, the documentation of this keyword claims otherwise. I have adjusted the documentation and value of `hex_colors` accordingly. However, it's crucial that you check my changes because in the function `coloring()` its default value is `False`. I have attached the reviewer patch `trac_6679-reviewer.patch`. Only my patch needs review. You should apply patches in this order:

 1. `trac_6679.patch`
 1. `trac_6679-reviewer.patch`


---

Comment by ncohen created at 2009-12-01 18:43:35

Well, graph coloring may be used to plot graphs but most of the time, its output is used to do more interesting things, so I think settng the default behaviour to returning the partition of independent sets is safe :-)

Short of this :
    * I'll remember to use xrange instead of range
    * I'll try not to go beyond 70 characters *even in the code*
    * I'll put more spaces in my code

And I thank you very very very much for your help !!! I agreed with all of your changes while reading the patch file, you're doing a great job !! 

Nathann


---

Comment by ncohen created at 2009-12-01 18:43:35

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-02 09:50:40

Resolution: fixed
