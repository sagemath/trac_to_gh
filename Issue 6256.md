# Issue 6256: bug in symbolic arithmetic with exp

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2009-06-10 08:48:57

Assignee: burcin

CC:  jason


```
sage: var('kappa')
kappa
sage: x = sqrt(kappa)
sage: F = exp(x)
sage: F
e^sqrt(kappa)
sage: F/F
e^(2*sqrt(kappa))
sage: 1/F
e^(-sqrt(kappa))
sage: (1/F) * F
e^(2*sqrt(kappa))
```



---

Comment by burcin created at 2009-06-13 22:23:40

Changing status from new to assigned.


---

Comment by burcin created at 2009-06-13 22:23:40

Here is the fix for pynac:

```
diff --git a/ginac/mul.cpp b/ginac/mul.cpp
--- a/ginac/mul.cpp
+++ b/ginac/mul.cpp
`@``@` -1167,7 +1167,7 `@``@`
        if (cmpval != 0) {
                return cmpval;
        }
-       if (seq.size() == 1 && overall_coeff.is_equal(_ex_1))
+       if (seq.size() == 1 && overall_coeff.is_equal(_ex1))
                return 0;
        return 1;
 }
```


I'll post an updated spkg later together with a fix for #6244.


---

Attachment

doctests


---

Comment by burcin created at 2009-06-14 20:59:32

New pynac package fixes this:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.8.p0.spkg

It also contains fixes for #6244 and #6211, so doctests should be run with patches from those tickets applied.


Jason, can you review this?


---

Comment by ncalexan created at 2009-06-14 21:36:21

Fine by me, works with new spkg.


---

Comment by ncalexan created at 2009-06-14 21:36:21

Resolution: fixed
