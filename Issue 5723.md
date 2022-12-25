# Issue 5723: sage new symbolics/pynac misbehave when evaluating with CDF elements

archive/issues_005723.json:
```json
{
    "body": "Keywords: sage symbolics pynac evaluating n CDF\n\n\n```\nsage: u0 = var('u0', ns=1)\nsage: sage.symbolic.function.function('f')(u0).subs(u0=CDF.0).n()\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/ncalexan/.sage/temp/pv139196.reshsg.uci.edu/33117/_Users_ncalexan_sage_3_4_rc0_devel_sage_sage_symbolic_test_sage_23.py in <module>()\n\n/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:6498)()\n\n/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/symbolic/pynac.so in sage.symbolic.pynac.py_float (sage/symbolic/pynac.cpp:3959)()\n\n/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/rings/complex_double.so in sage.rings.complex_double.ComplexDoubleElement.__float__ (sage/rings/complex_double.c:5799)()\n\nTypeError: can't convert complex to float; use abs(z)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5723\n\n",
    "created_at": "2009-04-09T03:10:51Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage new symbolics/pynac misbehave when evaluating with CDF elements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5723",
    "user": "https://github.com/ncalexan"
}
```
Keywords: sage symbolics pynac evaluating n CDF


```
sage: u0 = var('u0', ns=1)
sage: sage.symbolic.function.function('f')(u0).subs(u0=CDF.0).n()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/ncalexan/.sage/temp/pv139196.reshsg.uci.edu/33117/_Users_ncalexan_sage_3_4_rc0_devel_sage_sage_symbolic_test_sage_23.py in <module>()

/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:6498)()

/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/symbolic/pynac.so in sage.symbolic.pynac.py_float (sage/symbolic/pynac.cpp:3959)()

/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/rings/complex_double.so in sage.rings.complex_double.ComplexDoubleElement.__float__ (sage/rings/complex_double.c:5799)()

TypeError: can't convert complex to float; use abs(z)
```


Issue created by migration from https://trac.sagemath.org/ticket/5723





---

archive/issue_comments_044634.json:
```json
{
    "body": "add doctest",
    "created_at": "2009-04-13T16:12:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5723#issuecomment-44634",
    "user": "https://github.com/burcin"
}
```

add doctest



---

archive/issue_comments_044635.json:
```json
{
    "body": "Attachment [trac_5723.patch](tarball://root/attachments/some-uuid/ticket5723/trac_5723.patch) by @burcin created at 2009-04-13 16:14:55\n\nThis is fixed with the changes in #5777, attached patch adds the doctest to sage/symbolic/function.pyx.",
    "created_at": "2009-04-13T16:14:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5723#issuecomment-44635",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_5723.patch](tarball://root/attachments/some-uuid/ticket5723/trac_5723.patch) by @burcin created at 2009-04-13 16:14:55

This is fixed with the changes in #5777, attached patch adds the doctest to sage/symbolic/function.pyx.



---

archive/issue_comments_044636.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-13T16:14:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5723#issuecomment-44636",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_044637.json:
```json
{
    "body": "Set assignee to @burcin.",
    "created_at": "2009-04-13T16:14:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5723#issuecomment-44637",
    "user": "https://github.com/burcin"
}
```

Set assignee to @burcin.



---

archive/issue_comments_044638.json:
```json
{
    "body": "I get a failure for this doctest in 4.0.  Burcin, could you look at this again?\n\n\n```\nsage -t  \"devel/sage-main/sage/symbolic/function.pyx\"       \n**********************************************************************\nFile \"/home/jason/sage/devel/sage-main/sage/symbolic/function.pyx\", line 19:\n    sage: sage.symbolic.function.function('f')(u0).subs(u0=CDF.0).n()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jason/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/jason/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/jason/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[3]>\", line 1, in <module>\n        sage.symbolic.function.function('f')(u0).subs(u0=CDF.gen(0)).n()###line 19:\n    sage: sage.symbolic.function.function('f')(u0).subs(u0=CDF.0).n()\n      File \"expression.pyx\", line 3211, in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:15832)\n        x = new_Expression_from_GEx(self._parent, self._gobj.evalf(0, prec)).pyobject()\n      File \"expression.pyx\", line 199, in sage.symbolic.expression.Expression.pyobject (sage/symbolic/expression.cpp:2637)\n        raise TypeError, \"self must be a numeric expression\"\n    TypeError: self must be a numeric expression\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/jason/sage/tmp/.doctest_function.py\n\t [2.0 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t  \"devel/sage-main/sage/symbolic/function.pyx\"\nTotal time for all tests: 2.0 seconds\n```\n",
    "created_at": "2009-05-30T07:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5723#issuecomment-44638",
    "user": "https://github.com/jasongrout"
}
```

I get a failure for this doctest in 4.0.  Burcin, could you look at this again?


```
sage -t  "devel/sage-main/sage/symbolic/function.pyx"       
**********************************************************************
File "/home/jason/sage/devel/sage-main/sage/symbolic/function.pyx", line 19:
    sage: sage.symbolic.function.function('f')(u0).subs(u0=CDF.0).n()
Exception raised:
    Traceback (most recent call last):
      File "/home/jason/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jason/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jason/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[3]>", line 1, in <module>
        sage.symbolic.function.function('f')(u0).subs(u0=CDF.gen(0)).n()###line 19:
    sage: sage.symbolic.function.function('f')(u0).subs(u0=CDF.0).n()
      File "expression.pyx", line 3211, in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:15832)
        x = new_Expression_from_GEx(self._parent, self._gobj.evalf(0, prec)).pyobject()
      File "expression.pyx", line 199, in sage.symbolic.expression.Expression.pyobject (sage/symbolic/expression.cpp:2637)
        raise TypeError, "self must be a numeric expression"
    TypeError: self must be a numeric expression
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/jason/sage/tmp/.doctest_function.py
	 [2.0 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage-main/sage/symbolic/function.pyx"
Total time for all tests: 2.0 seconds
```




---

archive/issue_comments_044639.json:
```json
{
    "body": "Wait.  \n\n```\nsage: u0 = var('u0', ns=1)\nsage: sage.symbolic.function.function('f')(u0).subs(u0=CDF.0).n()\n```\n\nWhy should the last line ever work?  You're taking f(I) for formal f and asking to give back a specific number.  That *should* always result in an error.  This ticket looks invalid to me.",
    "created_at": "2009-05-30T13:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5723#issuecomment-44639",
    "user": "https://github.com/williamstein"
}
```

Wait.  

```
sage: u0 = var('u0', ns=1)
sage: sage.symbolic.function.function('f')(u0).subs(u0=CDF.0).n()
```

Why should the last line ever work?  You're taking f(I) for formal f and asking to give back a specific number.  That *should* always result in an error.  This ticket looks invalid to me.



---

archive/issue_comments_044640.json:
```json
{
    "body": "This now gives\n\n\n```\nsage: function('f')(u0).subs(u0=CDF.0).n()\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/mhansen/.sage/temp/sage.math.washington.edu/3525/_home_mhansen__sage_init_sage_0.py in <module>()\n\n/scratch/mhansen/release/4.0.1/rc1/sage-4.0.1.rc1/local/lib/python2.5/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:15832)()\n\n/scratch/mhansen/release/4.0.1/rc1/sage-4.0.1.rc1/local/lib/python2.5/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.pyobject (sage/symbolic/expression.cpp:2637)()\n\nTypeError: self must be a numeric expression\n```\n\n\nNick, do you think we can close this?",
    "created_at": "2009-06-05T02:33:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5723#issuecomment-44640",
    "user": "https://github.com/mwhansen"
}
```

This now gives


```
sage: function('f')(u0).subs(u0=CDF.0).n()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/mhansen/.sage/temp/sage.math.washington.edu/3525/_home_mhansen__sage_init_sage_0.py in <module>()

/scratch/mhansen/release/4.0.1/rc1/sage-4.0.1.rc1/local/lib/python2.5/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:15832)()

/scratch/mhansen/release/4.0.1/rc1/sage-4.0.1.rc1/local/lib/python2.5/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.pyobject (sage/symbolic/expression.cpp:2637)()

TypeError: self must be a numeric expression
```


Nick, do you think we can close this?



---

archive/issue_comments_044641.json:
```json
{
    "body": "Fine by me.",
    "created_at": "2009-06-05T02:43:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5723#issuecomment-44641",
    "user": "https://github.com/ncalexan"
}
```

Fine by me.



---

archive/issue_comments_044642.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-06-05T02:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5723#issuecomment-44642",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_events_005967.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-06-05T02:49:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5723",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5723#event-5967"
}
```
