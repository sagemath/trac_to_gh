# Issue 6209: fix flint

Issue created by migration from https://trac.sagemath.org/ticket/6209

Original creator: was

Original creation time: 2009-06-04 17:02:22

Assignee: tbd


```
in fmpz.c change

#include "zn_poly/zn_poly.h"

to

#include "zn_poly/src/zn_poly.h"

Also, in the FLINT makefile

-DNEBUG -> -DNDEBUG

in a couple of places. David Harvey found these.

These will fix the issues you note. The next version of FLINT due at
the end of June will have these fixes.

 -- Bill Hart
```



---

Comment by mhansen created at 2009-06-04 17:53:02

Changing status from new to assigned.


---

Comment by mhansen created at 2009-06-04 17:53:02

I've made these changes and put them in http://sage.math.washington.edu/home/mhansen/flint-1.2.5.p0.spkg


---

Comment by mhansen created at 2009-06-04 17:53:02

Changing assignee from tbd to mhansen.


---

Comment by wbhart created at 2009-06-04 19:16:29

The fmpz.c file still has #include "zn_poly/zn_poly.h"


---

Comment by mhansen created at 2009-06-04 19:17:45

Did you look in the fmpz.c file in the patches/directory?  That overwrites the one in the the src/ before the build.


---

Comment by wbhart created at 2009-06-04 19:39:35

Sorry, my mistake. It's fixed in patches not src indeed!!


---

Comment by mhansen created at 2009-06-04 19:39:59

Resolution: fixed


---

Comment by mhansen created at 2009-06-04 19:39:59

Merged in 4.0.1.rc1.
