# Issue 2344: python -- upgrade to version 2.5.2

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-28 06:04:33

Assignee: mabshoff

CC:  robertwb

Currently Sage ships with Python 2.5.1, but Python 2.5.2 was released on Feb 22, 2008, so we should try it out. 

http://python.org/download/


---

Comment by mabshoff created at 2008-03-26 09:52:56

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-03-26 09:52:56

Python 2.5.2 solves a number of compilation issues:

 * 64 bit build support on OSX 10.5 without the need to patch anything
 * 64 bit build support on Solaris 10 with Sun Forte 10

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-26 10:33:09

Ahh, after fearing that this could be another one of the WORST SPKG EVER all of our patches apply cleanly to 2.5.2:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha2/spkg/standard/python-2.5.2/src-patched$ patch -p1 --dry-run < ../readline-Itanium-fix.patch
patching file Modules/readline.c
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha2/spkg/standard/python-2.5.2/src-patched$ patch -p1 --dry-run < ../Sage-help-fix.patch
patching file Lib/pkgutil.py
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha2/spkg/standard/python-2.5.2/src-patched$ patch -p1 --dry-run < ../local.py-fixes.patch
patching file Lib/locale.py
Hunk #1 succeeded at 28 (offset 2 lines).
Hunk #2 succeeded at 489 (offset 2 lines).
Hunk #3 succeeded at 513 (offset 2 lines).
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha2/spkg/standard/python-2.5.2/src-patched$ patch -p1 --dry-run < ../ctypes__init__.patch
patching file Lib/ctypes/__init__.py
```


Cheers,

Micahael


---

Comment by mabshoff created at 2008-03-26 11:41:48

The updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/alpha2/python-2.5.2.spkg

It builds fine on x86, x86-64 Linux and OSX. It has OSX 10.5 64 bit support, but that is untested at the moment. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-26 12:55:15

There is some trouble on OSX 10.5 [even after a sage -ba]:

```
bsd:sage-2.11.alpha1-32bit mabshoff$ ./sage -t devel/sage-main/sage/rings/integer.pyx
sage -t  devel/sage-main/sage/rings/integer.pyx

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------


A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
         [4.8 s]
exit code: 768

----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage-main/sage/rings/integer.pyx
Total time for all tests: 4.8 seconds
```

Running the same code under gdb works fine. On the other hand `-verbose` tells us:

```
<SNIP>
Trying:
    n=Integer(100)###line 930:_sage_    >>> n=100
Expecting nothing
ok
Trying:
    n.set_str('100000',Integer(2))###line 931:_sage_    >>> n.set_str('100000',2)
Expecting nothing
ok
Trying:
    n###line 932:_sage_    >>> n
Expecting:
    32
ok


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```

We also have some trouble in dancing_links.pyx:

```
sage -t -long devel/sage-main/sage/combinat/matrices/dancing_links.pyx
**********************************************************************
File "dancing_links.pyx", line 135:
    sage: X = dlx_solver(rows)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.11.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[1]>", line 1, in <module>
        X = dlx_solver(rows)###line 135:
    sage: X = dlx_solver(rows)
    NameError: name 'dlx_solver' is not defined
**********************************************************************
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-03-26 13:24:48

I have moved the spkg to

http://sage.math.washington.edu/home/mabshoff/SPKG/python-2.5.2.spkg

for now.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-26 14:05:24

It seems that the following is the offending bug that causes the segfault on OSX:

```
==27080== Conditional jump or move depends on uninitialised value(s)
==27080==    at 0x6FAB622: modii (in /scratch/mabshoff/release-cycle/sage-2.11.alpha2/local/lib/libpari-gmp.so.2)
==27080==    by 0xB5C6DF7: __pyx_pf_4sage_4libs_4pari_3gen_3gen__mod (gen.c:2760)
==27080==    by 0x415832: PyObject_Call (abstract.c:1861)
==27080==    by 0xB5CB3E6: __pyx_pf_4sage_4libs_4pari_3gen_3gen___mod__ (gen.c:2825)
==27080==    by 0x415AFC: binary_op1 (abstract.c:398)
==27080==    by 0x416EAD: PyNumber_Remainder (abstract.c:450)
==27080==    by 0x7594FED: op_mod (operator.c:77)
==27080==    by 0x415832: PyObject_Call (abstract.c:1861)
==27080==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==27080==    by 0xA412A08: __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_bin_op_c (coerce.c:5158)
==27080==    by 0xA17E9E9: __pyx_pf_4sage_9structure_7element_bin_op (element.c:17105)
==27080==    by 0x415832: PyObject_Call (abstract.c:1861)
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-03-26 15:13:30

The dancing_links.pyx import error also happens with python-2.5.1.p13. So all we need to solve is the integer.pyx segfault issue.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-28 20:54:25

Note that I did another python.spkg, so that there need to be some changes backported to this spkg.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-19 22:48:09

With 3.0.alpha6 and Python 2.5.2 all doctests pass with long. William couldn't reproduce the above mentioned failure on his MacPB either, but he is also testing with 3.0.alpha6 on bsd.

Cheers,

Michael


---

Comment by was created at 2008-04-20 01:37:58

This just works for me on every mac I try... so positive review.


---

Comment by mabshoff created at 2008-04-20 01:38:35

Resolution: fixed


---

Comment by mabshoff created at 2008-04-20 01:38:35

Merged in Sage 3.0.rc0
