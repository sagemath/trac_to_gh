# Issue 3357: [with patch, needs review] Refactor pool code in integer.pyx

Issue created by migration from https://trac.sagemath.org/ticket/3357

Original creator: gfurnish

Original creation time: 2008-06-03 07:15:22

Assignee: somebody

CC:  robertwb

This patch moves some of the setup code from integer.pyx into misc.memory and creates a ext/python_rich_object.pxi file.  This patch makes it easy to generalize pools to other classes, and is needed for symbolics. 


---

Comment by gfurnish created at 2008-06-03 07:22:08

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-06-03 07:22:08

Changing assignee from somebody to gfurnish.


---

Comment by robertwb created at 2008-06-04 05:12:29

- You appear to have multiple change-sets in this one patch, which may be problematic for importing (though it worked fine for me). 

- The name "memory.pyx" I would probably call it something like "allocate.pyx" which gives a better impression of what it does. 

- Why are pool_stats, etc. added to sage/misc/memory.pyx, but then commented out? 

- Sage doesn't start up anymore. It's an import error, so it looks like an easy fix, but I'm wary of code that you haven't even tested.


---

Comment by gfurnish created at 2008-06-04 09:26:23

-The changeset issue should work correctly (I just exported two patches directly in a row)
-Namechange sounds decent enough
-The code to make them work is commented out in all pool allocators, so they are there, but they arn't actually used (in current code or in this one)
-Sage starts up for me, and in fact it works better then usual.. What did you apply the patch against?


---

Comment by mabshoff created at 2008-06-04 21:44:27

The problem here is that the old build system does not know about memory.[pyx|lxd] because then I get:

```
sage -t -long devel/sage/sage/structure/wrapper_parent.pyx
Traceback (most recent call last):
  File "/scratch/mabshoff/release-cycle/sage-3.0.2-vg/tmp/.doctest_wrapper_parent.py", line 2, in <module>
    from sage.all_cmdline import *;
  File "/scratch/mabshoff/release-cycle/sage-3.0.2-vg/local/lib/python2.5/site-packages/sage/all_cmdline.py", line 14, in <module>
    from sage.all import *
  File "/scratch/mabshoff/release-cycle/sage-3.0.2-vg/local/lib/python2.5/site-packages/sage/all.py", line 58, in <module>
    from sage.misc.all       import *         # takes a while
  File "/scratch/mabshoff/release-cycle/sage-3.0.2-vg/local/lib/python2.5/site-packages/sage/misc/all.py", line 76, in <module>
    from functional import (additive_order,
  File "/scratch/mabshoff/release-cycle/sage-3.0.2-vg/local/lib/python2.5/site-packages/sage/misc/functional.py", line 34, in <module>
    from sage.rings.complex_double import CDF
  File "integer.pxd", line 9, in sage.rings.complex_double (sage/rings/complex_double.c:9324)
  File "integer.pyx", line 1, in sage.rings.integer (sage/rings/integer.c:22427)
ImportError: No module named memory
```


As Robert suggested it might also be a good idea to renames memory.$FOO to allocator.$FOO.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-04 21:47:23

This fixes at least the build issue:

```
--- a/setup.py  Sat May 24 16:03:19 2008 -0700
+++ b/setup.py  Wed Jun 04 14:46:10 2008 -0700
@@ -720,6 +720,9 @@ ext_modules = [ \
     Extension('sage.rings.integer',
               sources = ['sage/ext/arith.pyx', 'sage/rings/integer.pyx'],
               libraries=['ntl', 'gmp']), \
+
+    Extension('sage.misc.memory',
+                  sources = ['sage/misc/memory.pyx']), \

     Extension('sage.rings.integer_ring',
               sources = ['sage/rings/integer_ring.pyx'],
```


Now doctesting & valgrinding ....

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-05 18:33:36

Ok, the whole doctest suite valgrinds clean on sage.math. I will merge this patch provided:

 * it doctests clean on OSX
 * Robert signs off on it
 * memory.[pyx|pxd] gets renamed to allocator.[pyx|pxd]
 * the setup.py issue gets fixed

Cheers,

Michael


---

Attachment

new patch


---

Comment by mabshoff created at 2008-06-06 03:39:46

Arrg, on OSX this patch causes some doctests to use 100% of the CPU without them making any progress. I have not attempted to debug this, but affected doctests inlcude

 * devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py

but there are others.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-06 04:48:14

Ok, as it turns out that tree did not doctest correctly without the patch anyway, so I am building a fresh 3.0.3.a1 tree to test. Apologies for the trouble, looks like I will have to ride on the short bus and wear my helmet ;)

Cheers,

Michael


---

Comment by robertwb created at 2008-06-09 20:20:39

Pending all doctests passing I give this a positive review. There is still too much "manual magic" in the integer.pyx file that I'd like to factor out, but that will be for another patch. Perhaps we could work something out at dev days coming up?


---

Comment by mabshoff created at 2008-06-11 03:44:39

Resolution: fixed


---

Comment by mabshoff created at 2008-06-11 03:44:39

Merged in Sage 3.0.3.alpha2 since doctests pass for me
