# Issue 6326: optional doctest failure -- all quadratic forms tests that involve " # optional -- souvigner"

archive/issues_006326.json:
```json
{
    "body": "Assignee: tbd\n\nThese all fail.  This \"souvigner\" is not an optional or even experimental spkg.  I have no clue where to get it. Either this code has to go, or Souvigner_AUTO has to be made an optional spkg (which would be a very reasonable way to resolve this ticket).\n\n\n```\nsage -t -long --optional devel/sage/sage/quadratic_forms/quadratic_form__automorphisms.py\nsh: /scratch/wstein/build/sage-4.0.2.alpha3/local/bin/Souvigner_AUTO: not found\nsh: /scratch/wstein/build/sage-4.0.2.alpha3/local/bin/Souvigner_AUTO: not found\nsh: /scratch/wstein/build/sage-4.0.2.alpha3/local/bin/Souvigner_AUTO: not found\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/quadratic_forms/quadratic_form__automorphisms.py\", line 257:\n    sage: Q.number_of_automorphisms()                     # optional -- souvigner\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[3]>\", line 1, in <module>\n        Q.number_of_automorphisms()                     # optional -- souvigner###line 257:\n    sage: Q.number_of_automorphisms()                     # optional -- souvigner\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py\", line 396, in number_of_automorphisms\n        self.__number_of_automorphisms = self.number_of_automorphisms__souvigner()\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py\", line 453, in number_of_automorphisms__souvigner\n        raise RuntimeError, \"Oops! There is a problem...\"\n    RuntimeError: Oops! There is a problem...\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/quadratic_forms/quadratic_form__automorphisms.py\", line 265:\n    sage: Q.number_of_automorphisms()                     # optional -- souvigner\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[7]>\", line 1, in <module>\n        Q.number_of_automorphisms()                     # optional -- souvigner###line 265:\n    sage: Q.number_of_automorphisms()                     # optional -- souvigner\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py\", line 396, in number_of_automorphisms\n        self.__number_of_automorphisms = self.number_of_automorphisms__souvigner()\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py\", line 453, in number_of_automorphisms__souvigner\n        raise RuntimeError, \"Oops! There is a problem...\"\n    RuntimeError: Oops! There is a problem...\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/quadratic_forms/quadratic_form__automorphisms.py\", line 363:\n    sage: Q.number_of_automorphisms(recompute=True)           # optional -- souvigner\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/binsh: /scratch/wstein/build/sage-4.0.2.alpha3/local/bin/Souvigner_AUTO: not found\nsh: /scratch/wstein/build/sage-4.0.2.alpha3/local/bin/Souvigner_AUTO: not found\n/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_4[5]>\", line 1, in <module>\n        Q.number_of_automorphisms(recompute=True)           # optional -- souvigner###line 363:\n    sage: Q.number_of_automorphisms(recompute=True)           # optional -- souvigner\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py\", line 396, in number_of_automorphisms\n        self.__number_of_automorphisms = self.number_of_automorphisms__souvigner()\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py\", line 453, in number_of_automorphisms__souvigner\n        raise RuntimeError, \"Oops! There is a problem...\"\n    RuntimeError: Oops! There is a problem...\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/quadratic_forms/quadratic_form__automorphisms.py\", line 365:\n    sage: Q.list_external_initializations()                   # optional -- souvigner\nExpected:\n    []\nGot:\n    ['number_of_automorphisms']\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/quadratic_forms/quadratic_form__automorphisms.py\", line 369:\n    sage: Q.number_of_automorphisms()                         # optional -- souvigner\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_4[8]>\", line 1, in <module>\n        Q.number_of_automorphisms()                         # optional -- souvigner###line 369:\n    sage: Q.number_of_automorphisms()                         # optional -- souvigner\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py\", line 396, in number_of_automorphisms\n        self.__number_of_automorphisms = self.number_of_automorphisms__souvigner()\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py\", line 453, in number_of_automorphisms__souvigner\n        raise RuntimeError, \"Oops! There is a problem...\"\n    RuntimeError: Oops! There is a problem...\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/quadratic_forms/quadratic_form__automorphisms.py\", line 410:\n    sage: Q.number_of_automorphisms__souvigner()                           # optional -- souvigner\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[3]>\", line 1, in <module>\n        Q.number_of_automorphisms__souvigner()                           # optional -- souvigner###line 410:\n    sage: Q.number_of_automorphisms__souvigner()                           # optional -- souvigner\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py\", line 453, in number_of_automorphisms__souvigner\n        raise RuntimeError, \"Oops! There is a problem...\"\n    RuntimeError: Oops! There is a problem...\n**********************************************************************\n3 items had failures:\n   2 of  15 in __main__.example_3\n   3 of  12 in __main__.example_4\n   1 of   5 in __main__.example_5\n***Test Failed*** 6 failures.\nFor whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_quadratic_form__automorphisms.p\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6326\n\n",
    "created_at": "2009-06-16T15:00:34Z",
    "labels": [
        "optional packages",
        "major",
        "bug"
    ],
    "title": "optional doctest failure -- all quadratic forms tests that involve \" # optional -- souvigner\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6326",
    "user": "was"
}
```
Assignee: tbd

These all fail.  This "souvigner" is not an optional or even experimental spkg.  I have no clue where to get it. Either this code has to go, or Souvigner_AUTO has to be made an optional spkg (which would be a very reasonable way to resolve this ticket).


```
sage -t -long --optional devel/sage/sage/quadratic_forms/quadratic_form__automorphisms.py
sh: /scratch/wstein/build/sage-4.0.2.alpha3/local/bin/Souvigner_AUTO: not found
sh: /scratch/wstein/build/sage-4.0.2.alpha3/local/bin/Souvigner_AUTO: not found
sh: /scratch/wstein/build/sage-4.0.2.alpha3/local/bin/Souvigner_AUTO: not found
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/quadratic_forms/quadratic_form__automorphisms.py", line 257:
    sage: Q.number_of_automorphisms()                     # optional -- souvigner
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[3]>", line 1, in <module>
        Q.number_of_automorphisms()                     # optional -- souvigner###line 257:
    sage: Q.number_of_automorphisms()                     # optional -- souvigner
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py", line 396, in number_of_automorphisms
        self.__number_of_automorphisms = self.number_of_automorphisms__souvigner()
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py", line 453, in number_of_automorphisms__souvigner
        raise RuntimeError, "Oops! There is a problem..."
    RuntimeError: Oops! There is a problem...
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/quadratic_forms/quadratic_form__automorphisms.py", line 265:
    sage: Q.number_of_automorphisms()                     # optional -- souvigner
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[7]>", line 1, in <module>
        Q.number_of_automorphisms()                     # optional -- souvigner###line 265:
    sage: Q.number_of_automorphisms()                     # optional -- souvigner
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py", line 396, in number_of_automorphisms
        self.__number_of_automorphisms = self.number_of_automorphisms__souvigner()
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py", line 453, in number_of_automorphisms__souvigner
        raise RuntimeError, "Oops! There is a problem..."
    RuntimeError: Oops! There is a problem...
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/quadratic_forms/quadratic_form__automorphisms.py", line 363:
    sage: Q.number_of_automorphisms(recompute=True)           # optional -- souvigner
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/binsh: /scratch/wstein/build/sage-4.0.2.alpha3/local/bin/Souvigner_AUTO: not found
sh: /scratch/wstein/build/sage-4.0.2.alpha3/local/bin/Souvigner_AUTO: not found
/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[5]>", line 1, in <module>
        Q.number_of_automorphisms(recompute=True)           # optional -- souvigner###line 363:
    sage: Q.number_of_automorphisms(recompute=True)           # optional -- souvigner
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py", line 396, in number_of_automorphisms
        self.__number_of_automorphisms = self.number_of_automorphisms__souvigner()
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py", line 453, in number_of_automorphisms__souvigner
        raise RuntimeError, "Oops! There is a problem..."
    RuntimeError: Oops! There is a problem...
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/quadratic_forms/quadratic_form__automorphisms.py", line 365:
    sage: Q.list_external_initializations()                   # optional -- souvigner
Expected:
    []
Got:
    ['number_of_automorphisms']
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/quadratic_forms/quadratic_form__automorphisms.py", line 369:
    sage: Q.number_of_automorphisms()                         # optional -- souvigner
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[8]>", line 1, in <module>
        Q.number_of_automorphisms()                         # optional -- souvigner###line 369:
    sage: Q.number_of_automorphisms()                         # optional -- souvigner
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py", line 396, in number_of_automorphisms
        self.__number_of_automorphisms = self.number_of_automorphisms__souvigner()
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py", line 453, in number_of_automorphisms__souvigner
        raise RuntimeError, "Oops! There is a problem..."
    RuntimeError: Oops! There is a problem...
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/quadratic_forms/quadratic_form__automorphisms.py", line 410:
    sage: Q.number_of_automorphisms__souvigner()                           # optional -- souvigner
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[3]>", line 1, in <module>
        Q.number_of_automorphisms__souvigner()                           # optional -- souvigner###line 410:
    sage: Q.number_of_automorphisms__souvigner()                           # optional -- souvigner
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/quadratic_forms/quadratic_form__automorphisms.py", line 453, in number_of_automorphisms__souvigner
        raise RuntimeError, "Oops! There is a problem..."
    RuntimeError: Oops! There is a problem...
**********************************************************************
3 items had failures:
   2 of  15 in __main__.example_3
   3 of  12 in __main__.example_4
   1 of   5 in __main__.example_5
***Test Failed*** 6 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_quadratic_form__automorphisms.p
```


Issue created by migration from https://trac.sagemath.org/ticket/6326





---

archive/issue_comments_050483.json:
```json
{
    "body": "Souvigner auto/isomorphism code tarball",
    "created_at": "2011-01-09T07:57:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50483",
    "user": "jonhanke"
}
```

Souvigner auto/isomorphism code tarball



---

archive/issue_comments_050484.json:
```json
{
    "body": "Attachment\n\nI have attached the Souvigner tarball sent to me by Gabi Nebe in March 2008.  I'm not sure how to arrange Sage to build it, but the two files ISOM64 and AUTO64 that the makeflie produces need to renamed as Souvigner_ISOM and Souvigner_AUTO and moved to sage-4.x/local/bin.",
    "created_at": "2011-01-09T08:01:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50484",
    "user": "jonhanke"
}
```

Attachment

I have attached the Souvigner tarball sent to me by Gabi Nebe in March 2008.  I'm not sure how to arrange Sage to build it, but the two files ISOM64 and AUTO64 that the makeflie produces need to renamed as Souvigner_ISOM and Souvigner_AUTO and moved to sage-4.x/local/bin.



---

archive/issue_comments_050485.json:
```json
{
    "body": "Changing assignee from tbd to justin.",
    "created_at": "2011-01-12T04:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50485",
    "user": "jonhanke"
}
```

Changing assignee from tbd to justin.



---

archive/issue_comments_050486.json:
```json
{
    "body": "Changing component from optional packages to quadratic forms.",
    "created_at": "2011-01-12T04:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50486",
    "user": "jonhanke"
}
```

Changing component from optional packages to quadratic forms.



---

archive/issue_comments_050487.json:
```json
{
    "body": "There is a bug within the interface the Souvigner code that produces false results:\n\n```\nsage: Q1 = DiagonalQuadraticForm(ZZ, [1,3,5])\nsage: Q2 = QuadraticForm(ZZ, 3, [1,0,0, 2,2, 8])\nsage: Q1.theta_series()\n1 + 2*q + 2*q^3 + 6*q^4 + 2*q^5 + 4*q^6 + 4*q^7 + 4*q^8 + 14*q^9 + O(q^10)\nsage: Q2.theta_series()\n1 + 2*q + 2*q^2 + 4*q^3 + 2*q^4 + 4*q^6 + 6*q^8 + 14*q^9 + O(q^10)\nsage: Q1.is_globally_equivalent_to(Q2)    ## Correct\nFalse\nsage: Q2.is_globally_equivalent_to(Q1)    ## Incorrect\nTrue\n```\n\n\nThe problem results from the differing possible failure messages (\"...not isometric...\" or \"...not isomorphic...\") returned from the Souvigner Code.  A patch is attached.",
    "created_at": "2011-01-12T04:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50487",
    "user": "jonhanke"
}
```

There is a bug within the interface the Souvigner code that produces false results:

```
sage: Q1 = DiagonalQuadraticForm(ZZ, [1,3,5])
sage: Q2 = QuadraticForm(ZZ, 3, [1,0,0, 2,2, 8])
sage: Q1.theta_series()
1 + 2*q + 2*q^3 + 6*q^4 + 2*q^5 + 4*q^6 + 4*q^7 + 4*q^8 + 14*q^9 + O(q^10)
sage: Q2.theta_series()
1 + 2*q + 2*q^2 + 4*q^3 + 2*q^4 + 4*q^6 + 6*q^8 + 14*q^9 + O(q^10)
sage: Q1.is_globally_equivalent_to(Q2)    ## Correct
False
sage: Q2.is_globally_equivalent_to(Q1)    ## Incorrect
True
```


The problem results from the differing possible failure messages ("...not isometric..." or "...not isomorphic...") returned from the Souvigner Code.  A patch is attached.



---

archive/issue_comments_050488.json:
```json
{
    "body": "Fixes a bug in the quadratic forms global equivalence testing using Souvigner's code",
    "created_at": "2011-01-12T04:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50488",
    "user": "jonhanke"
}
```

Fixes a bug in the quadratic forms global equivalence testing using Souvigner's code



---

archive/issue_comments_050489.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-12T04:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50489",
    "user": "jonhanke"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050490.json:
```json
{
    "body": "Attachment",
    "created_at": "2011-01-12T04:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50490",
    "user": "jonhanke"
}
```

Attachment



---

archive/issue_comments_050491.json:
```json
{
    "body": "In order for this to get into Sage proper, we'll need to make an spkg which installs the right things to the right places.",
    "created_at": "2011-03-11T06:06:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50491",
    "user": "rlm"
}
```

In order for this to get into Sage proper, we'll need to make an spkg which installs the right things to the right places.



---

archive/issue_comments_050492.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-03-11T06:06:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50492",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_050493.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-08-13T15:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50493",
    "user": "jdemeyer"
}
```

Attachment



---

archive/issue_comments_050494.json:
```json
{
    "body": "If anybody cares about this: this functionality is now also provided by the PARI functions `qfisom()` and `qfauto()`.",
    "created_at": "2015-06-10T20:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50494",
    "user": "jdemeyer"
}
```

If anybody cares about this: this functionality is now also provided by the PARI functions `qfisom()` and `qfauto()`.



---

archive/issue_comments_050495.json:
```json
{
    "body": "New commits:",
    "created_at": "2015-06-10T21:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50495",
    "user": "jdemeyer"
}
```

New commits:



---

archive/issue_comments_050496.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2015-06-10T21:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50496",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_050497.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-06-10T21:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50497",
    "user": "jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_050498.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2015-06-11T08:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50498",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_050499.json:
```json
{
    "body": "Changing keywords from \"\" to \"quadratic form\".",
    "created_at": "2015-06-12T15:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50499",
    "user": "chapoton"
}
```

Changing keywords from "" to "quadratic form".



---

archive/issue_comments_050500.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-06-12T15:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50500",
    "user": "chapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050501.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2015-06-12T15:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50501",
    "user": "chapoton"
}
```

Looks good to me.



---

archive/issue_comments_050502.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-06-12T22:58:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50502",
    "user": "vbraun"
}
```

Resolution: fixed
