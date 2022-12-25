# Issue 2796: Integer digits/ndigit disagree on default base

archive/issues_002796.json:
```json
{
    "body": "Assignee: somebody\n\nI find this quite non-intuitive:\n\n```\nsage: n=15\nsage: n.digits()\n[1, 1, 1, 1]\nsage: n.ndigits()\n2\nsage: n.bits()\n4\n```\n\nThe reason is that digits and ndigits have a different default for the base parameter.  I think they should both default to base=10.\n\nI also think that 'bits' should be renamed to 'nbits' and possibly the 'bits' method should call 'digits(base=2)'.  I enter this with-out a patch for the moment because I wanted some feedback before I submit a patch which could break user code.  Please vote in this ticket.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2796\n\n",
    "created_at": "2008-04-04T12:56:01Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "Integer digits/ndigit disagree on default base",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2796",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```
Assignee: somebody

I find this quite non-intuitive:

```
sage: n=15
sage: n.digits()
[1, 1, 1, 1]
sage: n.ndigits()
2
sage: n.bits()
4
```

The reason is that digits and ndigits have a different default for the base parameter.  I think they should both default to base=10.

I also think that 'bits' should be renamed to 'nbits' and possibly the 'bits' method should call 'digits(base=2)'.  I enter this with-out a patch for the moment because I wanted some feedback before I submit a patch which could break user code.  Please vote in this ticket.

Issue created by migration from https://trac.sagemath.org/ticket/2796





---

archive/issue_comments_019156.json:
```json
{
    "body": "Attachment [trac_2796.patch](tarball://root/attachments/some-uuid/ticket2796/trac_2796.patch) by @zimmermann6 created at 2008-10-19 13:10:18\n\nthe attached patch changes the default base to 10 for digits, so that digits and ndigits agree:\n\n```\nsage: n=15\nsage: n.digits()\n[5, 1]\nsage: n.ndigits()\n2\n```\nAs a consequence, calls to digits() were changed into digits(2).",
    "created_at": "2008-10-19T13:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2796#issuecomment-19156",
    "user": "https://github.com/zimmermann6"
}
```

Attachment [trac_2796.patch](tarball://root/attachments/some-uuid/ticket2796/trac_2796.patch) by @zimmermann6 created at 2008-10-19 13:10:18

the attached patch changes the default base to 10 for digits, so that digits and ndigits agree:

```
sage: n=15
sage: n.digits()
[5, 1]
sage: n.ndigits()
2
```
As a consequence, calls to digits() were changed into digits(2).



---

archive/issue_comments_019157.json:
```json
{
    "body": "I like this as far as it goes, but would also like n.bits() to return n.digits(2) and n.nbits() to return what n.bits() currently does.  Can we add that too?",
    "created_at": "2008-10-21T20:17:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2796#issuecomment-19157",
    "user": "https://github.com/JohnCremona"
}
```

I like this as far as it goes, but would also like n.bits() to return n.digits(2) and n.nbits() to return what n.bits() currently does.  Can we add that too?



---

archive/issue_comments_019158.json:
```json
{
    "body": "Attachment [trac_2796a.patch](tarball://root/attachments/some-uuid/ticket2796/trac_2796a.patch) by @zimmermann6 created at 2008-10-23 06:50:20\n\nReplying to [comment:2 cremona]:\n> I like this as far as it goes, but would also like n.bits() to return n.digits(2) and n.nbits() to return what n.bits() currently does.  Can we add that too?\n\n\nThe second patch (to be applied after the 1st one) does this. sage -t -long * returned the following failures,\nbut I guess they are related to another patch. In any case the reviewer should check them before and after applying\nthe 2nd patch:\n\n```\n      sage -t -long devel/sage-main/sage/modular/modform/j_invariant.py\n      sage -t -long devel/sage-main/sage/schemes/elliptic_curves/padics.py\n      sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_generic.py\n```",
    "created_at": "2008-10-23T06:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2796#issuecomment-19158",
    "user": "https://github.com/zimmermann6"
}
```

Attachment [trac_2796a.patch](tarball://root/attachments/some-uuid/ticket2796/trac_2796a.patch) by @zimmermann6 created at 2008-10-23 06:50:20

Replying to [comment:2 cremona]:
> I like this as far as it goes, but would also like n.bits() to return n.digits(2) and n.nbits() to return what n.bits() currently does.  Can we add that too?


The second patch (to be applied after the 1st one) does this. sage -t -long * returned the following failures,
but I guess they are related to another patch. In any case the reviewer should check them before and after applying
the 2nd patch:

```
      sage -t -long devel/sage-main/sage/modular/modform/j_invariant.py
      sage -t -long devel/sage-main/sage/schemes/elliptic_curves/padics.py
      sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_generic.py
```



---

archive/issue_comments_019159.json:
```json
{
    "body": "Looks good to me, and I think this is a good change too. \n\nI didn't get those modular/elliptic curve errors, so it must be due to something else.",
    "created_at": "2008-11-14T01:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2796#issuecomment-19159",
    "user": "https://github.com/robertwb"
}
```

Looks good to me, and I think this is a good change too. 

I didn't get those modular/elliptic curve errors, so it must be due to something else.



---

archive/issue_comments_019160.json:
```json
{
    "body": "The two patches here cause the following failures:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.rc1$ ./sage -t -long devel/sage/sage/symbolic/expression.pyx\nsage -t -long devel/sage/sage/symbolic/expression.pyx       \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/sage/sage/symbolic/expression.pyx\", line 1269:\n    sage: (x^3 - 1).gcd(x-1)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_38[4]>\", line 1, in <module>\n        (x**Integer(3) - Integer(1)).gcd(x-Integer(1))###line 1269:\n    sage: (x^3 - 1).gcd(x-1)\n      File \"expression.pyx\", line 1286, in sage.symbolic.expression.Expression.gcd (sage/symbolic/expression.cpp:5544)\n      File \"pynac.pyx\", line 575, in sage.symbolic.pynac.py_int_length (sage/symbolic/pynac.cpp:7102)\n    TypeError: an integer is required\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/sage/sage/symbolic/expression.pyx\", line 1271:\n    sage: (x^3 - 1).gcd(x^2+x+1)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_38[5]>\", line 1, in <module>\n        (x**Integer(3) - Integer(1)).gcd(x**Integer(2)+x+Integer(1))###line 1271:\n    sage: (x^3 - 1).gcd(x^2+x+1)\n      File \"expression.pyx\", line 1286, in sage.symbolic.expression.Expression.gcd (sage/symbolic/expression.cpp:5544)\n      File \"pynac.pyx\", line 575, in sage.symbolic.pynac.py_int_length (sage/symbolic/pynac.cpp:7102)\n    TypeError: an integer is required\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/sage/sage/symbolic/expression.pyx\", line 1277:\n    sage: gcd(x^3 - y^3, x-y)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_38[7]>\", line 1, in <module>\n        gcd(x**Integer(3) - y**Integer(3), x-y)###line 1277:\n    sage: gcd(x^3 - y^3, x-y)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/lib/python2.5/site-packages/sage/rings/arith.py\", line 1037, in gcd\n        return a.gcd(b, **kwargs)\n      File \"expression.pyx\", line 1286, in sage.symbolic.expression.Expression.gcd (sage/symbolic/expression.cpp:5544)\n      File \"pynac.pyx\", line 575, in sage.symbolic.pynac.py_int_length (sage/symbolic/pynac.cpp:7102)\n    TypeError: an integer is required\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/sage/sage/symbolic/expression.pyx\", line 1279:\n    sage: gcd(x^100-y^100, x^10-y^10)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_38[8]>\", line 1, in <module>\n        gcd(x**Integer(100)-y**Integer(100), x**Integer(10)-y**Integer(10))###line 1279:\n    sage: gcd(x^100-y^100, x^10-y^10)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/lib/python2.5/site-packages/sage/rings/arith.py\", line 1037, in gcd\n        return a.gcd(b, **kwargs)\n      File \"expression.pyx\", line 1286, in sage.symbolic.expression.Expression.gcd (sage/symbolic/expression.cpp:5544)\n      File \"pynac.pyx\", line 575, in sage.symbolic.pynac.py_int_length (sage/symbolic/pynac.cpp:7102)\n    TypeError: an integer is required\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/sage/sage/symbolic/expression.pyx\", line 1281:\n    sage: gcd(expand( (x^2+17*x+3/7*y)*(x^5 - 17*y + 2/3) ), expand((x^13+17*x+3/7*y)*(x^5 - 17*y + 2/3)) )\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_38[9]>\", line 1, in <module>\n        gcd(expand( (x**Integer(2)+Integer(17)*x+Integer(3)/Integer(7)*y)*(x**Integer(5) - Integer(17)*y + Integer(2)/Integer(3)) ), expand((x**Integer(13)+Integer(17)*x+Integer(3)/Integer(7)*y)*(x**Integer(5) - Integer(17)*y + Integer(2)/Integer(3))) )###line 1281:\n    sage: gcd(expand( (x^2+17*x+3/7*y)*(x^5 - 17*y + 2/3) ), expand((x^13+17*x+3/7*y)*(x^5 - 17*y + 2/3)) )\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/lib/python2.5/site-packages/sage/rings/arith.py\", line 1037, in gcd\n        return a.gcd(b, **kwargs)\n      File \"expression.pyx\", line 1286, in sage.symbolic.expression.Expression.gcd (sage/symbolic/expression.cpp:5544)\n      File \"pynac.pyx\", line 575, in sage.symbolic.pynac.py_int_length (sage/symbolic/pynac.cpp:7102)\n    TypeError: an integer is required\n**********************************************************************\n1 items had failures:\n   5 of  10 in __main__.example_38\n***Test Failed*** 5 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.rc1/tmp/.doctest_expression.py\n\t [10.3 s]\nexit code: 1024\n \n----------------------------------------------------------------------\n```",
    "created_at": "2008-11-14T05:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2796#issuecomment-19160",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The two patches here cause the following failures:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.rc1$ ./sage -t -long devel/sage/sage/symbolic/expression.pyx
sage -t -long devel/sage/sage/symbolic/expression.pyx       
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/sage/sage/symbolic/expression.pyx", line 1269:
    sage: (x^3 - 1).gcd(x-1)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_38[4]>", line 1, in <module>
        (x**Integer(3) - Integer(1)).gcd(x-Integer(1))###line 1269:
    sage: (x^3 - 1).gcd(x-1)
      File "expression.pyx", line 1286, in sage.symbolic.expression.Expression.gcd (sage/symbolic/expression.cpp:5544)
      File "pynac.pyx", line 575, in sage.symbolic.pynac.py_int_length (sage/symbolic/pynac.cpp:7102)
    TypeError: an integer is required
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/sage/sage/symbolic/expression.pyx", line 1271:
    sage: (x^3 - 1).gcd(x^2+x+1)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_38[5]>", line 1, in <module>
        (x**Integer(3) - Integer(1)).gcd(x**Integer(2)+x+Integer(1))###line 1271:
    sage: (x^3 - 1).gcd(x^2+x+1)
      File "expression.pyx", line 1286, in sage.symbolic.expression.Expression.gcd (sage/symbolic/expression.cpp:5544)
      File "pynac.pyx", line 575, in sage.symbolic.pynac.py_int_length (sage/symbolic/pynac.cpp:7102)
    TypeError: an integer is required
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/sage/sage/symbolic/expression.pyx", line 1277:
    sage: gcd(x^3 - y^3, x-y)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_38[7]>", line 1, in <module>
        gcd(x**Integer(3) - y**Integer(3), x-y)###line 1277:
    sage: gcd(x^3 - y^3, x-y)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/lib/python2.5/site-packages/sage/rings/arith.py", line 1037, in gcd
        return a.gcd(b, **kwargs)
      File "expression.pyx", line 1286, in sage.symbolic.expression.Expression.gcd (sage/symbolic/expression.cpp:5544)
      File "pynac.pyx", line 575, in sage.symbolic.pynac.py_int_length (sage/symbolic/pynac.cpp:7102)
    TypeError: an integer is required
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/sage/sage/symbolic/expression.pyx", line 1279:
    sage: gcd(x^100-y^100, x^10-y^10)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_38[8]>", line 1, in <module>
        gcd(x**Integer(100)-y**Integer(100), x**Integer(10)-y**Integer(10))###line 1279:
    sage: gcd(x^100-y^100, x^10-y^10)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/lib/python2.5/site-packages/sage/rings/arith.py", line 1037, in gcd
        return a.gcd(b, **kwargs)
      File "expression.pyx", line 1286, in sage.symbolic.expression.Expression.gcd (sage/symbolic/expression.cpp:5544)
      File "pynac.pyx", line 575, in sage.symbolic.pynac.py_int_length (sage/symbolic/pynac.cpp:7102)
    TypeError: an integer is required
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/sage/sage/symbolic/expression.pyx", line 1281:
    sage: gcd(expand( (x^2+17*x+3/7*y)*(x^5 - 17*y + 2/3) ), expand((x^13+17*x+3/7*y)*(x^5 - 17*y + 2/3)) )
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_38[9]>", line 1, in <module>
        gcd(expand( (x**Integer(2)+Integer(17)*x+Integer(3)/Integer(7)*y)*(x**Integer(5) - Integer(17)*y + Integer(2)/Integer(3)) ), expand((x**Integer(13)+Integer(17)*x+Integer(3)/Integer(7)*y)*(x**Integer(5) - Integer(17)*y + Integer(2)/Integer(3))) )###line 1281:
    sage: gcd(expand( (x^2+17*x+3/7*y)*(x^5 - 17*y + 2/3) ), expand((x^13+17*x+3/7*y)*(x^5 - 17*y + 2/3)) )
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/lib/python2.5/site-packages/sage/rings/arith.py", line 1037, in gcd
        return a.gcd(b, **kwargs)
      File "expression.pyx", line 1286, in sage.symbolic.expression.Expression.gcd (sage/symbolic/expression.cpp:5544)
      File "pynac.pyx", line 575, in sage.symbolic.pynac.py_int_length (sage/symbolic/pynac.cpp:7102)
    TypeError: an integer is required
**********************************************************************
1 items had failures:
   5 of  10 in __main__.example_38
***Test Failed*** 5 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.rc1/tmp/.doctest_expression.py
	 [10.3 s]
exit code: 1024
 
----------------------------------------------------------------------
```



---

archive/issue_comments_019161.json:
```json
{
    "body": "Hmm... this seems totally unrelated to the ticket. Given 3.2 is out soon, I'll see again if there's any interaction with the symbolic code.",
    "created_at": "2008-11-14T06:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2796#issuecomment-19161",
    "user": "https://github.com/robertwb"
}
```

Hmm... this seems totally unrelated to the ticket. Given 3.2 is out soon, I'll see again if there's any interaction with the symbolic code.



---

archive/issue_comments_019162.json:
```json
{
    "body": "Attachment [trac_2796b.patch](tarball://root/attachments/some-uuid/ticket2796/trac_2796b.patch) by @aghitza created at 2008-12-11 11:35:28\n\napply after the previous two patches",
    "created_at": "2008-12-11T11:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2796#issuecomment-19162",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_2796b.patch](tarball://root/attachments/some-uuid/ticket2796/trac_2796b.patch) by @aghitza created at 2008-12-11 11:35:28

apply after the previous two patches



---

archive/issue_comments_019163.json:
```json
{
    "body": "Ah yes, my shortest patch to date.  Apply trac_2796b.patch after the other two to fix the symbolic/expression.pyx failure.\n\nIt is of course trivial, yet it took about half an hour to find...\n\nThe first two patches look good to me, otherwise.",
    "created_at": "2008-12-11T11:37:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2796#issuecomment-19163",
    "user": "https://github.com/aghitza"
}
```

Ah yes, my shortest patch to date.  Apply trac_2796b.patch after the other two to fix the symbolic/expression.pyx failure.

It is of course trivial, yet it took about half an hour to find...

The first two patches look good to me, otherwise.



---

archive/issue_comments_019164.json:
```json
{
    "body": "Looks like that fixed it. Positive review on all three patches.",
    "created_at": "2008-12-12T01:37:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2796#issuecomment-19164",
    "user": "https://github.com/robertwb"
}
```

Looks like that fixed it. Positive review on all three patches.



---

archive/issue_comments_019165.json:
```json
{
    "body": "Indeed. I have checked the first three tests and the last one, and all four pass now.",
    "created_at": "2008-12-12T07:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2796#issuecomment-19165",
    "user": "https://github.com/zimmermann6"
}
```

Indeed. I have checked the first three tests and the last one, and all four pass now.



---

archive/issue_comments_019166.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-12T13:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2796#issuecomment-19166",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006452.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-12T13:48:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2796",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2796#event-6452"
}
```



---

archive/issue_comments_019167.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha2",
    "created_at": "2008-12-12T13:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2796",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2796#issuecomment-19167",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.2.alpha2
