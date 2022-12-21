# Issue 6053: Cython numpy broken in notebook

Issue created by migration from Trac.

Original creator: ghtdak

Original creation time: 2009-05-17 04:44:56

Assignee: jkantor

Keywords: numpy, cython, notebook

in a notebook cell with



```
%cython
cimport numpy as np
```


an error is thrown because numpy/arrayobject.h isn't found by gcc.  No directive for the numpy include directories is part of the compiler invocation.

the header path is:

$SAGE_LOCAL/lib/python2.5/site-packages/numpy/core/include/numpy/arrayobject.h




---

Attachment


---

Comment by mhansen created at 2009-05-28 07:17:21

Looks good to me.

Merged in 4.0.rc1.


---

Comment by mhansen created at 2009-05-28 07:17:21

Resolution: fixed
