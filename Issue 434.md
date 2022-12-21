# Issue 434: bug in mwrank interface -- something doesn't work

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-08-17 14:31:18

Assignee: was


```
Testing this using sage I found that the command
mwrank_set_precision() does not work:

sage: mwrank_set_precision(30)
---------------------------------------------------------------------------
<type 'exceptions.ImportError'>           Traceback (most recent call last)

/home/jec/gp/<ipython console> in <module>()

/home/jec/sage-2.7/local/lib/python2.5/site-packages/sage/libs/mwrank/interface.py
in set_precision(n)
    27         n -- long
    28     """
---> 29     from sage.libs.mwrank.mwrank import _set_precision #
import here to save time
    30     _set_precision(n)
    31

<type 'exceptions.ImportError'>: cannot import name _set_precision

-- can you fix that?  [Also, while preparing this email:  version() returns
sage: version()
 'SAGE Version 2.7.3, Release Date: 2007-08-02'

although this is 2.8 (accor
```



---

Comment by was created at 2007-08-23 01:44:10

Fix (I can't attach files right now)


```
# HG changeset patch
# User William Stein <wstein`@`gmail.com>
# Date 1187832852 25200
# Node ID 34d1ed88836b44c399cbf2aecd4cbb9ce67ece60
# Parent  7df7b573320b12540b9d8ba75e73354e3b993b48
Fix trac #434 -- but in mwrank interface.

diff -r 7df7b573320b -r 34d1ed88836b sage/libs/mwrank/interface.py
--- a/sage/libs/mwrank/interface.py     Wed Aug 22 17:50:17 2007 -0700
+++ b/sage/libs/mwrank/interface.py     Wed Aug 22 18:34:12 2007 -0700
`@``@` -25,9 +25,14 `@``@` def set_precision(n):

     INPUT:
         n -- long
+
+    EXAMPLES:
+        sage: mwrank_set_precision(20)
     """
-    from sage.libs.mwrank.mwrank import _set_precision # import here to save time
-    _set_precision(n)
+    # don't want to load mwrank every time SAGE starts up, so we do
+    # the import here.
+    from sage.libs.mwrank.mwrank import set_precision
+    set_precision(n)

 class mwrank_EllipticCurve(SageObject):
     r"""
```



---

Comment by was created at 2007-08-23 01:44:10

Resolution: fixed
