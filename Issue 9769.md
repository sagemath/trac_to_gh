# Issue 9769: SphericalDistribution() is not random

archive/issues_009769.json:
```json
{
    "body": "Assignee: amhou\n\nIn the following list `l`, some elements repeat quite often:\n\n\n```\nsage: l = [ SphericalDistribution(dimension=2).get_random_element() for _ in range(1000)]\nsage: uniq = []\nsage: for x in l:\n    if x not in uniq:\n        uniq.append(x)\n....:\nsage: len(uniq)\n34\n```\n\n\nThe output is not random. For example, the first line is repeated ~30 times in the 1000 lines of output.\tIt works fine if SphericalDistribution is only instantiated once!\n\nIssue created by migration from https://trac.sagemath.org/ticket/9770\n\n",
    "created_at": "2010-08-20T10:50:32Z",
    "labels": [
        "component: statistics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "SphericalDistribution() is not random",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9769",
    "user": "https://github.com/haraldschilly"
}
```
Assignee: amhou

In the following list `l`, some elements repeat quite often:


```
sage: l = [ SphericalDistribution(dimension=2).get_random_element() for _ in range(1000)]
sage: uniq = []
sage: for x in l:
    if x not in uniq:
        uniq.append(x)
....:
sage: len(uniq)
34
```


The output is not random. For example, the first line is repeated ~30 times in the 1000 lines of output.	It works fine if SphericalDistribution is only instantiated once!

Issue created by migration from https://trac.sagemath.org/ticket/9770





---

archive/issue_comments_095567.json:
```json
{
    "body": "Attachment [SageDays_random_element_bug.sws](tarball://root/attachments/some-uuid/ticket9770/SageDays_random_element_bug.sws) by jreaton created at 2010-12-10 19:52:19\n\nThe bug is not unique to the spherical distribution; rather, it has to do with whether the distribution is instantiated prior to the use of the random element method.  The worksheet above illustrates the same behavior with the Gaussian and uniform distributions.",
    "created_at": "2010-12-10T19:52:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95567",
    "user": "https://trac.sagemath.org/admin/accounts/users/jreaton"
}
```

Attachment [SageDays_random_element_bug.sws](tarball://root/attachments/some-uuid/ticket9770/SageDays_random_element_bug.sws) by jreaton created at 2010-12-10 19:52:19

The bug is not unique to the spherical distribution; rather, it has to do with whether the distribution is instantiated prior to the use of the random element method.  The worksheet above illustrates the same behavior with the Gaussian and uniform distributions.



---

archive/issue_comments_095568.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-10-31T04:03:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95568",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095569.json:
```json
{
    "body": "Oh, wow.  This is because of the lines\n\n\n```\n            self.seed = random.randint(1, 2^32)\n```\n\n\n2 xor 32 is 34.. and the `^` vs. `**` bug strikes again.",
    "created_at": "2011-10-31T04:03:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95569",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Oh, wow.  This is because of the lines


```
            self.seed = random.randint(1, 2^32)
```


2 xor 32 is 34.. and the `^` vs. `**` bug strikes again.



---

archive/issue_comments_095570.json:
```json
{
    "body": "fix seed randomization",
    "created_at": "2011-10-31T04:04:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95570",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

fix seed randomization



---

archive/issue_comments_095571.json:
```json
{
    "body": "Attachment [trac_9770_fix_distribution_seeds.patch](tarball://root/attachments/some-uuid/ticket9770/trac_9770_fix_distribution_seeds.patch) by @jasongrout created at 2011-12-13 16:18:36\n\nWow, good catch.  Affected file passes tests; code looks good.\n\nCan you fill in the author name?",
    "created_at": "2011-12-13T16:18:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95571",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_9770_fix_distribution_seeds.patch](tarball://root/attachments/some-uuid/ticket9770/trac_9770_fix_distribution_seeds.patch) by @jasongrout created at 2011-12-13 16:18:36

Wow, good catch.  Affected file passes tests; code looks good.

Can you fill in the author name?



---

archive/issue_comments_095572.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-12-13T16:18:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95572",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095573.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-12-17T09:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95573",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_095574.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2011-12-21T09:22:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95574",
    "user": "https://github.com/jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_095575.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2011-12-21T09:22:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95575",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_comments_095576.json:
```json
{
    "body": "On hawk (OpenSolaris 06.2009-32):\n\n```\nsage -t -long  -force_lib devel/sage/sage/gsl/probability_distribution.pyx\n**********************************************************************\nFile \"/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/devel/sage-main/sage/gsl/probability_distribution.pyx\", line 339:\n    sage: T = RealDistribution('rayleigh', sigma)\nException raised:\n    Traceback (most recent call last):\n      File \"/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_12[16]>\", line 1, in <module>\n        T = RealDistribution('rayleigh', sigma)###line 339:\n    sage: T = RealDistribution('rayleigh', sigma)\n      File \"probability_distribution.pyx\", line 503, in sage.gsl.probability_distribution.RealDistribution.__init__ (sage/gsl/probability_distribution.c:2309)\n        self.seed = random.randint(1, 2**32)\n    OverflowError: long int too large to convert to int\n**********************************************************************\n[...many more like this...]\n\nsage -t -long  -force_lib devel/sage/sage/matrix/constructor.py\n**********************************************************************\nFile \"/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/devel/sage-main/sage/matrix/constructor.py\", line 2944:\n    sage: print \"ignore this\";  B=random_matrix(FiniteField(7), 4, 4, algorithm='echelon_form', num_pivots=3); B # random\nException raised:\n    Traceback (most recent call last):\n      File \"/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_19[10]>\", line 1, in <module>\n        print \"ignore this\";  B=random_matrix(FiniteField(Integer(7)), Integer(4), Integer(4), algorithm='echelon_form', num_pivots=Integer(3)); B # random###line 2944:\n    sage: print \"ignore this\";  B=random_matrix(FiniteField(7), 4, 4, algorithm='echelon_form', num_pivots=3); B # random\n      File \"/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/lib/python/site-packages/sage/matrix/constructor.py\", line 1250, in random_matrix\n        return random_rref_matrix(parent, *args, **kwds)\n      File \"/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/lib/python/site-packages/sage/matrix/constructor.py\", line 3020, in random_rref_matrix\n        pivot_generator=pd.RealDistribution(\"beta\",[1.6,4.3])\n      File \"probability_distribution.pyx\", line 503, in sage.gsl.probability_distribution.RealDistribution.__init__ (sage/gsl/probability_distribution.c:2309)\n    OverflowError: long int too large to convert to int\n**********************************************************************\n[...]\n```\n",
    "created_at": "2011-12-21T09:22:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95576",
    "user": "https://github.com/jdemeyer"
}
```

On hawk (OpenSolaris 06.2009-32):

```
sage -t -long  -force_lib devel/sage/sage/gsl/probability_distribution.pyx
**********************************************************************
File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/devel/sage-main/sage/gsl/probability_distribution.pyx", line 339:
    sage: T = RealDistribution('rayleigh', sigma)
Exception raised:
    Traceback (most recent call last):
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_12[16]>", line 1, in <module>
        T = RealDistribution('rayleigh', sigma)###line 339:
    sage: T = RealDistribution('rayleigh', sigma)
      File "probability_distribution.pyx", line 503, in sage.gsl.probability_distribution.RealDistribution.__init__ (sage/gsl/probability_distribution.c:2309)
        self.seed = random.randint(1, 2**32)
    OverflowError: long int too large to convert to int
**********************************************************************
[...many more like this...]

sage -t -long  -force_lib devel/sage/sage/matrix/constructor.py
**********************************************************************
File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/devel/sage-main/sage/matrix/constructor.py", line 2944:
    sage: print "ignore this";  B=random_matrix(FiniteField(7), 4, 4, algorithm='echelon_form', num_pivots=3); B # random
Exception raised:
    Traceback (most recent call last):
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[10]>", line 1, in <module>
        print "ignore this";  B=random_matrix(FiniteField(Integer(7)), Integer(4), Integer(4), algorithm='echelon_form', num_pivots=Integer(3)); B # random###line 2944:
    sage: print "ignore this";  B=random_matrix(FiniteField(7), 4, 4, algorithm='echelon_form', num_pivots=3); B # random
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/lib/python/site-packages/sage/matrix/constructor.py", line 1250, in random_matrix
        return random_rref_matrix(parent, *args, **kwds)
      File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.8.alpha5/local/lib/python/site-packages/sage/matrix/constructor.py", line 3020, in random_rref_matrix
        pivot_generator=pd.RealDistribution("beta",[1.6,4.3])
      File "probability_distribution.pyx", line 503, in sage.gsl.probability_distribution.RealDistribution.__init__ (sage/gsl/probability_distribution.c:2309)
    OverflowError: long int too large to convert to int
**********************************************************************
[...]
```




---

archive/issue_comments_095577.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2011-12-21T16:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95577",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_095578.json:
```json
{
    "body": "Urf.  Probably (?) we can simply replace `2**32` here with sys.maxint, but I can't be sure because I can't reproduce.\n\nEmailed a guy who I know has access to a solaris box :-) but haven't heard back.  If anyone with an account on hawk could report the results of a cut-and-paste of the following\n\n\n```\npreparser(False)\nimport random, sys\n\nnn = [2**31, 2**32, sys.maxint]\nfor n in nn:\n    for d in -1, 0, 1:\n        print n, d, n+d, repr(n+d), type(n+d)\n        try:\n            seed = random.randint(1, n+d)\n        except Exception as err:\n            print err\n        try:\n            random.seed(n+d)\n        except Exception as err:\n            print err\n```\n\n\nfrom within Sage, that would test whether I understand what's going on.",
    "created_at": "2011-12-21T16:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95578",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Urf.  Probably (?) we can simply replace `2**32` here with sys.maxint, but I can't be sure because I can't reproduce.

Emailed a guy who I know has access to a solaris box :-) but haven't heard back.  If anyone with an account on hawk could report the results of a cut-and-paste of the following


```
preparser(False)
import random, sys

nn = [2**31, 2**32, sys.maxint]
for n in nn:
    for d in -1, 0, 1:
        print n, d, n+d, repr(n+d), type(n+d)
        try:
            seed = random.randint(1, n+d)
        except Exception as err:
            print err
        try:
            random.seed(n+d)
        except Exception as err:
            print err
```


from within Sage, that would test whether I understand what's going on.



---

archive/issue_comments_095579.json:
```json
{
    "body": "Output of your Sage script on `hawk`:\n\n```\n2147483648 -1 2147483647 2147483647L <type 'long'>\n2147483648 0 2147483648 2147483648L <type 'long'>\n2147483648 1 2147483649 2147483649L <type 'long'>\n4294967296 -1 4294967295 4294967295L <type 'long'>\n4294967296 0 4294967296 4294967296L <type 'long'>\n4294967296 1 4294967297 4294967297L <type 'long'>\n2147483647 -1 2147483646 2147483646 <type 'int'>\n2147483647 0 2147483647 2147483647 <type 'int'>\n2147483647 1 2147483648 2147483648L <type 'long'>\n```\n",
    "created_at": "2011-12-22T12:42:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95579",
    "user": "https://github.com/jdemeyer"
}
```

Output of your Sage script on `hawk`:

```
2147483648 -1 2147483647 2147483647L <type 'long'>
2147483648 0 2147483648 2147483648L <type 'long'>
2147483648 1 2147483649 2147483649L <type 'long'>
4294967296 -1 4294967295 4294967295L <type 'long'>
4294967296 0 4294967296 4294967296L <type 'long'>
4294967296 1 4294967297 4294967297L <type 'long'>
2147483647 -1 2147483646 2147483646 <type 'int'>
2147483647 0 2147483647 2147483647 <type 'int'>
2147483647 1 2147483648 2147483648L <type 'long'>
```




---

archive/issue_comments_095580.json:
```json
{
    "body": "*** bump ***",
    "created_at": "2012-01-24T09:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95580",
    "user": "https://github.com/jdemeyer"
}
```

*** bump ***



---

archive/issue_comments_095581.json:
```json
{
    "body": "hopefully maxint-safe version",
    "created_at": "2012-02-05T04:43:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95581",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

hopefully maxint-safe version



---

archive/issue_comments_095582.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2012-02-05T04:44:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95582",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_095583.json:
```json
{
    "body": "Attachment [trac_9770_fix_distribution_seeds_v2.patch](tarball://root/attachments/some-uuid/ticket9770/trac_9770_fix_distribution_seeds_v2.patch) by dsm created at 2012-02-05 04:44:50\n\nVersion modified to (hopefully) avoid overflow errors without sacrificing entropy.  `@`jdemeyer, you mind trying it on hawk?",
    "created_at": "2012-02-05T04:44:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95583",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Attachment [trac_9770_fix_distribution_seeds_v2.patch](tarball://root/attachments/some-uuid/ticket9770/trac_9770_fix_distribution_seeds_v2.patch) by dsm created at 2012-02-05 04:44:50

Version modified to (hopefully) avoid overflow errors without sacrificing entropy.  `@`jdemeyer, you mind trying it on hawk?



---

archive/issue_comments_095584.json:
```json
{
    "body": "Apply trac_9770_fix_distribution_seeds_v2.patch\n\n(for the patchbot, which is trying to install both patches at once)",
    "created_at": "2012-03-11T14:35:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95584",
    "user": "https://github.com/loefflerd"
}
```

Apply trac_9770_fix_distribution_seeds_v2.patch

(for the patchbot, which is trying to install both patches at once)



---

archive/issue_comments_095585.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-03-11T16:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95585",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_095586.json:
```json
{
    "body": "This seems to conflict (in a rather trivial way) with #9958, and hence doesn't apply to the latest Sage beta.",
    "created_at": "2012-03-11T16:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95586",
    "user": "https://github.com/loefflerd"
}
```

This seems to conflict (in a rather trivial way) with #9958, and hence doesn't apply to the latest Sage beta.



---

archive/issue_comments_095587.json:
```json
{
    "body": "Attachment [trac_9770_fix_distribution_seeds_v4.patch](tarball://root/attachments/some-uuid/ticket9770/trac_9770_fix_distribution_seeds_v4.patch) by dsm created at 2012-03-12 02:42:32\n\nrebased to 5.0.beta7",
    "created_at": "2012-03-12T02:42:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95587",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Attachment [trac_9770_fix_distribution_seeds_v4.patch](tarball://root/attachments/some-uuid/ticket9770/trac_9770_fix_distribution_seeds_v4.patch) by dsm created at 2012-03-12 02:42:32

rebased to 5.0.beta7



---

archive/issue_comments_095588.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-03-12T02:46:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95588",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_095589.json:
```json
{
    "body": "Apply trac_9770_fix_distribution_seeds_v4.patch\n\n(for patchbot)",
    "created_at": "2012-03-12T07:48:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95589",
    "user": "https://github.com/loefflerd"
}
```

Apply trac_9770_fix_distribution_seeds_v4.patch

(for patchbot)



---

archive/issue_comments_095590.json:
```json
{
    "body": "Let's not anthropomorphize the PatchBot :-)",
    "created_at": "2012-03-15T20:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95590",
    "user": "https://github.com/jdemeyer"
}
```

Let's not anthropomorphize the PatchBot :-)



---

archive/issue_comments_095591.json:
```json
{
    "body": "Seems to work as it should...",
    "created_at": "2012-03-19T16:14:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95591",
    "user": "https://github.com/jdemeyer"
}
```

Seems to work as it should...



---

archive/issue_comments_095592.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-19T16:14:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95592",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095593.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-03-21T22:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9769#issuecomment-95593",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
