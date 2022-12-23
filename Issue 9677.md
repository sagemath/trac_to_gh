# Issue 9677: Sage Sets don't implement genuine comparison

Issue created by migration from https://trac.sagemath.org/ticket/9677

Original creator: rlm

Original creation time: 2010-08-03 20:41:08

Assignee: AlexGhitza

CC:  kini

Right now there is either equals, or less than. If `a != b`, then we get `a < b` but not `b > a`:

```
sage: a = Set([1])
sage: b = Set([])
sage: a == b
False
sage: a < b
True
sage: b > a
False
```


This came up in

http://groups.google.com/group/sage-devel/browse_thread/thread/1c058efd05d3b91f


---

Comment by nbruin created at 2010-08-04 02:47:10

The noted behaviour is definitely a bug. However, the attached patch solves this by introducing an attempt at inducing a total ordering on Sets by sorting them first by cardinality and then by lexicographic ordering on the sorted list of set elements. This only works if the elements of the set have a total ordering implemented.

While python used to try to have a total ordering on all objects, this has been abandoned (e.g. python complex numbers and python sets)

Shouldn't the sage design follow python in this respect? See also

http://groups.google.ca/group/sage-devel/msg/eab3aafb319a2769


---

Comment by rlm created at 2010-08-04 11:01:16

I completely, emphatically disagree. I think that total orderings are very important to try to preserve wherever possible, especially in this case.


---

Comment by rlm created at 2010-08-04 11:24:32

Replying to [comment:2 rlm]:
> I completely, emphatically disagree. I think that total orderings are very important to try to preserve wherever possible, especially in this case.

See also my comments on the thread referenced above.


---

Comment by rlm created at 2010-08-04 12:57:53

Changing status from new to needs_review.


---

Comment by was created at 2010-08-04 17:02:52

I don't understand why you have these lines:

```
            if len_self != len_other: 
	                return cmp(len_self, len_other) 
```

that just makes it so that the comparison is incompatible with what it is for lists.  Why not just make it the same?


---

Comment by rlm created at 2010-08-04 18:00:19

You mean just remove those lines? That's fine with me. This was just meant to be an optimization.


---

Comment by rlm created at 2010-08-04 18:02:37

Patch is updated.


---

Comment by was created at 2010-08-05 03:05:44

I guess you didn't test your patch?
I just applied it and ran tests on sage.math, and got:

```
----------------------------------------------------------------------
The following tests failed:

        sage -t  devel/sage/sage/graphs/graph_generators.py # 2 doctests failed
        sage -t  devel/sage/sage/graphs/digraph.py # 2 doctests failed
        sage -t  devel/sage/sage/combinat/sf/powersum.py # 0 doctests failed
        sage -t  devel/sage/sage/graphs/graph.py # Time out
----------------------------------------------------------------------
Timings have been updated.
Total time for all tests: 488.9 seconds
```



---

Comment by was created at 2010-08-05 03:05:51

Changing status from needs_review to needs_work.


---

Comment by mhansen created at 2011-12-18 16:09:49

Changing status from needs_work to positive_review.


---

Attachment

I rebased the patch and ran the tests which do pass.  I think we can give this positive review.


---

Comment by dsm created at 2011-12-18 20:36:48

I think the patch behaviour of


```

sage: a = [2,3]
sage: b = [2,3,4j]
sage: set(a) < set(b)
True
sage: Set(a) < Set(b)
False

```


is too dangerous to let pass unremarked.


---

Comment by dsm created at 2011-12-18 20:36:48

Changing status from positive_review to needs_work.


---

Comment by was created at 2012-02-26 17:05:14

Replying to [comment:11 dsm]:
> I think the patch behaviour of
> 
> {{{
> 
> sage: a = [2,3]
> sage: b = [2,3,4j]
> sage: set(a) < set(b)
> True
> sage: Set(a) < Set(b)
> False
> 
> }}}
> 
> is too dangerous to let pass unremarked.

In Python (according to http://docs.python.org/library/sets.html) for the set type we have: "The subset and equality comparisons do not generalize to a complete ordering function. For example, any two disjoint sets are not equal and are not subsets of each other, so all of the following return False: a<b, a==b, or a>b. Accordingly, sets do not implement the __cmp__() method."

The Python convention does make sense and is what most people would expect... and is the direction Sage should move in.

RLM who wrote "I completely, emphatically disagree." has got sucked up into an industry job, so isn't involved in Sage development right now, so I don't think he'll care much what happens with this ticket. 

That said, having a total ordering -- which is different and inconsistent with set's order -- is useful (!).  However, it can be done as a separate explicit function or method, which can get passed to the sort method explicitly.
