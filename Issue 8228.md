# Issue 8228: Segfault in libsingular

Issue created by migration from https://trac.sagemath.org/ticket/8228

Original creator: malb

Original creation time: 2010-02-10 13:24:13

Assignee: malb

CC:  jsp

This is bad:


```python
sage: P.<x,y> = Zmod(10)[]; P(0)
0
sage: P.<x,y> = Zmod(2^10)[]; P(0)

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```



---

Comment by malb created at 2010-02-10 13:25:01

This is an upstream bug, cf.

  http://groups.google.com/group/libsingular-devel/browse_thread/thread/aa42455cb52257d

I will provide an updated SPKG later.


---

Comment by malb created at 2010-02-10 13:32:15

http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-9-20100125.p1.spkg


---

Comment by malb created at 2010-02-10 13:33:28

You will need the patch from #8059 to compile the Sage library with the Singular SPKG.


---

Comment by malb created at 2010-02-10 13:35:00

Changing status from new to needs_review.


---

Comment by malb created at 2010-03-03 12:52:00

Bumping this ticket because it is ridiculous that this bug is around.


---

Comment by malb created at 2010-03-03 12:52:00

Changing priority from major to critical.


---

Comment by malb created at 2010-03-11 10:29:44

Ticket depends on #8059


---

Comment by malb created at 2010-06-02 18:45:01

Setting to needs work since it depends on #8059 (though not strictly)


---

Comment by malb created at 2010-06-02 18:45:01

Changing status from needs_review to needs_work.


---

Attachment

add doctest


---

Comment by burcin created at 2010-09-19 14:51:20

Since #8059 is merged with the new Singular package, this works:


```
sage: P.<x,y> = Zmod(10)[]; P(0)
0
sage: P.<x,y> = Zmod(2^10)[]; P(0)
0
```


attachment:trac_8228-doctest.patch adds a doctest. Trivial review anyone?


---

Comment by burcin created at 2010-09-19 14:51:20

Changing keywords from "" to "singular".


---

Comment by burcin created at 2010-09-19 14:51:20

Changing status from needs_work to needs_review.


---

Comment by malb created at 2010-09-19 16:02:15

Changing status from needs_review to positive_review.


---

Comment by malb created at 2010-09-19 16:02:15

Patch looks good, doctests pass.


---

Comment by mpatel created at 2010-09-29 04:24:57

Resolution: fixed
