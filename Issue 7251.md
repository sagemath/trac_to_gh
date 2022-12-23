# Issue 7251: Allow for Integer(3, parent = MyParent)

Issue created by migration from https://trac.sagemath.org/ticket/7251

Original creator: nthiery

Original creation time: 2009-10-19 21:59:48

Assignee: somebody

CC:  sage-combinat mhansen robertwb

Keywords: Integer, IntegerWrapper

The attached patch allows for the creation of integers whose parents are not IntegerRing():


```
            sage: n = Integer(3, parent = Primes())
            sage: n
            3
            sage: n.parent()
            Set of all prime numbers: 2, 3, 5, 7, ...
```


That's used in a couple places in the category code #5891, when illustrating how to create new parents like the set of prime integers. So this is quite urgent.

Any better implementation welcome! I am fine also with having this work only for IntegerWrapper.


---

Comment by nthiery created at 2009-10-19 22:02:24

Changing assignee from somebody to nthiery.


---

Comment by robertwb created at 2009-10-20 06:27:06

This will break the integer pool, as recycled integer might not have ZZ as their parent.


---

Comment by hivert created at 2009-10-20 07:56:25

Replying to [comment:2 robertwb]:
> This will break the integer pool, as recycled integer might not have ZZ as their parent. 


Can you elaborate a little bit more. Is this a serious problem ? We definitely want to create parents whose element will be some kind of integers. Does sage definitely prevents to inherits from integer and change the parent ? Do we have to wrap the integer as an *attribute* ?

Cheers,

Florent


---

Comment by mhansen created at 2009-10-20 08:08:03

I may be mistaken, but I don't think the IntegerWrapper objects use the integer pool.  Robert?  If that's the case, then that would be a solution.he most innovative decor on the island. Located in the heart of Phuket Town. An absoute 'must' if you're in town.

mid-range reservations recommended parking nearby smoking dj music credit cards accepted


---

Comment by hivert created at 2009-10-20 08:19:56

Replying to [comment:4 mhansen]:
> I may be mistaken, but I don't think the IntegerWrapper objects use the integer pool.  Robert?  If that's the case, then that would be a solution.he most innovative decor on the island. Located in the heart of Phuket Town. An absoute 'must' if you're in town.
> 
> mid-range reservations recommended parking nearby smoking dj music credit cards accepted

Is trac adding some kind of subliminal add ? :-)

Florent


---

Comment by mhansen created at 2009-10-20 13:50:33

Haha -- I think it automagically copied / pasted for me.


---

Comment by nthiery created at 2009-10-20 16:32:11

Replying to [comment:4 mhansen]:
> I may be mistaken, but I don't think the IntegerWrapper objects use the integer pool.  Robert?

I double checked our use cases, and altogether we indeed only need the feature

```
     sage: IntegerWrapper(3, parent = Primes())
```

with the rest as in the description.

However, I have a problem, since if I move the __init__ to IntegerWrapper, then __cinit__ of Integer still gets called, and complains about the parent argument. Robert, Mike: would you mind investigating what's the right way for implementing this (I am not so familiar with cython initialization)?


---

Comment by robertwb created at 2009-10-20 17:44:43

Yes, you should just use the wrapper (at least for now). 

I should explain this a bit more--typically there shouldn't be any issues doing this with Cython classes. With Integers what we do is hijack the allocation/deallocation function slots with our own custom functions that stick already allocated Integers (with initialized parent and mpz_t fields) into a pool on "deallocation" and then pull them out whenever a new one is needed. Because Integers are so common, this is actually a significant savings, but does cause issues with subclassing from Python. 

IntegerWrapper is OK because it statically sets its alloc/dealloc methods to the *original* Integer alloc/dealloc methods (before we manually swap them out for ours). 

It's all a bit messy, and I've been wanting to redo it for a while (extending it to a cleaner and more generic framework that can be used elsewhere) but I have much higher priority stuff (like a thesis) to be doing.


---

Attachment

Replying to [comment:8 robertwb]:
> I should explain this a bit more--typically there shouldn't be any issues doing this with Cython classes. With Integers what we do is hijack the allocation/deallocation function slots with our own custom functions that stick already allocated Integers (with initialized parent and mpz_t fields) into a pool on "deallocation" and then pull them out whenever a new one is needed. Because Integers are so common, this is actually a significant savings, but does cause issues with subclassing from Python. 
> 
> IntegerWrapper is OK because it statically sets its alloc/dealloc methods to the *original* Integer alloc/dealloc methods (before we manually swap them out for ours). 

Thanks for the explanations! I have added them to the documentation of IntegerWrapper.

The latest patch also just modifies IntegerWrapper, without touching Integer.


---

Comment by nthiery created at 2009-10-20 21:20:13

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-10-21 04:35:44

Looks good to me and passes tests.


---

Comment by mhansen created at 2009-10-21 04:35:44

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-21 07:12:04

Resolution: fixed
