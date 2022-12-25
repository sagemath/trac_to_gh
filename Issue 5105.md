# Issue 5105: behaviour of the norm function in the p-adic ring

archive/issues_005105.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe p-adic norm seems to be defined differently in SAGE to the standard textbook definition, in which it is usually normalized so that $|p|=1/p$, but this is what SAGE does:\n\n```\nsage: Q11=pAdicField(11)\nsage: n=Q11(11)\nsage: n.norm()\n11 + O(11^21)\n```\n\nWould it be possible to swap it round so that the norm of 11 is given as 1/11?\n\nIssue created by migration from https://trac.sagemath.org/ticket/5105\n\n",
    "created_at": "2009-01-26T18:16:35Z",
    "labels": [
        "component: number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "behaviour of the norm function in the p-adic ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5105",
    "user": "https://trac.sagemath.org/admin/accounts/users/ljpk"
}
```
Assignee: @williamstein

The p-adic norm seems to be defined differently in SAGE to the standard textbook definition, in which it is usually normalized so that $|p|=1/p$, but this is what SAGE does:

```
sage: Q11=pAdicField(11)
sage: n=Q11(11)
sage: n.norm()
11 + O(11^21)
```

Would it be possible to swap it round so that the norm of 11 is given as 1/11?

Issue created by migration from https://trac.sagemath.org/ticket/5105





---

archive/issue_comments_038912.json:
```json
{
    "body": "3.4 is for ReST tickets only.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T23:02:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5105#issuecomment-38912",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

3.4 is for ReST tickets only.

Cheers,

Michael



---

archive/issue_comments_038913.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-02-10T18:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5105#issuecomment-38913",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_038914.json:
```json
{
    "body": "There is a confusion of terminology here.  It's the \"field norm\" that's defined for p-adics.  Thus\n\n```\nsage: Q11 = pAdicField(11, 6)\nsage: F.<a> = Q11.ext(x^2 - 2)\nsage: (2 + 3*a).norm()\n8 + 9*11 + 10*11^2 + 10*11^3 + 10*11^4 + 10*11^5 + O(11^6)\nsage: (2 + 3*a)*(2 - 3*a)\n8 + 9*11 + 10*11^2 + 10*11^3 + 10*11^4 + 10*11^5 + O(11^6)\n```\n\nSo\n\n```\nsage: Q11(22).norm()\n2*11 + O(11^7)\n```\n\nis correct, as is\n\n```\nsage: QQ(-163).norm()\n-163\n```\n\nWhat you're wanting is usually called the p-adic absolute value (it's a norm in the functional analysis sense).  It would be\ngood if one could do\n\n```\nsage: Q11(22).abs()\n```\n\nand get 1/11.  This isn't currently defined, if z is an element of a padic field, the absolute value can be obtained as\n\n```\nz.parent().prime()^(-z.ordp())\n```\n",
    "created_at": "2009-02-10T18:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5105#issuecomment-38914",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

There is a confusion of terminology here.  It's the "field norm" that's defined for p-adics.  Thus

```
sage: Q11 = pAdicField(11, 6)
sage: F.<a> = Q11.ext(x^2 - 2)
sage: (2 + 3*a).norm()
8 + 9*11 + 10*11^2 + 10*11^3 + 10*11^4 + 10*11^5 + O(11^6)
sage: (2 + 3*a)*(2 - 3*a)
8 + 9*11 + 10*11^2 + 10*11^3 + 10*11^4 + 10*11^5 + O(11^6)
```

So

```
sage: Q11(22).norm()
2*11 + O(11^7)
```

is correct, as is

```
sage: QQ(-163).norm()
-163
```

What you're wanting is usually called the p-adic absolute value (it's a norm in the functional analysis sense).  It would be
good if one could do

```
sage: Q11(22).abs()
```

and get 1/11.  This isn't currently defined, if z is an element of a padic field, the absolute value can be obtained as

```
z.parent().prime()^(-z.ordp())
```




---

archive/issue_comments_038915.json:
```json
{
    "body": "I thought this looked good, and it applied ok to 3.4.1.rc1, but I got a whole lot of doctest failures in sage/rings/padics:\n\n```\nThe following tests failed:\n\n\n        sage -t  \"devel/sage-5105/sage/rings/padics/padic_generic.py\"\n        sage -t  \"devel/sage-5105/sage/rings/padics/padic_ZZ_pX_CA_element.pyx\"\n        sage -t  \"devel/sage-5105/sage/rings/padics/padic_ZZ_pX_element.pyx\"\n        sage -t  \"devel/sage-5105/sage/rings/padics/pow_computer_ext.pyx\"\n        sage -t  \"devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx\"\n        sage -t  \"devel/sage-5105/sage/rings/padics/padic_ZZ_pX_CR_element.pyx\"\n        sage -t  \"devel/sage-5105/sage/rings/padics/padic_printing.pyx\"\n```\n\n\nMost look like this:\n\n```\nsage -t  \"devel/sage-5105/sage/rings/padics/padic_generic.py\"\n**********************************************************************\nFile \"/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_generic.py\", line 304:\n    sage: y = W.teichmuller(3); y\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jec/sage-3.4.1.rc1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/jec/sage-3.4.1.rc1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/jec/sage-3.4.1.rc1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_11[14]>\", line 1, in <module>\n        y = W.teichmuller(Integer(3)); y###line 304:\n    sage: y = W.teichmuller(3); y\n      File \"sage_object.pyx\", line 98, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1342)\n      File \"padic_generic_element.pyx\", line 212, in sage.rings.padics.padic_generic_element.pAdicGenericElement._repr_ (sage/rings/padics/padic_generic_element.c:6185)\n      File \"padic_printing.pyx\", line 373, in sage.rings.padics.padic_printing.pAdicPrinter_class.repr_gen (sage/rings/padics/padic_printing.cpp:8469)\n      File \"padic_printing.pyx\", line 460, in sage.rings.padics.padic_printing.pAdicPrinter_class._repr_gen (sage/rings/padics/padic_printing.cpp:9866)\n      File \"padic_printing.pyx\", line 580, in sage.rings.padics.padic_printing.pAdicPrinter_class._repr_spec (sage/rings/padics/padic_printing.cpp:12415)\n      File \"padic_ext_element.pyx\", line 171, in sage.rings.padics.padic_ext_element.pAdicExtElement._ext_p_list (sage/rings/padics/padic_ext_element.cpp:3643)\n      File \"padic_ext_element.pyx\", line 162, in sage.rings.padics.padic_ext_element.pAdicExtElement.ext_p_list (sage/rings/padics/padic_ext_element.cpp:3540)\n    NotImplementedError\n**********************************************************************\nFile \"/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_generic.py\", line 310:\n    sage: b = A.teichmuller(1 + 2*a - a^2); b\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jec/sage-3.4.1.rc1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/jec/sage-3.4.1.rc1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/jec/sage-3.4.1.rc1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_11[18]>\", line 1, in <module>\n        b = A.teichmuller(Integer(1) + Integer(2)*a - a**Integer(2)); b###line 310:\n    sage: b = A.teichmuller(1 + 2*a - a^2); b\n      File \"sage_object.pyx\", line 98, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1342)\n      File \"padic_generic_element.pyx\", line 212, in sage.rings.padics.padic_generic_element.pAdicGenericElement._repr_ (sage/rings/padics/padic_generic_element.c:6185)\n      File \"padic_printing.pyx\", line 373, in sage.rings.padics.padic_printing.pAdicPrinter_class.repr_gen (sage/rings/padics/padic_printing.cpp:8469)\n      File \"padic_printing.pyx\", line 460, in sage.rings.padics.padic_printing.pAdicPrinter_class._repr_gen (sage/rings/padics/padic_printing.cpp:9866)\n      File \"padic_printing.pyx\", line 580, in sage.rings.padics.padic_printing.pAdicPrinter_class._repr_spec (sage/rings/padics/padic_printing.cpp:12415)\n      File \"padic_ext_element.pyx\", line 171, in sage.rings.padics.padic_ext_element.pAdicExtElement._ext_p_list (sage/rings/padics/padic_ext_element.cpp:3643)\n      File \"padic_ext_element.pyx\", line 162, in sage.rings.padics.padic_ext_element.pAdicExtElement.ext_p_list (sage/rings/padics/padic_ext_element.cpp:3540)\n    NotImplementedError\n**********************************************************************\n1 items had failures:\n   2 of  20 in __main__.example_11\n```\n\n\nwhile there also some simpler ones:\n\n```\nFile \"/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_CR_element.pyx\", line 80:\n    sage: y.precision_relative()\nExpected:\n    20\nGot:\n    2\n**********************************************************************\nFile \"/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_CR_element.pyx\", line 82:\n    sage: y.precision_absolute()\nExpected:\n    24\nGot:\n    6\n```\n\n\nand \n\n```\nsage -t  \"devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx\"\n**********************************************************************\nFile \"/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx\", line 1214:\n    sage: ((1+2*w)^5).norm()\nExpected:\n    1 + 5^2 + O(5^5)\nGot:\n    1 + O(5^2)\n**********************************************************************\nFile \"/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx\", line 1216:\n    sage: ((1+2*w)).norm()^5\nExpected:\n    1 + 5^2 + O(5^5)\nGot:\n    1 + O(5^2)\n**********************************************************************\nFile \"/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx\", line 1246:\n    sage: a.trace()\nExpected:\n    3*5 + 2*5^2 + 3*5^3 + 2*5^4 + O(5^5)\nGot:\n    O(5)\n**********************************************************************\nFile \"/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx\", line 1248:\n    sage: a.trace() + b.trace()\nExpected:\n    4*5 + 5^2 + 5^3 + 2*5^4 + O(5^5)\nGot:\n    O(5)\n**********************************************************************\nFile \"/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx\", line 1250:\n    sage: (a+b).trace()\nExpected:\n    4*5 + 5^2 + 5^3 + 2*5^4 + O(5^5)\nGot:\n    O(5)\n**********************************************************************\nFile \"/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx\", line 1277:\n    sage: c._ntl_rep()\nExpected:\n    [89 9 4 1]\nGot:\n    [4 4 4]\n**********************************************************************\n3 items had failures:\n   2 of   8 in __main__.example_29\n   3 of  11 in __main__.example_30\n   1 of   8 in __main__.example_31\n***Test Failed*** 6 failures.\nFor whitespace errors, see the file /home/jec/sage-3.4.1.rc1/tmp/.doctest_padic_ZZ_pX_FM_element.py\n         [1.4 s]\n```\n\n\nI have absolutely no idea what in the patch has caused this, but it needs to be looked at!",
    "created_at": "2009-04-09T16:07:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5105#issuecomment-38915",
    "user": "https://github.com/JohnCremona"
}
```

I thought this looked good, and it applied ok to 3.4.1.rc1, but I got a whole lot of doctest failures in sage/rings/padics:

```
The following tests failed:


        sage -t  "devel/sage-5105/sage/rings/padics/padic_generic.py"
        sage -t  "devel/sage-5105/sage/rings/padics/padic_ZZ_pX_CA_element.pyx"
        sage -t  "devel/sage-5105/sage/rings/padics/padic_ZZ_pX_element.pyx"
        sage -t  "devel/sage-5105/sage/rings/padics/pow_computer_ext.pyx"
        sage -t  "devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx"
        sage -t  "devel/sage-5105/sage/rings/padics/padic_ZZ_pX_CR_element.pyx"
        sage -t  "devel/sage-5105/sage/rings/padics/padic_printing.pyx"
```


Most look like this:

```
sage -t  "devel/sage-5105/sage/rings/padics/padic_generic.py"
**********************************************************************
File "/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_generic.py", line 304:
    sage: y = W.teichmuller(3); y
Exception raised:
    Traceback (most recent call last):
      File "/home/jec/sage-3.4.1.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jec/sage-3.4.1.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jec/sage-3.4.1.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_11[14]>", line 1, in <module>
        y = W.teichmuller(Integer(3)); y###line 304:
    sage: y = W.teichmuller(3); y
      File "sage_object.pyx", line 98, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1342)
      File "padic_generic_element.pyx", line 212, in sage.rings.padics.padic_generic_element.pAdicGenericElement._repr_ (sage/rings/padics/padic_generic_element.c:6185)
      File "padic_printing.pyx", line 373, in sage.rings.padics.padic_printing.pAdicPrinter_class.repr_gen (sage/rings/padics/padic_printing.cpp:8469)
      File "padic_printing.pyx", line 460, in sage.rings.padics.padic_printing.pAdicPrinter_class._repr_gen (sage/rings/padics/padic_printing.cpp:9866)
      File "padic_printing.pyx", line 580, in sage.rings.padics.padic_printing.pAdicPrinter_class._repr_spec (sage/rings/padics/padic_printing.cpp:12415)
      File "padic_ext_element.pyx", line 171, in sage.rings.padics.padic_ext_element.pAdicExtElement._ext_p_list (sage/rings/padics/padic_ext_element.cpp:3643)
      File "padic_ext_element.pyx", line 162, in sage.rings.padics.padic_ext_element.pAdicExtElement.ext_p_list (sage/rings/padics/padic_ext_element.cpp:3540)
    NotImplementedError
**********************************************************************
File "/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_generic.py", line 310:
    sage: b = A.teichmuller(1 + 2*a - a^2); b
Exception raised:
    Traceback (most recent call last):
      File "/home/jec/sage-3.4.1.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jec/sage-3.4.1.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jec/sage-3.4.1.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_11[18]>", line 1, in <module>
        b = A.teichmuller(Integer(1) + Integer(2)*a - a**Integer(2)); b###line 310:
    sage: b = A.teichmuller(1 + 2*a - a^2); b
      File "sage_object.pyx", line 98, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1342)
      File "padic_generic_element.pyx", line 212, in sage.rings.padics.padic_generic_element.pAdicGenericElement._repr_ (sage/rings/padics/padic_generic_element.c:6185)
      File "padic_printing.pyx", line 373, in sage.rings.padics.padic_printing.pAdicPrinter_class.repr_gen (sage/rings/padics/padic_printing.cpp:8469)
      File "padic_printing.pyx", line 460, in sage.rings.padics.padic_printing.pAdicPrinter_class._repr_gen (sage/rings/padics/padic_printing.cpp:9866)
      File "padic_printing.pyx", line 580, in sage.rings.padics.padic_printing.pAdicPrinter_class._repr_spec (sage/rings/padics/padic_printing.cpp:12415)
      File "padic_ext_element.pyx", line 171, in sage.rings.padics.padic_ext_element.pAdicExtElement._ext_p_list (sage/rings/padics/padic_ext_element.cpp:3643)
      File "padic_ext_element.pyx", line 162, in sage.rings.padics.padic_ext_element.pAdicExtElement.ext_p_list (sage/rings/padics/padic_ext_element.cpp:3540)
    NotImplementedError
**********************************************************************
1 items had failures:
   2 of  20 in __main__.example_11
```


while there also some simpler ones:

```
File "/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_CR_element.pyx", line 80:
    sage: y.precision_relative()
Expected:
    20
Got:
    2
**********************************************************************
File "/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_CR_element.pyx", line 82:
    sage: y.precision_absolute()
Expected:
    24
Got:
    6
```


and 

```
sage -t  "devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx"
**********************************************************************
File "/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx", line 1214:
    sage: ((1+2*w)^5).norm()
Expected:
    1 + 5^2 + O(5^5)
Got:
    1 + O(5^2)
**********************************************************************
File "/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx", line 1216:
    sage: ((1+2*w)).norm()^5
Expected:
    1 + 5^2 + O(5^5)
Got:
    1 + O(5^2)
**********************************************************************
File "/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx", line 1246:
    sage: a.trace()
Expected:
    3*5 + 2*5^2 + 3*5^3 + 2*5^4 + O(5^5)
Got:
    O(5)
**********************************************************************
File "/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx", line 1248:
    sage: a.trace() + b.trace()
Expected:
    4*5 + 5^2 + 5^3 + 2*5^4 + O(5^5)
Got:
    O(5)
**********************************************************************
File "/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx", line 1250:
    sage: (a+b).trace()
Expected:
    4*5 + 5^2 + 5^3 + 2*5^4 + O(5^5)
Got:
    O(5)
**********************************************************************
File "/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx", line 1277:
    sage: c._ntl_rep()
Expected:
    [89 9 4 1]
Got:
    [4 4 4]
**********************************************************************
3 items had failures:
   2 of   8 in __main__.example_29
   3 of  11 in __main__.example_30
   1 of   8 in __main__.example_31
***Test Failed*** 6 failures.
For whitespace errors, see the file /home/jec/sage-3.4.1.rc1/tmp/.doctest_padic_ZZ_pX_FM_element.py
         [1.4 s]
```


I have absolutely no idea what in the patch has caused this, but it needs to be looked at!



---

archive/issue_comments_038916.json:
```json
{
    "body": "Changing assignee from @williamstein to @roed314.",
    "created_at": "2009-04-26T19:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5105#issuecomment-38916",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to @roed314.



---

archive/issue_comments_038917.json:
```json
{
    "body": "Changing component from number theory to padics.",
    "created_at": "2009-04-26T19:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5105#issuecomment-38917",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from number theory to padics.



---

archive/issue_comments_038918.json:
```json
{
    "body": "I guess this is reviewed by #5778 and the issues reported here due to doctest failures have been fixed there.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T09:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5105#issuecomment-38918",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I guess this is reviewed by #5778 and the issues reported here due to doctest failures have been fixed there.

Cheers,

Michael



---

archive/issue_comments_038919.json:
```json
{
    "body": "Implements abs() and exlains the difference between it and norm()",
    "created_at": "2009-05-11T10:10:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5105#issuecomment-38919",
    "user": "https://github.com/roed314"
}
```

Implements abs() and exlains the difference between it and norm()



---

archive/issue_comments_038920.json:
```json
{
    "body": "Attachment [trac_5105.patch](tarball://root/attachments/some-uuid/ticket5105/trac_5105.patch) by mabshoff created at 2009-05-11 10:33:04\n\nPositive review due to #5778 - credit goes to RobertWB.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T10:33:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5105#issuecomment-38920",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5105.patch](tarball://root/attachments/some-uuid/ticket5105/trac_5105.patch) by mabshoff created at 2009-05-11 10:33:04

Positive review due to #5778 - credit goes to RobertWB.

Cheers,

Michael



---

archive/issue_comments_038921.json:
```json
{
    "body": "Merged in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T10:33:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5105#issuecomment-38921",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_events_005353.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-05-11T10:33:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5105",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5105#event-5353"
}
```



---

archive/issue_comments_038922.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-11T10:33:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5105#issuecomment-38922",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
