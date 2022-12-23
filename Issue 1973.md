# Issue 1973: native partition_associated function

Issue created by migration from https://trac.sagemath.org/ticket/1973

Original creator: jason

Original creation time: 2008-01-29 16:13:05

Assignee: mhansen

CC:  sage-combinat

This patch replaces the wrapper around Gap to give the conjugate partition.  It speeds up the computation quite a bit.



---

Attachment


---

Comment by mhansen created at 2008-01-29 17:34:45

I'd say it's an improvement, but it may be better to avoid code duplication with the following:


```
sage: Partition([3,1]).conjugate()
[2, 1, 1]
```



---

Comment by jason created at 2008-01-29 18:38:41

With the patch:


```
sage: %timeit partition_associated([6,5,5,4,2,2,1])
100000 loops, best of 3: 9.21 µs per loop
sage: %timeit Partition([6,5,5,4,2,2,1]).conjugate()
10000 loops, best of 3: 154 µs per loop
sage: a=Partition([6,5,5,4,2,2,1])
sage: %timeit a.conjugate()
1000 loops, best of 3: 268 µs per loop
```


So I'll probably delete the partition_associated function and replace the Partition.conjugate() function, if that's all right, and post up another patch.


---

Comment by mhansen created at 2008-01-29 19:08:43

Well, the resason partition_associated is still there is for backward compatibility reasons.  I would make it so that partition_associated returns list(Partition(p).conjugate()). 


You can modify Partition_class.conjugate, but make sure you return Partition_class objects.  Within the function, you can eliminate some overhead by replacing "return Partition..." with "return Partition_class..." since Partition is a wrapper function which does type-checking, etc.


---

Comment by jason created at 2008-01-29 21:49:23

Some timings after I put my code into partition.py:


```
[15:42] <jason-> sage: a=Partition(sum([[i]*20 for i in range(50,1,-1)],[]))
[15:42] <jason-> sage: print len(a), len(a.conjugate('mike'))
[15:42] <jason-> 980 50
[15:42] <jason-> sage: %timeit a.conjugate('jason')
[15:42] <jason-> 100 loops, best of 3: 3.34 ms per loop
[15:42] <jason-> sage: %timeit a.conjugate('mike')
[15:42] <jason-> 100 loops, best of 3: 3.25 ms per loop
[15:42] <jason-> sage: %timeit a.conjugate('mikeandjason')
[15:42] <jason-> 100 loops, best of 3: 3.05 ms per loop
[15:42] <jason-> sage: a=Partition(sum([[i]*2 for i in range(5000,1,-1)],[]))
[15:42] <jason-> sage: print len(a), len(a.conjugate('mike'))
[15:42] <jason-> 9998 5000
[15:42] <jason-> sage: %timeit a.conjugate('jason')
[15:42] <jason-> 10 loops, best of 3: 246 ms per loop
[15:42] <jason-> sage: %timeit a.conjugate('mike')
[15:42] <jason-> 10 loops, best of 3: 34.8 ms per loop
[15:42] <jason-> sage: %timeit a.conjugate('mikeandjason')
[15:42] <jason-> 10 loops, best of 3: 32.4 ms per loop
[15:42] <jason-> we both win this time.
[15:42] <jason-> 'mikeandjason' is making a few slight modifications to your algorithm (like using .extend instead of +=, etc.)
```


So I'll post a minor patch to Mike's code.


---

Attachment

apply instead of first patch.


---

Comment by jason created at 2008-01-29 22:06:37

apply instead of first two patches.


---

Attachment

Yet again, apply this instead of the previous patches.


---

Attachment

Looks good to me.


---

Comment by mabshoff created at 2008-01-30 02:51:33

Merged conjugate-partition.4.patch in Sage 2.10.1.rc3


---

Comment by mabshoff created at 2008-01-30 02:51:33

Resolution: fixed


---

Comment by mabshoff created at 2008-01-30 04:07:09

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-01-30 04:07:09

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-01-30 04:07:09

The following is probably trivial to fix:

```

Exception exceptions.ImportError: 'cannot import name is_FractionFieldElement' in 'sage.rings.polynomial.polynomial_element.Polynomial_generic_dense.__normalize' ignored
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)
```

but it happens after a `sage -ba`

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-30 08:20:52

Reverted for good. Somebody needs to revisit this with 2.10.1.rc3 or later.

Cheers,

Michael


---

Comment by jason created at 2008-01-30 16:28:58

The error apparently has to do with the top-level import in combinat.py:

    from sage.combinat.partition import Partition

When I move the top-level import into the associated_partition function, the failing doctest passes.

Mike, do you know what is going on?


---

Attachment

I posted a new patch which should take care of this issue (although I never experienced the -ba issue on my machine).


---

Attachment


---

Comment by mabshoff created at 2008-02-01 04:24:50

Merged 1973.patch in Sage 2.10.1.rc4


---

Comment by mabshoff created at 2008-02-01 04:24:50

Resolution: fixed


---

Comment by mabshoff created at 2008-02-01 04:25:18

Patch looks good to me.

Cheers,

Michael
