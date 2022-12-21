# Issue 8288: Depth/Breadth improvement for SearchForest

Issue created by migration from Trac.

Original creator: nborie

Original creation time: 2010-02-16 22:17:26

Assignee: sage-combinat

CC:  sage-combinat nthiery

Keywords: enumeration depth breadth forest children

The goal of this patch is to include breadth enumeration method for SearchForest...

The interested is for enumerated Set defined by a set of roots and a children function. For a finite set of roots but infinite set (infinite depth of the tree), the breadth method is a necessity.

The breadth method is also a need to define properly indices of infinite Graded algebra (but finite degree by degree). The patch contains method returning iterator of all element of given depth.

Using extra argument : father and next_brother method, it is possible to enumerate not starting from the roots of trees. a _iter_from_to method build an iterator keeping nothing in memory than the first and the last point.


---

Comment by nborie created at 2010-02-16 22:20:31

One more time, my english is still bad... Feel free to point <my langage mistakes> and thus, make my english increasing....


---

Comment by nborie created at 2010-02-16 22:20:31

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-02-17 07:28:52

Hello !! I know nothing about the file sage/combinat/backtrack.py, and I intend to read it as soon as possible but I saw on TRAC the same of this patch, and I was convinced it woukd be using the Graph library : in sage/graphs/base/c_graph.pyx are written iterators for depth/breadth-first-search in general graphs.. Wouldn't it be better for this class to use such functions, are they are written in Cython and should be more efficient ? Or directly use the Graph structure, as it would automatically call these functions.. :-)

Nathann


---

Comment by mhansen created at 2010-02-17 07:37:33

Nathann, using the code the graphs code is not appropriate here as that would require the entire search tree to be created/known beforehand.


---

Comment by ncohen created at 2010-02-17 07:39:33

while it is not... Ok, I got it, then you can forget what I said :-)


---

Comment by hivert created at 2010-03-04 23:12:53

As discussed with Nicolas on irc. the patch needs some cleanup.


---

Comment by hivert created at 2010-03-04 23:12:53

Changing status from needs_review to needs_work.


---

Comment by nborie created at 2010-03-05 00:23:41

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2010-03-05 10:19:16

Discussed on trac: there is an algorithmic problem:
Here is my tests example:

```
    I = SearchForest([This is the Trac macro *3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#3-macro), lambda l: (l+[i] for i in range(l[-1])))
```

Do you have an easy father function for this tree ?
Yes : `lambda l -> l[:-1]`
It simply generate strictly decreasing lists starting with 3.
For me a call to

```
    list(I.element_of_depth_iterator(2, "Children"))
```

raise a `StopIteration` ...
Whereas:

```
    sage: list(I.element_of_depth_iterator(2))
    [[3, 1, 0], [3, 2, 0], [3, 2, 1]]
```



---

Comment by hivert created at 2010-03-05 10:19:16

Changing status from needs_review to needs_work.


---

Comment by nborie created at 2010-03-05 17:10:08

Changing status from needs_work to needs_review.


---

Attachment

One more time, my english is still bad... Feel free to point them and thus, make my english increasing....


---

Attachment


---

Comment by mvngu created at 2010-04-19 02:59:42

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2010-04-19 02:59:42

Don't use the keyword "method" to specify the algorithm to be used. Instead use "algorithm". See #6094 and #7971 for two attempts to get rid of using "method" for specifying the algorithm to be used. My reviewer patch makes this change to your implementation.



For any argument that can take more than one value, provide all the possible values. For example, if possible, list all the possible values for the argument "algorithm".



There is a slight bug in the method `search_forest_iterator()`. If `method="depth"`, then we would use depth-first search. But to get `search_forest_iterator()` to use breadth-first search, we could assign any value to the keyword `method`:


```
sage: from sage.combinat.backtrack import search_forest_iterator
sage: list(search_forest_iterator([[]], lambda l: [l+[0], l+[1]] if len(l) < 3 else [], method="breadth"))
[[], [0], [1], [0, 0], [0, 1], [1, 0], [1, 1], [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
sage: list(search_forest_iterator([[]], lambda l: [l+[0], l+[1]] if len(l) < 3 else [], method=None))
[[], [0], [1], [0, 0], [0, 1], [1, 0], [1, 1], [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
sage: list(search_forest_iterator([[]], lambda l: [l+[0], l+[1]] if len(l) < 3 else [], method="some sanity"))
[[], [0], [1], [0, 0], [0, 1], [1, 0], [1, 1], [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
```


To remedy this bug, we could explicitly test for "breadth" and "depth" and set the value `position` accordingly. For any other value assigned to `algorithm`, we raise an exception. The reviewer patch implements this fix.



There is a slight bug in the method `element_of_depth_iterator()`. From your example given for that method, we can do this:


```
sage: father = lambda t: (t[0]-1,0) if t[1] == 0 else (t[0],t[1]-1)
sage: I = SearchForest([(0,0)], lambda l: [(l[0]+1, l[1]), (l[0], 1)] if l[1] == 0 else [(l[0], l[1]+1)], father=father)
sage: list(I.element_of_depth_iterator(10, method="father"))
[(10, 0), (9, 1), (8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8), (1, 9), (0, 10)]
```


But then, we could assign the keyword `method` with any value and get the same result as above:


```
sage: father = lambda t: (t[0]-1,0) if t[1] == 0 else (t[0],t[1]-1)
sage: I = SearchForest([(0,0)], lambda l: [(l[0]+1, l[1]), (l[0], 1)] if l[1] == 0 else [(l[0], l[1]+1)], father=father)
sage: list(I.element_of_depth_iterator(10, method="mother"))
[(10, 0), (9, 1), (8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8), (1, 9), (0, 10)]
sage: list(I.element_of_depth_iterator(10, method="grandma"))
[(10, 0), (9, 1), (8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8), (1, 9), (0, 10)]
sage: list(I.element_of_depth_iterator(10, method="abc"))
[(10, 0), (9, 1), (8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8), (1, 9), (0, 10)]
```


One way to fix this is to make `full_generation` into a boolean keyword. If `full_generation=True`, the search starts from the root and generate all elements until the given depth is reached. If `full_generation=False`, the search algorithm makes use of the `father` and `next_brother` methods. My reviewer patch makes this change.




Other general remarks:

 * Whenever possible, avoid going over 79 characters per line.
 * When testing for `None`, don't use "!=". Instead use "is not", which is much faster than "!=". The same remark applies when testing for equality of an object with `None`.
 * For the method `first_element_of_depth()`, I don't understand what is the purpose of the keyword "father_with_depth". You need to document that keyword.
 * Some stylistic clean-ups in accordance with [PEP 8](http://www.python.org/dev/peps/pep-0008/).

I have provided a reviewer patch that implements some changes on top of nborie's patch. Someone needs to review the technical aspect of the features implemented by nborie's patch.


---

Comment by hivert created at 2010-06-02 14:41:40

Hi Nicolas,

I'm currently using search forest and I run into some troubles... I also want
to suggest some improvements in the code:

 - please define method `_repr_` (Sage way) rather than `__repr__`
   (Python's way).

 - when you need to link a class in the same file you don't have to give the
   full path for exampe `:class:`SearchForest`` is sufficient compared to
   `:class:`~sage.combinat.backtrack.SearchForest``

 - please make sure and *document* that a common intended use of
   `SearchForest` is to inherit from it, calling only
   `Parent.__init__` and overload the methods 
   `roots, children, post_process` rather than passing them to the constructors. 
   Please make sure to specify their result type (iterable vs. iterator).
   By the way, should'nt those methods be private methods (eg: `_roots`
   vs. `roots`. I don't expect the user to call them in my use-case.

Thanks for all this ! I'm using it...

Florent


---

Comment by nborie created at 2010-06-02 15:28:15

I upload a patch for this ticket to be discussed on http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/fbedf039a549c68b

Thanks for your comments Florent.

Nicolas.


---

Comment by nborie created at 2010-06-04 14:32:48

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2010-06-07 16:43:33

Replying to [comment:13 nborie]:

Some more remarks: please check your sphinx markup:

 - ``...`` is for mathematic ie is set up by TeX
 - ```...``` is for Sage/Python code. There are some ``__init__`` which doesn't compile.


---

Comment by hivert created at 2010-06-07 16:43:33

Changing status from needs_review to needs_work.


---

Comment by nborie created at 2010-07-13 16:12:52

Changing status from needs_work to needs_review.


---

Comment by nborie created at 2010-07-13 16:12:52

the last trac_8288_search_forest_depth_and_breath_improvement-nb.patch is ready from my side...


---

Comment by nborie created at 2010-08-01 23:42:04

rebased for 4.5.1


---

Comment by mhansen created at 2010-11-26 02:07:12

I put a patch up with some minor changes on the patch server.  Do you want to fold them into your patch.

Florent, what is the status of this ticket?


---

Comment by nborie created at 2010-11-26 10:59:56

Thanks Mike for yours changes.

I folded your patch in mine and uploaded it to the trac. I also just checked (one more time) it apply well on 4.6, that all the tests pass and the doc seems fine to me (accordingly I am a bad English language reviewer).

It will be fine to finalize this work... (Was this point in your TODO list Nicolas ?)


---

Comment by nthiery created at 2010-11-29 13:04:46

Yes: we should just take 1/2 hour shortly to finalize this together.


---

Comment by nborie created at 2011-01-19 11:57:04

Sorry for this post but with some hope that the buildbot take in care :

apply trac_8288_search_forest_depth_and_breath_improvement-nb.patch


---

Comment by nthiery created at 2011-03-24 11:07:41

Hi Nicolas,

I just made a couple minor improvements to the documentation on the sage-combinat patch server (directly in your patch). Please have a quick look, upload the new version to trac, and set a positive review on my behalf if you agree with my changes.

Cheers,
                Nicolas


---

Attachment


---

Comment by nborie created at 2011-03-24 17:08:03

It is ok with your changes. Let it go in!


---

Comment by nborie created at 2011-03-24 17:08:03

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2011-03-24 17:51:41

Oh my GOD `O_O`

This ticket is reviewed !! `O_O`

Well done `:-)`

Nathann


---

Comment by jdemeyer created at 2011-04-07 13:48:05

Resolution: fixed
