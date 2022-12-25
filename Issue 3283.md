# Issue 3283: [with patch, needs review] fix some memholes in PolyBoRi interface

archive/issues_003283.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @burcin polybori\n\nKeywords: PolyBoRi, memleak\n\nAll PolyBoRi iterators only destruct the iterator objects but never the object they act on. However, since we assign objects and not pointers/references a copy is triggered during creation and thus the destructor of the object ought to be called on self destruction of the iterator. So far the theory. In practice, while I didn't see any problems, I'd appreciate if somebody with more intime knowledge of the interface would take a careful look.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3283\n\n",
    "created_at": "2008-05-23T17:10:11Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch, needs review] fix some memholes in PolyBoRi interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3283",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @burcin polybori

Keywords: PolyBoRi, memleak

All PolyBoRi iterators only destruct the iterator objects but never the object they act on. However, since we assign objects and not pointers/references a copy is triggered during creation and thus the destructor of the object ought to be called on self destruction of the iterator. So far the theory. In practice, while I didn't see any problems, I'd appreciate if somebody with more intime knowledge of the interface would take a careful look.

Issue created by migration from https://trac.sagemath.org/ticket/3283





---

archive/issue_comments_022654.json:
```json
{
    "body": "Attachment [pbori_memleak.patch](tarball://root/attachments/some-uuid/ticket3283/pbori_memleak.patch) by mabshoff created at 2008-05-23 18:15:38",
    "created_at": "2008-05-23T18:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3283#issuecomment-22654",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [pbori_memleak.patch](tarball://root/attachments/some-uuid/ticket3283/pbori_memleak.patch) by mabshoff created at 2008-05-23 18:15:38



---

archive/issue_comments_022655.json:
```json
{
    "body": "Ok, if one cannot force to use references here (I'm sorry, I've no experience, what can be done within pyx-files.), one has to clean up after oneself. The internal PolyBoRi data structures use reference counting, so the missing destructor resulted in the fact, that the reference count was never decreased -> memleak. (On C++ all of this is done automatically.) So from my point of view this patch is ok.\n\nBut we should wait for Burcin's opinion, as he knows best.\n\nAlso, one should check somewhen, whether the object is still necessary in the interface for recent PolyBoRi.\n\nBest regards,\n  Alexander",
    "created_at": "2008-05-23T21:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3283#issuecomment-22655",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

Ok, if one cannot force to use references here (I'm sorry, I've no experience, what can be done within pyx-files.), one has to clean up after oneself. The internal PolyBoRi data structures use reference counting, so the missing destructor resulted in the fact, that the reference count was never decreased -> memleak. (On C++ all of this is done automatically.) So from my point of view this patch is ok.

But we should wait for Burcin's opinion, as he knows best.

Also, one should check somewhen, whether the object is still necessary in the interface for recent PolyBoRi.

Best regards,
  Alexander



---

archive/issue_comments_022656.json:
```json
{
    "body": "The iterator wrappers keep a reference to the objects only to be able to check if the iterator reaches the end. As in the following (from `BooleanMonomialVariableIterator.__next__`):\n\n\n```\nif self.iter.equal(self.obj.variableEnd()):\n    raise StopIteration\n```\n\n\nThe objects that iterators act on are wrapped by python objects, e.g. there is a corresponding `BooleanMonomial` object associated to the `PBMonom` the iterator is acting on. Python should keep track of the memory of `BooleanMonomial`, so python will deallocate that `PBMonom` by calling the `__dealloc__` method of `BooleanMonomial`. Calling the destructor of `PBMonom` from any other place would lead to segfaults.\n\nActually, it might be a good idea to add a reference to the `BooleanMonomial` object in the iterator as well. We wouldn't want python to garbage collect that while the iterator is still around. \n\nAnother problem you might want to ponder: We don't explicitly call the constructor of any iterator other than that of `BooleSet`, yet we still call their destructors. If we need to call the constructor, how do we get away without it most of the time? If we don't, why is `BooleSet` special?\n\nComments?",
    "created_at": "2008-05-24T09:13:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3283#issuecomment-22656",
    "user": "https://github.com/burcin"
}
```

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

archive/issue_comments_022657.json:
```json
{
    "body": "> The iterator wrappers keep a reference to the objects only to be able to check if the iterator reaches the end. As in the following (from `BooleanMonomialVariableIterator.__next__`):\n> \n> {{{\n> if self.iter.equal(self.obj.variableEnd()):\n>     raise StopIteration\n> }}}\nIf that's the only reason for the object, we could add some kind of isEnd() and skip the reference. If fact, the PolyBoRi-Iterators have the member function isZero(), which is equivalent to this. \n\n> The objects that iterators act on are wrapped by python objects, e.g. there is a corresponding `BooleanMonomial` object associated to the `PBMonom` the iterator is acting on. Python should keep track of the memory of `BooleanMonomial`, so python will deallocate that `PBMonom` by calling the `__dealloc__` method of `BooleanMonomial`. Calling the destructor of `PBMonom` from any other place would lead to segfaults.\nDo I understand you right: the patch is not correct, because the destructor of the PolyBoRi monomial must not be called at that place? But, since there is a memleak, the destructor not called correctly. So why, does the destruction of the \n\n> Actually, it might be a good idea to add a reference to the `BooleanMonomial` object in the iterator as well. We wouldn't want python to garbage collect that while the iterator is still around. \nThe iterators (upstream at C++) carry all references, which are need by them. For iterators in lexicographical rings, this is very much like - for instance -  std::vector-iterators, which do not have knowledge of the vector they belong to. (The degree-lexicographical have internal references to the polynomial structure.)\nBut using \"isZero()\" avoid the problem anyway.\n\n> Another problem you might want to ponder: We don't explicitly call the constructor of any iterator other than that of `BooleSet`, yet we still call their destructors. If we need to call the constructor, how do we get away without it most of the time? If we don't, why is `BooleSet` special?\nGood question, the iterators, which obey the ring ordering, like the iterators of polynomials, are wrapped by a shread-pointer construction, which is not the case for BooleSet iterators. Does that make any difference? \nWhat actually happens, if you use code like the one from new_BPI_from_PBPolyIter for\nnew_BSI_from_PBSetIter (including the function arguments)?\n\nI still have few experience in pyx code, but any kind of differences between the iterator types should not make any problems, because in both cases constructors, copy-constructors and destructors care for the memory management on c++-side. \n\nBest regards,\n  Alexander",
    "created_at": "2008-05-24T22:39:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3283#issuecomment-22657",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

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

archive/issue_comments_022658.json:
```json
{
    "body": "Sorry, to late:\n\n\n>  So why, does the destruction of the \n-> So why, is the destruction of the not called by the object itself?\n\n\n>  shread-pointer\n-> shared pointer \n \nBest regards,\n  Alexander",
    "created_at": "2008-05-24T22:44:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3283#issuecomment-22658",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

Sorry, to late:


>  So why, does the destruction of the 
-> So why, is the destruction of the not called by the object itself?


>  shread-pointer
-> shared pointer 
 
Best regards,
  Alexander



---

archive/issue_comments_022659.json:
```json
{
    "body": "So the strategy is either of the following?\n* get rid of the reference to the C++ object alltogether since the iterators have a method to check for the end anyway\n* add a reference to the Python Object rather than the C++ object and let Python do the refcounting?\n* apply this patch since either assignment causes a copy and we need to destruct or it adds a reference and increases the refcount, right?",
    "created_at": "2008-05-25T13:06:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3283#issuecomment-22659",
    "user": "https://github.com/malb"
}
```

So the strategy is either of the following?
* get rid of the reference to the C++ object alltogether since the iterators have a method to check for the end anyway
* add a reference to the Python Object rather than the C++ object and let Python do the refcounting?
* apply this patch since either assignment causes a copy and we need to destruct or it adds a reference and increases the refcount, right?



---

archive/issue_comments_022660.json:
```json
{
    "body": "Attachment [pbori_memleak_nex_attempt.patch](tarball://root/attachments/some-uuid/ticket3283/pbori_memleak_nex_attempt.patch) by @malb created at 2008-05-25 13:52:30",
    "created_at": "2008-05-25T13:52:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3283#issuecomment-22660",
    "user": "https://github.com/malb"
}
```

Attachment [pbori_memleak_nex_attempt.patch](tarball://root/attachments/some-uuid/ticket3283/pbori_memleak_nex_attempt.patch) by @malb created at 2008-05-25 13:52:30



---

archive/issue_comments_022661.json:
```json
{
    "body": "The attached patch removes all `.obj` members from the iterators and replaces them with `._end` members. Happy reviewing.",
    "created_at": "2008-05-25T13:53:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3283#issuecomment-22661",
    "user": "https://github.com/malb"
}
```

The attached patch removes all `.obj` members from the iterators and replaces them with `._end` members. Happy reviewing.



---

archive/issue_comments_022662.json:
```json
{
    "body": "Attachment [trac3283_bpi_object_reference.patch](tarball://root/attachments/some-uuid/ticket3283/trac3283_bpi_object_reference.patch) by @burcin created at 2008-05-25 19:36:13\n\nremove object references from BooleanPolynomialIterator",
    "created_at": "2008-05-25T19:36:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3283#issuecomment-22662",
    "user": "https://github.com/burcin"
}
```

Attachment [trac3283_bpi_object_reference.patch](tarball://root/attachments/some-uuid/ticket3283/trac3283_bpi_object_reference.patch) by @burcin created at 2008-05-25 19:36:13

remove object references from BooleanPolynomialIterator



---

archive/issue_comments_022663.json:
```json
{
    "body": "attachment:trac3283_bpi_object_reference.patch removes the object reference from `BooleanPolynomialIterator` as well. It should be applied after attachment:pbori_memleak_nex_attempt.patch.\n\nI give a positive review to Martin's patch, now someone needs to review mine. :)",
    "created_at": "2008-05-25T19:40:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3283#issuecomment-22663",
    "user": "https://github.com/burcin"
}
```

attachment:trac3283_bpi_object_reference.patch removes the object reference from `BooleanPolynomialIterator` as well. It should be applied after attachment:pbori_memleak_nex_attempt.patch.

I give a positive review to Martin's patch, now someone needs to review mine. :)



---

archive/issue_comments_022664.json:
```json
{
    "body": "Hm, I wouldn't have added this _end member, because one could check for equality using that iZero() member from the original PolyBoRi-Iterator. If access to this member function is too complicated, the results of end() could be generated on the fly, as they are the same as result from the default constructors. (But indeed, this could change somewhen...)\n\nOff-Trac Michael B. mentioned, that removing the object completely might cause problems. The object may be deleted meanwhile, and hence, the (C++-) iterator may become invalid.\n\nBest regards,\n  Alexander",
    "created_at": "2008-05-25T20:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3283#issuecomment-22664",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

Hm, I wouldn't have added this _end member, because one could check for equality using that iZero() member from the original PolyBoRi-Iterator. If access to this member function is too complicated, the results of end() could be generated on the fly, as they are the same as result from the default constructors. (But indeed, this could change somewhen...)

Off-Trac Michael B. mentioned, that removing the object completely might cause problems. The object may be deleted meanwhile, and hence, the (C++-) iterator may become invalid.

Best regards,
  Alexander



---

archive/issue_comments_022665.json:
```json
{
    "body": "So we remove the `_end` members and add a Python level reference to the original object (polynomial, monomial, set). This should prevent the GC from killing the original object.",
    "created_at": "2008-05-25T20:27:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3283#issuecomment-22665",
    "user": "https://github.com/malb"
}
```

So we remove the `_end` members and add a Python level reference to the original object (polynomial, monomial, set). This should prevent the GC from killing the original object.



---

archive/issue_comments_022666.json:
```json
{
    "body": "Replying to [comment:9 PolyBoRi]:\n> Hm, I wouldn't have added this _end member, because one could check for equality using that iZero() member from the original PolyBoRi-Iterator. If access to this member function is too complicated, the results of end() could be generated on the fly, as they are the same as result from the default constructors. (But indeed, this could change somewhen...)\n\nWhich iterators have an `isZero()` function? I tried using that for `BooleanMonomialIterator` and `BooleanMonomialVariableIterator` while I was reviewing Martin's patch. (The `PolyBoRi` equivalent of) `BooleanMonomialIterator` had an isEmpty() method, because of it's base class CCuddNavigator. However, the variable iterator didn't. I didn't test to see if `BooleanMonomialIterator` worked as intended with the `isEmpty()` method.",
    "created_at": "2008-05-25T20:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3283#issuecomment-22666",
    "user": "https://github.com/burcin"
}
```

Replying to [comment:9 PolyBoRi]:
> Hm, I wouldn't have added this _end member, because one could check for equality using that iZero() member from the original PolyBoRi-Iterator. If access to this member function is too complicated, the results of end() could be generated on the fly, as they are the same as result from the default constructors. (But indeed, this could change somewhen...)

Which iterators have an `isZero()` function? I tried using that for `BooleanMonomialIterator` and `BooleanMonomialVariableIterator` while I was reviewing Martin's patch. (The `PolyBoRi` equivalent of) `BooleanMonomialIterator` had an isEmpty() method, because of it's base class CCuddNavigator. However, the variable iterator didn't. I didn't test to see if `BooleanMonomialIterator` worked as intended with the `isEmpty()` method.



---

archive/issue_comments_022667.json:
```json
{
    "body": "You are right, my postings were isleading. \nIn my last comment, I wanted to say that\n`BoolePolynomial::const_iterator`  (`BooleanPolynomialIterator`) has the `isZero()` functionality, which could already be used in attachment:trac3283_bpi_object_reference.patch.\n(For `BooleanMonomialIterator` `isValid()` does the job, but \n`BooleanMonomialVariableIterator`, does not own it.)\n\nIn comment 3, I had meant, that I could add such some kind of `isEnd()` function upstream, for instance using `isZero()` for `BoolePolynomial::const_iterator`. \n\nBut now - after all these confusions - I must admit, that I first have to add this functionality to have a consistent interface for this test on all PolyBoRi iterators.\n\nI apologize for the trouble caused,\n  Alexander",
    "created_at": "2008-05-25T21:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3283#issuecomment-22667",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

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

archive/issue_comments_022668.json:
```json
{
    "body": "Changing keywords from \"PolyBoRi, memleak\" to \"PolyBoRi, memleak, editor_malb\".",
    "created_at": "2008-06-20T04:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3283#issuecomment-22668",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "PolyBoRi, memleak" to "PolyBoRi, memleak, editor_malb".



---

archive/issue_comments_022669.json:
```json
{
    "body": "**state of affairs for editoral meeting 26/06/08**\n\nI need to fix the code, possibly by next week.",
    "created_at": "2008-06-25T11:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3283#issuecomment-22669",
    "user": "https://github.com/malb"
}
```

**state of affairs for editoral meeting 26/06/08**

I need to fix the code, possibly by next week.



---

archive/issue_comments_022670.json:
```json
{
    "body": "Next attempt attached:\n* Python references to parent object\n* some docstrings added\n* I checked for memleaks with this patch and didn't find any in my short tests\n\nBurcin, can you review my patch?",
    "created_at": "2008-06-28T15:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3283#issuecomment-22670",
    "user": "https://github.com/malb"
}
```

Next attempt attached:
* Python references to parent object
* some docstrings added
* I checked for memleaks with this patch and didn't find any in my short tests

Burcin, can you review my patch?



---

archive/issue_comments_022671.json:
```json
{
    "body": "Two small problems:\n* adding `equal` to `ctypedef struct PBPolyVectorIter` seems to be redundant.\n* `BooleanPolynomialVectorIterator` does not deallocate `self._end`\n\nOther than these a very positive review. Thanks for sorting out the iterators in the polybori wrapper malb. :)",
    "created_at": "2008-07-04T17:53:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3283#issuecomment-22671",
    "user": "https://github.com/burcin"
}
```

Two small problems:
* adding `equal` to `ctypedef struct PBPolyVectorIter` seems to be redundant.
* `BooleanPolynomialVectorIterator` does not deallocate `self._end`

Other than these a very positive review. Thanks for sorting out the iterators in the polybori wrapper malb. :)



---

archive/issue_comments_022672.json:
```json
{
    "body": "new version addresses burcin's review",
    "created_at": "2008-07-06T12:17:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3283#issuecomment-22672",
    "user": "https://github.com/malb"
}
```

new version addresses burcin's review



---

archive/issue_comments_022673.json:
```json
{
    "body": "Attachment [pbori_iterators.patch](tarball://root/attachments/some-uuid/ticket3283/pbori_iterators.patch) by @malb created at 2008-07-06 12:18:30\n\nSince the pending changes are in the updated patch, I give the patch a positive review.",
    "created_at": "2008-07-06T12:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3283#issuecomment-22673",
    "user": "https://github.com/malb"
}
```

Attachment [pbori_iterators.patch](tarball://root/attachments/some-uuid/ticket3283/pbori_iterators.patch) by @malb created at 2008-07-06 12:18:30

Since the pending changes are in the updated patch, I give the patch a positive review.



---

archive/issue_events_003502.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-07-06T19:11:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3283",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3283#event-3502"
}
```



---

archive/issue_comments_022674.json:
```json
{
    "body": "Merged pbori_iterators.patch in Sage 3.0.4.alpha2",
    "created_at": "2008-07-06T19:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3283#issuecomment-22674",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged pbori_iterators.patch in Sage 3.0.4.alpha2



---

archive/issue_comments_022675.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-06T19:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3283#issuecomment-22675",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
