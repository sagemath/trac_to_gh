# Issue 4631: possible memory leak in matrix code?

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-11-27 00:34:14

Assignee: mabshoff

CC:  robertwb

So I was looking at another ticket, and noticed the following memory usage of Hermite normal form:


```
sage: M = random_matrix(ZZ,50,50)

sage: get_memory_usage()
'1104M+'

sage: for _ in range(100): foo = M.hermite_form()
   ....: 

sage: get_memory_usage()
'1170M+'
```


It could be that the memory is getting "lost" in some other way, but it might be nice to see why it's happening. In fact, it's probably got nothing to do with HNF:


```
sage: get_memory_usage()
'1170M+'

sage: for _ in range(100): foo = M.echelon_form()
   ....: 

sage: get_memory_usage()
'1237M+'
```


I'm happy to find out that there's a reasonable explanation for this.


---

Comment by mabshoff created at 2008-11-28 21:36:07

This might be related to #4639.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-10 06:26:46

This may be relevant here. Either way it warrants consideration to call %reset at the end of Sage, but that would be another ticket.

```
On Mon, Dec 8, 2008 at 19:15, frank wang <f.yw`@`hotmail.com> wrote:
> > Hi,
> >
> > I have a program with some variables consume a lot of memory. The first time
> > I run it, it is fine. The second time I run it, I will get MemoryError. If I
> > close the ipython and reopen it again, then I can run the program once. I am
> > looking for a command to delete the intermediate variable once it is not
> > used to save memory like in matlab clear command.

How are you running this program? Be aware that IPython may be holding
on to objects and preventing them from being deallocated. For example:

In [7]: !cat memtest.py
class A(object):
    def __del__(self):
        print 'Deleting %r' % self


a = A()

In [8]: %run memtest.py

In [9]: %run memtest.py

In [10]: %run memtest.py

In [11]: del a

In [12]:
Do you really want to exit ([y]/n)?

$ python memtest.py
Deleting <__main__.A object at 0x915ab0>


You can remove some of these references with %reset and maybe a
gc.collect() for good measure.


In [1]: %run memtest

In [2]: %run memtest

In [3]: %run memtest

In [4]: %reset
Once deleted, variables cannot be recovered. Proceed (y/[n])?  y
Deleting <__main__.A object at 0xf3e950>
Deleting <__main__.A object at 0xf3e6d0>
Deleting <__main__.A object at 0xf3e930>

-- Robert Kern "I have come to believe that the whole world is an enigma, 
a harmless enigma that is made terrible by our own mad attempt to interpret 
it as though it had an underlying truth." -- Umberto Eco _______________________________________________ 
Numpy-discussion mailing list Numpy-discussion`@`scipy.org 
http://projects.scipy.org/mailman/listinfo/numpy-discussion 
```



---

Comment by mabshoff created at 2008-12-14 17:53:06

Note that the latest upstream Cython 0.10.3 (merged in Sage 3.2.2.rc0 via #4798) improves things considerably:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: M = random_matrix(ZZ,50,50)
sage: get_memory_usage()
416.19921875
sage: for _ in range(100): foo = M.hermite_form()
....: 
sage: del foo
sage: get_memory_usage()
423.74609375
sage: for _ in range(100): foo = M.hermite_form()
....: 
sage: get_memory_usage()
424.73828125
sage: for _ in range(100): foo = M.hermite_form()
....: 
sage: get_memory_usage()
425.703125
```



---

Comment by mabshoff created at 2008-12-17 04:39:08

But #4639 does not improve this further. Note that "base" is the initial memory consumption:

```
sage: base=get_memory_usage()
sage: M = random_matrix(ZZ,50,50)
sage: for _ in range(100): foo = M.hermite_form()
....: 
sage: get_memory_usage()-base
7.5625
sage: for _ in range(100): foo = M.hermite_form()
....: 
sage: get_memory_usage()-base
8.515625
sage: for _ in range(100): foo = M.hermite_form()
....: 
sage: get_memory_usage()-base
9.5
```


Cheers,

Michael


---

Comment by burcin created at 2008-12-27 00:56:19

#4883 might be relevant here.


---

Comment by mabshoff created at 2009-01-04 03:05:36

The new Sage 3.2.3+eMPIRe build picked up the following leak in tut.py:

```
==5027== 8 bytes in 1 blocks are definitely lost in loss record 32 of 19,079
==5027==    at 0x4C22FEB: malloc (vg_replace_malloc.c:207)
==5027==    by 0x84B3A4B: __gmpz_init_set_si (in /home/mabshoff/build/eMPIRe/sage-3.2.3.final/local/lib/libgmp.so.3.4.1)
==5027==    by 0x271A110A: __pyx_pf_4sage_6matrix_4misc_matrix_integer_sparse_rational_reconstruction (misc.c:129
17)
==5027==    by 0x417E92: PyObject_Call (abstract.c:1861)
==5027==    by 0x25632FFA: __pyx_pf_4sage_6matrix_21matrix_integer_sparse_21Matrix_integer_sparse_rational_recons
truction (matrix_integer_sparse.c:8698)==5027==    by 0x417E92: PyObject_Call (abstract.c:1861)
==5027==    by 0x271B2171: __pyx_pf_4sage_6matrix_4misc_matrix_rational_echelon_form_multimodular (misc.c:15034)
==5027==    by 0x417E92: PyObject_Call (abstract.c:1861)
==5027==    by 0x4816E1: PyEval_CallObjectWithKeywords (ceval.c:3442)
==5027==    by 0x25CAAAE3: __pyx_pf_4sage_6matrix_22matrix_rational_sparse_22Matrix_rational_sparse__echelon_form
_multimodular (matrix_rational_sparse.c:12416)
==5027==    by 0x417E92: PyObject_Call (abstract.c:1861)
==5027==    by 0x4816E1: PyEval_CallObjectWithKeywords (ceval.c:3442)
==5027==    by 0x25CABA89: __pyx_pf_4sage_6matrix_22matrix_rational_sparse_22Matrix_rational_sparse_echelon_form 
(matrix_rational_sparse.c:12116)
```

William says:

```
[6:49pm] mabs: Yeah, I need to start poking around.
[6:52pm] wstein: That could only leak if there is an exception raised somewhere in the body of the function.
[6:52pm] wstein: In misc.pyx
[6:53pm] wstein: So an exception must be raised.
[6:54pm] wstein: maybe line 235 of matrix/misc.pyx could raise an exception,
[6:54pm] wstein: hence return from that function without clearing gmp vars
[6:58pm] mabs: mmhh
```



---

Comment by mabshoff created at 2009-01-04 03:05:45

Changing status from new to assigned.


---

Comment by craigcitro created at 2010-01-17 19:13:06

This seems to be fixed in sage-4.3:


```
sage: M = random_matrix(ZZ, 50, 50)
sage: get_memory_usage()
182.859375
sage: for _ in range(100): foo = M.echelon_form()
....: 
sage: get_memory_usage()
183.32421875
sage: for _ in range(100): foo = M.hermite_form()
....: 
sage: get_memory_usage()
183.32421875
```


Given that it was vague to start with, I'm closing this as worksforme. (I tested on my machine and sage.math, with the same results.)


---

Comment by craigcitro created at 2010-01-17 19:13:06

Resolution: worksforme
