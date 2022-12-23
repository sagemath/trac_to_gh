# Issue 156: freeze of gfan (actually singular -- not gfan's fault)

Issue created by migration from https://trac.sagemath.org/ticket/156

Original creator: was

Original creation time: 2006-10-27 18:47:06

Assignee: was


```
x,y = QQ['x,y'].gens() 
i = ideal(x^2 - y^2 + 1)
g = i.groebner_fan()
g.reduced_groebner_bases()

[[mysterious freeze]
```



---

Comment by was created at 2007-01-19 11:00:48

Resolution: fixed


---

Comment by was created at 2007-01-19 11:00:48

Fixed -- there was a spurious comma in the input to gfan, which caused some problems in some cases:


```

# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1169204310 28800
# Node ID 061691096b76580a55a655e654aa046f2071ebc4
# Parent  08b37570702281f7b6208e4df5871cc07c19250b
Fix trac bug #156 -- problem running gfan from SAGE.

diff -r 08b375707022 -r 061691096b76 sage/rings/groebner_fan.py
--- a/sage/rings/groebner_fan.py        Fri Jan 19 02:42:18 2007 -0800
+++ b/sage/rings/groebner_fan.py        Fri Jan 19 02:58:30 2007 -0800
@@ -34,6 +34,13 @@ AUTHORS:
    -- Tristram Bogart (bogart@math): the design of the \sage interface
       to gfan is joint work with Tristram Bogart, who also supplied
       numerous examples.
+
+EXAMPLES:
+    sage: x,y = QQ['x,y'].gens() 
+    sage: i = ideal(x^2 - y^2 + 1)
+    sage: g = i.groebner_fan()
+    sage: g.reduced_groebner_bases()
+    [[1 - y^2 + x^2], [-1 + y^2 - x^2]]
 """
 
 __doc_exclude = ['to_intvec', 'multiple_replace', 'forall', \
@@ -195,7 +202,7 @@ class GroebnerFan(SageObject):
             to_gfan, _ = self._gfan_maps()
             J = to_gfan(self.__ideal)
             s = str(J.gens())
-            s = s.replace('(','{').replace(')','}')
+            s = s.replace('(','{').replace(')','}').replace(',}','}')
             self.__gfan_ideal = s
             return s
 
@@ -292,7 +299,10 @@ class GroebnerFan(SageObject):
             I = self._gfan_ideal()
         # todo -- put something in here (?) when self.__symmetry isn't None...
         cmd += self._gfan_mod()
-        return gfan(I, cmd, verbose=self.__verbose, format=format)
+        s = gfan(I, cmd, verbose=self.__verbose, format=format)
+        if s.strip() == '{':
+            raise RuntimeError, "Error running gfan command %s on %s"%(cmd, self)
+        return s
         
     def __iter__(self):
         for x in self.reduced_groebner_bases():
```

