# Issue 98: p-adic print_prec does work as advertised

archive/issues_000098.json:
```json
{
    "body": "Assignee: somebody\n\n```\nsage: K = Qp(13); K.prec(6); K.print_prec(3)\nsage: K(1/2)\n 7 + 6*13 + 6*13^2 + O(13^6)\n```\n\nOutput should presumably be\n\n```\n 7 + 6*13 + 6*13^2 + O(13^3)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/98\n\n",
    "created_at": "2006-09-30T02:18:55Z",
    "labels": [
        "component: basic arithmetic",
        "trivial",
        "bug"
    ],
    "title": "p-adic print_prec does work as advertised",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/98",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: somebody

```
sage: K = Qp(13); K.prec(6); K.print_prec(3)
sage: K(1/2)
 7 + 6*13 + 6*13^2 + O(13^6)
```

Output should presumably be

```
 7 + 6*13 + 6*13^2 + O(13^3)
```


Issue created by migration from https://trac.sagemath.org/ticket/98





---

archive/issue_comments_000462.json:
```json
{
    "body": "This is terrible!  But it's pointless to fix when the p-adics are on the way out to be replaced by new implementation...  keep the example in mind though.",
    "created_at": "2007-01-13T02:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/98",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/98#issuecomment-462",
    "user": "https://github.com/williamstein"
}
```

This is terrible!  But it's pointless to fix when the p-adics are on the way out to be replaced by new implementation...  keep the example in mind though.



---

archive/issue_comments_000463.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-22T03:27:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/98",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/98#issuecomment-463",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_000464.json:
```json
{
    "body": "Fixed.\n\n```\n# HG changeset patch\n# User William Stein <wstein@gmail.com>\n# Date 1169435812 28800\n# Node ID 8da5c79260af2dab705c01b32f330f923a9e113d\n# Parent  3ca3f4250d3073970959522a8e6a4b651d441594\nFix trac #98 -- padic print_prec problem.\n\ndiff -r 3ca3f4250d30 -r 8da5c79260af sage/rings/padic.py\n--- a/sage/rings/padic.py       Sun Jan 21 18:58:31 2007 -0800\n+++ b/sage/rings/padic.py       Sun Jan 21 19:16:52 2007 -0800\n@@ -56,9 +56,9 @@ class pAdic(field_element.FieldElement):\n       p-adic field:\n         sage: K = pAdicField(5, 4)\n         sage: K(3)         # has an exact representation\n-          3 + O(5^Infinity)\n+          3 + ... + O(5^Infinity)\n         sage: K(3/5)\n-          3*5^-1 + O(5^Infinity)\n+          3*5^-1 + ... + O(5^Infinity)\n         sage: K(1/3)       # needs to be approximated; use default precision\n           2 + 3*5 + 5^2 + 3*5^3 + O(5^4)\n         sage: K(5/3)\n@@ -69,11 +69,11 @@ class pAdic(field_element.FieldElement):\n       Coercion from rational field with explicitly selected precision:\n         sage: K = pAdicField(5, 4)\n         sage: K(3, infinity)\n-          3 + O(5^Infinity)\n+          3 + ... + O(5^Infinity)\n         sage: K(3, 8)\n-          3 + O(5^8)\n+          3 + ... + O(5^8)\n         sage: K(3/5, 8)\n-          3*5^-1 + O(5^8)\n+          3*5^-1 + ... + O(5^8)\n         sage: K(1/3, 8)\n           2 + 3*5 + 5^2 + 3*5^3 + 5^4 + 3*5^5 + 5^6 + 3*5^7 + O(5^8)\n         sage: K(5/3, 8)\n@@ -244,7 +244,7 @@ class pAdic(field_element.FieldElement):\n             sage: a.denominator()\n             1\n             sage: b = K(3211/11^2); b\n-            10*11^-2 + 5*11^-1 + 4 + 2*11 + O(11^Infinity)\n+            10*11^-2 + 5*11^-1 + 4 + 2*11 + ... + O(11^Infinity)\n             sage: b.denominator()\n             121\n         \"\"\"\n@@ -264,7 +264,7 @@ class pAdic(field_element.FieldElement):\n             sage: a.ordp()\n             0\n             sage: b = K(3211/11^2); b\n-            10*11^-2 + 5*11^-1 + 4 + 2*11 + O(11^Infinity)\n+            10*11^-2 + 5*11^-1 + 4 + 2*11 + ... + O(11^Infinity)\n             sage: b.ordp()\n             -2\n \n@@ -365,7 +365,7 @@ class pAdic(field_element.FieldElement):\n         u     = self.__unit\n         exp   = self.__ordp\n         p     = self.__p\n-        prec  = min(self.__prec, self.parent().print_prec()-self.__ordp)\n+        prec  = min(self.__prec, self.parent().print_prec() - self.__ordp)\n         if prec == infinity:\n             prec = self.parent().prec()\n         u   %= self.__p ** prec\n@@ -390,8 +390,8 @@ class pAdic(field_element.FieldElement):\n                         s += \"%s + \"%var\n             exp += 1\n             u = (u-coeff)/p\n-        #if prec < self.big_oh()-1:\n-        #    s += '... + '\n+        if exp < self.big_oh()-1:\n+            s += '... + '\n         s += \"O(%s\"%(p)\n         if self.big_oh() == 1:\n             s += \")\"\n@@ -410,7 +410,7 @@ class pAdic(field_element.FieldElement):\n         EXAMPLES:\n             sage: K = Qp(11, 10); K.print_prec(5)\n             sage: a = K(-1); a\n-            10 + 10*11 + 10*11^2 + 10*11^3 + 10*11^4 + O(11^10)\n+            10 + 10*11 + 10*11^2 + 10*11^3 + 10*11^4 + ... + O(11^10)\n             sage: b = K(1); b\n             1\n             sage: a+b\n@@ -452,11 +452,11 @@ class pAdic(field_element.FieldElement):\n             sage: (-1)*one(K)\n             18 + 18*19 + 18*19^2 + 18*19^3 + 18*19^4 + O(19^5)\n             sage: a = K(2/19); a\n-            2*19^-1 + O(19^Infinity)\n+            2*19^-1 + ... + O(19^Infinity)\n             sage: b = K(3/19); b\n-            3*19^-1 + O(19^Infinity)\n+            3*19^-1 + ... + O(19^Infinity)\n             sage: a*b\n-            6*19^-2 + O(19^Infinity)\n+            6*19^-2 + ... + O(19^Infinity)\n         \"\"\"\n         prec = min(self.__prec, right.__prec)\n         ordp = self.__ordp + right.__ordp\n@@ -470,9 +470,9 @@ class pAdic(field_element.FieldElement):\n         EXAMPLES:\n             sage: K = Qp(19, 5)\n             sage: a = K(2/19); a\n-            2*19^-1 + O(19^Infinity)\n+            2*19^-1 + ... + O(19^Infinity)\n             sage: b = K(3/19); b\n-            3*19^-1 + O(19^Infinity)\n+            3*19^-1 + ... + O(19^Infinity)\n             sage: a/b\n             7 + 6*19 + 6*19^2 + 6*19^3 + 6*19^4 + O(19^5)\n             sage: (5 + O(5)) / 1\n@@ -500,11 +500,11 @@ class pAdic(field_element.FieldElement):\n             sage: a = K(-1); a\n             18 + 18*19 + 18*19^2 + 18*19^3 + 18*19^4 + O(19^5)\n             sage: a^2\n-            1 + O(19^5)\n+            1 + ... + O(19^5)\n             sage: a^3\n             18 + 18*19 + 18*19^2 + 18*19^3 + 18*19^4 + O(19^5)\n             sage: K(5)^30\n-            11 + 14*19 + 19^2 + 7*19^3 + O(19^Infinity)\n+            11 + 14*19 + 19^2 + 7*19^3 + ... + O(19^Infinity)\n         \"\"\"\n         right = integer.Integer(right)\n         if self == 0:\n@@ -550,12 +550,12 @@ class pAdic(field_element.FieldElement):\n         EXAMPLES:\n             sage: K = Qp(19, 5)\n             sage: a = K(20); a\n-            1 + 19 + O(19^Infinity)\n+            1 + 19 + ... + O(19^Infinity)\n             sage: b = ~a    # calls __invert__\n             sage: b\n             1 + 18*19 + 18*19^3 + O(19^5)\n             sage: a*b\n-            1 + O(19^5)\n+            1 + ... + O(19^5)\n \n         One can pass an optional argument to __invert__ to\n         affect the precision, which is especially useful when\n@@ -633,9 +633,9 @@ class pAdic(field_element.FieldElement):\n         EXAMPLES:\n             sage: K = Qp(19, 5)\n             sage: a = K(2); a\n-            2 + O(19^Infinity)\n+            2 + ... + O(19^Infinity)\n             sage: b = K(3); b\n-            3 + O(19^Infinity)\n+            3 + ... + O(19^Infinity)\n             sage: a < b\n             True\n         \"\"\"\n@@ -675,12 +675,12 @@ class pAdic(field_element.FieldElement):\n         EXAMPLES:\n             sage: x = 9*(2+3+O(3**7))\n             sage: x.unit_part()\n-            2 + 3 + O(3^7)\n+            2 + 3 + ... + O(3^7)\n             sage: K = Qp(19, 5)\n             sage: a = K(2)/19; a\n-            2*19^-1 + O(19^4)\n+            2*19^-1 + ... + O(19^4)\n             sage: a.unit_part()\n-            2 + O(19^5)\n+            2 + ... + O(19^5)\n         \"\"\"\n         return pAdic(self.__parent, self.__unit, self.__prec, 0)\n \n@@ -689,7 +689,7 @@ class pAdic(field_element.FieldElement):\n             EXAMPLES:\n             sage: K = Qp(11)\n             sage: a = K(2); a\n-            2 + O(11^Infinity)\n+            2 + ... + O(11^Infinity)\n             sage: a.is_zero()\n             False\n \n@@ -704,7 +704,7 @@ class pAdic(field_element.FieldElement):\n         EXAMPLES:\n             sage: K = Qp(11)\n             sage: a = K(2); a\n-            2 + O(11^Infinity)\n+            2 + ... + O(11^Infinity)\n             sage: a.is_unit()\n             True\n             sage: K(121).is_unit()\n@@ -731,7 +731,7 @@ class pAdic(field_element.FieldElement):\n             sage: a.rational_reconstruction()\n             -1\n             sage: a = K(2); a\n-            2 + O(11^Infinity)\n+            2 + ... + O(11^Infinity)\n             sage: a.rational_reconstruction()\n             2\n         \"\"\"\n@@ -782,7 +782,7 @@ class pAdic(field_element.FieldElement):\n         EXAMPLES:\n             sage: Q13 = Qp(13, 10)\n             sage: a = Q13(14); a\n-            1 + 13 + O(13^Infinity)\n+            1 + 13 + ... + O(13^Infinity)\n             sage: a.log()\n             13 + 6*13^2 + 2*13^3 + 5*13^4 + 10*13^6 + 13^7 + 11*13^8 + 8*13^9 + O(13^10)\n \n@@ -790,7 +790,7 @@ class pAdic(field_element.FieldElement):\n         First we create a field with {\\em default} precision 10.\n             sage: K = pAdicField(5,10)\n             sage: e = K(389); e\n-            4 + 2*5 + 3*5^3 + O(5^Infinity)\n+            4 + 2*5 + 3*5^3 + ... + O(5^Infinity)\n \n         If the input has infinite precision, the output is computed to the\n         default precision of the parent field. \ndiff -r 3ca3f4250d30 -r 8da5c79260af sage/rings/padic_field.py\n--- a/sage/rings/padic_field.py Sun Jan 21 18:58:31 2007 -0800\n+++ b/sage/rings/padic_field.py Sun Jan 21 19:16:52 2007 -0800\n@@ -59,8 +59,22 @@ class pAdicField_generic(field.Field):\n         p-adic field is truncated at $O(p^n)$.   Calling print_prec() with\n         no arguments returns n.  This command only affects printing,\n         and does not alter the actual values of elements of this field.\n+\n+        INPUT:\n+            n -- integer\n+                 infinity\n+                 None\n+\n+        EXAMPLES:\n+            sage: K = Qp(13, 6)\n+            sage: K.print_prec(infinity)\n+            sage: a = K(1/2); a\n+            7 + 6*13 + 6*13^2 + 6*13^3 + 6*13^4 + 6*13^5 + O(13^6)\n+            sage: K.print_prec(3)\n+            sage: a\n+            7 + 6*13 + 6*13^2 + ... + O(13^6)        \n         \"\"\"\n-        if n==None:\n+        if n is None:\n             return self.__print_prec\n         self.__print_prec = n\n \n```",
    "created_at": "2007-01-22T03:27:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/98",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/98#issuecomment-464",
    "user": "https://github.com/williamstein"
}
```

Fixed.

```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1169435812 28800
# Node ID 8da5c79260af2dab705c01b32f330f923a9e113d
# Parent  3ca3f4250d3073970959522a8e6a4b651d441594
Fix trac #98 -- padic print_prec problem.

diff -r 3ca3f4250d30 -r 8da5c79260af sage/rings/padic.py
--- a/sage/rings/padic.py       Sun Jan 21 18:58:31 2007 -0800
+++ b/sage/rings/padic.py       Sun Jan 21 19:16:52 2007 -0800
@@ -56,9 +56,9 @@ class pAdic(field_element.FieldElement):
       p-adic field:
         sage: K = pAdicField(5, 4)
         sage: K(3)         # has an exact representation
-          3 + O(5^Infinity)
+          3 + ... + O(5^Infinity)
         sage: K(3/5)
-          3*5^-1 + O(5^Infinity)
+          3*5^-1 + ... + O(5^Infinity)
         sage: K(1/3)       # needs to be approximated; use default precision
           2 + 3*5 + 5^2 + 3*5^3 + O(5^4)
         sage: K(5/3)
@@ -69,11 +69,11 @@ class pAdic(field_element.FieldElement):
       Coercion from rational field with explicitly selected precision:
         sage: K = pAdicField(5, 4)
         sage: K(3, infinity)
-          3 + O(5^Infinity)
+          3 + ... + O(5^Infinity)
         sage: K(3, 8)
-          3 + O(5^8)
+          3 + ... + O(5^8)
         sage: K(3/5, 8)
-          3*5^-1 + O(5^8)
+          3*5^-1 + ... + O(5^8)
         sage: K(1/3, 8)
           2 + 3*5 + 5^2 + 3*5^3 + 5^4 + 3*5^5 + 5^6 + 3*5^7 + O(5^8)
         sage: K(5/3, 8)
@@ -244,7 +244,7 @@ class pAdic(field_element.FieldElement):
             sage: a.denominator()
             1
             sage: b = K(3211/11^2); b
-            10*11^-2 + 5*11^-1 + 4 + 2*11 + O(11^Infinity)
+            10*11^-2 + 5*11^-1 + 4 + 2*11 + ... + O(11^Infinity)
             sage: b.denominator()
             121
         """
@@ -264,7 +264,7 @@ class pAdic(field_element.FieldElement):
             sage: a.ordp()
             0
             sage: b = K(3211/11^2); b
-            10*11^-2 + 5*11^-1 + 4 + 2*11 + O(11^Infinity)
+            10*11^-2 + 5*11^-1 + 4 + 2*11 + ... + O(11^Infinity)
             sage: b.ordp()
             -2
 
@@ -365,7 +365,7 @@ class pAdic(field_element.FieldElement):
         u     = self.__unit
         exp   = self.__ordp
         p     = self.__p
-        prec  = min(self.__prec, self.parent().print_prec()-self.__ordp)
+        prec  = min(self.__prec, self.parent().print_prec() - self.__ordp)
         if prec == infinity:
             prec = self.parent().prec()
         u   %= self.__p ** prec
@@ -390,8 +390,8 @@ class pAdic(field_element.FieldElement):
                         s += "%s + "%var
             exp += 1
             u = (u-coeff)/p
-        #if prec < self.big_oh()-1:
-        #    s += '... + '
+        if exp < self.big_oh()-1:
+            s += '... + '
         s += "O(%s"%(p)
         if self.big_oh() == 1:
             s += ")"
@@ -410,7 +410,7 @@ class pAdic(field_element.FieldElement):
         EXAMPLES:
             sage: K = Qp(11, 10); K.print_prec(5)
             sage: a = K(-1); a
-            10 + 10*11 + 10*11^2 + 10*11^3 + 10*11^4 + O(11^10)
+            10 + 10*11 + 10*11^2 + 10*11^3 + 10*11^4 + ... + O(11^10)
             sage: b = K(1); b
             1
             sage: a+b
@@ -452,11 +452,11 @@ class pAdic(field_element.FieldElement):
             sage: (-1)*one(K)
             18 + 18*19 + 18*19^2 + 18*19^3 + 18*19^4 + O(19^5)
             sage: a = K(2/19); a
-            2*19^-1 + O(19^Infinity)
+            2*19^-1 + ... + O(19^Infinity)
             sage: b = K(3/19); b
-            3*19^-1 + O(19^Infinity)
+            3*19^-1 + ... + O(19^Infinity)
             sage: a*b
-            6*19^-2 + O(19^Infinity)
+            6*19^-2 + ... + O(19^Infinity)
         """
         prec = min(self.__prec, right.__prec)
         ordp = self.__ordp + right.__ordp
@@ -470,9 +470,9 @@ class pAdic(field_element.FieldElement):
         EXAMPLES:
             sage: K = Qp(19, 5)
             sage: a = K(2/19); a
-            2*19^-1 + O(19^Infinity)
+            2*19^-1 + ... + O(19^Infinity)
             sage: b = K(3/19); b
-            3*19^-1 + O(19^Infinity)
+            3*19^-1 + ... + O(19^Infinity)
             sage: a/b
             7 + 6*19 + 6*19^2 + 6*19^3 + 6*19^4 + O(19^5)
             sage: (5 + O(5)) / 1
@@ -500,11 +500,11 @@ class pAdic(field_element.FieldElement):
             sage: a = K(-1); a
             18 + 18*19 + 18*19^2 + 18*19^3 + 18*19^4 + O(19^5)
             sage: a^2
-            1 + O(19^5)
+            1 + ... + O(19^5)
             sage: a^3
             18 + 18*19 + 18*19^2 + 18*19^3 + 18*19^4 + O(19^5)
             sage: K(5)^30
-            11 + 14*19 + 19^2 + 7*19^3 + O(19^Infinity)
+            11 + 14*19 + 19^2 + 7*19^3 + ... + O(19^Infinity)
         """
         right = integer.Integer(right)
         if self == 0:
@@ -550,12 +550,12 @@ class pAdic(field_element.FieldElement):
         EXAMPLES:
             sage: K = Qp(19, 5)
             sage: a = K(20); a
-            1 + 19 + O(19^Infinity)
+            1 + 19 + ... + O(19^Infinity)
             sage: b = ~a    # calls __invert__
             sage: b
             1 + 18*19 + 18*19^3 + O(19^5)
             sage: a*b
-            1 + O(19^5)
+            1 + ... + O(19^5)
 
         One can pass an optional argument to __invert__ to
         affect the precision, which is especially useful when
@@ -633,9 +633,9 @@ class pAdic(field_element.FieldElement):
         EXAMPLES:
             sage: K = Qp(19, 5)
             sage: a = K(2); a
-            2 + O(19^Infinity)
+            2 + ... + O(19^Infinity)
             sage: b = K(3); b
-            3 + O(19^Infinity)
+            3 + ... + O(19^Infinity)
             sage: a < b
             True
         """
@@ -675,12 +675,12 @@ class pAdic(field_element.FieldElement):
         EXAMPLES:
             sage: x = 9*(2+3+O(3**7))
             sage: x.unit_part()
-            2 + 3 + O(3^7)
+            2 + 3 + ... + O(3^7)
             sage: K = Qp(19, 5)
             sage: a = K(2)/19; a
-            2*19^-1 + O(19^4)
+            2*19^-1 + ... + O(19^4)
             sage: a.unit_part()
-            2 + O(19^5)
+            2 + ... + O(19^5)
         """
         return pAdic(self.__parent, self.__unit, self.__prec, 0)
 
@@ -689,7 +689,7 @@ class pAdic(field_element.FieldElement):
             EXAMPLES:
             sage: K = Qp(11)
             sage: a = K(2); a
-            2 + O(11^Infinity)
+            2 + ... + O(11^Infinity)
             sage: a.is_zero()
             False
 
@@ -704,7 +704,7 @@ class pAdic(field_element.FieldElement):
         EXAMPLES:
             sage: K = Qp(11)
             sage: a = K(2); a
-            2 + O(11^Infinity)
+            2 + ... + O(11^Infinity)
             sage: a.is_unit()
             True
             sage: K(121).is_unit()
@@ -731,7 +731,7 @@ class pAdic(field_element.FieldElement):
             sage: a.rational_reconstruction()
             -1
             sage: a = K(2); a
-            2 + O(11^Infinity)
+            2 + ... + O(11^Infinity)
             sage: a.rational_reconstruction()
             2
         """
@@ -782,7 +782,7 @@ class pAdic(field_element.FieldElement):
         EXAMPLES:
             sage: Q13 = Qp(13, 10)
             sage: a = Q13(14); a
-            1 + 13 + O(13^Infinity)
+            1 + 13 + ... + O(13^Infinity)
             sage: a.log()
             13 + 6*13^2 + 2*13^3 + 5*13^4 + 10*13^6 + 13^7 + 11*13^8 + 8*13^9 + O(13^10)
 
@@ -790,7 +790,7 @@ class pAdic(field_element.FieldElement):
         First we create a field with {\em default} precision 10.
             sage: K = pAdicField(5,10)
             sage: e = K(389); e
-            4 + 2*5 + 3*5^3 + O(5^Infinity)
+            4 + 2*5 + 3*5^3 + ... + O(5^Infinity)
 
         If the input has infinite precision, the output is computed to the
         default precision of the parent field. 
diff -r 3ca3f4250d30 -r 8da5c79260af sage/rings/padic_field.py
--- a/sage/rings/padic_field.py Sun Jan 21 18:58:31 2007 -0800
+++ b/sage/rings/padic_field.py Sun Jan 21 19:16:52 2007 -0800
@@ -59,8 +59,22 @@ class pAdicField_generic(field.Field):
         p-adic field is truncated at $O(p^n)$.   Calling print_prec() with
         no arguments returns n.  This command only affects printing,
         and does not alter the actual values of elements of this field.
+
+        INPUT:
+            n -- integer
+                 infinity
+                 None
+
+        EXAMPLES:
+            sage: K = Qp(13, 6)
+            sage: K.print_prec(infinity)
+            sage: a = K(1/2); a
+            7 + 6*13 + 6*13^2 + 6*13^3 + 6*13^4 + 6*13^5 + O(13^6)
+            sage: K.print_prec(3)
+            sage: a
+            7 + 6*13 + 6*13^2 + ... + O(13^6)        
         """
-        if n==None:
+        if n is None:
             return self.__print_prec
         self.__print_prec = n
 
```



---

archive/issue_events_000197.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-01-22T03:27:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/98",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/98#event-197"
}
```
