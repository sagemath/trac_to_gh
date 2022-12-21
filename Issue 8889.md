# Issue 8889: multidim'l enumeration over variable length tuples

Issue created by migration from Trac.

Original creator: ecurry

Original creation time: 2010-05-05 15:55:21

Assignee: jason

CC:  sage-combinat

I would like a function that takes
Input: range (a list)
       dim (a positive integer)
Output: a list of vectors or tuples of length dim including all combinations of range, but with replacement

Example: generate the vertices of the centered unit cube [-1/2,1/2]^dim, where dim is variable

The functions in sage.misc.mrange almost do this, except it seems that they require having dim specified ahead of time, whereas I want a function that I can call in another function where dim will vary.

The function Arrangements in sage.combinat.permutation almost does what I want, but the list that the digits of the tuple are chosen from must be larger than dim, and Arrangements selects without replacement.  I can solve my example problem using Arrangements as follows:

```
prelist=[]
for i in range(2**d):
    if i-2**(d-1) >= 0: prelist.append(1)
        else: prelist.append(-1)
list = (1/2)*matrix(Arrangements(prelist,d).list())
```

but it seems like there should be one specific function for this.

(Combinations and Permutations are also related, but don't quite do what I want.)


---

Comment by mhansen created at 2010-05-05 17:25:11

Does this do what you want?


```
sage: l = [1/2, -1/2]
sage: CartesianProduct(*([l]*3)).list()
[[1/2, 1/2, 1/2], [1/2, 1/2, -1/2], [1/2, -1/2, 1/2], [1/2, -1/2, -1/2], [-1/2, 1/2, 1/2], [-1/2, 1/2, -1/2], [-1/2, -1/2, 1/2], [-1/2, -1/2, -1/2]]
sage: CartesianProduct(*([l]*2)).list()
[[1/2, 1/2], [1/2, -1/2], [-1/2, 1/2], [-1/2, -1/2]]
```



---

Comment by jason created at 2010-05-05 17:34:11

It would be really nice if CartesianProduct supported a repeat keyword, like the python itertools product function does:


```

sage: import itertools                      
sage: list(itertools.product([1/2,-1/2],repeat=3))
[(1/2, 1/2, 1/2), (1/2, 1/2, -1/2), (1/2, -1/2, 1/2), (1/2, -1/2, -1/2), (-1/2, 1/2, 1/2), (-1/2, 1/2, -1/2), (-1/2, -1/2, 1/2), (-1/2, -1/2, -1/2)]
```


That would make a common case (cartesian product of a set with itself) much easier to read.


---

Comment by ecurry created at 2010-05-05 17:54:42

That does!  Sorry for opening the unnecessary ticket then.
-Eva

Replying to [comment:1 mhansen]:
> Does this do what you want?
> 
> {{{
> sage: l = [1/2, -1/2]
> sage: CartesianProduct(*([l]*3)).list()
> [[1/2, 1/2, 1/2], [1/2, 1/2, -1/2], [1/2, -1/2, 1/2], [1/2, -1/2, -1/2], [-1/2, 1/2, 1/2], [-1/2, 1/2, -1/2], [-1/2, -1/2, 1/2], [-1/2, -1/2, -1/2]]
> sage: CartesianProduct(*([l]*2)).list()
> [[1/2, 1/2], [1/2, -1/2], [-1/2, 1/2], [-1/2, -1/2]]
> }}}


---

Comment by mhansen created at 2010-05-05 18:53:57

Changing status from new to needs_review.


---

Attachment

I've added a patch which adds the repeat keyword.


---

Comment by mhansen created at 2010-05-05 18:54:15

Changing component from misc to combinatorics.


---

Comment by ecurry created at 2010-05-06 00:25:40

There is also Tuples in sage.combinat.tuple:
http://sagemath.org/doc/reference/sage/combinat/tuple.html


---

Comment by mhansen created at 2010-05-06 01:48:04

Replying to [comment:6 ecurry]:
> There is also Tuples in sage.combinat.tuple:
> http://sagemath.org/doc/reference/sage/combinat/tuple.html

Heh, I should have known about that since it was likely I who wrote it :-)


---

Comment by mhansen created at 2010-06-22 21:57:06

I'm going to close this as invalid for now.  If we have a discussion and decide we really want to repeat option to CartesianProduct, then we can add it.


---

Comment by mhansen created at 2010-06-22 21:57:06

Resolution: invalid


---

Comment by jason created at 2010-06-23 00:49:58

Wait!  Are you closing it because no one has reviewed it?  If so, I'll review it.  I've been wanting the repeat keyword for a long time, as it just feels like a big mess when I want to take the cartesian product of a set with itself a number of times.  It's much easier with the repeat keyword, especially since python supports that in the python equivalent.
