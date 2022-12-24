# Issue 4630: bug in functions real() and imag().

archive/issues_004630.json:
```json
{
    "body": "Assignee: somebody\n\nUsing sage-3.2 (compiled with make), but the same behaviour also happens on sage-3.1.4,\nOS:Debian on a 32-bit Core-Duo machine,\n\nthe examples where I use 'a' as variable work well,\nthe examples where I use 'b' as variable ('I' is substituted by 'CDF(I)') are buggy:\n\n\n```\ngeorg@HILBERT:~/Daten/Sync/Phd/Code/sde$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| Sage Version 3.2, Release Date: 2008-11-20                         |\n| Type notebook() for the GUI, and license() for information.        |\nsage: a = exp(I*0.2*pi); a; type(a); real(a); real(a).n()\ne^(0.200000000000000*I*pi)\n<class 'sage.calculus.calculus.SymbolicComposition'>\ncos(0.200000000000000*pi)\n0.809016994374947\nsage: b = exp(CDF(I)*0.2*pi); b; type(b); real(b); real(b).n()\ne^(0.200000000000000*pi*I)\n<class 'sage.calculus.calculus.SymbolicComposition'>\ne^(0.200000000000000*pi*I)\n0.809016994374947 + 0.587785252292473*I\nsage: a = exp(I*0.2*pi); a; type(a); imag(a); imag(a).n()\ne^(0.200000000000000*I*pi)\n<class 'sage.calculus.calculus.SymbolicComposition'>\nsin(0.200000000000000*pi)\n0.587785252292473\nsage: b = exp(CDF(I)*0.2*pi); b; type(b); imag(b); imag(b).n()\ne^(0.200000000000000*pi*I)\n<class 'sage.calculus.calculus.SymbolicComposition'>\n0\n0.000000000000000\nsage: n(exp(CDF(I)*0.2*pi))\n0.809016994374947 + 0.587785252292473*I\n```\n\n\nGeorg\n\nIssue created by migration from https://trac.sagemath.org/ticket/4630\n\n",
    "created_at": "2008-11-26T23:39:46Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "bug in functions real() and imag().",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4630",
    "user": "ggrafendorfer"
}
```
Assignee: somebody

Using sage-3.2 (compiled with make), but the same behaviour also happens on sage-3.1.4,
OS:Debian on a 32-bit Core-Duo machine,

the examples where I use 'a' as variable work well,
the examples where I use 'b' as variable ('I' is substituted by 'CDF(I)') are buggy:


```
georg@HILBERT:~/Daten/Sync/Phd/Code/sde$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.2, Release Date: 2008-11-20                         |
| Type notebook() for the GUI, and license() for information.        |
sage: a = exp(I*0.2*pi); a; type(a); real(a); real(a).n()
e^(0.200000000000000*I*pi)
<class 'sage.calculus.calculus.SymbolicComposition'>
cos(0.200000000000000*pi)
0.809016994374947
sage: b = exp(CDF(I)*0.2*pi); b; type(b); real(b); real(b).n()
e^(0.200000000000000*pi*I)
<class 'sage.calculus.calculus.SymbolicComposition'>
e^(0.200000000000000*pi*I)
0.809016994374947 + 0.587785252292473*I
sage: a = exp(I*0.2*pi); a; type(a); imag(a); imag(a).n()
e^(0.200000000000000*I*pi)
<class 'sage.calculus.calculus.SymbolicComposition'>
sin(0.200000000000000*pi)
0.587785252292473
sage: b = exp(CDF(I)*0.2*pi); b; type(b); imag(b); imag(b).n()
e^(0.200000000000000*pi*I)
<class 'sage.calculus.calculus.SymbolicComposition'>
0
0.000000000000000
sage: n(exp(CDF(I)*0.2*pi))
0.809016994374947 + 0.587785252292473*I
```


Georg

Issue created by migration from https://trac.sagemath.org/ticket/4630





---

archive/issue_comments_034807.json:
```json
{
    "body": "This appears to be fixed in sage-4.0.1.alpha0:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: a = exp(I*0.2*pi); a; type(a); real(a); real(a).n()\ne^(0.200000000000000*I*pi)\n<type 'sage.symbolic.expression.Expression'>\ncos(0.200000000000000*pi)\n0.809016994374947\nsage: b = exp(CDF(I)*0.2*pi); b; type(b); real(b); real(b).n()\ne^(0.2*I*pi)\n<type 'sage.symbolic.expression.Expression'>\ncos(0.2*pi)\n0.809016994375\nsage: a = exp(I*0.2*pi); a; type(a); imag(a); imag(a).n()\ne^(0.200000000000000*I*pi)\n<type 'sage.symbolic.expression.Expression'>\nsin(0.200000000000000*pi)\n0.587785252292473\nsage: b = exp(CDF(I)*0.2*pi); b; type(b); imag(b); imag(b).n()\ne^(0.2*I*pi)\n<type 'sage.symbolic.expression.Expression'>\nsin(0.2*pi)\n0.587785252292\nsage: n(exp(CDF(I)*0.2*pi))\n0.809016994375 + 0.587785252292*I\n```\n",
    "created_at": "2009-06-03T07:43:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4630#issuecomment-34807",
    "user": "AlexGhitza"
}
```

This appears to be fixed in sage-4.0.1.alpha0:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: a = exp(I*0.2*pi); a; type(a); real(a); real(a).n()
e^(0.200000000000000*I*pi)
<type 'sage.symbolic.expression.Expression'>
cos(0.200000000000000*pi)
0.809016994374947
sage: b = exp(CDF(I)*0.2*pi); b; type(b); real(b); real(b).n()
e^(0.2*I*pi)
<type 'sage.symbolic.expression.Expression'>
cos(0.2*pi)
0.809016994375
sage: a = exp(I*0.2*pi); a; type(a); imag(a); imag(a).n()
e^(0.200000000000000*I*pi)
<type 'sage.symbolic.expression.Expression'>
sin(0.200000000000000*pi)
0.587785252292473
sage: b = exp(CDF(I)*0.2*pi); b; type(b); imag(b); imag(b).n()
e^(0.2*I*pi)
<type 'sage.symbolic.expression.Expression'>
sin(0.2*pi)
0.587785252292
sage: n(exp(CDF(I)*0.2*pi))
0.809016994375 + 0.587785252292*I
```




---

archive/issue_comments_034808.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-26T03:33:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4630#issuecomment-34808",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_034809.json:
```json
{
    "body": "It looks like this is fixed in Sage 4.1:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: a = exp(I*0.2*pi); a; type(a); real(a); real(a).n()\ne^(0.200000000000000*I*pi)\n<type 'sage.symbolic.expression.Expression'>\ncos(0.200000000000000*pi)\n0.809016994374947\nsage: b = exp(CDF(I)*0.2*pi); b; type(b); real(b); real(b).n()\ne^(0.2*I*pi)\n<type 'sage.symbolic.expression.Expression'>\ncos(0.2*pi)\n0.809016994375\nsage: a = exp(I*0.2*pi); a; type(a); imag(a); imag(a).n()\ne^(0.200000000000000*I*pi)\n<type 'sage.symbolic.expression.Expression'>\nsin(0.200000000000000*pi)\n0.587785252292473\nsage: b = exp(CDF(I)*0.2*pi); b; type(b); imag(b); imag(b).n()\ne^(0.2*I*pi)\n<type 'sage.symbolic.expression.Expression'>\nsin(0.2*pi)\n0.587785252292\nsage: n(exp(CDF(I)*0.2*pi))\n0.809016994375 + 0.587785252292*I\n```\n\nI'm closing this ticket as fixed.",
    "created_at": "2009-07-26T03:33:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4630#issuecomment-34809",
    "user": "mvngu"
}
```

It looks like this is fixed in Sage 4.1:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: a = exp(I*0.2*pi); a; type(a); real(a); real(a).n()
e^(0.200000000000000*I*pi)
<type 'sage.symbolic.expression.Expression'>
cos(0.200000000000000*pi)
0.809016994374947
sage: b = exp(CDF(I)*0.2*pi); b; type(b); real(b); real(b).n()
e^(0.2*I*pi)
<type 'sage.symbolic.expression.Expression'>
cos(0.2*pi)
0.809016994375
sage: a = exp(I*0.2*pi); a; type(a); imag(a); imag(a).n()
e^(0.200000000000000*I*pi)
<type 'sage.symbolic.expression.Expression'>
sin(0.200000000000000*pi)
0.587785252292473
sage: b = exp(CDF(I)*0.2*pi); b; type(b); imag(b); imag(b).n()
e^(0.2*I*pi)
<type 'sage.symbolic.expression.Expression'>
sin(0.2*pi)
0.587785252292
sage: n(exp(CDF(I)*0.2*pi))
0.809016994375 + 0.587785252292*I
```

I'm closing this ticket as fixed.
