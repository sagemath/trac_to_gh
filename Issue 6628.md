# Issue 6628: [with patch, needs review] Singular functions via libSingular

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-07-26 13:59:05

Assignee: malb

CC:  burcin

Keywords: singular, libsingular, commutative algebra

The attached patch implements the following:


```
sage: P = PolynomialRing(GF(127),10,'x')
sage: I = Ideal(P.random_element() for _ in range(3000))
sage: from sage.libs.singular.function import singular_function, lib
sage: groebner = singular_function('groebner')
sage: %time groebner(I)
CPU times: user 0.07 s, sys: 0.00 s, total: 0.08 s
Wall time: 0.08 s
[1]
```


For comparison, the Singular pexpect interface needs almost two seconds for the same task (due to string parsing on both ends, IPC, etc.)


```
sage: %time I.groebner_basis()
CPU times: user 0.96 s, sys: 0.24 s, total: 1.21 s
Wall time: 1.92 s
[1]
```


This patch requires an updated Singular SPKG (see below).


---

Comment by malb created at 2009-07-26 14:04:31

* This patch depends on #6596
 * The updated SPKG is available at http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090723.spkg


---

Comment by malb created at 2009-07-26 15:17:01

Burcin, I just replaced the patch to fix a doctest failure.


---

Comment by malb created at 2009-07-26 15:26:35

Btw. this also works now:


```
sage: from sage.libs.singular.function import singular_function, lib
sage: groebner = singular_function('groebner')
sage: groebner?
Type:           SingularLibraryFunction
Base Class:     <type 'sage.libs.singular.function.SingularLibraryFunction'>
String Form:    groebner (singular function)
Namespace:      Interactive
File:           /usr/local/sage-4.1/local/lib/python2.6/site-packages/sage/libs/singular/function.so
Docstring:

    groebner
    --------

    Procedure from library `standard.lib' (*note standard_lib::).

    *Syntax:*
         `groebner (' ideal_expression `)'
         `groebner (' module_expression `)'
         `groebner (' ideal_expression`,' int_expression `)'
         `groebner (' module_expression`,' int_expression `)'
...
```



---

Comment by PolyBoRi created at 2009-07-27 07:48:30

Hi!
It looks very promosing.
However, I have difficulties to apply the patch.
Using sage-4.1.0 and the updated singular spkg:

I tried it with and without the refactoring patch, also using a fresh installation:

```
sage -hg import ~/Downloads/libsingular_functions.patch 
applying /Users/michael/Downloads/libsingular_functions.patch
patching file module_list.py
Hunk #1 FAILED at 441
1 out of 1 hunks FAILED -- saving rejects to file module_list.py.rej
unable to find 'sage/libs/singular/polynomial.pyx' for patching
1 out of 1 hunks FAILED -- saving rejects to file sage/libs/singular/polynomial.pyx.rej
patching file sage/libs/singular/singular-cdefs.pxi
Hunk #3 FAILED at 207
Hunk #4 succeeded at 215 with fuzz 2 (offset -43 lines).
Hunk #7 FAILED at 853
2 out of 7 hunks FAILED -- saving rejects to file sage/libs/singular/singular-cdefs.pxi.rej
patching file sage/libs/singular/singular.pxd
Hunk #1 FAILED at 0
Hunk #2 FAILED at 26
2 out of 2 hunks FAILED -- saving rejects to file sage/libs/singular/singular.pxd.rej
patching file sage/libs/singular/singular.pyx
Hunk #1 FAILED at 24
Hunk #2 succeeded at 514 with fuzz 2 (offset -15 lines).
Hunk #3 FAILED at 593
2 out of 3 hunks FAILED -- saving rejects to file sage/libs/singular/singular.pyx.rej
patching file sage/rings/polynomial/multi_polynomial_libsingular.pyx
Hunk #1 FAILED at 1906
Hunk #2 FAILED at 2019
2 out of 2 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_libsingular.pyx.rej
```

Michael


---

Comment by malb created at 2009-07-27 15:24:04

Hi Michael, this is strange, here is what works for me

 * I installed the new Singular SPKG
 * `hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6596/libsingular_refactoring.patch`
 * `hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6628/libsingular_functions.patch`
 * `sage -b`

I have no failed hunks etc. with that.


---

Comment by PolyBoRi created at 2009-07-27 15:50:42

I am happy with the refactoring of my code :-).
I played with it and I like it.
From the Singular side, this nontrivial patch looks fine.


---

Comment by PolyBoRi created at 2009-07-29 07:21:15

Here some different timings with even better factor: opposite kind of example: very tiny input, output and almost nothing to compute, replaces some
singular interpreter call via pexpect with libsingular kernel function call


```python
from sage.libs.singular import function as sf
intersect=sf.SingularKernelFunction("intersect")
sage: P.<x,y,z>=QQ[]
sage: j=P.ideal(x,z)
sage: i=P.ideal(x,y)
sage: timeit("z=i.intersection(j)")
125 loops, best of 3: 5.12 ms per loop
sage: timeit("z=intersect(i,j)")
625 loops, best of 3: 60.9 µs per loop

```



---

Comment by malb created at 2009-08-04 11:14:02

It seems this patch makes docbuild choke because


```
groebner
--------
```


is contained in one docstring.


---

Comment by malb created at 2009-08-04 11:32:55

fixed in updated patch.


---

Comment by malb created at 2009-08-04 12:55:34

On IRC:

```
[13:02] <mvngu> malb: The package singular-3-1-0-4-20090723.spkg compiles OK on t2!
```



---

Attachment

fixing docstring issue


---

Attachment

apply after the previous patch


---

Comment by AlexGhitza created at 2009-08-20 11:10:06

This stuff is great!  I've attached a small referee patch that fixes some very minor typos.

I will note that line 280 of `singular-cdefs.pxi` is not entirely confidence-inspiring, but I believe the best way to test and refine this stuff is to get it into Sage and start using it a lot.

Note to the release manager: as pointed out above, one must first merge the new Singular spkg, and the patch(es) at #6596.


---

Comment by malb created at 2009-08-20 11:23:30

The referee patch looks good. I think the next step would be to port stuff in `multi_polynomial_ideal.py` to use this new stuff and see what happens.


---

Comment by AlexGhitza created at 2009-08-20 11:27:07

Replying to [comment:13 malb]:
> The referee patch looks good. I think the next step would be to port stuff in `multi_polynomial_ideal.py` to use this new stuff and see what happens.

Indeed.  I'm expecting awesomeness (more Singular functionality readily exposed in Sage), speed, and the occasional bug fix.

I'll try to have a look at #6596 soon, but it's a bit bigger, and it will probably take a few days.


---

Comment by PolyBoRi created at 2009-08-20 12:34:56

regarding 280:
I was a little bit confused, as I thought it would be the same type in idrec and sleftv.
But it's indeed void* in sleftv, so the code is correct, but the comment is wrong.
Nothing dangerous, you can remove the warning.
Michael


---

Comment by mvngu created at 2009-09-03 06:09:14

Resolution: fixed


---

Comment by mvngu created at 2009-09-03 06:09:14

Merged both patches.
