# Issue 43: gap boolean values don't coerce back

archive/issues_000043.json:
```json
{
    "body": "Assignee: somebody\n\n(KiranKedlaya) GAP boolean values do not automatically coerce back to SAGE, e.g.,\n\n```\nsage: if gap(\"2+2=4\"):\n   .....:     pass\n```\nreturns an error, whereas\n\n```\nsage: if sage_eval(gap(\"2+2=4\")):\n   .....:     pass\n```\ndoes not. A more serious instance of this is:\n\n```\nsage: G = SymmetricGroup(8)\nsage: A = AlternatingGroup(8)\nsage: if (G._gap_().IsSubgroup(A)):\n   .....:     print 1\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/43\n\n",
    "created_at": "2006-09-12T23:32:43Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "title": "gap boolean values don't coerce back",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/43",
    "user": "https://github.com/williamstein"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/43





---

archive/issue_comments_000263.json:
```json
{
    "body": "Replying to [ticket:43 was]:\n\n\nwdj: Is this a bug or a syntax mistake? The following work and seem to\ndo what is desired:\n\nsage: if gap.eval(\"2+2=4\"): print 1\n\n1\n\nsage: G = SymmetricGroup(8)\n\nsage: A = AlternatingGroup(8)\n\nsage: gap(G).IsSubgroup(gap(A))\n true",
    "created_at": "2006-09-28T23:54:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/43",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/43#issuecomment-263",
    "user": "https://github.com/wdjoyner"
}
```

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

archive/issue_comments_000264.json:
```json
{
    "body": "```\n# HG changeset patch\n# User William Stein <wstein@gmail.com>\n# Date 1168639902 28800\n# Node ID 2a6823917a29813a484e00eea7b15f7c697269ab\n# Parent  4fe8209d82ae7980fd8ebc80db390f9265512cf6\nFix trac bug # 43\n\ndiff -r 4fe8209d82ae -r 2a6823917a29 sage/interfaces/expect.py\n--- a/sage/interfaces/expect.py Fri Jan 12 13:30:02 2007 -0800\n+++ b/sage/interfaces/expect.py Fri Jan 12 14:11:42 2007 -0800\n@@ -871,6 +871,9 @@ class ExpectElement(RingElement):\n         cmd = '%s %s %s'%(self._name, P._equality_symbol(), t)\n         return P.eval(cmd) == t\n \n+    def __bool__(self):\n+        return self.bool()\n+\n \n     def __long__(self):\n         return long(str(self))\ndiff -r 4fe8209d82ae -r 2a6823917a29 sage/interfaces/gap.py\n--- a/sage/interfaces/gap.py    Fri Jan 12 13:30:02 2007 -0800\n+++ b/sage/interfaces/gap.py    Fri Jan 12 14:11:42 2007 -0800\n@@ -566,9 +566,28 @@ class GapElement(ExpectElement):\n         return s\n \n     def __len__(self):\n-        if (self == \"true\"):\n+        \"\"\"\n+        EXAMPLES:\n+            sage: v = gap('[1,2,3]'); v\n+            [ 1, 2, 3 ]\n+            sage: len(v)\n+            3\n+\n+        len is also called implicitly by if:\n+            sage: if gap('1+1 = 2'):\n+            ...    print \"1 plus 1 does equal 2\"\n+            1 plus 1 does equal 2\n+            \n+            sage: if gap('1+1 = 3'): \n+            ...    print \"it is true\"\n+            ... else:\n+            ...    print \"it is false\"\n+            it is false\n+        \"\"\"\n+        P = self.parent()\n+        if P.eval('%s = true'%self.name()) == 'true':\n             return 1\n-        elif (self == \"false\"):\n+        elif P.eval('%s = false'%self.name()) == 'true':        \n             return 0\n         else:\n             return int(self.Length())\n```",
    "created_at": "2007-01-12T22:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/43",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/43#issuecomment-264",
    "user": "https://github.com/williamstein"
}
```

```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1168639902 28800
# Node ID 2a6823917a29813a484e00eea7b15f7c697269ab
# Parent  4fe8209d82ae7980fd8ebc80db390f9265512cf6
Fix trac bug # 43

diff -r 4fe8209d82ae -r 2a6823917a29 sage/interfaces/expect.py
--- a/sage/interfaces/expect.py Fri Jan 12 13:30:02 2007 -0800
+++ b/sage/interfaces/expect.py Fri Jan 12 14:11:42 2007 -0800
@@ -871,6 +871,9 @@ class ExpectElement(RingElement):
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
@@ -566,9 +566,28 @@ class GapElement(ExpectElement):
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

archive/issue_events_000091.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-01-12T22:12:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/43",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/43#event-91"
}
```



---

archive/issue_comments_000265.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-12T22:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/43",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/43#issuecomment-265",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
