# Issue 1570: typo in sage/rings/number_field/number_field.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-20 01:30:55

Assignee: tba

Reported by Francis Clarke

```
--- a/sage/rings/number_field/number_field.py   Sun Dec 16 06:37:16
2007 -0800
+++ b/sage/rings/number_field/number_field.py   Wed Dec 19 18:54:54
2007 +0000
`@``@` -751,7 +751,7 `@``@` class NumberField_generic(number_field_b

         You can also view a number field as having a different
         generator by just chosing the input to generate the
-        whole filed; for that it is better to use
+        whole field; for that it is better to use
         \code{self.change_generator}, which gives isomorphisms
         in both directions.
         """ 
```



---

Attachment


---

Comment by mabshoff created at 2008-01-13 17:49:03

Resolution: fixed
