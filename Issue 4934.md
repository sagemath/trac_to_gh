# Issue 4934: matrix1.pyx refernece related doctest crash on cicero

archive/issues_004934.json:
```json
{
    "body": "Assignee: @robertwb\n\nThe following looks very much like a Cython reference issue: When doctesting matrix1.pyx it segfaults at this point:\n\n```\n<SNIP>\nsage: a = matrix([[pi, sin(x)], [cos(x), 1/e]]); a\n\n[    pi sin(x)]\n[cos(x)   e^-1]\nsage: a._mathematica_init_()\n'{{Pi, Sin[x]}, {Cos[x], (E) ^ (-1)}}'\nsage: \n```\n\nValgrind says:\n\n```\n==26254== Invalid read of size 4\n==26254==    at 0x809FC3E: slot_tp_del (typeobject.c:5024)\n==26254==    by 0x809D32F: subtype_dealloc (typeobject.c:664)\n==26254==    by 0xD99F3FB: __pyx_tp_dealloc_4sage_6matrix_21matrix_symbolic_dense_Matrix_symbolic_dense (matrix_symbolic_dense.c:6534)\n==26254==    by 0x808643B: PyDict_Clear (dictobject.c:757)\n==26254==    by 0x8086460: dict_clear (dictobject.c:1776)\n==26254==    by 0x80CC54A: PyEval_EvalFrameEx (ceval.c:3557)\n==26254==    by 0x80CDCA4: PyEval_EvalCodeEx (ceval.c:2836)\n==26254==    by 0x8114835: function_call (funcobject.c:517)\n==26254==    by 0x805B126: PyObject_Call (abstract.c:1861)\n==26254==    by 0x806130E: instancemethod_call (classobject.c:2519)\n==26254==    by 0x805B126: PyObject_Call (abstract.c:1861)\n==26254==    by 0x80C9D85: PyEval_EvalFrameEx (ceval.c:3784)\n==26254==    by 0x80CDCA4: PyEval_EvalCodeEx (ceval.c:2836)\n==26254==    by 0x80CC61E: PyEval_EvalFrameEx (ceval.c:3669)\n==26254==    by 0x80CDCA4: PyEval_EvalCodeEx (ceval.c:2836)\n==26254==    by 0x80CC61E: PyEval_EvalFrameEx (ceval.c:3669)\n==26254==    by 0x80CDCA4: PyEval_EvalCodeEx (ceval.c:2836)\n==26254==    by 0x80CC61E: PyEval_EvalFrameEx (ceval.c:3669)\n==26254==    by 0x80CDCA4: PyEval_EvalCodeEx (ceval.c:2836)\n==26254==    by 0x80CDEB6: PyEval_EvalCode (ceval.c:494)\n==26254==    by 0x80EB24E: PyRun_FileExFlags (pythonrun.c:1273)\n==26254==    by 0x80EB519: PyRun_SimpleFileExFlags (pythonrun.c:879)\n==26254==    by 0x805705A: Py_Main (main.c:523)\n==26254==    by 0x8056431: main (python.c:23)\n==26254==  Address 0x68cdeac is 12 bytes inside a block of size 36 free'd\n==26254==    at 0x400593A: free (vg_replace_malloc.c:323)\n==26254==    by 0x57E1594: __pyx_tp_dealloc_4sage_9structure_11sage_object_SageObject (sage_object.c:7414)\n==26254==    by 0x6181EC3: __pyx_tp_dealloc_4sage_9structure_7element_Element (element.c:18963)\n==26254==    by 0x809D4C4: subtype_dealloc (typeobject.c:709)\n==26254==    by 0x806185B: instancemethod_dealloc (classobject.c:2311)\n==26254==    by 0x809FD02: slot_tp_del (typeobject.c:5014)\n==26254==    by 0x809D32F: subtype_dealloc (typeobject.c:664)\n==26254==    by 0xD99F3FB: __pyx_tp_dealloc_4sage_6matrix_21matrix_symbolic_dense_Matrix_symbolic_dense (matrix_symbolic_dense.c:6534)\n==26254==    by 0x808643B: PyDict_Clear (dictobject.c:757)\n==26254==    by 0x8086460: dict_clear (dictobject.c:1776)\n==26254==    by 0x80CC54A: PyEval_EvalFrameEx (ceval.c:3557)\n==26254==    by 0x80CDCA4: PyEval_EvalCodeEx (ceval.c:2836)\n==26254==    by 0x8114835: function_call (funcobject.c:517)\n==26254==    by 0x805B126: PyObject_Call (abstract.c:1861)\n==26254==    by 0x806130E: instancemethod_call (classobject.c:2519)\n==26254==    by 0x805B126: PyObject_Call (abstract.c:1861)\n==26254==    by 0x80C9D85: PyEval_EvalFrameEx (ceval.c:3784)\n==26254==    by 0x80CDCA4: PyEval_EvalCodeEx (ceval.c:2836)\n==26254==    by 0x80CC61E: PyEval_EvalFrameEx (ceval.c:3669)\n==26254==    by 0x80CDCA4: PyEval_EvalCodeEx (ceval.c:2836)\n==26254==    by 0x80CC61E: PyEval_EvalFrameEx (ceval.c:3669)\n==26254==    by 0x80CDCA4: PyEval_EvalCodeEx (ceval.c:2836)\n==26254==    by 0x80CC61E: PyEval_EvalFrameEx (ceval.c:3669)\n==26254==    by 0x80CDCA4: PyEval_EvalCodeEx (ceval.c:2836)\n==26254==    by 0x80CDEB6: PyEval_EvalCode (ceval.c:494)\n```\n\nThe segfault is in auto-generated code:\n\n```\nstatic void __pyx_tp_dealloc_4sage_6matrix_21matrix_symbolic_dense_Matrix_symbolic_dense(PyObject *o) {\n  struct __pyx_obj_4sage_6matrix_21matrix_symbolic_dense_Matrix_symbolic_dense \n  *p = (struct __pyx_obj_4sage_6matrix_21matrix_symbolic_dense_Matrix_symbolic_dense *)o;\n  Py_XDECREF(p->_maxima);                [this is line 6534]\n  Py_XDECREF(p->__variables);\n  Py_XDECREF(p->__number_of_args);\n  Py_XDECREF(p->_simp);\n  __pyx_ptype_4sage_6matrix_12matrix_dense_Matrix_dense->tp_dealloc(o);\n}\n```\n\nRunning it all by itself is clean:\n\n```\n[mabshoff@cicero sage-3.2.3.final-cicero]$ ./sage -valgrind\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n/home/mabshoff/build-3.2.3.final/sage-3.2.3.final-cicero/local/bin/sage-ipython\nLog file is /home/mabshoff/.sage/valgrind/sage-memcheck.%p\nUsing default flags:\n--leak-resolution=high --leak-check=full --num-callers=25 \n--suppressions=/home/mabshoff/build-3.2.3.final/sage-3.2.3.final-cicero/\nlocal/lib/valgrind/sage.supp\n==26391== Memcheck, a memory error detector.\n==26391== Copyright (C) 2002-2007, and GNU GPL'd, by Julian Seward et al.\n==26391== Using LibVEX rev 1854, a library for dynamic binary translation.\n==26391== Copyright (C) 2004-2007, and GNU GPL'd, by OpenWorks LLP.\n==26391== Using valgrind-3.3.1, a dynamic binary instrumentation framework.\n==26391== Copyright (C) 2000-2007, and GNU GPL'd, by Julian Seward et al.\n==26391== For more details, rerun with: -v\n==26391==\nPython 2.5.2 (r252:60911, Jan  3 2009, 15:33:57)\n[GCC 4.3.0 20080428 (Red Hat 4.3.0-8)] on linux2\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\nsage: a = matrix([[pi, sin(x)], [cos(x), 1/e]]); a\n| Sage Version 3.2.3.final, Release Date: 2009-01-02                 |\n| Type notebook() for the GUI, and license() for information.        |\n[    pi sin(x)]\n[cos(x)   e^-1]\nsage: a._mathematica_init_()\n'{{Pi, Sin[x]}, {Cos[x], (E) ^ (-1)}}'\nsage: \nExiting SAGE (CPU time 0m5.61s, Wall time 3m4.55s).\nExiting spawned Maxima process.\n==26391== \n==26391== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 1321 from 1)\n==26391== malloc/free: in use at exit: 24,986,088 bytes in 215,178 blocks.\n==26391== malloc/free: 783,764 allocs, 568,586 frees, 100,000,527 bytes allocated.\n==26391== For counts of detected errors, rerun with: -v\n==26391== searching for pointers to 215,178 not-freed blocks.\n==26391== checked 30,982,372 bytes.\n```\n\n3.2.3.alpha0 with \n\n```\n[mabshoff@cicero sage-3.2.3.alpha0-cicero-gcc432]$ gcc -v\nUsing built-in specs.\nTarget: i686-pc-linux-gnu\nConfigured with: /usr/local/gcc-4.3.2/src/gcc-4.3.2/configure \n--enable-languages=c,c++,fortran \n--with-gmp=/usr/local/gmp-4.2.3/x86-Linux-fc8-gcc-4.3.1 \n--with-mpfr=/usr/local/mpfr-2.3.2/x86-Linux-fc8-gmp-4.2.3-gcc-4.3.1 \n--prefix=/usr/local/gcc-4.3.2/x86-Linux-fc8\nThread model: posix\ngcc version 4.3.2 (GCC) \n```\n\nworks fine. But 3.2.3.rc0 with \n\n```\n[mabshoff@cicero sage-3.2.3.alpha0-cicero-gcc432]$ gcc -v\nUsing built-in specs.\nTarget: i386-redhat-linux\nConfigured with: ../configure --prefix=/usr --mandir=/usr/share/man \n--infodir=/usr/share/info --with-bugurl=http://bugzilla.redhat.com/bugzilla \n--enable-bootstrap --enable-shared --enable-threads=posix \n--enable-checking=release --with-system-zlib --enable-__cxa_atexit \n--disable-libunwind-exceptions --enable-languages=c,c++,objc,obj-c++,java,fortran,ada \n--enable-java-awt=gtk --disable-dssi --enable-plugin \n--with-java-home=/usr/lib/jvm/java-1.5.0-gcj-1.5.0.0/jre \n--enable-libgcj-multifile --enable-java-maintainer-mode \n--with-ecj-jar=/usr/share/java/eclipse-ecj.jar \n--disable-libjava-multilib --with-cpu=generic --build=i386-redhat-linux\nThread model: posix\ngcc version 4.3.0 20080428 (Red Hat 4.3.0-8) (GCC) \n```\n\nhas trouble.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4934\n\n",
    "created_at": "2009-01-03T21:44:43Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "matrix1.pyx refernece related doctest crash on cicero",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4934",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @robertwb

The following looks very much like a Cython reference issue: When doctesting matrix1.pyx it segfaults at this point:

```
<SNIP>
sage: a = matrix([[pi, sin(x)], [cos(x), 1/e]]); a

[    pi sin(x)]
[cos(x)   e^-1]
sage: a._mathematica_init_()
'{{Pi, Sin[x]}, {Cos[x], (E) ^ (-1)}}'
sage: 
```

Valgrind says:

```
==26254== Invalid read of size 4
==26254==    at 0x809FC3E: slot_tp_del (typeobject.c:5024)
==26254==    by 0x809D32F: subtype_dealloc (typeobject.c:664)
==26254==    by 0xD99F3FB: __pyx_tp_dealloc_4sage_6matrix_21matrix_symbolic_dense_Matrix_symbolic_dense (matrix_symbolic_dense.c:6534)
==26254==    by 0x808643B: PyDict_Clear (dictobject.c:757)
==26254==    by 0x8086460: dict_clear (dictobject.c:1776)
==26254==    by 0x80CC54A: PyEval_EvalFrameEx (ceval.c:3557)
==26254==    by 0x80CDCA4: PyEval_EvalCodeEx (ceval.c:2836)
==26254==    by 0x8114835: function_call (funcobject.c:517)
==26254==    by 0x805B126: PyObject_Call (abstract.c:1861)
==26254==    by 0x806130E: instancemethod_call (classobject.c:2519)
==26254==    by 0x805B126: PyObject_Call (abstract.c:1861)
==26254==    by 0x80C9D85: PyEval_EvalFrameEx (ceval.c:3784)
==26254==    by 0x80CDCA4: PyEval_EvalCodeEx (ceval.c:2836)
==26254==    by 0x80CC61E: PyEval_EvalFrameEx (ceval.c:3669)
==26254==    by 0x80CDCA4: PyEval_EvalCodeEx (ceval.c:2836)
==26254==    by 0x80CC61E: PyEval_EvalFrameEx (ceval.c:3669)
==26254==    by 0x80CDCA4: PyEval_EvalCodeEx (ceval.c:2836)
==26254==    by 0x80CC61E: PyEval_EvalFrameEx (ceval.c:3669)
==26254==    by 0x80CDCA4: PyEval_EvalCodeEx (ceval.c:2836)
==26254==    by 0x80CDEB6: PyEval_EvalCode (ceval.c:494)
==26254==    by 0x80EB24E: PyRun_FileExFlags (pythonrun.c:1273)
==26254==    by 0x80EB519: PyRun_SimpleFileExFlags (pythonrun.c:879)
==26254==    by 0x805705A: Py_Main (main.c:523)
==26254==    by 0x8056431: main (python.c:23)
==26254==  Address 0x68cdeac is 12 bytes inside a block of size 36 free'd
==26254==    at 0x400593A: free (vg_replace_malloc.c:323)
==26254==    by 0x57E1594: __pyx_tp_dealloc_4sage_9structure_11sage_object_SageObject (sage_object.c:7414)
==26254==    by 0x6181EC3: __pyx_tp_dealloc_4sage_9structure_7element_Element (element.c:18963)
==26254==    by 0x809D4C4: subtype_dealloc (typeobject.c:709)
==26254==    by 0x806185B: instancemethod_dealloc (classobject.c:2311)
==26254==    by 0x809FD02: slot_tp_del (typeobject.c:5014)
==26254==    by 0x809D32F: subtype_dealloc (typeobject.c:664)
==26254==    by 0xD99F3FB: __pyx_tp_dealloc_4sage_6matrix_21matrix_symbolic_dense_Matrix_symbolic_dense (matrix_symbolic_dense.c:6534)
==26254==    by 0x808643B: PyDict_Clear (dictobject.c:757)
==26254==    by 0x8086460: dict_clear (dictobject.c:1776)
==26254==    by 0x80CC54A: PyEval_EvalFrameEx (ceval.c:3557)
==26254==    by 0x80CDCA4: PyEval_EvalCodeEx (ceval.c:2836)
==26254==    by 0x8114835: function_call (funcobject.c:517)
==26254==    by 0x805B126: PyObject_Call (abstract.c:1861)
==26254==    by 0x806130E: instancemethod_call (classobject.c:2519)
==26254==    by 0x805B126: PyObject_Call (abstract.c:1861)
==26254==    by 0x80C9D85: PyEval_EvalFrameEx (ceval.c:3784)
==26254==    by 0x80CDCA4: PyEval_EvalCodeEx (ceval.c:2836)
==26254==    by 0x80CC61E: PyEval_EvalFrameEx (ceval.c:3669)
==26254==    by 0x80CDCA4: PyEval_EvalCodeEx (ceval.c:2836)
==26254==    by 0x80CC61E: PyEval_EvalFrameEx (ceval.c:3669)
==26254==    by 0x80CDCA4: PyEval_EvalCodeEx (ceval.c:2836)
==26254==    by 0x80CC61E: PyEval_EvalFrameEx (ceval.c:3669)
==26254==    by 0x80CDCA4: PyEval_EvalCodeEx (ceval.c:2836)
==26254==    by 0x80CDEB6: PyEval_EvalCode (ceval.c:494)
```

The segfault is in auto-generated code:

```
static void __pyx_tp_dealloc_4sage_6matrix_21matrix_symbolic_dense_Matrix_symbolic_dense(PyObject *o) {
  struct __pyx_obj_4sage_6matrix_21matrix_symbolic_dense_Matrix_symbolic_dense 
  *p = (struct __pyx_obj_4sage_6matrix_21matrix_symbolic_dense_Matrix_symbolic_dense *)o;
  Py_XDECREF(p->_maxima);                [this is line 6534]
  Py_XDECREF(p->__variables);
  Py_XDECREF(p->__number_of_args);
  Py_XDECREF(p->_simp);
  __pyx_ptype_4sage_6matrix_12matrix_dense_Matrix_dense->tp_dealloc(o);
}
```

Running it all by itself is clean:

```
[mabshoff@cicero sage-3.2.3.final-cicero]$ ./sage -valgrind
----------------------------------------------------------------------
----------------------------------------------------------------------
/home/mabshoff/build-3.2.3.final/sage-3.2.3.final-cicero/local/bin/sage-ipython
Log file is /home/mabshoff/.sage/valgrind/sage-memcheck.%p
Using default flags:
--leak-resolution=high --leak-check=full --num-callers=25 
--suppressions=/home/mabshoff/build-3.2.3.final/sage-3.2.3.final-cicero/
local/lib/valgrind/sage.supp
==26391== Memcheck, a memory error detector.
==26391== Copyright (C) 2002-2007, and GNU GPL'd, by Julian Seward et al.
==26391== Using LibVEX rev 1854, a library for dynamic binary translation.
==26391== Copyright (C) 2004-2007, and GNU GPL'd, by OpenWorks LLP.
==26391== Using valgrind-3.3.1, a dynamic binary instrumentation framework.
==26391== Copyright (C) 2000-2007, and GNU GPL'd, by Julian Seward et al.
==26391== For more details, rerun with: -v
==26391==
Python 2.5.2 (r252:60911, Jan  3 2009, 15:33:57)
[GCC 4.3.0 20080428 (Red Hat 4.3.0-8)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
sage: a = matrix([[pi, sin(x)], [cos(x), 1/e]]); a
| Sage Version 3.2.3.final, Release Date: 2009-01-02                 |
| Type notebook() for the GUI, and license() for information.        |
[    pi sin(x)]
[cos(x)   e^-1]
sage: a._mathematica_init_()
'{{Pi, Sin[x]}, {Cos[x], (E) ^ (-1)}}'
sage: 
Exiting SAGE (CPU time 0m5.61s, Wall time 3m4.55s).
Exiting spawned Maxima process.
==26391== 
==26391== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 1321 from 1)
==26391== malloc/free: in use at exit: 24,986,088 bytes in 215,178 blocks.
==26391== malloc/free: 783,764 allocs, 568,586 frees, 100,000,527 bytes allocated.
==26391== For counts of detected errors, rerun with: -v
==26391== searching for pointers to 215,178 not-freed blocks.
==26391== checked 30,982,372 bytes.
```

3.2.3.alpha0 with 

```
[mabshoff@cicero sage-3.2.3.alpha0-cicero-gcc432]$ gcc -v
Using built-in specs.
Target: i686-pc-linux-gnu
Configured with: /usr/local/gcc-4.3.2/src/gcc-4.3.2/configure 
--enable-languages=c,c++,fortran 
--with-gmp=/usr/local/gmp-4.2.3/x86-Linux-fc8-gcc-4.3.1 
--with-mpfr=/usr/local/mpfr-2.3.2/x86-Linux-fc8-gmp-4.2.3-gcc-4.3.1 
--prefix=/usr/local/gcc-4.3.2/x86-Linux-fc8
Thread model: posix
gcc version 4.3.2 (GCC) 
```

works fine. But 3.2.3.rc0 with 

```
[mabshoff@cicero sage-3.2.3.alpha0-cicero-gcc432]$ gcc -v
Using built-in specs.
Target: i386-redhat-linux
Configured with: ../configure --prefix=/usr --mandir=/usr/share/man 
--infodir=/usr/share/info --with-bugurl=http://bugzilla.redhat.com/bugzilla 
--enable-bootstrap --enable-shared --enable-threads=posix 
--enable-checking=release --with-system-zlib --enable-__cxa_atexit 
--disable-libunwind-exceptions --enable-languages=c,c++,objc,obj-c++,java,fortran,ada 
--enable-java-awt=gtk --disable-dssi --enable-plugin 
--with-java-home=/usr/lib/jvm/java-1.5.0-gcj-1.5.0.0/jre 
--enable-libgcj-multifile --enable-java-maintainer-mode 
--with-ecj-jar=/usr/share/java/eclipse-ecj.jar 
--disable-libjava-multilib --with-cpu=generic --build=i386-redhat-linux
Thread model: posix
gcc version 4.3.0 20080428 (Red Hat 4.3.0-8) (GCC) 
```

has trouble.

Issue created by migration from https://trac.sagemath.org/ticket/4934





---

archive/issue_comments_037384.json:
```json
{
    "body": "Some debugging info:\n\n```\nI'm getting exactly this test failure in \"make check\" on debian 32 and\n64-bit vanilla (with gcc-4.1.2) under vmware with 1GB RAM and also the\nsame failure on 32-bit Ubuntu 1GB RAM (with gcc-4.3.2):\n\nsage -t  \"devel/sage/sage/matrix/matrix1.pyx\"\nA mysterious error (perphaps a memory error?) occurred, which may have\ncrashed doctest.\n        [4.3 s]\n\nIf I do --verbose I get:\n\nTrying:\n   a._mathematica_init_()###line 171:_sage_    >>> a._mathematica_init_()\nExpecting:\n   '{{Pi, Sin[x]}, {Cos[x], (E) ^ (-1)}}'\nok\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n        [4.9 s]\nexit code: 1024\n\n============================\n\nUnder gdb, I get:\n\nProgram received signal SIGSEGV, Segmentation fault.\n[Switching to Thread 0xb7d5c8c0 (LWP 19059)]\n0xb2d53673 in __pyx_tp_dealloc_4sage_6matrix_21matrix_symbolic_dense_Matrix_symbolic_dense\n(o=0xb57a65c) at sage/matrix/matrix_symbolic_dense.c:6535\n6535      Py_XDECREF(p->__variables);\n(gdb) bt\n#0  0xb2d53673 in\n__pyx_tp_dealloc_4sage_6matrix_21matrix_symbolic_dense_Matrix_symbolic_dense\n(o=0xb57a65c) at sage/matrix/matrix_symbolic_dense.c:6535\n#1  0x0808a1fc in PyDict_Clear (op=0xb3e713c) at Objects/dictobject.c:757\n...\n\n============================\n```\n\n\nI also found a way to stop the problem.  I think this is just programming around a bug in Cython though.   Hopefully the fact that the attached patch stops the will help Robert Bradshaw find the true source of the problem (which I suspect to be a Cython bug).   \n\nAnyway, applying the attached patch would at least make it so we can release sage-3.2.3.   If this is done, though, then another ticket must be opened to fix whatever cython bug (I maintain) caused this.",
    "created_at": "2009-01-05T05:16:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4934#issuecomment-37384",
    "user": "https://github.com/williamstein"
}
```

Some debugging info:

```
I'm getting exactly this test failure in "make check" on debian 32 and
64-bit vanilla (with gcc-4.1.2) under vmware with 1GB RAM and also the
same failure on 32-bit Ubuntu 1GB RAM (with gcc-4.3.2):

sage -t  "devel/sage/sage/matrix/matrix1.pyx"
A mysterious error (perphaps a memory error?) occurred, which may have
crashed doctest.
        [4.3 s]

If I do --verbose I get:

Trying:
   a._mathematica_init_()###line 171:_sage_    >>> a._mathematica_init_()
Expecting:
   '{{Pi, Sin[x]}, {Cos[x], (E) ^ (-1)}}'
ok
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
        [4.9 s]
exit code: 1024

============================

Under gdb, I get:

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0xb7d5c8c0 (LWP 19059)]
0xb2d53673 in __pyx_tp_dealloc_4sage_6matrix_21matrix_symbolic_dense_Matrix_symbolic_dense
(o=0xb57a65c) at sage/matrix/matrix_symbolic_dense.c:6535
6535      Py_XDECREF(p->__variables);
(gdb) bt
#0  0xb2d53673 in
__pyx_tp_dealloc_4sage_6matrix_21matrix_symbolic_dense_Matrix_symbolic_dense
(o=0xb57a65c) at sage/matrix/matrix_symbolic_dense.c:6535
#1  0x0808a1fc in PyDict_Clear (op=0xb3e713c) at Objects/dictobject.c:757
...

============================
```


I also found a way to stop the problem.  I think this is just programming around a bug in Cython though.   Hopefully the fact that the attached patch stops the will help Robert Bradshaw find the true source of the problem (which I suspect to be a Cython bug).   

Anyway, applying the attached patch would at least make it so we can release sage-3.2.3.   If this is done, though, then another ticket must be opened to fix whatever cython bug (I maintain) caused this.



---

archive/issue_comments_037385.json:
```json
{
    "body": "Attachment [trac_4934.patch](tarball://root/attachments/some-uuid/ticket4934/trac_4934.patch) by @williamstein created at 2009-01-05 05:20:13",
    "created_at": "2009-01-05T05:20:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4934#issuecomment-37385",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_4934.patch](tarball://root/attachments/some-uuid/ticket4934/trac_4934.patch) by @williamstein created at 2009-01-05 05:20:13



---

archive/issue_comments_037386.json:
```json
{
    "body": "Looks good to me and fixes the issue. I am still valgrinding and testing, so having a second reviewer won't hurt here.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-05T05:46:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4934#issuecomment-37386",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Looks good to me and fixes the issue. I am still valgrinding and testing, so having a second reviewer won't hurt here.

Cheers,

Michael



---

archive/issue_comments_037387.json:
```json
{
    "body": "The offending file now valgrinds clean, but I am running a full doctest run on the machine to make 100% sure nothing else gets broken by accident.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-05T06:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4934#issuecomment-37387",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The offending file now valgrinds clean, but I am running a full doctest run on the machine to make 100% sure nothing else gets broken by accident.

Cheers,

Michael



---

archive/issue_comments_037388.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-06T01:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4934#issuecomment-37388",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037389.json:
```json
{
    "body": "Merged in Sage 3.2.3.post-final\n\nCheers,\n\nMichael",
    "created_at": "2009-01-06T01:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4934#issuecomment-37389",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.3.post-final

Cheers,

Michael
