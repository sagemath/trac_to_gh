# Issue 9049: v4.4.1 bug in variety() over finite field extensions of Q?

Issue created by migration from Trac.

Original creator: cynthia_vinzant

Original creation time: 2010-05-25 20:37:38

Assignee: AlexGhitza

I'm interested in computing the 0-dimensional variety of an ideal over finite field extensions of Q. I've tried the following code both on my copy (v4.4.1) of sage and online and it produces an error message. My friend tried the same code on his v4.2 sage and it worked fine. Is it possible there's a bug in the newer version?


```
S.<t>=PolynomialRing(QQ)
F.<q>=QQ.extension(t^4+1)
R.<x,y>=PolynomialRing(F)
I=R.ideal(x,y^4+1)
I.variety()
```


This produces the following error message:
          	

Traceback (click to the left of this block for traceback)
...
ValueError: Length must be equal to the degree of this number field

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_11.py", line 10, in <module>
    exec compile(u'open("___code___.py","w").write("# -*- coding: utf-8 -*-\\n" + _support_.preparse_worksheet_cell(base64.b64decode("Uy48dD49UG9seW5vbWlhbFJpbmcoUVEpCkYuPHE+PVFRLmV4dGVuc2lvbih0XjQrMSkKUi48eCx5Pj1Qb2x5bm9taWFsUmluZyhGKQpJPVIuaWRlYWwoeCx5XjQrMSkKSS52YXJpZXR5KCk="),globals())+"\\n"); execfile(os.path.abspath("___code___.py"))
  File "", line 1, in <module>
    
  File "/tmp/tmpZcwb0q/___code___.py", line 7, in <module>
    exec compile(u'I.variety()
  File "", line 1, in <module>
    
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 407, in __call__
    return self.f(self._instance, *args, **kwds)
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 2094, in variety
    TI = self.triangular_decomposition('singular:triangLfak')
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 407, in __call__
    return self.f(self._instance, *args, **kwds)
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 901, in triangular_decomposition
    is_groebner = self.basis_is_groebner()
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/misc/cachefunc.py", line 322, in __call__
    return self._cachedmethod._instance_call(self._instance, *args, **kwds)
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/misc/cachefunc.py", line 466, in _instance_call
    cache[key] = self._cachedfunc.f(inst, *args, **kwds)
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 1666, in basis_is_groebner
    F = matrix(R, 1, self.ngens(), self.gens())
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/matrix/constructor.py", line 652, in matrix
    return matrix_space.MatrixSpace(ring, nrows, ncols, sparse=sparse)(entries)
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/matrix/matrix_space.py", line 405, in __call__
    return self.matrix(entries, copy=copy, coerce=coerce, rows=rows)
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/matrix/matrix_space.py", line 1136, in matrix
    return self.__matrix_class(self, entries=x, copy=copy, coerce=coerce) 
  File "matrix_generic_dense.pyx", line 68, in sage.matrix.matrix_generic_dense.Matrix_generic_dense.__init__ (sage/matrix/matrix_generic_dense.c:1997)
  File "multi_polynomial_libsingular.pyx", line 758, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:7176)
  File "parent.pyx", line 854, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)
  File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)
  File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/rings/number_field/number_field.py", line 1023, in _element_constructor_
    raise ValueError, "Length must be equal to the degree of this number field"
ValueError: Length must be equal to the degree of this number field


---

Comment by novoselt created at 2010-05-26 01:21:32

I just made the error message to be a code block.


---

Comment by syazdani created at 2010-06-23 17:35:31

I can verify that the bug still exists in v4.4.3.
This seems to be because of I.gens() is returning a tuple, while I.basis_is_groebner,  specifically the line

```
 F = matrix(R, 1, self.ngens(), self.gens())
```

expects I.gens() to be a list. Did I.gens() change its return type recently? A quick hack converting self.gens() to a list solves the problem. Should I provide that patch?


---

Comment by cynthia_vinzant created at 2010-06-24 18:00:00

>Should I provide that patch? 

That would be great. Thanks!


---

Attachment

converts a tuple to a list so matrix constructor isn't confused.


---

Comment by cynthia_vinzant created at 2010-06-25 17:52:36

Thanks very much -- it works wonderfully.


---

Comment by AlexGhitza created at 2010-09-22 12:02:01

Changing status from new to needs_review.


---

Comment by novoselt created at 2010-09-24 16:45:35

While the previous patch works for the problem of this ticket, it does not solve the real issue - you can construct a matrix from a list, but not from a tuple of the same elements, which does not make much sense. The new patch changes the relevant matrix constructor to allow tuples.


---

Comment by novoselt created at 2010-09-24 16:45:35

Changing component from algebraic geometry to linear algebra.


---

Comment by burcin created at 2010-09-24 17:47:07

Can you provide a more direct test to check the case when `entries` is a `tuple`?

Perhaps the example given in this ticket should be placed in the `.variety()` method of the ideal class. It is not guaranteed that we will always use the `Matrix_generic_dense` class in the future.


---

Comment by burcin created at 2010-09-24 17:47:07

Changing status from needs_review to needs_work.


---

Comment by novoselt created at 2010-09-24 18:20:00

Apply this patch only: allow construction of matrices from tuples.


---

Attachment

Done!


---

Comment by novoselt created at 2010-09-24 18:20:58

Changing status from needs_work to needs_review.


---

Attachment

alternative patch


---

Comment by burcin created at 2010-09-24 21:24:22

Thanks! That was quick. :)

I suggest to replace the check

```
if not isinstance(entries, list):
```

with

```
if not isinstance(entries, (list, tuple)):
```

instead of accepting `ValueError`s as well.

attachment:trac_9049_bug_in_matrices_from_tuples.take2.patch includes this alternative approach.

Please switch this to `positive_review` if you agree with my changes.


---

Comment by novoselt created at 2010-09-24 21:36:04

I thought about it, but I was not sure if it is necessary somewhere later to have exactly list, rather than tuple. Also, since the point of this try-block is to see whether or not it is possible to perform certain conversion, I think that any exception resulting from "wrong" conversion can be intercepted. If we just skip it for tuples, will we need later to skip it for, say, sequences? So I would prefer to stick with my patch as I think it is more universal. What do you think?


---

Comment by burcin created at 2010-09-24 21:54:18

`Sequence`s are lists:

```
sage: t = Sequence([1..5])
sage: isinstance(t, list)
True
```


Explicitly checking for the condition you are testing is better than trial and error. You cannot know the meaning of the `ValueError` returned from the base rings `__call__` method, especially in such a generic setting. 

IMHO, that `try` & `except` block should be cleaned up. However it's hard to do so as it is, since this is a generic constructor, there are no doctests or specification of what the acceptable input is and doctesting the whole sage library takes hours on my laptop.

Please reconsider my suggestion, with the "better safe then sorry" motto in mind.


---

Comment by novoselt created at 2010-09-24 22:46:54

OK, let's use the alternative patch! Switching to positive review.


---

Comment by novoselt created at 2010-09-24 22:46:54

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-28 10:57:41

Resolution: fixed
