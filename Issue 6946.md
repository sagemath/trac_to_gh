# Issue 6946: Duplicated mpmath <-> sympy/mpmath and delaunay <-> matplotlib/delaunay

Issue created by migration from Trac.

Original creator: pcpa

Original creation time: 2009-09-16 20:19:33

Assignee: mabshoff

CC:  jason

The delaunay packages appears to be the same, with just some name changes.

But the mpmath while providing the same feature, has a significant large amount of patches.

In either case, if patching sage to use sympy/mpmath and mpatplotlib/delaunay, the doctests works, but there may exit some special reason to use mpmath instead of sympy/mpmath.


---

Attachment

delaunay rpm patch


---

Comment by fredrik.johansson created at 2009-09-17 16:30:48

(Sorry, accidentally changed the description instead of posting a comment. Restored the original description.)

sympy/mpmath should probably be regarded as an internal module of sympy. It includes some sympy-specific changes and is updated less frequently. More likely sympy/mpmath will go away some time in the future.


---

Comment by pcpa created at 2009-09-17 23:41:46

Replying to [comment:2 fredrik.johansson]:
> (Sorry, accidentally changed the description instead of posting a comment. Restored the original description.)
> 
> sympy/mpmath should probably be regarded as an internal module of sympy. It includes some sympy-specific changes and is updated less frequently. More likely sympy/mpmath will go away some time in the future.

Many thanks for the reply. I was unsure if I should create a mandriva package for mpmath, or assume it was unintended duplication of code. I even just updated the mpmath patch to also use sympy.mpmath from sage/libs/mpmath/utils.pyx

I will add a python-mpmath package to mandriva, and revert the patch to use sympy.mpmath from my rpm. Guess for now it will also have duplicated %py_platsitedir/sympy/mpath and %py_platsitedir/mpath, what may be a source of confusion...


---

Comment by pcpa created at 2009-09-17 23:43:30

just for documentation - but this patch should be no longer applied, and instead, create the python-mpmath rpm package


---

Attachment


---

Comment by mmezzarobba created at 2015-04-13 13:30:57

Apparently `sympy.mpmath` no longer exists, nor does `delaunay`.


---

Comment by mmezzarobba created at 2015-04-13 13:30:57

Changing status from new to needs_review.


---

Comment by vdelecroix created at 2015-04-24 21:43:17

But it is still mentioned in the sympy documentation [http://docs.sympy.org/dev/modules/mpmath/setup.html#mpmath-under-sympy](http://docs.sympy.org/dev/modules/mpmath/setup.html#mpmath-under-sympy)(http://docs.sympy.org/dev/modules/mpmath/setup.html#mpmath-under-sympy). Weird!


---

Comment by kcrisman created at 2015-05-29 02:15:29

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-06-19 08:41:47

Resolution: fixed
