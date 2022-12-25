# Issue 8459: broken translatin of polylog from Maxima

archive/issues_008459.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @kcrisman @burcin\n\nKeywords: symbolics\n\nMaixma's li[2](x) translates to polylog2(x) which is not defined in Sage\n\n```\nsage: maxima('li[1](x)').sage().subs(x=2).n() \n-3.14159265358979*I\nsage: maxima('li[2](x)').sage().subs(x=2).n()\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/opt/sage-4.3.3-i686-Linux/<ipython console> in <module>()\n\n/opt/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:17036)()\n\nTypeError: cannot evaluate symbolic expresssion numerically\n\nsage: f(x)= integrate(log(1-x^2)/x, x); f(2).n()\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/opt/sage-4.3.3-i686-Linux/<ipython console> in <module>()\n\n/opt/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:17036)()\n\nTypeError: cannot evaluate symbolic expresssion numerically\n\n```\n\n\npatch comes soon\n\nIssue created by migration from https://trac.sagemath.org/ticket/8459\n\n",
    "created_at": "2010-03-06T21:41:27Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "broken translatin of polylog from Maxima",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8459",
    "user": "https://github.com/robert-marik"
}
```
Assignee: @burcin

CC:  @kcrisman @burcin

Keywords: symbolics

Maixma's li[2](x) translates to polylog2(x) which is not defined in Sage

```
sage: maxima('li[1](x)').sage().subs(x=2).n() 
-3.14159265358979*I
sage: maxima('li[2](x)').sage().subs(x=2).n()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/opt/sage-4.3.3-i686-Linux/<ipython console> in <module>()

/opt/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:17036)()

TypeError: cannot evaluate symbolic expresssion numerically

sage: f(x)= integrate(log(1-x^2)/x, x); f(2).n()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/opt/sage-4.3.3-i686-Linux/<ipython console> in <module>()

/opt/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:17036)()

TypeError: cannot evaluate symbolic expresssion numerically

```


patch comes soon

Issue created by migration from https://trac.sagemath.org/ticket/8459





---

archive/issue_comments_076025.json:
```json
{
    "body": "Attachment [trac-8390.patch](tarball://root/attachments/some-uuid/ticket8459/trac-8390.patch) by @robert-marik created at 2010-03-06 22:28:53\n\napply only this patch",
    "created_at": "2010-03-06T22:28:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8459#issuecomment-76025",
    "user": "https://github.com/robert-marik"
}
```

Attachment [trac-8390.patch](tarball://root/attachments/some-uuid/ticket8459/trac-8390.patch) by @robert-marik created at 2010-03-06 22:28:53

apply only this patch



---

archive/issue_comments_076026.json:
```json
{
    "body": "Attachment [trac-8459.patch](tarball://root/attachments/some-uuid/ticket8459/trac-8459.patch) by @robert-marik created at 2010-03-06 22:32:42\n\nThe patch is attached. Still have behavior which I do not understand:\nlog(-x^2 + 1)*log(x) + 1/2*polylog(2, -x^2 + 1) evaluates numerically at x=1/2 only if it is obtained from direct input and not from Maxima.\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: f(x)=integrate(ln(1-x^2)/x,x)                       \nsage: f\nx |--> log(-x^2 + 1)*log(x) + 1/2*polylog(2, -x^2 + 1)\nsage: g(x)=log(-x^2 + 1)*log(x) + 1/2*polylog(2, -x^2 + 1)\nsage: g\nx |--> log(-x^2 + 1)*log(x) + 1/2*polylog(2, -x^2 + 1)\nsage: bool(f==g)                                          \nFalse\nsage: bool(f._repr_()==g._repr_())                        \nTrue\nsage: g(1/2).n()\n0.688640713882747\nsage: f(1/2).n()\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n| Sage Version 4.3.3, Release Date: 2010-02-21                       |\n| Type notebook() for the GUI, and license() for information.        |\n/opt/sage-4.3.3-i686-Linux/<ipython console> in <module>()\n\n/opt/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:17036)()\n\nTypeError: cannot evaluate symbolic expresssion numerically\nsage:\n```\n\nAny idea what happens?",
    "created_at": "2010-03-06T22:32:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8459#issuecomment-76026",
    "user": "https://github.com/robert-marik"
}
```

Attachment [trac-8459.patch](tarball://root/attachments/some-uuid/ticket8459/trac-8459.patch) by @robert-marik created at 2010-03-06 22:32:42

The patch is attached. Still have behavior which I do not understand:
log(-x^2 + 1)*log(x) + 1/2*polylog(2, -x^2 + 1) evaluates numerically at x=1/2 only if it is obtained from direct input and not from Maxima.

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: f(x)=integrate(ln(1-x^2)/x,x)                       
sage: f
x |--> log(-x^2 + 1)*log(x) + 1/2*polylog(2, -x^2 + 1)
sage: g(x)=log(-x^2 + 1)*log(x) + 1/2*polylog(2, -x^2 + 1)
sage: g
x |--> log(-x^2 + 1)*log(x) + 1/2*polylog(2, -x^2 + 1)
sage: bool(f==g)                                          
False
sage: bool(f._repr_()==g._repr_())                        
True
sage: g(1/2).n()
0.688640713882747
sage: f(1/2).n()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.3.3, Release Date: 2010-02-21                       |
| Type notebook() for the GUI, and license() for information.        |
/opt/sage-4.3.3-i686-Linux/<ipython console> in <module>()

/opt/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:17036)()

TypeError: cannot evaluate symbolic expresssion numerically
sage:
```

Any idea what happens?



---

archive/issue_comments_076027.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-06T22:32:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8459#issuecomment-76027",
    "user": "https://github.com/robert-marik"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076028.json:
```json
{
    "body": "And anther issue which I do not understand:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: polylog\nsage: g(x)=integrate(ln(1-x^2)/x,x)\nsage: g(1/2).n()\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n| Sage Version 4.3.3, Release Date: 2010-02-21                       |\n| Type notebook() for the GUI, and license() for information.        |\n/opt/sage-4.3.3/<ipython console> in <module>()\n\n/opt/sage-4.3.3/local/lib/python2.6/site-packages/sage/symbolic/expression.so in                                              sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:17036)()\n\nTypeError: cannot evaluate symbolic expresssion numerically\nsage: g(x)=eval(preparse(integrate(ln(1-x^2)/x,x)._repr_()))\nsage: g(1/2).n()\n0.688640713882747\nsage: g\nx |--> log(-x^2 + 1)*log(x) + 1/2*polylog(2, -x^2 + 1)\nsage:\n```\n\nwhy are eval and _repr_ necessary?",
    "created_at": "2010-03-07T14:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8459#issuecomment-76028",
    "user": "https://github.com/robert-marik"
}
```

And anther issue which I do not understand:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: polylog
sage: g(x)=integrate(ln(1-x^2)/x,x)
sage: g(1/2).n()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.3.3, Release Date: 2010-02-21                       |
| Type notebook() for the GUI, and license() for information.        |
/opt/sage-4.3.3/<ipython console> in <module>()

/opt/sage-4.3.3/local/lib/python2.6/site-packages/sage/symbolic/expression.so in                                              sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:17036)()

TypeError: cannot evaluate symbolic expresssion numerically
sage: g(x)=eval(preparse(integrate(ln(1-x^2)/x,x)._repr_()))
sage: g(1/2).n()
0.688640713882747
sage: g
x |--> log(-x^2 + 1)*log(x) + 1/2*polylog(2, -x^2 + 1)
sage:
```

why are eval and _repr_ necessary?



---

archive/issue_comments_076029.json:
```json
{
    "body": "[sage-support](http://groups.google.cz/group/sage-support/browse_thread/thread/d1ef50cd207e0f76) question concerning the problem above",
    "created_at": "2010-03-07T14:58:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8459#issuecomment-76029",
    "user": "https://github.com/robert-marik"
}
```

[sage-support](http://groups.google.cz/group/sage-support/browse_thread/thread/d1ef50cd207e0f76) question concerning the problem above



---

archive/issue_comments_076030.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-05T10:51:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8459#issuecomment-76030",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076031.json:
```json
{
    "body": "Attachment [trac_8459-doctest.patch](tarball://root/attachments/some-uuid/ticket8459/trac_8459-doctest.patch) by @burcin created at 2010-04-05 10:51:47\n\nThank you for the patch and pointing out the conversion problem Robert.\n\nI fixed the problems reported in comment:2 in #7661.\n\nattachment:trac_8459-doctest.patch adds a doctest to sage.functions.log.Function_polylog to check if the conversion works. It also moves the compilation of the regular expression out of the `symbolic_expression_from_maxima_string()` function.\n\nPatches to be applied, in this order:\n* attachment:trac-8459.patch\n* attachment:trac_8459-doctest.patch\n\nThis ticket depends on #7661.",
    "created_at": "2010-04-05T10:51:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8459#issuecomment-76031",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_8459-doctest.patch](tarball://root/attachments/some-uuid/ticket8459/trac_8459-doctest.patch) by @burcin created at 2010-04-05 10:51:47

Thank you for the patch and pointing out the conversion problem Robert.

I fixed the problems reported in comment:2 in #7661.

attachment:trac_8459-doctest.patch adds a doctest to sage.functions.log.Function_polylog to check if the conversion works. It also moves the compilation of the regular expression out of the `symbolic_expression_from_maxima_string()` function.

Patches to be applied, in this order:
* attachment:trac-8459.patch
* attachment:trac_8459-doctest.patch

This ticket depends on #7661.



---

archive/issue_comments_076032.json:
```json
{
    "body": "Thanks for improving this, Burcin. \n\nTo the release manager: Apply only the patches trac-8459* , the first patch was my mistake and it is not relevant in this ticket.",
    "created_at": "2010-04-09T07:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8459#issuecomment-76032",
    "user": "https://github.com/robert-marik"
}
```

Thanks for improving this, Burcin. 

To the release manager: Apply only the patches trac-8459* , the first patch was my mistake and it is not relevant in this ticket.



---

archive/issue_comments_076033.json:
```json
{
    "body": "After applying \"trac-8459.patch\" and \"trac_8459-doctest.patch\" to Sage 4.3.5, I get doctest errors for functions/log.py:\n\n```\nsage -t  \"devel/sage/sage/functions/log.py\"                 \n**********************************************************************\nFile \"/Applications/sage/devel/sage/sage/functions/log.py\", line 305:\n    sage: t.operator() == polylog\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/Applications/sage/devel/sage/sage/functions/log.py\", line 307:\n    sage: t.subs(x=.5).n()\nException raised:\n    Traceback (most recent call last):\n      File \"/Applications/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Applications/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Applications/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[17]>\", line 1, in <module>\n        t.subs(x=RealNumber('.5')).n()###line 307:\n    sage: t.subs(x=.5).n()\n      File \"expression.pyx\", line 3797, in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:17043)\n    TypeError: cannot evaluate symbolic expression numerically\n**********************************************************************\n1 items had failures:\n   2 of  18 in __main__.example_5\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /Users/palmieri/.sage//tmp/.doctest_log.py\n\t [7.6 s]\n```\n",
    "created_at": "2010-04-15T23:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8459#issuecomment-76033",
    "user": "https://github.com/jhpalmieri"
}
```

After applying "trac-8459.patch" and "trac_8459-doctest.patch" to Sage 4.3.5, I get doctest errors for functions/log.py:

```
sage -t  "devel/sage/sage/functions/log.py"                 
**********************************************************************
File "/Applications/sage/devel/sage/sage/functions/log.py", line 305:
    sage: t.operator() == polylog
Expected:
    True
Got:
    False
**********************************************************************
File "/Applications/sage/devel/sage/sage/functions/log.py", line 307:
    sage: t.subs(x=.5).n()
Exception raised:
    Traceback (most recent call last):
      File "/Applications/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Applications/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Applications/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[17]>", line 1, in <module>
        t.subs(x=RealNumber('.5')).n()###line 307:
    sage: t.subs(x=.5).n()
      File "expression.pyx", line 3797, in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:17043)
    TypeError: cannot evaluate symbolic expression numerically
**********************************************************************
1 items had failures:
   2 of  18 in __main__.example_5
***Test Failed*** 2 failures.
For whitespace errors, see the file /Users/palmieri/.sage//tmp/.doctest_log.py
	 [7.6 s]
```




---

archive/issue_comments_076034.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-15T23:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8459#issuecomment-76034",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_076035.json:
```json
{
    "body": "Replying to [comment:7 jhpalmieri]:\n> After applying \"trac-8459.patch\" and \"trac_8459-doctest.patch\" to Sage 4.3.5, I get doctest errors for functions/log.py:\n<snipped the error log>\n\nThese errors look like the patch attachment:trac_8459-doctest.patch was applied without #7661. That ticket was merged before this, so I have no idea what went wrong.\n\nI applied these patches to Sage-4.4.1 and ran the tests. There were no errors. Switching this back to positive review, and keeping fingers crossed that there is no subtle bug hiding somewhere.",
    "created_at": "2010-05-04T21:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8459#issuecomment-76035",
    "user": "https://github.com/burcin"
}
```

Replying to [comment:7 jhpalmieri]:
> After applying "trac-8459.patch" and "trac_8459-doctest.patch" to Sage 4.3.5, I get doctest errors for functions/log.py:
<snipped the error log>

These errors look like the patch attachment:trac_8459-doctest.patch was applied without #7661. That ticket was merged before this, so I have no idea what went wrong.

I applied these patches to Sage-4.4.1 and ran the tests. There were no errors. Switching this back to positive review, and keeping fingers crossed that there is no subtle bug hiding somewhere.



---

archive/issue_comments_076036.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-04T21:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8459#issuecomment-76036",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076037.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-04T21:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8459#issuecomment-76037",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076038.json:
```json
{
    "body": "Patches to be applied, in this order:\n\n* attachment:trac-8459.patch\n* attachment:trac_8459-doctest.patch",
    "created_at": "2010-05-04T21:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8459#issuecomment-76038",
    "user": "https://github.com/burcin"
}
```

Patches to be applied, in this order:

* attachment:trac-8459.patch
* attachment:trac_8459-doctest.patch



---

archive/issue_comments_076039.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T22:11:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8459#issuecomment-76039",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_076040.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac-8459.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8459/trac-8459.patch)\n2. [trac_8459-doctest.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8459/trac_8459-doctest.patch)",
    "created_at": "2010-05-08T22:11:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8459#issuecomment-76040",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged in this order:

1. [trac-8459.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8459/trac-8459.patch)
2. [trac_8459-doctest.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8459/trac_8459-doctest.patch)
