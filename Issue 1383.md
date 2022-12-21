# Issue 1383: Modular Arithmetic Error

Issue created by migration from Trac.

Original creator: trixb4kidz

Original creation time: 2007-12-03 17:32:25

Assignee: trixb4kidz

I recently discovered that the following commands cause a segfault:


```
z = Mod(2, 256)
z^8
```


I have already discovered a solution to this problem, which I will post shortly.


---

Comment by trixb4kidz created at 2007-12-03 17:44:23

I haven't figured out Mercurial yet, so I'll post the fix here.  I will officially submit a patch later today.

The bug is in the class `IntegerMod_gmp` in `sage/rings/integer_mod.pyx` .  The function `mod_pow_int` needs to be modified as follows:




```

cdef int_fast32_t mod_pow_int(int_fast32_t base, int_fast32_t exp, int_fast32_t n):
    """
    Returns base^exp mod n
    For use in IntegerMod_int
    AUTHOR:
      -- Robert Bradshaw
    """
    cdef int_fast32_t prod, pow2
    if exp <= 5:
        if exp == 0: return 1
        if exp == 1: return base
        prod = base * base % n
        if exp == 2: return prod
        if exp == 3: return (prod * base) % n
        if exp == 4: return (prod * prod) % n

    pow2 = base
    if exp % 2: prod = base
    else: prod = 1
    exp = exp >> 1
    while(exp != 0):
        pow2 = pow2 * pow2
        if pow2 >= INTEGER_MOD_INT32_LIMIT: pow2 = pow2 % n
        if exp % 2:
            prod = prod * pow2

            if prod >= INTEGER_MOD_INT32_LIMIT: prod = prod % n
        exp = exp >> 1

    #######################################################
    #    THIS IS THE BUG.  THIS SHOULD READ prod >= n.    #
    #######################################################
    if prod > n:
        prod = prod % n
    return prod


```



---

Comment by mabshoff created at 2007-12-03 19:55:39

I applied the following patch and doctests pass:

```
# HG changeset patch
# User mabshoff`@`sage.math.washington.edu
# Date 1196711612 28800
# Node ID 612d5a72a9e1a9c4eb90a0c746da5a358882b5a0
# Parent  f6137fb146cb310be74c0ddb22faa3ee5eaa71a4
Fix modp arithmetic bug [fix by trixb4kidz], added doctest

diff -r f6137fb146cb -r 612d5a72a9e1 sage/rings/integer_mod.pyx
--- a/sage/rings/integer_mod.pyx        Mon Dec 03 11:26:06 2007 -0800
+++ b/sage/rings/integer_mod.pyx        Mon Dec 03 11:53:32 2007 -0800
`@``@` -1836,6 +1836,12 `@``@` cdef int_fast32_t mod_pow_int(int_fast32
     """
     Returns base^exp mod n
     For use in IntegerMod_int
+
+    EXAMPLES:
+       sage: z = Mod(2, 256)
+       sage: z^8
+       0
+
     AUTHOR:
       -- Robert Bradshaw
     """
`@``@` -1860,7 +1866,7 `@``@` cdef int_fast32_t mod_pow_int(int_fast32
             if prod >= INTEGER_MOD_INT32_LIMIT: prod = prod % n
         exp = exp >> 1

-    if prod > n:
+    if prod >= n:
         prod = prod % n
     return prod
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-12-03 19:58:41

Merged in 2.8.15.rc1.


---

Comment by mabshoff created at 2007-12-03 19:58:41

Resolution: fixed
