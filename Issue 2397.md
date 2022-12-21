# Issue 2397: speed up matrix_from_rows

Issue created by migration from Trac.

Original creator: dfdeshom

Original creation time: 2008-03-05 16:47:07

Assignee: dfdeshom

matrix_from_rows could be made faster by using  PY_TYPE_CHECK or pyrex-style for loops.


---

Comment by dfdeshom created at 2008-03-05 17:31:13

I've gone ahead and added the same pyrex stuff to matrix_from_columns too since these methods are nearly identical.


---

Comment by dfdeshom created at 2008-03-05 17:31:13

Changing status from new to assigned.


---

Comment by jsp created at 2008-03-12 11:52:50

This could also be done with matrix_from_rows_and_columns(self, rows, columns)

I'll open a new ticket.

Patch worked.

Jaap


---

Comment by jsp created at 2008-03-12 19:29:49

All test passed with ./sage -t devel/sage/sage/matrix/matrix1.pyx

But I got a segmentation fault running:

./sage -t devel/sage/sage/matrix/matrix2.pyx

even after ./sage -ba


```
(gdb) r
Starting program: /home/jaap/work/downloads/sage-2.10.3/local/bin/python .doctest_matrix2.py
[Thread debugging using libthread_db enabled]
[New Thread -1209047360 (LWP 30302)]
[Detaching after fork from child process 30305. (Try `set detach-on-fork off'.)]

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread -1209047360 (LWP 30302)]
0x0014cd72 in __gmpz_set () from /home/jaap/work/downloads/sage-2.10.3/local/lib/libgmp.so.3
(gdb) bt
#0  0x0014cd72 in __gmpz_set () from /home/jaap/work/downloads/sage-2.10.3/local/lib/libgmp.so.3
#1  0x0b0e86e0 in ?? ()
#2  0x0b0e86e0 in ?? ()
#3  0xbfa980d8 in ?? ()
#4  0x01b9be98 in __pyx_f_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense_get_unsafe (__pyx_v_self=0x0, __pyx_v_i=1320220, 
    __pyx_v_j=1348880) at sage/matrix/matrix_integer_dense.c:5143
Backtrace stopped: previous frame inner to this frame (corrupt stack?)
(gdb) 


This concerns line 373 in matrix2.pyx


```


This seems te be related.


---

Comment by jsp created at 2008-03-12 19:53:23

This seems to be consistent. I can reproduce this Segmentation fault on an other install.

My hypothesis is that a cdef is replaced by a def. Is this possible?


---

Comment by mabshoff created at 2008-03-12 19:56:42

This patch actually causes segfaults all over the map.


---

Attachment

Found the bug and doctests on matrix0,1,2 pass. I've updated the patch (2397.patch) but please ignore the bundle file (I'm having trouble making hg bundles work). More ewviews, please!


---

Attachment

The hg bundle should also work now.


---

Comment by jsp created at 2008-03-14 18:27:24

This works for me now (the patch).

No segfaults anymore. Can someone explain what went wrong?!!


---

Comment by dfdeshom created at 2008-03-14 18:34:13

Replying to [comment:10 jsp]:
> This works for me now (the patch).
> 
> No segfaults anymore. Can someone explain what went wrong?!!


Gladly. The bug was in `matrix_from_columns`, around line 718.  I was checking against `self._ncols`:
  

```
            for r from 0 <= r < self._ncols: 
                A.set_unsafe(r,k, self.get_unsafe(r,columns[i])) 
```


when I should be checking against `self._nrows`

```
            for r from 0 <= r < self._nrows: 
                A.set_unsafe(r,k, self.get_unsafe(r,columns[i])) 
```


This didn't go over well for non-sqaure matrices, since we weren't checking bounds anyway.


---

Comment by mabshoff created at 2008-03-15 06:29:59

Replying to [comment:9 dfdeshom]:
> The hg bundle should also work now. 

Hi Didier,

we have a very strong preference for patches over bundles, especially for single commits. Is there a specific reason you don't use mercurial to export patches?

Cheers,

Michael


---

Comment by dfdeshom created at 2008-03-15 06:47:08

Replying to [comment:12 mabshoff]:
> Replying to [comment:9 dfdeshom]:
> > The hg bundle should also work now. 
> 
> Hi Didier,
> 
> we have a very strong preference for patches over bundles, especially for single commits. Is there a specific reason you don't use mercurial to export patches?

I remember in another ticket (#2421) you said to submit mercurial patches so I could get credit. I thought you meant bundles, so that's what I started doing. I think the issue here is that there are 2 ways to get patches out of hg: either hg diff > patch or hg export rev > patch. The differences between them are very small, at first glance. So I'm guessing that hg export rev > patch is the way to go? Maybe this should be written somewhere?


---

Comment by mabshoff created at 2008-03-15 08:05:38

> I remember in another ticket (#2421) you said to submit mercurial patches so I could get credit. I thought you meant bundles, so that's what I started doing. I think the issue here is that there are 2 ways to get patches out of hg: either hg diff > patch or hg export rev > patch. The differences between them are very small, at first glance. So I'm guessing that hg export rev > patch is the way to go? Maybe this should be written somewhere?
> 

Yep, hg export is the way to go. It is in the development manual, but I am too lazy to find the exact location. I will merge the bundles from this ticket and also #2459, but it would be great if you could use hg export for future patches.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-15 08:05:48

Merged 2397.hg in Sage 2.10.4.alpha0


---

Comment by mabshoff created at 2008-03-15 08:05:48

Resolution: fixed
