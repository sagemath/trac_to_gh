# Issue 2239: Leak in totallyreal.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-02-20 23:31:49

Assignee: craigcitro

Running the doctest under valgrind leads to:

```
==24549== 12,656 (10,848 direct, 1,808 indirect) bytes in 226 blocks are definitely lost in loss record 7,761 of 7,934
==24549==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==24549==    by 0xB323D52: __pyx_f_4sage_5rings_7integer_fast_tp_new (integer.c:19858)
==24549==    by 0x10FA7030: __pyx_pf_4sage_5rings_10polynomial_28polynomial_integer_dense_ntl_28Polynomial_integer_dense_ntl
___getitem__(_object*, _object*) (polynomial_integer_dense_ntl.cpp:2898)
==24549==    by 0x10FA76B0: __pyx_pf_4sage_5rings_10polynomial_28polynomial_integer_dense_ntl_28Polynomial_integer_dense_ntl
_list(_object*, _object*) (polynomial_integer_dense_ntl.cpp:6561)
==24549==    by 0x415542: PyObject_Call (abstract.c:1860)
==24549==    by 0x10FB2902: __pyx_pf_4sage_5rings_10polynomial_28polynomial_integer_dense_ntl_28Polynomial_integer_dense_ntl
___floordiv__(_object*, _object*) (polynomial_integer_dense_ntl.cpp:4761)
==24549==    by 0x41580C: binary_op1 (abstract.c:398)
==24549==    by 0x416CDD: PyNumber_FloorDivide (abstract.c:450)
==24549==    by 0x142523FE: __pyx_pf_4sage_5rings_12number_field_16totallyreal_data_lagrange_degree_3 (totallyreal_data.c:39
75)
==24549==    by 0x415542: PyObject_Call (abstract.c:1860)
==24549==    by 0x14271583: __pyx_pf_4sage_5rings_12number_field_16totallyreal_data_7tr_data_incr (totallyreal_data.c:7355)
==24549==    by 0x415542: PyObject_Call (abstract.c:1860)
```

And:

```
==24549== 25,424 (21,792 direct, 3,632 indirect) bytes in 454 blocks are definitely lost in loss record 7,823 of 7,934
==24549==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==24549==    by 0xB323D52: __pyx_f_4sage_5rings_7integer_fast_tp_new (integer.c:19858)
==24549==    by 0x458D92: type_call (typeobject.c:422)
==24549==    by 0x415542: PyObject_Call (abstract.c:1860)
==24549==    by 0x10FAC427: __pyx_pf_4sage_5rings_10polynomial_28polynomial_integer_dense_ntl_28Polynomial_integer_dense_ntl
___init__(_object*, _object*, _object*) (polynomial_integer_dense_ntl.cpp:2659)
==24549==    by 0x458E40: type_call (typeobject.c:436)
==24549==    by 0x415542: PyObject_Call (abstract.c:1860)
==24549==    by 0x482221: PyEval_EvalFrameEx (ceval.c:3775)
==24549==    by 0x4852CA: PyEval_EvalCodeEx (ceval.c:2831)
==24549==    by 0x4CE817: function_call (funcobject.c:517)
==24549==    by 0x415542: PyObject_Call (abstract.c:1860)
==24549==    by 0x41BC62: instancemethod_call (classobject.c:2497)
```

And:

```
==24549== 25,368 (21,744 direct, 3,624 indirect) bytes in 453 blocks are definitely lost in loss record 7,827 of 7,934
==24549==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==24549==    by 0xB323D52: __pyx_f_4sage_5rings_7integer_fast_tp_new (integer.c:19858)
==24549==    by 0x458D92: type_call (typeobject.c:422)
==24549==    by 0x415542: PyObject_Call (abstract.c:1860)
==24549==    by 0x10FAC427: __pyx_pf_4sage_5rings_10polynomial_28polynomial_integer_dense_ntl_28Polynomial_integer_dense_ntl
___init__(_object*, _object*, _object*) (polynomial_integer_dense_ntl.cpp:2659)
==24549==    by 0x458E40: type_call (typeobject.c:436)
==24549==    by 0x415542: PyObject_Call (abstract.c:1860)
==24549==    by 0x482221: PyEval_EvalFrameEx (ceval.c:3775)
==24549==    by 0x4852CA: PyEval_EvalCodeEx (ceval.c:2831)
==24549==    by 0x4CE7B0: function_call (funcobject.c:517)
==24549==    by 0x415542: PyObject_Call (abstract.c:1860)
==24549==    by 0x41BC62: instancemethod_call (classobject.c:2497)
```

And:

```
==24549== 165,032 (141,456 direct, 23,576 indirect) bytes in 2,947 blocks are definitely lost in loss record 7,910 of 7,934
==24549==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==24549==    by 0xB323D52: __pyx_f_4sage_5rings_7integer_fast_tp_new (integer.c:19858)
==24549==    by 0xB344219: __pyx_f_4sage_5rings_7integer_7Integer__floordiv (integer.c:7921)
==24549==    by 0xB343FFF: __pyx_pf_4sage_5rings_7integer_7Integer___floordiv__ (integer.c:8020)
==24549==    by 0x41580C: binary_op1 (abstract.c:398)
==24549==    by 0x416CDD: PyNumber_FloorDivide (abstract.c:450)
==24549==    by 0x10FB29B1: __pyx_pf_4sage_5rings_10polynomial_28polynomial_integer_dense_ntl_28Polynomial_integer_dense_ntl
___floordiv__(_object*, _object*) (polynomial_integer_dense_ntl.cpp:4779)
==24549==    by 0x41580C: binary_op1 (abstract.c:398)
==24549==    by 0x416CDD: PyNumber_FloorDivide (abstract.c:450)
==24549==    by 0x142523FE: __pyx_pf_4sage_5rings_12number_field_16totallyreal_data_lagrange_degree_3 (totallyreal_data.c:39
75)
==24549==    by 0x415542: PyObject_Call (abstract.c:1860)
==24549==    by 0x14271583: __pyx_pf_4sage_5rings_12number_field_16totallyreal_data_7tr_data_incr (totallyreal_data.c:7355)
```

In total:

```
==24549==    definitely lost: 196,328 bytes in 4,087 blocks.
==24549==    indirectly lost: 36,148 bytes in 4,090 blocks.
==24549==      possibly lost: 267,538 bytes in 814 blocks.
==24549==    still reachable: 30,329,036 bytes in 188,033 blocks.
==24549==         suppressed: 0 bytes in 0 blocks.
```


Cheers,

Michael


---

Comment by craigcitro created at 2008-02-28 06:57:48

So there's definitely a leak somewhere here, but it's not in the totallyreal code. For example, if you define:


```
def foo(f):
    tmp = f.list()
    rts = numpy.roots(tmp)
```


and run this with a `polynomial_integer_dense_ntl` as input, it'll leak like crazy. If you pass it anything else, it doesn't leak at all. It's something to do with the interaction between NTL and numpy, though I don't understand what the problem is yet. In particular, if you run either of the two lines above independently, over and over, you don't get a memory leak. It's only in concert that they leak ...

If someone understands this, they should explain it to me. :) In any event, it's not in the totallyreal code ...

-cc


---

Comment by was created at 2008-02-28 17:33:26

SOLUTION: If you change the list into a list of Python ints (which is surely what numpy is vastly more comfortable with) taht completely gets rid of the memory leak.  I'm guessing numpy is just doing some sort of black magic to convert the list to some internal format, and it makes assumptions that aren't satisfied by Sage integers.  The right solution is to give numpy standard Python input, so it can do whatever black magic it wants under valid assumptions.  The code below illustrates how to do this.



```
id=115|
import numpy
def foo(f):
    tmp = [int(a) for a in f.list()]
    rts = numpy.roots(tmp)
```



```
id=114|
x = polygen(ZZ)
f = x^10 - 1
print get_memory_usage()
for _ in xrange(10^4): a = foo(f)
print get_memory_usage()
///
172M+
172M+
```



---

Comment by was created at 2008-02-28 17:34:14

Sorry, I forgot to delete the id's:


```
import numpy
def foo(f):
    tmp = [int(a) for a in f.list()]
    rts = numpy.roots(tmp)
```



```
x = polygen(ZZ)
f = x^10 - 1
print get_memory_usage()
for _ in xrange(10^4): a = foo(f)
print get_memory_usage()
///
172M+
172M+
```



---

Comment by jvoight created at 2008-02-29 20:04:34

I followed Will's advice to fix the memleak.  Please review--it worked for me.  JV


---

Attachment


---

Comment by cremona created at 2008-03-02 17:39:35

The patch looks ok to me.


---

Comment by mabshoff created at 2008-03-02 18:03:02

Resolution: fixed


---

Comment by mabshoff created at 2008-03-02 18:03:02

Merged in Sage 2.10.3.rc1. This patch is a work around and William, Travis, Gary, Josh and various other people have tracked the issue down, so there will be a new ticket about this.

Cheers,

Michael
