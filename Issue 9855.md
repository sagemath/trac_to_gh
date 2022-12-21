# Issue 9855: improve `augment` method for sparse matrices

Issue created by migration from Trac.

Original creator: ylchapuy

Original creation time: 2010-09-04 20:27:21

Assignee: jason, was

CC:  zimmerma

see #7199 for a patch improving `stack`.


---

Attachment

Patch based on sage 4.5.3 + #7199 (but I don't know if it depends on it).
Paul, as you did such a good job reviewing the other ticket, I cc'd you.


---

Comment by ylchapuy created at 2010-09-22 08:44:57

Changing status from new to needs_review.


---

Comment by zimmerma created at 2010-09-22 09:52:42

> Paul, as you did such a good job reviewing the other ticket, I cc'd you.

Yann, please could you provide a description saying in what sense you did "improve"
augment, maybe with an example? Is that an improvement in functionality or speed?

Paul


---

Comment by zimmerma created at 2010-09-22 09:52:42

Changing status from needs_review to needs_info.


---

Comment by ylchapuy created at 2010-09-22 11:43:00

It's a speed improvement. Here's the example:


```
sage: m = identity_matrix(QQ, 1000, sparse=True)
sage: timeit('m.augment(m)')
```


BEFORE

```
5 loops, best of 3: 368 ms per loop
```

AFTER

```
625 loops, best of 3: 1.2 ms per loop
```


And we are not loosing anything for small cases:

```
sage: m = identity_matrix(QQ, 5, sparse=True)  
sage: timeit('m.augment(m)')
```


BEFORE

```
625 loops, best of 3: 198 µs per loop
```

AFTER

```
625 loops, best of 3: 197 µs per loop
```



---

Comment by ylchapuy created at 2010-09-22 11:43:00

Changing status from needs_info to needs_review.


---

Comment by zimmerma created at 2010-09-22 19:49:42

Changing status from needs_review to needs_work.


---

Comment by zimmerma created at 2010-09-22 19:49:42

A small typo in the code: "number of columns must be the same" should be
"number of rows must be the same". I confirm the great speed improvement.
Once the typo is fixed, I will check the doctests still pass.

Paul


---

Comment by ylchapuy created at 2010-09-23 00:28:47

Changing status from needs_work to needs_review.


---

Attachment

Nice spot, typo fixed. Apply both patches.

    Yann


---

Comment by zimmerma created at 2010-09-24 20:04:45

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2010-09-24 20:04:45

good work once again, Yann!

Paul


---

Comment by mpatel created at 2010-09-28 10:58:16

Resolution: fixed
