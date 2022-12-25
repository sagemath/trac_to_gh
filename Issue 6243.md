# Issue 6243: add support for arbitrary parents in pynac's evalf

archive/issues_006243.json:
```json
{
    "body": "CC:  @mwhansen\n\nFrom Alex Raichev on sage-support:\n\n\n```\nHi all:\n\nUpon upgrading to Sage 4.0, i can no longer make a dictionary with\nderivatives as keys (see below).  Can someone please fix this?\n\nAlex\n\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: X= var('x,y')\nsage: f= function('f',*X); f\nf(x, y)\nsage: for x in X:\n....:     diff(f,x)\n....:\nD[0](f)(x, y)\nD[1](f)(x, y)\nsage: d= {}\nsage: for x in X:\n....:     d[diff(f,x)] = 1\n....:\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call\nlast)\n| Sage Version 4.0, Release Date: 2009-05-29                         |\n| Type notebook() for the GUI, and license() for information.        |\n/Users/raichev/<ipython console> in <module>()\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/symbolic/\nexpression.so in sage.symbolic.expression.Expression.__nonzero__ (sage/\nsymbolic/expression.cpp:7814)()\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/symbolic/\nexpression.so in sage.symbolic.expression.Expression.test_relation\n(sage/symbolic/expression.cpp:9187)()\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/rings/\ncomplex_interval_field.pyc in __call__(self, x, im)\n    286\n    287             try:\n--> 288                 return x._complex_mpfi_( self )  \n    289             except AttributeError:\n    290                 pass\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/symbolic/\nexpression.so in sage.symbolic.expression.Expression._complex_mpfi_\n(sage/symbolic/expression.cpp:5484)()\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/symbolic/\nexpression_conversions.pyc in __call__(self, ex)\n    212                 div = self.get_fake_div(ex)\n    213                 return self.arithmetic(div, div.operator())\n--> 214             return self.arithmetic(ex, operator)  \n    215         elif operator in relation_operators:\n    216             return self.relation(ex, operator)\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/symbolic/\nexpression_conversions.pyc in arithmetic(self, ex, operator)\n   1424             return base ** expt\n   1425         else:\n-> 1426             return reduce(operator, map(self, operands))  \n   1427\n   1428     def composition(self, ex, operator):\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/symbolic/\nexpression_conversions.pyc in __call__(self, ex)\n    216             return self.relation(ex, operator)\n    217         elif isinstance(operator, FDerivativeOperator):\n--> 218             return self.derivative(ex, operator)  \n    219         else:\n    220             return self.composition(ex, operator)\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/symbolic/\nexpression_conversions.pyc in derivative(self, ex, operator)\n    344             NotImplementedError: derivative\n    345         \"\"\"\n--> 346         raise NotImplementedError, \"derivative\"  \n    347\n    348     def arithmetic(self, ex, operator):\n\nNotImplementedError: derivative\n```\n\n\nI suppose an immediate fix is to implement the derivative method in `sage.symbolic.expression_conversions.Converter`. I believe the right fix is to change pynac to pass on the parent for numerical approximation instead of just the precision. I'll work on making the necessary changes in pynac.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6243\n\n",
    "created_at": "2009-06-07T19:07:43Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "add support for arbitrary parents in pynac's evalf",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6243",
    "user": "https://github.com/burcin"
}
```
CC:  @mwhansen

From Alex Raichev on sage-support:


```
Hi all:

Upon upgrading to Sage 4.0, i can no longer make a dictionary with
derivatives as keys (see below).  Can someone please fix this?

Alex

----------------------------------------------------------------------
----------------------------------------------------------------------
sage: X= var('x,y')
sage: f= function('f',*X); f
f(x, y)
sage: for x in X:
....:     diff(f,x)
....:
D[0](f)(x, y)
D[1](f)(x, y)
sage: d= {}
sage: for x in X:
....:     d[diff(f,x)] = 1
....:
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call
last)
| Sage Version 4.0, Release Date: 2009-05-29                         |
| Type notebook() for the GUI, and license() for information.        |
/Users/raichev/<ipython console> in <module>()

/Applications/sage/local/lib/python2.5/site-packages/sage/symbolic/
expression.so in sage.symbolic.expression.Expression.__nonzero__ (sage/
symbolic/expression.cpp:7814)()

/Applications/sage/local/lib/python2.5/site-packages/sage/symbolic/
expression.so in sage.symbolic.expression.Expression.test_relation
(sage/symbolic/expression.cpp:9187)()

/Applications/sage/local/lib/python2.5/site-packages/sage/rings/
complex_interval_field.pyc in __call__(self, x, im)
    286
    287             try:
--> 288                 return x._complex_mpfi_( self )  
    289             except AttributeError:
    290                 pass

/Applications/sage/local/lib/python2.5/site-packages/sage/symbolic/
expression.so in sage.symbolic.expression.Expression._complex_mpfi_
(sage/symbolic/expression.cpp:5484)()

/Applications/sage/local/lib/python2.5/site-packages/sage/symbolic/
expression_conversions.pyc in __call__(self, ex)
    212                 div = self.get_fake_div(ex)
    213                 return self.arithmetic(div, div.operator())
--> 214             return self.arithmetic(ex, operator)  
    215         elif operator in relation_operators:
    216             return self.relation(ex, operator)

/Applications/sage/local/lib/python2.5/site-packages/sage/symbolic/
expression_conversions.pyc in arithmetic(self, ex, operator)
   1424             return base ** expt
   1425         else:
-> 1426             return reduce(operator, map(self, operands))  
   1427
   1428     def composition(self, ex, operator):

/Applications/sage/local/lib/python2.5/site-packages/sage/symbolic/
expression_conversions.pyc in __call__(self, ex)
    216             return self.relation(ex, operator)
    217         elif isinstance(operator, FDerivativeOperator):
--> 218             return self.derivative(ex, operator)  
    219         else:
    220             return self.composition(ex, operator)

/Applications/sage/local/lib/python2.5/site-packages/sage/symbolic/
expression_conversions.pyc in derivative(self, ex, operator)
    344             NotImplementedError: derivative
    345         """
--> 346         raise NotImplementedError, "derivative"  
    347
    348     def arithmetic(self, ex, operator):

NotImplementedError: derivative
```


I suppose an immediate fix is to implement the derivative method in `sage.symbolic.expression_conversions.Converter`. I believe the right fix is to change pynac to pass on the parent for numerical approximation instead of just the precision. I'll work on making the necessary changes in pynac.


Issue created by migration from https://trac.sagemath.org/ticket/6243





---

archive/issue_comments_049759.json:
```json
{
    "body": "doctests for the fix",
    "created_at": "2009-07-31T21:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6243#issuecomment-49759",
    "user": "https://github.com/burcin"
}
```

doctests for the fix



---

archive/issue_comments_049760.json:
```json
{
    "body": "Attachment [trac_6243-fderivative_hash.patch](tarball://root/attachments/some-uuid/ticket6243/trac_6243-fderivative_hash.patch) by @burcin created at 2009-07-31 21:25:17\n\nI have a fix for this in my local pynac tree. I took a shortcut and changed the fderivative hashes to include the parameters.\n\nI'll make a new pynac package with fixes for some other bugs available soon.",
    "created_at": "2009-07-31T21:25:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6243#issuecomment-49760",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_6243-fderivative_hash.patch](tarball://root/attachments/some-uuid/ticket6243/trac_6243-fderivative_hash.patch) by @burcin created at 2009-07-31 21:25:17

I have a fix for this in my local pynac tree. I took a shortcut and changed the fderivative hashes to include the parameters.

I'll make a new pynac package with fixes for some other bugs available soon.



---

archive/issue_comments_049761.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-08-01T02:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6243#issuecomment-49761",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049762.json:
```json
{
    "body": "This now depends on the package linked from #6404.\n\nPlease follow the instructions on that ticket to apply & test.",
    "created_at": "2009-08-01T02:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6243#issuecomment-49762",
    "user": "https://github.com/burcin"
}
```

This now depends on the package linked from #6404.

Please follow the instructions on that ticket to apply & test.



---

archive/issue_comments_049763.json:
```json
{
    "body": "Set assignee to @burcin.",
    "created_at": "2009-08-01T02:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6243#issuecomment-49763",
    "user": "https://github.com/burcin"
}
```

Set assignee to @burcin.



---

archive/issue_comments_049764.json:
```json
{
    "body": "I tested this out. Pynac changes seem fine to me. I encountered one issue though:\n\n```\nsage: d = {}\nsage: d[x] = 1\nsage: d\n{x: 1}\nsage: f(x) = function('f',x)\nsage: d[diff(f(x),x)] = 2\nsage: d.keys()\n[D[0](f)(x), x]\nsage: d.values()\n[2, 1]\nsage: d\n!boom!\n```\n\n\nThe origin of this !boom! lies in expression_conversions.py for fderivative\nwhich is clearly NOT in purview of this patch. So I am going to give it a positive review \nshortly.",
    "created_at": "2009-08-02T17:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6243#issuecomment-49764",
    "user": "https://github.com/golam-m-hossain"
}
```

I tested this out. Pynac changes seem fine to me. I encountered one issue though:

```
sage: d = {}
sage: d[x] = 1
sage: d
{x: 1}
sage: f(x) = function('f',x)
sage: d[diff(f(x),x)] = 2
sage: d.keys()
[D[0](f)(x), x]
sage: d.values()
[2, 1]
sage: d
!boom!
```


The origin of this !boom! lies in expression_conversions.py for fderivative
which is clearly NOT in purview of this patch. So I am going to give it a positive review 
shortly.



---

archive/issue_comments_049765.json:
```json
{
    "body": "Note: I am giving partial positive review because I tested this patch against my stable \nsage-4.1. So if it applies cleanly on Sage-4.1.1.rc1 then that would be full positive from me.",
    "created_at": "2009-08-02T19:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6243#issuecomment-49765",
    "user": "https://github.com/golam-m-hossain"
}
```

Note: I am giving partial positive review because I tested this patch against my stable 
sage-4.1. So if it applies cleanly on Sage-4.1.1.rc1 then that would be full positive from me.



---

archive/issue_comments_049766.json:
```json
{
    "body": "I applied patches in the following order:\n1. the spkg `pynac-0.1.8.p2.spkg` at #6404\n2. `trac_6404-conjugate_typesetting.patch`\n3. `trac_6401-real_imag_typesetting.patch`\n4. `trac_6377-exp_infinity.patch`\n5. `trac_6243-fderivative_hash.patch`\nAll doctests pass in my merge tree. So I'm changing #6404, #6401, #6377 and #6243 to positive review as per Golam's request.",
    "created_at": "2009-08-03T00:32:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6243#issuecomment-49766",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I applied patches in the following order:
1. the spkg `pynac-0.1.8.p2.spkg` at #6404
2. `trac_6404-conjugate_typesetting.patch`
3. `trac_6401-real_imag_typesetting.patch`
4. `trac_6377-exp_infinity.patch`
5. `trac_6243-fderivative_hash.patch`
All doctests pass in my merge tree. So I'm changing #6404, #6401, #6377 and #6243 to positive review as per Golam's request.



---

archive/issue_comments_049767.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-03T00:32:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6243#issuecomment-49767",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
