# Issue 204: bug in real number comparison or coercion

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-01-21 03:45:11

Assignee: somebody

from Yi


```
Ok, here is a weird bug:
on sage.math.washington.edu
 
sage: sys.maxint
9223372036854775807
sage: sys.maxint >= 0.01
False
 
sage: sys.maxint >= int(0.01)
True
 
Looks to be a problem with <type 'sage.rings.real_mpfr.RealNumber'>
 
Any ideas on how to fix this?
```



---

Comment by was created at 2007-01-21 03:47:59


```
It's a coercion issue:

import sys
sage: sys.maxint
9223372036854775807
sage: type(sys.maxint)
<type 'int'>
sage: RR(sys.maxint)
-1.00000000000000
sage: RDF(sys.maxint)
9.22337203685e+18
sage: RealField(100)(sys.maxint)
-1.0000000000000000000000000000
```



---

Comment by was created at 2007-01-23 21:50:33

This is now fixed for sage > 1.8.  The problem in involved the 
real number constructor.   While I was at it, I optimized that a lot.


---

Comment by was created at 2007-01-23 21:50:33

Resolution: fixed
