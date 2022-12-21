# Issue 3283: [with patch, needs review] fix some memholes in PolyBoRi interface

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-05-23 17:10:11

Assignee: malb

CC:  burcin polybori

Keywords: PolyBoRi, memleak

All PolyBoRi iterators only destruct the iterator objects but never the object they act on. However, since we assign objects and not pointers/references a copy is triggered during creation and thus the destructor of the object ought to be called on self destruction of the iterator. So far the theory. In practice, while I didn't see any problems, I'd appreciate if somebody with more intime knowledge of the interface would take a careful look.


---

Attachment


---

Comment by PolyBoRi created at 2008-05-23 21:09:30

Ok, if one cannot force to use references here (I'm sorry, I've no experience, what can be done within pyx-files.), one has to clean up after oneself. The internal PolyBoRi data structures use reference counting, so the missing destructor resulted in the fact, that the reference count was never decreased -> memleak. (On C++ all of this is done automatically.) So from my point of view this patch is ok.

But we should wait for Burcin's opinion, as he knows best.

Also, one should check somewhen, whether the object is still necessary in the interface for recent PolyBoRi.

Best regards,
  Alexander


---

Comment by burcin created at 2008-05-24 09:13:30

The iterator wrappers keep a reference to the objects only to be able to check if the iterator reaches the end. As in the following (from `BooleanMonomialVariableIterator.__next__`):


```
if self.iter.equal(self.obj.variableEnd()):
    raise StopIteration
```


The objects that iterators act on are wrapped by python objects, e.g. there is a corresponding `BooleanMonomial` object associated to the `PBMonom` the iterator is acting on. Python should keep track of the memory of `BooleanMonomial`, so python will deallocate that `PBMonom` by calling the `__dealloc__` method of `BooleanMonomial`. Calling the destructor of `PBMonom` from any other place would lead to segfaults.

Actually, it might be a good idea to add a reference to the `BooleanMonomial` object in the iterator as well. We wouldn't want python to garbage collect that while the iterator is still around. 

Another problem you might want to ponder: We don't explicitly call the constructor of any iterator other than that of `BooleSet`, yet we still call their destructors. If we need to call the constructor, how do we get away without it most of the time? If we don't, why is `BooleSet` special?

Comments?


---

Comment by PolyBoRi created at 2008-05-24 22:39:01

> The iterator wrappers keep a reference to the objects only to be able to check if the iterator reaches the end. As in the following (from `BooleanMonomialVariableIterator.__next__`):
> 
> {{{
> if self.iter.equal(self.obj.variableEnd()):
>     raise StopIteration
> }}}
If that's the only reason for the object, we could add some kind of isEnd() and skip the reference. If fact, the PolyBoRi-Iterators have the member function isZero(), which is equivalent to this. 

> The objects that iterators act on are wrapped by python objects, e.g. there is a corresponding `BooleanMonomial` object associated to the `PBMonom` the iterator is acting on. Python should keep track of the memory of `BooleanMonomial`, so python will deallocate that `PBMonom` by calling the `__dealloc__` method of `BooleanMonomial`. Calling the destructor of `PBMonom` from any other place would lead to segfaults.
Do I understand you right: the patch is not correct, because the destructor of the PolyBoRi monomial must not be called at that place? But, since there is a memleak, the destructor not called correctly. So why, does the destruction of the 

> Actually, it might be a good idea to add a reference to the `BooleanMonomial` object in the iterator as well. We wouldn't want python to garbage collect that while the iterator is still around. 
The iterators (upstream at C++) carry all references, which are need by them. For iterators in lexicographical rings, this is very much like - for instance -  std::vector-iterators, which do not have knowledge of the vector they belong to. (The degree-lexicographical have internal references to the polynomial structure.)
But using "isZero()" avoid the problem anyway.

> Another problem you might want to ponder: We don't explicitly call the constructor of any iterator other than that of `BooleSet`, yet we still call their destructors. If we need to call the constructor, how do we get away without it most of the time? If we don't, why is `BooleSet` special?
Good question, the iterators, which obey the ring ordering, like the iterators of polynomials, are wrapped by a shread-pointer construction, which is not the case for BooleSet iterators. Does that make any difference? 
What actually happens, if you use code like the one from new_BPI_from_PBPolyIter for
new_BSI_from_PBSetIter (including the function arguments)?

I still have few experience in pyx code, but any kind of differences between the iterator types should not make any problems, because in both cases constructors, copy-constructors and destructors care for the memory management on c++-side. 

Best regards,
  Alexander


---

Comment by PolyBoRi created at 2008-05-24 22:44:30

Sorry, to late:


>  So why, does the destruction of the 
-> So why, is the destruction of the not called by the object itself?


>  shread-pointer
-> shared pointer 
 
Best regards,
  Alexander


---

Comment by malb created at 2008-05-25 13:06:02

So the strategy is either of the following?
 * get rid of the reference to the C++ object alltogether since the iterators have a method to check for the end anyway
 * add a reference to the Python Object rather than the C++ object and let Python do the refcounting?
 * apply this patch since either assignment causes a copy and we need to destruct or it adds a reference and increases the refcount, right?


---

Attachment


---

Comment by malb created at 2008-05-25 13:53:19

The attached patch removes all `.obj` members from the iterators and replaces them with `._end` members. Happy reviewing.


---

Attachment

remove object references from BooleanPolynomialIterator


---

Comment by burcin created at 2008-05-25 19:40:18

attachment:trac3283_bpi_object_reference.patch removes the object reference from `BooleanPolynomialIterator` as well. It should be applied after attachment:pbori_memleak_nex_attempt.patch.

I give a positive review to Martin's patch, now someone needs to review mine. :)


---

Comment by PolyBoRi created at 2008-05-25 20:19:50

Hm, I wouldn't have added this _end member, because one could check for equality using that iZero() member from the original PolyBoRi-Iterator. If access to this member function is too complicated, the results of end() could be generated on the fly, as they are the same as result from the default constructors. (But indeed, this could change somewhen...)

Off-Trac Michael B. mentioned, that removing the object completely might cause problems. The object may be deleted meanwhile, and hence, the (C++-) iterator may become invalid.

Best regards,
  Alexander


---

Comment by malb created at 2008-05-25 20:27:25

So we remove the `_end` members and add a Python level reference to the original object (polynomial, monomial, set). This should prevent the GC from killing the original object.


---

Comment by burcin created at 2008-05-25 20:49:06

Replying to [comment:9 PolyBoRi]:
> Hm, I wouldn't have added this _end member, because one could check for equality using that iZero() member from the original PolyBoRi-Iterator. If access to this member function is too complicated, the results of end() could be generated on the fly, as they are the same as result from the default constructors. (But indeed, this could change somewhen...)

Which iterators have an `isZero()` function? I tried using that for `BooleanMonomialIterator` and `BooleanMonomialVariableIterator` while I was reviewing Martin's patch. (The `PolyBoRi` equivalent of) `BooleanMonomialIterator` had an isEmpty() method, because of it's base class CCuddNavigator. However, the variable iterator didn't. I didn't test to see if `BooleanMonomialIterator` worked as intended with the `isEmpty()` method.


---

Comment by PolyBoRi created at 2008-05-25 21:46:36

You are right, my postings were isleading. 
In my last comment, I wanted to say that
`BoolePolynomial::const_iterator`  (`BooleanPolynomialIterator`) has the `isZero()` functionality, which could already be used in attachment:trac3283_bpi_object_reference.patch.
(For `BooleanMonomialIterator` `isValid()` does the job, but 
`BooleanMonomialVariableIterator`, does not own it.)

In comment 3, I had meant, that I could add such some kind of `isEnd()` function upstream, for instance using `isZero()` for `BoolePolynomial::const_iterator`. 

But now - after all these confusions - I must admit, that I first have to add this functionality to have a consistent interface for this test on all PolyBoRi iterators.

I apologize for the trouble caused,
  Alexander


---

Comment by craigcitro created at 2008-06-20 04:57:08

Changing keywords from "PolyBoRi, memleak" to "PolyBoRi, memleak, editor_malb".


---

Comment by malb created at 2008-06-25 11:17:39

*state of affairs for editoral meeting 26/06/08*

I need to fix the code, possibly by next week.


---

Comment by malb created at 2008-06-28 15:55:27

Next attempt attached:
 * Python references to parent object
 * some docstrings added
 * I checked for memleaks with this patch and didn't find any in my short tests

Burcin, can you review my patch?


---

Comment by burcin created at 2008-07-04 17:53:21

Two small problems:
 * adding `equal` to `ctypedef struct PBPolyVectorIter` seems to be redundant.
 * `BooleanPolynomialVectorIterator` does not deallocate `self._end`

Other than these a very positive review. Thanks for sorting out the iterators in the polybori wrapper malb. :)


---

Comment by malb created at 2008-07-06 12:17:55

new version addresses burcin's review


---

Attachment

Since the pending changes are in the updated patch, I give the patch a positive review.


---

Comment by mabshoff created at 2008-07-06 19:11:48

Merged pbori_iterators.patch in Sage 3.0.4.alpha2


---

Comment by mabshoff created at 2008-07-06 19:11:48

Resolution: fixed
