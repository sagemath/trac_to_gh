# Issue 2372: [with patch, needs review] speedup to matrix_from_rows_and_columns

Issue created by migration from Trac.

Original creator: dfdeshom

Original creation time: 2008-03-03 05:32:28

Assignee: dfdeshom

We make `matrix_from_rows_and_columns` a little faster by using well-known pyrex tricks.


---

Comment by dfdeshom created at 2008-03-03 05:34:59

Changing status from new to assigned.


---

Comment by dfdeshom created at 2008-03-03 15:23:16

Note: this is closely related to #2355, since speeding up  `matrix_from_rows_and_columns` will speed up `matrix.__getitem__()`


---

Comment by jsp created at 2008-03-12 13:49:57

This patch looks cleaner(?)


---

Attachment

Sorry for the duplicate! I missed that. But I could not resist to send my patch!

What do you think?

Cheers,

Jaap


---

Comment by dfdeshom created at 2008-03-12 18:34:02

Replying to [comment:4 jsp]:
> Sorry for the duplicate! I missed that. But I could not resist to send my patch!
> 
> What do you think?
> 
> Cheers,
> 
> Jaap
> 

Hi Jaap,
I'm willing to sacrifice a little elegance for speed gains. My function seems to be faster so far:

```
sage:  w = random_matrix(ZZ,2000,2000)

sage: %time w.matrix_from_rows_and_columns(range(1000),range(1300));
CPU times: user 0.42 s, sys: 0.13 s, total: 0.55 s
Wall time: 0.55

sage: %time w.matrix_from_rows_and_columns(range(1000),range(1300));
CPU times: user 0.48 s, sys: 0.05 s, total: 0.53 s
Wall time: 0.54

sage: %time w.matrix_from_rows_and_columns(range(1000),range(1300));
CPU times: user 0.49 s, sys: 0.05 s, total: 0.54 s
Wall time: 0.53
```


vs

```
Loading SAGE library. Current Mercurial branch is: jaap

sage:  w = random_matrix(ZZ,2000,2000)

sage: %time w.matrix_from_rows_and_columns(range(1000),range(1300));
CPU times: user 0.73 s, sys: 0.12 s, total: 0.84 s
Wall time: 0.84

sage: %time w.matrix_from_rows_and_columns(range(1000),range(1300));
CPU times: user 0.74 s, sys: 0.10 s, total: 0.84 s
Wall time: 0.84

sage: %time w.matrix_from_rows_and_columns(range(1000),range(1300));
CPU times: user 0.72 s, sys: 0.12 s, total: 0.84 s
Wall time: 0.83
```


All times are on sage.math. If you can do better, great :)


---

Comment by jsp created at 2008-03-14 13:26:32

Ok, time is money. So I better give a positive review.

One question before I do so:
why not cdef i an j?

```
        cdef Py_ssize_t nrows, ncols,i,j,k,r

```


All test in deve/sage/sage/matrix passed.


---

Attachment


---

Comment by dfdeshom created at 2008-03-14 14:38:18

Replying to [comment:6 jsp]:
> why not cdef i an j?
> {{{
>         cdef Py_ssize_t nrows, ncols,i,j,k,r
> 
> }}}

Good point. I've added these declarations and updated the patch (2372.patch). All tests in sage/matrix pass.


---

Comment by jsp created at 2008-03-14 18:34:38

I had that tested already :)


---

Comment by mabshoff created at 2008-03-16 00:01:58

Resolution: fixed


---

Comment by mabshoff created at 2008-03-16 00:01:58

Merged 2372.patch in Sage 2.10.4.rc0
