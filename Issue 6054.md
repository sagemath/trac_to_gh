# Issue 6054: [with patch, needs review] fix display2d with ecl on OSX

Issue created by migration from https://trac.sagemath.org/ticket/6054

Original creator: mhansen

Original creation time: 2009-05-17 06:05:05

Assignee: mabshoff


```
 * ecl causes about two bugs and a half on OSX and probably some other
systems. __repr__ seems to cause sync issues, there is some problem
with numerical noise and the list of Maxima commands seems to have
different orderings on different platforms. All this can be fixed with
too many problems. The doctests affected:

32 bit OSX 10.5/Intel:

       sage -t -long "devel/sage/doc/en/constructions/calculus.rst"
       sage -t -long "devel/sage/doc/en/constructions/
polynomials.rst"
       sage -t -long "devel/sage/doc/en/tutorial/introduction.rst"
       sage -t -long "devel/sage/doc/en/tutorial/tour_algebra.rst"
       sage -t -long "devel/sage/doc/fr/tutorial/introduction.rst"
       sage -t -long "devel/sage/doc/fr/tutorial/tour_algebra.rst"
       sage -t -long "devel/sage/sage/calculus/calculus.py"
       sage -t -long "devel/sage/sage/calculus/equations.py"
       sage -t -long "devel/sage/sage/calculus/functional.py"
       sage -t -long "devel/sage/sage/calculus/test_sympy.py"
       sage -t -long "devel/sage/sage/calculus/tests.py"
       sage -t -long "devel/sage/sage/calculus/wester.py"
       sage -t -long "devel/sage/sage/interfaces/maxima.py"
       sage -t -long "devel/sage/sage/schemes/elliptic_curves/
ell_generic.py"
       sage -t -long "devel/sage/sage/symbolic/expression.pyx"

noise/blankline of "print $FOO" type

64 bit OSX 10.5/Intel

       sage -t -long "devel/sage/doc/en/constructions/calculus.rst"
       sage -t -long "devel/sage/doc/en/constructions/
polynomials.rst"
       sage -t -long "devel/sage/doc/en/tutorial/introduction.rst"
       sage -t -long "devel/sage/doc/en/tutorial/tour_algebra.rst"
       sage -t -long "devel/sage/doc/fr/tutorial/introduction.rst"
       sage -t -long "devel/sage/doc/fr/tutorial/tour_algebra.rst"
       sage -t -long "devel/sage/sage/calculus/calculus.py"
       sage -t -long "devel/sage/sage/calculus/equations.py"
       sage -t -long "devel/sage/sage/calculus/functional.py"
       sage -t -long "devel/sage/sage/calculus/test_sympy.py"
       sage -t -long "devel/sage/sage/calculus/tests.py"
       sage -t -long "devel/sage/sage/calculus/wester.py"
       sage -t -long "devel/sage/sage/interfaces/maxima.py"
       sage -t -long "devel/sage/sage/schemes/elliptic_curves/
ell_generic.py"
       sage -t -long "devel/sage/sage/symbolic/expression.pyx"
```



---

Attachment

Thanks. Great patch. But the semicolon removal in the patch

```
--- a/sage/interfaces/maxima.py Fri May 15 18:39:25 2009 -0700
+++ b/sage/interfaces/maxima.py Sat May 16 23:30:51 2009 -0700
@@ -755,7 +755,7 @@
         if self._expect is None: return
         r = randrange(2147483647)
         s = marker + str(r+1)
-        cmd = ''';sconcat("%s",(%s+1));\n'''%(marker,r)
+        cmd = '''sconcat("%s",(%s+1));\n'''%(marker,r)
         self._sendstr(cmd)
         try:
             self._expect_expr(timeout=0.5)
```

causes sync issues on sage.math, so I am taking it out.

Cheers,

Michael


---

Attachment

The patch I just posted replaces Mike's patch and also fixes the failure in 

```
devel/sage/doc/en/constructions/calculus.rst
```

that Mike did point out he forgot to change when he cut the patch. I committed in Mike's name obviously ;)

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-18 13:17:08

Resolution: fixed


---

Comment by mabshoff created at 2009-05-18 13:17:08

Merged in Sage 4.0.rc0.

Cheers,

Michael
