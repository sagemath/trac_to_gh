# Issue 1260: clean up spkg-install for FLINT [flint-0.9-r1075.px]

archive/issues_001260.json:
```json
{
    "body": "Assignee: mabshoff\n\nToward the end of http://groups.google.com/group/sage-devel/t/7fad3e24f3777d92 Bill says:\n\n```\nThe new build system for FLINT has the dylib stuff in it already. If\nyou do make library, it should make a dylib if you are compiling on\nDarwin. (If you have other systems you want to compile a dylib instead\nof a .so, just edit the file flint_env in the FLINT trunk and send me\nthe modifications and I'll commit them.)\n\nThe only things spkg_install should need to do is:\n\n1) Tell it where GMP is, i.e:\n\nexport FLINT_GMP_LIB_DIR=....\nexport FLINT_GMP_INCLUDE_DIR=....\n\n2) Make sure LD_LIBRARY_PATH has the GMP library path in it (currently\nif LD_LIBRARY_PATH is empty FLINT sets it to FLINT_GMP_LIB_DIR,\notherwise it assumes you set it yourself)\n\n3) source flint_env\n\n4) make library\n\n5) Move the library and header files to wherever you need them to be\n\nEverything else should be done by flint_env automatically, including\nall the platform specific stuff. If not, let me know and I'll fix it.\n\nSimilarly if you are building the test programs, you'd do the above\nbut with make test instead of make library. There is also make\nexamples, make tune (only makes the tuning targets at this point,\ndoesn't run them, and they aren't ready to be used yet), make profiles\n(again just makes profiling programs, doesn't do anything with them)\nand make all (does all of the above except it doesn't make a library).\n\nEventually SAGE will want to build FLINT by doing make tune before\nmake library. But this is not useful yet.\n\nBill. \n```\n\nand later\n\n```\nMichael,\n\nIs there a simple way to either:\n\n1) Use a bash script to parse the existing $LD_LIBRARY_PATH to see if\none of the path strings it contains is equal to $FLINT_GMP_LIB_DIR\n\n2) Add $FLINT_GMP_LIB_DIR to $LD_LIBRARY_PATH if it isn't already in\nthere (I see how to add it whether or not it is in there, but this\ncould lead to a duplicate path string)\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1260\n\n",
    "created_at": "2007-11-25T04:47:41Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "clean up spkg-install for FLINT [flint-0.9-r1075.px]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1260",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Toward the end of http://groups.google.com/group/sage-devel/t/7fad3e24f3777d92 Bill says:

```
The new build system for FLINT has the dylib stuff in it already. If
you do make library, it should make a dylib if you are compiling on
Darwin. (If you have other systems you want to compile a dylib instead
of a .so, just edit the file flint_env in the FLINT trunk and send me
the modifications and I'll commit them.)

The only things spkg_install should need to do is:

1) Tell it where GMP is, i.e:

export FLINT_GMP_LIB_DIR=....
export FLINT_GMP_INCLUDE_DIR=....

2) Make sure LD_LIBRARY_PATH has the GMP library path in it (currently
if LD_LIBRARY_PATH is empty FLINT sets it to FLINT_GMP_LIB_DIR,
otherwise it assumes you set it yourself)

3) source flint_env

4) make library

5) Move the library and header files to wherever you need them to be

Everything else should be done by flint_env automatically, including
all the platform specific stuff. If not, let me know and I'll fix it.

Similarly if you are building the test programs, you'd do the above
but with make test instead of make library. There is also make
examples, make tune (only makes the tuning targets at this point,
doesn't run them, and they aren't ready to be used yet), make profiles
(again just makes profiling programs, doesn't do anything with them)
and make all (does all of the above except it doesn't make a library).

Eventually SAGE will want to build FLINT by doing make tune before
make library. But this is not useful yet.

Bill. 
```

and later

```
Michael,

Is there a simple way to either:

1) Use a bash script to parse the existing $LD_LIBRARY_PATH to see if
one of the path strings it contains is equal to $FLINT_GMP_LIB_DIR

2) Add $FLINT_GMP_LIB_DIR to $LD_LIBRARY_PATH if it isn't already in
there (I see how to add it whether or not it is in there, but this
could lead to a duplicate path string)
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1260





---

archive/issue_comments_007878.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-25T04:48:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1260#issuecomment-7878",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007879.json:
```json
{
    "body": "The new spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/flint-1.0.spkg\n\nCheers,\n\nMichael",
    "created_at": "2007-12-06T20:50:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1260#issuecomment-7879",
    "user": "mabshoff"
}
```

The new spkg is at

http://sage.math.washington.edu/home/mabshoff/flint-1.0.spkg

Cheers,

Michael



---

archive/issue_comments_007880.json:
```json
{
    "body": "Merged in 2.9.alpha1.",
    "created_at": "2007-12-06T20:51:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1260#issuecomment-7880",
    "user": "mabshoff"
}
```

Merged in 2.9.alpha1.



---

archive/issue_comments_007881.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-06T20:51:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1260#issuecomment-7881",
    "user": "mabshoff"
}
```

Resolution: fixed
