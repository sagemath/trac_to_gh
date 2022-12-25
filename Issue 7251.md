# Issue 7251: Allow for Integer(3, parent = MyParent)

archive/issues_007251.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  sage-combinat @mwhansen @robertwb\n\nKeywords: Integer, IntegerWrapper\n\nThe attached patch allows for the creation of integers whose parents are not IntegerRing():\n\n```\n            sage: n = Integer(3, parent = Primes())\n            sage: n\n            3\n            sage: n.parent()\n            Set of all prime numbers: 2, 3, 5, 7, ...\n```\n\nThat's used in a couple places in the category code #5891, when illustrating how to create new parents like the set of prime integers. So this is quite urgent.\n\nAny better implementation welcome! I am fine also with having this work only for IntegerWrapper.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7251\n\n",
    "created_at": "2009-10-19T21:59:48Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "Allow for Integer(3, parent = MyParent)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7251",
    "user": "https://github.com/nthiery"
}
```
Assignee: somebody

CC:  sage-combinat @mwhansen @robertwb

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

Issue created by migration from https://trac.sagemath.org/ticket/7251





---

archive/issue_comments_060119.json:
```json
{
    "body": "Changing assignee from somebody to @nthiery.",
    "created_at": "2009-10-19T22:02:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7251#issuecomment-60119",
    "user": "https://github.com/nthiery"
}
```

Changing assignee from somebody to @nthiery.



---

archive/issue_comments_060120.json:
```json
{
    "body": "This will break the integer pool, as recycled integer might not have ZZ as their parent.",
    "created_at": "2009-10-20T06:27:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7251#issuecomment-60120",
    "user": "https://github.com/robertwb"
}
```

This will break the integer pool, as recycled integer might not have ZZ as their parent.



---

archive/issue_comments_060121.json:
```json
{
    "body": "Replying to [comment:2 robertwb]:\n> This will break the integer pool, as recycled integer might not have ZZ as their parent. \n\n\n\nCan you elaborate a little bit more. Is this a serious problem ? We definitely want to create parents whose element will be some kind of integers. Does sage definitely prevents to inherits from integer and change the parent ? Do we have to wrap the integer as an *attribute* ?\n\nCheers,\n\nFlorent",
    "created_at": "2009-10-20T07:56:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7251#issuecomment-60121",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:2 robertwb]:
> This will break the integer pool, as recycled integer might not have ZZ as their parent. 



Can you elaborate a little bit more. Is this a serious problem ? We definitely want to create parents whose element will be some kind of integers. Does sage definitely prevents to inherits from integer and change the parent ? Do we have to wrap the integer as an *attribute* ?

Cheers,

Florent



---

archive/issue_comments_060122.json:
```json
{
    "body": "I may be mistaken, but I don't think the IntegerWrapper objects use the integer pool.  Robert?  If that's the case, then that would be a solution.he most innovative decor on the island. Located in the heart of Phuket Town. An absoute 'must' if you're in town.\n\nmid-range reservations recommended parking nearby smoking dj music credit cards accepted",
    "created_at": "2009-10-20T08:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7251#issuecomment-60122",
    "user": "https://github.com/mwhansen"
}
```

I may be mistaken, but I don't think the IntegerWrapper objects use the integer pool.  Robert?  If that's the case, then that would be a solution.he most innovative decor on the island. Located in the heart of Phuket Town. An absoute 'must' if you're in town.

mid-range reservations recommended parking nearby smoking dj music credit cards accepted



---

archive/issue_comments_060123.json:
```json
{
    "body": "Replying to [comment:4 mhansen]:\n> I may be mistaken, but I don't think the IntegerWrapper objects use the integer pool.  Robert?  If that's the case, then that would be a solution.he most innovative decor on the island. Located in the heart of Phuket Town. An absoute 'must' if you're in town.\n> \n> mid-range reservations recommended parking nearby smoking dj music credit cards accepted\n\n\nIs trac adding some kind of subliminal add ? :-)\n\nFlorent",
    "created_at": "2009-10-20T08:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7251#issuecomment-60123",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:4 mhansen]:
> I may be mistaken, but I don't think the IntegerWrapper objects use the integer pool.  Robert?  If that's the case, then that would be a solution.he most innovative decor on the island. Located in the heart of Phuket Town. An absoute 'must' if you're in town.
> 
> mid-range reservations recommended parking nearby smoking dj music credit cards accepted


Is trac adding some kind of subliminal add ? :-)

Florent



---

archive/issue_comments_060124.json:
```json
{
    "body": "Haha -- I think it automagically copied / pasted for me.",
    "created_at": "2009-10-20T13:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7251#issuecomment-60124",
    "user": "https://github.com/mwhansen"
}
```

Haha -- I think it automagically copied / pasted for me.



---

archive/issue_comments_060125.json:
```json
{
    "body": "Replying to [comment:4 mhansen]:\n> I may be mistaken, but I don't think the IntegerWrapper objects use the integer pool.  Robert?\n\n\nI double checked our use cases, and altogether we indeed only need the feature\n\n```\n     sage: IntegerWrapper(3, parent = Primes())\n```\nwith the rest as in the description.\n\nHowever, I have a problem, since if I move the __init__ to IntegerWrapper, then __cinit__ of Integer still gets called, and complains about the parent argument. Robert, Mike: would you mind investigating what's the right way for implementing this (I am not so familiar with cython initialization)?",
    "created_at": "2009-10-20T16:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7251#issuecomment-60125",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:4 mhansen]:
> I may be mistaken, but I don't think the IntegerWrapper objects use the integer pool.  Robert?


I double checked our use cases, and altogether we indeed only need the feature

```
     sage: IntegerWrapper(3, parent = Primes())
```
with the rest as in the description.

However, I have a problem, since if I move the __init__ to IntegerWrapper, then __cinit__ of Integer still gets called, and complains about the parent argument. Robert, Mike: would you mind investigating what's the right way for implementing this (I am not so familiar with cython initialization)?



---

archive/issue_comments_060126.json:
```json
{
    "body": "Yes, you should just use the wrapper (at least for now). \n\nI should explain this a bit more--typically there shouldn't be any issues doing this with Cython classes. With Integers what we do is hijack the allocation/deallocation function slots with our own custom functions that stick already allocated Integers (with initialized parent and mpz_t fields) into a pool on \"deallocation\" and then pull them out whenever a new one is needed. Because Integers are so common, this is actually a significant savings, but does cause issues with subclassing from Python. \n\nIntegerWrapper is OK because it statically sets its alloc/dealloc methods to the *original* Integer alloc/dealloc methods (before we manually swap them out for ours). \n\nIt's all a bit messy, and I've been wanting to redo it for a while (extending it to a cleaner and more generic framework that can be used elsewhere) but I have much higher priority stuff (like a thesis) to be doing.",
    "created_at": "2009-10-20T17:44:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7251#issuecomment-60126",
    "user": "https://github.com/robertwb"
}
```

Yes, you should just use the wrapper (at least for now). 

I should explain this a bit more--typically there shouldn't be any issues doing this with Cython classes. With Integers what we do is hijack the allocation/deallocation function slots with our own custom functions that stick already allocated Integers (with initialized parent and mpz_t fields) into a pool on "deallocation" and then pull them out whenever a new one is needed. Because Integers are so common, this is actually a significant savings, but does cause issues with subclassing from Python. 

IntegerWrapper is OK because it statically sets its alloc/dealloc methods to the *original* Integer alloc/dealloc methods (before we manually swap them out for ours). 

It's all a bit messy, and I've been wanting to redo it for a while (extending it to a cleaner and more generic framework that can be used elsewhere) but I have much higher priority stuff (like a thesis) to be doing.



---

archive/issue_comments_060127.json:
```json
{
    "body": "Attachment [trac_7251-integer_parent-nt.patch](tarball://root/attachments/some-uuid/ticket7251/trac_7251-integer_parent-nt.patch) by @nthiery created at 2009-10-20 21:20:13\n\nReplying to [comment:8 robertwb]:\n> I should explain this a bit more--typically there shouldn't be any issues doing this with Cython classes. With Integers what we do is hijack the allocation/deallocation function slots with our own custom functions that stick already allocated Integers (with initialized parent and mpz_t fields) into a pool on \"deallocation\" and then pull them out whenever a new one is needed. Because Integers are so common, this is actually a significant savings, but does cause issues with subclassing from Python. \n> \n> IntegerWrapper is OK because it statically sets its alloc/dealloc methods to the *original* Integer alloc/dealloc methods (before we manually swap them out for ours). \n\n\nThanks for the explanations! I have added them to the documentation of IntegerWrapper.\n\nThe latest patch also just modifies IntegerWrapper, without touching Integer.",
    "created_at": "2009-10-20T21:20:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7251#issuecomment-60127",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_7251-integer_parent-nt.patch](tarball://root/attachments/some-uuid/ticket7251/trac_7251-integer_parent-nt.patch) by @nthiery created at 2009-10-20 21:20:13

Replying to [comment:8 robertwb]:
> I should explain this a bit more--typically there shouldn't be any issues doing this with Cython classes. With Integers what we do is hijack the allocation/deallocation function slots with our own custom functions that stick already allocated Integers (with initialized parent and mpz_t fields) into a pool on "deallocation" and then pull them out whenever a new one is needed. Because Integers are so common, this is actually a significant savings, but does cause issues with subclassing from Python. 
> 
> IntegerWrapper is OK because it statically sets its alloc/dealloc methods to the *original* Integer alloc/dealloc methods (before we manually swap them out for ours). 


Thanks for the explanations! I have added them to the documentation of IntegerWrapper.

The latest patch also just modifies IntegerWrapper, without touching Integer.



---

archive/issue_comments_060128.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-20T21:20:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7251#issuecomment-60128",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060129.json:
```json
{
    "body": "Looks good to me and passes tests.",
    "created_at": "2009-10-21T04:35:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7251#issuecomment-60129",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me and passes tests.



---

archive/issue_comments_060130.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-21T04:35:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7251#issuecomment-60130",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_017164.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-21T07:12:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7251",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7251#event-17164"
}
```



---

archive/issue_comments_060131.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-21T07:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7251#issuecomment-60131",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
