# Issue 2344: python -- upgrade to version 2.5.2

archive/issues_002344.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @robertwb\n\nCurrently Sage ships with Python 2.5.1, but Python 2.5.2 was released on Feb 22, 2008, so we should try it out. \n\nhttp://python.org/download/\n\nIssue created by migration from https://trac.sagemath.org/ticket/2344\n\n",
    "created_at": "2008-02-28T06:04:33Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "python -- upgrade to version 2.5.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2344",
    "user": "@williamstein"
}
```
Assignee: mabshoff

CC:  @robertwb

Currently Sage ships with Python 2.5.1, but Python 2.5.2 was released on Feb 22, 2008, so we should try it out. 

http://python.org/download/

Issue created by migration from https://trac.sagemath.org/ticket/2344





---

archive/issue_comments_015690.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-26T09:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2344#issuecomment-15690",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015691.json:
```json
{
    "body": "Python 2.5.2 solves a number of compilation issues:\n\n* 64 bit build support on OSX 10.5 without the need to patch anything\n* 64 bit build support on Solaris 10 with Sun Forte 10\n\nCheers,\n\nMichael",
    "created_at": "2008-03-26T09:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2344#issuecomment-15691",
    "user": "mabshoff"
}
```

Python 2.5.2 solves a number of compilation issues:

* 64 bit build support on OSX 10.5 without the need to patch anything
* 64 bit build support on Solaris 10 with Sun Forte 10

Cheers,

Michael



---

archive/issue_comments_015692.json:
```json
{
    "body": "Ahh, after fearing that this could be another one of the WORST SPKG EVER all of our patches apply cleanly to 2.5.2:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha2/spkg/standard/python-2.5.2/src-patched$ patch -p1 --dry-run < ../readline-Itanium-fix.patch\npatching file Modules/readline.c\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha2/spkg/standard/python-2.5.2/src-patched$ patch -p1 --dry-run < ../Sage-help-fix.patch\npatching file Lib/pkgutil.py\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha2/spkg/standard/python-2.5.2/src-patched$ patch -p1 --dry-run < ../local.py-fixes.patch\npatching file Lib/locale.py\nHunk #1 succeeded at 28 (offset 2 lines).\nHunk #2 succeeded at 489 (offset 2 lines).\nHunk #3 succeeded at 513 (offset 2 lines).\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha2/spkg/standard/python-2.5.2/src-patched$ patch -p1 --dry-run < ../ctypes__init__.patch\npatching file Lib/ctypes/__init__.py\n```\n\n\nCheers,\n\nMicahael",
    "created_at": "2008-03-26T10:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2344#issuecomment-15692",
    "user": "mabshoff"
}
```

Ahh, after fearing that this could be another one of the WORST SPKG EVER all of our patches apply cleanly to 2.5.2:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha2/spkg/standard/python-2.5.2/src-patched$ patch -p1 --dry-run < ../readline-Itanium-fix.patch
patching file Modules/readline.c
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha2/spkg/standard/python-2.5.2/src-patched$ patch -p1 --dry-run < ../Sage-help-fix.patch
patching file Lib/pkgutil.py
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha2/spkg/standard/python-2.5.2/src-patched$ patch -p1 --dry-run < ../local.py-fixes.patch
patching file Lib/locale.py
Hunk #1 succeeded at 28 (offset 2 lines).
Hunk #2 succeeded at 489 (offset 2 lines).
Hunk #3 succeeded at 513 (offset 2 lines).
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha2/spkg/standard/python-2.5.2/src-patched$ patch -p1 --dry-run < ../ctypes__init__.patch
patching file Lib/ctypes/__init__.py
```


Cheers,

Micahael



---

archive/issue_comments_015693.json:
```json
{
    "body": "The updated spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/alpha2/python-2.5.2.spkg\n\nIt builds fine on x86, x86-64 Linux and OSX. It has OSX 10.5 64 bit support, but that is untested at the moment. \n\nCheers,\n\nMichael",
    "created_at": "2008-03-26T11:41:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2344#issuecomment-15693",
    "user": "mabshoff"
}
```

The updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/alpha2/python-2.5.2.spkg

It builds fine on x86, x86-64 Linux and OSX. It has OSX 10.5 64 bit support, but that is untested at the moment. 

Cheers,

Michael



---

archive/issue_comments_015694.json:
```json
{
    "body": "There is some trouble on OSX 10.5 [even after a sage -ba]:\n\n```\nbsd:sage-2.11.alpha1-32bit mabshoff$ ./sage -t devel/sage-main/sage/rings/integer.pyx\nsage -t  devel/sage-main/sage/rings/integer.pyx\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n         [4.8 s]\nexit code: 768\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  devel/sage-main/sage/rings/integer.pyx\nTotal time for all tests: 4.8 seconds\n```\n\nRunning the same code under gdb works fine. On the other hand `-verbose` tells us:\n\n```\n<SNIP>\nTrying:\n    n=Integer(100)###line 930:_sage_    >>> n=100\nExpecting nothing\nok\nTrying:\n    n.set_str('100000',Integer(2))###line 931:_sage_    >>> n.set_str('100000',2)\nExpecting nothing\nok\nTrying:\n    n###line 932:_sage_    >>> n\nExpecting:\n    32\nok\n\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n```\n\nWe also have some trouble in dancing_links.pyx:\n\n```\nsage -t -long devel/sage-main/sage/combinat/matrices/dancing_links.pyx\n**********************************************************************\nFile \"dancing_links.pyx\", line 135:\n    sage: X = dlx_solver(rows)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha2/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_4[1]>\", line 1, in <module>\n        X = dlx_solver(rows)###line 135:\n    sage: X = dlx_solver(rows)\n    NameError: name 'dlx_solver' is not defined\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-03-26T12:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2344#issuecomment-15694",
    "user": "mabshoff"
}
```

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

archive/issue_comments_015695.json:
```json
{
    "body": "I have moved the spkg to\n\nhttp://sage.math.washington.edu/home/mabshoff/SPKG/python-2.5.2.spkg\n\nfor now.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-26T13:24:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2344#issuecomment-15695",
    "user": "mabshoff"
}
```

I have moved the spkg to

http://sage.math.washington.edu/home/mabshoff/SPKG/python-2.5.2.spkg

for now.

Cheers,

Michael



---

archive/issue_comments_015696.json:
```json
{
    "body": "It seems that the following is the offending bug that causes the segfault on OSX:\n\n```\n==27080== Conditional jump or move depends on uninitialised value(s)\n==27080==    at 0x6FAB622: modii (in /scratch/mabshoff/release-cycle/sage-2.11.alpha2/local/lib/libpari-gmp.so.2)\n==27080==    by 0xB5C6DF7: __pyx_pf_4sage_4libs_4pari_3gen_3gen__mod (gen.c:2760)\n==27080==    by 0x415832: PyObject_Call (abstract.c:1861)\n==27080==    by 0xB5CB3E6: __pyx_pf_4sage_4libs_4pari_3gen_3gen___mod__ (gen.c:2825)\n==27080==    by 0x415AFC: binary_op1 (abstract.c:398)\n==27080==    by 0x416EAD: PyNumber_Remainder (abstract.c:450)\n==27080==    by 0x7594FED: op_mod (operator.c:77)\n==27080==    by 0x415832: PyObject_Call (abstract.c:1861)\n==27080==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)\n==27080==    by 0xA412A08: __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_bin_op_c (coerce.c:5158)\n==27080==    by 0xA17E9E9: __pyx_pf_4sage_9structure_7element_bin_op (element.c:17105)\n==27080==    by 0x415832: PyObject_Call (abstract.c:1861)\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-03-26T14:05:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2344#issuecomment-15696",
    "user": "mabshoff"
}
```

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

archive/issue_comments_015697.json:
```json
{
    "body": "The dancing_links.pyx import error also happens with python-2.5.1.p13. So all we need to solve is the integer.pyx segfault issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-26T15:13:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2344#issuecomment-15697",
    "user": "mabshoff"
}
```

The dancing_links.pyx import error also happens with python-2.5.1.p13. So all we need to solve is the integer.pyx segfault issue.

Cheers,

Michael



---

archive/issue_comments_015698.json:
```json
{
    "body": "Note that I did another python.spkg, so that there need to be some changes backported to this spkg.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-28T20:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2344#issuecomment-15698",
    "user": "mabshoff"
}
```

Note that I did another python.spkg, so that there need to be some changes backported to this spkg.

Cheers,

Michael



---

archive/issue_comments_015699.json:
```json
{
    "body": "With 3.0.alpha6 and Python 2.5.2 all doctests pass with long. William couldn't reproduce the above mentioned failure on his MacPB either, but he is also testing with 3.0.alpha6 on bsd.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-19T22:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2344#issuecomment-15699",
    "user": "mabshoff"
}
```

With 3.0.alpha6 and Python 2.5.2 all doctests pass with long. William couldn't reproduce the above mentioned failure on his MacPB either, but he is also testing with 3.0.alpha6 on bsd.

Cheers,

Michael



---

archive/issue_comments_015700.json:
```json
{
    "body": "This just works for me on every mac I try... so positive review.",
    "created_at": "2008-04-20T01:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2344#issuecomment-15700",
    "user": "@williamstein"
}
```

This just works for me on every mac I try... so positive review.



---

archive/issue_comments_015701.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-20T01:38:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2344#issuecomment-15701",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015702.json:
```json
{
    "body": "Merged in Sage 3.0.rc0",
    "created_at": "2008-04-20T01:38:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2344#issuecomment-15702",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.rc0
