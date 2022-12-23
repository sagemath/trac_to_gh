# Issue 5982: Can't construct fraction field

archive/issues_005982.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  malb\n\n----------------------------------------------------------------------\nthe GUI, and license() for information.  |\n----------------------------------------------------------------------\n| Sage Version 3.4, Release Date: 2009-03-11 | | Type notebook() for\nsage: R.<x, y> = PolynomialRing(QQ, 2) sage: I = (x^2 + y^2 - 1)*R\nsage: Q = R.quotient(I) sage: Q Quotient of Multivariate Polynomial\nRing in x, y over Rational Field by the ideal (x^2 + y^2 - 1) sage:\nQ.fraction_field()\n---------------------------------------------------------------------------\nNotImplementedError Traceback (most recent call last)\n\n...\n\nIssue created by migration from https://trac.sagemath.org/ticket/5982\n\n",
    "created_at": "2009-05-04T23:19:45Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "Can't construct fraction field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5982",
    "user": "jmbr"
}
```
Assignee: tbd

CC:  malb

----------------------------------------------------------------------
the GUI, and license() for information.  |
----------------------------------------------------------------------
| Sage Version 3.4, Release Date: 2009-03-11 | | Type notebook() for
sage: R.<x, y> = PolynomialRing(QQ, 2) sage: I = (x^2 + y^2 - 1)*R
sage: Q = R.quotient(I) sage: Q Quotient of Multivariate Polynomial
Ring in x, y over Rational Field by the ideal (x^2 + y^2 - 1) sage:
Q.fraction_field()
---------------------------------------------------------------------------
NotImplementedError Traceback (most recent call last)

...

Issue created by migration from https://trac.sagemath.org/ticket/5982





---

archive/issue_comments_047501.json:
```json
{
    "body": "Attachment\n\nFix/workaround using Macaulay 2",
    "created_at": "2009-05-04T23:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47501",
    "user": "jmbr"
}
```

Attachment

Fix/workaround using Macaulay 2



---

archive/issue_comments_047502.json:
```json
{
    "body": "[with patch, needs review]\n\n\n```\n----------------------------------------------------------------------\nthe GUI, and license() for information.  |\n----------------------------------------------------------------------\n| Sage Version 3.4, Release Date: 2009-03-11 | | Type notebook() for\nsage: R.<x, y> = PolynomialRing(QQ, 2) sage: I = (x^2 + y^2 - 1)*R\nsage: Q = R.quotient(I) sage: Q Quotient of Multivariate Polynomial\nRing in x, y over Rational Field by the ideal (x^2 + y^2 - 1) sage:\nQ.fraction_field()\n---------------------------------------------------------------------------\nNotImplementedError Traceback (most recent call last)\n\n...\n```\n",
    "created_at": "2009-05-04T23:23:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47502",
    "user": "jmbr"
}
```

[with patch, needs review]


```
----------------------------------------------------------------------
the GUI, and license() for information.  |
----------------------------------------------------------------------
| Sage Version 3.4, Release Date: 2009-03-11 | | Type notebook() for
sage: R.<x, y> = PolynomialRing(QQ, 2) sage: I = (x^2 + y^2 - 1)*R
sage: Q = R.quotient(I) sage: Q Quotient of Multivariate Polynomial
Ring in x, y over Rational Field by the ideal (x^2 + y^2 - 1) sage:
Q.fraction_field()
---------------------------------------------------------------------------
NotImplementedError Traceback (most recent call last)

...
```




---

archive/issue_comments_047503.json:
```json
{
    "body": "Hi,\n\nM2 isn't a default part of Sage, so the doctest must be made optional. I also don't see a reason why this cannot be implemented via libSingular for example, but maybe I am overlooking things.\n\nYou also posted a diff, so please check in the code and post an hg patch to properly preserve credit. \n\nAnd since you are not listed at http://trac.sagemath.org/sage_trac/wiki please add yourself there.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-05T01:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47503",
    "user": "mabshoff"
}
```

Hi,

M2 isn't a default part of Sage, so the doctest must be made optional. I also don't see a reason why this cannot be implemented via libSingular for example, but maybe I am overlooking things.

You also posted a diff, so please check in the code and post an hg patch to properly preserve credit. 

And since you are not listed at http://trac.sagemath.org/sage_trac/wiki please add yourself there.

Cheers,

Michael



---

archive/issue_comments_047504.json:
```json
{
    "body": "Hi Michael,\n\nAttached is a Mercurial bundle with the same patch plus the docstring modifications you requested.  I'd like to write a native Sage implementation of this in the future but for now this works well enough for me.\n\nRegards,",
    "created_at": "2009-05-06T16:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47504",
    "user": "jmbr"
}
```

Hi Michael,

Attached is a Mercurial bundle with the same patch plus the docstring modifications you requested.  I'd like to write a native Sage implementation of this in the future but for now this works well enough for me.

Regards,



---

archive/issue_comments_047505.json:
```json
{
    "body": "Hi Juan,\n\na patch would have been better, but someone can extra the changeset from the bundle and post the patch.\n\nOne more thing: When you post an updated patch you need to change the summary to read \"needs review\" again.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-06T21:47:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47505",
    "user": "mabshoff"
}
```

Hi Juan,

a patch would have been better, but someone can extra the changeset from the bundle and post the patch.

One more thing: When you post an updated patch you need to change the summary to read "needs review" again.

Cheers,

Michael



---

archive/issue_comments_047506.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-06-19T22:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47506",
    "user": "ncalexan"
}
```

Attachment



---

archive/issue_comments_047507.json:
```json
{
    "body": "`trac_5982-ncalexan.patch` replaces all others.  This version doesn't use Macaulay2, but it could be really slow.",
    "created_at": "2009-06-19T22:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47507",
    "user": "ncalexan"
}
```

`trac_5982-ncalexan.patch` replaces all others.  This version doesn't use Macaulay2, but it could be really slow.



---

archive/issue_comments_047508.json:
```json
{
    "body": "Would it be reasonable to have both versions of `is_prime` added, with a flag for which to use (defaulting to `native`, but with `M2` an option)? This way, if there were cases that one cared about but were slow, one could call off to M2 and (hopefully) get an answer back faster ...",
    "created_at": "2009-06-20T21:43:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47508",
    "user": "craigcitro"
}
```

Would it be reasonable to have both versions of `is_prime` added, with a flag for which to use (defaulting to `native`, but with `M2` an option)? This way, if there were cases that one cared about but were slow, one could call off to M2 and (hopefully) get an answer back faster ...



---

archive/issue_comments_047509.json:
```json
{
    "body": "I thought about doing exactly that, but if you're clever enough to know one is better than the other, aren't you clever enough to call `_macaulay2_().isPrime()`?  Also, as far as I can tell, the Macaulay2 algorithm is the same as the Singular.",
    "created_at": "2009-06-21T08:17:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47509",
    "user": "ncalexan"
}
```

I thought about doing exactly that, but if you're clever enough to know one is better than the other, aren't you clever enough to call `_macaulay2_().isPrime()`?  Also, as far as I can tell, the Macaulay2 algorithm is the same as the Singular.



---

archive/issue_comments_047510.json:
```json
{
    "body": "Hi Nick,\n\nCould you point me to the location of Singular's ideal primality testing algorithm?  Thanks",
    "created_at": "2009-06-21T10:20:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47510",
    "user": "jmbr"
}
```

Hi Nick,

Could you point me to the location of Singular's ideal primality testing algorithm?  Thanks



---

archive/issue_comments_047511.json:
```json
{
    "body": "Replying to [comment:11 jmbr]:\n> Hi Nick,\n> \n> Could you point me to the location of Singular's ideal primality testing algorithm?  Thanks\n\nAFAICT, Singular does not have a toplevel isprime() (or ismaximal()) function.  Reading some mailing list posts regarding Singular and Macaulay2, I believe both implement the same two algorithms for calculating the complete primary decomposition of an ideal.  I don't understand enough to say definitively and I may be misusing the complete primary decomposition for testing primality.  I was hoping that Martin Albrecht would review and clarify the situation.",
    "created_at": "2009-06-21T18:39:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47511",
    "user": "ncalexan"
}
```

Replying to [comment:11 jmbr]:
> Hi Nick,
> 
> Could you point me to the location of Singular's ideal primality testing algorithm?  Thanks

AFAICT, Singular does not have a toplevel isprime() (or ismaximal()) function.  Reading some mailing list posts regarding Singular and Macaulay2, I believe both implement the same two algorithms for calculating the complete primary decomposition of an ideal.  I don't understand enough to say definitively and I may be misusing the complete primary decomposition for testing primality.  I was hoping that Martin Albrecht would review and clarify the situation.



---

archive/issue_comments_047512.json:
```json
{
    "body": "The patch looks good to me, I didn't run doctests though. I can't really clarify the situation any more than what Nick wrote above.",
    "created_at": "2009-06-21T20:36:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47512",
    "user": "malb"
}
```

The patch looks good to me, I didn't run doctests though. I can't really clarify the situation any more than what Nick wrote above.



---

archive/issue_comments_047513.json:
```json
{
    "body": "As far as I can recall, Macaulay2 implements the Gianni-Trager-Zacharias algorithm for primality testing instead of relying on primary decomposition.\n\nBest regards",
    "created_at": "2009-06-21T20:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47513",
    "user": "jmbr"
}
```

As far as I can recall, Macaulay2 implements the Gianni-Trager-Zacharias algorithm for primality testing instead of relying on primary decomposition.

Best regards



---

archive/issue_comments_047514.json:
```json
{
    "body": "Positive review modulo fixing this one trivial change to a doctest:\n\n```\nwstein@sage:~/build/sage-4.1$ ./sage -t  devel/sage/sage/rings/quotient_ring.py\nsage -t  \"devel/sage/sage/rings/quotient_ring.py\"           \n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.1/devel/sage/sage/rings/quotient_ring.py\", line 442:\n    sage: Q.is_integral_domain()\nExpected:\n    Traceback (most recent call last):\n    ...\n    NotImplementedError\nGot:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_13[7]>\", line 1, in <module>\n        Q.is_integral_domain()###line 442:\n    sage: Q.is_integral_domain()\n      File \"/scratch/wstein/build/sage-4.1/local/lib/python/site-packages/sage/rings/quotient_ring.py\", line 447, in is_integral_domain\n        return self.defining_ideal().is_prime()\n      File \"/scratch/wstein/build/sage-4.1/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 854, in is_prime\n        CPD = self.complete_primary_decomposition(**kwds)\n      File \"/scratch/wstein/build/sage-4.1/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 401, in __call__\n        raise ValueError(\"Coefficient ring must be a field for function '%s'.\"%(self.f.__name__))\n    ValueError: Coefficient ring must be a field for function 'complete_primary_decomposition'.\n**********************************************************************\n1 items had failures:\n   1 of   8 in __main__.example_13\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/wstein/build/sage-4.1/tmp/.doctest_quotient_ring.py\n         [1.8 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/sage/rings/quotient_ring.py\"\nTotal time for all tests: 1.8 seconds\nwstein@sage:~/build/sage-4.1$ \n```\n",
    "created_at": "2009-07-21T04:51:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47514",
    "user": "was"
}
```

Positive review modulo fixing this one trivial change to a doctest:

```
wstein@sage:~/build/sage-4.1$ ./sage -t  devel/sage/sage/rings/quotient_ring.py
sage -t  "devel/sage/sage/rings/quotient_ring.py"           
**********************************************************************
File "/scratch/wstein/build/sage-4.1/devel/sage/sage/rings/quotient_ring.py", line 442:
    sage: Q.is_integral_domain()
Expected:
    Traceback (most recent call last):
    ...
    NotImplementedError
Got:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_13[7]>", line 1, in <module>
        Q.is_integral_domain()###line 442:
    sage: Q.is_integral_domain()
      File "/scratch/wstein/build/sage-4.1/local/lib/python/site-packages/sage/rings/quotient_ring.py", line 447, in is_integral_domain
        return self.defining_ideal().is_prime()
      File "/scratch/wstein/build/sage-4.1/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 854, in is_prime
        CPD = self.complete_primary_decomposition(**kwds)
      File "/scratch/wstein/build/sage-4.1/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 401, in __call__
        raise ValueError("Coefficient ring must be a field for function '%s'."%(self.f.__name__))
    ValueError: Coefficient ring must be a field for function 'complete_primary_decomposition'.
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_13
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-4.1/tmp/.doctest_quotient_ring.py
         [1.8 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/rings/quotient_ring.py"
Total time for all tests: 1.8 seconds
wstein@sage:~/build/sage-4.1$ 
```




---

archive/issue_comments_047515.json:
```json
{
    "body": "Attachment\n\nMinh (or whoever merges this),\n\nApply *only* trac_5982-ncalexan-with-check.patch.  Note that you'll have to check it in as Nick Alexander and \"Juan M. Bello Rivas <jmbr`@`superadditive.com>\" when applying the patch, since Juan didn't use HG evidently.",
    "created_at": "2009-07-26T21:51:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47515",
    "user": "was"
}
```

Attachment

Minh (or whoever merges this),

Apply *only* trac_5982-ncalexan-with-check.patch.  Note that you'll have to check it in as Nick Alexander and "Juan M. Bello Rivas <jmbr`@`superadditive.com>" when applying the patch, since Juan didn't use HG evidently.



---

archive/issue_comments_047516.json:
```json
{
    "body": "Attachment\n\nreviewer patch: fix ReST typos",
    "created_at": "2009-08-23T10:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47516",
    "user": "mvngu"
}
```

Attachment

reviewer patch: fix ReST typos



---

archive/issue_comments_047517.json:
```json
{
    "body": "The reviewer patch `trac_5982-reviewer.patch` fixes some ReST typos in `trac_5982-ncalexan-with-check.patch` so that the reference manual builds without warnings. After applying patches in this order:\n\n1. `trac_5982-ncalexan-with-check.patch`\n2. `trac_5982-reviewer.patch`\n \nI get the following doctest failure:\n\n```\nsage -t -long devel/sage-main/sage/schemes/hyperelliptic_curves/jacobian_morphism.py\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/schemes/hyperelliptic_curves/jacobian_morphism.py\", line 297:\n    sage: J = H.jacobian()(F); J\nExpected:\n    verbose 0 (919: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.\n    Set of points of Jacobian of Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1 defined over Finite Field of size 1000000000000000000000000000057\nGot:\n    verbose 0 (964: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.\n    Set of points of Jacobian of Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1 defined over Finite Field of size 1000000000000000000000000000057\n**********************************************************************\n1 items had failures:\n   1 of  20 in __main__.example_4\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_jacobian_morphism.py\n\t [3.1 s]\n```\n",
    "created_at": "2009-08-23T11:12:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47517",
    "user": "mvngu"
}
```

The reviewer patch `trac_5982-reviewer.patch` fixes some ReST typos in `trac_5982-ncalexan-with-check.patch` so that the reference manual builds without warnings. After applying patches in this order:

1. `trac_5982-ncalexan-with-check.patch`
2. `trac_5982-reviewer.patch`
 
I get the following doctest failure:

```
sage -t -long devel/sage-main/sage/schemes/hyperelliptic_curves/jacobian_morphism.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/schemes/hyperelliptic_curves/jacobian_morphism.py", line 297:
    sage: J = H.jacobian()(F); J
Expected:
    verbose 0 (919: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.
    Set of points of Jacobian of Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1 defined over Finite Field of size 1000000000000000000000000000057
Got:
    verbose 0 (964: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.
    Set of points of Jacobian of Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1 defined over Finite Field of size 1000000000000000000000000000057
**********************************************************************
1 items had failures:
   1 of  20 in __main__.example_4
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_jacobian_morphism.py
	 [3.1 s]
```




---

archive/issue_comments_047518.json:
```json
{
    "body": "It looks like the difference is just the line number of the doctest...",
    "created_at": "2009-09-29T07:42:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47518",
    "user": "jason"
}
```

It looks like the difference is just the line number of the doctest...



---

archive/issue_comments_047519.json:
```json
{
    "body": "All tests pass for me when I tried the two patches.  I'm giving this a positive review again.  The doctest in question has \"...\" where the 919/964 are.",
    "created_at": "2009-10-05T19:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47519",
    "user": "mhansen"
}
```

All tests pass for me when I tried the two patches.  I'm giving this a positive review again.  The doctest in question has "..." where the 919/964 are.



---

archive/issue_comments_047520.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-10-16T08:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47520",
    "user": "mhansen"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_047521.json:
```json
{
    "body": "In 4.1.2, I get a number of failures arising from NotImplementedErrors in is_integral_domain.",
    "created_at": "2009-10-16T08:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47521",
    "user": "mhansen"
}
```

In 4.1.2, I get a number of failures arising from NotImplementedErrors in is_integral_domain.



---

archive/issue_comments_047522.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-23T18:36:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47522",
    "user": "davidloeffler"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_047523.json:
```json
{
    "body": "Curiously, all tests in sage/rings and sage/schemes pass for me under sage 4.6.2.alpha1. I'm going to reinstate the \"needs review\", since I can't replicate mhansen's problem. We'll see if patchbot agrees :-)\n\nApply trac_5982-ncalexan-with-check.patch, trac_5982-reviewer.patch",
    "created_at": "2011-01-23T18:36:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47523",
    "user": "davidloeffler"
}
```

Curiously, all tests in sage/rings and sage/schemes pass for me under sage 4.6.2.alpha1. I'm going to reinstate the "needs review", since I can't replicate mhansen's problem. We'll see if patchbot agrees :-)

Apply trac_5982-ncalexan-with-check.patch, trac_5982-reviewer.patch



---

archive/issue_comments_047524.json:
```json
{
    "body": "Patchbot seems to be happy with it, but a full ptestlong run on my 4.6.2.alpha1 build revealed a couple of failures: `sage/algebras/quatalg/quaternion_algebra.py` and `sage/matrix/tests.py`. Both of these are to do with the symbolic ring, which (rather oddly) knows it's a field but isn't sure if it's an integral domain. These can be squashed by simply moving the field check to before the integral domain check.",
    "created_at": "2011-01-23T19:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47524",
    "user": "davidloeffler"
}
```

Patchbot seems to be happy with it, but a full ptestlong run on my 4.6.2.alpha1 build revealed a couple of failures: `sage/algebras/quatalg/quaternion_algebra.py` and `sage/matrix/tests.py`. Both of these are to do with the symbolic ring, which (rather oddly) knows it's a field but isn't sure if it's an integral domain. These can be squashed by simply moving the field check to before the integral domain check.



---

archive/issue_comments_047525.json:
```json
{
    "body": "Attachment\n\nWhy is this\n\n```\n        The following is Trac #5982.  Note that the quotient ring \n        is not recognized as being a field at this time, so the \n        fraction field is not the quotient ring itself:: \n \n            sage: Q = R.quotient(I); Q \n            Quotient of Multivariate Polynomial Ring in x, y over Rational Field by the ideal (x^2 - y^2 - 1) \n            sage: Q.fraction_field() \n            Fraction Field of Quotient of Multivariate Polynomial Ring in x, y over Rational Field by the ideal (x^2 - y^2 - 1) \n```\n\npart of the documentation of `is_prime` and not of `fraction_field`?\n\nAll tests pass with these patches on sage-4.6.2.alpha4. Patches fix the problem in the ticket description, and all changes look good.",
    "created_at": "2011-02-14T09:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47525",
    "user": "mstreng"
}
```

Attachment

Why is this

```
        The following is Trac #5982.  Note that the quotient ring 
        is not recognized as being a field at this time, so the 
        fraction field is not the quotient ring itself:: 
 
            sage: Q = R.quotient(I); Q 
            Quotient of Multivariate Polynomial Ring in x, y over Rational Field by the ideal (x^2 - y^2 - 1) 
            sage: Q.fraction_field() 
            Fraction Field of Quotient of Multivariate Polynomial Ring in x, y over Rational Field by the ideal (x^2 - y^2 - 1) 
```

part of the documentation of `is_prime` and not of `fraction_field`?

All tests pass with these patches on sage-4.6.2.alpha4. Patches fix the problem in the ticket description, and all changes look good.



---

archive/issue_comments_047526.json:
```json
{
    "body": "Marco, did you forget to mark this as \"positive review\"?",
    "created_at": "2011-04-22T15:20:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47526",
    "user": "cremona"
}
```

Marco, did you forget to mark this as "positive review"?



---

archive/issue_comments_047527.json:
```json
{
    "body": "Replying to [comment:27 cremona]:\n> Marco, did you forget to mark this as \"positive review\"?\n\nActually, I was waiting for an answer to my question first, and then forgot all about the ticket.\n\nIf I recall correctly, the question was not that important.",
    "created_at": "2011-04-22T15:45:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47527",
    "user": "mstreng"
}
```

Replying to [comment:27 cremona]:
> Marco, did you forget to mark this as "positive review"?

Actually, I was waiting for an answer to my question first, and then forgot all about the ticket.

If I recall correctly, the question was not that important.



---

archive/issue_comments_047528.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-04-22T15:45:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47528",
    "user": "mstreng"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_047529.json:
```json
{
    "body": "[attachment:trac_5982-ncalexan-with-check.patch] is not a proper `hg` changeset.  Patches should be made using `hg export tip` and not `hg diff`.",
    "created_at": "2011-04-25T13:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47529",
    "user": "jdemeyer"
}
```

[attachment:trac_5982-ncalexan-with-check.patch] is not a proper `hg` changeset.  Patches should be made using `hg export tip` and not `hg diff`.



---

archive/issue_comments_047530.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-04-25T13:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47530",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_047531.json:
```json
{
    "body": "proper hg changeset version of trac_5982-ncalexan-with-check.patch",
    "created_at": "2011-04-28T10:38:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47531",
    "user": "mstreng"
}
```

proper hg changeset version of trac_5982-ncalexan-with-check.patch



---

archive/issue_comments_047532.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-04-28T10:41:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47532",
    "user": "mstreng"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_047533.json:
```json
{
    "body": "Attachment\n\nI made that patch into a proper hg changeset. All tests still pass, and as the new patch does exactly the same as the old one, I put it back to positive_review.\n\n(apply [attachment:trac_5982-ncalexan-with-check2.patch], [attachment:trac_5982-reviewer.patch], [attachment:trac_5982_review2.patch])",
    "created_at": "2011-04-28T10:41:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47533",
    "user": "mstreng"
}
```

Attachment

I made that patch into a proper hg changeset. All tests still pass, and as the new patch does exactly the same as the old one, I put it back to positive_review.

(apply [attachment:trac_5982-ncalexan-with-check2.patch], [attachment:trac_5982-reviewer.patch], [attachment:trac_5982_review2.patch])



---

archive/issue_comments_047534.json:
```json
{
    "body": "Attachment\n\nthe difference between trac_5982-ncalexan-with-check.patch and trac_5982-ncalexan-with-check2.patch",
    "created_at": "2011-04-28T10:46:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47534",
    "user": "mstreng"
}
```

Attachment

the difference between trac_5982-ncalexan-with-check.patch and trac_5982-ncalexan-with-check2.patch



---

archive/issue_comments_047535.json:
```json
{
    "body": "(apply trac_5982-ncalexan-with-check2.patch, trac_5982-reviewer.patch, trac_5982_review2.patch)",
    "created_at": "2011-04-28T10:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47535",
    "user": "mstreng"
}
```

(apply trac_5982-ncalexan-with-check2.patch, trac_5982-reviewer.patch, trac_5982_review2.patch)



---

archive/issue_comments_047536.json:
```json
{
    "body": "(apply trac_5982-ncalexan-with-check2.patch, trac_5982-reviewer.patch, trac_5982_review2.patch )",
    "created_at": "2011-04-28T10:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47536",
    "user": "mstreng"
}
```

(apply trac_5982-ncalexan-with-check2.patch, trac_5982-reviewer.patch, trac_5982_review2.patch )



---

archive/issue_comments_047537.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-05-03T12:28:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5982#issuecomment-47537",
    "user": "jdemeyer"
}
```

Resolution: fixed
