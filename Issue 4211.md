# Issue 4211: new optional spkg: guppy

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-09-27 22:53:53

Assignee: mabshoff

From http://pypi.python.org/pypi/guppy/0.1.8:

Guppy-PE is a library and programming environment for Python, currently providing in particular the Heapy subsystem, which supports object and heap memory sizing, profiling and debugging. It also includes a prototypical specification language, the Guppy Specificaion Language (GSL), which can be used to formally specify aspects of Python programs and generate tests and documentation from a common source.

This should help us track down some interesting issues :)

Cheers,

Michael

A sample session:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2$ ./sage
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



---

Comment by mabshoff created at 2008-09-27 22:54:09

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-09-27 22:55:36

The spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha2/guppy-0.1.8.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-27 22:56:18

Also: check out the tutorial at

http://www.pkgcore.org/trac/pkgcore/doc/dev-notes/heapy.rst

Cheers,

Michael


---

Comment by mhansen created at 2008-09-27 22:59:08

Nice.  +1 to the optional spkg


---

Comment by mabshoff created at 2008-09-27 23:02:21

Merged in the optional spkg repo in Sage 3.1.3.alpha2


---

Comment by mabshoff created at 2008-09-27 23:02:21

Resolution: fixed
