# Issue 328: maximafunction bug

Issue created by migration from https://trac.sagemath.org/ticket/328

Original creator: was

Original creation time: 2007-03-22 02:39:30

Assignee: was


```

	Gregory Vanuxem <g.vanuxem@wanadoo.fr> 	
to SAGE-Devel
	
show details
	 Mar 10 

Hello,

Here is a simple session that exhibits a bug, I don't know "where" it
comes from:


========================================================================
$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.3, Release Date: 2007-03-06                         |
| Type notebook() for the GUI, and license() for information.        |

sage: f = maxima.function('x','gamma(x)')

sage: # f # do not print f

sage: g = f(1/7)

sage: g
 gamma(1/7)

sage: f = gp(sin(x))

sage: f
 x - 1/6*x^3 + 1/120*x^5 - 1/5040*x^7 + 1/362880*x^9 - 1/39916800*x^11 +
1/6227020800*x^13 - 1/1307674368000*x^15 + O(x^17)

sage: maxima(sin(x))
 gamma(x)
==========================================================================


At the end maxima(sin(x)) returns the MaximaElement gamma(x) :-(

I spent some time trying to find a simple and reproducible way that
triggers this bug, modifying one line, for example printing 'f', can
lead to an, apparently, correct computation so try this in a fresh
session.

Many thanks for your work,

Greg
```



---

Comment by was created at 2007-03-22 02:39:42

I've confirmed that this bug occurs.


---

Comment by was created at 2007-03-22 02:58:11

Resolution: fixed


---

Comment by was created at 2007-03-22 02:58:11

Fixed for sage-2.4:


```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1174532177 25200
# Node ID 722fce5223fdc8bde9f0365993458a6893bc60b5
# Parent  d49a5c6e928f2ae350f8de0b4c4d63b2da6c938e
Fix trac # 328 -- weirdness with maxima function definition.

diff -r d49a5c6e928f -r 722fce5223fd sage/interfaces/maxima.py
--- a/sage/interfaces/maxima.py Wed Mar 21 18:25:59 2007 -0700
+++ b/sage/interfaces/maxima.py Wed Mar 21 19:56:17 2007 -0700
@@ -326,7 +326,17 @@ is much less robust, and is not recommen
 is much less robust, and is not recommended.}

     sage: t = '"%s"'%10^10000   # ten thousand character string.
-    sage: a = maxima(t)
+    sage: a = maxima(t)
+
+TESTS:
+This working tests that a subtle bug has been fixed:
+    sage: f = maxima.function('x','gamma(x)')
+    sage: g = f(1/7)
+    sage: g
+    gamma(1/7)
+    sage: del f
+    sage: maxima(sin(x))
+    sin(x)
 """

 #*****************************************************************************
@@ -650,6 +660,8 @@ class Maxima(Expect):
             0.90929742682568171
             sage: loads(t.dumps())
             gamma(x)*sin(x)
+
+
         """
         name = self._next_var_name()
         defn = str(defn)
@@ -678,14 +690,17 @@ class Maxima(Expect):
         s = self._eval_line('%s'%var)
         return s

-    #def clear(self, var):
-    #    """
-    #    Clear the variable named var.
-    #    """
-    #    if self._expect is None:
-    #        return
-    #    self._expect.sendline('kill(%s);'%var)
-    #    self._expect.expect(self._prompt)
+    def clear(self, var):
+        """
+        Clear the variable named var.
+        """
+        if self._expect is None:
+            return
+        try:
+            self._expect.sendline('kill(%s);'%var)
+            self._expect.expect(self._prompt)
+        except:  # program around weirdness in pexpect
+            pass

     def console(self):
         maxima_console()
```

