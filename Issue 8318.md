# Issue 8318: overlap_partion of a word should return an instance disjoint set data structure

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2010-02-21 02:27:56

Assignee: sage-combinat

CC:  abmasse

When I coded the `overlap_partition` function in 2007, the purpose was to study equations on words. But, when the sage-words code was merged into sage in december 2008, the disjoint set data structure was not ready so that sage-words got merged without it. That is why `overlap_partition` returns a set of sets (and also why I don't use the function ever since then).

The disjoint set data structure got merged into sage recently : #6775. So this patch changes the behavior of `overlap_partition` to its initial goal.

BEFORE (sage-4.3.2):


```
sage: w = Words(range(10))(range(10))
sage: w.overlap_partition(w,3)
{{0, 9, 3, 6}, {1, 4, 7}, {8, 2, 5}}
sage: 
sage: type(_)
<class 'sage.sets.set.Set_object_enumerated'>
```


WITH THE PATCH:

The following example illustrates that a word that overlaps with itself has a period :


```
sage: w = Words(range(10))(range(10))
sage: p = w.overlap_partition(w, 3)
sage: type(p)
<type 'sage.sets.disjoint_set.DisjointSet_of_hashables'>
sage: d = p.element_to_root_dict()
sage: m = WordMorphism(d)
sage: print m
WordMorphism: 0->3, 1->4, 2->5, 3->3, 4->4, 5->5, 6->3, 7->4, 8->5, 9->3
sage: m(w)
word: 3453453453
```


The following example shows that if the image of a word under an involution f overlaps its square, then it is f-symmetric i.e. the product of two f-palindromes :


```
sage: W = Words([-11,-9,..,11])
sage: w = W([1,3,..,11])
sage: w
word: 1,3,5,7,9,11
sage: inv = lambda x:-x
sage: f = WordMorphism(dict( (a, inv(a)) for a in W.alphabet()))
sage: print f
WordMorphism: -1->1, -11->11, -3->3, -5->5, -7->7, -9->9, 1->-1, 11->-11, 3->-3, 5->-5, 7->-7, 9->-9
sage: p = (w*w).overlap_partition(f(w).reversal(), 2, involution=inv)
sage: m = WordMorphism(p.element_to_root_dict())
sage: m(w)
word: 1,-1,5,7,-7,-5
sage: m(w).is_symmetric(f)
True
```





---

Comment by slabbe created at 2010-02-21 02:36:49

Changing status from new to needs_review.


---

Comment by abmasse created at 2010-02-23 22:16:33

Hello, Sébastien !

I tested your patch and generated the documentation. I have some comments on the latter:

1. The first sentence appears kind of complicated.

  Returns the partition of the alphabet induced by the equivalence relation obtained
  from the symmetric, reflexive and transitive closure of the set of pairs of letters
  R_{self,other,delay}\cup p defined below.

I suggest something like:

  Returns the partition over the alphabet induced by overlapping the words self
  and other with given delay.

Then you give the formal definition and the example.

2. In the example, it is not clear how the words `cheval` and `abcdef` overlap. It could be better to use a constant width character font if possible.

3. You should give more details about what the involution is there for.

4. Same comment about parameter `p`. I prefer more significant name (in that case, maybe `partition` ?) and it would be nice to know what `p` is used for (I guess it's a partition corresponding to already equivalent letters ?)

That's all for now. The rest seems fine. As soon as you fix the documentation according to my comments, I'll resume the review.


---

Comment by abmasse created at 2010-02-23 22:16:33

Changing status from needs_review to needs_work.


---

Comment by abmasse created at 2010-02-23 22:16:33

Changing keywords from "" to "equation, words, partition".


---

Comment by slabbe created at 2010-02-28 18:13:55

Changing status from needs_work to needs_review.


---

Attachment

I fixed the documentation. Needs review!


---

Comment by abmasse created at 2010-03-01 13:24:18

I'm done with the review. All tests passed, I corrected a minor error in the documentation. The code makes sense. Positive review.


---

Attachment

one-character review -- apply on top of the first patch


---

Comment by abmasse created at 2010-03-01 13:25:17

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-02 21:35:05

Merged in this order:

 1. [trac_8318_overlap_partition-sl.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8318/trac_8318_overlap_partition-sl.patch)
 1. [trac_8313_review-abm.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8318/trac_8313_review-abm.patch)


---

Comment by mvngu created at 2010-03-02 21:35:05

Resolution: fixed
