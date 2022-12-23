# Issue 3634: minpoly still slow for elements of finte fields

Issue created by migration from https://trac.sagemath.org/ticket/3634

Original creator: robertwb

Original creation time: 2008-07-10 17:11:44

Assignee: tbd

The improvement at #3620 is significant, but NTL does have minimal polynomial computations, though provided in http://www.shoup.net/ntl/doc/GF2X.txt rather than http://www.shoup.net/ntl/doc/GF2E.txt . We should probably use the proof flag to decide the algorithm. Trace could be wrapped as well.

Also, the computation of matrix() is using the completely generic code, which has got to be sub-optimal for manipulating elements of GF(2).



---

Attachment


```
sage: sage: k.<a> = GF(2^500)

sage: sage: time g = k.random_element()
CPU times: user 0.07 s, sys: 0.00 s, total: 0.07 s
Wall time: 0.07 s

sage: time f = g.minpoly()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.00 s

sage: f(g)
 0
sage: timeit("g.minpoly()")
125 loops, best of 3: 4.03 ms per loop
```



---

Attachment

add fast charpoly


---

Comment by was created at 2008-07-10 23:22:06

Great work Robert!

I added a patch that adds a fast charpoly method by the way.

Apply both of them.


---

Comment by robertwb created at 2008-07-11 17:43:08

Charpoly method is good too. Apply both patches.


---

Comment by mabshoff created at 2008-07-11 17:46:26

This is one of the few patches that will be merged in 3.0.5 :)

Cheers,

Michael


---

Comment by was created at 2008-07-11 18:09:48

Resolution: fixed
