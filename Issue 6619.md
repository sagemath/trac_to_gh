# Issue 6619: [with patch, needs review] Fix ``inner`` option for integer vectors

Issue created by migration from https://trac.sagemath.org/ticket/6619

Original creator: nthiery

Original creation time: 2009-07-25 15:01:53

Assignee: tbd

CC:  sage-combinat burcin

Keywords: inner, integer vectors


```
            sage: IV = IntegerVectors(3,10,inner=[4,1,3], min_part = 2)
            sage: min_length, max_length, floor, ceiling, min_slope, max_slope = IV._parameters()
            sage: floor(1), floor(2), floor(3)
            (4, 2, 3)

            sage: IV = IntegerVectors(3, 10, outer=[4,1,3], max_part = 3)
            sage: min_length, max_length, floor, ceiling, min_slope, max_slope = IV._parameters()
            sage: ceiling(1), ceiling(2), ceiling(3)
            (3, 1, 3)
```



---

Attachment


---

Comment by nthiery created at 2009-07-25 15:09:24

Changing status from new to assigned.


---

Comment by nthiery created at 2009-07-25 15:09:24

Changing assignee from tbd to nthiery.


---

Comment by ddrake created at 2009-07-25 16:59:08

Changing component from algebra to combinatorics.


---

Comment by ddrake created at 2009-07-25 16:59:08

Positive review.


---

Comment by mvngu created at 2009-07-25 21:16:01

Resolution: fixed
