# Issue 6596: [with patch, needs review] Singular refactoring and Groebner Strategy objects

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-07-23 07:57:04

Assignee: malb

CC:  polybori burcin

Keywords: singular

The attached patch factors out some commonly called code for dealing with libsingular to make it more accessible.

Also, the attached patch wraps Singular's Gröbner strategy objects which allow much faster normal form computations.



---

Comment by malb created at 2009-07-23 08:36:33

CCing Burcin, because this patch contains the first step of refactoring he wants.


---

Comment by malb created at 2009-07-23 08:39:36

Groebner Strategy in action


```
sage: P = PolynomialRing(QQ,6,'x')
sage: I = sage.rings.ideal.Cyclic(P)
sage: J = Ideal(I.groebner_basis())
sage: J.ngens()
45
```



```
sage: f = P.random_element()
```


The usual call to `kNF`:


```
sage: %timeit f.reduce(J.gens())
1000 loops, best of 3: 1.11 ms per loop
```


Using the `GroebnerStrategy` object.


```
sage: %timeit J.reduce(f)
100000 loops, best of 3: 9.37 µs per loop
```



---

Comment by malb created at 2009-07-24 09:07:55

This patch requires Singular 3-1-0-4 which is available at

  http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090723.spkg


---

Comment by malb created at 2009-07-26 16:10:17

Doctests may fail on 32-bit system, #6628 contains the fix, sorry for the mixing.


---

Comment by malb created at 2009-07-26 16:12:17

Fixed doctests on 32-bit OSX.


---

Comment by AlexGhitza created at 2009-08-19 07:47:11

I am having trouble applying this patch on top of sage-4.1.1 + the latest spkg at #6476.  The issues occur in `multi_polynomial_libsingular.pyx`, and there is too much stuff going on for me to just rebase it myself...


---

Comment by malb created at 2009-08-19 10:04:03

Replying to [comment:3 malb]:
> This patch requires Singular 3-1-0-4 which is available at
> 
>   http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090723.spkg
> 

Note that this is outdated, use 

  http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090818.spkg

instead.


---

Attachment

should apply cleanly against 4.1.1


---

Comment by malb created at 2009-08-19 11:43:07

I rebased and updated the patch.


---

Attachment

apply after the previous patch


---

Comment by AlexGhitza created at 2009-08-27 00:54:48

Looks good.  The attached patch fixes some minor docstring problems.


---

Comment by malb created at 2009-08-27 09:34:25

Thanks, the referee patch looks good to me.


---

Comment by mvngu created at 2009-09-03 05:34:03

Merged both patches.


---

Comment by mvngu created at 2009-09-03 05:34:03

Resolution: fixed


---

Comment by mvngu created at 2009-09-03 05:34:54

See #6872 for a follow-up to this ticket.
