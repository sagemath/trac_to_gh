# Issue 7403: adds FiniteEnumeratedSet

Issue created by migration from https://trac.sagemath.org/ticket/7403

Original creator: nthiery

Original creation time: 2009-11-06 15:56:12

Assignee: mhansen

CC:  sage-combinat

Keywords: finite enumerated sets

This patch adds sage.sets.finite_enumerated_set.FiniteEnumeratedSet

depends on #5891


---

Comment by nthiery created at 2009-11-06 15:58:14

Changing status from new to needs_review.


---

Comment by nthiery created at 2009-11-06 15:58:21

Changing status from needs_review to positive_review.


---

Attachment


---

Attachment

Apply only this one (ignore the next one)


---

Comment by hivert created at 2009-11-09 07:53:36

Since it's not yet integrated, I take the chance to solve this stupid bug:

```
sage: FiniteEnumeratedSet([1])
{1,}
```

I'm re-uploading a patch with the following folded in

```
diff --git a/sage/sets/finite_enumerated_set.py b/sage/sets/finite_enumerated_set.py
--- a/sage/sets/finite_enumerated_set.py
+++ b/sage/sets/finite_enumerated_set.py
@@ -123,8 +123,13 @@ class FiniteEnumeratedSet(UniqueRepresen
             sage: S = FiniteEnumeratedSet([1,2,3])
             sage: repr(S)
             '{1, 2, 3}'
+            sage: S = FiniteEnumeratedSet([1])
+            sage: repr(S)
+            '{1}'
         """
-        return "{"+str(self._elements)[1:-1] + '}'
+        if len(self._elements) == 1: # avoid printing '{1,}'
+            return "{" + str(self._elements[0]) + '}'
+        return "{" + str(self._elements)[1:-1] + '}'
 
     def __contains__(self, x):
         """
```


Florent


---

Comment by hivert created at 2009-11-09 07:53:36

Changing status from positive_review to needs_work.


---

Attachment

Please Nicolas (or anyone else re-view the small change. 

Only trac_7403-finite-enumeratedsets-fh.3.patch should be applied on top of #5891

Cheers,

Florent


---

Comment by hivert created at 2009-11-09 07:55:54

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2009-11-09 10:47:37

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2009-11-13 15:01:25

Changing assignee from mhansen to hivert.


---

Comment by mhansen created at 2009-11-19 16:57:08

Resolution: fixed
