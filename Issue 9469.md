# Issue 9469: Category membership, without arguments

Issue created by migration from https://trac.sagemath.org/ticket/9469

Original creator: nthiery

Original creation time: 2010-07-10 02:52:00

Assignee: nthiery

CC:  sage-combinat

Currently one can do:

```
    sage: F = FreeModule(QQ,3)
    sage: F in VectorSpaces(QQ)
    True
```


This patch implements:

```
    sage: F in VectorSpaces
    True
```



---

Comment by nthiery created at 2010-07-10 03:15:55

Changing status from new to needs_review.


---

Comment by nthiery created at 2010-07-10 03:23:33

Changing status from needs_review to needs_work.


---

Comment by nthiery created at 2012-02-09 17:00:10

Changing keywords from "" to "Cernay2012".


---

Comment by nthiery created at 2012-02-09 17:00:10

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2012-02-09 17:00:39

Patch reviewed by Florent on the Sage-Combinat queue. Positive review on his behalf.


---

Comment by nthiery created at 2012-02-09 17:00:39

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2012-02-09 17:18:56

Florent wants to add a pointer to the feature elsewhere


---

Comment by nthiery created at 2012-02-09 17:18:56

Changing status from positive_review to needs_work.


---

Comment by nthiery created at 2012-02-10 01:49:44

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2012-02-10 01:51:24

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2012-02-10 01:51:24

The new patch is Ok with me.


---

Comment by nthiery created at 2012-02-18 14:37:54

I just stumbled upon the following hunk later in the queue, and thought we might as well
fold it into this patch:

```
diff --git a/sage/categories/category.py b/sage/categories/category.py
--- a/sage/categories/category.py
+++ b/sage/categories/category.py
@@ -627,8 +627,19 @@ class Category(UniqueRepresentation, Sag
 
             sage: F in Algebras
             False
+
+        TESTS:
+
+        Non category object shall be handled properly::
+
+            sage: [1,2] in Algebras
+            False
         """
-        return any(isinstance(cat, cls) for cat in x.categories())
+        try:
+            c = x.categories()
+        except AttributeError:
+            return False
+        return any(isinstance(cat, cls) for cat in c)
 
     def is_abelian(self):
         """
```


I am running the tests now. Florent: shall I reinstate the positive review if the test pass?


---

Comment by nthiery created at 2012-02-18 14:37:54

Changing status from positive_review to needs_work.


---

Comment by nthiery created at 2012-02-18 14:38:28

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2012-02-18 14:41:14

Note: I fixed the missing 's' in 'Non category objects'.


---

Attachment


---

Comment by nthiery created at 2012-02-21 07:43:13

I backported here your fix to the Category object link


---

Comment by hivert created at 2012-02-21 08:27:30

The new version is Ok with me !


---

Comment by hivert created at 2012-02-21 08:27:30

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-02-27 11:19:53

Resolution: fixed
