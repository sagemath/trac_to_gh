# Issue 5981: Sage 3.4.2: prime_pi() broken on 32 bit

Issue created by migration from https://trac.sagemath.org/ticket/5981

Original creator: mabshoff

Original creation time: 2009-05-04 16:45:52

Assignee: mabshoff

This patch fixes the problem:

```
diff -r 8713e0a599f3 sage/functions/prime_pi.pyx
--- a/sage/functions/prime_pi.pyx	Sun May 03 23:10:56 2009 -0700
+++ b/sage/functions/prime_pi.pyx	Mon May 04 12:44:03 2009 -0400
@@ -171,7 +171,7 @@
             raise ValueError, "mem_mult must be positive"
         if x < 2:
             return 0
-        if x > Integer(2**40):
+        if x > 1099511627776L:
             raise NotImplementedError, "computation of prime_pi() greater 2**40 not implemented"
         x += x & 1
         # m_max is the current sieving value, for prime counting - this value is sqrt(x)
```



---

Attachment


---

Comment by mabshoff created at 2009-05-04 17:00:43

Changing status from new to assigned.


---

Comment by jsp created at 2009-05-04 17:08:05

Positive review :)


```

 ./sage -t  "devel/sage/sage/functions/prime_pi.pyx"
sage -t  "devel/sage/sage/functions/prime_pi.pyx"
     [48.1 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 48.1 seconds


Jaap


```



---

Comment by mabshoff created at 2009-05-05 04:20:48

Merged in Sage 3.4.2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-05 04:20:48

Resolution: fixed
