# Issue 6284: fix the numerous broken optional magma doctests

archive/issues_006284.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nwstein@sage:~/build/sage-4.0.2.alpha3$  ./sage -tp 30 --only_optional=magma devel/sage/sage/\n...\n\n        sage -t --only_optional=magma devel/sage/sage/symbolic/expression.pyx # 1 doctests failed\n        sage -t --only_optional=magma devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py # 4 doctests fa\niled\n        sage -t --only_optional=magma devel/sage/sage/interfaces/magma.py # 6 doctests failed\n```\n\n\nThe actual failures\n\n```\nsage -t --only_optional=magma devel/sage/sage/symbolic/expression.pyx\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/symbolic/expression.pyx\", line 473:\n    sage: magma(f)                         # optional - magma\nExpected:\n    sin(cos(x^2) + log(x))\nGot:\n    sin(log(x) + cos(x^2))\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_0\n\n\nsage -t --only_optional=magma devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py\",\nline 218:\n    sage: magma(HyperellipticCurve(f)).IgusaClebschInvariants() # optional - magma\nExpected:\n    [ 0, -2048/375, -4096/25, -4881645568/84375 ]\nGot:\n    [ -640, -20480, 1310720, 52160364544 ]\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py\",\nline 220:\n    sage: magma(HyperellipticCurve(f(2*x))).IgusaClebschInvariants() # optional - magma\nExpected:\n    [ 0, -8388608/375, -1073741824/25, -5241627016305836032/84375 ]\nGot:\n    [ -40960, -83886080, 343597383680, 56006764965979488256 ]\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py\",\nline 222:\n    sage: magma(HyperellipticCurve(f, x)).IgusaClebschInvariants() # optional - magma\nExpected:\n    [ -8/15, 17504/5625, -23162896/140625, -420832861216768/7119140625 ]\nGot:\n    [ -640, 17920, -1966656, 52409511936 ]\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py\",\nline 224:\n    sage: magma(HyperellipticCurve(f(2*x), 2*x)).IgusaClebschInvariants() # optional - magma\nExpected:\n    [ -512/15, 71696384/5625, -6072014209024/140625, -451865844002031331704832/7119140625 ]\nGot:\n    [ -40960, 73400320, -515547070464, 56274284941110411264 ]\n**********************************************************************\n1 items had failures:\n   4 of  12 in __main__.example_3\n***Test Failed*** 4 failures.\n\n\nsage -t --only_optional=magma devel/sage/sage/interfaces/magma.py\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py\", line 856:\n    sage: magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_14[2]>\", line 1, in <module>\n        magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma###line 856:\n    sage: magma.attach('%s/data/extcode/magma/sage/basic.m'%Sage_ROOT)    # optional - magma\n    NameError: name 'Sage_ROOT' is not defined\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py\", line 860:\n    sage: magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma\nExpected:\n    Traceback (most recent call last):\n    ...\n    RuntimeError: Error evaluating Magma code...\nGot:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_14[3]>\", line 1, in <module>\n        magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma###line 860:\n    sage: magma.attach('%s/data/extcode/magma/sage/basic2.m'%Sage_ROOT)     # optional - magma\n    NameError: name 'Sage_ROOT' is not defined\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py\", line 917:\n    sage: print magma.load(SAGE_TMP + 'a.m')      # optional - magma\nExpected:\n    Loading \".../.sage//temp/.../a.m\"\n    hi\nGot:\n    Loading \"/scratch/wstein/sage//temp/sage.math.washington.edu/19243/a.m\"\n    hi\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py\", line 463:\n    sage: magma.eval(\"a := %s;\"%(10^10000))    # optional - magma\nExpected:\n    \"\nGot:\n    ''\n**********************************************************************\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py\", line 2148:\n    sage: magma.eval('R<x> := PolynomialRing(RationalField()); f := (x-17/2)^3;')     # optional - magma\nExpected:\n    \"\nGot:\n    ''\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py\", line 2160:\n    sage: magma.eval('K<a> := CyclotomicField(11)')       # optional - magma\nExpected:\n    \"\nGot:\n    ''\n**********************************************************************\n4 items had failures:\n   2 of   4 in __main__.example_14\n   1 of   5 in __main__.example_16\n   1 of   4 in __main__.example_3\n   2 of  28 in __main__.example_47\n***Test Failed*** 6 failures.\n```\n\n\n}}}\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6284\n\n",
    "created_at": "2009-06-14T10:36:29Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "fix the numerous broken optional magma doctests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6284",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd


```
wstein@sage:~/build/sage-4.0.2.alpha3$  ./sage -tp 30 --only_optional=magma devel/sage/sage/
...

        sage -t --only_optional=magma devel/sage/sage/symbolic/expression.pyx # 1 doctests failed
        sage -t --only_optional=magma devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py # 4 doctests fa
iled
        sage -t --only_optional=magma devel/sage/sage/interfaces/magma.py # 6 doctests failed
```


The actual failures

```
sage -t --only_optional=magma devel/sage/sage/symbolic/expression.pyx
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/symbolic/expression.pyx", line 473:
    sage: magma(f)                         # optional - magma
Expected:
    sin(cos(x^2) + log(x))
Got:
    sin(log(x) + cos(x^2))
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_0


sage -t --only_optional=magma devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py",
line 218:
    sage: magma(HyperellipticCurve(f)).IgusaClebschInvariants() # optional - magma
Expected:
    [ 0, -2048/375, -4096/25, -4881645568/84375 ]
Got:
    [ -640, -20480, 1310720, 52160364544 ]
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py",
line 220:
    sage: magma(HyperellipticCurve(f(2*x))).IgusaClebschInvariants() # optional - magma
Expected:
    [ 0, -8388608/375, -1073741824/25, -5241627016305836032/84375 ]
Got:
    [ -40960, -83886080, 343597383680, 56006764965979488256 ]
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py",
line 222:
    sage: magma(HyperellipticCurve(f, x)).IgusaClebschInvariants() # optional - magma
Expected:
    [ -8/15, 17504/5625, -23162896/140625, -420832861216768/7119140625 ]
Got:
    [ -640, 17920, -1966656, 52409511936 ]
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py",
line 224:
    sage: magma(HyperellipticCurve(f(2*x), 2*x)).IgusaClebschInvariants() # optional - magma
Expected:
    [ -512/15, 71696384/5625, -6072014209024/140625, -451865844002031331704832/7119140625 ]
Got:
    [ -40960, 73400320, -515547070464, 56274284941110411264 ]
**********************************************************************
1 items had failures:
   4 of  12 in __main__.example_3
***Test Failed*** 4 failures.


sage -t --only_optional=magma devel/sage/sage/interfaces/magma.py
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
      File "<doctest __main__.example_14[2]>", line 1, in <module>
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
      File "<doctest __main__.example_14[3]>", line 1, in <module>
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
    Loading "/scratch/wstein/sage//temp/sage.math.washington.edu/19243/a.m"
    hi
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/magma.py", line 463:
    sage: magma.eval("a := %s;"%(10^10000))    # optional - magma
Expected:
    "
Got:
    ''
**********************************************************************
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
4 items had failures:
   2 of   4 in __main__.example_14
   1 of   5 in __main__.example_16
   1 of   4 in __main__.example_3
   2 of  28 in __main__.example_47
***Test Failed*** 6 failures.
```


}}}



Issue created by migration from https://trac.sagemath.org/ticket/6284





---

archive/issue_comments_050085.json:
```json
{
    "body": "I believe this ticket can be closed as it has been superceded by #7870.",
    "created_at": "2011-05-24T20:17:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6284#issuecomment-50085",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

I believe this ticket can be closed as it has been superceded by #7870.



---

archive/issue_comments_050086.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-05-24T20:17:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6284#issuecomment-50086",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050087.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-08-23T05:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6284#issuecomment-50087",
    "user": "https://github.com/williamstein"
}
```

Resolution: duplicate



---

archive/issue_events_006528.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2011-08-23T05:19:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6284",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6284#event-6528"
}
```



---

archive/issue_comments_050088.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd32\".",
    "created_at": "2011-08-24T23:44:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6284#issuecomment-50088",
    "user": "https://github.com/williamstein"
}
```

Changing keywords from "" to "sd32".
