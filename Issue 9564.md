# Issue 9564: libsingular exponentiation can not be interrupted

Issue created by migration from https://trac.sagemath.org/ticket/9564

Original creator: SimonKing

Original creation time: 2010-07-21 13:50:23

Assignee: malb

Keywords: KeyboardInterrupt libsingular exponentiation

When trying to get some timings for #7795, I did

```
sage: R.<x,y,z> = QQ[]
sage: p = R.random_element()
sage: p
-x^2 + 1/3*x*y + 7/2*y + 2*z
sage: timeit('q=p^(2^10)')
```

which might be stupid. 

Anyway, it was impossible to interrupt the computation with ctrl-C, which I think is a bug.


---

Comment by jdemeyer created at 2010-09-27 11:10:45

After applying #10018, the interrupt gives a segmentation fault instead of not doing anything at all.


---

Comment by jdemeyer created at 2010-09-27 11:11:15

Changing priority from major to critical.


---

Comment by jdemeyer created at 2010-09-27 11:11:15

Changing assignee from malb to tba.


---

Comment by jdemeyer created at 2010-09-27 11:11:15

Changing component from commutative algebra to c_lib.


---

Comment by jdemeyer created at 2010-09-27 13:38:57

The problem is the following:

When an interrupt is caught, the program acts as if `_sig_on` returns the value 0.  So, when using `_sig_on`, functions should be declared `except 0` and not `except -1`, which is what the Singular functions do.

The attached patch is purely proof-of-concept showing some improvement (but it doesn't fully fix the problem).


---

Comment by jdemeyer created at 2010-09-27 13:38:57

Changing keywords from "KeyboardInterrupt libsingular exponentiation" to "KeyboardInterrupt interrupt singular exception cython".


---

Comment by jdemeyer created at 2010-09-27 13:39:31

Note also that what I just said is completely undocumented :-)


---

Comment by jdemeyer created at 2011-01-14 17:39:16

Fixed by #9678.


---

Comment by jdemeyer created at 2011-01-14 17:39:16

Changing status from new to needs_review.


---

Comment by ncohen created at 2011-05-04 14:40:45

Isn't "closed" more fitting that "need_review" in that case ? `:-)`

Nathann


---

Comment by jdemeyer created at 2011-05-04 15:06:16

Resolution: duplicate
