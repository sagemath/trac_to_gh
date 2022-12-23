# Issue 9957: Upgrade python to 2.7

Issue created by migration from https://trac.sagemath.org/ticket/9958

Original creator: mhampton

Original creation time: 2010-09-20 20:01:06

Assignee: tbd

CC:  jhpalmieri leif jason kcrisman kini

From the release notes:

Python 2.7 was released on July 3rd, 2010.

Python 2.7 is scheduled to be the last major version in the 2.x series before it moves into an extended maintenance period. This release contains many of the features that were first released in Python 3.1. Improvements in this release include:

    * An ordered dictionary type
    * New unittest features including test skipping, new assert methods, and test discovery
    * A much faster io module
    * Automatic numbering of fields in the str.format() method
    * Float repr improvements backported from 3.x
    * Tile support for Tkinter
    * A backport of the memoryview object from 3.x
    * Set literals
    * Set and dictionary comprehensions
    * Dictionary views
    * New syntax for nested with statements
    * The sysconfig module


---

Comment by mhampton created at 2010-09-20 20:09:34

First attempt is at:
[http://sage.math.washington.edu/home/palmieri/SPKG/python-2.7.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/python-2.7.p0.spkg)

John (jhpalmieri) reports that this builds but Sage does not on sage.math, and "packages for
twisted, zodb, pygments, and numpy don't build correctly."

Apparently the fix for [http://bugs.python.org/issue7491](http://bugs.python.org/issue7491) causes some of these problems.

On the numpy/scipy lists Ralf Gommers says "Numpy 1.5 should work with Python 2.7 and 3.1 and not be too far off. In August hopefully". 

So it looks like [http://trac.sagemath.org/sage_trac/ticket/9808](http://trac.sagemath.org/sage_trac/ticket/9808) should fix the numpy issues.


---

Comment by jhpalmieri created at 2010-09-20 20:17:18

Changing component from PLEASE CHANGE to packages.


---

Comment by leif created at 2010-09-24 12:28:07

Changing type from defect to enhancement.


---

Comment by fbissey created at 2010-10-04 00:03:27

Replying to [comment:1 mhampton]:
> First attempt is at:
> [http://sage.math.washington.edu/home/palmieri/SPKG/python-2.7.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/python-2.7.p0.spkg)
> 
> John (jhpalmieri) reports that this builds but Sage does not on sage.math, and "packages for
> twisted, zodb, pygments, and numpy don't build correctly."
> 
> Apparently the fix for [http://bugs.python.org/issue7491](http://bugs.python.org/issue7491) causes some of these problems.

This fix has been included in python-2.6.5 onwards. We are using 2.6.5 which includes this fix and everything builds (haven't tried 2.7 yet). The only problem we have is with [http://github.com/cschwan/sage-on-gentoo/issues#issue/1](http://github.com/cschwan/sage-on-gentoo/issues#issue/1) so I think it is unfair to single out this issue as the source of problems.


---

Comment by novoselt created at 2011-02-27 21:19:50

Is there still any interest in this upgrade? I wanted to use ordered dictionaries, which require 2.7. Unfortunately, active participation in this ticket is beyond my current capabilities...


---

Comment by fbissey created at 2011-02-27 21:27:59

It will happen at least in sage-on-gentoo as we are following the system python.
I have a couple of things in our tree to fix problems with python-2.6.5 and 2.6.6
we are looking into 2.7 now. I should post any patch to have it working here.

We are not talking about using the new capabilities just porting, I imagine my
counterpart in Mandriva does the same.


---

Comment by fbissey created at 2011-02-28 09:30:05

I just attached a patch that is needed for python 2.6.5 and later.


---

Comment by fbissey created at 2011-02-28 09:30:05

Changing status from new to needs_work.


---

Comment by fbissey created at 2011-03-11 03:44:37

Build sage-4.6.2 (and dependency) against python-2.7.1 on OS X. I get a lot of the following

```
Expected nothing
Got:
    Failure in _test_pickling:
    Traceback (most recent call last):
      File "/Users/frb15/Desktop/Gentoo/usr/lib/python2.7/site-packages/sage/misc/sage_unittest.py", line 275, in run
        test_method(tester = tester)
      File "/Users/frb15/Desktop/Gentoo/usr/lib/python2.7/site-packages/sage/misc/sage_unittest.py", line 498, in _test_pickling
        tester.assertEqual(loads(dumps(self._instance)), self._instance)
      File "/Users/frb15/Desktop/Gentoo/usr/lib/python2.7/unittest/case.py", line 493, in assertEqual
        assertion_func = self._getAssertEqualityFunc(first, second)
      File "/Users/frb15/Desktop/Gentoo/usr/lib/python2.7/unittest/case.py", line 476, in _getAssertEqualityFunc
        asserter = self._type_equality_funcs.get(type(first))
    AttributeError: 'InstanceTester' object has no attribute '_type_equality_funcs'
    ------------------------------------------------------------
```

I patched python with the cpickle patch. Any ideas?


---

Comment by fbissey created at 2011-03-11 03:48:39

A lot of "doctest... DeprecationWarning: ..." lines that were expected are just gone. Which fails the test.


---

Comment by fbissey created at 2011-03-11 03:50:36

Lots of numerical and a little bit of formatting noise.


---

Comment by fbissey created at 2011-03-27 03:47:53

Ok so now I understand the differences between unittest and unittest2 which is shipped with python-2.7. This will require a massive number of non-backward compatible changes. I am starting to experiment with a few sage components but that promise to be long and boring.


---

Comment by fbissey created at 2011-04-08 02:41:11

I have attached a log of sage -testall. This is a sage-on-gentoo install a few tests are expected to fail [https://github.com/cschwan/sage-on-gentoo/wiki/Known-test-failures](https://github.com/cschwan/sage-on-gentoo/wiki/Known-test-failures) but it should give you an idea of the problems we face.


---

Comment by fbissey created at 2011-04-14 09:21:16

I attached a log of test failures with 4.7.alpha4 (+ #7377). It is mostly number of decimals and messages. I added PYTHONWARNINGS=default to sage-env so I collected extra messages. The most important one being the deprecations of "sets".

There are 3 tests killed reason currently unknown. And a few that may need special attention.


---

Comment by fbissey created at 2011-04-14 23:27:53

A little bit more details, these are curious:

```
sage -t -long  -force_lib devel/sage-main/sage/rings/padics/padic_capped_relative_element.pyx
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/rings/padics/padic_capped_relative_element.pyx", line 2297:
    sage: hash(R(-1)) 
Expected:
    95367431640624
Got:
    1977800240
```



```
sage -t -long  -force_lib devel/sage-main/sage/combinat/words/suffix_trees.py
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/combinat/words/suffix_trees.py", line 1345:
    sage: t.trie_type_dict() == dict([[(0, W("a")), 4], [(0, W("b")), 3], [(3, W("a")), 2], [(4, W("b")), 5], [(5, W("a")), 1]])
Expected:
    True
Got:
    False
**********************************************************************
sage -t -long  -force_lib devel/sage-main/sage/combinat/words/suffix_trees.py
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/combinat/words/suffix_trees.py", line 1345:
    sage: t.trie_type_dict() == dict([[(0, W("a")), 4], [(0, W("b")), 3], [(3, W("a")), 2], [(4, W("b")), 5], [(5, W("a")), 1]])
Expected:
    True
Got:
    False
**********************************************************************
```

This one doesn't worry me as much but should be looked at

```
sage -t -long  -force_lib devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py", line 22:
    sage: it.next()
Expected:
    word: 5645
Got:
    word: 4564
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py", line 24:
    sage: it.next()
Expected:
    word: 4564
Got:
    word: 5645
**********************************************************************
```



```
sage -t -long  -force_lib devel/sage-main/sage/structure/parent.pyx
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/structure/parent.pyx", line 634:
    sage: CCls()._test_eq()
Expected:
    Traceback (most recent call last):
    ...
    AssertionError: <class '__main__.CCls'> == None
Got nothing
```


The following were killed:

```
sage -t -long  -force_lib devel/sage-main/sage/rings/homset.py # Killed/crashed
sage -t -long  -force_lib devel/sage-main/sage/schemes/generic/scheme.py # Killed/crashed
```

In my original run 

```
sage -t -long -force_lib "devel/sage-main/sage/rings/morphism.pyx"
```

also got killed but not in a subsequent run after I adopted a small change in sage-doctest to get rid of PYTHONWARNINGS=default in sage-env.

Example of killed test:

```
sage -t -long -verbose -force_lib "devel/sage-main/sage/rings/homset.py"
...

Trying:
    phi = S.hom([b,a])###line 141:_sage_    >>> phi = S.hom([b,a])
Expecting nothing
ok
Trying:
    phi == loads(dumps(phi))###line 142:_sage_    >>> phi == loads(dumps(phi))
Expecting:
    True
/usr/lib64/libcsage.so(print_backtrace+0x24)[0x7f83de940534]
/usr/lib64/libcsage.so(sigdie+0x1d)[0x7f83de9405cd]
/usr/lib64/libcsage.so(sage_signal_handler+0x131)[0x7f83de940741]
/lib64/libpthread.so.0(+0xfae0)[0x7f83e2385ae0]
/usr/lib64/libsingular.so.3(_Z9id_DeletePP10sip_sidealP9sip_sring+0x53)[0x7f83c5c48383]
/usr/lib64/python2.7/site-packages/sage/libs/singular/groebner_strategy.so(+0x388d)[0x7f83ad27488d]
/usr/lib64/libpython2.7.so.1.0(PyDict_Clear+0xfc)[0x7f83e261597c]
/usr/lib64/libpython2.7.so.1.0(+0x82a09)[0x7f83e2615a09]
/usr/lib64/libpython2.7.so.1.0(+0x112e7e)[0x7f83e26a5e7e]
/usr/lib64/libpython2.7.so.1.0(_PyObject_GC_Malloc+0x11c)[0x7f83e26a684c]
/usr/lib64/libpython2.7.so.1.0(_PyObject_GC_New+0xd)[0x7f83e26a685d]
/usr/lib64/libpython2.7.so.1.0(+0x7fe11)[0x7f83e2612e11]
/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]
/usr/lib64/python2.7/site-packages/sage/rings/polynomial/polydict.so(+0x168c3)[0x7f83c8f378c3]
/usr/lib64/libpython2.7.so.1.0(+0xa0468)[0x7f83e2633468]
/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]
/usr/lib64/python2.7/site-packages/sage/rings/polynomial/polydict.so(+0xa451)[0x7f83c8f2b451]
/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]
/usr/lib64/libpython2.7.so.1.0(PyEval_CallObjectWithKeywords+0x47)[0x7f83e2670ca7]
/usr/lib64/python2.7/lib-dynload/cPickle.so(+0x5f06)[0x7f83dcb2df06]
/usr/lib64/python2.7/lib-dynload/cPickle.so(+0xaf47)[0x7f83dcb32f47]
/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]
/usr/lib64/python2.7/site-packages/sage/structure/sage_object.so(+0x152fc)[0x7f83dc7012fc]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x56bc)[0x7f83e267692c]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCode+0x32)[0x7f83e26782f2]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x5a78)[0x7f83e2676ce8]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]
/usr/lib64/libpython2.7.so.1.0(+0x71282)[0x7f83e2604282]
/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]
/usr/lib64/libpython2.7.so.1.0(+0x5a24f)[0x7f83e25ed24f]
/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x491d)[0x7f83e2675b8d]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x522e)[0x7f83e267649e]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]
/usr/lib64/libpython2.7.so.1.0(+0x71282)[0x7f83e2604282]
/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]
/usr/lib64/libpython2.7.so.1.0(+0x5a24f)[0x7f83e25ed24f]
/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x491d)[0x7f83e2675b8d]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x522e)[0x7f83e267649e]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]
/usr/lib64/libpython2.7.so.1.0(+0x7138b)[0x7f83e260438b]
/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]
/usr/lib64/libpython2.7.so.1.0(+0x5a24f)[0x7f83e25ed24f]
/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x491d)[0x7f83e2675b8d]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x522e)[0x7f83e267649e]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x522e)[0x7f83e267649e]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x522e)[0x7f83e267649e]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCode+0x32)[0x7f83e26782f2]
/usr/lib64/libpython2.7.so.1.0(+0xff25c)[0x7f83e269225c]
/usr/lib64/libpython2.7.so.1.0(PyRun_FileExFlags+0x90)[0x7f83e2693090]
/usr/lib64/libpython2.7.so.1.0(PyRun_SimpleFileExFlags+0x1ff)[0x7f83e2693c6f]
/usr/lib64/libpython2.7.so.1.0(Py_Main+0xb53)[0x7f83e26a4fc3]
/lib64/libc.so.6(__libc_start_main+0xfd)[0x7f83e201cb6d]
/usr/bin/python2.7[0x4008a9]

------------------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occurred in Sage.
This probably occurred because a *compiled* component of Sage has a bug
in it and is not properly wrapped with sig_on(), sig_off(). You might
want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate.
------------------------------------------------------------------------
The doctested process was killed by signal 11
         [2.5 s]
```



---

Comment by fbissey created at 2011-04-15 00:10:53

small patch to sage-doctest in sage_script to reenable sage's deprecation warnings. Idea by my friend Steve Trogdon.


---

Attachment

this form of comparison is removed in python 2.6.5 and later, refreshed using --git.


---

Comment by fbissey created at 2011-04-15 02:42:22

It looks like the crash problems originates somewhere in libsingular

```
sage: f = Zmod(6).cover()
sage: f.kernel()
Principal ideal (6) of Integer Ring
sage: R.<x,y> = PolynomialRing(QQ, 2)
sage: S.<a,b> = R.quo(x^2 + y^2)
sage: phi = S.cover()
sage: phi == loads(dumps(phi))
True
sage: phi == R.quo(x^2 + y^3).cover()

Program received signal SIGSEGV, Segmentation fault.
id_Delete (h=0x50687d8, r=0x0) at ideals.cc:127
127     ideals.cc: No such file or directory.
        in ideals.cc
(gdb) bt
#0  id_Delete (h=0x50687d8, r=0x0) at ideals.cc:127
#1  0x00007fffb9670b49 in __pyx_pf_4sage_4libs_8singular_17groebner_strategy_16GroebnerStrategy_1__dealloc__ (
    o=<value optimized out>) at sage/libs/singular/groebner_strategy.cpp:2570
#2  __pyx_tp_dealloc_4sage_4libs_8singular_17groebner_strategy_GroebnerStrategy (o=<value optimized out>)
    at sage/libs/singular/groebner_strategy.cpp:3190
#3  0x00007ffff7aa98c7 in PyDict_Clear (op=<value optimized out>) at Objects/dictobject.c:891
#4  0x00007ffff7aa990f in dict_tp_clear (op=<value optimized out>) at Objects/dictobject.c:2088
#5  0x00007ffff7b32f27 in delete_garbage (generation=0) at Modules/gcmodule.c:769
#6  collect (generation=0) at Modules/gcmodule.c:930
#7  0x00007ffff7b33616 in collect_generations (basicsize=<value optimized out>) at Modules/gcmodule.c:996
#8  _PyObject_GC_Malloc (basicsize=<value optimized out>) at Modules/gcmodule.c:1457
#9  0x00007ffff7ac4a96 in PyType_GenericAlloc (type=0x7ffff7d9ad40, nitems=0) at Objects/typeobject.c:744
#10 0x00007ffff7a8d256 in BaseException_new (type=<value optimized out>, args=<value optimized out>, kwds=<value optimized out>)
    at Objects/exceptions.c:34
#11 0x00007ffff7ac57b5 in type_call (type=0x7ffff7d9ad40, args=0x4ae46d0, kwds=0x0) at Objects/typeobject.c:712
#12 0x00007ffff7a77539 in PyObject_Call (func=0x7ffff7d9ad40, arg=0x4ae46d0, kw=0x0) at Objects/abstract.c:2529
#13 0x00007ffff7b00b45 in PyEval_CallObjectWithKeywords (func=0x7ffff7d9ad40, arg=0x4ae46d0, kw=0x0) at Python/ceval.c:3881
#14 0x00007ffff7b10443 in PyErr_NormalizeException (exc=0x7fffffffa778, val=0x7fffffffa770, tb=0x7fffffffa768)
    at Python/errors.c:190
#15 0x00007fffe433021c in __Pyx_GetException (type=0x7fffffffa7c0, value=0x7fffffffa7b8, tb=0x7fffffffa7c8)
    at sage/structure/parent.c:20909
#16 0x00007fffe433e4d1 in __pyx_pf_4sage_9structure_6parent_6Parent_2element_class (__pyx_v_self=0x4aea500, 
    unused=<value optimized out>) at sage/structure/parent.c:4251
#17 0x00007ffff7aac1e2 in PyCFunction_Call (func=0x504ebd8, arg=0x7ffff7f81050, kw=<value optimized out>)
    at Objects/methodobject.c:90
#18 0x00007ffff7a77539 in PyObject_Call (func=0x504ebd8, arg=0x7ffff7f81050, kw=0x0) at Objects/abstract.c:2529
#19 0x00007ffff7b00b45 in PyEval_CallObjectWithKeywords (func=0x504ebd8, arg=0x7ffff7f81050, kw=0x0) at Python/ceval.c:3881
#20 0x00007ffff7a8b51f in methoddescr_call (descr=<value optimized out>, args=0x7ffff7f81050, kwds=0x0)
    at Objects/descrobject.c:246
#21 0x00007ffff7a77539 in PyObject_Call (func=0x138e950, arg=0x7ffff7e9c050, kw=0x0) at Objects/abstract.c:2529
#22 0x00007ffff7b05efe in do_call (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:4230
#23 call_function (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:4035
#24 PyEval_EvalFrameEx (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:2665
#25 0x00007ffff7b07b65 in PyEval_EvalCodeEx (co=0x1159e30, globals=<value optimized out>, locals=<value optimized out>, 
    args=<value optimized out>, argcount=3, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:3252
#26 0x00007ffff7a99a97 in function_call (func=0x115d5f0, arg=0xfadeb0, kw=0x0) at Objects/funcobject.c:526
#27 0x00007ffff7a77539 in PyObject_Call (func=0x115d5f0, arg=0xfadeb0, kw=0x0) at Objects/abstract.c:2529
#28 0x00007ffff7a77cca in PyObject_CallFunctionObjArgs (callable=0x115d5f0) at Objects/abstract.c:2760
#29 0x00007ffff7ac8a8e in slot_tp_descr_get (self=0x13179d0, obj=0x4aea500, type=0x19e91f0) at Objects/typeobject.c:5621
#30 0x00007ffff7aae433 in _PyObject_GenericGetAttrWithDict (obj=0x4aea500, name=0x13c5a78, dict=0x5068fb0) at Objects/object.c:1432
#31 0x00007ffff7aae4d1 in PyObject_GenericGetAttr (obj=<value optimized out>, name=<value optimized out>) at Objects/object.c:1454
#32 0x00007fffe434ed62 in __pyx_tp_getattro_4sage_9structure_6parent_Parent (o=0x4aea500, n=0x13c5a78)
    at sage/structure/parent.c:18702
#33 0x00007ffff7aad8f4 in PyObject_GetAttr (v=0x4aea500, name=<value optimized out>) at Objects/object.c:1189
#34 0x00007ffff7afdbab in builtin_hasattr (self=<value optimized out>, args=<value optimized out>) at Python/bltinmodule.c:885
#35 0x00007ffff7aac1a0 in PyCFunction_Call (func=0x7ffff7fae3b0, arg=0x503d680, kw=<value optimized out>)
    at Objects/methodobject.c:81
#36 0x00007ffff7b05ba3 in call_function (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:4012
#37 PyEval_EvalFrameEx (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:2665
#38 0x00007ffff7b05cfa in fast_function (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:4098
#39 call_function (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:4033
#40 PyEval_EvalFrameEx (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:2665
#41 0x00007ffff7b07b65 in PyEval_EvalCodeEx (co=0x1159e30, globals=<value optimized out>, locals=<value optimized out>, 
    args=<value optimized out>, argcount=3, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:3252
#42 0x00007ffff7a99a97 in function_call (func=0x115d5f0, arg=0xfadbe0, kw=0x0) at Objects/funcobject.c:526

```



---

Comment by fbissey created at 2011-04-20 23:30:42

Same two doctests killed after upgrade to alpha5.


---

Comment by fbissey created at 2011-04-21 00:42:11

Over-eager garbage collection in python-2.7.1! Preceding the sequence by

```
sage: import gc
sage: gc.disable()
```

Makes everything go smoothly.


---

Comment by nthiery created at 2011-04-22 13:43:24

trac_9958-fix_cmp.patch is perfectly reasonable, since this is the idiom used everywhere else in similar situations. I don't have enough background to judge on the warning patch.


---

Comment by fbissey created at 2011-04-24 02:16:05

Put an updated list of tests failing with 4.7.alpha5 and the latest patches from Nicolas M. Thiery.
I think the next area do need some work is the problem of garbage collection in polynomial rings that leads to "random" failures in libsingular. See:
[http://groups.google.com/group/sage-devel/browse_thread/thread/8c165c887d6b9e54](http://groups.google.com/group/sage-devel/browse_thread/thread/8c165c887d6b9e54)


---

Comment by fbissey created at 2011-04-24 03:48:43

Split the deprecation issue in its own ticket in #11244 - this is a different patch.


---

Comment by fbissey created at 2011-04-27 01:59:47

Replying to [comment:23 nthiery]:
> trac_9958-fix_cmp.patch is perfectly reasonable, since this is the idiom used everywhere else in similar situations. I don't have enough background to judge on the warning patch.

I will put the cmp patch in its own ticket would you review it?


---

Attachment

fix numerical noise part 1


---

Attachment

fix numerical noise part 3


---

Comment by fbissey created at 2011-04-28 03:19:58

fix numerical noise part 4: the forgotten bits


---

Attachment

49 failures in colors.py, numerical noise except one.


---

Attachment

fix the element reported by list index


---

Comment by fbissey created at 2011-04-28 03:22:54

odds and ends missed in the other patches


---

Attachment

I have attached some patches to fix all the noise for numerics and formatting changes. What's left should be looked at before patching.

There are several failures because hashes have changed but I cannot say it is allright to just change the doctest:

```
sage -t -long -force_lib "devel/sage-main/sage/rings/padics/padic_capped_relative_element.pyx"
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/rings/padics/padic_capped_relative_element.pyx", line 2339:
    sage: hash(R(-1)) 
Expected:
    95367431640624
Got:
    1977800240
**********************************************************************
```



```
sage -t -long -force_lib "devel/sage-main/sage/rings/integer.pyx"
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/rings/integer.pyx", line 2995:
    sage: n = -920390823904823094890238490238484; n.__hash__()                                                                      
Expected:                                                                                                                           
    6874330978542788722                                                                                                             
Got:                                                                                                                                
    -2623069716                                                                                                                     
**********************************************************************                                                              
File "/usr/share/sage/devel/sage-main/sage/rings/integer.pyx", line 3010:                                                           
    sage: hash(n)                                                                                                                   
Expected:                                                                                                                           
    -9223372036854767616                                                                                                            
Got:                                                                                                                                
    8192                                                                                                                            
**********************************************************************                                                              
File "/usr/share/sage/devel/sage-main/sage/rings/integer.pyx", line 3013:                                                           
    sage: hash(n) == hash(int(n))                                                                                                   
Expected:                                                                                                                           
    True
Got:
    False
**********************************************************************
```

That hash(n) == hash(int(n)) is now false should be looked into carefully.

```
sage -t -long -force_lib "devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py"
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py", line 20:
    sage: it.next()
Expected:
    word: 6456
Got:
    word: 5645
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py", line 22:
    sage: it.next()
Expected:
    word: 5645
Got:
    word: 6456
**********************************************************************
```

I think that one is OK, just a change of order but a second opinion would be nice.

Finally there are still three tests killed in libsingular's id_delete because a ring has been garbage collected even so there are some precautions in place for it:
[http://groups.google.com/group/sage-devel/browse_thread/thread/8c165c887d6b9e54](http://groups.google.com/group/sage-devel/browse_thread/thread/8c165c887d6b9e54)

Next we need an updated python spkg so that more people can play and even try the patchbot on it.


---

Comment by fbissey created at 2011-04-28 03:48:54

The replacement of type.__cmp__ by cmp in strata.py is now in its own ticket #11264 as it can be applied independently of a python upgrade.


---

Comment by fbissey created at 2011-04-28 09:31:20

I forgot because I build on sage-on-gentoo but I'll post some patch to build against python-2.7 a little bit later.


---

Comment by fbissey created at 2011-05-02 23:37:47

Unless someone steps in I'll make a new python-2.7.1 spkg by the end of the week. I'll have to figure out if the latest change going in for sage-4.7 will be needed for that one.


---

Comment by fbissey created at 2011-05-05 22:32:05

I won't be able to do that this week.


---

Comment by fbissey created at 2011-05-16 21:47:11

Our lead sage-on-gentoo debugger Martin tracked down the segfault problem to cython, this is now #11339


---

Comment by kcrisman created at 2011-05-18 16:01:39

I'd like to try this but don't have time to figure out exactly what patches are needed in what order - can someone update the description with this?  Also, is it the same spkg that Marshall originally posted that one should try?


---

Comment by kcrisman created at 2011-05-18 16:24:58

Also, is it possible to test this by ./sage -f something, or would one have to take a fresh tarball and replace the Python spkg?


---

Comment by fbissey created at 2011-05-18 21:41:17

Replying to [comment:34 kcrisman]:
> Also, is it possible to test this by ./sage -f something, or would one have to take a fresh tarball and replace the Python spkg?

Hi Karl,

I am mainly developing from sage-on-gentoo at the moment. I need to make a current python-2.7.1 spkg to match. I will update the description and give the patch order when there is a spkg (feel free to make one). The patch have initially been made against 4.7.1.alpha0 and the current version works against 4.7.1.alpha1. You would get failures against a 4.7 because #7377 finally landed.

I think the best course of action will be to start from scratch, it may even be useful to host an alternative tarball somewhere because the change in python version will be extremely messy. I don't know if we can do it without breaking sage -upgrade or being overly complicated.

In the meantime you could have a look at #11244 (which I need to update for 4.7.1.alpha1 because of #10334). 

Francois


---

Comment by fbissey created at 2011-05-18 23:29:46

OK if you want to look at #11244 it can be tested against either the latest 4.7 or 4.7.1.alpha1 now.


---

Comment by kcrisman created at 2011-05-19 00:33:11

I see.  Well, I just want to make sure that it all works fine on older Macs, of course.  I definitely don't have time to make an spkg now, though I do have time to do ./sage -f and slap a few patches on it :)  Just let me know when you get around to it; I don't think there is a huge rush.

I should probably test 4.7.1.alpha1 on my box.  I'm amazed at Jeroen's stamina on this, especially with several different versions simultaneously existing.


---

Comment by fbissey created at 2011-05-19 00:49:57

Replying to [comment:37 kcrisman]:
> I see.  Well, I just want to make sure that it all works fine on older Macs, of course.  I definitely don't have time to make an spkg now, though I do have time to do ./sage -f and slap a few patches on it :)  Just let me know when you get around to it; I don't think there is a huge rush.
> 
> I should probably test 4.7.1.alpha1 on my box.  I'm amazed at Jeroen's stamina on this, especially with several different versions simultaneously existing.

That's why I asked about #11244 it is an issue I split from this ticket because it should apply on a sage running python-2.6 without side effects. So it could be in place when we come around to the upgrade. Any ideas on #11339 which was recently split from this ticket is also welcome.


---

Comment by fbissey created at 2011-05-20 20:49:09

My friend Steven Trogdon made some quick and dirty spkgs. His early tests indicate that setuptools needs to be updated. This is now #11363 it also revealed that I missed something in misc/cython.py watch out for an updated patch sometimes this weekend.
There were also a few things that needed to be done in two other patches which I refreshed yesterday.
I have a python-2.7.1 spkg ready to be uploaded probably sometimes today.
If you want fun before that you can always use Steve's spkg (they are not in a reviewable state) at:
[http://www.d.umn.edu/~strogdon/sage/](http://www.d.umn.edu/~strogdon/sage/)


---

Comment by fbissey created at 2011-05-20 21:09:43

Didn't take long. I have been naughty and committed two changes to patches that needed touching after my first commit of python-2.7.1 so the log will show 3 entries for just the one SPKG.txt entry. They were minor changes.
I dropped a number of patches because they were applied upstream. However in the case of two patches I dropped them because the upstream has changed in a way they don't apply anymore but I don't know if patching is still necessary for the underlying issues. If so new patches will need to be developed. The issues are
 * readline on itanium
 * multiprocessing on solaris

As promised I will give a patch order. The next to last one needs updating as stated earlier and the last one is really optional. The patches do not have to be taken n that order as they don't overlap.


---

Comment by fbissey created at 2011-05-20 21:11:26

I forgot apply the patches on 4.7.1.alpha1, there may be rejection on 4.7.rcX.


---

Comment by fbissey created at 2011-05-21 12:23:43

misc/cython.py patch updated for people who want to test it.


---

Comment by fbissey created at 2011-05-21 19:45:40

corrected a syntax error in the last patch.


---

Comment by fbissey created at 2011-05-22 12:32:34

Not strictly necessary but this file needed a scrub. (refreshed for syntax errors)


---

Attachment

Had to redo trac_9958-build_module_listpy.patch again as I messed up the syntax of one bit.


---

Comment by fbissey created at 2011-05-22 18:44:32

My friend Steve Trogdon made a prepatched sage-4.7.1.alpha1 spkg (4.7.1.alpha1.p0 we named it) available to make testing easier, find it with hos own test.log here
[http://www.d.umn.edu/~strogdon/sage/](http://www.d.umn.edu/~strogdon/sage/)
It has all the necessary patches from #11244 and this this ticket.
We are a bit puzzled by the cause of failure in sage/misc/cython.py, white spaces?


---

Comment by kcrisman created at 2011-05-23 12:54:59

I am getting the twisted install fail that jhpalmieri refers to.  So my guess is that the Gentoo system has some updated things along those lines that vanilla 4.7.1.alpha1 does not.  Is that possible?


---

Comment by fbissey created at 2011-05-23 13:59:36

Replying to [comment:46 kcrisman]:
> I am getting the twisted install fail that jhpalmieri refers to.  So my guess is that the Gentoo system has some updated things along those lines that vanilla 4.7.1.alpha1 does not.  Is that possible?

Well sage-on-gentoo uses a newer twisted. On the other I and Steve have build twisted in vanilla sage with python-2.7.1. Did you get the new setuptools spkg from #11363? It is necessary to build twisted with python-2.7.1.


---

Comment by kcrisman created at 2011-05-23 15:01:49

No, I didn't realize there was an spkg involved with that.  I installed that first, and it seems to be working now.


---

Comment by kcrisman created at 2011-05-23 19:51:48

Replying to [comment:45 fbissey]:
> My friend Steve Trogdon made a prepatched sage-4.7.1.alpha1 spkg (4.7.1.alpha1.p0 we named it) available to make testing easier, find it with hos own test.log here
> [http://www.d.umn.edu/~strogdon/sage/](http://www.d.umn.edu/~strogdon/sage/)
> It has all the necessary patches from #11244 and this this ticket.

Is one of these patches needed _before_ doing the Sage spkg itself? I get an immediate failure

```
gcc -o src/convert.os -c -fPIC -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include/python2.6 -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include/NTL -Iinclude src/convert.c
In file included from include/memory.h:23,
                 from /Users/student/Desktop/sage-4.7.1.alpha1/local/include/pari/pari.h:42,
                 from include/convert.h:12,
                 from src/convert.c:14:
include/interrupt.h:32:20: error: Python.h: No such file or directory
scons: *** [src/convert.os] Error 1
*** TOUCHING ALL CYTHON (.pyx) FILES ***
gcc -o src/convert.os -c -fPIC -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include/python2.6 -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include/NTL -Iinclude src/convert.c
In file included from include/memory.h:23,
                 from /Users/student/Desktop/sage-4.7.1.alpha1/local/include/pari/pari.h:42,
                 from include/convert.h:12,
                 from src/convert.c:14:
include/interrupt.h:32:20: error: Python.h: No such file or directory
scons: *** [src/convert.os] Error 1

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
gcc -o src/convert.os -c -fPIC -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include/python2.6 -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include/NTL -Iinclude src/convert.c
In file included from include/memory.h:23,
                 from /Users/student/Desktop/sage-4.7.1.alpha1/local/include/pari/pari.h:42,
                 from include/convert.h:12,
                 from src/convert.c:14:
include/interrupt.h:32:20: error: Python.h: No such file or directory
scons: *** [src/convert.os] Error 1
ERROR: There was an error building c_lib.
```

which I assume is related to one of the patches involved here, though I couldn't say which one...


---

Comment by fbissey created at 2011-05-23 20:04:42

Did you rebuild cython after the python upgrade? In fact I have now added a list of package that needs to be rebuild after the python upgrade. Not all of them are necessary for building sage (scipy could be done after) but cython, numpy, matplotlib and pynac really need to be rebuilt.

Once you have done that apply all the patches with build in their names:
 * [attachment:trac_9958-build_setuppy.patch]
 * [attachment:trac_9958-build-sage_clib.patch]
 * [attachment:trac_9958-build_misc_cythonpy.patch]
 * [attachment:trac_9958-build_module_listpy.patch] (actually optional)

That should help sage build but will not correct many of the doctests. To fix most of the doctests apply the patches in #11244 as well as the one in the description of this bug. I have made a list now, have you seen it?


---

Comment by kcrisman created at 2011-05-23 20:17:06

Well, I'm building from scratch, so that shouldn't affect it from that side.  

Are you saying that before I build the Sage library, I have to apply these patches?  That's a little tricky in a scratch build (for me, at least). 

Yes, I saw the lists, but I thought they were only relevant for an upgrade/after actually building Sage.  My apologies.  I may not be able to finish testing this properly for a while now.


---

Comment by fbissey created at 2011-05-23 20:24:03

Replying to [comment:52 kcrisman]:
> Well, I'm building from scratch, so that shouldn't affect it from that side.  
> 
> Are you saying that before I build the Sage library, I have to apply these patches?  That's a little tricky in a scratch build (for me, at least). 
> 
> Yes, I saw the lists, but I thought they were only relevant for an upgrade/after actually building Sage.  My apologies.  I may not be able to finish testing this properly for a while now.

That's all right there are still things to sort out. But you could use the sage spkg prepared by Steve with all patches included rather than patch yourself:
[http://www.d.umn.edu/~strogdon/sage/sage-4.7.1.alpha1.p0.spkg](http://www.d.umn.edu/~strogdon/sage/sage-4.7.1.alpha1.p0.spkg)

And yes it is tricky from scratch unless you have a premade spkg.


---

Comment by jhpalmieri created at 2011-05-24 01:01:47

I may have made mistakes, but I tried to do this, starting with sage-4.7.rc4:

 - install the new python spkg
 - install the new setuptools spkg (from #11363)
 - apply the patches from #11244 to the main Sage library
 - apply the patches from this ticket with "build" in their name -- some of these didn't apply cleanly, so I had to work around that.

I used that to build a new version of Sage (using "sage -sdist ...").  The tar file is here:

 - [http://sage.math.washington.edu/home/palmieri/misc/python2.7/sage-4.7.rc4-python2.7.tar](http://sage.math.washington.edu/home/palmieri/misc/python2.7/sage-4.7.rc4-python2.7.tar)

On sage.math, I've been able to untar this and build Sage, although tests haven't run yet.  You can also try upgrading, although I haven't tested this at all: run


```
$ sage -upgrade http://sage.math.washington.edu/home/palmieri/misc/python2.7/sage-4.7.rc4-python2.7/
```



---

Comment by fbissey created at 2011-05-24 02:13:19

Replying to [comment:54 jhpalmieri]:
> I may have made mistakes, but I tried to do this, starting with sage-4.7.rc4:
> 
>  - install the new python spkg
>  - install the new setuptools spkg (from #11363)
>  - apply the patches from #11244 to the main Sage library
>  - apply the patches from this ticket with "build" in their name -- some of these didn't apply cleanly, so I had to work around that.
> 
> I used that to build a new version of Sage (using "sage -sdist ...").  The tar file is here:
> 
>  - [http://sage.math.washington.edu/home/palmieri/misc/python2.7/sage-4.7.rc4-python2.7.tar](http://sage.math.washington.edu/home/palmieri/misc/python2.7/sage-4.7.rc4-python2.7.tar)
> 
> On sage.math, I've been able to untar this and build Sage, although tests haven't run yet.  You can also try upgrading, although I haven't tested this at all: run
> 
> {{{
> $ sage -upgrade http://sage.math.washington.edu/home/palmieri/misc/python2.7/sage-4.7.rc4-python2.7/
> }}}

I have tried to keep abreast of everything so the patches are based on 4.7.1.alpha1 there are enough differences that a lot of patches for 4.7 would need rebasing.

So I decided to go straight for the bleeding edge. I am doing some more work on the "build" patches, I am trying to do something smarter with the python version number so some change could be applied independently of this ticket. The module_list,py patch definitely won't apply cleanly on 4.7.rc mainly because of #10334. What's more #11264 and #11236 which are needed here are merged in 4.7.1.alpha0.

That's all a bit of hassle to start from 4.7.1.alpha, but I would have to start again if I was starting from 4.7.rc.


---

Comment by fbissey created at 2011-05-24 03:31:06

let's not forget the hardcoded version of python in SConstruct for sage_clib


---

Attachment

I have updated trac_9958-build-sage_clib.patch it could now be splited in its own ticket. It enables sage-clib to be smarter about the python version used. It would figure it on its own. I am looking at doing the same for setup.py, anyone would review that in its own ticket? Once in, we could at least build sage against python2.6 or 2.7 without changes.


---

Comment by fbissey created at 2011-05-24 03:44:43

change needed in setup.py made it python version smart. I also scrubbed the debian stuff


---

Attachment

OK I also made setup.py python version smart any volunteer to review a separate ticket?


---

Comment by kcrisman created at 2011-05-24 12:50:05


```
g++ -o libcsage.dylib -single_module -flat_namespace -undefined dynamic_lookup -dynamiclib src/convert.os src/interrupt.os src/memory.os src/mpn_pylong.os src/mpz_pylong.os src/mpz_longlong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os -L/Users/student/Desktop/sage-4.7.1.alpha1/local/lib -L/Users/student/Desktop/sage-4.7.1.alpha1/local/lib/python/config -lntl -lpari -lgmp -lpython2.7
Traceback (most recent call last):
  File "setup.py", line 18, in <module>
    from module_list import ext_modules
  File "/Users/student/Desktop/sage-4.7.1.alpha1/devel/sage-main/module_list.py", line 1529, in <module>
    flint_depends],
TypeError: cannot concatenate 'str' and 'list' objects
sage: There was an error installing modified sage library code.


real    0m34.577s
user    0m19.519s
sys     0m6.901s
Error building new version of SAGE.
You might try typing 'sage -ba' or write to sage-support with as much information as possible.

real    2m42.066s
user    0m52.903s
sys     0m25.133s
sage: An error occurred while installing sage-4.7.1.alpha1.p0
```

Note this is the p0 package referred to above.


---

Comment by strogdon created at 2011-05-24 14:15:56

Well, there was a problem with this but it was corrected. I've checked the present sage-4.7.1.alpha.p0 and this problem should not be there. The md5sum (md5sum sage-4.7.1.alpha1.p0.spkg) should be 

b54da7bee966eaf15942964a05a8b6b1  sage-4.7.1.alpha1.p0.spkg

If the spkg you have is not this could you download again and see if that fixed things.


---

Attachment

Some minor changes. The biggest change is to the doctest which explicitly refereed to python2.6 also we have extra include folders in a doctest apparently. [updated 20110525]


---

Comment by fbissey created at 2011-05-25 01:33:22

I am splitting the ticket again: in #11376 we make sage building system smart and work out the python version by itself. If we get this in the next alpha that will make testing easier as you won't need a patched sage spkg to build against python-2.7.1. One will still need to patch the doctests afterwards and any other issues but it will build.

In #11377 I put the clean up of module_list.py this is not necessary for python-2.7.1 per see but it would be a huge favour to me if it was going in (it makes work on sage-on-gentoo and sage-prefix much easier).


---

Comment by kcrisman created at 2011-06-01 16:02:29

Replying to [comment:59 strogdon]:
> Well, there was a problem with this but it was corrected. I've checked the present sage-4.7.1.alpha.p0 and this problem should not be there. The md5sum (md5sum sage-4.7.1.alpha1.p0.spkg) should be 
> 
> b54da7bee966eaf15942964a05a8b6b1  sage-4.7.1.alpha1.p0.spkg
> 
> If the spkg you have is not this could you download again and see if that fixed things.

It didn't seem to fix things (and I did check the md5 sum).  I'm now starting a build from scratch, having replaced the python and sage spkgs.  

By the way, now that 4.7.1.alpha1 is "official", one may have to upgrade the drop-in spkg.


---

Comment by strogdon created at 2011-06-01 17:59:01

Replying to [comment:61 kcrisman]:

> Replying to [comment:59 strogdon]:
> > Well, there was a problem with this but it was corrected. I've checked the present sage-4.7.1.alpha.p0 and this problem should not be there. The md5sum (md5sum sage-4.7.1.alpha1.p0.spkg) should be  b54da7bee966eaf15942964a05a8b6b1  sage-4.7.1.alpha1.p0.spkg If the spkg you have is not this could you download again and see if that fixed things.
> It didn't seem to fix things (and I did check the md5 sum).  I'm now starting a build from scratch, having replaced the python and sage spkgs.   By the way, now that 4.7.1.alpha1 is "official", one may have to upgrade the drop-in spkg.

OK, for those interested I have a new drop-in spkg based on the released 4.7.1.alpha1. This spkg includes the patches from this ticket as well as the patches from tickets #11244, #11373, #11376 and #11377 . I'm presently building Sage to make sure everything is as it should be. If successful, I'll post links to the drop-in spkg later today.


---

Comment by fbissey created at 2011-06-01 19:18:07

I was hoping that #11376 and #11363 would have made it in alpha2 which would have made things easier. But I think Jeroen has closed alpha2 and is starting on alpha3. We should try to have at least these two in 4.7.1 to make testing easier.


---

Comment by strogdon created at 2011-06-01 20:44:27

The following have been uploaded:

http://www.d.umn.edu/~strogdon/sage/install.log-4.7.1.alpha1

http://www.d.umn.edu/~strogdon/sage/test.log-4.7.1.alpha1

http://www.d.umn.edu/~strogdon/sage/sage-4.7.1.alpha1.p0.spkg

http://www.d.umn.edu/~strogdon/sage/sage-4.7.1.alpha1.p0.spkg.md5

for comparisons, perhaps just under the wire for alpha2. Note, the drop-in sage spkg has the same revision .p0 extension, so I've provided the md5 sum for the spkg.


---

Comment by fbissey created at 2011-06-02 00:41:01

Changed the cython.py patch in the list to accommodate new changes made in #11376.


---

Comment by kcrisman created at 2011-06-06 15:11:46

End of a looong traceback while building from scratch on PPC 10.4 with the spkgs dropped in (though not the absolute most recent alpha1.p0 spkg, but that hasn't even been gotten to yet, so it shouldn't matter).  Just FYI in case that helps.

```
  File "/Users/student/Desktop/sage-4.7.1.alpha1-python/local/lib/python/os.py", line 284, in walk
    if isdir(join(top, name)):
  File "/Users/student/Desktop/sage-4.7.1.alpha1-python/local/lib/python/genericpath.py", line 44, in isdir
    return stat.S_ISDIR(st.st_mode)
  File "/Users/student/Desktop/sage-4.7.1.alpha1-python/local/lib/python/stat.py", line 41, in S_ISDIR
    return S_IFMT(mode) == S_IFDIR
RuntimeError: maximum recursion depth exceeded
Error installing Zope/Twisted interface.

real    0m16.055s
user    0m3.349s
sys     0m4.671s
sage: An error occurred while installing twisted-9.0.p2
```



---

Comment by fbissey created at 2011-06-06 19:38:59

Replying to [comment:66 kcrisman]:
> End of a looong traceback while building from scratch on PPC 10.4 with the spkgs dropped in (though not the absolute most recent alpha1.p0 spkg, but that hasn't even been gotten to yet, so it shouldn't matter).  Just FYI in case that helps.
> {{{
>   File "/Users/student/Desktop/sage-4.7.1.alpha1-python/local/lib/python/os.py", line 284, in walk
>     if isdir(join(top, name)):
>   File "/Users/student/Desktop/sage-4.7.1.alpha1-python/local/lib/python/genericpath.py", line 44, in isdir
>     return stat.S_ISDIR(st.st_mode)
>   File "/Users/student/Desktop/sage-4.7.1.alpha1-python/local/lib/python/stat.py", line 41, in S_ISDIR
>     return S_IFMT(mode) == S_IFDIR
> RuntimeError: maximum recursion depth exceeded
> Error installing Zope/Twisted interface.
> 
> real    0m16.055s
> user    0m3.349s
> sys     0m4.671s
> sage: An error occurred while installing twisted-9.0.p2
> }}}

Were you using the new setuptools from #11363? If so it may be worth trying a newer twisted from #8741.


---

Comment by fbissey created at 2011-06-14 13:33:36

fix doctest in sage/misc/cython.py, needs to be applied after #11376.


---

Attachment

Updated trac_9958-fix-misc_cythonpy.patch to take into account changes in #11376. For some reason the numpy include line appears after the application of the other patches over there. Why it didn't appear before is a mistery.


---

Comment by jhpalmieri created at 2011-06-20 18:40:47

By the way, I don't know how feasible this is, but it would be very nice if the new python spkg passed self-tests: set SAGE_CHECK to "yes" and install the spkg.  Previous versions of Python have failed the self-tests, but it's perhaps the only standard spkg for which this is true.  With the spkg here, on an OS X box:

```
344 tests OK.
4 tests failed:
    test__locale test_ctypes test_distutils test_locale
38 tests skipped:
    test_aepack test_al test_applesingle test_bsddb test_bsddb3
    test_cd test_cl test_codecmaps_cn test_codecmaps_hk
    test_codecmaps_jp test_codecmaps_kr test_codecmaps_tw test_curses
    test_dl test_epoll test_gdb test_gdbm test_gl test_imageop
    test_imgfile test_largefile test_linuxaudiodev test_macos
    test_macostools test_ossaudiodev test_scriptpackages test_smtpnet
    test_socketserver test_startfile test_sunaudiodev test_timeout
    test_tk test_ttk_guionly test_urllib2net test_urllibnet
    test_winreg test_winsound test_zipfile64
5 skips unexpected on darwin:
    test_aepack test_applesingle test_dl test_macos
    test_scriptpackages
make: *** [test] Error 1
An error occurred while testing Python
```

On sage.math:

```
346 tests OK.
1 test failed:
    test_distutils
39 tests skipped:
    test_aepack test_al test_applesingle test_bsddb test_bsddb185
    test_bsddb3 test_cd test_cl test_codecmaps_cn test_codecmaps_hk
    test_codecmaps_jp test_codecmaps_kr test_codecmaps_tw test_curses
    test_dbm test_dl test_gdb test_gdbm test_gl test_imageop
    test_imgfile test_kqueue test_linuxaudiodev test_macos
    test_macostools test_ossaudiodev test_scriptpackages test_smtpnet
    test_socketserver test_startfile test_sunaudiodev test_timeout
    test_tk test_ttk_guionly test_urllib2net test_urllibnet
    test_winreg test_winsound test_zipfile64
7 skips unexpected on linux2:
    test_bsddb test_bsddb3 test_dbm test_gdb test_gdbm test_tk
    test_ttk_guionly
make: *** [test] Error 1
An error occurred while testing Python
```

(I didn't upgrade the distutils package or anything else, just ran "sage -f python-2.7.1.spkg", so some of these may go away.)


---

Comment by fbissey created at 2011-06-20 20:25:14

python testing is difficult. Even in gentoo the procedure is complicated. I'll have a look at it but I cannot make promise. There may be modules that we shouldn't build in the first place (nothing useful to sage, don't worry).

We have this for example in the ebuild:

```
	if use berkdb; then
		ewarn "\"bsddb\" module is out-of-date and no longer maintained inside dev-lang/python. It has"
		ewarn "been additionally removed in Python 3. You should use external, still maintained \"bsddb3\""
		ewarn "module provided by dev-python/bsddb3 which supports both Python 2 and Python 3."
	fi
```


gdb, gdm, dbm and tk require extra things on the host system so they may very well fail without. Actually according to the ebuild distutils and gdm are known to fail.


---

Comment by leif created at 2011-06-24 22:55:06

Just for the record:

http://trac.sagemath.org/sage_trac/ticket/8664#comment:33 gives an example on how to automatically rebuild packages that depend on a newly added spkg (here: Python).

(Artificial version bumps aren't necessary, and simply `touch`ing `spkg/installed/<spkg-that-others-depend-on>` alone doesn't work.)

In general:
 1. Copy the new spkg(s) to `$SAGE_ROOT/spkg/standard/`.
 1. `export SAGE_UPGRADING=yes`
 1. (Optionally set `MAKE` and `SAGE_PARALLEL_SPKG_BUILD`, perhaps `SAGE_CHECK`.)
 1. Run `make` (or better `make build`) rather than doing `./sage -f ...`
 1. Apply patches to the Sage library.
 1. Run `./sage -b` (or `./sage -ba-force` in case not all dependencies are covered by `module_list.py`, which in general I'd consider a bug, but this might be necessary upon a Python upgrade)
 1. Run tests or whatever.

Note that Sage switches to the "main" branch whenever the Sage spkg gets reinstalled.

Of course patches to the build system are usually a bit trickier, but as far as I can see Francois already sorted these out.


---

Comment by fbissey created at 2011-06-24 23:13:27

Thanks for the pointer, it will make testing easier for everyone. The bad news is that all the bits that makes testing easier won't be in 4.7.1. The good news is that everything is merged in 4.7.2.alpha0 at the moment. So once the next release cycle begins things will get easier. No patch will be needed to the build system. All that will remain will be doctest fix and issues like #11339.

I will update trac_9958-fixing_numericalnoise-part2.patch shortly as #11255 broke it. Which means an extra patch may appear later once I have put all the pieces back together.


---

Comment by fbissey created at 2011-06-24 23:15:14

fix numerical noise part 2 (refreshed against 4.7.1.alpha3 -20110625)


---

Attachment

OK. There are a few more patches needed for numerical and formatting noise in 4.7.2.alpha1 but now anyone should be able to upgrade python without a premade sage spkg. All fixes to be able to build sage against python-2.7 out of the box are in!


---

Comment by kcrisman created at 2011-08-23 23:58:15

> (Artificial version bumps aren't necessary, and simply `touch`ing `spkg/installed/<spkg-that-others-depend-on>` alone doesn't work.)
> 
> In general:
>  1. Copy the new spkg(s) to `$SAGE_ROOT/spkg/standard/`.
>  1. `export SAGE_UPGRADING=yes`
Huh, I didn't know about that, and it would be quite useful.  I can't find it in either the installation guide or the developer guide, though - is this documented yet?  Just curious.

Francois, I'll try to give this a test run on PPC OS X and/or Cygwin if you like.


---

Comment by fbissey created at 2011-08-24 00:03:05

Replying to [comment:76 kcrisman]:
> Francois, I'll try to give this a test run on PPC OS X and/or Cygwin if you like.  

Be my guest, I thought that the fact things just became easier warranted an announcement.


---

Comment by kini created at 2011-08-24 01:33:52

Wonderful, this is great news! :) Thanks!


---

Comment by kcrisman created at 2011-08-24 17:43:32

So far Mac PPC is doing fine (I just swapped out the spkgs in a source tar).  Numpy, mercurial, various other python-related spkgs apparently built ok, though it isn't at Scipy or Sage yet.  I did NOT check with `SAGE_CHECK=yes` since I didn't want to have to watch the build and turn that off during the Python build...  Anyway, looks good so far.  If it finishes I'll apply all the patches :)


---

Comment by jhpalmieri created at 2011-08-25 02:00:54

I tried this (new python spkg plus all of the patches, then built from scratch) and I'm seeing a bunch of doctest failures.  Are some of these due to #11339?

```
The following tests failed:

        sage -t  -long -force_lib devel/sage/sage/categories/finite_crystals.py # 1 doctests failed
        sage -t  -long -force_lib devel/sage/sage/rings/morphism.pyx # 0 doctests failed
        sage -t  -long -force_lib devel/sage/sage/rings/integer.pyx # 3 doctests failed
        sage -t  -long -force_lib devel/sage/sage/rings/homset.py # 0 doctests failed
        sage -t  -long -force_lib devel/sage/sage/rings/padics/padic_capped_relative_element.pyx #  1 doctests failed
        sage -t  -long -force_lib devel/sage/sage/combinat/e_one_star.py # 1 doctests failed
        sage -t  -long -force_lib devel/sage/sage/combinat/words/nfactor_enumerable_word.py # 2 doctests failed
        sage -t  -long -force_lib devel/sage/sage/geometry/polyhedra.py # 1 doctests failed
        sage -t  -long -force_lib devel/sage/sage/schemes/generic/scheme.py # 0 doctests failed
        sage -t  -long -force_lib devel/sage/sage/symbolic/callable.py # 5 doctests failed
```

I think I did everything right.  I put together a Sage distribution with the python spkg and the patches, based on 4.7.2.alpha1:

 - [http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.7.2.9958.tar](http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.7.2.9958.tar)

Upgrade path:

 - [http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.7.2.9958/](http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.7.2.9958/)


---

Comment by fbissey created at 2011-08-25 03:44:28

Any failures from #11339 gives you a killed doctest, so

```
sage -t  -long -force_lib devel/sage/sage/rings/morphism.pyx
sage -t  -long -force_lib devel/sage/sage/rings/homset.py
sage -t  -long -force_lib devel/sage/sage/schemes/generic/scheme.py
```

could all be, a verbose run would help figure it out. By nature #11339 is somewhat random, not everyone see the same failures but all these are familiar.

Just checking the others with my current list.

 * sage/categories/finite_crystals.py is a new one introduced in 4.7.2 where the error message has changed slightly when using python-2.7.
 * sage/rings/integer.pyx is definitely python-2.7 related but not patched yet because I am not sure what should be done there.
 * sage/rings/padics/padic_capped_relative_element.pyx same thing
 * sage/combinat/e_one_star.py I had a patch but it became to fuzzy haven't done a new one.
 * sage/combinat/words/nfactor_enumerable_word.py python-2.7 two successive results are inverted, I want someone else to look at that one to make sure we can just do the obvious thing.
 * sage/symbolic/callable.py new in 4.7.2 change in the error message because we are running python-2.7
 * sage/geometry/polyhedra.py never seen that one before, can you re-run it and give more info on the failure?

As you can see a few more patches are needed and apart from #11339 which is a big show stopper because of the crashes at least two other tests point to some potential problems that should be looked at.


---

Comment by strogdon created at 2011-08-25 04:50:39

Here are the failures I get on x86:


```
sage -t -long  -force_lib devel/sage-main/sage/libs/cremona/newforms.pyx # 1 doctests failed
sage -t -long  -force_lib devel/sage-main/sage/misc/sageinspect.py # 1 doctests failed
sage -t -long  -force_lib devel/sage-main/sage/misc/randstate.pyx # 1 doctests failed
sage -t -long  -force_lib devel/sage-main/sage/rings/real_mpfr.pyx # 1 doctests failed
sage -t -long  -force_lib devel/sage-main/sage/stats/intlist.pyx # 1 doctests failed
sage -t -long  -force_lib devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py # 1 doctests failed
sage -t -long  -force_lib devel/sage-main/sage/combinat/e_one_star.py # 1 doctests failed
sage -t -long  -force_lib devel/sage-main/sage/geometry/polyhedra.py # 1 doctests failed
sage -t -long  -force_lib devel/sage-main/sage/crypto/mq/mpolynomialsystem.py # Killed/crashed
sage -t -long  -force_lib devel/sage-main/sage/symbolic/callable.py # 5 doctests failed
sage -t -long  -force_lib devel/sage-main/sage/functions/transcendental.py # 1 doctests failed
sage -t -long  -force_lib devel/sage-main/sage/categories/finite_crystals.py # 1 doctests failed
```


The failures newforms.pyx, real_mpfr.pyx and intlist.pyx are all of the form:


```
File "/storage/sage/sage-4.7.2.alpha1/devel/sage-main/sage/libs/cremona/newforms.pyx", line 53:
    sage: ECModularSymbol(E)
Expected:
    Traceback (most recent call last):
    ...
    OverflowError: long int too large to convert to int
Got:
    Traceback (most recent call last):
      File "/storage/sage/sage-4.7.2.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/storage/sage/sage-4.7.2.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/storage/sage/sage-4.7.2.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[11]>", line 1, in <module>
        ECModularSymbol(E)###line 53:
    sage: ECModularSymbol(E)
      File "newforms.pyx", line 69, in sage.libs.cremona.newforms.ECModularSymbol.__init__ (sage/libs/cremona/newforms.cpp:1820)
        a6 = new_bigint(int(E.a6()))
    OverflowError: Python int too large to convert to C long
```


These tests do not fail on amd64 because "long int too large to convert to int" is returned as the OverflowError instead of "Python int too large to convert to C long".


---

Comment by fbissey created at 2011-08-25 05:00:17

I had forgotten about these. We need different test results for 32 and 64 bits for these.


---

Comment by jhpalmieri created at 2011-08-25 17:30:20

Here's the failure for `sage/geometry/polyhedra.py`:

```
sage -t -long -force_lib "devel/sage/sage/geometry/polyhedra.py"
**********************************************************************
File "/mnt/usb1/scratch/palmieri/9958/sage-4.7.2.9958/devel/sage/sage/geometry/polyhedra.py", line 4948:
    sage: ppoints[0]
Expected:
    (-1.92296268638e-15, -1.92296268638e-15)
Got:
    (0.0, 0.0)
**********************************************************************
```

It looks like numerical noise, but is it an acceptable level of accuracy?


---

Comment by fbissey created at 2011-08-26 01:19:29

Now I remember that test, it is even in the log [attachment:sage-4.7.alpha5-test.log.bz2] I produced a while ago. Strangely enough it doesn't happen anymore on my sage-on-gentoo install. I also have pari-2.5.0 and maxima-5.25.0 on this install, I suspect one of them may be responsible for the disparition of that failure


---

Comment by fbissey created at 2011-08-26 01:35:02

I am wrong! Not maxima or pari, there is a patch for it in [attachment:trac_9958-fixing_numericalnoise-part1.patch]. So it looks like that bit may not be applied properly.


---

Attachment

fix numerical noise in e_one_star.py


---

Comment by fbissey created at 2011-08-26 03:22:48

fix error message in finite_crystals.py


---

Attachment

fix error message in symbolics/callable.py


---

Attachment

Added three new patches. I will rework the patches that need adjusting between 32 and 64 bits next.


---

Comment by fbissey created at 2011-08-26 03:37:03

Replying to [comment:82 strogdon]:
> Here are the failures I get on x86:
> 
> {{{
> sage -t -long  -force_lib devel/sage-main/sage/libs/cremona/newforms.pyx # 1 doctests failed
> sage -t -long  -force_lib devel/sage-main/sage/misc/sageinspect.py # 1 doctests failed
> sage -t -long  -force_lib devel/sage-main/sage/misc/randstate.pyx # 1 doctests failed
> sage -t -long  -force_lib devel/sage-main/sage/rings/real_mpfr.pyx # 1 doctests failed
> sage -t -long  -force_lib devel/sage-main/sage/stats/intlist.pyx # 1 doctests failed
> sage -t -long  -force_lib devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py # 1 doctests failed
> sage -t -long  -force_lib devel/sage-main/sage/combinat/e_one_star.py # 1 doctests failed
> sage -t -long  -force_lib devel/sage-main/sage/geometry/polyhedra.py # 1 doctests failed
> sage -t -long  -force_lib devel/sage-main/sage/crypto/mq/mpolynomialsystem.py # Killed/crashed
> sage -t -long  -force_lib devel/sage-main/sage/symbolic/callable.py # 5 doctests failed
> sage -t -long  -force_lib devel/sage-main/sage/functions/transcendental.py # 1 doctests failed
> sage -t -long  -force_lib devel/sage-main/sage/categories/finite_crystals.py # 1 doctests failed
> }}}
> 
> The failures newforms.pyx, real_mpfr.pyx and intlist.pyx are all of the form:
> 
> {{{
> File "/storage/sage/sage-4.7.2.alpha1/devel/sage-main/sage/libs/cremona/newforms.pyx", line 53:
>     sage: ECModularSymbol(E)
> Expected:
>     Traceback (most recent call last):
>     ...
>     OverflowError: long int too large to convert to int
> Got:
>     Traceback (most recent call last):
>       File "/storage/sage/sage-4.7.2.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
>         self.run_one_example(test, example, filename, compileflags)
>       File "/storage/sage/sage-4.7.2.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
>         OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
>       File "/storage/sage/sage-4.7.2.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
>         compileflags, 1) in test.globs
>       File "<doctest __main__.example_1[11]>", line 1, in <module>
>         ECModularSymbol(E)###line 53:
>     sage: ECModularSymbol(E)
>       File "newforms.pyx", line 69, in sage.libs.cremona.newforms.ECModularSymbol.__init__ (sage/libs/cremona/newforms.cpp:1820)
>         a6 = new_bigint(int(E.a6()))
>     OverflowError: Python int too large to convert to C long
> }}}
> 
> These tests do not fail on amd64 because "long int too large to convert to int" is returned as the OverflowError instead of "Python int too large to convert to C long".


Steve, what about

```
sage -t -long  -force_lib devel/sage-main/sage/rings/polynomial/polynomial_rational_flint.pyx
```



---

Comment by strogdon created at 2011-08-26 03:53:30

Replying to [comment:88 fbissey]:
> Replying to [comment:82 strogdon]:
> 
> Steve, what about
> {{{
> sage -t -long  -force_lib devel/sage-main/sage/rings/polynomial/polynomial_rational_flint.pyx
> }}}

Here on x86 and amd64 the test passes. So, there seems to be some sort of inconsistency, doesn't it?


---

Comment by fbissey created at 2011-08-26 03:58:09

Replying to [comment:89 strogdon]:
> Replying to [comment:88 fbissey]:
> > Replying to [comment:82 strogdon]:
> > 
> > Steve, what about
> > {{{
> > sage -t -long  -force_lib devel/sage-main/sage/rings/polynomial/polynomial_rational_flint.pyx
> > }}}
> 
> Here on x86 and amd64 the test passes. So, there seems to be some sort of inconsistency, doesn't it?

Yes! I'll fix it but it should be investigated. Gut feeling is on variation in cython definitions.


---

Comment by kcrisman created at 2011-08-26 19:45:09

I've tried to remove the failures known above here.  Note that I didn't get the last few patches in time, but I removed those failures as well, assuming they were the same.  The timeouts/killed are _probably_ unrelated - my computer is < 1 GHz, so I get a lot of timeouts and I forgot to set `SAGE_TIMEOUT_LONG` before I ran the tests - but at any rate I hope this will be useful.  After the hurricane I'll start this up again and run the remaining tests.

```
        sage -t -long "devel/sage/sage/crypto/mq/mpolynomialsystem.py" # Killed/crashed
        sage -t -long "devel/sage/sage/functions/transcendental.py"
        sage -t -long "devel/sage/sage/groups/generic.py" # Killed/crashed
        sage -t -long "devel/sage/sage/interfaces/maxima.py" # Time out
        sage -t -long "devel/sage/sage/interfaces/singular.py" # Killed/crashed
        sage -t -long "devel/sage/sage/libs/cremona/newforms.pyx"
        sage -t -long "devel/sage/sage/libs/ppl.pyx" # Time out
        sage -t -long "devel/sage/sage/libs/singular/ring.pyx" # Killed/crashed
        sage -t -long "devel/sage/sage/misc/randstate.pyx"
        sage -t -long "devel/sage/sage/misc/sageinspect.py"
        sage -t -long "devel/sage/sage/rings/multi_power_series_ring_element.py" # Killed/crashed
        sage -t -long "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py" # Killed/crashed
        sage -t -long "devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx" # Killed/crashed
        sage -t -long "devel/sage/sage/rings/polynomial/polynomial_singular_interface.py" # Killed/crashed
        sage -t -long "devel/sage/sage/rings/real_mpfr.pyx"
        sage -t -long "devel/sage/sage/rings/tests.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/BSD.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_curve_isogeny.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_field.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_finite_field.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_generic.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_local_data.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_number_field.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_point.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py" # Time out
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/gal_reps.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/heegner.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/period_lattice.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/generic/scheme.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/plane_conics/con_finite_field.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/plane_curves/projective_curve.py" # Killed/crashed
        sage -t -long "devel/sage/sage/stats/intlist.pyx"
        sage -t -long "devel/sage/sage/structure/sage_object.pyx" # Killed/crashed
```



---

Comment by kcrisman created at 2011-08-26 20:14:00

Here is one example.

```
sage -t -long "devel/sage/sage/functions/transcendental.py" 
**********************************************************************
File "/Users/student/Desktop/sage-4.7.2.alpha1/devel/sage/sage/functions/transcendental.py", line 83:
    sage: w = exponential_integral_1(2,4); w
Expected:
    [0.04890051070806112, 0.0037793524098489067, 0.00036008245216265873, 3.7665622843924751e-05] 
Got:
    [0.04890051070806112, 0.0037793524098489067, 0.00036008245216265873, 3.766562284392475e-05]
**********************************************************************
```

Here is one of the killed ones (not a timeout, I'm surprised):

```
sage -t -long "devel/sage/sage/crypto/mq/mpolynomialsystem.py"
The doctested process was killed by signal 10
         [352.0 s]
```

Could this be an unrelated 4.7.2.alpha1 issue on my platform?


---

Comment by fbissey created at 2011-08-26 21:22:40

I am particularly interested in the killed/crashed tests. And also those for which there is already a patch.

```
sage -t -long "devel/sage/sage/libs/cremona/newforms.pyx"
sage -t -long "devel/sage/sage/rings/real_mpfr.pyx"
sage -t -long "devel/sage/sage/stats/intlist.pyx"
```

are the 32/64 bits message difference already mentioned by Steve.

The timeouts are the regular suspect on ppc if I am not mistaken.

The transcendental.py doctest you are quoting is worrying me. It is patched in [attachment:trac_9958-fixing_numericalnoise-part1.patch] but you have a slightly different result again (one less digit on the last number). We may have to consider 
a different patch.

All killed/crashed doctest are candidates for #11339 but you'll have to run sage -gdb on them to be sure.


---

Comment by leif created at 2011-08-26 23:32:33

Replying to [comment:93 kcrisman]:
> Here is one of the killed ones (not a timeout, I'm surprised):

```
sage -t -long "devel/sage/sage/crypto/mq/mpolynomialsystem.py"
The doctested process was killed by signal 10
         [352.0 s]
```

> Could this be an unrelated 4.7.2.alpha1 issue on my platform?

Does `SIGUSR1` (!#10) have a special meaning on Darwin?


---

Comment by fbissey created at 2011-08-26 23:52:44

Almost anything with "polynomial" in its name is likely to use singular (and crypto/mq/mpolynomialsystem.py is no exception), signal 10 is apparently a user defined signal so it could be anything. 

We'll have to wait for the hurricane to move on before Karl can answer us on any of this points.

Looking back at you list Karl I am also very curious about

```
sage -t -long "devel/sage/sage/structure/sage_object.pyx
sage -t -long "devel/sage/sage/misc/sageinspect.py"
sage -t -long "devel/sage/sage/misc/randstate.pyx"
```

two of these have already been patched (sage_object and randstate) in this ticket so I am quite curious about what's wrong with them.


---

Comment by kcrisman created at 2011-08-27 00:47:01

Yeah, I'm sorry I couldn't provide more information.  The tests only just finished after classes, and I had one hour to copy/paste the above, restart just doing the failed tests, write a lecture, check email, and then turn off and unplug my PPC machine.   I just couldn't do any more.  I certainly wasn't taking an eMac home on the bike/train with me!

But we are just due for heavy rain and wind, so hopefully Monday I can get back on it and tell you more, save an extended power outage.  Much better than an earthquake, I think fbissey would heartily agree.  I wish I'd had a chance to run tests after #11339, but I just knew it would take eons.  I'd do it on one of my home PPC machines (believe it or not, I have two more) but one I can no longer get !XCode for, and the other is also slow enough it wouldn't be ready by the time we have to unplug _it_... sigh.

Anyway, I'll keep this ticket on the priority list for the machine I did these tests on.


---

Comment by leif created at 2011-08-29 02:59:44

So, I did test this with Sage 4.7.2.alpha2 on my "last" 32-bit machine, a Pentium4 Prescott (which has SSE3) running Ubuntu 9.04; my other Pentium4 (Northwood, without SSE3 / PNI) recently died, and I won't revive it in the near future.

The good news are: The patches all still apply to 4.7.2.alpha2, though many hunks with partially large offsets, but no fuzz.

The bad news: I expected some numerical noise because of 32-bit architecture with (there rather rare) SSE3 (`-mfpmath=sse`), but also experienced at least one segfault (in `sage/rings/homset.py`). I'll have to investigate the rest, for now just:

```
...
sage -t  -long -force_lib "devel/sage/sage/geometry/polyhedra.py"
**********************************************************************
File "/media/H-1TB-P6-linux2/Sage/sage-4.7.2.alpha2-gcc-4.5.1/devel/sage/sage/geometry/polyhedra.py", line 4948:
    sage: ppoints[0]
Expected:
    (-1.92296268638e-15, -1.92296268638e-15)
Got:
    (0.0, 0.0)
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_171
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/leif/.sage//tmp/.doctest_polyhedra.py
	 [166.0 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  -long -force_lib "devel/sage/sage/libs/cremona/newforms.pyx"
	sage -t  -long -force_lib "devel/sage/sage/functions/transcendental.py"
	sage -t  -long -force_lib "devel/sage/sage/misc/randstate.pyx"
	sage -t  -long -force_lib "devel/sage/sage/combinat/words/suffix_trees.py"
	sage -t  -long -force_lib "devel/sage/sage/combinat/words/nfactor_enumerable_word.py"
	sage -t  -long -force_lib "devel/sage/sage/rings/morphism.pyx"
	sage -t  -long -force_lib "devel/sage/sage/rings/real_mpfr.pyx"
	sage -t  -long -force_lib "devel/sage/sage/rings/homset.py"
	sage -t  -long -force_lib "devel/sage/sage/stats/intlist.pyx"
	sage -t  -long -force_lib "devel/sage/sage/schemes/generic/scheme.py"
	sage -t  -long -force_lib "devel/sage/sage/geometry/polyhedra.py"
Total time for all tests: 26263.8 seconds
make: *** [testlong] Error 128

real	439m23.357s
user	393m40.644s
sys	31m7.485s
leif@californication:~/Sage/sage-4.7.2.alpha2-gcc-4.5.1$ 
```

(The tail of the log. More to come later.)

Note that I didn't test in parallel, although with some other CPU-greedy process running, but time-outs are unlikely. Vanilla 4.7.2.alpha2 passed all tests in exactly the same setting (and I did rebuild all dependent packages when installing the Python 2.7 spkg, modulo missing extension module dependencies in `module_list.py`).


---

Comment by leif created at 2011-08-29 03:32:28

Ok, *three* segfaults (two of them without backtrace / Sage message, for whatever reason), some Python ints too large ("as usual" I guess), some numerical noise, the rest apparently related to dictionaries / hashing(?).

Attaching short logs of rerun tests (all reproducable)...


---

Attachment

Pentium4 Prescott (SSE3 / PNI, 32-bit), GCC 4.5.1, native code, `-mfpmath=sse`, Ubuntu 9.04 x86


---

Comment by leif created at 2011-08-29 04:20:12

Pentium4 Prescott (SSE3 / PNI, 32-bit), GCC 4.5.1, native code, -mfpmath=sse, Ubuntu 9.04 x86 (The three segfaulting files tested in verbose mode.)


---

Attachment

Replying to [comment:99 leif]:
> Attaching short logs of rerun tests (all reproducable)...

Done.

Haha, the first segfault is an especially nice one:

```
...
  10 tests in __main__.example_7
   6 tests in __main__.example_8
   7 tests in __main__.example_9
511 tests in 55 items.
511 passed and 0 failed.
Test passed.
Segmentation fault
	 [9.8 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long -verbose "devel/sage/sage/rings/morphism.pyx"
Total time for all tests: 9.8 seconds

real	0m10.013s
user	0m6.980s
sys	0m1.068s
```



---

Comment by fbissey created at 2011-08-29 05:05:40

Thanks leif. Nothing worrying there. There is a patch for sage/geometry/polyhedra.py but obviously it doesn't apply properly anymore. transcendantal.py, randstate.pyx and intlist.pyx are all already patched but may need more tweaking, I'd be grateful for the output of these.

```
sage -t  -long -force_lib "devel/sage/sage/combinat/words/nfactor_enumerable_word.py"
```

is known to fail but is probably a minor adjustment.

```
sage -t  -long -force_lib "devel/sage/sage/combinat/words/suffix_trees.py"
```

is new. The rest look like #11339 material.


---

Comment by leif created at 2011-08-29 05:48:12

Replying to [comment:101 fbissey]:
> Thanks leif. Nothing worrying there. There is a patch for sage/geometry/polyhedra.py but obviously it doesn't apply properly anymore. transcendantal.py, randstate.pyx and intlist.pyx are all already patched but may need more tweaking, I'd be grateful for the output of these.

The failing doctests are all in [attachment:Doctest_failures_Sage-4.7.2.alpha2_Linux_x86_SSE3-individual_tests_rerun.log].

> [...] The rest look like #11339 material.

I'm just to apply the patches from there; the machine is dead slow, doing a `./sage -ba-force` atm to exclude missing extension module dependencies, as I've not built from scratch.


---

Comment by fbissey created at 2011-08-29 06:50:48

I was too fast. Some of the failures are already reported by Steve. I may try to update the patch set a bit tonight.


---

Comment by leif created at 2011-08-29 07:00:33

Just experienced some new(?) error when cloning the Sage library for #11339:

```
...
byte-compiling /home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python2.7/site-packages/sage/misc/copying.py to copying.pyc
byte-compiling /home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python2.7/site-packages/sage/version.py to version.pyc
running install_egg_info
Removing /home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python2.7/site-packages/sage-0.0.0-py2.7.egg-info
Writing /home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python2.7/site-packages/sage-0.0.0-py2.7.egg-info
Exception in thread Thread-4 (most likely raised during interpreter shutdown):
Traceback (most recent call last):
  File "/home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python/threading.py", line 530, in __bootstrap_inner
  File "/home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python/threading.py", line 483, in run
  File "/home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python/multiprocessing/pool.py", line 272, in _handle_workers
<type 'exceptions.TypeError'>: 'NoneType' object is not callable
Exception in thread Thread-1 (most likely raised during interpreter shutdown):
Traceback (most recent call last):
  File "/home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python/threading.py", line 530, in __bootstrap_inner
  File "/home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python/threading.py", line 483, in run
  File "/home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python/multiprocessing/pool.py", line 272, in _handle_workers
<type 'exceptions.TypeError'>: 'NoneType' object is not callable

real	1m35.816s
user	1m35.794s
sys	0m5.648s

After cloning, if you change any Sage library files and want to rebuild
the html version of the reference manual, use the command
    sage -docbuild reference html
(after running 'sage -b').
...
```



---

Comment by leif created at 2011-08-29 07:09:55

Waaaaaah!

```
leif@californication:~/Sage/sage-4.7.2.alpha2-gcc-4.5.1/devel/sage-9958-11339$ ../../sage -hg import -v ~/Sage/patches/trac_11339_refcount_singular_polynomials.patch 
applying /home/leif/Sage/patches/trac_11339_refcount_singular_polynomials.patch
patching file sage/rings/polynomial/multi_polynomial_libsingular.pxd
patching file sage/rings/polynomial/multi_polynomial_libsingular.pyx
Hunk #13 FAILED at 727
Hunk #14 FAILED at 741
Hunk #15 FAILED at 763
Hunk #16 FAILED at 773
Hunk #17 FAILED at 825
Hunk #18 succeeded at 910 with fuzz 2 (offset 72 lines).
Hunk #19 FAILED at 875
Hunk #20 succeeded at 961 (offset 75 lines).
Hunk #21 succeeded at 980 (offset 75 lines).
Hunk #22 succeeded at 1006 (offset 75 lines).
...
```

(The first patch still applies, with offsets.)

I'm not going to fix that...


---

Comment by strogdon created at 2011-08-29 13:26:15

Replying to [comment:101 fbissey]:
> Thanks leif. Nothing worrying there. There is a patch for sage/geometry/polyhedra.py but obviously it doesn't apply properly anymore. transcendantal.py, randstate.pyx and intlist.pyx are all already patched but may need more tweaking, I'd be grateful for the output of these.
I'm sure the polyhedra.py patch was needed at one time but it now (?) appears that 

```

@@ -4946,7 +4946,7 @@
         sage: proj = ProjectionFuncStereographic([1.1,1.1,1.1])
         sage: ppoints = [proj(vector(x)) for x in cube]
         sage: ppoints[0]
-        (0.0, 0.0)
+        (-1.92296268638e-15, -1.92296268638e-15)
     """
     def __init__(self, projection_point):
         """
```


from trac_9958-fixing_numericalnoise-part1.patch is no longer needed.


---

Comment by fbissey created at 2011-08-29 13:39:00

Replying to [comment:106 strogdon]:
> Replying to [comment:101 fbissey]:
> > Thanks leif. Nothing worrying there. There is a patch for sage/geometry/polyhedra.py but obviously it doesn't apply properly anymore. transcendantal.py, randstate.pyx and intlist.pyx are all already patched but may need more tweaking, I'd be grateful for the output of these.
> I'm sure the polyhedra.py patch was needed at one time but it now (?) appears that 
> {{{
> 
> `@``@` -4946,7 +4946,7 `@``@`
>          sage: proj = ProjectionFuncStereographic([1.1,1.1,1.1])
>          sage: ppoints = [proj(vector(x)) for x in cube]
>          sage: ppoints[0]
> -        (0.0, 0.0)
> +        (-1.92296268638e-15, -1.92296268638e-15)
>      """
>      def __init__(self, projection_point):
>          """
> }}}
> 
> from trac_9958-fixing_numericalnoise-part1.patch is no longer needed.

You are right I am reading the test results backwards. It now seems to go to 0 properly. One less patch in the patch and one less worry.


---

Comment by kcrisman created at 2011-08-29 19:37:16

Okay, you can get a full list of current failure and what they looked like at [this link](http://sage.math.washington.edu/home/kcrisman/Failures.txt).  Some are definitely known above, but others may be unknown.  The timeouts are probably just due to this machine (and the Maxima one), but others I don't know whether they are here or #11339.


---

Comment by fbissey created at 2011-08-29 19:54:27

fixing numerical noise part 1 - updated 20110830


---

Attachment

Updated the first patch for polyhedra.py, split transcendental.py in its own patch. I lowered the precision tested in the last numbers so that results from 32 and 64 bits are not different.


---

Comment by fbissey created at 2011-08-29 20:10:36

Replying to [comment:108 kcrisman]:
> Okay, you can get a full list of current failure and what they looked like at [this link](http://sage.math.washington.edu/home/kcrisman/Failures.txt).  Some are definitely known above, but others may be unknown.  The timeouts are probably just due to this machine (and the Maxima one), but others I don't know whether they are here or #11339.

You have some nasty stuff in polyhedra.py

```
File "/Users/student/Desktop/sage-4.7.2.alpha1/devel/sage/sage/geometry/polyhedra.py", line 5250:
    sage: _.show()
Exception raised:
    Traceback (most recent call last):
      File "/Users/student/Desktop/sage-4.7.2.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/student/Desktop/sage-4.7.2.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/student/Desktop/sage-4.7.2.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_183[5]>", line 1, in <module>
        _.show()###line 5250:
    sage: _.show()
      File "/Users/student/Desktop/sage-4.7.2.alpha1/local/lib/python/site-packages/sage/misc/displayhook.py", line 174, in displayhook
        print_obj(sys.stdout, obj)
      File "/Users/student/Desktop/sage-4.7.2.alpha1/local/lib/python/site-packages/sage/misc/displayhook.py", line 142, in print_obj
        print >>out_stream, `obj`
      File "base.pyx", line 80, in sage.plot.plot3d.base.Graphics3d.__repr__ (sage/plot/plot3d/base.c:2526)
      File "base.pyx", line 1124, in sage.plot.plot3d.base.Graphics3d.show (sage/plot/plot3d/base.c:10344)
      File "base.pyx", line 663, in sage.plot.plot3d.base.Graphics3d.export_jmol (sage/plot/plot3d/base.c:5867)
      File "/Users/student/Desktop/sage-4.7.2.alpha1/local/lib/python2.7/zipfile.py", line 1138, in writestr
        self.fp.write(zinfo.FileHeader())
      File "/Users/student/Desktop/sage-4.7.2.alpha1/local/lib/python2.7/zipfile.py", line 348, in FileHeader
        len(filename), len(extra))
    error: integer out of range for 'H' format code
```

You get an extra digit in randstate compared to x86 :( [note to self it is in numerical_noise_part4].

sage-inspect looks bad :( but not hopeless. The message is just overly long. I will have to postpone the rest for later.


---

Comment by fbissey created at 2011-08-29 22:17:57

sage-inspect is actually an example merged in 4.7.2.alpha1 from #11298 it may not be a python2.7 problems unless you already tested that ticket. I wonder if #11734 would help, the result should be python code but you have cython code instead.


---

Comment by fbissey created at 2011-08-29 22:26:29

In polyhedra.py it looks like you have a problem with jmol printing 3D images to file. It involves zip, looking at the pyx there is an instance of testing zip. Could you paste the cython code that produced sage/plot/plot3d/base.c:5867 ?


---

Attachment

fix some 32/64 bits messages


---

Comment by fbissey created at 2011-08-29 23:05:01

all fixes to real_mpfr.pyx split from everything else


---

Attachment

split real_mpfr.pyx from the mixed fixes patch


---

Attachment

Updated the patch set again. split real_mpfr.pyx from the mixedfix patch. The 32/64 bits issues reported is separate from the message that was already patched. Added a patch to fix 32/64 bit messages.


---

Comment by kcrisman created at 2011-08-30 16:04:03

Replying to [comment:112 fbissey]:
> In polyhedra.py it looks like you have a problem with jmol printing 3D images to file. It involves zip, looking at the pyx there is an instance of testing zip. Could you paste the cython code that produced sage/plot/plot3d/base.c:5867 ?

```
  /* "sage/plot/plot3d/base.pyx":663
 *         f.write("isosurface fullylit; pmesh o* fullylit; set antialiasdisplay on;\n")
 * 
 *         render_params.output_archive.writestr('SCRIPT', f.getvalue())             # <<<<<<<<<<<<<<
 *         render_params.output_archive.close()
 * 
 */
  __pyx_t_3 = PyObject_GetAttr(__pyx_v_render_params, __pyx_n_s__output_archive); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_3, __pyx_n_s__writestr); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = PyObject_GetAttr(__pyx_v_f, __pyx_n_s__getvalue); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = PyObject_Call(__pyx_t_3, ((PyObject *)__pyx_empty_tuple), NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = PyTuple_New(2); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(((PyObject *)__pyx_t_3));
  __Pyx_INCREF(((PyObject *)__pyx_n_s__SCRIPT));
  PyTuple_SET_ITEM(__pyx_t_3, 0, ((PyObject *)__pyx_n_s__SCRIPT));
  __Pyx_GIVEREF(((PyObject *)__pyx_n_s__SCRIPT));
  PyTuple_SET_ITEM(__pyx_t_3, 1, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  __pyx_t_4 = 0;
  __pyx_t_4 = PyObject_Call(__pyx_t_2, ((PyObject *)__pyx_t_3), NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(((PyObject *)__pyx_t_3)); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

5867 is 

```
  __pyx_t_4 = PyObject_Call(__pyx_t_2, ((PyObject *)__pyx_t_3), NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
```


----
I was also surprised by the polyhedra.py additional weirdness.  Anything I can do to help identify it?  Warning: I'm planning on building and testing alpha2 _without_ Python 2.7 now, which will tie up most resources on this machine for a couple days.


---

Comment by strogdon created at 2011-08-31 02:10:06

Replying to [comment:109 fbissey]:
> Updated the first patch for polyhedra.py, split transcendental.py in its own patch. I lowered the precision tested in the last numbers so that results from 32 and 64 bits are not different.
Here the fix_transcendental patch fixed the associated test on x86 but now the test fails on amd64:


```
sage -t -long  -force_lib devel/sage-main/sage/functions/transcendental.py
**********************************************************************
File "/storage/sage/sage-4.7.2.alpha2/devel/sage-main/sage/functions/transcendental.p
y", line 83:
    sage: w = exponential_integral_1(2,4); w
Expected:
    [0.04890051070806112, 0.0037793524098489067, 0.00036008245216265873, 3.7665622843
924...e-05]
Got:
    [0.04890051070806112, 0.0037793524098489063, 0.00036008245216265873, 3.7665622843
924534e-05]
**********************************************************************
```


This is odd! I wonder what changed? Previously this test must have returned ...67 and not ...63 for it to pass.


---

Comment by fbissey created at 2011-08-31 02:42:02

Replying to [comment:115 strogdon]:
> Replying to [comment:109 fbissey]:
> > Updated the first patch for polyhedra.py, split transcendental.py in its own patch. I lowered the precision tested in the last numbers so that results from 32 and 64 bits are not different.
> Here the fix_transcendental patch fixed the associated test on x86 but now the test fails on amd64:
> 
> {{{
> sage -t -long  -force_lib devel/sage-main/sage/functions/transcendental.py
> **********************************************************************
> File "/storage/sage/sage-4.7.2.alpha2/devel/sage-main/sage/functions/transcendental.p
> y", line 83:
>     sage: w = exponential_integral_1(2,4); w
> Expected:
>     [0.04890051070806112, 0.0037793524098489067, 0.00036008245216265873, 3.7665622843
> 924...e-05]
> Got:
>     [0.04890051070806112, 0.0037793524098489063, 0.00036008245216265873, 3.7665622843
> 924534e-05]
> **********************************************************************
> }}}
> 
> This is odd! I wonder what changed? Previously this test must have returned ...67 and not ...63 for it to pass.


It's my fault for not noticing this difference between 32 and 64 bit results. It was there before but I didn't notice it. I thought the last number was the only thing different so when I truncated the last number to the common digits I dropped the difference between 32 and 64 bit. So it is entirely my fault.


---

Attachment

fixing numerical noise in transcendental.py- split from numerical noise pt1 - updated 2011092


---

Comment by fbissey created at 2011-09-01 23:37:35

transcendental patch updated.


---

Comment by leif created at 2011-09-02 01:15:48

Replying to [comment:117 fbissey]:
> transcendental patch updated.

Literally?


---

Comment by fbissey created at 2011-09-02 01:33:50

Replying to [comment:118 leif]:
> Replying to [comment:117 fbissey]:
> > transcendental patch updated.
> 
> Literally?
Literally.


---

Comment by kcrisman created at 2011-09-02 12:04:43

Just for reference, on the PPC machine all tests pass with alpha2 except three timeouts which are long-standing (I didn't bother to set `SAGE_TIMEOUT_LONG` but I've seen these many times).

So all the rest are due to this ticket or #11339.  

Would it be helpful for me to do #11339 on this new build (without Python 2.7), or is that in limbo right now anyway?  Alternately, is there any way to decouple this ticket from that one?


---

Comment by fbissey created at 2011-09-02 12:57:55

Replying to [comment:120 kcrisman]:
> Just for reference, on the PPC machine all tests pass with alpha2 except three timeouts which are long-standing (I didn't bother to set `SAGE_TIMEOUT_LONG` but I've seen these many times).
> 
> So all the rest are due to this ticket or #11339.  

That's a very useful point of reference. Thank you for providing it.

> 
> Would it be helpful for me to do #11339 on this new build (without Python 2.7), or is that in limbo right now anyway?  Alternately, is there any way to decouple this ticket from that one?

Technically you can apply #11339 without python 2.7 - the behavior we want to correct is only revealed when we use python 2.7 but I guess it would be useful to know if there are any side effects if you apply the patch on a python 2.6 install. Bear in mind that the current patch are not necessarily the best solution to the problem, what's more they are a whack a mole game. Fix something here and some new fault appears in a completely unexpected location.


---

Comment by fbissey created at 2011-10-04 21:14:01

I will update the python spkg to 2.7.3 when it will be released. 2.7.3 will include the patch to python that we have been carrying in sage for the longest time. See:
[http://bugs.python.org/issue7689](http://bugs.python.org/issue7689)

Does anyone know if the apocalypse is about to happen?


---

Comment by jason created at 2011-10-18 18:28:02

Fixes #1159, according to that ticket.


---

Comment by fbissey created at 2011-11-01 23:18:48

That's really weird. Some of the hashing problems I encounter with python 2.7 are almost the same as reported in [http://trac.sagemath.org/sage_trac/ticket/4957#comment:3](http://trac.sagemath.org/sage_trac/ticket/4957#comment:3)

```
sage -t -long -force_lib "devel/sage-main/sage/rings/integer.pyx"
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/rings/integer.pyx", line 3046:
    sage: n = -920390823904823094890238490238484; n.__hash__()
Expected:
    6874330978542788722   
Got:
    -2623069716
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/rings/integer.pyx", line 3061:
    sage: hash(n)
Expected:
    -9223372036854767616      
Got:
    8192
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/rings/integer.pyx", line 3064:
    sage: hash(n) == hash(int(n))
Expected:
    True
Got:
    False
**********************************************************************
```



---

Comment by fbissey created at 2011-11-02 01:48:48

With python-2.6:

```
sage: n=2^63+2^13
sage: n
9223372036854784000
sage: int(n)
9223372036854784000L
sage: hash(n)
-9223372036854767616
sage: hash(int(n))
-9223372036854767616
```

with python-2.7

```
sage: n=2^63+2^13
sage: n
9223372036854784000
sage: hash(n)
8192
sage: int(n)
9223372036854784000L
sage: hash(int(n))
-9223372036854767616
```

Furthermore in both case:

```
sage: type(n)
<type 'sage.rings.integer.Integer'>
sage: type(int(n))
<type 'long'>
```

So I would expect different hashes naively.


---

Comment by fbissey created at 2011-11-02 02:02:57

Regarding

```
sage -t -long -force_lib "devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py"
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py", line 20:
    sage: it.next()
Expected:
    word: 6456
Got:
    word: 5645
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py", line 22:
    sage: it.next()
Expected:
    word: 5645
Got:
    word: 6456
**********************************************************************
```

With python-2.7

```
sage: w = Word([4,5,6])^7
sage: w
word: 456456456456456456456
sage: it = w.factor_iterator(4)
sage: it.next()
word: 5645
sage: it.next()
word: 6456
sage: it.next()
word: 4564
```

with python-2.6

```
sage: w = Word([4,5,6])^7
sage: w
word: 456456456456456456456
sage: it = w.factor_iterator(4)
sage: it.next()
word: 6456
sage: it.next()
word: 5645
sage: it.next()
word: 4564
```

So it looks like with python 2.6 we where moving in the series of number with a stride 2 while python 2.7 works through the sequence with a stride 1.


---

Comment by strogdon created at 2011-11-02 05:01:46

Here on x86 I get only two failures:


```

sage -t -long  -force_lib devel/sage-main/sage/misc/randstate.pyx
**********************************************************************
File "/storage/sage/sage-4.7.2.rc0/devel/sage-main/sage/misc/randstate.pyx", line 61:
    sage: rtest()
Expected:
    (978, 0.184109262667515, -3*x^2 - 1/12, (4,5), [ 0, 1, 1, 0, 0 ], 1161603091, 603
59, 0.83350776541997362)
Got:
    (978, 0.184109262667515, -3*x^2 - 1/12, (4,5), [ 0, 1, 1, 0, 0 ], 1161603091, 603
59, 0.8335077654199736)
**********************************************************************
```


and 


```
sage -t -long  -force_lib devel/sage-main/sage/matrix/matrix_double_dense.pyx
**********************************************************************
File "/storage/sage/sage-4.7.2.rc0/devel/sage-main/sage/matrix/matrix_double_dense.py
x", line 1046:
    sage: A.singular_values(eps='junk')
Expected:
    Traceback (most recent call last):
    ...
    ValueError: invalid literal for float(): junk
Got:
    Traceback (most recent call last):
      File "/storage/sage/sage-4.7.2.rc0/local/bin/ncadoctest.py", line 1231, in run_
one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/storage/sage/sage-4.7.2.rc0/local/bin/sagedoctest.py", line 38, in run_o
ne_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags
)
      File "/storage/sage/sage-4.7.2.rc0/local/bin/ncadoctest.py", line 1172, in run_
one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[37]>", line 1, in <module>
        A.singular_values(eps='junk')###line 1046:
    sage: A.singular_values(eps='junk')
      File "matrix_double_dense.pyx", line 1075, in sage.matrix.matrix_double_dense.M
atrix_double_dense.singular_values (sage/matrix/matrix_double_dense.c:6338)
        eps = RDF(eps)
      File "parent.pyx", line 988, in sage.structure.parent.Parent.__call__ (sage/str
ucture/parent.c:7326)
      File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMa
p_unique._call_ (sage/structure/coerce_maps.c:3268)
      File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMa
p_unique._call_ (sage/structure/coerce_maps.c:3171)
      File "real_double.pyx", line 548, in sage.rings.real_double.RealDoubleElement._
_init__ (sage/rings/real_double.c:5567)
    ValueError: could not convert string to float: junk
**********************************************************************
```


The latter also fails here the same way on amd64 and is documented on sage-devel

http://groups.google.com/group/sage-devel/browse_thread/thread/8e1d7f665ac5be37

but with some slight differences.


---

Comment by fbissey created at 2011-11-02 11:41:04

OK Steve, I got the matrix_double_dense but you don't get the numerical noise. I believe the noise may come from python-2.7.2. Interesting that the hashing and enumeration problem are 64bit only. I'll check on the mac.


---

Comment by fbissey created at 2011-11-02 22:37:12

Fix doctest in matrix_double_dense.pyx about junk


---

Attachment

New patch to fix the message about junk.


---

Comment by fbissey created at 2011-11-03 01:52:16

I have now split the hashing issue in #11986


---

Comment by fbissey created at 2011-11-03 02:13:15

fix the doctest on enumeration order for 64bit system


---

Attachment

One more patch added to fix combinat/words/nfactor_enumerable_word.py on 64 bit system. I believe is output is equivalent in both case so it is not important.


---

Comment by jdemeyer created at 2011-11-03 21:16:30

Removed old dependencies.


---

Comment by jdemeyer created at 2011-11-03 21:24:31

The spkg needs to be rebased to #11447.


---

Comment by jdemeyer created at 2011-11-03 21:26:35

Permissions is the spkg should be 0644 (or 0755 for executables), currently many files are 0640 or 0750.


---

Comment by fbissey created at 2011-11-04 01:12:44

Replying to [comment:133 jdemeyer]:
> The spkg needs to be rebased to #11447.
I looked at that before making my spkg. I believe the strategy used in #11447 is in python-2.7. Someone with a debian system proves me wrong but I think that works out of the box.


---

Comment by leif created at 2011-11-04 01:48:05

Replying to [comment:135 fbissey]:
> Replying to [comment:133 jdemeyer]:
> > The spkg needs to be rebased to #11447.
> I looked at that before making my spkg. I believe the strategy used in #11447 is in python-2.7. Someone with a debian system proves me wrong but I think that works out of the box.

Well, we did take the patch from Python upstream, but IIRC there are further changes to `spkg-install`, and the new spkg needs the previous one to be mentioned in `SPKG.txt` anyway (to pass the merger's sanity check).


---

Comment by leif created at 2011-11-04 02:03:06

Indeed, there've been *a lot of* changes inbetween:

```diff
diff -Nu python-2.7.1/spkg-install python-2.6.4.p11/spkg-install
--- python-2.7.1/spkg-install	2011-05-20 05:41:41.000000000 +0200
+++ python-2.6.4.p11/spkg-install	2011-07-05 10:46:40.000000000 +0200
@@ -5,50 +5,127 @@
 
 CUR=`pwd`
 
-if [ "$SAGE_LOCAL" = "" ]; then
-   echo "SAGE_LOCAL undefined ... exiting";
-   echo "Maybe run 'sage -sh'?"
-   exit 1
+if [ -z "$SAGE_LOCAL" ]; then
+    echo >&2 "SAGE_LOCAL undefined ... exiting"
+    echo >&2 "Maybe run 'sage -sh'?"
+    exit 1
 fi
 
 # PATCH
 
-# Due to issues building Python on Ubuntu 11.04, a file is patched
-# on these systems. 
+# When building Python 2.6 on Debian and derivatives with multiarch,
+# system library directories are not correctly setup.  This patch
+# fixes this, with no-op on other systems.
+# The fix requires 'dpkg-architecture' to be installed there though
+# (see below).
+echo "Patching src/setup.py for multiarch."
+patch -p0 < patches/setup.py.multiarch.patch
+if [ $? -ne 0 ]; then
+    echo >&2 "Error patching src/setup.py"
+    exit 1
+fi
 
-if [ -f /etc/issue ] && grep "Ubuntu 11.04" /etc/issue ; then
-   echo "Patching src/Modules/Setup.dist as this is Ubuntu 11.04"
-   patch -p0 < patches/Modules.Setup.dist.patch
+# Due to a python bug with Solaris 
+# see http://bugs.python.org/issue1759169
+# it is necessary to apply a patch to configure.in
+# then run autoconf. This not only generates a
+# new 'configure' script, but some subdirectories too
+# so these will be copied. 
+
+if [ "x`uname`" = xSunOS ] ; then
+   echo "Applying a revised 'configure' script for Solaris"
+   echo "See http://bugs.python.org/issue1759169"
+   echo "http://trac.sagemath.org/sage_trac/ticket/7867"
+   cp -r patches/autom4te.cache patches/configure patches/configure.in src
    if [ $? -ne 0 ]; then
-      echo "Error patching src/Modules/Setup.dist"
+      echo >&2 "Failed to apply the Solaris patches needed for"
+      echo >&2 "http://bugs.python.org/issue1759169"
+      echo >&2 "http://trac.sagemath.org/sage_trac/ticket/7867"
       exit 1
    fi
+   echo "Setting  HAVE_FD_TRANSFER=0 for Solaris to allow"
+   echo "the python module '_multiprocessing' to build" 
+   echo "See: http://trac.sagemath.org/sage_trac/ticket/8440"
+   cp patches/setup.py src
+   if [ $? -ne 0 ]; then
+      echo >&2 "Failed to apply the Solaris patch needed for"
+      echo >&2 "http://trac.sagemath.org/sage_trac/ticket/8440"
+      exit 1
+   fi
+fi 
+
+
+cp patches/locale.py src/Lib/locale.py
+if [ $? -ne 0 ]; then
+    echo >&2 "Error copying patched locale.py"
+    exit 1
 fi
 
-patch -p0 < patches/Lib.distutils.command.sdist.patch
+cp patches/Makefile.pre.in src/Makefile.pre.in
 if [ $? -ne 0 ]; then
-    echo "Error copying patched sdist.py"
+    echo >&2 "Error copying patched Makefile.pre.in"
     exit 1
 fi
 
-patch -p0 < patches/Lib.socket.patch
+cp patches/sdist.py src/Lib/distutils/command/sdist.py
 if [ $? -ne 0 ]; then
-    echo "Error copying patched socket.py"
+    echo >&2 "Error copying patched sdist.py"
     exit 1
 fi
 
-patch -p0 < patches/dynamic_class_copyreg_py.patch
+cp patches/socket.py src/Lib/socket.py
 if [ $? -ne 0 ]; then
-    echo "Error copying patched pickle.py"
+    echo >&2 "Error copying patched socket.py"
     exit 1
 fi
 
-patch -p0 < patches/dynamic_class_copyreg_c.patch
+cp patches/pickle.py src/Lib/pickle.py
 if [ $? -ne 0 ]; then
-    echo "Error copying patched cPickle.c"
+    echo >&2 "Error copying patched pickle.py"
     exit 1
 fi
 
+cp patches/cPickle.c src/Modules/cPickle.c
+if [ $? -ne 0 ]; then
+    echo >&2 "Error copying patched cPickle.c"
+    exit 1
+fi
+
+# Due to a problem with _socket not building on OpenSolaris on x64
+# see http://bugs.python.org/issue8852
+# http://trac.sagemath.org/sage_trac/ticket/9041
+# http://trac.sagemath.org/sage_trac/ticket/9022
+# Modules/socketmodule.c needs patching. The patch consists of 
+# only checking if things are defined before trying to build with them
+# so it is safe (and desirable) on any platform. 
+
+cp patches/Modules.socketmodule.c src/Modules/socketmodule.c
+if [ $? -ne 0 ]; then
+    echo >&2 "Error copying patched socketmodule.c"
+    exit 1
+fi
+
+# The following patch for fixing broken readline behavior on Itanium
+# Linux definitely does *not* work on anything else.
+if [ "`uname -m`" = "ia64" -a "`uname`" = "Linux" ]; then
+    echo "Updating readline.c for Linux/Itanium"
+    cp patches/readline.c-Itanium-fix src/Modules/readline.c
+else
+    # Readline patch: http://bugs.python.org/file14599/python-2.6-readline.patch
+    # Associated bug: http://bugs.python.org/issue5833
+    #
+    # Committed to Python as r75747 in the py26-maint branch, but not
+    # in time for 2.6.4 -- so we can remove this patch the next time
+    # we update Python in Sage.
+    cp patches/readline.c-spacebug src/Modules/readline.c
+fi
+
+if [ $? -ne 0 ]; then
+    echo >&2 "Error copying patched readline.c"
+    exit 1
+fi
+
+
 # We are setting LDFLAGS and CPPFLAGS so that we pick up Sage's readline
 LDFLAGS="-L$SAGE_LOCAL/lib $LDFLAGS"
 export LDFLAGS
@@ -62,6 +139,23 @@
     EXTRAFLAGS="--without-pymalloc"; export EXTRAFLAGS
 fi
 
+# Program around weird bug in build process:
+#      Apparently if you have this:
+#         export DISTUTILS_DEBUG=1
+#      in your environment variables, the build craps out.  No idea why this
+#       is.
+#       -- Yi Qiang
+#
+# This bug was fixed in Python, but not yet in Python 2.6.4. So this fix
+# can be removed the next time we upgrade our version of Python. See
+#
+#   http://bugs.python.org/issue6954
+#
+# for the fix.
+#
+unset DISTUTILS_DEBUG
+
+
 cd src
 
 touch Include/*
@@ -93,27 +187,30 @@
             --enable-unicode=ucs4
         fi
     else
-        ./configure $EXTRAFLAGS --prefix="$SAGE_LOCAL"  --enable-unicode=ucs4 CC="$CC $CFLAGS" CXX="$CXX $CXXFLAGS"
+        ./configure $EXTRAFLAGS --prefix="$SAGE_LOCAL"  --enable-unicode=ucs4 \
+            CC="$CC $CFLAGS" CXX="$CXX $CXXFLAGS"
     fi
 
 
     if [ $? -ne 0 ]; then
-        echo "Error configuring Python."
+        echo >&2 "Error configuring Python."
         exit 1
     fi
 
     $MAKE
     if [ $? -ne 0 ]; then
-        echo "Error building Python."
+        echo >&2 "Error building Python."
         exit 1
     fi
 
     # running 'make install' in parallel is a bad, bad idea
+    # FIXME: The proper way to disable parallel make is to use
+    #        $MAKE -j1 ... (We rely on GNU make anyway).
     MAKE=make; export MAKE
     # the "-i" is crucial, esp. in the case of a major upgrade
     make -i install
     if [ $? -ne 0 ]; then
-        echo "Error installing Python."
+        echo >&2 "Error installing Python."
         exit 1
     fi
 }
@@ -122,27 +219,28 @@
 # informative error message. This is helps in determining why the
 # configuration, compilation or installation failed. So put this before the
 # build() function.
-set +e
+set +e # This is redundant here, but doesn't hurt to keep it... ;-)
 
 build
 
-cd $SAGE_LOCAL/lib
+cd "$SAGE_LOCAL/lib"
 
 # move the python directory if we're upgrading from a version
-# of sage with python 2.6
-if [ -d python2.6/site-packages ]; then
-   mv python2.6/site-packages python2.7/site-packages-old
+# of sage with python 2.5
+if [ -d python2.5/site-packages ]; then
+   mv python2.5/site-packages python2.6/site-packages-old
 fi
 
-rm -rf python/python2.7 python/python2.6 python/python2.5 python/python python python2.4 python2.5
-ln -s python2.7 python
+rm -rf python/python2.6 python/python2.5 python/python python python2.4 python2.5
+ln -s python2.6 python
 if [ $? -ne 0 ]; then
-    echo "Error creating symbolic link"
+    echo >&2 "Error creating symbolic link"
     exit 1
 fi
 
 # Sleeping for three seconds so that parallel 'make install' catches up
 # with the following test.
+# XXX We have disabled parallel 'make install' above, but never mind.
 echo "Sleeping for three seconds before testing python"
 sleep 3
 
@@ -150,12 +248,28 @@
 # All these modules are important and if any one 
 # fails to build, Sage will not work. 
 
+import_errors=false
 for module in math hashlib crypt ; do 
    "$SAGE_LOCAL/bin/python" -c "import $module"
    if [ $? -eq 0 ] ; then
       echo "$module module imported OK"
    else
-      echo "$module module failed to import"
-      exit 1
+      echo >&2 "$module module failed to import"
+      import_errors=true
+      # exit 1 # not yet
    fi
 done
+
+if $import_errors; then
+    echo >&2 "Error: One or more modules failed to import."
+    # Check if we are on Debian or one of its derivatives:
+    if command -v dpkg && ! command -v dpkg-architecture >/dev/null; then
+        echo >&2 "You may have to install 'dpkg-architecture'"
+        echo >&2 "which is part of the Debian package 'dpkg-dev'."
+        echo >&2 "Try installing it by typing"
+        echo >&2 "    sudo apt-get install dpkg-dev"
+        echo >&2 "and rerun 'make'."
+    fi
+    exit 1
+fi
+
```



---

Comment by fbissey created at 2011-11-04 02:07:13

OK that's not a biggy while I had a look at #11447 I made my spkg before it was closed and possibly before it had reached its final shape. I wanted to wait for 2.7.3 but I will probably cut a 2.7.2 in which I will add this then. 

I am keen to have this landing ASAP but I would understand if the release manager only wants to do it in a alpha0. That's both a big change and a big patch set. My concern is that my last patch may not be adequate. Steve tested a number of configurations and the order this comes out are all over the place. I may have to make it random which is not nice.

The other concern is #11986 which looks like a blast from the past and I have no clues on either of them.


---

Comment by jdemeyer created at 2011-11-04 09:24:20

Replying to [comment:138 fbissey]:
> OK that's not a biggy while I had a look at #11447 I made my spkg before it was closed and possibly before it had reached its final shape. I wanted to wait for 2.7.3 but I will probably cut a 2.7.2 in which I will add this then. 
> 
> I am keen to have this landing ASAP but I would understand if the release manager only wants to do it in a alpha0. That's both a big change and a big patch set.

If you can finish it, I'd be happy to merge it.  But to be realistic, I don't think this ticket is close to being finished.  There is a huge amount of patches which needs to be reviewed, there is still #11986, there is the rebasing to #11447, maybe testing will reveal breakage on some systems...


---

Comment by jdemeyer created at 2011-11-04 10:10:57

There is a warning when building the reference manual:

```
docstring of sage.crypto.boolean_function:3: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
```



---

Comment by jdemeyer created at 2011-11-05 21:41:43

Another minor comment: please use UTF8 in `SPKG.txt`.  Currently, "François" is encoded as latin1.


---

Comment by jdemeyer created at 2011-11-05 22:14:54

By the way: Python 2.7.2 was released on June 11th, 2011 so you might as well go for that.


---

Comment by fbissey created at 2011-11-05 22:25:24

Replying to [comment:144 jdemeyer]:
> By the way: Python 2.7.2 was released on June 11th, 2011 so you might as well go for that.

sage-5.0 is probably more realistic. Thanks for the useful comments, I hadn't seen the warnings in the documentation, this probably could be spun out of this ticket as it is probably a problem in the existing doc - just silent with the current python. I really would like to go to 2.7.3 when it comes out but I'll make a stop 2.7.2. I have a heavy workload this week but I'll try to put the spkg together. I know from sage-on-gentto that there will be some more patching to be done unfortunately although in some case I think that would be just a band aid. So more dependencies may appear :(

I am surprised at the "latin-1" encoding I am defaulting to UTF-8 and even my Changelogs now come correct everywhere.

We need someone with the know how to look at #11986.


---

Comment by jdemeyer created at 2011-11-09 08:39:10

Replying to [comment:145 fbissey]:
> Replying to [comment:144 jdemeyer]:
> > By the way: Python 2.7.2 was released on June 11th, 2011 so you might as well go for that.
> 
> sage-5.0 is probably more realistic.
Especially since William essentially _defined_ sage-5.0 as the release which will contain this ticket.

> I hadn't seen the warnings in the documentation, this probably could be spun out of this ticket as it is probably a problem in the existing doc - just silent with the current python.
True, but I have no idea how Python 2.7 has changed this particular doctest.  It could also be that something changed inside Sphinx or Cython because of Python 2.7.

> I am surprised at the "latin-1" encoding I am defaulting to UTF-8 and even my Changelogs now come correct everywhere.
And now you're punished for the rest of your live as a developer because your name is not ASCII (and please don't write "Francois", that just looks very wrong).

> We need someone with the know how to look at #11986.
I _might_ have a look, but I don't want to promise anything.  In any case, once #11986 is really the only remaining issue, it will certainly get fixed.


---

Comment by fbissey created at 2011-11-10 02:53:04

All right. Very busy week so far. I am removing the last patch and will spin it in a separate ticket because Steve did more testing and it appears that the test is somewhat random and was only working everywhere the same with python 2.6 by sheer luck. 

Steve had a few interesting suggestions for replacing the test but that's clearly another ticket on which we'll forward people who touched that file for comments.


---

Comment by fbissey created at 2011-11-21 00:55:23

I finished updating the spkg to 2.7.2 in a moment of freedom. I called it 2.7.2.p0 as it has some patches in it. Hope all the permissions are right this time. And SPKG.txt is UTF-8 now.

I will need to update one patch and I think add a new one. At least relative to 4.7.2, I am so bogged down in work that I haven't been working at all on 4.8.0 which may require new patches.


---

Comment by fbissey created at 2011-11-24 21:33:39

fix pure assertErrors failures - updated for python-2.7.2


---

Attachment

fix sage_unittest.py failures - updated for python-2.7.2


---

Attachment

Patch set updated for python-2.7.2.


---

Comment by jdemeyer created at 2011-11-25 22:51:12

Replying to [comment:148 fbissey]:
> I finished updating the spkg to 2.7.2 in a moment of freedom. I called it 2.7.2.p0 as it has some patches in it. Hope all the permissions are right this time.
Unfortunately, they are not.  I fixed this in [http://boxen.math.washington.edu/home/jdemeyer/spkg/python-2.7.2.p0.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/python-2.7.2.p0.spkg)


---

Comment by fbissey created at 2011-11-25 23:19:25

Replying to [comment:151 jdemeyer]:
> Replying to [comment:148 fbissey]:
> > I finished updating the spkg to 2.7.2 in a moment of freedom. I called it 2.7.2.p0 as it has some patches in it. Hope all the permissions are right this time.
> Unfortunately, they are not.  I fixed this in [http://boxen.math.washington.edu/home/jdemeyer/spkg/python-2.7.2.p0.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/python-2.7.2.p0.spkg)

OK. Was it the src folder and its content? Or did I forget something else in the spkg root folder?


---

Comment by jdemeyer created at 2011-11-25 23:24:38

Replying to [comment:153 fbissey]:
> OK. Was it the src folder and its content?
Yes.  I solved this by doing `chmod ugo+rX -R .`

> Or did I forget something else in the spkg root folder?
Also, yes.  spkg-check should be executable.


---

Comment by jdemeyer created at 2011-11-25 23:36:05

This fails to build from scratch with sage-4.8.alpha2 on sage.math:

```
gcc  -pthread -DNDEBUG -g  -O3 -Wall -Wstrict-prototypes -L/scratch/jdemeyer/merger/sage-5.0/local/lib   Parser/acceler.o Parser/grammar1.
o Parser/listnode.o Parser/node.o Parser/parser.o Parser/parsetok.o Parser/bitset.o Parser/metagrammar.o Parser/firstsets.o Parser/grammar
.o Parser/pgen.o Objects/obmalloc.o Python/mysnprintf.o Python/pyctype.o Parser/tokenizer_pgen.o Parser/printgrammar.o Parser/pgenmain.o -
lpthread -ldl  -lutil -o Parser/pgen
Parser/pgen ./Grammar/Grammar ./Include/graminit.h ./Python/graminit.c
touch Parser/pgen.stamp
gcc  -pthread -c -fno-strict-aliasing -g -O2 -DNDEBUG -g  -O3 -Wall -Wstrict-prototypes  -I. -IInclude -I./Include -I/scratch/jdemeyer/mer
ger/sage-5.0/local/include  -fPIC -DPy_BUILD_CORE -o Python/ast.o Python/ast.c
gcc  -pthread -c -fno-strict-aliasing -g -O2 -DNDEBUG -g  -O3 -Wall -Wstrict-prototypes  -I. -IInclude -I./Include -I/scratch/jdemeyer/mer
ger/sage-5.0/local/include  -fPIC -DPy_BUILD_CORE -o Python/compile.o Python/compile.c
gcc  -pthread -c -fno-strict-aliasing -g -O2 -DNDEBUG -g  -O3 -Wall -Wstrict-prototypes  -I. -IInclude -I./Include -I/scratch/jdemeyer/mer
ger/sage-5.0/local/include  -fPIC -DPy_BUILD_CORE -o Python/graminit.o Python/graminit.c
gcc  -pthread -c -fno-strict-aliasing -g -O2 -DNDEBUG -g  -O3 -Wall -Wstrict-prototypes  -I. -IInclude -I./Include -I/scratch/jdemeyer/mer
ger/sage-5.0/local/include  -fPIC -DPy_BUILD_CORE -o Python/symtable.o Python/symtable.c
gcc  -pthread -c -fno-strict-aliasing -g -O2 -DNDEBUG -g  -O3 -Wall -Wstrict-prototypes  -I. -IInclude -I./Include -I/scratch/jdemeyer/mer
ger/sage-5.0/local/include  -fPIC -DPy_BUILD_CORE \
              -DSVNVERSION="\"`LC_ALL=C svnversion .`\"" \
              -DHGVERSION="\"`LC_ALL=C hg id -i .`\"" \
              -DHGTAG="\"`LC_ALL=C hg id -t .`\"" \
              -DHGBRANCH="\"`LC_ALL=C hg id -b .`\"" \
              -o Modules/getbuildinfo.o ./Modules/getbuildinfo.c
You must compile Sage first using 'make' in the Sage root directory.
You must compile Sage first using 'make' in the Sage root directory.
You must compile Sage first using 'make' in the Sage root directory.
<command-line>: warning: missing terminating " character
<command-line>:1:7: warning: missing terminating " character
<command-line>:2:10: warning: missing terminating " character
./Modules/getbuildinfo.c: In function 'Py_GetBuildInfo':
./Modules/getbuildinfo.c:45: error: missing terminating " character
./Modules/getbuildinfo.c:45: error: expected expression before ')' token
./Modules/getbuildinfo.c:46: error: missing terminating " character
./Modules/getbuildinfo.c:46: error: missing terminating " character
./Modules/getbuildinfo.c:47: error: missing terminating " character
./Modules/getbuildinfo.c:47: error: missing terminating " character
./Modules/getbuildinfo.c:53: error: 'buildinfo' undeclared (first use in this function)
./Modules/getbuildinfo.c:53: error: (Each undeclared identifier is reported only once
./Modules/getbuildinfo.c:53: error: for each function it appears in.)
./Modules/getbuildinfo.c: In function '_Py_hgversion':
./Modules/getbuildinfo.c:72: error: missing terminating " character
./Modules/getbuildinfo.c:72: warning: 'return' with no value, in function returning non-void
./Modules/getbuildinfo.c: In function '_Py_hgidentifier':
./Modules/getbuildinfo.c:79: error: missing terminating " character
./Modules/getbuildinfo.c:79: error: expected expression before ';' token
./Modules/getbuildinfo.c:83: error: missing terminating " character
./Modules/getbuildinfo.c:83: error: expected expression before ';' token
make[2]: *** [Modules/getbuildinfo.o] Error 1
make[2]: Leaving directory `/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/spkg/build/python-2.7.2.p0/src'
Error building Python.
```


Mhy guess would be that `spkg-install` is trying to run Mercurial or something, which obviously fails because Mercurial has not been compiled yet (and it can't since it depends on Python).


---

Comment by jdemeyer created at 2011-11-25 23:50:15

The error above might be fixed by #5852...


---

Comment by jhpalmieri created at 2011-11-26 00:23:04

The current spkg installs fine on OS X 10.6 and 10.7, at least when I do "sage -f ..." in an existing Sage installation.  I haven't tried building from scratch, and I haven't tried doctests or the patches yet.  Would it be possible to provide a single large patch in addition to the individual small ones?  That would be easier to apply for testing, while the small ones are easier to review.


---

Comment by fbissey created at 2011-11-26 00:33:04

Replying to [comment:154 jdemeyer]:
> Replying to [comment:153 fbissey]:
> > OK. Was it the src folder and its content?
> Yes.  I solved this by doing `chmod ugo+rX -R .`
> 
> > Or did I forget something else in the spkg root folder?
> Also, yes.  spkg-check should be executable.
Never used symbolic mode of chmod, always octal. But this looks like it is more effective to get the directory permissions right. Darn spkg-check.

Thanks for the tips. Sorry for being a pest at times.

I haven't tested the spkg from scratch on OSX I did on linux x86_64 and 4.8.alpha2.
I will see what happens on my 10.5 machine later. 2.7.1 worked from scratch there i am sure. That looks very strange, can you link the full python building log?


---

Comment by jhpalmieri created at 2011-11-26 03:28:00

A build from scratch on OS X 10.6 worked just fine, by the way.


---

Comment by jdemeyer created at 2011-11-26 09:32:44

There is still the docbuild warning:

```
docstring of sage.crypto.boolean_function:3: WARNING: Block quote ends without a blank line; unexpected unindent.
```

I am investigating.


---

Comment by jdemeyer created at 2011-11-26 10:07:15

I absolutely do not understand the docbuild warning but created a ticket at #12085.


---

Comment by fbissey created at 2011-11-26 18:50:52

Just an idea! This is because it wants to execute some mercurial commands to find if there are tags in the source. If we were to set 

```
DHGVERSION
DHGTAG
DHGBRANCH
```

To something or even nothing we may not have this problem. A normal run with a system mercurial installed looks like:

```
x86_64-pc-linux-gnu-gcc -pthread -c -fno-strict-aliasing -O2 -pipe -march=native -fwrapv -DNDEBUG   -I. -IInclude -I./Include  -fPIC -DPy_BUILD_CORE \
      -DSVNVERSION="\"`LC_ALL=C svnversion .`\"" \
      -DHGVERSION="\"`LC_ALL=C hg id -i .`\"" \
      -DHGTAG="\"`LC_ALL=C hg id -t .`\"" \
      -DHGBRANCH="\"`LC_ALL=C hg id -b .`\"" \
      -o Modules/getbuildinfo.o ./Modules/getbuildinfo.c
abort: repository . not found!
abort: repository . not found!
abort: repository . not found!
```

I will try to see if I can fit that in the spkg.


---

Comment by jdemeyer created at 2011-11-26 18:55:47

Replying to [comment:163 fbissey]:
> I will try to see if I can fit that in the spkg.

No, I would leave that alone.  With #5852, it will build properly.  Since you get errors anyway with the system Mercurial, apparently it's not a problem that `hg` fails.


---

Comment by fbissey created at 2011-11-26 19:03:41

If you insist but it would be easy to path Makefile.pre.in to prevent this from happening. It is mainly used to get pre-release version info if you checked out python source from hg. It is supposed to fail if you are using a properly released tarball.


---

Comment by jdemeyer created at 2011-11-26 19:53:06

Replying to [comment:165 fbissey]:
> If you insist
I will *not* insist: if you want to make the patch, go ahead.


---

Comment by fbissey created at 2011-11-26 20:51:59

I may try something more subtle first. Makefile.pre.in has

```
SVNVERSION=	@SVNVERSION@
HGVERSION=	@HGVERSION@
HGTAG=		@HGTAG@
HGBRANCH=	@HGBRANCH@
```

and

```
	$(CC) -c $(PY_CFLAGS) \
	      -DSVNVERSION="\"`LC_ALL=C $(SVNVERSION)`\"" \
	      -DHGVERSION="\"`LC_ALL=C $(HGVERSION)`\"" \
	      -DHGTAG="\"`LC_ALL=C $(HGTAG)`\"" \
	      -DHGBRANCH="\"`LC_ALL=C $(HGBRANCH)`\"" \
	      -o $@ $(srcdir)/Modules/getbuildinfo.c
```

later so exporting HG* to something like /bin/true on non-windows OS would presumably solve the problem. But just patching to pass empty strings in the later would probably be safe everywhere.


---

Comment by fbissey created at 2011-12-05 02:18:31

The first patch doesn't apply in 4.8.alpha3 because of the changes in #12047. New patches will come some. There may be other surprises.


---

Comment by fbissey created at 2011-12-05 11:04:50

Updated the first patch. Haven't been able to test things to find any new problems yet.


---

Comment by jdemeyer created at 2011-12-05 11:25:12

There are a few test failures on a Pentium 4 32-bit Linux system with sage-4.8.alpha2 + #9958 + #11986:

```
sage -t  --long -force_lib devel/sage/sage/combinat/words/suffix_trees.py
**********************************************************************
File "/home/jdemeyer/sage-5.0/devel/sage-main/sage/combinat/words/suffix_trees.py", line 1323:
    sage: t.trie_type_dict() == dict([[(0, W("a")), 4], [(0, W("b")), 3], [(3, W("a")), 2], [(4, W("b")), 5], [(5, W("a")), 1]])
Expected:
    True
Got:
    False
**********************************************************************
sage -t  --long -force_lib devel/sage/sage/misc/randstate.pyx
**********************************************************************
File "/home/jdemeyer/sage-5.0/devel/sage-main/sage/misc/randstate.pyx", line 61:
    sage: rtest()
Expected:
    (978, 0.184109262667515, -3*x^2 - 1/12, (4,5), [ 0, 1, 1, 0, 0 ], 1161603091, 60359, 0.83350776541997362)
Got:
    (978, 0.184109262667515, -3*x^2 - 1/12, (4,5), [ 0, 1, 1, 0, 0 ], 1161603091, 60359, 0.8335077654199736)
**********************************************************************
sage -t  --long -force_lib devel/sage/sage/combinat/words/nfactor_enumerable_word.py
**********************************************************************
File "/home/jdemeyer/sage-5.0/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py", line 20:
    sage: it.next()
Expected:
    word: 6456
Got:
    word: 4564
**********************************************************************
File "/home/jdemeyer/sage-5.0/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py", line 23:
    sage: it.next()
Expected:
    word: 5645
Got:
    word: 6456
**********************************************************************
File "/home/jdemeyer/sage-5.0/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py", line 26:
    sage: it.next()
Expected:
    word: 4564
Got:
    word: 5645
**********************************************************************
```



---

Comment by jdemeyer created at 2011-12-05 11:26:37

I have made a patch for the Integer hashing, see #11986.


---

Comment by fbissey created at 2011-12-05 11:48:50

I have seen your patch in #11986 that's a good rewrite of the hashing in question, the -1 bit is particularly tricky. I mentioned it before but we probably need a different approach for combinat/words/nfactor_enumerable_word.py, the sequence is pretty much random depending on arch and other factors it seems. The randstate.pyx must have escaped [http://trac.sagemath.org/sage_trac/attachment/ticket/9958/trac_9958-fixing_numericalnoise-part4.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9958/trac_9958-fixing_numericalnoise-part4.patch) because the test results are identical to some performed later in the same file. I'll correct that shortly. 

The suffix_trees.pyx rings a bell but I cannot remember where and when.


---

Comment by fbissey created at 2011-12-05 11:51:17

ha [http://trac.sagemath.org/sage_trac/ticket/9958#comment:18](http://trac.sagemath.org/sage_trac/ticket/9958#comment:18) is where I had suffix_trees.pyx before. I don't have a 32 bit linux box anymore so it is more difficult. I note they were two you only see one now.


---

Comment by fbissey created at 2011-12-05 21:18:00

I need a kind soul with 32 bit linux system to explore the suffix tree issue, the doctest is as follow:

```
            sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree, SuffixTrie
            sage: W = Words("ab")
            sage: t = ImplicitSuffixTree(W("aba"))
            sage: t.trie_type_dict() == dict([[(0, W("a")), 4], [(0, W("b")), 3], [(3, W("a")), 2], [(4, W("b")), 5], [(5, W("a")), 1]])
            True
```

It would be helpful to get the values of "W", "t" and "t.trie_type_dict()" on python-2.6 and 2.7. Then we can make a decision on whether the answer we get with python-2.7 is equivalent to the current output or not.


---

Comment by strogdon created at 2011-12-05 21:57:54

Here (x86) with sage-4.8.alpha3 + #9958 + #11986 the suffix_trees test passes:


```
./sage -t  -long -force_lib devel/sage/sage/combinat/words/suffix_trees.py
sage -t -long -force_lib "devel/sage/sage/combinat/words/suffix_trees.py"
         [5.1 s]
 
----------------------------------------------------------------------
All tests passed!
```


The requested values are:


```
sage: W
Words over Ordered Alphabet ['a', 'b']
sage: t
Implicit Suffix Tree of the word: aba
sage: t.trie_type_dict()
{(4, word: b): 5, (0, word: a): 4, (0, word: b): 3, (5, word: a): 1, (3, word: a): 2}
```


FWIW, on amd64 the test fails with the same sage-4.8.alpha3 + #9958 + #11986


---

Comment by jdemeyer created at 2011-12-05 22:20:33

On sage.math (x86_64 Linux), sage-4.8.alpha3 + #12106 (unrelated) + #9958 + #11986 gives errors in two files:

```
sage -t  -force_lib devel/sage/sage/matrix/matrix_mod2e_dense.pyx
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/devel/sage-main/sage/matrix/matrix_mod2e_dense.pyx", line 790:
    sage: float(A.density())
Expected:
    0.099738...
Got:
    0.099739
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/devel/sage-main/sage/matrix/matrix_mod2e_dense.pyx", line 798:
    sage: float(A.density())
Expected:
    0.499759...
Got:
    0.49976
**********************************************************************
```

(related ticket: #9562)
and

```
sage -t  -force_lib devel/sage/sage/gsl/integration.pyx
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/devel/sage-main/sage/gsl/integration.pyx", line 110:
    sage: numerical_integral(x^2, 0, 1, max_points=100)
Expected:
    (0.33333333333333331, 3.7007434154171879e-15)
Got:
    (0.3333333333333333, 3.700743415417188e-15)
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/devel/sage-main/sage/gsl/integration.pyx", line 115:
    sage: numerical_integral(sin(x)^3 + sin(x),  0, pi)
Expected:
    (3.333333333333333, 3.7007434154171883e-14)
Got:
    (3.333333333333333, 3.700743415417188e-14)
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/devel/sage-main/sage/gsl/integration.pyx", line 120:
    sage: numerical_integral(lambda x: sin(x)^3 + sin(x),  0, pi)
Expected:
    (3.333333333333333, 3.7007434154171883e-14)
Got:
    (3.333333333333333, 3.700743415417188e-14)
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/devel/sage-main/sage/gsl/integration.pyx", line 131:
    sage: numerical_integral(f, 0, 1, max_points=200, eps_abs=1e-7, eps_rel=1e-7, rule=4)
Expected:
    (0.33333333333333331, 3.7007434154171879e-15)
Got:
    (0.3333333333333333, 3.700743415417188e-15)
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/devel/sage-main/sage/gsl/integration.pyx", line 172:
    sage: exp(-1/x).nintegral(x, 1, 2)  # via maxima
Expected:
    (0.50479221787318396, 5.6043194293440752e-15, 21, 0)
Got:
    (0.504792217873184, 5.604319429344075e-15, 21, 0)
**********************************************************************
```

(related ticket: #12047)

Also, the spkg should be rebased to #12096.


---

Comment by jdemeyer created at 2011-12-05 22:24:02

I get on 32-bit i386 Linux with sage-4.8.alpha2 + various patches including #9958:

```
sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree, SuffixTrie
sage: W = Words("ab")
sage: t = ImplicitSuffixTree(W("aba"))
sage: W
Words over Ordered Alphabet ['a', 'b']
sage: t
Implicit Suffix Tree of the word: aba
sage: t.trie_type_dict()
{(4, word: a): 1, (0, word: b): 5, (0, word: a): 3, (5, word: a): 2, (3, word: b): 4}
```



---

Comment by fbissey created at 2011-12-05 22:52:27

thanks for all that feedback. I knew there would be new stuff. I unfortunately (like all of us) not enough time to do things in a speedy fashion. I am bogged down as well with the sage-on-gentoo version of alpha3 not wanting to play nice with #4260 [https://github.com/cschwan/sage-on-gentoo/issues/108](https://github.com/cschwan/sage-on-gentoo/issues/108) and it annoys me.


---

Comment by jdemeyer created at 2011-12-05 22:59:35

Replying to [comment:180 fbissey]:
> I am bogged down as well with the sage-on-gentoo version of alpha3 not wanting to play nice with #4260 [https://github.com/cschwan/sage-on-gentoo/issues/108](https://github.com/cschwan/sage-on-gentoo/issues/108) and it annoys me.

Does vanilla Sage build and run on that same machine with the same compiler?  Be sure to try a different gcc version, Linbox seems to be sensitive to that.


---

Comment by strogdon created at 2011-12-05 23:09:44

On x86 with sage-4.8.alpha3 + #9958 + #11986 I have the following failures:


```
sage -t -long  -force_lib devel/sage-main/sage/gsl/integration.pyx
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/gsl/integration.pyx", line 110:
    sage: numerical_integral(x^2, 0, 1, max_points=100)
Expected:
    (0.33333333333333331, 3.7007434154171879e-15)
Got:
    (0.3333333333333333, 3.700743415417188e-15)
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/gsl/integration.pyx", line 115:
    sage: numerical_integral(sin(x)^3 + sin(x),  0, pi)
Expected:
    (3.333333333333333, 3.7007434154171883e-14)
Got:
    (3.333333333333333, 3.700743415417188e-14)
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/gsl/integration.pyx", line 120:
    sage: numerical_integral(lambda x: sin(x)^3 + sin(x),  0, pi)
Expected:
    (3.333333333333333, 3.7007434154171883e-14)
Got:
    (3.333333333333333, 3.700743415417188e-14)
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/gsl/integration.pyx", line 131:
    sage: numerical_integral(f, 0, 1, max_points=200, eps_abs=1e-7, eps_rel=1e-7, rule=4)
Expected:
    (0.33333333333333331, 3.7007434154171879e-15)
Got:
    (0.3333333333333333, 3.700743415417188e-15)
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/gsl/integration.pyx", line 172:
    sage: exp(-1/x).nintegral(x, 1, 2)  # via maxima
Expected:
    (0.50479221787318396, 5.6043194293440752e-15, 21, 0)
Got:
    (0.504792217873184, 5.604319429344075e-15, 21, 0)
**********************************************************************
```


```
sage -t -long  -force_lib devel/sage-main/sage/misc/randstate.pyx
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/misc/randstate.pyx", line 61:
    sage: rtest()
Expected:
    (978, 0.184109262667515, -3*x^2 - 1/12, (4,5), [ 0, 1, 1, 0, 0 ], 1161603091, 60359, 0.83350776541997362)
Got:
    (978, 0.184109262667515, -3*x^2 - 1/12, (4,5), [ 0, 1, 1, 0, 0 ], 1161603091, 60359, 0.8335077654199736)
**********************************************************************
```


```
sage -t -long  -force_lib devel/sage-main/sage/matrix/matrix_mod2e_dense.pyx
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/matrix/matrix_mod2e_dense.pyx", line 790:
    sage: float(A.density())
Expected:
    0.099738...
Got:
    0.099739
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/matrix/matrix_mod2e_dense.pyx", line 798:
    sage: float(A.density())
Expected:
    0.499759...
Got:
    0.49976
**********************************************************************
```


```
sage -t -long  -force_lib devel/sage-main/sage/functions/transcendental.py
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/functions/transcendental.py", line 80:
    sage: w = exponential_integral_1(2,4); w
Expected:
    [0.04890051070806112, 0.0037793524098489067, 0.00036008245216265873, 3.7665622843924751e-05]
Got:
    [0.04890051070806112, 0.0037793524098489067, 0.00036008245216265873, 3.766562284392475e-05]
**********************************************************************
```



---

Comment by fbissey created at 2011-12-06 00:43:17

I now understand why you removed the transcendental patch Jereon some bits ended in my revised trac_9958-fixing_numericalnoise-part1_p2.patch when they shouldn't have. That's what is happening to Steve. I will rectify that. 

I removed the gsl bits because of #12047 so that has to be redone.

And I haven't had time to try vanilla yet but it is on my TODO list and I suspect g++ too.


---

Comment by fbissey created at 2011-12-06 00:53:36

fixing numerical noise part 1 - updated for 4.8.alpha3


---

Attachment

updated the first patch and readded the transcendental patch to the list.


---

Comment by fbissey created at 2011-12-06 01:35:48

For suffix_tree it looks like your two values don't agree:

```
{(4, word: a): 1, (0, word: b): 5, (0, word: a): 3, (5, word: a): 2, (3, word: b): 4}
{(4, word: b): 5, (0, word: a): 4, (0, word: b): 3, (5, word: a): 1, (3, word: a): 2}
```

If we add that I don't see it on OS X x86 that looks bad. I also have an x86_64 machine where the value is the same as Jeroen and the test fails. Steve get the right value on the other hand so there is something going there.


---

Attachment

fix numerical noise in gsl/integration.pyx


---

Attachment

fix numerical noise introduced by m4rie


---

Comment by fbissey created at 2011-12-06 01:40:27

Added two new patches for gsl integration and m4rie tickets merged in 4.8.alpha3.


---

Comment by fbissey created at 2011-12-06 03:41:00

Rebased the spkg against #12096.


---

Attachment

Diff for the Python spkg, for review only


---

Comment by jdemeyer created at 2011-12-06 17:19:36

Everything passes against sage-4.8.alpha3 on 64bit.  Yay!


---

Comment by fbissey created at 2011-12-06 19:45:41

I forgot to add a new bit for randstate.pyx on 32 bit. I'll do that later but I know it is missing. Should we involve someone from combinatronics to get to the bottom of suffix_tree and nfactor_enumerate_word?


---

Comment by jdemeyer created at 2011-12-06 19:55:47

Replying to [comment:189 fbissey]:
> Should we involve someone from combinatronics to get to the bottom of suffix_tree and nfactor_enumerate_word?
Sounds good, try to send an email to sage-devel.


---

Comment by strogdon created at 2011-12-06 20:21:24

For the sake of completeness, I now have

32bit: one failure


```
sage -t -long  -force_lib devel/sage-main/sage/misc/randstate.pyx
```

which was mentioned above.

64bit: two failures


```

sage -t -long  -force_lib devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/combinat/words/nfactor_enumerable
_word.py", line 20:
    sage: it.next()
Expected:
    word: 5645
Got:
    word: 4564
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/combinat/words/nfactor_enumerable
_word.py", line 23:
    sage: it.next()
Expected:
    word: 6456
Got:
    word: 5645
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/combinat/words/nfactor_enumerable
_word.py", line 26:
    sage: it.next()
Expected:
    word: 4564
Got:
    word: 6456
**********************************************************************


sage -t -long  -force_lib devel/sage-main/sage/combinat/words/suffix_trees.py
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/combinat/words/suffix_trees.py",
line 1323:
    sage: t.trie_type_dict() == dict([[(0, W("a")), 4], [(0, W("b")), 3], [(3, W("a")), 2]
, [(4, W("b")), 5], [(5, W("a")), 1]])
Expected:
    True
Got:
    False
**********************************************************************
```

which have been mentioned previously.


---

Comment by jdemeyer created at 2011-12-06 20:53:53

This ticket made me notice a bug with the L-series of Eisenstein series: #12124.  With that ticket applied, the patch to `sage/modular/modform/eis_series.py` here can be removed.


---

Comment by hivert created at 2011-12-07 22:27:56

First of all, I'm not an expert of combinatorics on word. So I'd rather
Sebastien Labbe to jump in the discussion. I just trying to help.

> 64bit: two failures

```
sage -t -long  -force_lib devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/combinat/words/nfactor_enumerable
_word.py", line 20:
    sage: it.next()
Expected:
    word: 5645
Got:
    word: 4564
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/combinat/words/nfactor_enumerable
_word.py", line 23:
    sage: it.next()
Expected:
    word: 6456
Got:
    word: 5645
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/combinat/words/nfactor_enumerable
_word.py", line 26:
    sage: it.next()
Expected:
    word: 4564
Got:
    word: 6456
**********************************************************************
```


This first failure is not a problem. The iterator here is extracted from a
dict of dict so it is not unexpected to have a random order. Fixing the test
of marking it at random should be ok. This test is an explanation for the
user, the real feature is tested further in the file.


> which have been mentioned previously.

```
{(4, word: a): 1, (0, word: b): 5, (0, word: a): 3, (5, word: a): 2, (3, word: b): 4}
{(4, word: b): 5, (0, word: a): 4, (0, word: b): 3, (5, word: a): 1, (3, word: a): 2}
```


This one is more tricky: As far as I understand, both result are perfectly
legible: the second is the same as the first after applying the following
cyclic permutation (3,4,5). The numbering is random. So (again as far as I
understand), the problem in only created by the cross-platform non-determinism
of the set/dict data structure. I'm not sure here what is the best fix.

Cheers,

Florent


---

Comment by fbissey created at 2011-12-08 00:52:06

Thank you Florent, that is helpful. We kind of worked out that word was OK but we thought we could have a better test. If you think that's ok to mark it random I think we'll do that with some explanation.

The fact that both output in suffix_tree are legit is good to know. We can probably work around that. We may even have a complete patch set by Monday, cross fingers.


---

Comment by jdemeyer created at 2011-12-09 21:42:14

Upgraded succesfully from sage-4.6.2, all tests pass except for the known problematic tests.


---

Comment by fbissey created at 2011-12-10 11:21:16

I'll work on the remaining tests tomorrow, I hope. I will remove the eis_series.py and see if I can review #12124 as well. I looks like the python spkg will need rebasing again with #12131.


---

Comment by jdemeyer created at 2011-12-10 20:27:46

Replying to [comment:196 fbissey]:
> I'll work on the remaining tests tomorrow, I hope.
That would be great!  I would love to see this finished in time, such that the next release can really be sage-5.0.


---

Attachment

test against more valid dictionaries in suffix_trees


---

Comment by fbissey created at 2011-12-10 22:13:27

fix all numerical noise in randstate


---

Attachment

fixing numerical noise part 1 - updated 20111211: separate randstate and eis_modn_series


---

Attachment

updating the patch set with a tentative solution for suffix_trees. It may not be exhaustive of all possible answers though. If we are going for it for the next release I can redo the python spkg to fix the lib/lib64 from #12131.

Putting to need review :)


---

Comment by fbissey created at 2011-12-10 22:22:11

Changing status from needs_work to needs_review.


---

Comment by slabbe created at 2011-12-10 22:54:59

Hi,

I just read randomly sage-devel (I was away from sage development for several weeks) and saw that the discussion about upgrading to 2.7 was having problem with some files I am related with (suffix_tree.py nfactor_enumerable_word.py). I still don't understand the dict problem for suffix tree (one minute was not enough). I will look into that to avoid similar problem in the future. If something else pops up in those file, I can do the fix next time.

Sébastien


---

Comment by fbissey created at 2011-12-10 23:03:54

Your input on the matter is welcome. According to Florent, the problem in suffix_trees is that there are several equivalent answers and some platforms now give a different one than the one you originally tested for. Note that we don't know what the trigger is for having a different answer it is not a 32/64 bit separation as we have seen both answers on the two kinds of systems.


---

Comment by fbissey created at 2011-12-11 00:51:33

Actually, you should have a look at what I did for both of these in [attachment:trac_9958-nfactor_enumerable_word-randomness.patch] and [attachment:trac_9958-suffix_trees-variations.patch]. If you could give your opinion on the patches or if you want to submit patches of your own it would be appreciated.


---

Comment by strogdon created at 2011-12-11 07:07:13

With the current update I have the following failures:


```
32bit
sage -t -long  -force_lib devel/sage-9958/sage/combinat/words/nfactor_enumerable_word
.py
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-9958/sage/combinat/words/nfactor_enume
rable_word.py", line 23:
    sage: it.next()
Expected:
    word: 6456     # random
Got:
    word: 6456
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-9958/sage/combinat/words/nfactor_enume
rable_word.py", line 25:
    sage: it.next()
Expected:
    word: 5645     # random
Got:
    word: 5645
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-9958/sage/combinat/words/nfactor_enume
rable_word.py", line 27:
    sage: it.next()
Expected:
    word: 4564     # random
Got:
    word: 4564
**********************************************************************

64bit

sage -t -long  -force_lib devel/sage-9958/sage/combinat/words/nfactor_enumerable_word
.py
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-9958/sage/combinat/words/nfactor_enume
rable_word.py", line 23:
    sage: it.next()
Expected:
    word: 6456     # random
Got:
    word: 4564
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-9958/sage/combinat/words/nfactor_enume
rable_word.py", line 25:
    sage: it.next()
Expected:
    word: 5645     # random
Got:
    word: 5645
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-9958/sage/combinat/words/nfactor_enume
rable_word.py", line 27:
    sage: it.next()
Expected:
    word: 4564     # random
Got:
    word: 6456
**********************************************************************
```

and on 32bit and 64bit


```

sage -t -long  -force_lib devel/sage-9958/sage/misc/randstate.pyx
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-9958/sage/misc/randstate.pyx", line 15
3:
    sage: random(), getrandbits(20), uniform(5.0, 10.0), normalvariate(0, 1)
Expected:
    (0.82940228518742587, 624859L, 5.77894484361117, -0.42013668263087578)
Got:
    (0.8294022851874259, 624859L, 5.77894484361117, -0.4201366826308758)
**********************************************************************
```

I don't recall previously seeing this particular randstate.pyx failure. Perhaps I've missed something.


---

Comment by jdemeyer created at 2011-12-11 09:59:18

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2011-12-11 09:59:18

Yeah, the `#random` should be on the line with the command to execute, not the result.


---

Comment by fbissey created at 2011-12-11 11:28:07

I had to make that mistake :(

The last randstate.pyx one is definitely new, I am sure it didn't happen before.


---

Attachment

take into account the randomness of it.next sequence of call - put random in the right place this time.


---

Comment by fbissey created at 2011-12-11 11:34:48

OK I replaced the trac_9958-nfactor_enumerable_word-randomness.patch in place. So random should be in the right place now. I am looking to see if I can reproduce this particular randstate.pyx problem.


---

Comment by fbissey created at 2011-12-11 11:43:13

I missed a line in randstate! And you cut the last digit of the line number Steve, now that caused me some confusion. Updating shortly.


---

Attachment

fix all numerical noise in randstate


---

Comment by fbissey created at 2011-12-11 11:51:57

OK new randstate patch, this time it is even a .patch instead of .pyx. Thanks for pointing out those mistakes.


---

Comment by fbissey created at 2011-12-11 11:51:57

Changing status from needs_work to needs_review.


---

Comment by strogdon created at 2011-12-11 19:00:06

OK, #9958 + #11986 + #12124, all tests pass here on 32bit and 64bit machines. Is it too early for champagne?


---

Comment by fbissey created at 2011-12-11 21:08:16

Unfortunately, I'd say it is too early. We need Karl to test it on his old ppc OS X 10.4 mac and a run on solaris is also in order. I removed a patch for ia64 that didn't obviously port to python-2.7 so a look at that platform is also in order. In the mean time we can review #11986 and #12124 which I think can be done independently.

We could even split the combinat patches as they should work with python-2.6. It just there is nothing obvious to fix there.


---

Comment by jdemeyer created at 2011-12-11 21:18:47

As I have said before, testing is easy.  I am currently running tests for the upcoming sage-4.8.alpha4, but after that, I could test the new Python on various systems.

But still, somebody needs to actually _look_ at the patches and verify that they make sense.


---

Comment by fbissey created at 2011-12-11 21:33:50

OK Jeroen, that's a boring task for someone most of them are of the form:

```
diff --git a/sage/misc/sage_unittest.py b/sage/misc/sage_unittest.py
--- a/sage/misc/sage_unittest.py
+++ b/sage/misc/sage_unittest.py
@@ -201,12 +201,12 @@
             Failure in _test_b:
             Traceback (most recent call last):
               ...
-            AssertionError
+            AssertionError: None
             ------------------------------------------------------------
             Failure in _test_d:
             Traceback (most recent call last):
               ...
-            AssertionError
+            AssertionError: None
             ------------------------------------------------------------
             Failure in _test_pickling:
             Traceback (most recent call last):
@@ -220,14 +220,14 @@
             running ._test_b() . . . fail
             Traceback (most recent call last):
               ...
-            AssertionError
+            AssertionError: None
             ------------------------------------------------------------
             running ._test_c() . . . pass
             running ._test_category() . . . pass
             running ._test_d() . . . fail
             Traceback (most recent call last):
               ...
-            AssertionError
+            AssertionError: None
             ------------------------------------------------------------
             running ._test_not_implemented_methods() . . . pass
             running ._test_pickling() . . . fail
@@ -249,7 +249,7 @@
               File ..., in _test_b
                 def _test_b(self, tester): tester.fail()
               ...
-            AssertionError
+            AssertionError: None
 
         In conjonction with ``%pdb on``, this allows for the debbuger
         to jump directly to the first failure location.
@@ -311,7 +311,7 @@
         sage: tester.assert_(1 == 0)
         Traceback (most recent call last):
         ...
-        AssertionError
+        AssertionError: False is not true
         sage: tester.assert_(1 == 0, "this is expected to fail")
         Traceback (most recent call last):
         ...
```

and other numerical noise niceties cutting one digit and sometimes the rounding makes a lot of digits disappear (and it looks better actually), for example in plot/colors.py

```
@@ -290,23 +290,23 @@
 
         sage: from sage.plot.colors import rgbcolor
         sage: rgbcolor(Color(0.25, 0.4, 0.9))
-        (0.25, 0.40000000000000002, 0.90000000000000002)
+        (0.25, 0.4, 0.9)
         sage: rgbcolor('purple')
```

Only the two combinat patches are a bit more subtle.


---

Comment by kcrisman created at 2011-12-12 13:55:59

Replying to [comment:209 fbissey]:
> Unfortunately, I'd say it is too early. We need Karl to test it on his old ppc OS X 10.4 mac and a run on solaris is also in order.
Is this all based on 4.8.alpha3?  I can try to do this starting today.  Jeroen might be done before me, though :) at least by the time I finish applying ALL of these patches.


---

Comment by fbissey created at 2011-12-12 20:27:27

It should apply to 4.8.alpha3, apply #11986 + #12124 also.


---

Comment by jdemeyer created at 2011-12-13 08:16:16

Replying to [comment:212 kcrisman]:
> Replying to [comment:209 fbissey]:
> > Unfortunately, I'd say it is too early. We need Karl to test it on his old ppc OS X 10.4 mac and a run on solaris is also in order.
> Is this all based on 4.8.alpha3?  I can try to do this starting today.  Jeroen might be done before me, though :)
Go ahead, I'm currently tackling other beasts...


---

Comment by slabbe created at 2011-12-13 17:20:08

Replying to [comment:201 fbissey]:
> Actually, you should have a look at what I did for both of these in [attachment:trac_9958-nfactor_enumerable_word-randomness.patch] and [attachment:trac_9958-suffix_trees-variations.patch]. If you could give your opinion on the patches or if you want to submit patches of your own it would be appreciated.

Hi,

I just look at the suffix tree code (written not by me but by Franco Saliola). The method `trie_type_dict` is not used anywhere in the file neither in `sage/combinat/words` neither in all Sage I would guess. So, it's kind of difficult to guess what the result should be (input and output blocks are absent in documentation). I think that method was used by Franco to compare the implementation of `ImplicitSuffixTree` with that of `SuffixTrie` but not seriously because the output is not practical (one can't create a `DiGraph` out of it).

Anyway, there are two loops in that method that both go through `.iteritems()` of a dictionary... Integer indexes present in the result depends on the ordering of those two loops. So, it is possible that a third different result is obtained in some other machine or system today or later. I just made a patch which should be more durable in the long term.

For the nfactor enumerable file, the fix is perfect.


---

Comment by slabbe created at 2011-12-13 17:23:09

Fix machine dependant doctest in suffix tree


---

Attachment

> > > Unfortunately, I'd say it is too early. We need Karl to test it on his old ppc OS X 10.4 mac and a run on solaris is also in order.
> > Is this all based on 4.8.alpha3?  I can try to do this starting today.  Jeroen might be done before me, though :)
> Go ahead, I'm currently tackling other beasts...
Okay, at least everything applies and builds from this and the two other tickets.  (Note that #11986 is listed as a dependency of *and* for #9958.)

So presumably sometime tomorrow I can report back.  So far six files having tested well...


---

Comment by fbissey created at 2011-12-13 18:32:14

Replying to [comment:216 slabbe]:
> Anyway, there are two loops in that method that both go through `.iteritems()` of a dictionary... Integer indexes present in the result depends on the ordering of those two loops. So, it is possible that a third different result is obtained in some other machine or system today or later. I just made a patch which should be more durable in the long term.
> 
> For the nfactor enumerable file, the fix is perfect.

Thanks. I thought there could be a third possible results from Florent's comments (permutation (3,4,5)) but couldn't figure what it would look like. Happy to have some serious review for that bit.


---

Comment by fbissey created at 2011-12-13 21:08:09

OK the upgrade of R in #12057 shipped with 4.8.alpha4 makes a small bit of patch for r.py obsolete. Updating it shortly.


---

Attachment

fixing numerical noise part 1 - updated 20111214 for 4.8.alpha4


---

Comment by fbissey created at 2011-12-13 21:12:15

First patch updated. I don't think there will be any more changes because of 4.8.alpha4 but I could be wrong.


---

Comment by strogdon created at 2011-12-14 02:08:21

It looks like a slight modification is still needed in interfaces/r.py. On both x86 and amd64 I get


```
sage -t -long  -force_lib devel/sage-main/sage/interfaces/r.py
**********************************************************************
File "/storage/sage/sage-4.8.alpha4/devel/sage-main/sage/interfaces/r.py", line 173:
    sage: sum(rr._sage_())
Expected:
    9.97721251689810...
Got:
    9.97721251689811
**********************************************************************
```

attachment:trac_9958-suffix_trees-variations-sl.patch:ticket:9958 was used in the tests.


---

Comment by fbissey created at 2011-12-14 02:22:05

I have seen it on my sage-on-gentoo test run but I hadn't tried yet on a vanilla to check if it was caused by other gentoo stuff. I will add a small patch ASAP.


---

Attachment

numerical noise in interface/r.py updated for R-2.14.0


---

Comment by fbissey created at 2011-12-14 03:22:05

New patch included for interface/r.py in 4.8.alpha4.


---

Comment by jason created at 2011-12-14 10:02:02

How do we test this ticket?  Is it enough to untar a fresh tarball of the 4.8.alpha4 source, replace the existing python spkg with the one from this ticket, and do a normal make?  Then apply the patches to the sage library and run doctests?

On OSX 10.6.8, I tried downloading a fresh copy of 4.8.alpha4, putting this python spkg in the spkg/standard directory and deleting the old python spkg.  I ended up getting a build error, seemingly right after I finished building scipy (even though scipy said it was built succesfully, but I was also building spkgs in parallel).  I typed "make" again to restart the process and the same thing happened after rpy built---it said rpy was built successfully, but then it stopped the build, saying "Error building Sage".


---

Comment by fbissey created at 2011-12-14 11:51:11

Replying to [comment:224 jason]:
> How do we test this ticket?  Is it enough to untar a fresh tarball of the 4.8.alpha4 source, replace the existing python spkg with the one from this ticket, and do a normal make?  Then apply the patches to the sage library and run doctests?
> 

Yes that's how you should do it.

> On OSX 10.6.8, I tried downloading a fresh copy of 4.8.alpha4, putting this python spkg in the spkg/standard directory and deleting the old python spkg.  I ended up getting a build error, seemingly right after I finished building scipy (even though scipy said it was built succesfully, but I was also building spkgs in parallel).  I typed "make" again to restart the process and the same thing happened after rpy built---it said rpy was built successfully, but then it stopped the build, saying "Error building Sage".
> 

Could you post the log for the build of python somewhere? scipy and rpy are built after sage (or at least they can be since they are runtime and not buildtime dependencies) so it is possible you were building sage itself at the same time. Is there a log for the sage spkg (in spkg/log)?


---

Comment by jason created at 2011-12-14 14:20:39

I posted the install.log here: http://sage.math.washington.edu/home/jason/sage-4.8.alpha4-python2.7-install.log.bz2

If you search for "Error building Sage", you'll see the multiple times I restarted the build (that message appeared after each time I restarted the build).

Here's the list of spkg logs I have:


```

sage-4.8.alpha4newpython/spkg/logs% ls
atlas-3.8.4.log                gdmodule-0.56.p7.log           moin-1.9.1.p2.log              ratpoints-2.1.3.p1.log
blas-20070724.log              genus2reduction-0.3.p8.log     mpfi-1.3.4-cvs20071125.p8.log  readline-6.2.p1.log
boehm_gc-7.2.alpha6.p1.log     gfan-0.4plus.p1.log            mpfr-2.4.2.log                 rpy2-2.0.8.log
boost-cropped-1.34.1.log       givaro-3.2.13rc2.p2.log        mpir-2.1.3.p8.log              rubiks-20070912.p17.log
bzip2-1.0.5.log                glpk-4.44.log                  mpmath-0.17.log                sage_root-4.8.alpha4.log
cddlib-094f.p8.log             gnutls-2.2.1.p5.log            networkx-1.2.p1.log            sage_scripts-4.8.alpha4.log
cephes-2.8.log                 graphs-20070722.p1.log         ntl-5.5.2.log                  sagenb-0.8.25.log
cliquer-1.2.p10.log            gsl-1.15.log                   numpy-1.5.1.log                scipy-0.9.p1.log
conway_polynomials-0.2.log     iconv-1.13.1.p3.log            opencdk-0.6.6.p5.log           scons-1.2.0.log
cvxopt-1.1.3.log               iml-1.0.1.p13.log              palp-1.1.p3.log                setuptools-0.6.16.log
cython-0.15.1.log              ipython-0.10.2.p0.log          pari-2.5.0.p2.log              singular-3-1-3-3.p2.log
dir-0.1.log                    jinja2-2.5.5.log               patch-2.5.9.p2.log             sphinx-1.1.2.p0.log
docutils-0.7.p0.log            lapack-20071123.p2.log         pexpect-2.0.p4.log             sqlalchemy-0.5.8.log
ecl-11.1.2.cvs20111120.p0.log  lcalc-1.23.p9.log              pil-1.1.6.p4.log               sqlite-3.7.5.log
eclib-20100711.p0.log          libfplll-3.0.12.p1.log         polybori-0.7.1.p6.log          symmetrica-2.0.p7.log
ecm-6.3.p2.log                 libgcrypt-1.4.4.p3.log         polytopes_db-20100210.log      sympow-1.018.1.p9.log
elliptic_curves-0.3.log        libgpg_error-1.6.p3.log        ppl-0.11.2.log                 sympy-0.7.1.log
extcode-4.8.alpha4.log         libm4ri-20111004.log           prereq-0.9.log                 tachyon-0.98.9.p5.log
f2c-20070816.p2.log            libm4rie-20111004.log          pycrypto-2.1.0.log             termcap-1.3.1.p1.log
flint-1.5.0.p10.log            libpng-1.2.35.p3.log           pygments-1.3.1.p0.log          twisted-9.0.p2.log
flintqs-20070817.p6.log        linbox-1.1.6.p5.log            pynac-0.2.3.log                zlib-1.2.5.p0.log
fortran-20100629.log           matplotlib-1.0.1.p0.log        python-2.7.2.p0.log            zn_poly-0.9.p5.log
freetype-2.3.5.p3.log          maxima-5.23.2.p2.log           python_gnutls-1.1.4.p7.log     zodb3-3.7.0.p4.log
gd-2.0.35.p5.log               mercurial-1.8.4.log            r-2.14.0.p0.log
```



---

Comment by kcrisman created at 2011-12-14 21:15:10

All is well on the PPC OS X front, even with the r.py, amazingly; it failed the first time but passed on a rerun.


---

Comment by fbissey created at 2011-12-14 22:46:02

Jason the log you sent is not very useful, at least I cannot easily find something interesting. Could you provide the following:

 * python-2.7.2.p0.log
 * polybori-0.7.1.p6.log
 * ppl-0.11.2.log
 * pynac-0.2.3.log

That's a shot in the dark so far. But the building of sage never started as there is no log for sage itself.

I digged a little bit more before posting it looks like R fails to build so I want to see r-2.14.0.p0.log but that may be a separate issue from python. matplotlib seems to fail to build too so I want matplotlib-1.0.1.p0.log and now we are talking real potential python trouble.


---

Comment by kcrisman created at 2011-12-15 01:30:56

I'm going to try this with 

```
export MAKE="make -j2"
```

on the same platform and report back.


---

Comment by jason created at 2011-12-15 02:49:03

First, here are my standard build environment settings:


```
export SAGE_MATPLOTLIB_GUI=yes
export SAGE_PARALLEL_SPKG_BUILD=yes     
export MAKE="make -j6"    
export SAGE_SPKG_INSTALL_DOCS=yes
```


All the requested logs are tarred up at http://sage.math.washington.edu/home/jason/newpython-spkg-logs.tar.gz


---

Comment by jason created at 2011-12-15 02:51:08

Tonight, I'll try building again without setting any of those environment variables to see if it succeeds with a "stock" build.


---

Comment by kcrisman created at 2011-12-15 02:56:44

Replying to [comment:229 kcrisman]:
> I'm going to try this with 

```
> export MAKE="make -j2"
```

> on the same platform and report back. 

Interestingly, Scipy and R are definitely (right now) building before Sage.  And they usually do not, for sure not Scipy, on my ancient older Mac.  

Scipy has successfully installed, as has matplotlib.  R takes forever but so far is fine.  Maybe it was "just a race condition"?


---

Comment by jason created at 2011-12-15 03:02:05

I bet the matplotlib error shows up for me because I define SAGE_MATPLOTLIB_GUI (so that matplotlib tries to build the GUI backends).


---

Comment by fbissey created at 2011-12-15 03:04:25

It is quite possibly something broken with the GUI from what I can see of your original log. scipy can build whenever after numpy independently of sage so I don't see a problem there.


---

Comment by fbissey created at 2011-12-15 03:06:16

Yes I think matplotlib cannot find tk. We may want to look at this in depth on OS X.


---

Comment by jason created at 2011-12-15 03:12:45

The matplotlib error is fixed upstream: https://github.com/matplotlib/matplotlib/issues/139


---

Comment by fbissey created at 2011-12-15 03:22:13

Very good, we may want to bump the spkg to 1.1.0 then. From my sage-on-gentoo experience there is just one minor doctest failure from matplotli-1.1.0

```
sage -t -long -force_lib "devel/sage/sage/plot/colors.py"   
**********************************************************************
File "/usr/share/sage/devel/sage/sage/plot/colors.py", line 1241:
    sage: len(maps.maps)
Expected:
    134
Got:
    138
**********************************************************************
File "/usr/share/sage/devel/sage/sage/plot/colors.py", line 1285:
    sage: len(maps)
Expected:
    134
Got:
    138
**********************************************************************
```

Fairly standard each time we bump matplotlib or almost.

You R package definitely broke the first time around. I am fairly sure this is a parallel make issue. I have seen at least one instance that I suspect is parallel make on Gentoo. Of course given that it stop because of

```
make[6]: gcc: Resource temporarily unavailable
```

I think, we may have something else altogether. It should go into a separate ticket.


---

Comment by jason created at 2011-12-15 03:24:13

Do you already have a 1.1.0 spkg?  I'm working on one right now, but you already have one...


---

Comment by kcrisman created at 2011-12-15 03:29:14

> Scipy has successfully installed, as has matplotlib.  R takes forever but so far is fine.  Maybe it was "just a race condition"?

_Everything_ built before the Sage library except Gap and SageTeX.  No problems.  I say this shouldn't keep the Python upgrade out, or?


---

Comment by fbissey created at 2011-12-15 03:31:41

Replying to [comment:238 jason]:
> Do you already have a 1.1.0 spkg?  I'm working on one right now, but you already have one...

I don't have one. I don't need one for sage-on-gentoo as I am using system packages. You go ahead and create a ticket to upgrade matplotlib. I say it is a show stopper because it would happen on other platforms. Hopefully we can review it quickly.


---

Comment by kcrisman created at 2011-12-15 03:47:02

Replying to [comment:240 fbissey]:
> Replying to [comment:238 jason]:
> > Do you already have a 1.1.0 spkg?  I'm working on one right now, but you already have one...
> 
> I don't have one. I don't need one for sage-on-gentoo as I am using system packages. You go ahead and create a ticket to upgrade matplotlib. I say it is a show stopper because it would happen on other platforms. Hopefully we can review it quickly.

What about just making a patch upgrade with [the 1.5-liner](https://github.com/matplotlib/matplotlib/commit/e4a34df93f6) rather than making a whole new package which would require even MORE testing?  Plus, then you don't have to worry about getting those four extra colormaps :)  Anyway, I feel this is easier and more reasonable just to get this in 5.0.alpha0 (or whatever release is next for such a big spkg change as this ticket).


---

Comment by fbissey created at 2011-12-15 03:54:36

I have no objections to that. Faster is better in that case because we really want to land this quickly because every other moves of the tree makes me rewrite stuff. It start to be hard to manage.


---

Comment by jason created at 2011-12-15 06:24:50

I added a link to a patched version of the current matplotlib spkg.  I also added the diff as an information-only patch above.  Independent from this fix, I've also made a matplotlib 1.1.0 spkg, which also fixes the problem, but may need more testing than this very slight change to the existing matplotlib spkg.


---

Comment by jason created at 2011-12-15 06:49:55

By the way, the matplotlib 1.1.0 spkg is at #11915, but the spkg here should be sufficient.


---

Comment by fbissey created at 2011-12-15 11:50:07

#12131 has been merged, I'll rebase the python spkg by next Monday hopefully.


---

Comment by jason created at 2011-12-15 13:36:43

Using the new matplotlib-1.0.1.p1.spkg above, and my standard build environment variables:


```
export SAGE_MATPLOTLIB_GUI=yes
export SAGE_PARALLEL_SPKG_BUILD=yes     
export MAKE="make -j6"    
export SAGE_SPKG_INSTALL_DOCS=yes
```


Everything except R builds nicely.  R still has that message about resources not being available (something about fork).  I then changed MAKE to "make -j2" and restarted the make and everything finished just fine.  Again, on OSX 10.6.8 (4G of memory).

That's a bummer that make -j6 doesn't work.  Regular old 4.8.alpha4 built fine, so I don't think it's just the new R spkg.  I'll try building fresh one more time, but with MAKE=make -j4 just to check things out.


---

Comment by jason created at 2011-12-15 18:18:10

The matplotlib spkg at #11915 is ready for review (and depends on the #11976, also ready for review).  Instead of using the matplotlib-1.0.1.p1.spkg above, it would be preferable to review and merge #11976 and #11915.


---

Comment by jhpalmieri created at 2011-12-15 19:49:35

Okay, I started with 4.8.alpha4, added the new python spkg from this ticket, the new matplotlib spkg from #11915, applied all of the patches from this ticket, #11976, #11986, and #12124.  I have a tarball with all of these:

[http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.alpha4-9958.tar](http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.alpha4-9958.tar)

along with an upgrade path:

[http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.alpha4-9958/](http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.alpha4-9958/)

for testing.


---

Comment by jason created at 2011-12-15 21:39:34

Did you also apply the patch from #11915?


---

Comment by jhpalmieri created at 2011-12-15 22:59:13

No, looks like I missed that one.


---

Comment by jhpalmieri created at 2011-12-16 00:50:28

Okay, here are versions including the patch from #11915:

 - [http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.a4-9958.tar](http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.a4-9958.tar)
 - [http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.a4-9958/](http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.a4-9958/)


---

Comment by jason created at 2011-12-16 16:14:12

I took jhpalmieri's original tarball, applied the patch from #11915 myself, built it with these settings:


```
SAGE_MATPLOTLIB_GUI=yes
SAGE_PARALLEL_SPKG_BUILD=yes
MAKE=make -j12
SAGE_SPKG_INSTALL_DOCS=yes
```


on Ubuntu 10.04.  Everything built fine, and make ptestlong passed all tests. Yeah!


---

Comment by kcrisman created at 2011-12-20 02:33:49

What remains to be done here for positive review?


---

Comment by fbissey created at 2011-12-20 02:43:45

Replying to [comment:258 kcrisman]:
> What remains to be done here for positive review?

First I have to rebase the python spkg to #12131. Second there is a new matplotlib spkg currently merged in 4.8.alpha5 (unreleased) that needs review in #11915. Then someone has to look at the patches to make sure they are not completely stupid (long tiedous job).

Then we can move this to a positive review. I was hoping to be able to to rebase the spkg on Sunday but it didn't happen. I am busy doing a bit of code for my paid work but once it is done. I'll go for it, that may be tomorrow in my time zone.


---

Comment by fbissey created at 2011-12-20 21:28:22

python-2.7.2.p0 spkg rebased and available.


---

Comment by fbissey created at 2011-12-20 22:16:22

#11986 also needs review. It looks like it may need to go at the same time as python 2.7 as my own testing with python 2.6 on linux amd64 was not positive but everything is smooth with python 2.7.


---

Comment by strogdon created at 2011-12-21 01:14:50

For sage-4.8.alpha4 with tickets #9958 + #11986 + #12124 + #11976 + #11915 all tests pass on x86 and on amd64 there is one TIME OUT

```
sage -t -long  -force_lib devel/sage-matplotlib-1.1.0/sage/interfaces/ecm.py
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***

         [1800.2 s]
```

The test did pass when run individually. I'm sure this is due to running the tests in parallel. I've seen it before, not with this ticket, but with sage-on-gentoo builds.


---

Comment by fbissey created at 2011-12-21 01:26:36

Replying to [comment:262 strogdon]:
> For sage-4.8.alpha4 with tickets #9958 + #11986 + #12124 + #11976 + #11915 all tests pass on x86 and on amd64 there is one TIME OUT
> {{{
> sage -t -long  -force_lib devel/sage-matplotlib-1.1.0/sage/interfaces/ecm.py
> *** *** Error: TIMED OUT! PROCESS KILLED! *** ***
> 
>          [1800.2 s]
> }}}
> The test did pass when run individually. I'm sure this is due to running the tests in parallel. I've seen it before, not with this ticket, but with sage-on-gentoo builds.

I have seen it before too - in parallel tests as well. It seems that ecm can be a bad boy, not sure what to do about it but that would be outside of the scope of this ticket in my opinion.

Steve, did you do any test of #11986 with python-2.6?


---

Comment by strogdon created at 2011-12-21 01:48:03

Replying to [comment:263 fbissey]:
> Steve, did you do any test of #11986 with python-2.6?
No, I haven't done that with python-2.6. I will do it, but hopefully someone beats me to it.


---

Comment by jdemeyer created at 2012-01-03 13:17:23

Upgrading from sage-4.5 fails with:

```
Testing that Sage starts...
[2012-01-03 13:47:34]
Traceback (most recent call last):
  File "/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/bin/sage-eval", line 4, in <module>
    from sage.all import *
  File "/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/lib/python2.7/site-packages/sage/all.py", line 75, in <module>
    from sage.matrix.all     import *
  File "/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/lib/python2.7/site-packages/sage/matrix/all.py", line 1, in <module>
    from matrix_space import MatrixSpace, is_MatrixSpace
  File "/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/lib/python2.7/site-packages/sage/matrix/matrix_space.py", line 37, in <module>
    import matrix_modn_dense
  File "matrix_modn_dense.pyx", line 1, in init sage.matrix.matrix_modn_dense (sage/matrix/matrix_modn_dense.c:15026)
AttributeError: 'module' object has no attribute 'Matrix_dense'
Sage failed to start up.
Please email sage-devel (http://groups.google.com/group/sage-devel)
explaining the problem and send the log file
  /mnt/usb1/scratch/jdemeyer/sage-4.5-python27/start.log
Describe your computer, operating system, etc.
```


After `sage -ba-force`, it works again.


---

Comment by fbissey created at 2012-01-04 01:35:47

Replying to [comment:265 jdemeyer]:
> Upgrading from sage-4.5 fails with:
> {{{
> Testing that Sage starts...
> [2012-01-03 13:47:34]
> Traceback (most recent call last):
>   File "/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/bin/sage-eval", line 4, in <module>
>     from sage.all import *
>   File "/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/lib/python2.7/site-packages/sage/all.py", line 75, in <module>
>     from sage.matrix.all     import *
>   File "/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/lib/python2.7/site-packages/sage/matrix/all.py", line 1, in <module>
>     from matrix_space import MatrixSpace, is_MatrixSpace
>   File "/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/lib/python2.7/site-packages/sage/matrix/matrix_space.py", line 37, in <module>
>     import matrix_modn_dense
>   File "matrix_modn_dense.pyx", line 1, in init sage.matrix.matrix_modn_dense (sage/matrix/matrix_modn_dense.c:15026)
> AttributeError: 'module' object has no attribute 'Matrix_dense'
> Sage failed to start up.
> Please email sage-devel (http://groups.google.com/group/sage-devel)
> explaining the problem and send the log file
>   /mnt/usb1/scratch/jdemeyer/sage-4.5-python27/start.log
> Describe your computer, operating system, etc.
> }}}
> 
> After `sage -ba-force`, it works again.

Quite weird. You would think those particular libraries would have been rebuilt already after the linbox upgrade at least. Shouldn't a complete rebuild of sage occur after a python upgrade? In any case that seems mild for upgrading from 4.5 which was released on June 2010 many versions away.


---

Comment by jdemeyer created at 2012-01-04 07:31:59

Replying to [comment:266 fbissey]:
> Shouldn't a complete rebuild of sage occur after a python upgrade?
I guess it should.  Do you know how to make this happen?


---

Comment by jdemeyer created at 2012-01-04 07:31:59

Changing status from needs_review to needs_work.


---

Attachment

Diff for the Python spkg (without deleted files), for review only


---

Comment by jdemeyer created at 2012-01-04 19:06:38

Upgrading fixed by deleting

```
$SAGE_ROOT/devel/sage-*/build
```

when an old version of Python is detected.

New spkg: [http://boxen.math.washington.edu/home/jdemeyer/spkg/python-2.7.2.p1.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/python-2.7.2.p1.spkg)


---

Comment by jdemeyer created at 2012-01-04 19:06:38

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2012-01-04 19:07:16

Diff for the Python spkg 2.7.2.p0 -> 2.7.2.p1, for review only


---

Attachment

*positive_review* to the spkg, modulo my changes in the 2.7.2.p1 package.


---

Comment by fbissey created at 2012-01-05 02:52:18

Looks good to me. I didn't notice I missed a patch in the stuff I removed. Anyway I'll be on low activity because my home computer has given up the ghost (writing from an old box cobbled together running puppy 4.00 from a _1_GB hard drive) and I am on leave.


---

Attachment


---

Attachment


---

Attachment

Folded all the patches into only four patches.


---

Comment by jdemeyer created at 2012-01-05 16:09:20

Replying to [comment:272 fbissey]:
> Looks good to me.

Meaning "positive review"? :-)


---

Comment by fbissey created at 2012-01-05 21:36:15

Changing status from needs_review to positive_review.


---

Comment by fbissey created at 2012-01-05 21:36:15

Replying to [comment:274 jdemeyer]:
> Replying to [comment:272 fbissey]:
> > Looks good to me.
> 
> Meaning "positive review"? :-)
Absolutely positive! Hopefully nothing will happen to make us break or add to those 4 megapatches.


---

Comment by jdemeyer created at 2012-01-05 22:09:05

[attachment:9958_combinat.patch] is the only non-trivial change I guess, but has been discussed well in the comments on this ticket.  Potentially, the `trie_type_dict()` test might yield other results, but we can still change the test in that case.  Anyway, that method is nowhere called in the Sage library.


---

Comment by fbissey created at 2012-01-05 22:18:27

Replying to [comment:276 jdemeyer]:
> [attachment:9958_combinat.patch] is the only non-trivial change I guess, but has been discussed well in the comments on this ticket.  Potentially, the `trie_type_dict()` test might yield other results, but we can still change the test in that case.  Anyway, that method is nowhere called in the Sage library.

I didn't notice you had listed this particular patch. Why not use [attachment:trac_9958-suffix_trees-variations-sl.patch] from Sébastien Labbé instead? It is more foolproof.


---

Comment by fbissey created at 2012-01-05 22:25:13

I obviously meant to use Sébastien Labbé's patch for suffix_tree, we can still use the other patch for nfactor_enumerable_word.py, Sébastien think that patch is perfect which I count as a positive review of it.


---

Comment by jdemeyer created at 2012-01-05 22:39:10

Replying to [comment:277 fbissey]:
> I didn't notice you had listed this particular patch. Why not use [attachment:trac_9958-suffix_trees-variations-sl.patch] from Sébastien Labbé instead? It is more foolproof.
I overlooked that patch, it was not in the list of patches to be applied.  I agree it is better.


---

Attachment

Replying to [comment:279 jdemeyer]:
> Replying to [comment:277 fbissey]:
> > I didn't notice you had listed this particular patch. Why not use [attachment:trac_9958-suffix_trees-variations-sl.patch] from Sébastien Labbé instead? It is more foolproof.
> I overlooked that patch, it was not in the list of patches to be applied.  I agree it is better.

It was [http://trac.sagemath.org/sage_trac/ticket/9958?action=diff&version=273](http://trac.sagemath.org/sage_trac/ticket/9958?action=diff&version=273) but never mind we have it now.


---

Comment by jdemeyer created at 2012-01-05 22:49:13

Replying to [comment:280 fbissey]:
> It was [http://trac.sagemath.org/sage_trac/ticket/9958?action=diff&version=273](http://trac.sagemath.org/sage_trac/ticket/9958?action=diff&version=273) but never mind we have it now.
Look more carefully, it wasn't :-)


---

Comment by fbissey created at 2012-01-05 23:33:23

You are right I put the wrong patch in the list actually I never updated the list to include the right one, complete oversight. It's good that we are getting this merged now before more confusion arise from the number of patches attached.


---

Comment by jhpalmieri created at 2012-01-05 23:59:53

François and others: thank you for all of the work you did on this ticket.


---

Comment by slabbe created at 2012-01-09 03:51:55

Hi, 

I am removing my name from the authors list. For three lines of code I wrote, I don't feel as an author at all for such an important ticket. Being a reviewer of the small combinat part is enough and more appropriate.

Sébastien


---

Comment by jdemeyer created at 2012-01-15 21:55:53

Resolution: fixed


---

Comment by kcrisman created at 2012-01-19 01:40:59

Just as FYI, though I doubt it matters since the patch still applies, I get

```
patching file Lib/distutils/command/sdist.py
Hunk #1 succeeded at 327 (offset 3 lines).
Hunk #2 succeeded at 342 (offset 3 lines).
```

before the other patches and configuration.


---

Comment by fbissey created at 2012-01-19 01:58:29

Doesn't matter anymore indeed, we have it merged in 5.0.beta0 finally. I am personally moving to #11705 and #11334 unless something very bad happen.


---

Comment by jdemeyer created at 2012-01-19 08:10:47

Replying to [comment:286 kcrisman]:
> Just as FYI, though I doubt it matters since the patch still applies, I get
> {{{
> patching file Lib/distutils/command/sdist.py
> Hunk #1 succeeded at 327 (offset 3 lines).
> Hunk #2 succeeded at 342 (offset 3 lines).
> }}}

Not a big deal.  The patch still applies perfectly.
