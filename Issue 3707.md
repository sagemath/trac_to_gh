# Issue 3707: Make all common Sage classes convertible to SymPy

Issue created by migration from Trac.

Original creator: certik

Original creation time: 2008-07-22 11:19:25

Assignee: gfurnish

The attached patch is here like a request for comments. 

We are about to release a new sympy that contains thorough tests for Sage <-> SymPy conversion:

http://hg.sympy.org/sympy/file/16cfc09420ee/sympy/test_external/test_sage.py

When sage 3.0.6 gets released, I'll create a new sympy spkg and expand tests in Sage too, so that we are sure things work in Sage environment too.


---

Comment by malb created at 2008-08-10 13:18:25

*Review*
 * the patch contains functions without doctests and some without documentation
 * Maybe `import sympy` could be avoided in each method using a `late_import` tricK?


---

Comment by certik created at 2008-08-10 15:45:22

Thanks for the review. I'll write doctests and learn about late_import() to see how I could use it.


---

Comment by malb created at 2008-08-10 16:14:59

Replying to [comment:3 certik]:
> Thanks for the review. I'll write doctests and learn about late_import() to see how I could use it.

Examples of this idea (we don't have a framework for that), can be found in:

 * `sage.rings.finite_field_givaro`
 * `sage.libs.pari.gen`
 * `sage.rings.integer`

Looking at those should get you started.


---

Attachment

apply this together with sympy-0.6.2.spkg


---

Attachment


---

Comment by certik created at 2008-08-17 20:39:55

Please update this spkg:

http://sage.math.washington.edu/home/ondrej/spkg/sympy-0.6.2.spkg

and apply the above two patches.

malb: I wrote docstrings and doctests. I didn't use late_import(), as I think in pure python it won't slow things that much and there is a question where I should put this late_import(). But if you think it's necessary, I'll fix that.


---

Attachment

apply after the other patches


---

Comment by malb created at 2008-08-18 10:11:46

*Referee Report*
 * one new function didn't have a doctest (fixed in attached patch)
 * some doctests were failing (fixed in attached patch)
 * `#indirect doctest` directive was missing to make `sage -coverage` happy (fixed in attached patch)
 * One typo (fixed in attached patch)

I'd give the patches a positive review if my fixes are accepted by Ondrej. Ondrej, you now need to check my fixup patch and review it. If you settle for a positive review, then you can change the title to `positive review`.


---

Comment by certik created at 2008-08-18 10:21:32

Oops, thanks you did so much work with it, this is weird, all tests passed for me before posting here. Let me investigate what went wrong, I'll report later.


---

Attachment


---

Comment by certik created at 2008-08-19 22:26:59

My review is +1, only please apply this patch:

trac_3707_fixup.2.patch

instead of yours. The diff is this:

```
$ hg di
diff -r 25553a0bd339 sage/calculus/calculus.py
--- a/sage/calculus/calculus.py	Mon Aug 18 11:04:52 2008 +0100
+++ b/sage/calculus/calculus.py	Tue Aug 19 15:18:50 2008 -0700
`@``@` -5099,7 +5099,8 `@``@`
 
         EXAMPLE:
             sage: x,y = var('x,y')
-            sage: sympy(x) # indirect doctest
+            sage: import sympy
+            sage: sympy.sympify(x) # indirect doctest
             x
         """
```



your version didn't pass doctests, but this should fix it. 

Thanks again for the patch you did, it really helps. I hope all should be fine now. I'll attache the result of sage tests once it finishes.


---

Comment by certik created at 2008-08-19 23:20:03

Here is a result of the tests:

http://sage.math.washington.edu/home/ondrej/ext/sage/devel/sage/test.log

all tests pass. :)

So as to me, it's ok to go in.


---

Comment by malb created at 2008-08-19 23:47:54

I give this a positive review. Ondrej could give the release manager (probably mabshoff) a precise list of patches to apply in which order in a comment? I suspect:
 * sympy0.6.2fix.patch
 * sage_sympy.patch
 * trac_3707_fixup.2.patch
in that order.


---

Comment by certik created at 2008-08-20 07:30:36

Yes, apply the new spkg first and then the patches in exactly this order.

Thanks for the review!


---

Comment by mabshoff created at 2008-08-22 19:21:16

Ondrej,

I did a number of cleanups to spkg-install and SPKG.txt. SPKG.txt still needs some more work, but I guess this has been a step in the right direction. Please base future sympy.spkgs of this one - I did not change the version number.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-22 19:36:43

Merged the patches listed above in Sage 3.1.2.alpha0


---

Comment by mabshoff created at 2008-08-22 19:36:43

Resolution: fixed
