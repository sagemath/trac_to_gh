# Issue 6045: [with patch, needs review] Computation of Heegner points

archive/issues_006045.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @williamstein\n\nAdds Heegner point method to elliptic curves over Q. Also cleans up the modular parametrization code.\n\nThis ticket is almost certainly related: #4849\n\nIssue created by migration from https://trac.sagemath.org/ticket/6045\n\n",
    "created_at": "2009-05-15T09:59:52Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "[with patch, needs review] Computation of Heegner points",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6045",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein

CC:  @williamstein

Adds Heegner point method to elliptic curves over Q. Also cleans up the modular parametrization code.

This ticket is almost certainly related: #4849

Issue created by migration from https://trac.sagemath.org/ticket/6045





---

archive/issue_comments_048051.json:
```json
{
    "body": "I just looked at this and realized I can't just lift_x, I need to pick the right one. That should be easy given I have it embedded into C.",
    "created_at": "2009-05-16T03:11:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48051",
    "user": "https://github.com/robertwb"
}
```

I just looked at this and realized I can't just lift_x, I need to pick the right one. That should be easy given I have it embedded into C.



---

archive/issue_comments_048052.json:
```json
{
    "body": "Fixed the lifting issue, ready for review.",
    "created_at": "2009-06-06T06:30:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48052",
    "user": "https://github.com/robertwb"
}
```

Fixed the lifting issue, ready for review.



---

archive/issue_comments_048053.json:
```json
{
    "body": "This code isn't ready for primetime, even with the lifting issue fixed, because increasing the precision until algdep succeeds is a recipe for disaster.  Maybe a bound on the number of precision increases?",
    "created_at": "2009-06-06T20:26:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48053",
    "user": "https://github.com/ncalexan"
}
```

This code isn't ready for primetime, even with the lifting issue fixed, because increasing the precision until algdep succeeds is a recipe for disaster.  Maybe a bound on the number of precision increases?



---

archive/issue_comments_048054.json:
```json
{
    "body": "There is a bound on how often it increases precision--in fact it's even one of the parameters (max_prec).",
    "created_at": "2009-06-06T23:05:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48054",
    "user": "https://github.com/robertwb"
}
```

There is a bound on how often it increases precision--in fact it's even one of the parameters (max_prec).



---

archive/issue_comments_048055.json:
```json
{
    "body": "Sorry, totally asleep at the wheel.  This looks good to me, but I'm not expert in the genus 1 case.  Maybe was can be the final word?",
    "created_at": "2009-06-06T23:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48055",
    "user": "https://github.com/ncalexan"
}
```

Sorry, totally asleep at the wheel.  This looks good to me, but I'm not expert in the genus 1 case.  Maybe was can be the final word?



---

archive/issue_comments_048056.json:
```json
{
    "body": "I'm intending to try this and review it since I have implemented similar in C++ and in gp.",
    "created_at": "2009-06-14T17:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48056",
    "user": "https://github.com/JohnCremona"
}
```

I'm intending to try this and review it since I have implemented similar in C++ and in gp.



---

archive/issue_comments_048057.json:
```json
{
    "body": "REVIEW:  I applied this to 4.0.1, but got some doctest failures:\n\n```\nsage -t  \"devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py\"\n**********************************************************************\nFile \"/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py\", line 5248:\n    sage: E._heegner_best_tau(-7)\nExpected:\n    (sqrt(7)*I - 17)/74\nGot:\n    1/74*sqrt(-7) - 17/74\n**********************************************************************\nFile \"/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py\", line 5250:\n    sage: EllipticCurve('389a')._heegner_best_tau(-11)\nExpected:\n    (sqrt(11)*I - 355)/778\nGot:\n    1/778*sqrt(-11) - 355/778\n**********************************************************************\nFile \"/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py\", line 5291:\n    sage: P = E.heegner_point(-40); P\nException raised:\n    Traceback (most recent call last):\n      File \"/home/john/sage-4.0.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/john/sage-4.0.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/john/sage-4.0.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_115[5]>\", line 1, in <module>\n        P = E.heegner_point(-Integer(40)); P###line 5291:\n    sage: P = E.heegner_point(-40); P\n      File \"/home/john/sage-4.0.1/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py\", line 5335, in heegner_point\n        raise ValueError, \"Not enough precision (%s) to get heegner point exactly, try passing a larger max_prec.\" % (prec)\n    ValueError: Not enough precision (2000) to get heegner point exactly, try passing a larger max_prec.\n**********************************************************************\nFile \"/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py\", line 5301:\n    sage: f = algdep(P[0], 5); f\nExpected:\n    x^5 + 2*x^4 + x^3 - x^2 - x - 1\nGot:\n    x^5 - x^4 + x^3 + x^2 - 2*x + 1\n**********************************************************************\nFile \"/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py\", line 6825:\n    sage: phi(CC.0)\nExpected:\n    (-2.04158222510587 + 3.21664059900000e-29*I : -0.500000000000000 + 0.0906126752327350*I : 1.00000000000000)\nGot:\n    (287826.309565255 : -1.54417490329940e8 : 1.00000000000000)\n**********************************************************************\nFile \"/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py\", line 3114:\n    sage: X,Y=E.modular_parametrization()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/john/sage-4.0.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/john/sage-4.0.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/john/sage-4.0.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_70[3]>\", line 1, in <module>\n        X,Y=E.modular_parametrization()###line 3114:\n    sage: X,Y=E.modular_parametrization()\n    TypeError: iteration over non-sequence\n**********************************************************************\nFile \"/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py\", line 3115:\n    sage: X\nException raised:\n    Traceback (most recent call last):\n      File \"/home/john/sage-4.0.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/john/sage-4.0.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/john/sage-4.0.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_70[4]>\", line 1, in <module>\n        X###line 3115:\n    sage: X\n    NameError: name 'X' is not defined\n**********************************************************************\nFile \"/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py\", line 3117:\n    sage: Y\nException raised:\n    Traceback (most recent call last):\n      File \"/home/john/sage-4.0.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/john/sage-4.0.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/john/sage-4.0.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_70[5]>\", line 1, in <module>\n        Y###line 3117:\n    sage: Y\n    NameError: name 'Y' is not defined\n**********************************************************************\nFile \"/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py\", line 3122:\n    sage: q = X.parent().gen()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/john/sage-4.0.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/john/sage-4.0.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/john/sage-4.0.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_70[6]>\", line 1, in <module>\n        q = X.parent().gen()###line 3122:\n    sage: q = X.parent().gen()\n    NameError: name 'X' is not defined\n**********************************************************************\nFile \"/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py\", line 3123:\n    sage: E.defining_polynomial()(X,Y,1) + O(q^11) == 0\nException raised:\n    Traceback (most recent call last):\n      File \"/home/john/sage-4.0.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/john/sage-4.0.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/john/sage-4.0.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_70[7]>\", line 1, in <module>\n        E.defining_polynomial()(X,Y,Integer(1)) + O(q**Integer(11)) == Integer(0)###line 3123:\n    sage: E.defining_polynomial()(X,Y,1) + O(q^11) == 0\n    NameError: name 'X' is not defined\n**********************************************************************\nFile \"/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py\", line 3133:\n    sage: f/q == (X.derivative()/(2*Y+a1*X+a3))\nException raised:\n    Traceback (most recent call last):\n      File \"/home/john/sage-4.0.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/john/sage-4.0.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/john/sage-4.0.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_70[11]>\", line 1, in <module>\n        f/q == (X.derivative()/(Integer(2)*Y+a1*X+a3))###line 3133:\n    sage: f/q == (X.derivative()/(2*Y+a1*X+a3))\n    NameError: name 'X' is not defined\n**********************************************************************\n4 items had failures:\n   2 of   5 in __main__.example_114\n   2 of  11 in __main__.example_115\n   1 of   5 in __main__.example_137\n   6 of  12 in __main__.example_70\n***Test Failed*** 11 failures.\nFor whitespace errors, see the file /home/john/sage-4.0.1/tmp/.doctest_ell_rational_field.py\n\t [85.3 s]\nexit code: 1024\n```\n\n\nThis is on a 32-bit machine -- possibly the problem?\n\nNote -- I'm planning to implement a better weierstrass function, calling the pari library.  In fact I already did that, got stuck on precision problems, then deleted that branch by mistake so it is back to square one.\n\nAlso, for recognising the points, what I have always done is compute all the conjugates (not quite all, I do one from each complex conjugate pair) and then add them up (on C mod the lattice) before applying Weierstrass.  I have never tried to recognise the points as points defined over the Hilbert class field.",
    "created_at": "2009-06-14T17:58:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48057",
    "user": "https://github.com/JohnCremona"
}
```

REVIEW:  I applied this to 4.0.1, but got some doctest failures:

```
sage -t  "devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py"
**********************************************************************
File "/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 5248:
    sage: E._heegner_best_tau(-7)
Expected:
    (sqrt(7)*I - 17)/74
Got:
    1/74*sqrt(-7) - 17/74
**********************************************************************
File "/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 5250:
    sage: EllipticCurve('389a')._heegner_best_tau(-11)
Expected:
    (sqrt(11)*I - 355)/778
Got:
    1/778*sqrt(-11) - 355/778
**********************************************************************
File "/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 5291:
    sage: P = E.heegner_point(-40); P
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_115[5]>", line 1, in <module>
        P = E.heegner_point(-Integer(40)); P###line 5291:
    sage: P = E.heegner_point(-40); P
      File "/home/john/sage-4.0.1/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 5335, in heegner_point
        raise ValueError, "Not enough precision (%s) to get heegner point exactly, try passing a larger max_prec." % (prec)
    ValueError: Not enough precision (2000) to get heegner point exactly, try passing a larger max_prec.
**********************************************************************
File "/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 5301:
    sage: f = algdep(P[0], 5); f
Expected:
    x^5 + 2*x^4 + x^3 - x^2 - x - 1
Got:
    x^5 - x^4 + x^3 + x^2 - 2*x + 1
**********************************************************************
File "/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 6825:
    sage: phi(CC.0)
Expected:
    (-2.04158222510587 + 3.21664059900000e-29*I : -0.500000000000000 + 0.0906126752327350*I : 1.00000000000000)
Got:
    (287826.309565255 : -1.54417490329940e8 : 1.00000000000000)
**********************************************************************
File "/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 3114:
    sage: X,Y=E.modular_parametrization()
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_70[3]>", line 1, in <module>
        X,Y=E.modular_parametrization()###line 3114:
    sage: X,Y=E.modular_parametrization()
    TypeError: iteration over non-sequence
**********************************************************************
File "/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 3115:
    sage: X
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_70[4]>", line 1, in <module>
        X###line 3115:
    sage: X
    NameError: name 'X' is not defined
**********************************************************************
File "/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 3117:
    sage: Y
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_70[5]>", line 1, in <module>
        Y###line 3117:
    sage: Y
    NameError: name 'Y' is not defined
**********************************************************************
File "/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 3122:
    sage: q = X.parent().gen()
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_70[6]>", line 1, in <module>
        q = X.parent().gen()###line 3122:
    sage: q = X.parent().gen()
    NameError: name 'X' is not defined
**********************************************************************
File "/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 3123:
    sage: E.defining_polynomial()(X,Y,1) + O(q^11) == 0
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_70[7]>", line 1, in <module>
        E.defining_polynomial()(X,Y,Integer(1)) + O(q**Integer(11)) == Integer(0)###line 3123:
    sage: E.defining_polynomial()(X,Y,1) + O(q^11) == 0
    NameError: name 'X' is not defined
**********************************************************************
File "/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 3133:
    sage: f/q == (X.derivative()/(2*Y+a1*X+a3))
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_70[11]>", line 1, in <module>
        f/q == (X.derivative()/(Integer(2)*Y+a1*X+a3))###line 3133:
    sage: f/q == (X.derivative()/(2*Y+a1*X+a3))
    NameError: name 'X' is not defined
**********************************************************************
4 items had failures:
   2 of   5 in __main__.example_114
   2 of  11 in __main__.example_115
   1 of   5 in __main__.example_137
   6 of  12 in __main__.example_70
***Test Failed*** 11 failures.
For whitespace errors, see the file /home/john/sage-4.0.1/tmp/.doctest_ell_rational_field.py
	 [85.3 s]
exit code: 1024
```


This is on a 32-bit machine -- possibly the problem?

Note -- I'm planning to implement a better weierstrass function, calling the pari library.  In fact I already did that, got stuck on precision problems, then deleted that branch by mistake so it is back to square one.

Also, for recognising the points, what I have always done is compute all the conjugates (not quite all, I do one from each complex conjugate pair) and then add them up (on C mod the lattice) before applying Weierstrass.  I have never tried to recognise the points as points defined over the Hilbert class field.



---

archive/issue_comments_048058.json:
```json
{
    "body": "Some of these are due to new symbolics printing differently, others may be due to different choices of root (it was developed on Sage < 4.0). I'll rebase and see what's up.",
    "created_at": "2009-06-17T06:19:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48058",
    "user": "https://github.com/robertwb"
}
```

Some of these are due to new symbolics printing differently, others may be due to different choices of root (it was developed on Sage < 4.0). I'll rebase and see what's up.



---

archive/issue_comments_048059.json:
```json
{
    "body": "Attachment [6045-heegner.patch](tarball://root/attachments/some-uuid/ticket6045/6045-heegner.patch) by @robertwb created at 2009-06-23 08:58:57\n\nOK, I fixed the patch. As well as the symbolics printing changes, I had moved some doctests around and got some of them associated with the wrong output. Based on 4.0.2, ready to be looked at again.",
    "created_at": "2009-06-23T08:58:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48059",
    "user": "https://github.com/robertwb"
}
```

Attachment [6045-heegner.patch](tarball://root/attachments/some-uuid/ticket6045/6045-heegner.patch) by @robertwb created at 2009-06-23 08:58:57

OK, I fixed the patch. As well as the symbolics printing changes, I had moved some doctests around and got some of them associated with the wrong output. Based on 4.0.2, ready to be looked at again.



---

archive/issue_comments_048060.json:
```json
{
    "body": "Robert, can I suggest that we first get #6386 approved (e.g. by you reviewing it) as then your step of going from z mod period lattice to E(CC) can be done much better than your explicit use of pari/gp?  (I do use pari behind the scene of course).  I think that might be better than reviewing this now and then patching it again later.  john",
    "created_at": "2009-06-23T20:04:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48060",
    "user": "https://github.com/JohnCremona"
}
```

Robert, can I suggest that we first get #6386 approved (e.g. by you reviewing it) as then your step of going from z mod period lattice to E(CC) can be done much better than your explicit use of pari/gp?  (I do use pari behind the scene of course).  I think that might be better than reviewing this now and then patching it again later.  john



---

archive/issue_comments_048061.json:
```json
{
    "body": "That's a clever way of getting someone to review your work :). Actually, I was planning on looking at your elliptic exponential function anyways, so I'll go review that (and modify this to use it, under the very safe assumption that it's good).",
    "created_at": "2009-06-25T03:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48061",
    "user": "https://github.com/robertwb"
}
```

That's a clever way of getting someone to review your work :). Actually, I was planning on looking at your elliptic exponential function anyways, so I'll go review that (and modify this to use it, under the very safe assumption that it's good).



---

archive/issue_comments_048062.json:
```json
{
    "body": "Replying to [comment:13 robertwb]:\n> That's a clever way of getting someone to review your work :). Actually, I was planning on looking at your elliptic exponential function anyways, so I'll go review that (and modify this to use it, under the very safe assumption that it's good). \n\nI hoped you would not mind.  It was seeing that code in your patch which spurred me to get mine working properly.  It seems that for some of these wrapped functions (particularly the pari ones), there are two distinct layers:  the basic wrapper (here in gen.pyx), use of which directly requires careful study of the pari manual;  and a proper Sage function, well documented and *not* requiring any knowledge of the deeper library.",
    "created_at": "2009-06-25T08:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48062",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:13 robertwb]:
> That's a clever way of getting someone to review your work :). Actually, I was planning on looking at your elliptic exponential function anyways, so I'll go review that (and modify this to use it, under the very safe assumption that it's good). 

I hoped you would not mind.  It was seeing that code in your patch which spurred me to get mine working properly.  It seems that for some of these wrapped functions (particularly the pari ones), there are two distinct layers:  the basic wrapper (here in gen.pyx), use of which directly requires careful study of the pari manual;  and a proper Sage function, well documented and *not* requiring any knowledge of the deeper library.



---

archive/issue_comments_048063.json:
```json
{
    "body": "Depends on #6386.",
    "created_at": "2009-06-26T04:47:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48063",
    "user": "https://github.com/robertwb"
}
```

Depends on #6386.



---

archive/issue_comments_048064.json:
```json
{
    "body": "apply on top of previous",
    "created_at": "2009-06-26T06:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48064",
    "user": "https://github.com/robertwb"
}
```

apply on top of previous



---

archive/issue_comments_048065.json:
```json
{
    "body": "Attachment [6045-heegner2.patch](tarball://root/attachments/some-uuid/ticket6045/6045-heegner2.patch) by @JohnCremona created at 2009-06-28 16:29:33\n\nNB this requires #6386.  Applies fine to 4.1.alpha2 + the four patches there.  Tests in ell_rational_field pass.\n\nModular param: type \"and and\" in a comment.\n\nHeegner:  typo \"give\" -> \"given\" in 2 or 3 places in docstrings.  Why\ndo you reverse the order of summation of a_n/n?  Can you sum the\nseries using an iterator for the an instead of forming the whole list?\n\n _heegner_forms_list: (this only depends on N and D so could perhaps be\n factored out of the class to a stand-alone function).\n\nMore seriously, this function is *wrong*!  (Though in a way which does\nnot matter for the use which is made of it here so far.)  The point is\nthis:  To get a complete set of forms you need to choose *one* sqrt of\nD mod 4*N and use the same b for all the forms.  Otherwise the points\nyou get are not Galois conjugate.  [Changing b to another sqrt amounts\nto applying to the point in the upper half plane one of the\nAtkin-Lehner involutions.  This has two effects: firstly, it may\nchange the sign of the integral (depending on the A-L eigenvalue;\nsecondly, it maps \\infty to another cusp, hence adds a torsion point\nto the Heegner point.  So instead of getting come conjugate point P\nyou get either P+T or -P+T with T torsion.  The reason that this does\nnot make the rest of the code wrong here is that you only actually use\none of the forms (the one with smallest a to get best accuracy) and\nthen use algdep.  But we should have code that could in principal\ndeliver a set of Galois conjugate points.\n\nTo get around this:  try all the sqrt of D mod 4*N;  for each, try to\nfind a complete set of forms with that same b.  If that fails, either\nlook at another b, or choose a different lift of b from Z/2N to Z\n(since larger b's will give more possible forms).  I implemented this\nin gp ages ago, so I have gp code which does this!\n\nFuture work: one useful application of Heegner points is to find\nrational points on curves of rank 1.   I have been doing this\nsuccessfully for years, and in 2005 work of Delaunay and Watkins made\nit vastly more efficient.  That excellent efficient version found its\nway into Magma (thanks for Mark) and it would be good to get something\nas good in Sage.  The idea is to compute all the complex z (mod period\nlattice L) for a complete set of forms, then take the trace by adding\nthose up (as complex numbers) before mapping to the curve, at which\npoint you only need to recognise the coordinates as rational numbers.\nYou can use the action of complex conjugation on the forms to halve\nthe number of evaluations (and in each pair can choose the smallest\na).  The Delaunay-Watkins improvement allows to use even smaller a,\nand I can explain further if asked!\n\nLastly:  I tried 873b1 and D=-11, which works fine, though the point constructed has height 14.785 but the heegner_point_height function returns double that.  This might need a different ticket.",
    "created_at": "2009-06-28T16:29:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48065",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [6045-heegner2.patch](tarball://root/attachments/some-uuid/ticket6045/6045-heegner2.patch) by @JohnCremona created at 2009-06-28 16:29:33

NB this requires #6386.  Applies fine to 4.1.alpha2 + the four patches there.  Tests in ell_rational_field pass.

Modular param: type "and and" in a comment.

Heegner:  typo "give" -> "given" in 2 or 3 places in docstrings.  Why
do you reverse the order of summation of a_n/n?  Can you sum the
series using an iterator for the an instead of forming the whole list?

 _heegner_forms_list: (this only depends on N and D so could perhaps be
 factored out of the class to a stand-alone function).

More seriously, this function is *wrong*!  (Though in a way which does
not matter for the use which is made of it here so far.)  The point is
this:  To get a complete set of forms you need to choose *one* sqrt of
D mod 4*N and use the same b for all the forms.  Otherwise the points
you get are not Galois conjugate.  [Changing b to another sqrt amounts
to applying to the point in the upper half plane one of the
Atkin-Lehner involutions.  This has two effects: firstly, it may
change the sign of the integral (depending on the A-L eigenvalue;
secondly, it maps \infty to another cusp, hence adds a torsion point
to the Heegner point.  So instead of getting come conjugate point P
you get either P+T or -P+T with T torsion.  The reason that this does
not make the rest of the code wrong here is that you only actually use
one of the forms (the one with smallest a to get best accuracy) and
then use algdep.  But we should have code that could in principal
deliver a set of Galois conjugate points.

To get around this:  try all the sqrt of D mod 4*N;  for each, try to
find a complete set of forms with that same b.  If that fails, either
look at another b, or choose a different lift of b from Z/2N to Z
(since larger b's will give more possible forms).  I implemented this
in gp ages ago, so I have gp code which does this!

Future work: one useful application of Heegner points is to find
rational points on curves of rank 1.   I have been doing this
successfully for years, and in 2005 work of Delaunay and Watkins made
it vastly more efficient.  That excellent efficient version found its
way into Magma (thanks for Mark) and it would be good to get something
as good in Sage.  The idea is to compute all the complex z (mod period
lattice L) for a complete set of forms, then take the trace by adding
those up (as complex numbers) before mapping to the curve, at which
point you only need to recognise the coordinates as rational numbers.
You can use the action of complex conjugation on the forms to halve
the number of evaluations (and in each pair can choose the smallest
a).  The Delaunay-Watkins improvement allows to use even smaller a,
and I can explain further if asked!

Lastly:  I tried 873b1 and D=-11, which works fine, though the point constructed has height 14.785 but the heegner_point_height function returns double that.  This might need a different ticket.



---

archive/issue_comments_048066.json:
```json
{
    "body": "> Lastly: I tried 873b1 and D=-11, which works fine, though the point constructed \n> has height 14.785 but the heegner_point_height function returns double that. \n> This might need a different ticket. \n\nHeegner points are naturally defined over K, and the height over K is *double* the height over Q.   In general, if P in E(Q) and L is a number field, then `[L:Q]*h_Q(P) = h_L(P)`",
    "created_at": "2009-06-28T21:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48066",
    "user": "https://github.com/williamstein"
}
```

> Lastly: I tried 873b1 and D=-11, which works fine, though the point constructed 
> has height 14.785 but the heegner_point_height function returns double that. 
> This might need a different ticket. 

Heegner points are naturally defined over K, and the height over K is *double* the height over Q.   In general, if P in E(Q) and L is a number field, then `[L:Q]*h_Q(P) = h_L(P)`



---

archive/issue_comments_048067.json:
```json
{
    "body": "Replying to [comment:17 was]:\n> > Lastly: I tried 873b1 and D=-11, which works fine, though the point constructed \n> > has height 14.785 but the heegner_point_height function returns double that. \n> > This might need a different ticket. \n> \n> Heegner points are naturally defined over K, and the height over K is *double* the height over Q.   In general, if P in E(Q) and L is a number field, then `[L:Q]*h_Q(P) = h_L(P)`\n\nOK, I stand corrected!   I'm just used to computing rational Heegner points (via the trace) so that had not occurred to me.",
    "created_at": "2009-06-28T21:50:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48067",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:17 was]:
> > Lastly: I tried 873b1 and D=-11, which works fine, though the point constructed 
> > has height 14.785 but the heegner_point_height function returns double that. 
> > This might need a different ticket. 
> 
> Heegner points are naturally defined over K, and the height over K is *double* the height over Q.   In general, if P in E(Q) and L is a number field, then `[L:Q]*h_Q(P) = h_L(P)`

OK, I stand corrected!   I'm just used to computing rational Heegner points (via the trace) so that had not occurred to me.



---

archive/issue_comments_048068.json:
```json
{
    "body": "Thanks for the feedback--I'll take a look at `_heegner_forms_list`. \n\nWe're interested in computing Heegner points for rank >= 2 elliptic curves, and of course by the Gross-Zagier theorem their traces down to Q are always torsion. However, I agree it would be useful to have a \"trace\" option to trace it down (via summation in the lattice) as well.",
    "created_at": "2009-06-29T16:32:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48068",
    "user": "https://github.com/robertwb"
}
```

Thanks for the feedback--I'll take a look at `_heegner_forms_list`. 

We're interested in computing Heegner points for rank >= 2 elliptic curves, and of course by the Gross-Zagier theorem their traces down to Q are always torsion. However, I agree it would be useful to have a "trace" option to trace it down (via summation in the lattice) as well.



---

archive/issue_comments_048069.json:
```json
{
    "body": "Attachment [6045-heegner-fixes.patch](tarball://root/attachments/some-uuid/ticket6045/6045-heegner-fixes.patch) by @robertwb created at 2009-07-01 08:31:14",
    "created_at": "2009-07-01T08:31:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48069",
    "user": "https://github.com/robertwb"
}
```

Attachment [6045-heegner-fixes.patch](tarball://root/attachments/some-uuid/ticket6045/6045-heegner-fixes.patch) by @robertwb created at 2009-07-01 08:31:14



---

archive/issue_comments_048070.json:
```json
{
    "body": "Replying to [comment:16 cremona]:\n\n> Modular param: type \"and and\" in a comment.\n\nNot sure what you meant by this...\n\n> Why do you reverse the order of summation of a_n/n?  \n\nBecause there's less rounding error by starting with the tail. \n\n\n```\nsage: E = EllipticCurve('37a')\nsage: tau = E._heegner_best_tau(-7, prec=100)\nsage: r1 = sum([an/(m+1)*tau**(m+1) for m, an in enumerate(E.anlist(100))])\nsage: r2 = sum(reversed([an/(m+1)*tau**(m+1) for m, an in enumerate(E.anlist(100))]))\nsage: tau500 = E._heegner_best_tau(-7, prec=500)\nsage: r = sum([an/(m+1)*tau500**(m+1) for m, an in enumerate(E.anlist(100))])\nsage: (r1-r)\n9.8607613152626475676466070660e-32 - 3.6977854932234928378674776498e-32*I\nsage: (r2-r)\n2.4651903288156618919116517665e-32*I\n```\n\n\nNot that that's really much of a difference... \n\n> Can you sum the series using an iterator for the an instead of forming the whole list?\n\nThere's not a way to get the `a_n` as an iterator rather than a list. FYI, I do plan on optimizing this part a lot more. \n\n> \n>  _heegner_forms_list: (this only depends on N and D so could perhaps be\n>  factored out of the class to a stand-alone function).\n\nPerhaps, although I couldn't think of a better place to put it (one advantage of having it there is it's defined close to where it's used). \n\n> More seriously, this function is *wrong*!  \n\nI was thinking of this as the `H_N^D` rather than the `H_N^D(\\beta)` from Mark Watkins \"Some Remarks on Heegner Point Computations,\" though I see that it may not have been a complete set. \n\nI not make it take the chosen square root as a parameter, and it returns all the forms associated to that square root. I'm actually not using this function right now (as I only want a single surd to recover the Heegner point over the Hilbert Class Field) but it will be valuable when implementing computation of the Heegner point traced down to Q (which we should definitely have n optimized version of in Sage).",
    "created_at": "2009-07-01T08:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48070",
    "user": "https://github.com/robertwb"
}
```

Replying to [comment:16 cremona]:

> Modular param: type "and and" in a comment.

Not sure what you meant by this...

> Why do you reverse the order of summation of a_n/n?  

Because there's less rounding error by starting with the tail. 


```
sage: E = EllipticCurve('37a')
sage: tau = E._heegner_best_tau(-7, prec=100)
sage: r1 = sum([an/(m+1)*tau**(m+1) for m, an in enumerate(E.anlist(100))])
sage: r2 = sum(reversed([an/(m+1)*tau**(m+1) for m, an in enumerate(E.anlist(100))]))
sage: tau500 = E._heegner_best_tau(-7, prec=500)
sage: r = sum([an/(m+1)*tau500**(m+1) for m, an in enumerate(E.anlist(100))])
sage: (r1-r)
9.8607613152626475676466070660e-32 - 3.6977854932234928378674776498e-32*I
sage: (r2-r)
2.4651903288156618919116517665e-32*I
```


Not that that's really much of a difference... 

> Can you sum the series using an iterator for the an instead of forming the whole list?

There's not a way to get the `a_n` as an iterator rather than a list. FYI, I do plan on optimizing this part a lot more. 

> 
>  _heegner_forms_list: (this only depends on N and D so could perhaps be
>  factored out of the class to a stand-alone function).

Perhaps, although I couldn't think of a better place to put it (one advantage of having it there is it's defined close to where it's used). 

> More seriously, this function is *wrong*!  

I was thinking of this as the `H_N^D` rather than the `H_N^D(\beta)` from Mark Watkins "Some Remarks on Heegner Point Computations," though I see that it may not have been a complete set. 

I not make it take the chosen square root as a parameter, and it returns all the forms associated to that square root. I'm actually not using this function right now (as I only want a single surd to recover the Heegner point over the Hilbert Class Field) but it will be valuable when implementing computation of the Heegner point traced down to Q (which we should definitely have n optimized version of in Sage).



---

archive/issue_comments_048071.json:
```json
{
    "body": "Final review:  Sorry about the first one, I meant to say that in the comment now in line 7026 \"the the\" should be \"the\".\n\nOne small thing I found:\n\n```\nsage: E=EllipticCurve([1,0,0,-1,0]) \nsage: [E.heegner_point(D) for D in E.heegner_discriminants_list(3)]\n...\n/home/jec/sage-4.1.alpha3/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in _heegner_best_tau(self, D, prec)\n   5353         N = self.conductor()\n   5354         b = ZZ(Integers(4*N)(D).sqrt(extend=False) % (2*N))\n-> 5355         return (-b + D.sqrt(prec=prec)) / (2*N)\n   5356\n   5357     def heegner_point(self, D, prec=None, max_prec=2000):\n\nAttributeError: 'int' object has no attribute 'sqrt'\n```\n\n\nThe function  _heegner_best_tau() needs to coerce D into ZZ before calling D.sqrt().  I think some other functions might do well to make D into a ZZ as well.\n\nOtherwise I am happy.",
    "created_at": "2009-07-03T11:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48071",
    "user": "https://github.com/JohnCremona"
}
```

Final review:  Sorry about the first one, I meant to say that in the comment now in line 7026 "the the" should be "the".

One small thing I found:

```
sage: E=EllipticCurve([1,0,0,-1,0]) 
sage: [E.heegner_point(D) for D in E.heegner_discriminants_list(3)]
...
/home/jec/sage-4.1.alpha3/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in _heegner_best_tau(self, D, prec)
   5353         N = self.conductor()
   5354         b = ZZ(Integers(4*N)(D).sqrt(extend=False) % (2*N))
-> 5355         return (-b + D.sqrt(prec=prec)) / (2*N)
   5356
   5357     def heegner_point(self, D, prec=None, max_prec=2000):

AttributeError: 'int' object has no attribute 'sqrt'
```


The function  _heegner_best_tau() needs to coerce D into ZZ before calling D.sqrt().  I think some other functions might do well to make D into a ZZ as well.

Otherwise I am happy.



---

archive/issue_comments_048072.json:
```json
{
    "body": "Attachment [6045-heegner-more-fixes.patch](tarball://root/attachments/some-uuid/ticket6045/6045-heegner-more-fixes.patch) by @robertwb created at 2009-07-04 22:15:38\n\nApply all four patches.",
    "created_at": "2009-07-04T22:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48072",
    "user": "https://github.com/robertwb"
}
```

Attachment [6045-heegner-more-fixes.patch](tarball://root/attachments/some-uuid/ticket6045/6045-heegner-more-fixes.patch) by @robertwb created at 2009-07-04 22:15:38

Apply all four patches.



---

archive/issue_comments_048073.json:
```json
{
    "body": "This looks ok now.  I applied it to 4.1.alpha3 + patches from #6386.  Tests pass.  Assuming that it's still ok with rc0 this can go in now.",
    "created_at": "2009-07-09T11:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48073",
    "user": "https://github.com/JohnCremona"
}
```

This looks ok now.  I applied it to 4.1.alpha3 + patches from #6386.  Tests pass.  Assuming that it's still ok with rc0 this can go in now.



---

archive/issue_comments_048074.json:
```json
{
    "body": "I'm getting numerical noise when running all doctests:\n\n```\nsage -t -long devel/sage-exp/sage/schemes/elliptic_curves/ell_rational_field.py\n/scratch/mvngu/release/sage-4.1.1/local/lib/python/site-packages/sage/misc/misc.py:1901: DeprecationWarning: functions overriding warnings.showwarning() must support the 'line' argument\n  warn(message, DeprecationWarning, stacklevel=3)\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-exp/sage/schemes/elliptic_curves/ell_rational_field.py\", line 6989:\n    sage: phi((sqrt(7)*I - 17)/74, 53)\nExpected:\n    (-3.37746093871080e-16 - 2.21824021705058e-16*I : 3.33066907387547e-16 + 2.21719344273286e-16*I : 1.00000000000000)\nGot:\n    (-3.37704345632016e-16 - 2.21996076934245e-16*I : 3.33066907387547e-16 + 2.22044604925031e-16*I : 1.00000000000000)\n**********************************************************************\n1 items had failures:\n   1 of  11 in __main__.example_141\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_ell_rational_field.py\n\t [257.8 s]\n\n<SNIP>\n\n----------------------------------------------------------------------\n\nThe following tests failed:\n\n\tsage -t -long devel/sage-exp/sage/schemes/elliptic_curves/ell_rational_field.py # 1 doctests failed\n----------------------------------------------------------------------\nTotal time for all tests: 504.7 seconds\n```\n",
    "created_at": "2009-07-16T10:10:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48074",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I'm getting numerical noise when running all doctests:

```
sage -t -long devel/sage-exp/sage/schemes/elliptic_curves/ell_rational_field.py
/scratch/mvngu/release/sage-4.1.1/local/lib/python/site-packages/sage/misc/misc.py:1901: DeprecationWarning: functions overriding warnings.showwarning() must support the 'line' argument
  warn(message, DeprecationWarning, stacklevel=3)
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-exp/sage/schemes/elliptic_curves/ell_rational_field.py", line 6989:
    sage: phi((sqrt(7)*I - 17)/74, 53)
Expected:
    (-3.37746093871080e-16 - 2.21824021705058e-16*I : 3.33066907387547e-16 + 2.21719344273286e-16*I : 1.00000000000000)
Got:
    (-3.37704345632016e-16 - 2.21996076934245e-16*I : 3.33066907387547e-16 + 2.22044604925031e-16*I : 1.00000000000000)
**********************************************************************
1 items had failures:
   1 of  11 in __main__.example_141
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_ell_rational_field.py
	 [257.8 s]

<SNIP>

----------------------------------------------------------------------

The following tests failed:

	sage -t -long devel/sage-exp/sage/schemes/elliptic_curves/ell_rational_field.py # 1 doctests failed
----------------------------------------------------------------------
Total time for all tests: 504.7 seconds
```




---

archive/issue_comments_048075.json:
```json
{
    "body": "Attachment [6045-heegner-doctest-noise.patch](tarball://root/attachments/some-uuid/ticket6045/6045-heegner-doctest-noise.patch) by @robertwb created at 2009-07-20 15:16:36\n\nNoise issue fixed.",
    "created_at": "2009-07-20T15:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48075",
    "user": "https://github.com/robertwb"
}
```

Attachment [6045-heegner-doctest-noise.patch](tarball://root/attachments/some-uuid/ticket6045/6045-heegner-doctest-noise.patch) by @robertwb created at 2009-07-20 15:16:36

Noise issue fixed.



---

archive/issue_comments_048076.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-20T15:48:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48076",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_006300.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-07-20T15:48:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6045#event-6300"
}
```



---

archive/issue_comments_048077.json:
```json
{
    "body": "Ticket #4849 has been closed as a duplicate of this ticket.",
    "created_at": "2009-07-20T15:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6045#issuecomment-48077",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Ticket #4849 has been closed as a duplicate of this ticket.
