# Issue 43: gap boolean values don't coerce back

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-12 23:32:43

Assignee: somebody

(KiranKedlaya) GAP boolean values do not automatically coerce back to SAGE, e.g.,

```
sage: if gap("2+2=4"):
   .....:     pass
```

returns an error, whereas

```
sage: if sage_eval(gap("2+2=4")):
   .....:     pass
```

does not. A more serious instance of this is:

```
sage: G = SymmetricGroup(8)
sage: A = AlternatingGroup(8)
sage: if (G._gap_().IsSubgroup(A)):
   .....:     print 1
```




---

Comment by wdj created at 2006-09-28 23:54:46

Replying to [ticket:43 was]:


wdj: Is this a bug or a syntax mistake? The following work and seem to
do what is desired:

sage: if gap.eval("2+2=4"): print 1

1

sage: G = SymmetricGroup(8)

sage: A = AlternatingGroup(8)

sage: gap(G).IsSubgroup(gap(A))
 true


---

Comment by was created at 2007-01-12 22:12:37


```
# HG changeset patch
# User William Stein <wstein`@`gmail.com>
# Date 1168639902 28800
# Node ID 2a6823917a29813a484e00eea7b15f7c697269ab
# Parent  4fe8209d82ae7980fd8ebc80db390f9265512cf6
Fix trac bug # 43

diff -r 4fe8209d82ae -r 2a6823917a29 sage/interfaces/expect.py
--- a/sage/interfaces/expect.py Fri Jan 12 13:30:02 2007 -0800
+++ b/sage/interfaces/expect.py Fri Jan 12 14:11:42 2007 -0800
`@``@` -871,6 +871,9 `@``@` class ExpectElement(RingElement):
         cmd = '%s %s %s'%(self._name, P._equality_symbol(), t)
         return P.eval(cmd) == t
 
+    def __bool__(self):
+        return self.bool()
+
 
     def __long__(self):
         return long(str(self))
diff -r 4fe8209d82ae -r 2a6823917a29 sage/interfaces/gap.py
--- a/sage/interfaces/gap.py    Fri Jan 12 13:30:02 2007 -0800
+++ b/sage/interfaces/gap.py    Fri Jan 12 14:11:42 2007 -0800
`@``@` -566,9 +566,28 `@``@` class GapElement(ExpectElement):
         return s
 
     def __len__(self):
-        if (self == "true"):
+        """
+        EXAMPLES:
+            sage: v = gap('[1,2,3]'); v
+            [ 1, 2, 3 ]
+            sage: len(v)
+            3
+
+        len is also called implicitly by if:
+            sage: if gap('1+1 = 2'):
+            ...    print "1 plus 1 does equal 2"
+            1 plus 1 does equal 2
+            
+            sage: if gap('1+1 = 3'): 
+            ...    print "it is true"
+            ... else:
+            ...    print "it is false"
+            it is false
+        """
+        P = self.parent()
+        if P.eval('%s = true'%self.name()) == 'true':
             return 1
-        elif (self == "false"):
+        elif P.eval('%s = false'%self.name()) == 'true':        
             return 0
         else:
             return int(self.Length())
```



---

Comment by was created at 2007-01-12 22:12:37

Resolution: fixed
