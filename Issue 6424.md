# Issue 6424: One can no longer convert I=sqrt(-1) to sympy

Issue created by migration from https://trac.sagemath.org/ticket/6424

Original creator: drkirkby

Original creation time: 2009-06-26 15:02:01

Assignee: tbd

CC:  david.kirkby@onetel.net

As a comment related to trac item 6423, 

_By the way, evidently one can no longer convert I=sqrt(-1) to sympy:_

```
sage: (x+sqrt(2))._sympy_()
x + 2**(1/2)
sage: (x+I)._sympy_()
SympifyError: SympifyError: I is NOT a valid SymPy expression
```


He wanted this, and the other issue reported as TRAC tickets, but was busy writing a talk. 

I don't feel able to comment much more on this, and personally don't intend trying to fix it (outside my knowledge), so I've just reported it.

Can someone else please add appropriate priority, milestones, keywords etc, as this is completely outside my comfort zone.

David Kirkby



---

Comment by AlexGhitza created at 2009-07-11 11:28:23

Changing component from algebra to symbolics.


---

Comment by mvngu created at 2009-07-14 03:08:39

From this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c484e5ccbc884998) thread by Ondrej Certik:

Currently this fails:

sage: sympy.test("sympy/test_external/")
============================= test process starts ==============================
executable:   /home/ondrej/sage-4.1-sage.math.washington.edu-x86_64-Linux/local/bin/sage.bin
 (2.6.2-final-0)

sympy/test_external/test_codegen_c_cc.py[5] .....                           [OK]
sympy/test_external/test_numpy.py[19] ...................                   [OK]
sympy/test_external/test_sage.py[13] .E...........                        [FAIL]
[...]
 File "/home/ondrej/sage-4.1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sympy/core/sympify.py",
line 194, in _sympify
   raise SympifyError("%r is NOT a valid SymPy expression" % (a,))
SympifyError: SympifyError: I is NOT a valid SymPy expression

=========== tests finished: 36 passed, 1 exceptions in 3.26 seconds ============
DO *NOT* COMMIT!
False


This patch fixes it:

diff -r ca1f31d6f6bf sage/symbolic/expression_conversions.py
--- a/sage/symbolic/expression_conversions.py   Thu Jul 09 15:14:36 2009 -0700
+++ b/sage/symbolic/expression_conversions.py   Mon Jul 13 16:57:22 2009 -0700
`@``@` -572,7 +572,7 `@``@`
        """
        import sympy
        operator = arithmetic_operators[operator]
-        ops = [self(a) for a in ex.operands()]
+        ops = [sympy.sympify(self(a)) for a in ex.operands()]
        if operator == "+":
            return sympy.Add(*ops)
        elif operator == "*":

Now:

sage: sympy.test("sympy/test_external/")
============================= test process starts ==============================
executable:   /home/ondrej/sage-4.1-sage.math.washington.edu-x86_64-Linux/local/bin/sage.bin
 (2.6.2-final-0)

sympy/test_external/test_codegen_c_cc.py[5] .....                           [OK]
sympy/test_external/test_numpy.py[19] ...................                   [OK]
sympy/test_external/test_sage.py[13] .............                          [OK]

================== tests finished: 37 passed in 2.29 seconds ===================
True


I vaguely remember William run into this bug recently. It was caused
by switching to the new symbolic, the problem was that passing things
directly to Mul classes in sympy goes in the fast track and only
sympifies easy things like python ints. For Sage integers, a full
sympify must be called, which is what my patch does. The core of the
problem is in fact in sympy cache mechanism, which only does fast
track sympify for performance reasons, so the proper fix is to fix our
cache, which is exactly what we plan to do --- get rid of it,
hopefully by the end of the summer.

We are about to release a new sympy now, so the above patch makes all
sympy 0.6.6 tests pass.


---

Comment by dsm created at 2011-12-14 01:00:25

fix sympy conversion of I


---

Attachment

For various reasons I need this to work.  Patch attached, which simply does what Ondrej recommended and adds a doctest.


---

Comment by dsm created at 2011-12-14 01:01:57

Changing status from new to needs_review.


---

Comment by mhansen created at 2011-12-17 20:49:50

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2011-12-17 20:49:50

Looks good to me.


---

Comment by jdemeyer created at 2011-12-22 13:06:27

Resolution: fixed
