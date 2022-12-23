# Issue 6223: Remove ext/python_*.pxi

Issue created by migration from https://trac.sagemath.org/ticket/6223

Original creator: robertwb

Original creation time: 2009-06-05 09:41:06

Assignee: tbd

Cython ships them all now, no need to have them here.


---

Comment by jdemeyer created at 2010-10-12 13:09:54

Removing `include "../ext/python_list.pxi"` from `sage/structure/coerce_dict.pyx` gives trouble:


```
python `which cython` --embed-positions --directive cdivision=True,autotestdict=False -I/usr/local/src/sage-4.6.alpha3/devel/sage-test -o sage/structure/coerce_dict.c sage/structure/coerce_dict.pyx

Error converting Pyrex file to C:
------------------------------------------------------------
...

    cdef get(self, k1, k2, k3):
        cdef Py_ssize_t h = (<Py_ssize_t><void *>k1 + 13*<Py_ssize_t><void *>k2 ^ 503*<Py_ssize_t><void *>k3)
        if h < 0: h = -h
        cdef Py_ssize_t i
        bucket = <object>PyList_GET_ITEM(self.buckets, h % PyList_GET_SIZE(self.buckets))
                                       ^
------------------------------------------------------------

/usr/local/src/sage-4.6.alpha3/devel/sage-test/sage/structure/coerce_dict.pyx:225:40: undeclared name not builtin: PyList_GET_ITEM
```



---

Comment by jdemeyer created at 2010-10-12 13:09:54

Changing status from new to needs_work.


---

Attachment


---

Attachment


---

Comment by jdemeyer created at 2013-04-13 15:47:35

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by vbraun created at 2013-04-18 17:20:31

Great!


---

Comment by vbraun created at 2013-04-18 17:20:31

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-04-19 08:40:42

Thanks!


---

Comment by jdemeyer created at 2013-04-23 09:40:02

Resolution: fixed
