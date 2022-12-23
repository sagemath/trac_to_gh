# Issue 226: sagex enum issue and solution

Issue created by migration from https://trac.sagemath.org/ticket/226

Original creator: was

Original creation time: 2007-01-28 20:27:20

Assignee: was


```
The following code compiled just fine with 0.9.4.1
 
cdef extern from "whatever.h":
    ctypedef enum someenum_t:
        ENUMVALUE_1
        ENUMVALUE_2
 
cdef somefunction(someenum_t val):
    if val == ENUMVALUE_1:
        print "1"
    else:
        print "2"
 
 
With 0.9.5 it gives the following error:
/tmp/Pyrex-0.9.5/regression.pyx:8:11: Invalid types for '=='
(someenum_t, someenum_t)
 
 
 anders
 
 
_______________________________________________
Pyrex mailing list
Pyrex@lists.copyleft.no
http://lists.copyleft.no/mailman/listinfo/pyrex
--------

I wrote:
> /tmp/Pyrex-0.9.5/regression.pyx:8:11: Invalid types for '=='
> (someenum_t, someenum_t)
 
This patch seems to help, but I don't know enough pyrex internals to
tell if it is the correct solution.
 
--- Pyrex-0.9.5/Pyrex/Compiler/ExprNodes.py     2007-01-27
05:21:03.000000000 +0100
+++ Pyrex-0.9.5-enumcmpfix/Pyrex/Compiler/ExprNodes.py  2007-01-28
16:14:45.366599915 +0100
@@ -2594,6 +2594,8 @@
         elif (type1.is_numeric and type2.is_numeric
                 and op not in ('is', 'is_not')):
             return 1
+        elif (type1.is_enum and type2.is_enum):
+            return 1
         else:
             return 0
 
 
 
_______________________________________________
Pyrex mailing list
Pyrex@lists.copyleft.no
http://lists.copyleft.no/mailman/listinfo/pyrex
```



---

Comment by mabshoff created at 2007-08-18 17:48:12

Resolution: fixed


---

Comment by mabshoff created at 2007-08-18 17:48:12

The problem has been fixed in a previous release of cython.
cython regression.pyx now works fine.
