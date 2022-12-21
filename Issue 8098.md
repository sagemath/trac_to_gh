# Issue 8098: solve_mod is horribly broken

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-01-27 23:13:42

Assignee: AlexGhitza

CC:  polybori malb robertwb

I was just grading papers in my class and one student (Andrew Ohana) pointed out in his solution that Sage's solve_mod is massively broken.  For example:

```
sage: var('x')
sage: solve_mod([x^2==1], 9)
[]         # WTF?
```

and:

```
sage: solve_mod([x^2==1], 8)
[(1,), (3,), (4,), (5,), (7,)]
```


Etc. 


---

Comment by rkirov created at 2010-02-01 06:16:19

I tried to chase down the bug but it seems the rabbit hole goes deeper (all the way to multivariate singular polynomial evaluation). 


```
sage: P.<x,y> = Zmod(3^2)[]
sage: f=P(x*x)
sage: f(3,0)
1

sage: P.<x,y> = Zmod(10)[]
sage: f=P(x*y)
sage: f(2,5)
1
```


I think the problem is in the __call__ method in http://sagenb.org/src/libs/singular/polynomial.pyx/ but its all Cython land there, so I can't do much. In any case seems that Singular is fine, and something gets lost in the translation.


```
> ring R= (integer,9),(x,y),dp;
> poly f=x2;
> subst(f,x,3,y,0);
0
```



---

Comment by burcin created at 2010-02-01 18:40:17

We need a Singular expert to comment on this.

Note that the function we call is `fast_map()` and it returns `1` as the generator of the ideal in this case.


---

Comment by PolyBoRi created at 2010-02-02 08:16:48

The Singular map works fine in my somewhat ancient Singular version here...

```
> poly f=x2;
> subst(f,x,3,y,0);
0
> map m=R,3,0;
> m(f);
0

```


Does this fail with newer versions?


---

Comment by rkirov created at 2010-02-02 08:24:27

I have version 3-1-0 and Singular returns the same output as you (which is correct). I think the problem is in Sage.


---

Comment by malb created at 2010-02-04 11:29:05

There's a discussion on this matter on [libsingular-devel], cf. http://groups.google.com/group/libsingular-devel/browse_thread/thread/bd0aa6c4d7b6ecc3

This still doesn't explain why subst works but I guess it uses a different code path.


---

Comment by PolyBoRi created at 2010-02-04 12:28:47

completely independent implementation.

Cheers,
Michael


---

Comment by malb created at 2010-02-09 18:50:54

Changing status from new to needs_review.


---

Attachment

Sorry for the delay.


---

Comment by malb created at 2010-02-09 20:46:19

The attached patch will cause a SEGFAULT which is due to a bug in Singular (I believe). The bug is not caused by my patch but just uncovered (well, if my analysis on [libsingular-devel] is correct)


---

Comment by malb created at 2010-02-10 13:25:19

Ticket depends on #8228


---

Comment by malb created at 2010-03-03 12:54:31

Anyone?


---

Comment by zimmerma created at 2010-03-14 15:27:33

I tried the doctests, but unfortunately one more test is Segfaulting wrt #7773:

```
[zimmerma`@`coing sage]$ sage -t -verbose rings/polynomial/multi_polynomial_libsingular.pyx
...
Trying:
    f(Integer(0),Integer(0),Integer(0))###line 1725:_sage_    >>> f(0,0,0)
Expecting:
    0


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```

Since this is precisely linked to the modified file, I give a negative review.


---

Comment by zimmerma created at 2010-03-14 15:27:33

Changing status from needs_review to needs_work.


---

Comment by malb created at 2010-03-14 15:36:57

Paul, which combination of SPKGs and patches did you apply?


---

Comment by zimmerma created at 2010-03-15 10:15:08

Michael,

> Paul, which combination of SPKGs and patches did you apply? 

just a clone of 4.3.3 + your patch. I just reproduced it on a different computer.

Paul


---

Comment by malb created at 2010-03-15 11:27:37

Paul, this ticket depends on an update of Singular (cf. #8228 and #8059)

Cheers,
Martin


---

Comment by malb created at 2011-01-14 15:49:05

With 4.6.1.rc1 I get:

```python
sage: var('x')
x
sage: solve_mod([x^2==1], 9)
[(1,), (8,)]
sage: solve_mod([x^2==1], 8)
[(1,), (3,), (5,), (7,)]
```


Thus, I believe this bug is fixed.


---

Comment by malb created at 2011-01-14 15:49:05

Resolution: fixed
