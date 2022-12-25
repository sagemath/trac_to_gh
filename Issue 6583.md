# Issue 6583: Implement two descent over QQ natively in Sage using ratpoints

archive/issues_006583.json:
```json
{
    "body": "Assignee: @loefflerd\n\nCC:  @JohnCremona @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6583\n\n",
    "created_at": "2009-07-21T19:26:23Z",
    "labels": [
        "component: elliptic curves",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Implement two descent over QQ natively in Sage using ratpoints",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6583",
    "user": "https://github.com/rlmill"
}
```
Assignee: @loefflerd

CC:  @JohnCremona @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/6583





---

archive/issue_comments_053670.json:
```json
{
    "body": "Although the patch above isn't finished, I do consider it polished for what it does. The next steps are:\n\n1. plug into NTL for factoring over FF_p[X] for large p.\n\n2. incorporate the optimization based on linear algebra in QQ*/(QQ*)^2.\n\n3. do second descents in the case that the exact rank is not found.\n\n4. General two-descent -- I have a rudimentary version of this in a notebook worksheet, which will eventually wind up here.\n\nAlthough not in a completely finished state, comments are still welcome!",
    "created_at": "2009-07-21T19:44:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53670",
    "user": "https://github.com/rlmill"
}
```

Although the patch above isn't finished, I do consider it polished for what it does. The next steps are:

1. plug into NTL for factoring over FF_p[X] for large p.

2. incorporate the optimization based on linear algebra in QQ*/(QQ*)^2.

3. do second descents in the case that the exact rank is not found.

4. General two-descent -- I have a rudimentary version of this in a notebook worksheet, which will eventually wind up here.

Although not in a completely finished state, comments are still welcome!



---

archive/issue_comments_053671.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-09-17T20:34:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53671",
    "user": "https://github.com/rlmill"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_053672.json:
```json
{
    "body": "For my purposes (working within Cremona's big table, N<130000), the dimensions of the subspaces of Q*/(Q*)^2 I am considering are \n\n0: 242 cases\n1: 15019 cases\n2: 93479 cases\n3: 141373 cases\n4: 59005 cases\n5: 7339 cases\n6: 187 cases\n\nBased on this, I do not consider it a priority to do #2. The others are also not necessary for my purposes, so I'm doing some serious triage and getting this into a mergable state now. These other enhancements can come later.",
    "created_at": "2009-09-17T23:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53672",
    "user": "https://github.com/rlmill"
}
```

For my purposes (working within Cremona's big table, N<130000), the dimensions of the subspaces of Q*/(Q*)^2 I am considering are 

0: 242 cases
1: 15019 cases
2: 93479 cases
3: 141373 cases
4: 59005 cases
5: 7339 cases
6: 187 cases

Based on this, I do not consider it a priority to do #2. The others are also not necessary for my purposes, so I'm doing some serious triage and getting this into a mergable state now. These other enhancements can come later.



---

archive/issue_comments_053673.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-18T01:18:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53673",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to assigned.



---

archive/issue_comments_053674.json:
```json
{
    "body": "Changing assignee from @loefflerd to @rlmill.",
    "created_at": "2009-09-18T01:18:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53674",
    "user": "https://github.com/rlmill"
}
```

Changing assignee from @loefflerd to @rlmill.



---

archive/issue_comments_053675.json:
```json
{
    "body": "Attachment [trac_6583.patch](tarball://root/attachments/some-uuid/ticket6583/trac_6583.patch) by @rlmill created at 2009-09-18 01:18:43",
    "created_at": "2009-09-18T01:18:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53675",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_6583.patch](tarball://root/attachments/some-uuid/ticket6583/trac_6583.patch) by @rlmill created at 2009-09-18 01:18:43



---

archive/issue_comments_053676.json:
```json
{
    "body": "Attachment [trac_6583_large_primes.patch](tarball://root/attachments/some-uuid/ticket6583/trac_6583_large_primes.patch) by @rlmill created at 2009-09-19 03:09:46",
    "created_at": "2009-09-19T03:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53676",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_6583_large_primes.patch](tarball://root/attachments/some-uuid/ticket6583/trac_6583_large_primes.patch) by @rlmill created at 2009-09-19 03:09:46



---

archive/issue_comments_053677.json:
```json
{
    "body": "Applying the patch and doing \"sage -t\" yields some failures, probably because you assume the large cremona database is installed, but it isn't:\n\n```\nwstein@sage:~/build/sage-4.1.2.alpha1$ ./sage -t  devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx\nsage -t  \"devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx\"\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.1.2.alpha1/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx\", line 1093:\n    sage: E = EllipticCurve('59450i')\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_18[12]>\", line 1, in <module>\n        E = EllipticCurve('59450i')###line 1093:\n    sage: E = EllipticCurve('59450i')\n      File \"/scratch/wstein/build/sage-4.1.2.alpha1/local/lib/python/site-packages/sage/schemes/elliptic_curves/constructor.py\", line 216, in EllipticCurve\n        return ell_rational_field.EllipticCurve_rational_field(x)\n      File \"/scratch/wstein/build/sage-4.1.2.alpha1/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py\", line 191, in __init__\n        X = sage.databases.cremona.CremonaDatabase()[label]\n      File \"/scratch/wstein/build/sage-4.1.2.alpha1/local/lib/python/site-packages/sage/databases/cremona.py\", line 383, in __getitem__\n        return self.elliptic_curve(N)\n      File \"/scratch/wstein/build/sage-4.1.2.alpha1/local/lib/python/site-packages/sage/databases/cremona.py\", line 570, in elliptic_curve\n        raise RuntimeError, message\n    RuntimeError: There is no elliptic curve with label 59450i in the default database; try installing the optional package database_cremona_ellcurve-20071019 which contains all curves of conductor up to 130000\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.1.2.alpha1/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx\", line 1095:\n    sage: log(n1,2) + log(n1_prime,2) - 2 # the rank\nExpected:\n    3\nGot:\n    2\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.1.2.alpha1/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx\", line 56:\n    sage: from sage.schemes.elliptic_curves.descent import test_valuation as tv\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[2]>\", line 1, in <module>\n        from sage.schemes.elliptic_curves.descent import test_valuation as tv###line 56:\n    sage: from sage.schemes.elliptic_curves.descent import test_valuation as tv\n    ImportError: No module named descent\n**********************************************************************\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.1.2.alpha1/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx\", line 57: \n    sage: for i in [1..20]:\n       print '%10s'%factor(i), tv(i,Integer(2)), tv(i,Integer(3)), tv(i,Integer(5))\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[3]>\", line 2, in <module>\n        print '%10s'%factor(i), tv(i,Integer(2)), tv(i,Integer(3)), tv(i,Integer(5))\n    NameError: name 'tv' is not defined\n**********************************************************************\n2 items had failures:\n   2 of  24 in __main__.example_18\n   2 of   4 in __main__.example_2\n***Test Failed*** 4 failures.\nFor whitespace errors, see the file /scratch/wstein/build/sage-4.1.2.alpha1/tmp/.doctest_descent_two_isogeny.py\n         [3.4 s]\nexit code: 1024\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx\"\nTotal time for all tests: 3.4 seconds\nwstein@sage:~/build/sage-4.1.2.alpha1$ \n```",
    "created_at": "2009-09-22T14:43:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53677",
    "user": "https://github.com/williamstein"
}
```

Applying the patch and doing "sage -t" yields some failures, probably because you assume the large cremona database is installed, but it isn't:

```
wstein@sage:~/build/sage-4.1.2.alpha1$ ./sage -t  devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx
sage -t  "devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx"
**********************************************************************
File "/scratch/wstein/build/sage-4.1.2.alpha1/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx", line 1093:
    sage: E = EllipticCurve('59450i')
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_18[12]>", line 1, in <module>
        E = EllipticCurve('59450i')###line 1093:
    sage: E = EllipticCurve('59450i')
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/lib/python/site-packages/sage/schemes/elliptic_curves/constructor.py", line 216, in EllipticCurve
        return ell_rational_field.EllipticCurve_rational_field(x)
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 191, in __init__
        X = sage.databases.cremona.CremonaDatabase()[label]
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/lib/python/site-packages/sage/databases/cremona.py", line 383, in __getitem__
        return self.elliptic_curve(N)
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/lib/python/site-packages/sage/databases/cremona.py", line 570, in elliptic_curve
        raise RuntimeError, message
    RuntimeError: There is no elliptic curve with label 59450i in the default database; try installing the optional package database_cremona_ellcurve-20071019 which contains all curves of conductor up to 130000
**********************************************************************
File "/scratch/wstein/build/sage-4.1.2.alpha1/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx", line 1095:
    sage: log(n1,2) + log(n1_prime,2) - 2 # the rank
Expected:
    3
Got:
    2
**********************************************************************
File "/scratch/wstein/build/sage-4.1.2.alpha1/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx", line 56:
    sage: from sage.schemes.elliptic_curves.descent import test_valuation as tv
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[2]>", line 1, in <module>
        from sage.schemes.elliptic_curves.descent import test_valuation as tv###line 56:
    sage: from sage.schemes.elliptic_curves.descent import test_valuation as tv
    ImportError: No module named descent
**********************************************************************
**********************************************************************
File "/scratch/wstein/build/sage-4.1.2.alpha1/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx", line 57: 
    sage: for i in [1..20]:
       print '%10s'%factor(i), tv(i,Integer(2)), tv(i,Integer(3)), tv(i,Integer(5))
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[3]>", line 2, in <module>
        print '%10s'%factor(i), tv(i,Integer(2)), tv(i,Integer(3)), tv(i,Integer(5))
    NameError: name 'tv' is not defined
**********************************************************************
2 items had failures:
   2 of  24 in __main__.example_18
   2 of   4 in __main__.example_2
***Test Failed*** 4 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-4.1.2.alpha1/tmp/.doctest_descent_two_isogeny.py
         [3.4 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx"
Total time for all tests: 3.4 seconds
wstein@sage:~/build/sage-4.1.2.alpha1$ 
```



---

archive/issue_comments_053678.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-30T03:01:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53678",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_053679.json:
```json
{
    "body": "Attachment [trac_6583-fix.patch](tarball://root/attachments/some-uuid/ticket6583/trac_6583-fix.patch) by @rlmill created at 2009-10-30 03:01:22",
    "created_at": "2009-10-30T03:01:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53679",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_6583-fix.patch](tarball://root/attachments/some-uuid/ticket6583/trac_6583-fix.patch) by @rlmill created at 2009-10-30 03:01:22



---

archive/issue_comments_053680.json:
```json
{
    "body": "Ok. I tested the patches and they all go through. Also the -coverage gives 6 out of 6 despite the fact that many functions in descent_two_isogeny.pyx lack a good documentation and especially examples are missing often. I guess this is because cdefs are not tested. (I admit I never reviewed a cython file.)\n\nCurrently the main function gives back four integers, like mwrank does. They are useful to compute an upper bound on the rank of the Mordell-Weil group and should (in the future) be called from `rank()` and also from `sha()`.\n\nPersonnally I would like more, namely I would like to have a phi-Selmer group. Ideally we should give back a abelian group associated to the elliptic curve, or even better to the isogeny. But isogenies are not there yet, though 2-isogenies should be. The Selmer groups would contain more information than just these four integers and I believe this extra-information is already computed in this algorithm.\n\nRight now the functions are not callable without an extra import and so they do not pollute the name-space and we are still flexible in how to do this later; like `.selmer_group()` etc. That is very good. Yet it does not really look like a finished patch.\n\nIt is work in progress (and it is very good work in the right direction), but I am incapable of saying whether this sort of work should already be included in sage or not. So before giving a positive review to this patch, I would like to ask the author's and other's opinion on this. Maybe I could also ask for more examples, especially in the header of the file, despite the fact that it is not included in the documentation right now.\n\nChris.",
    "created_at": "2009-11-04T13:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53680",
    "user": "https://github.com/categorie"
}
```

Ok. I tested the patches and they all go through. Also the -coverage gives 6 out of 6 despite the fact that many functions in descent_two_isogeny.pyx lack a good documentation and especially examples are missing often. I guess this is because cdefs are not tested. (I admit I never reviewed a cython file.)

Currently the main function gives back four integers, like mwrank does. They are useful to compute an upper bound on the rank of the Mordell-Weil group and should (in the future) be called from `rank()` and also from `sha()`.

Personnally I would like more, namely I would like to have a phi-Selmer group. Ideally we should give back a abelian group associated to the elliptic curve, or even better to the isogeny. But isogenies are not there yet, though 2-isogenies should be. The Selmer groups would contain more information than just these four integers and I believe this extra-information is already computed in this algorithm.

Right now the functions are not callable without an extra import and so they do not pollute the name-space and we are still flexible in how to do this later; like `.selmer_group()` etc. That is very good. Yet it does not really look like a finished patch.

It is work in progress (and it is very good work in the right direction), but I am incapable of saying whether this sort of work should already be included in sage or not. So before giving a positive review to this patch, I would like to ask the author's and other's opinion on this. Maybe I could also ask for more examples, especially in the header of the file, despite the fact that it is not included in the documentation right now.

Chris.



---

archive/issue_comments_053681.json:
```json
{
    "body": "A couple of follow-up points to Chris, from an independent observer:  first, can we have some motivation, such as examples where this works better than calling mwrank?  There will certainly be curves for which the performance is worse (where mwrank would use a second descent).  I suspect that any enhanced perofrmance comes from the use of the more recent version of ratpoints than mwrank uses.\n\nSecondly, the isogeny patch I am finishing up will allow 2-isogenies (and more) to be easily constructed (which they almost can already).  A very interesting project would be to take any (cyclic) isogeny between elliptic curves, defined over QQ, and return an appropriate Selmer group.",
    "created_at": "2009-11-04T13:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53681",
    "user": "https://github.com/JohnCremona"
}
```

A couple of follow-up points to Chris, from an independent observer:  first, can we have some motivation, such as examples where this works better than calling mwrank?  There will certainly be curves for which the performance is worse (where mwrank would use a second descent).  I suspect that any enhanced perofrmance comes from the use of the more recent version of ratpoints than mwrank uses.

Secondly, the isogeny patch I am finishing up will allow 2-isogenies (and more) to be easily constructed (which they almost can already).  A very interesting project would be to take any (cyclic) isogeny between elliptic curves, defined over QQ, and return an appropriate Selmer group.



---

archive/issue_comments_053682.json:
```json
{
    "body": "Here's an example where mwrank does not do a second descent, where the runtime is approximately 90 times faster:\n\n```\nsage: E = EllipticCurve('676a1')\nsage: from sage.schemes.elliptic_curves.descent_two_isogeny import two_descent_by_two_isogeny\nsage: timeit('two_descent_by_two_isogeny(E)')\n125 loops, best of 3: 2.83 ms per loop\nsage: A = E.mwrank_curve()\nsage: timeit('A.two_descent(verbose=False)')\n5 loops, best of 3: 252 ms per loop\n```\n\nI ran the following to compare times in general:\n\n```\nsage: for E in cremona_optimal_curves(range(200)):\n...    if E.torsion_order()%2 == 0:\n...        t = walltime()\n...        E.mwrank_curve().two_descent(verbose=False, second_descent=False)\n...        t = walltime(t)\n...        s = walltime()\n...        _ = two_descent_by_two_isogeny(E)\n...        s = walltime(s)\n```\n\nmwrank is always slower by a factor of at least 5, almost always slower by a factor of at least 20, and frequently slower by factors of up to 150.",
    "created_at": "2009-12-01T18:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53682",
    "user": "https://github.com/rlmill"
}
```

Here's an example where mwrank does not do a second descent, where the runtime is approximately 90 times faster:

```
sage: E = EllipticCurve('676a1')
sage: from sage.schemes.elliptic_curves.descent_two_isogeny import two_descent_by_two_isogeny
sage: timeit('two_descent_by_two_isogeny(E)')
125 loops, best of 3: 2.83 ms per loop
sage: A = E.mwrank_curve()
sage: timeit('A.two_descent(verbose=False)')
5 loops, best of 3: 252 ms per loop
```

I ran the following to compare times in general:

```
sage: for E in cremona_optimal_curves(range(200)):
...    if E.torsion_order()%2 == 0:
...        t = walltime()
...        E.mwrank_curve().two_descent(verbose=False, second_descent=False)
...        t = walltime(t)
...        s = walltime()
...        _ = two_descent_by_two_isogeny(E)
...        s = walltime(s)
```

mwrank is always slower by a factor of at least 5, almost always slower by a factor of at least 20, and frequently slower by factors of up to 150.



---

archive/issue_comments_053683.json:
```json
{
    "body": "Maybe this is a more accurate comparison:\n\n```\nsage: L = []\nsage: for E in cremona_optimal_curves(range(200)):\n    if E.torsion_order()%2 == 0:\n        A = E.mwrank_curve(); t = walltime()\n        A.two_descent(verbose=False, second_descent=False)\n        t = walltime(t)\n        s = walltime()\n        _ = two_descent_by_two_isogeny(E)\n        s = walltime(s)\n        if s > t: print E.label()\n        else:\n            L.append(t/s)\n....:             \nsage: sum(L)/len(L)\n28.023321958157503\n```\n\nThus the average speedup is 28x.",
    "created_at": "2009-12-01T19:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53683",
    "user": "https://github.com/rlmill"
}
```

Maybe this is a more accurate comparison:

```
sage: L = []
sage: for E in cremona_optimal_curves(range(200)):
    if E.torsion_order()%2 == 0:
        A = E.mwrank_curve(); t = walltime()
        A.two_descent(verbose=False, second_descent=False)
        t = walltime(t)
        s = walltime()
        _ = two_descent_by_two_isogeny(E)
        s = walltime(s)
        if s > t: print E.label()
        else:
            L.append(t/s)
....:             
sage: sum(L)/len(L)
28.023321958157503
```

Thus the average speedup is 28x.



---

archive/issue_comments_053684.json:
```json
{
    "body": "For the curious, standard deviation:\n\n```\nsage: sqrt(sum([(l - 28.0233)^2 for l in L])/len(L))\n10.6330410085500\n```",
    "created_at": "2009-12-01T19:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53684",
    "user": "https://github.com/rlmill"
}
```

For the curious, standard deviation:

```
sage: sqrt(sum([(l - 28.0233)^2 for l in L])/len(L))
10.6330410085500
```



---

archive/issue_comments_053685.json:
```json
{
    "body": "Robert -- I am quite prepared to believe that your code is fast, but all these tests on the curves of conductor up to 200 are not exactly typical!  I seem to remember that there is one curve in that range which mwrank used to take longer on than all the others put together, for example.",
    "created_at": "2009-12-01T20:08:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53685",
    "user": "https://github.com/JohnCremona"
}
```

Robert -- I am quite prepared to believe that your code is fast, but all these tests on the curves of conductor up to 200 are not exactly typical!  I seem to remember that there is one curve in that range which mwrank used to take longer on than all the others put together, for example.



---

archive/issue_comments_053686.json:
```json
{
    "body": "I was just trying to address your question whether there were examples where this was better than mwrank. Your second comment, \"any enhanced performance comes from the use of the more recent version of ratpoints\" is very false: if I remove the use of ratpoints altogether, the speedup factors increase!\n\n```\nsage: L = []\nsage: for E in cremona_optimal_curves(range(200)):\n    if E.torsion_order()%2 == 0:\n        A = E.mwrank_curve()\n        t = walltime()\n        A.two_descent(verbose=False, selmer_only=True, second_descent=False)\n        t = walltime(t)\n        s = walltime()\n        _ = two_descent_by_two_isogeny(E, selmer_only=True)\n        s = walltime(s)\n        if s > t: print E.label()\n        else:\n            L.append(t/s)\n....:             \nsage: sum(L)/len(L)\n147.24136054804828\n```\n\nThus I argue that this code is definitely worth including, especially since this exact code was the main motivation for including ratpoints in Sage in the first place. I don't know what \"typical\" means regarding the conductor bound, especially since I'm primarily interested in curves with small conductor. I spent a long time optimizing this code, and I'd rather not see that work getting lost to the four winds.\n\n(John-- Maybe I'm just missing your point?)",
    "created_at": "2009-12-01T21:34:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53686",
    "user": "https://github.com/rlmill"
}
```

I was just trying to address your question whether there were examples where this was better than mwrank. Your second comment, "any enhanced performance comes from the use of the more recent version of ratpoints" is very false: if I remove the use of ratpoints altogether, the speedup factors increase!

```
sage: L = []
sage: for E in cremona_optimal_curves(range(200)):
    if E.torsion_order()%2 == 0:
        A = E.mwrank_curve()
        t = walltime()
        A.two_descent(verbose=False, selmer_only=True, second_descent=False)
        t = walltime(t)
        s = walltime()
        _ = two_descent_by_two_isogeny(E, selmer_only=True)
        s = walltime(s)
        if s > t: print E.label()
        else:
            L.append(t/s)
....:             
sage: sum(L)/len(L)
147.24136054804828
```

Thus I argue that this code is definitely worth including, especially since this exact code was the main motivation for including ratpoints in Sage in the first place. I don't know what "typical" means regarding the conductor bound, especially since I'm primarily interested in curves with small conductor. I spent a long time optimizing this code, and I'd rather not see that work getting lost to the four winds.

(John-- Maybe I'm just missing your point?)



---

archive/issue_comments_053687.json:
```json
{
    "body": "Sorry, I did not mean to sound so critical.  Of course this should be included.  I have not had time to look at it in detail (though I feel that people expect me to, and give an expert opinion).  I think it would be good to have native 2-descent code in Sage (another extremely useful project would be to rewrite Simon's gp program over number fields in Sage), not least because the current interface is not very good (hard to use non-standard parameter settings, for example) and uses the ancient ratpoints, all because I have not had the time to improve those things.\n\nExperience tells me that if you put in code which was designed for curves with small conductor then you will very soon find that people try to run the same code on huge examples.  This is precisely what happened to me -- the first version of what later became mwrank was written solely for the purpose of computing the ranks of the curves in my book, i.e. N<1000.  So the new code must be tested on large examples too.",
    "created_at": "2009-12-02T15:43:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53687",
    "user": "https://github.com/JohnCremona"
}
```

Sorry, I did not mean to sound so critical.  Of course this should be included.  I have not had time to look at it in detail (though I feel that people expect me to, and give an expert opinion).  I think it would be good to have native 2-descent code in Sage (another extremely useful project would be to rewrite Simon's gp program over number fields in Sage), not least because the current interface is not very good (hard to use non-standard parameter settings, for example) and uses the ancient ratpoints, all because I have not had the time to improve those things.

Experience tells me that if you put in code which was designed for curves with small conductor then you will very soon find that people try to run the same code on huge examples.  This is precisely what happened to me -- the first version of what later became mwrank was written solely for the purpose of computing the ranks of the curves in my book, i.e. N<1000.  So the new code must be tested on large examples too.



---

archive/issue_comments_053688.json:
```json
{
    "body": "I've tried the same benchmarks on curves in the conductor range 129800 to 130000. There the average speedup is 117x. Once I have the Stein-Watkins database downloaded, I can try running some examples from there.\n\nI'd like to attempt to summarize the referee comments so far:\n\n- more documentation\n- more examples\n- output the Selmer group explicitly\n- eventually we need to implement second descents",
    "created_at": "2009-12-02T20:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53688",
    "user": "https://github.com/rlmill"
}
```

I've tried the same benchmarks on curves in the conductor range 129800 to 130000. There the average speedup is 117x. Once I have the Stein-Watkins database downloaded, I can try running some examples from there.

I'd like to attempt to summarize the referee comments so far:

- more documentation
- more examples
- output the Selmer group explicitly
- eventually we need to implement second descents



---

archive/issue_comments_053689.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-09T00:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53689",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053690.json:
```json
{
    "body": "REPORT:\n\n1. I can't apply the patch to 4.3.alpha1:\n\n```\npatching file sage/libs/flint/zmod_poly.pxd\nHunk #2 FAILED at 249\n1 out of 2 hunks FAILED -- saving rejects to file sage/libs/flint/zmod_poly.pxd.rej\nabort: patch failed to apply\n```\n\nThe rebase is trivial, and I've posted it.\n\n---\n\n2. The main concern in Chris's report is just that this code doesn't yet do enough.  However, rlm isn't just writing this as some one-off thing for a little project.  He's doing his Ph.D. thesis mostly on descent (and its applications), and this is what he'll be working on fulltime, probably for the next year (for his thesis, then his postdoc).  So I think getting this in now makes *perfect* sense, instead of waiting until we get a big patch bomb later. \n\n3. All those cdef'd methods with no doctests and minimal documentation isn't good, just as Chris says.  You could open another ticket and fix that, since it will make it way easier for others to work on (and use in surprising ways!) this code if those functions are documented and tested.  For each cdef'd method, just make a corresponding def'd method called \"test_...\" that calls the cdef'd method, then put the tests there.   You already do just that in *some* cases, e.g., `def test_els(a,b,c,d,e):`. \n\n4. Docstrings like this would be more readable if they used latex:\n\n```\nGiven an elliptic curve E with a two-isogeny phi : E --> E' and dual isogeny \n \t799\t    phi', runs a two-isogeny descent on E, returning n1, n2, n1' and n2'. Here \n \t800\t    n1 is the number of quartic covers found with a rational point, and n2 is \n \t801\t    the number which are ELS. \n```\n\n5. All tests pass with this code applied to sage-4.3.alpha1.\n\nIn summary:\n\nI've applied the patches, skimmed them, and run the test suite.  Positive review.",
    "created_at": "2009-12-09T00:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53690",
    "user": "https://github.com/williamstein"
}
```

REPORT:

1. I can't apply the patch to 4.3.alpha1:

```
patching file sage/libs/flint/zmod_poly.pxd
Hunk #2 FAILED at 249
1 out of 2 hunks FAILED -- saving rejects to file sage/libs/flint/zmod_poly.pxd.rej
abort: patch failed to apply
```

The rebase is trivial, and I've posted it.

---

2. The main concern in Chris's report is just that this code doesn't yet do enough.  However, rlm isn't just writing this as some one-off thing for a little project.  He's doing his Ph.D. thesis mostly on descent (and its applications), and this is what he'll be working on fulltime, probably for the next year (for his thesis, then his postdoc).  So I think getting this in now makes *perfect* sense, instead of waiting until we get a big patch bomb later. 

3. All those cdef'd methods with no doctests and minimal documentation isn't good, just as Chris says.  You could open another ticket and fix that, since it will make it way easier for others to work on (and use in surprising ways!) this code if those functions are documented and tested.  For each cdef'd method, just make a corresponding def'd method called "test_..." that calls the cdef'd method, then put the tests there.   You already do just that in *some* cases, e.g., `def test_els(a,b,c,d,e):`. 

4. Docstrings like this would be more readable if they used latex:

```
Given an elliptic curve E with a two-isogeny phi : E --> E' and dual isogeny 
 	799	    phi', runs a two-isogeny descent on E, returning n1, n2, n1' and n2'. Here 
 	800	    n1 is the number of quartic covers found with a rational point, and n2 is 
 	801	    the number which are ELS. 
```

5. All tests pass with this code applied to sage-4.3.alpha1.

In summary:

I've applied the patches, skimmed them, and run the test suite.  Positive review.



---

archive/issue_comments_053691.json:
```json
{
    "body": "Attachment [trac_6583-rebase.patch](tarball://root/attachments/some-uuid/ticket6583/trac_6583-rebase.patch) by @williamstein created at 2009-12-09 00:55:51",
    "created_at": "2009-12-09T00:55:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53691",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_6583-rebase.patch](tarball://root/attachments/some-uuid/ticket6583/trac_6583-rebase.patch) by @williamstein created at 2009-12-09 00:55:51



---

archive/issue_comments_053692.json:
```json
{
    "body": "I am very happy to endorse this decision.  When I looked at this some time ago I think I found some extra functionality with the ratpoints package which should be, but is not yet, exposed, and started to work on that, but got diverted into other things.  Never mind:  we can always build on this and extra things if and when we want to.  Good, job, Robert!",
    "created_at": "2009-12-09T16:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53692",
    "user": "https://github.com/JohnCremona"
}
```

I am very happy to endorse this decision.  When I looked at this some time ago I think I found some extra functionality with the ratpoints package which should be, but is not yet, exposed, and started to work on that, but got diverted into other things.  Never mind:  we can always build on this and extra things if and when we want to.  Good, job, Robert!



---

archive/issue_events_015525.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-01-04T04:02:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6583#event-15525"
}
```



---

archive/issue_comments_053693.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-04T04:02:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53693",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_053694.json:
```json
{
    "body": "Could you please take a look at #7867 which is a ticket indicating a problem building Sage on 't2' which could possibly be related to this.",
    "created_at": "2010-01-07T07:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53694",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Could you please take a look at #7867 which is a ticket indicating a problem building Sage on 't2' which could possibly be related to this.



---

archive/issue_comments_053695.json:
```json
{
    "body": "For the record, this is definitely the code which has broken the Solaris build. \n\nMinh has proven this: \n\nhttp://groups.google.com/group/sage-devel/msg/bb1da5365b7f1c90\n\n\nDave",
    "created_at": "2010-02-22T14:14:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6583#issuecomment-53695",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

For the record, this is definitely the code which has broken the Solaris build. 

Minh has proven this: 

http://groups.google.com/group/sage-devel/msg/bb1da5365b7f1c90


Dave
