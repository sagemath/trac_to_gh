# Issue 9443: infinite polynomial ring is_integral_domain and is_field omit optional argument 'proof'

Issue created by migration from Trac.

Original creator: niles

Original creation time: 2010-07-07 02:52:26

Assignee: AlexGhitza

Keywords: infinite polynomial ring

Other implementations of is_integral_domain allow an argument 'proof' whose default value is False.  Infinite polynomial ring omits this argument in its definition of is_integral_domain:

sage: W = PolynomialRing(InfinitePolynomialRing(QQ,'a'),2,'x,y')
sage: W.is_integral_domain()
-------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...
TypeError: is_integral_domain() takes exactly 1 argument (2 given)


sage: W = PowerSeriesRing(InfinitePolynomialRing(QQ,'a'),'x')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...
TypeError: is_field() got an unexpected keyword argument 'proof'


---

Attachment

add argument 'proof' with default value False to is_field and is_integral_domain


---

Comment by niles created at 2010-07-07 03:02:18

Changing status from new to needs_review.


---

Comment by niles created at 2010-07-12 15:33:19

apply after previous patch; includes doctests, and updates a few functions to accept positional and keyword arguments; removes duplicate definition of is_field


---

Comment by SimonKing created at 2010-07-30 16:53:56

Changing priority from trivial to major.


---

Attachment

Thank you for working on Infinite Polynomial Rings! Why didn't you add me (as original author) to Cc? I think I am a natural candidate for being reviewer...

First of all, the patches apply cleanly, and `sage -b` does not complain.

Second, I think the patches provide a clean solution. I am sorry that I didn't use `*args` and `**kwds` in the first place.

Third, it is a formal requirement that the commit message of each patch must point to the relevant ticket. So, could you please add "#9443: " or so to the commit messages? Moreover, the attachments name a wrong ticket number (9943 rather than 9443).

Fourth, I am now running `make ptestlong` and report back whether it has worked.

Fifth, since you fix a bug, I believe the priority is certainly not "trivial". I am promoting it to "major".


---

Comment by SimonKing created at 2010-07-30 16:53:56

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2010-07-30 17:51:48

`make ptestlong` is not done yet. But at least I can confirm that the original problem is fixed:

```
sage: W = PolynomialRing(InfinitePolynomialRing(QQ,'a'),2,'x,y')
sage: W.is_integral_domain()
True
sage: W = PowerSeriesRing(InfinitePolynomialRing(QQ,'a'),'x')
sage: W
Power Series Ring in x over Infinite polynomial ring in a over Rational Field
```



---

Comment by SimonKing created at 2010-07-30 20:17:27

All tests pass. 

So, I can give this a positive review - modulo the minor nitpicking about the commit message. This is easy to change.

I hope it is, in this case, correct to mark this ticket as "positive review" but keep the "work issues" field.


---

Comment by SimonKing created at 2010-07-30 20:17:27

Changing status from needs_work to positive_review.


---

Attachment

compined patch replacing the previous two; patch name and commit message fixed


---

Comment by niles created at 2010-08-01 15:11:38

Thanks!  The combined patch should now be complete.


---

Comment by mpatel created at 2010-08-07 06:36:07

Applying [attachment:trac_9443_default_arguments_combined.patch] to the forthcoming Sage 4.5.2, which is just 4.5.2.rc1 + #9226, I see

```
Hunk #1 FAILED at 1036
1 out of 4 hunks FAILED -- saving rejects to file sage/rings/polynomial/infinite_polynomial_ring.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_9443_default_arguments_combined.patch
```

The reject file's contents:

```diff
--- infinite_polynomial_ring.py
+++ infinite_polynomial_ring.py
`@``@` -1037,10 +1037,17 `@``@`
         """
         return False
 
-    def is_field(self,**kwds):
+    def is_field(self, *args, **kwds):
         """
-        Since Infinite Polynomial Rings must have at least one generator, they
-        have infinitely many variables and thus never are fields.
+        Return ``False``, since an infinite polynomial ring has at least one
+        generator and hence infinitely many variables.
+
+        EXAMPLES::
+
+            sage: R.<x, y> = InfinitePolynomialRing(QQ)
+            sage: R.is_field()
+            False
+
 
         TESTS::
 
```


Can someone rebase the patch when it's convenient?  It might be sufficient to work from #9114.


---

Comment by mpatel created at 2010-08-07 06:36:07

Changing status from positive_review to needs_work.


---

Attachment

rebased against #9114 (for 4.5.2); apply only this patch.


---

Comment by niles created at 2010-08-10 20:55:41

should now apply cleanly, although I admit I haven't had time to test it thoroughly.


---

Comment by niles created at 2010-08-10 20:55:41

Changing status from needs_work to needs_review.


---

Attachment

Restore commit string.  Apply only this patch.


---

Comment by mpatel created at 2010-08-10 22:50:48

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-10 22:50:48

Thanks!  The new patch applies cleanly to 4.5.3.alpha0.  I've attached V2, which simply restores the earlier fixed commit message.


---

Comment by mpatel created at 2010-09-15 11:14:08

Resolution: fixed
