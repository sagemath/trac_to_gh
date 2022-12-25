# Issue 4667: [with first patch, not ready for review] quadratic twists for p-adic L-functions

archive/issues_004667.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @JohnCremona @williamstein\n\nKeywords: padic l-functions, quadratic twists\n\nThis ticket is aimed at implementing p-adic L-function of quadratic twists of elliptic curves.\n\nOf course one could compute the modular symbols for the twist and then the p-adic L-function, but it is much faster to use the simple formula for the twisted modular symbols as a sum of \nmodular symbols. See section 8 in Mazur-Tate-Teitelbaum = [MTT].\n\nHere is a list of things implemented and changed by this patch. Maybe this is too long and it\nwould be preferable to split it up into smaller patches. I will add more documentation and more compatibility checks in the docstring.\n\n## ell_modular_symbol.py\n\nI changed completely the normalization. Until now, the normalization was done in such a way as to guarantee that [0]+, the modular_symbol(0) for sign=+1, is equal to L(E_0,1)/Omega_E_0, where E_0 is the optimal X_0(N) curve in the isogeny class of E and Omega_* is the least positive real period of E. Up to sign, which was arbitrary, and up to a factor 2, which comes from the fact that we do not know that the Manin-constant is 1 as it should be. (I hope I got this right).\n\nNow instead I normalize it in such a way as to make sure that [0]+ is equal to L(E,1)/Omega_E. So the result will depend on the curve E and not only on the isogeny class. Let {0}+ be the non-normalized modular symbol. If the above algebraic L-value is non-zero, then so is {0}+ and they are rational multiples of each other with small numerator and denominator. So we just compute a real approximation to this fraction and we scale {0}+ to get [0]+. If the L-value is zero, then we try to use a quadratic twist of E by a small positive (or later negative) fundamental discriminant, hoping that we will hit one that is not zero. If we fail to find one, we have to go back to the previous way of normalizing, but multiplying with Omega_E_0/Omega_E as to make sure that the missed factor +-1/2 is the same for all curves in the isogeny class. And we issue a warning to the user.\n\nRight now, I substituted the normalization by mine, it would be easy to change the optional argument in such a way as to allow the user to choose between the two normalizations.\n\nI have tested the correctness of this for hundreds of curves, using twists by -31 and 37 that do\nnot appear in the code. Of course, there will be curves for which the new normalization fails. For negative modular symbols we only use negative twists (in order to avoid an obvious infinite loop). But we are safe to assume that negative modular symbols are not very often used without the positive ones.\n\nI have not rewritten the normalization of modular symbols coming from ec_lib in padic_lseries.py. This should be done, but I have no idea if the negative symbols can be computed with that library.\n\nAdded more docstrings.\n\n## padic_lseries.py\n\nI got rid of _quotient_of_period which is no longer needed because of the above normalization.\nI added a try around the cremona-label look-up. Caused a bug before. modular_symbol has now an optional argument to twist by a fundamental discriminant D. Similar for measure and series.\nNew we need a function to compute the quotient of Omega_E by Omega_(ED)*sqrt(D), if D>0, or Omega-_E by  Omega_(ED)*sqrt(-D), if D<0. According to [MTT] this should be 1 or 2. This\nis done in _quotient_of_periods_to_twist.\n\nFurthermore, I have changed the sign of the Dp-values height, just like I had to change the sign in the canonical p-adic height in the ordinary case.\n \nSo far I have tested this on good ordinary primes for curves of rank 0 and rank 1 and some rank 2 curves. I have also checked a few supersingular cases.\n\n## padics.py\n\nI changed the sign of the padic height. It is now clear that there must be a -1 in front to make sure that the p-adic BSD conjecture holds as stated in [MTT].\nI also removed the statement that the equation must be globally minimal to compute the height as the gens() no longer fails for non-minimal curves.\n\n\n## ell_rational_field.py\n\nadjusted the documentation according to the change in ell_modular_symbol.\nadded a function minimal_quadratic_twist that find a twist of E with minimal conductor. This is used in sha_tate.py but could be of use later in rank as well.\n\ntodo : normalization if using ec_lib (?)\n\ntodo : add in rank() the possibility to use modular-symbols for a twisted curve with low conductor\n\n## sha_tate.py\n\nan_padic has now an optional argument to control whether the modular symbols computations can be done on a minimal quadratic twist instead.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4667\n\n",
    "created_at": "2008-12-01T00:07:59Z",
    "labels": [
        "component: number theory",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with first patch, not ready for review] quadratic twists for p-adic L-functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4667",
    "user": "https://github.com/categorie"
}
```
Assignee: @williamstein

CC:  @JohnCremona @williamstein

Keywords: padic l-functions, quadratic twists

This ticket is aimed at implementing p-adic L-function of quadratic twists of elliptic curves.

Of course one could compute the modular symbols for the twist and then the p-adic L-function, but it is much faster to use the simple formula for the twisted modular symbols as a sum of 
modular symbols. See section 8 in Mazur-Tate-Teitelbaum = [MTT].

Here is a list of things implemented and changed by this patch. Maybe this is too long and it
would be preferable to split it up into smaller patches. I will add more documentation and more compatibility checks in the docstring.

## ell_modular_symbol.py

I changed completely the normalization. Until now, the normalization was done in such a way as to guarantee that [0]+, the modular_symbol(0) for sign=+1, is equal to L(E_0,1)/Omega_E_0, where E_0 is the optimal X_0(N) curve in the isogeny class of E and Omega_* is the least positive real period of E. Up to sign, which was arbitrary, and up to a factor 2, which comes from the fact that we do not know that the Manin-constant is 1 as it should be. (I hope I got this right).

Now instead I normalize it in such a way as to make sure that [0]+ is equal to L(E,1)/Omega_E. So the result will depend on the curve E and not only on the isogeny class. Let {0}+ be the non-normalized modular symbol. If the above algebraic L-value is non-zero, then so is {0}+ and they are rational multiples of each other with small numerator and denominator. So we just compute a real approximation to this fraction and we scale {0}+ to get [0]+. If the L-value is zero, then we try to use a quadratic twist of E by a small positive (or later negative) fundamental discriminant, hoping that we will hit one that is not zero. If we fail to find one, we have to go back to the previous way of normalizing, but multiplying with Omega_E_0/Omega_E as to make sure that the missed factor +-1/2 is the same for all curves in the isogeny class. And we issue a warning to the user.

Right now, I substituted the normalization by mine, it would be easy to change the optional argument in such a way as to allow the user to choose between the two normalizations.

I have tested the correctness of this for hundreds of curves, using twists by -31 and 37 that do
not appear in the code. Of course, there will be curves for which the new normalization fails. For negative modular symbols we only use negative twists (in order to avoid an obvious infinite loop). But we are safe to assume that negative modular symbols are not very often used without the positive ones.

I have not rewritten the normalization of modular symbols coming from ec_lib in padic_lseries.py. This should be done, but I have no idea if the negative symbols can be computed with that library.

Added more docstrings.

## padic_lseries.py

I got rid of _quotient_of_period which is no longer needed because of the above normalization.
I added a try around the cremona-label look-up. Caused a bug before. modular_symbol has now an optional argument to twist by a fundamental discriminant D. Similar for measure and series.
New we need a function to compute the quotient of Omega_E by Omega_(ED)*sqrt(D), if D>0, or Omega-_E by  Omega_(ED)*sqrt(-D), if D<0. According to [MTT] this should be 1 or 2. This
is done in _quotient_of_periods_to_twist.

Furthermore, I have changed the sign of the Dp-values height, just like I had to change the sign in the canonical p-adic height in the ordinary case.
 
So far I have tested this on good ordinary primes for curves of rank 0 and rank 1 and some rank 2 curves. I have also checked a few supersingular cases.

## padics.py

I changed the sign of the padic height. It is now clear that there must be a -1 in front to make sure that the p-adic BSD conjecture holds as stated in [MTT].
I also removed the statement that the equation must be globally minimal to compute the height as the gens() no longer fails for non-minimal curves.


## ell_rational_field.py

adjusted the documentation according to the change in ell_modular_symbol.
added a function minimal_quadratic_twist that find a twist of E with minimal conductor. This is used in sha_tate.py but could be of use later in rank as well.

todo : normalization if using ec_lib (?)

todo : add in rank() the possibility to use modular-symbols for a twisted curve with low conductor

## sha_tate.py

an_padic has now an optional argument to control whether the modular symbols computations can be done on a minimal quadratic twist instead.

Issue created by migration from https://trac.sagemath.org/ticket/4667





---

archive/issue_comments_035067.json:
```json
{
    "body": "the first part.",
    "created_at": "2008-12-01T00:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35067",
    "user": "https://github.com/categorie"
}
```

the first part.



---

archive/issue_comments_035068.json:
```json
{
    "body": "Attachment [twisted_padic_l_functions.1.patch](tarball://root/attachments/some-uuid/ticket4667/twisted_padic_l_functions.1.patch) by @categorie created at 2008-12-10 12:48:16\n\nWith respect to the above description, this new version of the patch does everything as said before, but the modular_symbols are handled differently.\n\nIn ell_modular_symbol there are now two option, either to use or not to use eclib (for the + part at least). I implemented an optional argument that controls what method is used to normalize the modular symbols, for both eclib and sage's own modular symbols.",
    "created_at": "2008-12-10T12:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35068",
    "user": "https://github.com/categorie"
}
```

Attachment [twisted_padic_l_functions.1.patch](tarball://root/attachments/some-uuid/ticket4667/twisted_padic_l_functions.1.patch) by @categorie created at 2008-12-10 12:48:16

With respect to the above description, this new version of the patch does everything as said before, but the modular_symbols are handled differently.

In ell_modular_symbol there are now two option, either to use or not to use eclib (for the + part at least). I implemented an optional argument that controls what method is used to normalize the modular symbols, for both eclib and sage's own modular symbols.



---

archive/issue_events_010681.json:
```json
{
    "actor": "https://github.com/categorie",
    "created_at": "2008-12-10T12:48:16Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "milestone": "sage-3.2.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4667#event-10681"
}
```



---

archive/issue_comments_035069.json:
```json
{
    "body": "New Patch, replaces the first patch. Exported against 3.2.1.",
    "created_at": "2008-12-10T12:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35069",
    "user": "https://github.com/categorie"
}
```

New Patch, replaces the first patch. Exported against 3.2.1.



---

archive/issue_comments_035070.json:
```json
{
    "body": "Attachment [twisted_padic_lseries.patch](tarball://root/attachments/some-uuid/ticket4667/twisted_padic_lseries.patch) by GeorgSWeber created at 2008-12-29 21:12:25\n\nTarget time for the review: January 10th",
    "created_at": "2008-12-29T21:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35070",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Attachment [twisted_padic_lseries.patch](tarball://root/attachments/some-uuid/ticket4667/twisted_padic_lseries.patch) by GeorgSWeber created at 2008-12-29 21:12:25

Target time for the review: January 10th



---

archive/issue_comments_035071.json:
```json
{
    "body": "Rescheduled for January 18th",
    "created_at": "2009-01-15T21:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35071",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Rescheduled for January 18th



---

archive/issue_comments_035072.json:
```json
{
    "body": "Needs work, but only minor issues:\n\n```\napplying ../../../patches/twisted_padic_lseries.patch\npatching file sage/schemes/elliptic_curves/ell_rational_field.py\nHunk #5 FAILED at 4640\n1 out of 5 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_rational_field.py.rej\nabort: patch failed to apply\n```\n\nThat one hunk is only an empty line replacing an empty line (?!?), so could be ignored (and wouldn't prevent a positive review from my side). But there's real work also, some doctest failures:\n\n```\nsage -t -long \"local/lib/python/site-packages/sage/schemes/elliptic_curves/padic_lseries.py\"\n**********************************************************************\nFile \"/Users/georgweber/Public/sage/sage-3.2.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/padic_lseries.py\", line 644:\n    sage: E.quadratic_twist(-19).label()\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/georgweber/Public/sage/sage-3.2.3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/georgweber/Public/sage/sage-3.2.3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/georgweber/Public/sage/sage-3.2.3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_14[22]>\", line 1, in <module>\n        E.quadratic_twist(-Integer(19)).label()###line 644:\n    sage: E.quadratic_twist(-19).label()\n      File \"/Users/georgweber/Public/sage/sage-3.2.3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py\", line 2720, in cremona_label\n        raise RuntimeError, \"Cremona label not known for %s.\"%self\n    RuntimeError: Cremona label not known for Elliptic Curve defined by y^2 + y = x^3 - x^2 - 120*x - 2183 over Rational Field.\n**********************************************************************\n1 items had failures:\n   1 of  23 in __main__.example_14\n***Test Failed*** 1 failures.\n```\n\nThe doctest failure above seems to come from that I used a vanilla Sage 3.2.3, and the example seems to need the optional extended Cremona tables --- so just add a \"#optional\" or so.\n\nThere are also a bunch of doctest failures for \"sha_tate.py\", which pop up (only) if the doctest \"-long\" option is used.\n\n```\nsage -t -long \"local/lib/python/site-packages/sage/schemes/elliptic_curves/sha_tate.py\"\n**********************************************************************\nFile \"/Users/georgweber/Public/sage/sage-3.2.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/sha_tate.py\", line 276:\n    sage: EllipticCurve('123a1').sha().an_padic(41) #rank 1    (long time)\nExpected:\n    1 + O(41)\nGot:\n    40 + O(41)\n**********************************************************************\nFile \"/Users/georgweber/Public/sage/sage-3.2.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/sha_tate.py\", line 283:\n    sage: EllipticCurve('34a1').sha().an_padic(5) # rank 0     (long time)\nException raised:\n.......\n    sage: EllipticCurve('34a1').sha().an_padic(5) # rank 0     (long time)\n      File \"/Users/georgweber/Public/sage/sage-3.2.3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/sha_tate.py\", line 394, in an_padic\n        lps = lp.Dp_valued_series(n,quadratic_twist=D,prec=r+1)\n    TypeError: Dp_valued_series() got an unexpected keyword argument 'quadratic_twist'\n........\n    sage: e.sha().p_primary_bound(7)           # long time\n      File \"/Users/georgweber/Public/sage/sage-3.2.3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/sha_tate.py\", line 458, in p_primary_bound\n        shan = self.an_padic(p,prec = 0,use_twist=True)\n    TypeError: an_padic() got an unexpected keyword argument 'use_twist'\n```\n\nExcept for the first (which might be architecture related, the old file had this doctest with a \"#random\" comment --- I'm using a Mac) all the following \"long\" doctest failures in sha_tate.py just seem to be artifacts from development, easily to be cleaned up.\n\nAll in all: nothing serious, but as-is it can't go in.",
    "created_at": "2009-01-18T23:43:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35072",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Needs work, but only minor issues:

```
applying ../../../patches/twisted_padic_lseries.patch
patching file sage/schemes/elliptic_curves/ell_rational_field.py
Hunk #5 FAILED at 4640
1 out of 5 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_rational_field.py.rej
abort: patch failed to apply
```

That one hunk is only an empty line replacing an empty line (?!?), so could be ignored (and wouldn't prevent a positive review from my side). But there's real work also, some doctest failures:

```
sage -t -long "local/lib/python/site-packages/sage/schemes/elliptic_curves/padic_lseries.py"
**********************************************************************
File "/Users/georgweber/Public/sage/sage-3.2.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/padic_lseries.py", line 644:
    sage: E.quadratic_twist(-19).label()
Exception raised:
    Traceback (most recent call last):
      File "/Users/georgweber/Public/sage/sage-3.2.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/georgweber/Public/sage/sage-3.2.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/georgweber/Public/sage/sage-3.2.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_14[22]>", line 1, in <module>
        E.quadratic_twist(-Integer(19)).label()###line 644:
    sage: E.quadratic_twist(-19).label()
      File "/Users/georgweber/Public/sage/sage-3.2.3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 2720, in cremona_label
        raise RuntimeError, "Cremona label not known for %s."%self
    RuntimeError: Cremona label not known for Elliptic Curve defined by y^2 + y = x^3 - x^2 - 120*x - 2183 over Rational Field.
**********************************************************************
1 items had failures:
   1 of  23 in __main__.example_14
***Test Failed*** 1 failures.
```

The doctest failure above seems to come from that I used a vanilla Sage 3.2.3, and the example seems to need the optional extended Cremona tables --- so just add a "#optional" or so.

There are also a bunch of doctest failures for "sha_tate.py", which pop up (only) if the doctest "-long" option is used.

```
sage -t -long "local/lib/python/site-packages/sage/schemes/elliptic_curves/sha_tate.py"
**********************************************************************
File "/Users/georgweber/Public/sage/sage-3.2.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/sha_tate.py", line 276:
    sage: EllipticCurve('123a1').sha().an_padic(41) #rank 1    (long time)
Expected:
    1 + O(41)
Got:
    40 + O(41)
**********************************************************************
File "/Users/georgweber/Public/sage/sage-3.2.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/sha_tate.py", line 283:
    sage: EllipticCurve('34a1').sha().an_padic(5) # rank 0     (long time)
Exception raised:
.......
    sage: EllipticCurve('34a1').sha().an_padic(5) # rank 0     (long time)
      File "/Users/georgweber/Public/sage/sage-3.2.3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/sha_tate.py", line 394, in an_padic
        lps = lp.Dp_valued_series(n,quadratic_twist=D,prec=r+1)
    TypeError: Dp_valued_series() got an unexpected keyword argument 'quadratic_twist'
........
    sage: e.sha().p_primary_bound(7)           # long time
      File "/Users/georgweber/Public/sage/sage-3.2.3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/sha_tate.py", line 458, in p_primary_bound
        shan = self.an_padic(p,prec = 0,use_twist=True)
    TypeError: an_padic() got an unexpected keyword argument 'use_twist'
```

Except for the first (which might be architecture related, the old file had this doctest with a "#random" comment --- I'm using a Mac) all the following "long" doctest failures in sha_tate.py just seem to be artifacts from development, easily to be cleaned up.

All in all: nothing serious, but as-is it can't go in.



---

archive/issue_comments_035073.json:
```json
{
    "body": "Finally it was easier to correct than what I thought. I simply forgot to change the sign in the p-adic height for split multiplicative primes. \n\nThe new patch should apply cleanly against 3.3.rc3 ( i hope ) and no test (with -long) failed except for\n\nthe issue about the unknown Cremona label in line 644 that Gregor mentioned. I don't know how to solve this; the error only occurs if the optional package _is_ present. It does not belong to this trac ticket anyway.\n\nchris.",
    "created_at": "2009-02-21T16:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35073",
    "user": "https://github.com/categorie"
}
```

Finally it was easier to correct than what I thought. I simply forgot to change the sign in the p-adic height for split multiplicative primes. 

The new patch should apply cleanly against 3.3.rc3 ( i hope ) and no test (with -long) failed except for

the issue about the unknown Cremona label in line 644 that Gregor mentioned. I don't know how to solve this; the error only occurs if the optional package _is_ present. It does not belong to this trac ticket anyway.

chris.



---

archive/issue_comments_035074.json:
```json
{
    "body": "New patch, replaces the previous two. Exported against 3.3.rc3",
    "created_at": "2009-02-21T16:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35074",
    "user": "https://github.com/categorie"
}
```

New patch, replaces the previous two. Exported against 3.3.rc3



---

archive/issue_comments_035075.json:
```json
{
    "body": "Attachment [trac4667.twisted_padic_lseries.patch](tarball://root/attachments/some-uuid/ticket4667/trac4667.twisted_padic_lseries.patch) by GeorgSWeber created at 2009-02-26 05:17:01\n\napply after the last one above (it changes only one line)",
    "created_at": "2009-02-26T05:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35075",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Attachment [trac4667.twisted_padic_lseries.patch](tarball://root/attachments/some-uuid/ticket4667/trac4667.twisted_padic_lseries.patch) by GeorgSWeber created at 2009-02-26 05:17:01

apply after the last one above (it changes only one line)



---

archive/issue_comments_035076.json:
```json
{
    "body": "Attachment [trac4667_doctestfix.patch](tarball://root/attachments/some-uuid/ticket4667/trac4667_doctestfix.patch) by GeorgSWeber created at 2009-02-26 05:24:17\n\nAs I said in my remark of #4933, this patch here definitely should be applied before any work on #4933 is done.\n\nCould you help with the rebase? It's just two of the six files where rebasing is needed, and with the scripts, shouldn't it be rather easy?\n\nP.S.:\n\nApply the last two patches only, the latter is just a one-liner that makes a certain doctest optional. That doctest is only of illustrative nature anyway, and depends on the optional larger Cremona ell curves database for curves of conductor between 10000 and 130000. (A curve of conductor around 15000 is involved.)",
    "created_at": "2009-02-26T05:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35076",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Attachment [trac4667_doctestfix.patch](tarball://root/attachments/some-uuid/ticket4667/trac4667_doctestfix.patch) by GeorgSWeber created at 2009-02-26 05:24:17

As I said in my remark of #4933, this patch here definitely should be applied before any work on #4933 is done.

Could you help with the rebase? It's just two of the six files where rebasing is needed, and with the scripts, shouldn't it be rather easy?

P.S.:

Apply the last two patches only, the latter is just a one-liner that makes a certain doctest optional. That doctest is only of illustrative nature anyway, and depends on the optional larger Cremona ell curves database for curves of conductor between 10000 and 130000. (A curve of conductor around 15000 is involved.)



---

archive/issue_events_010682.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber",
    "created_at": "2009-02-26T05:24:17Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "milestone": "sage-3.2.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4667#event-10682"
}
```



---

archive/issue_events_010683.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber",
    "created_at": "2009-02-26T05:24:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "milestone": "sage-3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4667#event-10683"
}
```



---

archive/issue_events_010684.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-01T02:03:51Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "milestone": "sage-3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4667#event-10684"
}
```



---

archive/issue_events_010685.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-01T02:03:51Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4667#event-10685"
}
```



---

archive/issue_comments_035077.json:
```json
{
    "body": "Once the rebase has been done the positive review can be added back.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T07:20:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35077",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Once the rebase has been done the positive review can be added back.

Cheers,

Michael



---

archive/issue_comments_035078.json:
```json
{
    "body": "OK, it took me some work to rebase it. Of course the docstrings are not all restified, but this should be done in #4933.\n\nI attach a new patch that will replace all others before. It was exported against my sage 3.4.\n\nI added the 'positive review' back, but maybe soneone else should check the tests again, indep. of me.",
    "created_at": "2009-03-25T19:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35078",
    "user": "https://github.com/categorie"
}
```

OK, it took me some work to rebase it. Of course the docstrings are not all restified, but this should be done in #4933.

I attach a new patch that will replace all others before. It was exported against my sage 3.4.

I added the 'positive review' back, but maybe soneone else should check the tests again, indep. of me.



---

archive/issue_comments_035079.json:
```json
{
    "body": "Attachment [trac_4667_z.patch](tarball://root/attachments/some-uuid/ticket4667/trac_4667_z.patch) by @categorie created at 2009-03-25 19:23:27\n\nReplaces all previous patches.",
    "created_at": "2009-03-25T19:23:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35079",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_4667_z.patch](tarball://root/attachments/some-uuid/ticket4667/trac_4667_z.patch) by @categorie created at 2009-03-25 19:23:27

Replaces all previous patches.



---

archive/issue_comments_035080.json:
```json
{
    "body": "The latest patch causes doctest failures in two files:\n\n```\n\tsage -t -long devel/sage/doc/en/bordeaux_2008/elliptic_curves.rst # 2 doctests failed\n\tsage -t -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # 6 doctests failed\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T23:45:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35080",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The latest patch causes doctest failures in two files:

```
	sage -t -long devel/sage/doc/en/bordeaux_2008/elliptic_curves.rst # 2 doctests failed
	sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # 6 doctests failed
```


Cheers,

Michael



---

archive/issue_comments_035081.json:
```json
{
    "body": "Michael,\n\nbegging your pardon, but I see none of these doctest failures against vanilla Sage-3.4 on my MacIntel box. I do confirm \"positive review\" (just finished testlong and docbuild)! Let's wait for 3.4.1.alpha and see, I think the reason is that some other patch that went already in your local tree causes this. It should be sorted out easily, once the first 3.4.1.alpha release is out. :-)\n\nCheers,\ngsw",
    "created_at": "2009-03-26T00:19:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35081",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Michael,

begging your pardon, but I see none of these doctest failures against vanilla Sage-3.4 on my MacIntel box. I do confirm "positive review" (just finished testlong and docbuild)! Let's wait for 3.4.1.alpha and see, I think the reason is that some other patch that went already in your local tree causes this. It should be sorted out easily, once the first 3.4.1.alpha release is out. :-)

Cheers,
gsw



---

archive/issue_events_010686.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber",
    "created_at": "2009-03-26T00:19:12Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4667#event-10686"
}
```



---

archive/issue_events_010687.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber",
    "created_at": "2009-03-26T00:19:12Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4667#event-10687"
}
```



---

archive/issue_comments_035082.json:
```json
{
    "body": "Replying to [comment:12 GeorgSWeber]:\n> Michael,\n> \n> begging your pardon, but I see none of these doctest failures against vanilla Sage-3.4 on my MacIntel box. I do confirm \"positive review\" (just finished testlong and docbuild)! Let's wait for 3.4.1.alpha and see, I think the reason is that some other patch that went already in your local tree causes this. It should be sorted out easily, once the first 3.4.1.alpha release is out. :-)\n\nThese failures happen against my merge tree, so no point in reinstating the positive review. I would also prefer if William took a look at this patch since he seemed to have written most of the original code.\n\n> Cheers,\n> gsw\n\nCheers,\n\nMichael",
    "created_at": "2009-03-26T00:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35082",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:12 GeorgSWeber]:
> Michael,
> 
> begging your pardon, but I see none of these doctest failures against vanilla Sage-3.4 on my MacIntel box. I do confirm "positive review" (just finished testlong and docbuild)! Let's wait for 3.4.1.alpha and see, I think the reason is that some other patch that went already in your local tree causes this. It should be sorted out easily, once the first 3.4.1.alpha release is out. :-)

These failures happen against my merge tree, so no point in reinstating the positive review. I would also prefer if William took a look at this patch since he seemed to have written most of the original code.

> Cheers,
> gsw

Cheers,

Michael



---

archive/issue_events_010688.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber",
    "created_at": "2009-03-26T00:55:51Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4667#event-10688"
}
```



---

archive/issue_events_010689.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber",
    "created_at": "2009-03-26T00:55:51Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4667#event-10689"
}
```



---

archive/issue_comments_035083.json:
```json
{
    "body": "Uh oh.\n\nNo offense meant, I was just too excited so I started the review after midnight.\n\nAnd sorry, my fault, I re-checked my setup and it seems that somehow I had forgotten a \"sage -b\" in the course. I do see the failures against vanilla sage-3.4, and they seem to be severe:\n\n```\nFile \"/Users/georgweber/Public/sage/sage-3.4/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py\", line 5164:\n    sage: [P[0] for P in EllipticCurve([0,0,0,-468,2592]).integral_points()]\nExpected:\n    [-24, -18, -14, -6, -3, 4, 6, 18, 21, 24, 36, 46, 102, 168, 186, 381, 1476, 2034, 67246]\nGot:\n    [-24, -18, -14, -6, -3, 4, 6, 18, 21, 24, 36, 46, 102, 186]\n```\n\nand most of the other failed doctests also point to missing integral points. There had been a patch of John (IIRC) that had healed an issue with this, and the current patch of Chris seems to miss these parts (more precisely seems to revert the code to the old buggy state).\n\nAs a by-result, this means that I definitely shouldn't try to review patches without being well-rested. Which probably means I won't be able to do reviews at all. :-((( \n\nCheers,\ngsw",
    "created_at": "2009-03-26T00:55:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35083",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Uh oh.

No offense meant, I was just too excited so I started the review after midnight.

And sorry, my fault, I re-checked my setup and it seems that somehow I had forgotten a "sage -b" in the course. I do see the failures against vanilla sage-3.4, and they seem to be severe:

```
File "/Users/georgweber/Public/sage/sage-3.4/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 5164:
    sage: [P[0] for P in EllipticCurve([0,0,0,-468,2592]).integral_points()]
Expected:
    [-24, -18, -14, -6, -3, 4, 6, 18, 21, 24, 36, 46, 102, 168, 186, 381, 1476, 2034, 67246]
Got:
    [-24, -18, -14, -6, -3, 4, 6, 18, 21, 24, 36, 46, 102, 186]
```

and most of the other failed doctests also point to missing integral points. There had been a patch of John (IIRC) that had healed an issue with this, and the current patch of Chris seems to miss these parts (more precisely seems to revert the code to the old buggy state).

As a by-result, this means that I definitely shouldn't try to review patches without being well-rested. Which probably means I won't be able to do reviews at all. :-((( 

Cheers,
gsw



---

archive/issue_comments_035084.json:
```json
{
    "body": "Uiuiui, I am sorry that was quite bad. I did not merge well ell_rational_field. \n\nI add another patch that should be applied after the previous. \nIt looks to me as if everything passes now. Except\n\n\n```\nFile \"/maths/staff/pmzcw/Desktop/sage/twists/elliptic_curves/ell_rational_field.py\", line 3096:\n    sage: E.cremona_label()\nExpected:\n    Traceback (most recent call last):\n    ...\n    RuntimeError: Cremona label not known for Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 5 over Rational Field.\nGot:\n    '10351a1'\n```\n\n\nbut this is due to having installed the optional package. I still don't know if there is a way to include a test only if the optional package is NOT there. But anyway that is not in my code.",
    "created_at": "2009-03-26T15:03:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35084",
    "user": "https://github.com/categorie"
}
```

Uiuiui, I am sorry that was quite bad. I did not merge well ell_rational_field. 

I add another patch that should be applied after the previous. 
It looks to me as if everything passes now. Except


```
File "/maths/staff/pmzcw/Desktop/sage/twists/elliptic_curves/ell_rational_field.py", line 3096:
    sage: E.cremona_label()
Expected:
    Traceback (most recent call last):
    ...
    RuntimeError: Cremona label not known for Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 5 over Rational Field.
Got:
    '10351a1'
```


but this is due to having installed the optional package. I still don't know if there is a way to include a test only if the optional package is NOT there. But anyway that is not in my code.



---

archive/issue_comments_035085.json:
```json
{
    "body": "Attachment [trac_4667_z2.patch](tarball://root/attachments/some-uuid/ticket4667/trac_4667_z2.patch) by @categorie created at 2009-03-26 15:04:10\n\napply after the previous patch",
    "created_at": "2009-03-26T15:04:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35085",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_4667_z2.patch](tarball://root/attachments/some-uuid/ticket4667/trac_4667_z2.patch) by @categorie created at 2009-03-26 15:04:10

apply after the previous patch



---

archive/issue_comments_035086.json:
```json
{
    "body": "I just found out that my issue with the optional package has actually a trac ticket : #5346 .",
    "created_at": "2009-03-26T15:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35086",
    "user": "https://github.com/categorie"
}
```

I just found out that my issue with the optional package has actually a trac ticket : #5346 .



---

archive/issue_comments_035087.json:
```json
{
    "body": "Ok, changed the summary to have the ticket picked up by the right reports again. I would also be happy if John and/or William looked at this code since it seems to touch code they have written.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-26T20:40:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35087",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, changed the summary to have the ticket picked up by the right reports again. I would also be happy if John and/or William looked at this code since it seems to touch code they have written.

Cheers,

Michael



---

archive/issue_comments_035088.json:
```json
{
    "body": "There are two aspects to be considered with a patch of this kind:\n\n- The technical one (is the code correctly merged into the system, or are regressions introduced?). In this area of Sage I would trust the doctests, especially John has added valuable ones that should cover enough cases so regressions are caught. As was exactly the case, BTW! A reviewer has to have an eye on the new code in this regard, too --- would the new doctests show regressions possibly introduced later? (Let's say some erronuous future patch to the core code of the p-adic numbers?) I did covince myself of that two months ago, but would like to look into it again now. And alas, I seem to desparately need the oncoming two weeks Easter vacation (where I will have no Internet access at all).\n\n- The theoretical one (do the mathematics make sense, are the normalizations reasonable, and such?) In this regard, the patch of Chris is an absolute win for Sage. The original p-adic L-series code of William was OK, and it was good to have that code in Sage at all. But the reworkings of Chris are certainly enhancements heading in the right direction --- William?\n\nI certainly want to make Michael's (the integrator's) life easier, not harder. And from the experience yesterday I don't trust myself right now (it's again only 10 minutes before midnight). So either the review has to wait for, say, another month or so, or a new reviewer steps in. William, John?",
    "created_at": "2009-03-26T22:57:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35088",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

There are two aspects to be considered with a patch of this kind:

- The technical one (is the code correctly merged into the system, or are regressions introduced?). In this area of Sage I would trust the doctests, especially John has added valuable ones that should cover enough cases so regressions are caught. As was exactly the case, BTW! A reviewer has to have an eye on the new code in this regard, too --- would the new doctests show regressions possibly introduced later? (Let's say some erronuous future patch to the core code of the p-adic numbers?) I did covince myself of that two months ago, but would like to look into it again now. And alas, I seem to desparately need the oncoming two weeks Easter vacation (where I will have no Internet access at all).

- The theoretical one (do the mathematics make sense, are the normalizations reasonable, and such?) In this regard, the patch of Chris is an absolute win for Sage. The original p-adic L-series code of William was OK, and it was good to have that code in Sage at all. But the reworkings of Chris are certainly enhancements heading in the right direction --- William?

I certainly want to make Michael's (the integrator's) life easier, not harder. And from the experience yesterday I don't trust myself right now (it's again only 10 minutes before midnight). So either the review has to wait for, say, another month or so, or a new reviewer steps in. William, John?



---

archive/issue_comments_035089.json:
```json
{
    "body": "Concerning the issue with the optional database: I have added a comment to trac #5346 with an idea how to address it --- this idea applies verbatim here. Chris, you certainly are able to provide a concrete example of a (twist of a) curve such that the resulting conductor is larger than 130000, in less than a minute? \n\nCheers, gsw",
    "created_at": "2009-03-26T23:10:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35089",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Concerning the issue with the optional database: I have added a comment to trac #5346 with an idea how to address it --- this idea applies verbatim here. Chris, you certainly are able to provide a concrete example of a (twist of a) curve such that the resulting conductor is larger than 130000, in less than a minute? 

Cheers, gsw



---

archive/issue_comments_035090.json:
```json
{
    "body": "Hi Georg,\n\nwell, all I am saying is that someone ought to take a second look that nothing got broken that used to work before and that we do not notice because the doctest was \"corrected\". I am not claiming that this is the case, but I want to be 100% on this. I personally have no clue about padic l-functions and do not know who the experts are in the field, so I wanted to err on the side of caution by pinging John and William. I did mention this patch to William while he was sitting next to me yesterday and hopefully he will have time to look at this during the weekend - most likely sunday, but we will see what happens. It would be very nice to get this into 3.4.1 :)\n\nI will certainly doctest the two current patches and give feedback.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-26T23:11:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35090",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Georg,

well, all I am saying is that someone ought to take a second look that nothing got broken that used to work before and that we do not notice because the doctest was "corrected". I am not claiming that this is the case, but I want to be 100% on this. I personally have no clue about padic l-functions and do not know who the experts are in the field, so I wanted to err on the side of caution by pinging John and William. I did mention this patch to William while he was sitting next to me yesterday and hopefully he will have time to look at this during the weekend - most likely sunday, but we will see what happens. It would be very nice to get this into 3.4.1 :)

I will certainly doctest the two current patches and give feedback.

Cheers,

Michael



---

archive/issue_comments_035091.json:
```json
{
    "body": "FYI: if I apply trac_4667_z.patch and trac_4667_z2.patch to my 3.4.1.alpha0 merge tree all tests pass.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-26T23:33:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35091",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

FYI: if I apply trac_4667_z.patch and trac_4667_z2.patch to my 3.4.1.alpha0 merge tree all tests pass.

Cheers,

Michael



---

archive/issue_events_010690.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber",
    "created_at": "2009-03-31T18:11:02Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4667#event-10690"
}
```



---

archive/issue_events_010691.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber",
    "created_at": "2009-03-31T18:11:02Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4667#event-10691"
}
```



---

archive/issue_comments_035092.json:
```json
{
    "body": "Can't help it, this code does look good to me.\n\nTested against Sage-3.4.1.alpha0.",
    "created_at": "2009-03-31T18:11:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35092",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Can't help it, this code does look good to me.

Tested against Sage-3.4.1.alpha0.



---

archive/issue_comments_035093.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-31T21:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35093",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035094.json:
```json
{
    "body": "Merged  trac_4667_z.patch and trac_4667_z2.patch in Sage 3.4.1.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-31T21:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4667#issuecomment-35094",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged  trac_4667_z.patch and trac_4667_z2.patch in Sage 3.4.1.rc0.

Cheers,

Michael



---

archive/issue_events_010692.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-31T21:29:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4667",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4667#event-10692"
}
```
