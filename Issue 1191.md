# Issue 1191: wrap pari's matsolvemodn for A.solve_right over Z/nZ

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-11-17 15:24:47

Assignee: was

This


```
matsolvemod(M,D,B,{flag=0}): one solution of system of congruences 
MX=B mod D (M matrix, B and D column vectors). If (optional) flag is
non-null return all solutions.
```


should allow to implement A.solve_right for matrices over Z/nZ.


---

Comment by robharron created at 2013-03-30 18:54:17

It seems like one would first have to add matsolvemod as a method in the gen class. (Or use the interface...).


---

Comment by robharron created at 2013-03-31 01:35:17

I've added http://trac.sagemath.org/sage_trac/ticket/14391 so that one can access matsolvemod through the C-library interface. However, I now remember William telling me you can solve equations in *Z*/n*Z* using the code he wrote for finitely generated modular over a PID. And you can. It would be nice to use that implementation for A.solve_right.

Replying to [comment:1 robharron]:
> It seems like one would first have to add matsolvemod as a method in the gen class. (Or use the interface...).


---

Comment by robharron created at 2013-04-02 04:05:50

Okay, I've written a patch for this! Using pari is significantly faster than using the f.g. modules over a PID code, so the patch depends on #14391. This patch applies onto sage 5.8 and all doctests passed (using --testall --long).


---

Attachment


---

Comment by robharron created at 2013-04-02 04:28:22

Changing status from new to needs_review.


---

Comment by robharron created at 2013-04-02 04:28:22

Changing keywords from "" to "solve_right, matsolvemod, Zmod".


---

Comment by malb created at 2013-04-02 11:32:02

Can you post some timings comparing the two approaches (I am curious about larger dimensions & bitsizes)? The patch itself looks fine to me.


---

Comment by robharron created at 2013-04-02 18:20:11

Here are some times (I temporarily added a method .solve_left_slow that uses the f.g. over a pid code; the latter naturally does things on the left):



```
sage: N = 124; r = 21; c = 17; M = MatrixSpace(Zmod(N), r, c); A = M.random_element(); AL = A.lift(); X = Zmod(N) ** c; x = X.random_element(); xL = x.lift(); bL = AL * xL; bL = bL % N; AT = A.transpose(); b = (Zmod(N) ** r)(bL)
sage: timeit('A.solve_right(b)')
125 loops, best of 3: 3.72 ms per loop
sage: timeit('AT.solve_left_slow(b)')
5 loops, best of 3: 707 ms per loop

sage: N = 12; r = 50; c = 38; M = MatrixSpace(Zmod(N), r, c); A = M.random_element(); AL = A.lift(); X = Zmod(N) ** c; x = X.random_element(); xL = x.lift(); bL = AL * xL; bL = bL % N; AT = A.transpose(); b = (Zmod(N) ** r)(bL)
sage: timeit('A.solve_right(b)')
5 loops, best of 3: 44.3 ms per loop
sage: timeit('AT.solve_left_slow(b)')
5 loops, best of 3: 6.41 s per loop

sage: N = 4829; r = 9; c = 5; M = MatrixSpace(Zmod(N), r, c); A = M.random_element(); AL = A.lift(); X = Zmod(N) ** c; x = X.random_element(); xL = x.lift(); bL = AL * xL; bL = bL % N; AT = A.transpose(); b = (Zmod(N) ** r)(bL)
sage: timeit('A.solve_right(b)')
625 loops, best of 3: 343 µs per loop
sage: timeit('AT.solve_left_slow(b)')
5 loops, best of 3: 133 ms per loop

sage: N = 2634095876; r = 21; c = 17; M = MatrixSpace(Zmod(N), r, c); A = M.random_element(); AL = A.lift(); X = Zmod(N) ** c; x = X.random_element(); xL = x.lift(); bL = AL * xL; bL = bL % N; AT = A.transpose(); b = (Zmod(N) ** r)(bL)
sage: timeit('A.solve_right(b)')25 loops, best of 3: 13 ms per loop
sage: timeit('AT.solve_left_slow(b)')5 loops, best of 3: 799 ms per loop

sage: sage: N = 23457602398746509872634095876; r = 21; c = 17; M = MatrixSpace(Zmod(N), r, c); A = M.random_element(); AL = A.lift(); X = Zmod(N) ** c; x = X.random_element(); xL = x.lift(); bL = AL * xL; bL = bL % N; AT = A.transpose(); b = (Zmod(N) ** r)(bL)
sage: timeit('A.solve_right(b)')
5 loops, best of 3: 66.5 ms per loop
sage: timeit('AT.solve_left_slow(b)')
5 loops, best of 3: 1.18 s per loop

sage: N = 29834756092364523457602398746509872634095876; r = 21; c = 17; M = MatrixSpace(Zmod(N), r, c); A = M.random_element(); AL = A.lift(); X = Zmod(N) ** c; x = X.random_element(); xL = x.lift(); bL = AL * xL; bL = bL % N; AT = A.transpose(); b = (Zmod(N) ** r)(bL)
sage: timeit('A.solve_right(b)')
5 loops, best of 3: 231 ms per loop
sage: timeit('AT.solve_left_slow(b)')
5 loops, best of 3: 1.54 s per loop
```



I also attached a code snippet of .solve_left_slow to this ticket for transparency and posterity!

Replying to [comment:5 malb]:
> Can you post some timings comparing the two approaches (I am curious about larger dimensions & bitsizes)? The patch itself looks fine to me.


---

Comment by robharron created at 2013-04-02 18:21:18

Snippet of the f.g. modules over a PID implementation. This is much slower and only included for you curious people out there.


---

Attachment

Okay, that convinces me.


---

Comment by malb created at 2013-04-02 18:33:50

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-04-04 17:38:58

Resolution: fixed
