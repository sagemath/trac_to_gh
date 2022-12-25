# Issue 6329: optional doctest failure -- bad data type breakage in the sage-->magma interface

archive/issues_006329.json:
```json
{
    "body": "Assignee: tbd\n\n```\nsage -t -long --optional devel/sage/sage/rings/rational.pyx\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/rings/rational.pyx\", line 3087:\n    sage: magma(3/1).Type()             # optional\nExpected:\n    FldRatElt\nGot:\n    RngIntElt\n**********************************************************************\n1 items had failures:\n   1 of   5 in __main__.example_84\n***Test Failed*** 1 failures.\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6329\n\n",
    "created_at": "2009-06-16T15:06:55Z",
    "labels": [
        "component: optional packages",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "optional doctest failure -- bad data type breakage in the sage-->magma interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6329",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

```
sage -t -long --optional devel/sage/sage/rings/rational.pyx
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/rings/rational.pyx", line 3087:
    sage: magma(3/1).Type()             # optional
Expected:
    FldRatElt
Got:
    RngIntElt
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_84
***Test Failed*** 1 failures.
```

Issue created by migration from https://trac.sagemath.org/ticket/6329





---

archive/issue_comments_050425.json:
```json
{
    "body": "More failures:\n\n```\nsage -t -long --optional devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py\", line 218:\n    sage: magma(HyperellipticCurve(f)).IgusaClebschInvariants() # optional - magma\nExpected:\n    [ 0, -2048/375, -4096/25, -4881645568/84375 ]\nGot:\n    [ -640, -20480, 1310720, 52160364544 ]\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py\", line 220:\n    sage: magma(HyperellipticCurve(f(2*x))).IgusaClebschInvariants() # optional - magma\nExpected:\n    [ 0, -8388608/375, -1073741824/25, -5241627016305836032/84375 ]\nGot:\n    [ -40960, -83886080, 343597383680, 56006764965979488256 ]\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py\", line 222:\n    sage: magma(HyperellipticCurve(f, x)).IgusaClebschInvariants() # optional - magma\nExpected:\n    [ -8/15, 17504/5625, -23162896/140625, -420832861216768/7119140625 ]\nGot:\n    [ -640, 17920, -1966656, 52409511936 ]\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py\", line 224:\n    sage: magma(HyperellipticCurve(f(2*x), 2*x)).IgusaClebschInvariants() # optional - magma\nExpected:\n    [ -512/15, 71696384/5625, -6072014209024/140625, -451865844002031331704832/7119140625 ]\nGot:\n    [ -40960, 73400320, -515547070464, 56274284941110411264 ]\n**********************************************************************\n1 items had failures:\n   4 of  12 in __main__.example_7\n***Test Failed*** 4 failures.\n\n```",
    "created_at": "2009-06-16T15:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6329#issuecomment-50425",
    "user": "https://github.com/williamstein"
}
```

More failures:

```
sage -t -long --optional devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py", line 218:
    sage: magma(HyperellipticCurve(f)).IgusaClebschInvariants() # optional - magma
Expected:
    [ 0, -2048/375, -4096/25, -4881645568/84375 ]
Got:
    [ -640, -20480, 1310720, 52160364544 ]
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py", line 220:
    sage: magma(HyperellipticCurve(f(2*x))).IgusaClebschInvariants() # optional - magma
Expected:
    [ 0, -8388608/375, -1073741824/25, -5241627016305836032/84375 ]
Got:
    [ -40960, -83886080, 343597383680, 56006764965979488256 ]
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py", line 222:
    sage: magma(HyperellipticCurve(f, x)).IgusaClebschInvariants() # optional - magma
Expected:
    [ -8/15, 17504/5625, -23162896/140625, -420832861216768/7119140625 ]
Got:
    [ -640, 17920, -1966656, 52409511936 ]
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py", line 224:
    sage: magma(HyperellipticCurve(f(2*x), 2*x)).IgusaClebschInvariants() # optional - magma
Expected:
    [ -512/15, 71696384/5625, -6072014209024/140625, -451865844002031331704832/7119140625 ]
Got:
    [ -40960, 73400320, -515547070464, 56274284941110411264 ]
**********************************************************************
1 items had failures:
   4 of  12 in __main__.example_7
***Test Failed*** 4 failures.

```



---

archive/issue_comments_050426.json:
```json
{
    "body": "More failures:\n\n```\nsage -t -long --optional devel/sage/sage/interfaces/magma.py\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py\", line 856:\n    sage: magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_20[2]>\", line 1, in <module>\n        magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma###line 856:\n    sage: magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma\n    NameError: name 'Sage_ROOT' is not defined\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py\", line 860:\n    sage: magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma\nExpected:\n    Traceback (most recent call last):\n    ...\n    RuntimeError: Error evaluating Magma code...\nGot:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_20[3]>\", line 1, in <module>\n        magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma###line 860:\n    sage: magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma\n    NameError: name 'Sage_ROOT' is not defined\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py\", line 917:\n    sage: print magma.load(SAGE_TMP + 'a.m')      # optional - magma\nExpected:\n    Loading \".../.sage//temp/.../a.m\"\n    hi\nGot:\n    Loading \"/scratch/wstein/sage//temp/sage.math.washington.edu/31604/a.m\"\n    hi\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py\", line 2148:\n    sage: magma.eval('R<x> := PolynomialRing(RationalField()); f := (x-17/2)^3;')     # optional - magma\nExpected:\n    \"\nGot:\n    ''\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py\", line 2160:\n    sage: magma.eval('K<a> := CyclotomicField(11)')       # optional - magma\nExpected:\n    \"\nGot:\n    ''\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py\", line 463:\n    sage: magma.eval(\"a := %s;\"%(10^10000))    # optional - magma\nExpected:\n    \"\nGot:\n    ''\n**********************************************************************\n4 items had failures:\n   2 of   4 in __main__.example_20\n   1 of   5 in __main__.example_22\n   2 of  28 in __main__.example_64\n   1 of   4 in __main__.example_9\n***Test Failed*** 6 failures.\nFor whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_magma.py\n\t [32.9 s]\n\n```",
    "created_at": "2009-06-16T15:19:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6329#issuecomment-50426",
    "user": "https://github.com/williamstein"
}
```

More failures:

```
sage -t -long --optional devel/sage/sage/interfaces/magma.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py", line 856:
    sage: magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_20[2]>", line 1, in <module>
        magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma###line 856:
    sage: magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma
    NameError: name 'Sage_ROOT' is not defined
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py", line 860:
    sage: magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma
Expected:
    Traceback (most recent call last):
    ...
    RuntimeError: Error evaluating Magma code...
Got:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_20[3]>", line 1, in <module>
        magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma###line 860:
    sage: magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma
    NameError: name 'Sage_ROOT' is not defined
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py", line 917:
    sage: print magma.load(SAGE_TMP + 'a.m')      # optional - magma
Expected:
    Loading ".../.sage//temp/.../a.m"
    hi
Got:
    Loading "/scratch/wstein/sage//temp/sage.math.washington.edu/31604/a.m"
    hi
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py", line 2148:
    sage: magma.eval('R<x> := PolynomialRing(RationalField()); f := (x-17/2)^3;')     # optional - magma
Expected:
    "
Got:
    ''
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py", line 2160:
    sage: magma.eval('K<a> := CyclotomicField(11)')       # optional - magma
Expected:
    "
Got:
    ''
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py", line 463:
    sage: magma.eval("a := %s;"%(10^10000))    # optional - magma
Expected:
    "
Got:
    ''
**********************************************************************
4 items had failures:
   2 of   4 in __main__.example_20
   1 of   5 in __main__.example_22
   2 of  28 in __main__.example_64
   1 of   4 in __main__.example_9
***Test Failed*** 6 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_magma.py
	 [32.9 s]

```



---

archive/issue_comments_050427.json:
```json
{
    "body": "Attachment [trac_6329.patch](tarball://root/attachments/some-uuid/ticket6329/trac_6329.patch) by mariah created at 2011-05-25 18:24:06",
    "created_at": "2011-05-25T18:24:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6329#issuecomment-50427",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Attachment [trac_6329.patch](tarball://root/attachments/some-uuid/ticket6329/trac_6329.patch) by mariah created at 2011-05-25 18:24:06



---

archive/issue_events_014868.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mariah",
    "created_at": "2011-05-25T18:35:39Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6329",
    "milestone": "sage-4.7.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6329#event-14868"
}
```



---

archive/issue_comments_050428.json:
```json
{
    "body": "[attachment: trac_6329.patch] corrects the test output in the problem in the description.  The Got output is correct - there is **not** a breakage in the sage<-->magma interface.  'magma(3/1)' returns the integer '3' (after coercion), so Type() returns that\nthe value is an integer.\n\nThe other two reports of failures are no longer valid, as they seem to already be fixed in sage-4.7.rc4.",
    "created_at": "2011-05-25T18:35:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6329#issuecomment-50428",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

[attachment: trac_6329.patch] corrects the test output in the problem in the description.  The Got output is correct - there is **not** a breakage in the sage<-->magma interface.  'magma(3/1)' returns the integer '3' (after coercion), so Type() returns that
the value is an integer.

The other two reports of failures are no longer valid, as they seem to already be fixed in sage-4.7.rc4.



---

archive/issue_comments_050429.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-05-25T18:35:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6329#issuecomment-50429",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050430.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2011-05-25T18:35:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6329#issuecomment-50430",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing priority from major to minor.



---

archive/issue_comments_050431.json:
```json
{
    "body": "Changing component from optional packages to interfaces.",
    "created_at": "2011-06-14T03:11:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6329#issuecomment-50431",
    "user": "https://github.com/kcrisman"
}
```

Changing component from optional packages to interfaces.



---

archive/issue_comments_050432.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-08-23T01:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6329#issuecomment-50432",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_050433.json:
```json
{
    "body": "It seems like the correct fix would be to always put the denominator in the _magma_init_ method.\n\n```\n        s = self.numerator()._magma_init_(magma)\n        s += '/' + self.denominator()._magma_init_(magma)\n        return s\n```\n\ninstead of \n\n```\n        s = self.numerator()._magma_init_(magma)\n        if not self.is_integral():\n            s += '/' + self.denominator()._magma_init_(magma)\n        return s\n\n```",
    "created_at": "2011-08-23T01:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6329#issuecomment-50433",
    "user": "https://github.com/mwhansen"
}
```

It seems like the correct fix would be to always put the denominator in the _magma_init_ method.

```
        s = self.numerator()._magma_init_(magma)
        s += '/' + self.denominator()._magma_init_(magma)
        return s
```

instead of 

```
        s = self.numerator()._magma_init_(magma)
        if not self.is_integral():
            s += '/' + self.denominator()._magma_init_(magma)
        return s

```



---

archive/issue_comments_050434.json:
```json
{
    "body": "Mhansen, you're right, the patch Mariah posted is wrong.   I'll post a correct patch, and hopefully you can review it.",
    "created_at": "2011-08-23T05:04:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6329#issuecomment-50434",
    "user": "https://github.com/williamstein"
}
```

Mhansen, you're right, the patch Mariah posted is wrong.   I'll post a correct patch, and hopefully you can review it.



---

archive/issue_comments_050435.json:
```json
{
    "body": "Attachment [trac_6329.2.patch](tarball://root/attachments/some-uuid/ticket6329/trac_6329.2.patch) by @williamstein created at 2011-08-23 05:34:53\n\napply only this one",
    "created_at": "2011-08-23T05:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6329#issuecomment-50435",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_6329.2.patch](tarball://root/attachments/some-uuid/ticket6329/trac_6329.2.patch) by @williamstein created at 2011-08-23 05:34:53

apply only this one



---

archive/issue_comments_050436.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-08-23T05:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6329#issuecomment-50436",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_050437.json:
```json
{
    "body": "Patch up that is ready for review (the .2 one).  This was a result of some overzealous optimization on my part a few years ago.  Reverting this change will barely slow things down.",
    "created_at": "2011-08-23T05:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6329#issuecomment-50437",
    "user": "https://github.com/williamstein"
}
```

Patch up that is ready for review (the .2 one).  This was a result of some overzealous optimization on my part a few years ago.  Reverting this change will barely slow things down.



---

archive/issue_comments_050438.json:
```json
{
    "body": "We should add a doctest for the integral case.",
    "created_at": "2011-08-23T05:49:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6329#issuecomment-50438",
    "user": "https://github.com/mwhansen"
}
```

We should add a doctest for the integral case.



---

archive/issue_comments_050439.json:
```json
{
    "body": "Replying to [comment:8 mhansen]:\n> We should add a doctest for the integral case.\n\n\nWhat do you mean by this?  If you mean `sage: magma(3/1).Type()`, which is in the ticket description, then there is *already* a doctest for this case, which is how we found this bug in the first place. \n\nOr do you mean adding something to integer.pyx???",
    "created_at": "2011-08-24T04:49:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6329#issuecomment-50439",
    "user": "https://github.com/williamstein"
}
```

Replying to [comment:8 mhansen]:
> We should add a doctest for the integral case.


What do you mean by this?  If you mean `sage: magma(3/1).Type()`, which is in the ticket description, then there is *already* a doctest for this case, which is how we found this bug in the first place. 

Or do you mean adding something to integer.pyx???



---

archive/issue_comments_050440.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd32\".",
    "created_at": "2011-08-24T23:36:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6329#issuecomment-50440",
    "user": "https://github.com/williamstein"
}
```

Changing keywords from "" to "sd32".



---

archive/issue_comments_050441.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-08-24T23:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6329#issuecomment-50441",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050442.json:
```json
{
    "body": "I was thinking about the old code and verifying that the \"is_integral\" code path worked (since that test was missing before).  However, it is obviously not needed now.\n\nPositive review.",
    "created_at": "2011-08-24T23:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6329#issuecomment-50442",
    "user": "https://github.com/mwhansen"
}
```

I was thinking about the old code and verifying that the "is_integral" code path worked (since that test was missing before).  However, it is obviously not needed now.

Positive review.



---

archive/issue_comments_050443.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-09-12T19:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6329#issuecomment-50443",
    "user": "https://github.com/nexttime"
}
```

Resolution: fixed



---

archive/issue_events_014869.json:
```json
{
    "actor": "https://github.com/nexttime",
    "created_at": "2011-09-12T19:27:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6329",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6329#event-14869"
}
```



---

archive/issue_comments_050444.json:
```json
{
    "body": "Shame on the idiot who wrote this with no tests... and who forgot that there are optional tests all over Sage that would be broken by this: see #12006, where I'm doing my penance.",
    "created_at": "2012-01-22T21:57:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6329#issuecomment-50444",
    "user": "https://github.com/williamstein"
}
```

Shame on the idiot who wrote this with no tests... and who forgot that there are optional tests all over Sage that would be broken by this: see #12006, where I'm doing my penance.
