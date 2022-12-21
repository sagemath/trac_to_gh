# Issue 6637: Follow up on #6000: standardize the interface to TransitiveIdeal and friends

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-07-27 12:10:47

Assignee: mhansen

CC:  sage-combinat hivert

Keywords: backtrack, enumerated set, transitive closure

Implement a single entry point:


```
     TransitiveClosure(roots, operators = ..., children = , acyclic = True, algo = "DFS", "BFS", internal_nodes = False)
```


for all the functions in sage.combinat.backtrack.py SearchForest, TransitiveIdeal, TransitiveIdealGraded

TODO: discuss the names above


---

Comment by slabbe created at 2013-02-09 17:28:51

Here are some discussions related to this ticket:

 - [TransitiveIdeal vs TransitiveIdealGraded](https://groups.google.com/d/topic/sage-combinat-devel/5Be8FSY5w6I/discussion) on sage-combinat, Feb 2013.

 - [Comment of Nicolas Thiéry at #14052](http://trac.sagemath.org/sage_trac/ticket/14052#comment:7), Feb 2013

 - [SearchForest and post_process...](https://groups.google.com/d/topic/sage-devel/97_5g0Pjuuw/discussion), on sage-devel, Oct. 2012.

 - [Sage modules and forking](https://groups.google.com/d/msg/sage-devel/5XHvEx89RlQ/Tb_QBWepC5YJ) on sage-devel, a comment by Florent Hivert, Oct. 2012.

 - #13580, patch available on sage-combinat : [trac_13580-map_reduce-fh.patch](http://combinat.sagemath.org/patches/file/7e81f6e12973/trac_13580-map_reduce-fh.patch)


---

Comment by slabbe created at 2013-02-09 19:39:07

In a tentative to find good choices for name and so on, here is how I see this.

 - Let X be a set.
 - Let R be a binary relation on X, that is R is a subset of the cartesian product of X times X.
 - Denote by xRy if x is R-related to y.

Now

 - Let `seeds` be a subset of X.
 - Let `succ` be a callable python object `X -> 2^X` such that xRy if and only if y is in `succ(x)`.

We are interested in the subset S of X that can be generated from the `seeds` using the `succ` recursively. More precisely in the set 

 S = {y : x = x1 R x2 R x3 R ... R xn = y and x in `seeds`}.

Moreover, we are interested in the enumeration of S itself and we consider depth-first and breadth-first as different and both usefull.

Such a relation G = (X,R) can be seen as a directed graph. I think this remark is useful as it may provide some vocabulary. Indeed the set S is the connected components of the generators in the digraph G.

I see some different cases :

*1. We do not know anything more about the relation.* We need to save in memory all the `known` objects to avoid duplicates. This is what is currently done in `TransitiveIdeal` (depth-first search) and (curiously) in `TransitiveIdealGraded` (breadth-first search) also.

*2. The directed graph S is a forest with given `seeds`.* Equivalently, one may say that S do not contain cycle (oriented or not). This is what is currently done in `SearchForest`.

*3. The relation is graded.* By graded here I mean what I thought `TransitiveIdealGraded` was doing until I look more carefully at the doc and the code. More seriously, by graded I mean the following : for all (x1 in seeds) and (y1 in seeds), 

 if (x1 R x2 R ... R xn) and (y1 R y2 R ... R ym) and (xn=ym), then (n=m).

The relation is graded if all path from the origin to an element have the same length. In this case, we only need to save in memory the current level.

*4. The relation is symmetric.* If the relation is symmetric, we only need to keep in memory the last two level of depth. This is what I needed and coded this week. And this is why I started to look more carefully at the code in `sage/combinat/backtrack.py`...

That is it for now!


---

Comment by nthiery created at 2013-02-09 19:50:07

I totally agree with the analysis!

I don't know yet what would be the best name for the argument provided by the user to describe the relation. Behind the scene we are definitely modelling relation. But what the user provide is not the relation but a function that computes the (out) neighbors for this relation. If at the end of the day we choose "TransitiveClosure" as name for the main entry point, then "neighbors" would be consistent. If we go for "RecursiveSet" (or RecursiveEnumeratedSet or variant thereof) then "operators" would be consistent.

Cheers,
                           Nicolas


---

Comment by slabbe created at 2013-02-09 20:37:00

I think `relation` would not be too bad for the name of the successor keyword and should be considered as well. In some sense, a binary relation is a function `f: X -> 2^X` and a function is a relation such that `|f(x)|=1` for all x.

Possibilities for successor keyword :

 - `succ` : suitable for non symmetric relation, currently used in `TransitiveIdeal` and `TransitiveIdealGraded`
 - `successors`
 - `operators`
 - `neighbors` : suitable vocabulary for symmetric relation
 - `children` : suitable vocabulary for non symmetric relation, currently used in `SearchForest`.
 - `relatives` : suitable vocabulary for symmetric relation

Possibilities for generators keyword :

 - `generators`
 - `gens`
 - `roots`
 - `seeds`


---

Comment by slabbe created at 2013-02-09 20:55:43

> If we go for RecursiveSet (or RecursiveEnumeratedSet or variant thereof) 

I like RecursiveSet. Maybe RecursiveEnumeratedSet is more related to what we do but is also longer.

Some links:

 - http://en.wikipedia.org/wiki/Recursive_set
 - http://en.wikipedia.org/wiki/Recursively_enumerable_set


---

Comment by slabbe created at 2013-02-09 21:04:01

> I don't know yet what would be the best name for the argument provided by the user to describe the relation.

For the above 4 cases, I would suggest arguments like the following :


```
RecursiveSet(seeds, succ)
RecursiveSet(seeds, succ, structure="forest")
RecursiveSet(seeds, succ, structure="graded")
RecursiveSet(seeds, succ, structure="symmetric")
```



---

Attachment


---

Comment by slabbe created at 2013-02-10 21:10:00

I just added a patch. It implements the `RecursiveSet_symmetric` class and creates factory called `RecursiveSet`. For now, `RecursiveSet` returns either an instance of `TransitiveIdeal`, `SearchForest` or `RecursiveSet_symmetric`. I started an empty class `RecursiveSet_graded`. See examples inside the docstring of the class `RecursiveSet`.

It is not ready for review, but comments are welcome to help me continue this work.

Actually, my questions are : 

 - How should I merge `RecursiveSet` with `TransitiveIdeal` and `SearchForest`?
 - Do we like this interface?


---

Comment by slabbe created at 2014-04-08 13:50:41

New commits:


---

Comment by git created at 2014-04-08 19:07:38

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-04-09 10:41:53

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-04-10 11:23:15

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-04-10 12:21:24

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-04-10 19:26:49

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-04-11 00:01:35

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by slabbe created at 2014-04-11 00:09:36

Changing status from new to needs_review.


---

Comment by git created at 2014-04-11 10:28:58

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-04-13 20:22:57

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-04-13 21:38:21

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by slabbe created at 2014-04-13 21:45:42

I think I will stop now. The next thing to do would be to move code from `sage/combinat/backtrack.py` to `sage/sets/recursively_enumerated_set.py` more precisely, the SearchForest code. But since it is mostly about moving code (does not change any functionality), I suggest to do it in a another ticket and review/merge this ticket now.

Needs review!

Sébastien


---

Comment by slabbe created at 2014-04-15 19:40:40

Changing keywords from "backtrack, enumerated set, transitive closure" to "backtrack, enumerated set, transitive closure, days57".


---

Comment by chapoton created at 2014-05-10 14:59:19

your commits remove completely combinat/all.py ....


---

Comment by chapoton created at 2014-05-10 14:59:19

Changing status from needs_review to needs_work.


---

Comment by slabbe created at 2014-05-10 17:00:17

Replying to [comment:28 chapoton]:
> your commits remove completely combinat/all.py ....

I see. It is strange because I can't see which commit did that... I will investigate.


---

Comment by tscrim created at 2014-05-10 17:30:38

I believe that's an error with the trac plugin (I've seen that before).

Can I make a feature request for this ticket, could we also cythonize this for speed (or at least make the new file a `.pyx` file)?


---

Comment by slabbe created at 2014-05-10 21:43:43

Indeed, there is some gain. I did one example:

Python:


```
sage: f = lambda a: [a-1,a+1]
sage: C = RecursivelyEnumeratedSet([10, 15], f, structure='symmetric')
sage: it = iter(C)
sage: %time L = [next(it) for _ in xrange(10^6)]
CPU times: user 5.82 s, sys: 239 ms, total: 6.06 s
Wall time: 6.07 s
```


Cython:


```
sage: f = lambda a: [a-1,a+1]
sage: C = RecursivelyEnumeratedSet([10, 15], f, structure='symmetric')
sage: it = iter(C)
sage: %time L = [next(it) for _ in xrange(10^6)]
CPU times: user 4.47 s, sys: 408 ms, total: 4.88 s
Wall time: 4.89 s
```



---

Comment by git created at 2014-05-10 22:28:14

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by slabbe created at 2014-05-10 23:50:19

I keep the status of the ticket to needs work because I realized that some doctest were broken in the sage library. I am working on it.


---

Comment by git created at 2014-05-11 00:20:54

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by slabbe created at 2014-05-11 00:30:47

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2014-05-11 01:55:23

Some more speedup by doing some more cythonization. Before:

```
sage: f = lambda a: [a-1,a+1]
sage: C = RecursivelyEnumeratedSet([10, 15], f, structure='symmetric')
sage: it = iter(C)
sage: %time L = [next(it) for _ in xrange(10^6)]
CPU times: user 9.68 s, sys: 147 ms, total: 9.83 s
Wall time: 9.81 s
```

With my commit:

```
sage: f = lambda a: [a-1,a+1]
sage: C = RecursivelyEnumeratedSet([10, 15], f, structure='symmetric')
sage: it = iter(C)
sage: %time L = [next(it) for _ in xrange(10^6)]
CPU times: user 8.02 s, sys: 103 ms, total: 8.13 s
Wall time: 8.15 s
```

I'm sure I haven't done the best cythonization job on this, but it works and all tests pass. If you're happy with my changes, then positive review.
----
New commits:


---

Comment by slabbe created at 2014-05-11 09:02:21

I do gain one more second with your improvements. Great!


```
sage: sage: f = lambda a: [a-1,a+1]                                         
sage: sage: C = RecursivelyEnumeratedSet([10, 15], f, structure='symmetric')
sage: sage: it = iter(C)                                                    
sage: sage: %time L = [next(it) for _ in xrange(10^6)]                      
CPU times: user 3.49 s, sys: 246 ms, total: 3.74 s                          
Wall time: 3.79 s   
```


I do not like factory function in general and was happy to use for the first time the metaclass stuff. But apparently, it is not as efficient? Did you check if only removing the metaclass stuff was giving a speedup?


---

Comment by git created at 2014-05-11 09:29:38

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by slabbe created at 2014-05-11 10:03:29

Travis, did you check that the doc was building fine? I am not able to, I get :


```
$ sage -docbuild reference/structure html
   [structure] WARNING: intersphinx inventory '/Users/slabbe/Applications/sage-git/src/doc/output/html/en/reference/quivers/objects.inv' not fetchable due to <type 'exceptions.IOError'>: [Errno 2] No such file or directory: '/Users/slabbe/Applications/sage-git/src/doc/output/html/en/reference/quivers/objects.inv'
   Error building the documentation.

   Note: incremental documentation builds sometimes cause spurious
   error messages. To be certain that these are real errors, run
   "make doc-clean" first and try again.
   Traceback (most recent call last):
     File "/Users/slabbe/Applications/sage-git/src/doc/common/builder.py", line 1477, in <module>
         getattr(get_builder(name), type)()
           File "/Users/slabbe/Applications/sage-git/src/doc/common/builder.py", line 699, in _wrapper
               getattr(DocBuilder, build_type)(self, *args, **kwds)
                 File "/Users/slabbe/Applications/sage-git/src/doc/common/builder.py", line 94, in f
                     execfile(sys.argv[0])
                       File "/Users/slabbe/Applications/sage-git/src/doc/common/custom-sphinx-build.py", line 210, in <module>
                           raise OSError(ERROR_MESSAGE)
                           OSError: [structure] WARNING: intersphinx inventory '/Users/slabbe/Applications/sage-git/src/doc/output/html/en/reference/quivers/objects.inv' not fetchable due to <type 'exceptions.IOError'>: [Errno 2] No such file or directory: '/Users/slabbe/Applications/sage-git/src/doc/output/html/en/reference/quivers/objects.inv'
```


Once, I may confirm the docs does build fine. I will set this to positive review.


---

Comment by slabbe created at 2014-05-11 10:27:12

`make doc-clean` fixed the error. Doc builds fine.


---

Comment by slabbe created at 2014-05-11 10:27:12

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2014-05-11 14:11:00

Changing status from positive_review to needs_info.


---

Comment by nthiery created at 2014-05-11 14:11:00

Sebastien wants to double check the Metaclass thingy.


---

Comment by tscrim created at 2014-05-11 15:26:01

As I recall, metaclasses are not supported in extension classes by Cython. The metaclass should not change the speed since it's only called/used upon object creation.


---

Comment by tscrim created at 2014-05-11 21:31:56

Also FTR, I liked your usage of the metaclass (and I can't check the doc until I get my docbuilder to actually work again... `:/` ).


---

Comment by slabbe created at 2014-05-12 08:18:03

If you agree Travis, I will try to put the metaclass use back in. Also, maybe Florent can say a word about it. He coached me on how to implement it.


---

Comment by slabbe created at 2014-05-12 09:14:03

Replying to [comment:45 tscrim]:
> As I recall, metaclasses are not supported in extension classes by Cython. The metaclass should not change the speed since it's only called/used upon object creation.

Ok, now I see what you mean. When the class is `cdef`, then the `__classcall_private__` do not get called instead of the `__init__`:


```
sage: f = lambda a: [a-1,a+1]
sage: RecursivelyEnumeratedSet([0], f)
A recursively enumerated set (depth first search)
sage: RecursivelyEnumeratedSet([0], f, structure='symmetric')
Traceback (most recent call last):
...
TypeError: __init__() got an unexpected keyword argument 'structure'
```


I also saw in the [doc](http://www.sagemath.org/doc/reference/misc/sage/misc/classcall_metaclass.html) that: "_For a Cython class (not cdef since they doesn’t allows metaclasses)_"


---

Comment by slabbe created at 2014-05-12 09:53:53

I pushed on my [branch](http://git.sagemath.org/sage.git/diff/?id2=fa885d90d609c8311d8fa52deac1340cd558b5a9&id=38a82f820d5314890a34d0707851c40ea5eb5b67) a [commit](http://git.sagemath.org/sage.git/commit/?h=u/slabbe/6637&id=38a82f820d5314890a34d0707851c40ea5eb5b67) using metaclass. In the end, I had to create a factory def outside of the class...


---

Comment by git created at 2014-05-12 14:59:18

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by tscrim created at 2014-05-12 15:00:31

Looking at your commit, I don't see any benefit in using the metaclass. However I'm not opposed to the renaming, so I've just pushed that.


---

Comment by slabbe created at 2014-05-12 20:33:20

Replying to [comment:51 tscrim]:
> Looking at your commit, I don't see any benefit in using the metaclass. 

Yes exactly. I needed to play with it to understand what you meant.

> However I'm not opposed to the renaming, so I've just pushed that.

Well, the renaming was just an easy way for me to check that `sage -t recursively_enumerated_set.pyx` was ok after I realised that `__classcall_private__` was ignored by `cdef` class. It was not a suggestion, but it would not be the first renamed function:


```
sage: import_statements(sum)
from sage.misc.functional import symbolic_sum
```


So, we go with commit ​dd72bfc instead of ​3191690 ?


---

Comment by tscrim created at 2014-05-12 20:38:05

Changing status from needs_info to needs_review.


---

Comment by tscrim created at 2014-05-12 20:38:05

If that's okay with you.


---

Comment by slabbe created at 2014-05-12 20:51:09

Replying to [comment:53 tscrim]:
> If that's okay with you.

The more I think about it, the less I like it. I think ​dd72bfc can be confusing for someone looking at the file for the first time. Until that person looks at the file sage/sets/all.py he will not understand how the `__init__` handles the structure argument. And the key will always be hidden in some other file `sage/sets/all.py`. I suggest we go with your initial factory function. More precisely with commit ​3191690. Do you agree?

If so, I do not know what should we do then (git question). Should we update the commit field? Should we reset the HEAD of the branch? Should we create a new branch pointing to the commit?


---

Comment by tscrim created at 2014-05-12 20:55:17

Good point. What we'll do is create a new branch which just points to the old commit (afterwards we can delete our old branches). Do you want to do this or should I?


---

Comment by slabbe created at 2014-05-12 20:59:59

Let me try.


---

Comment by slabbe created at 2014-05-12 21:10:32

The following did the trick:


```
git checkout 3191690 -b t/6637a
```



---

Comment by tscrim created at 2014-05-12 21:23:23

Then let's get this in. Thanks Sébastien.


---

Comment by tscrim created at 2014-05-12 21:23:23

Changing status from needs_review to positive_review.


---

Comment by slabbe created at 2014-05-12 21:27:57

Thanks for the review and cython improvements!


---

Comment by vbraun created at 2014-05-13 08:42:15

Resolution: fixed
