# Issue 5800: Nice wrapper for bitset

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-04-16 05:01:03

Assignee: cwitty

CC:  robertwb mhansen rlm mvngu

bitset.pxi provides a set of inline functions for dealing with bitsets. It would be nice to wrap this in a C class with automatic memory management for ease of use as well as testing. 


---

Comment by robertwb created at 2009-04-16 05:05:03

Also, hopefully it could all be moved into a .pxd rather than a .pxi now that .pxds support inline functions.


---

Comment by jason created at 2009-04-16 07:29:17

I tried to move it all into a pxd, but the default arguments for several functions prevented that.  It's probably not a huge obstacle, though.  It was just the string printing functions, so nothing crucial.


---

Comment by robertwb created at 2009-04-16 07:35:13

See http://trac.cython.org/cython_trac/ticket/283


---

Comment by jason created at 2009-05-15 10:37:23

The patch doesn't do automatic memory management yet.


---

Comment by robertwb created at 2009-05-15 10:46:12

I'd like to see the size be arbitrary, i.e. it acts like an infinite (dense) bitset and grows as needed.


---

Comment by jason created at 2009-05-15 11:04:21

Yep, that's part of the reason it is still [needs work]


---

Comment by jason created at 2009-09-29 05:51:52

Changing assignee from cwitty to jason.


---

Comment by jason created at 2009-09-29 07:38:07

doctests need to be added to the functions.


---

Comment by jason created at 2009-10-16 11:10:28

Timings:


```
sage: a=Bitset([3*i for i in range(100)])
sage: b=Bitset([4*i for i in range(100)])
sage: d=set([4*i for i in range(100)])
sage: c=set([3*i for i in range(100)])
sage: %timeit a|b
1000000 loops, best of 3: 1.55 µs per loop
sage: %timeit c|d
100000 loops, best of 3: 17.6 µs per loop
sage: %timeit a-b
100000 loops, best of 3: 1.53 µs per loop
sage: %timeit c-d
100000 loops, best of 3: 10.4 µs per loop
```


So I guess we have a pretty good data structure.  And this is even accessing it with python!


---

Comment by jason created at 2009-10-16 11:29:51

Changing status from needs_work to needs_review.


---

Comment by jason created at 2009-10-16 11:29:51

Okay, this is a big rewrite of this patch.  Things should be good now; timings are great compared to python set/frozenset operations too.

I need this functionality in Sage for some research code I'm writing (and contributing soon), so if you have a minute to review it, that would be fantastic!


---

Comment by jason created at 2009-10-16 11:34:31

CCing some more people that would be great reviewers.


---

Attachment


---

Comment by robertwb created at 2009-10-22 03:10:09

For the most part looks good. I'd like to see some more examples of binary operations between (much) differently sized operands, and perhaps some greater than word length ones.


---

Comment by jason created at 2009-10-22 22:43:33

The second patch adds lots of doctests with different set sizes (and double-checking with the python builtin set type).  It also adds an iter function that allows one to do list(b) for a bitset b.


---

Comment by jason created at 2009-10-23 00:46:28

apply on top of previous patch


---

Attachment

Apologies: that last patch had a bit of another unrelated patch in it.  I've just uploaded the corrected patch.


---

Comment by robertwb created at 2009-10-27 18:26:03

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2009-10-27 18:26:03

Looks good, thanks for finally wrapping this up.


---

Comment by mhansen created at 2009-10-31 05:33:55

Resolution: fixed
