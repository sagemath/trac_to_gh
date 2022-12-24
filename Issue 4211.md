# Issue 4211: new optional spkg: guppy

archive/issues_004211.json:
```json
{
    "body": "Assignee: mabshoff\n\nFrom http://pypi.python.org/pypi/guppy/0.1.8:\n\nGuppy-PE is a library and programming environment for Python, currently providing in particular the Heapy subsystem, which supports object and heap memory sizing, profiling and debugging. It also includes a prototypical specification language, the Guppy Specificaion Language (GSL), which can be used to formally specify aspects of Python programs and generate tests and documentation from a common source.\n\nThis should help us track down some interesting issues :)\n\nCheers,\n\nMichael\n\nA sample session:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.1.3.alpha1, Release Date: 2008-09-24                |\n| Type notebook() for the GUI, and license() for information.        |\nsage: from guppy import hpy; h=hpy()\nsage: h.heap()           \n\nPartition of a set of 301445 objects. Total size = 46220768 bytes.\n Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)\n     0 140520  47 20492952  44  20492952  44 str\n     1  79975  27  6936840  15  27429792  59 tuple\n     2   1297   0  3251608   7  30681400  66 dict of module\n     3  22307   7  2676840   6  33358240  72 types.CodeType\n     4  21938   7  2632560   6  35990800  78 function\n     5   2531   1  2427464   5  38418264  83 dict of type\n     6   2531   1  2214200   5  40632464  88 type\n     7   2312   1  1674560   4  42307024  92 dict (no owner)\n     8    670   0   682192   1  42989216  93 dict of class\n     9   4935   2   355320   1  43344536  94 __builtin__.method_descriptor\n<736 more rows. Type e.g. '_.more' to view.>\nsage: h.iso(1,[],{})\n\nPartition of a set of 3 objects. Total size = 400 bytes.\n Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)\n     0      1  33      280  70       280  70 dict (no owner)\n     1      1  33       72  18       352  88 list\n     2      1  33       48  12       400 100 sage.rings.integer.Integer\nsage: h.iso(2,[],{})\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4211\n\n",
    "created_at": "2008-09-27T22:53:53Z",
    "labels": [
        "packages: optional",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "new optional spkg: guppy",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4211",
    "user": "mabshoff"
}
```
Assignee: mabshoff

From http://pypi.python.org/pypi/guppy/0.1.8:

Guppy-PE is a library and programming environment for Python, currently providing in particular the Heapy subsystem, which supports object and heap memory sizing, profiling and debugging. It also includes a prototypical specification language, the Guppy Specificaion Language (GSL), which can be used to formally specify aspects of Python programs and generate tests and documentation from a common source.

This should help us track down some interesting issues :)

Cheers,

Michael

A sample session:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.3.alpha1, Release Date: 2008-09-24                |
| Type notebook() for the GUI, and license() for information.        |
sage: from guppy import hpy; h=hpy()
sage: h.heap()           

Partition of a set of 301445 objects. Total size = 46220768 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0 140520  47 20492952  44  20492952  44 str
     1  79975  27  6936840  15  27429792  59 tuple
     2   1297   0  3251608   7  30681400  66 dict of module
     3  22307   7  2676840   6  33358240  72 types.CodeType
     4  21938   7  2632560   6  35990800  78 function
     5   2531   1  2427464   5  38418264  83 dict of type
     6   2531   1  2214200   5  40632464  88 type
     7   2312   1  1674560   4  42307024  92 dict (no owner)
     8    670   0   682192   1  42989216  93 dict of class
     9   4935   2   355320   1  43344536  94 __builtin__.method_descriptor
<736 more rows. Type e.g. '_.more' to view.>
sage: h.iso(1,[],{})

Partition of a set of 3 objects. Total size = 400 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0      1  33      280  70       280  70 dict (no owner)
     1      1  33       72  18       352  88 list
     2      1  33       48  12       400 100 sage.rings.integer.Integer
sage: h.iso(2,[],{})
```


Issue created by migration from https://trac.sagemath.org/ticket/4211





---

archive/issue_comments_030600.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-27T22:54:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4211#issuecomment-30600",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030601.json:
```json
{
    "body": "The spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha2/guppy-0.1.8.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-09-27T22:55:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4211#issuecomment-30601",
    "user": "mabshoff"
}
```

The spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha2/guppy-0.1.8.spkg

Cheers,

Michael



---

archive/issue_comments_030602.json:
```json
{
    "body": "Also: check out the tutorial at\n\nhttp://www.pkgcore.org/trac/pkgcore/doc/dev-notes/heapy.rst\n\nCheers,\n\nMichael",
    "created_at": "2008-09-27T22:56:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4211#issuecomment-30602",
    "user": "mabshoff"
}
```

Also: check out the tutorial at

http://www.pkgcore.org/trac/pkgcore/doc/dev-notes/heapy.rst

Cheers,

Michael



---

archive/issue_comments_030603.json:
```json
{
    "body": "Nice.  +1 to the optional spkg",
    "created_at": "2008-09-27T22:59:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4211#issuecomment-30603",
    "user": "mhansen"
}
```

Nice.  +1 to the optional spkg



---

archive/issue_comments_030604.json:
```json
{
    "body": "Merged in the optional spkg repo in Sage 3.1.3.alpha2",
    "created_at": "2008-09-27T23:02:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4211#issuecomment-30604",
    "user": "mabshoff"
}
```

Merged in the optional spkg repo in Sage 3.1.3.alpha2



---

archive/issue_comments_030605.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-27T23:02:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4211#issuecomment-30605",
    "user": "mabshoff"
}
```

Resolution: fixed
