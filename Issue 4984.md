# Issue 4984: Clean up __getitem__ for matrices once Cython is smarter

Issue created by migration from https://trac.sagemath.org/ticket/4984

Original creator: craigcitro

Original creation time: 2009-01-16 02:36:55

Assignee: was

So we currently use several Python/C API calls to speed up the `__getitem__` method in `sage/matrix/matrix0.pyx`. In particular, we do several typechecks against standard Python types, and replacing generic `PY_TYPE_CHECK` calls with specific Python/C API calls (like `PySlice_Check`) provides a significant speedup. Once Cython can do all these things for us, we should clean up `__getitem__` so that it's more readable/portable. 

Alternatively, if such functionality still doesn't exist in Cython, one should feel free to go, implement that functionality, get it merged, create a new Cython spkg, and then make these changes. `:)`


---

Comment by AlexGhitza created at 2009-01-23 02:45:25

Changing type from defect to enhancement.


---

Comment by jdemeyer created at 2016-01-22 10:47:31

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2016-01-22 10:47:31

`PY_TYPE_CHECK` is gone.


---

Comment by jdemeyer created at 2016-01-22 10:47:39

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-02-23 22:59:24

Resolution: fixed
