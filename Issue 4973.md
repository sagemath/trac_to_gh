# Issue 4973: rewrite the function __getitem__ in matrix0.pyx to not explicitly use the python/C api

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-01-14 09:30:10

Assignee: craigcitro

CC:  craigcitro

`__getitem__` in matrix0.pyx uses C Python API and that code should have *never* been merged as is. The C API was used to get maximum speed. If possible rewrite this code to not use the C API, but it should not lose too much speed. This might be impossible or require adding bits to Cython.

Cheers,

Michael


---

Comment by jason created at 2009-01-14 10:25:41

Changing status from new to assigned.


---

Comment by jason created at 2009-01-14 10:25:41

Changing assignee from craigcitro to jason.


---

Attachment


---

Comment by jason created at 2009-01-14 15:30:23

I didn't mean to mark this as needs review.  There are a few additions to the getitem syntax (like allowing negative indices) for which doctests need to be changed.  The main function should be about done, though.  More speed regression testing should be done as well.


---

Attachment

Apply matrix-getitem.2.patch only.  This eliminates the C API calls, but keeps the speed, approximately (some cases are a bit slower, some are a bit faster).  This patch also adds more standard slicing functionality to getitem, which actually changes a few behaviors which went against python convention.  See the changed docstrings, for example.


---

Attachment

apply only matrix-getitem.3.patch.  This patch replaces the call to normalize_slice with a standard python idiom for the same functionality.


---

Comment by craigcitro created at 2009-01-15 19:05:36

So I've reviewed Jason's patch, and everything looks good -- except that for lots of cases, in particular the primary `M[i,j]` use case, things are noticeably slower (on the order of 25%). This is no good on such a basic operation.

This code actually does *more* than the previous version (i.e. accepts additional types, negative indices, etc), and is still the same speed. 

Cython doesn't quite do everything we want to get maximal speed out of this call. I'm going to submit another patch that uses it more judiciously, but gets yet more speed, because this is such an important piece of code.


---

Attachment

New version of the patch. So this adds one additional Python/C API call, but gets a 10% speedup for the case of `M[i,j]`, which I think is worthwhile. Furthermore, it's only necessary because this is a case where Cython doesn't do enough specific optimization for us -- one day, when Cython gets smarter, we can clean this up more.

Also fixed a bug in matrix indexing with tuples, and added a doctest for that case.


---

Comment by craigcitro created at 2009-01-15 22:54:28

As a note, the patches to be applied, in order:

 * `matrix-getitem.3.patch`
 * `trac-4973-pt2.patch`


---

Comment by jason created at 2009-01-16 01:57:47

Doctests pass. I've tried lots of the doc examples and they are faster or the same as the old code, except for the following case.  These commands are each executed in a fresh Sage session.


```

AFTER PATCH:

sage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 167 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 168 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 166 µs per loop


BEFORE PATCH:

sage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 134 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 138 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 143 µs per loop
```


So, positive review if this regression is fixed.


---

Attachment

Patch attached that fixes the regression (at least on my machine).


---

Comment by jason created at 2009-01-16 02:23:50

Okay, pt3 fixes the regression.  Here are my new timings:


```
AFTER PATCH:

sage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 167 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 168 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 166 µs per loop


BEFORE PATCH:

sage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 134 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 138 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 143 µs per loop
```


So we're faster than the original code again.

Great job. Positive review, with the doctest fix that I'm going to post in a second.  I presume that mabshoff will run all doctests on it to make sure that there are no errors in other code because of the additional capabilities.


---

Comment by jason created at 2009-01-16 02:24:33

apply on top of previous patch


---

Attachment


---

Comment by jason created at 2009-01-16 02:26:07

I mean, *here* are my new timings after the regression fix in pt3.patch:


```
AFTER PATCH:

sage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 167 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 168 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 166 µs per loop


BEFORE PATCH:

sage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 134 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 138 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 143 µs per loop
```


I copied the wrong thing before.


---

Comment by jason created at 2009-01-16 02:27:14

Grrr, apparently I again copied the wrong thing.  So much for middle-click vs. ctrl-v.

*here* are the new timings:


```
sage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 125 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 120 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 124 µs per loop
```



---

Comment by robertwb created at 2009-01-16 19:52:02

BTW, now it's even faster to write


```
row_index, col_index = key_tuple
```


Then 


```
row_index = key_tuple[0] 
col_index = key_tuple[1]
```



---

Comment by craigcitro created at 2009-01-16 20:00:43

Though do either of those keep up with directly using `PyTuple_GET_ITEM`? I didn't think they did based on my timings, but I'd be happy to find out otherwise.


---

Comment by robertwb created at 2009-01-16 20:24:34

Here's the actual generated code for `x,y = t`


```
    if (PyTuple_CheckExact(__pyx_v_t) && PyTuple_GET_SIZE(__pyx_v_t) == 2) {
    PyObject* tuple = __pyx_v_t;
    __pyx_2 = PyTuple_GET_ITEM(tuple, 0);
    Py_INCREF(__pyx_2);
    Py_DECREF(__pyx_v_x);
    __pyx_v_x = __pyx_2;
    __pyx_2 = 0;
    __pyx_2 = PyTuple_GET_ITEM(tuple, 1);
    Py_INCREF(__pyx_2);
    Py_DECREF(__pyx_v_y);
    __pyx_v_y = __pyx_2;
    __pyx_2 = 0;
  }
  else {
     [generic code]
  }
```


If `t` is declared to be a tuple, half of the first check shouldn't be needed (I don't think this optimization is in place yet). So it should be as fast as type check + length check + PyTuple_GET_ITEM. In any case, it's faster than indexing not using PyTyple_GET_ITEM.


---

Comment by craigcitro created at 2009-01-17 21:31:29

Ah, excellent. In this particular case, we've just done both of those checks -- the typecheck and the length check -- so I'm going to say we should stick with the `PyTuple_GET_ITEM` (we also raise an explicit exception if the length is wrong), but I'm happy to know that in general, Cython generates such good code.

It'd be nice if Cython skipped the typecheck when it knew the type -- should a ticket be filed on the Cython trac server?


---

Comment by robertwb created at 2009-01-17 21:39:47

Sounds like a good course of action for now. 

Yes, that should be a ticket on the Cython trac.


---

Comment by mabshoff created at 2009-01-18 14:44:33

Resolution: fixed


---

Comment by mabshoff created at 2009-01-18 14:44:33

Merged

 * matrix-getitem.3.patch
 * trac-4973-pt2.patch
 * trac-4973-pt3.patch
 * doctest-fix.patch 

in Sage 3.3.alpha0

Cheers,

Michael
