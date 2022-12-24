# Issue 6189: 'integrate' produces incorrect answer

archive/issues_006189.json:
```json
{
    "body": "Assignee: burcin\n\nKeywords: integrate, integral, incorrect\n\nAffects: \nx64 Ubuntu 9.04 (Jaunty)\nSage 4.0, compiled from source, and updated (sage -upgrade) as of this posting\n\nBy simply casting a number using 'n()', I can cause integrate to return a vastly different result. See below:\n\n```\nvar = sage.calculus.calculus.var\n\ndef NormalPDF(x,mu,sigma):\n    return 1/sqrt(2*pi*sigma^2)*exp(-1/(2*sigma**2)*(x-mu)^2)\n\nx = var('x')\nmu = var('m')\nsigma = var('s')\nassume(sigma>0)\nchild1 = NormalPDF(x,0,1)\nchild2 = NormalPDF(x,n(0),n(1))\nparent = NormalPDF(x,mu,sigma)\n\n# this expansion helps Sage to do the integral\nintegrand1 = ((parent-child1)^2).expand()\nintegrand2 = ((parent-child2)^2).expand()\n\nint1 = integrate(integrand1,x,-infinity,infinity)\nint2 = integrate(integrand2,x,-infinity,infinity)\n\nprint \"THIS EXPRESSION:\"\nprint int1\nprint \"\\nSHOULD BE VERY SIMILIAR TO THIS EXPRESSION:\"\nprint int2\n\nprint \"\\nMAKING THIS NUMBER:\"\nprint int1.subs({mu:0,sigma:1}).n()\nprint \"\\nVERY SIMILAR TO THIS NUMBER:\"\nprint int2.subs({mu:0,sigma:1}).n()\n```\n\n\nThe above produces the output:\n\n```\nTHIS EXPRESSION:\n1/2*((s + 1)*sqrt(s^2 + 1)*e^(1/2*m^2/(s^2 + 1)) - 2*sqrt(2)*s)*e^(-1/2*m^2/(s^2 + 1))/(sqrt(s^2 + 1)*sqrt(pi)*s)\n\nSHOULD BE VERY SIMILIAR TO THIS EXPRESSION:\n1/2*(sqrt(0.5*s^2 + 0.5)*e^(1/2*m^2/(s^2 + 1)) - sqrt(2)*s)*e^(-1/2*m^2/(s^2 + 1))/(sqrt(0.5*s^2 + 0.5)*sqrt(pi)*s)\n\nMAKING THIS NUMBER:\n0.000000000000000\n\nVERY SIMILAR TO THIS NUMBER:\n-0.116847488627555\n```\n\n\nMathematica claims the correct integral is:\n\n```\n\\frac{1+\\sigma }{2 \\sqrt{\\pi } \\sigma }-\\frac{\\sqrt{2} e^{-\\frac{\\mu ^2}{2+2 \\sigma ^2}}}{\\sqrt{\\pi +\\pi  \\sigma ^2}}\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6189\n\n",
    "created_at": "2009-06-02T19:29:04Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "'integrate' produces incorrect answer",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6189",
    "user": "emchristiansen"
}
```
Assignee: burcin

Keywords: integrate, integral, incorrect

Affects: 
x64 Ubuntu 9.04 (Jaunty)
Sage 4.0, compiled from source, and updated (sage -upgrade) as of this posting

By simply casting a number using 'n()', I can cause integrate to return a vastly different result. See below:

```
var = sage.calculus.calculus.var

def NormalPDF(x,mu,sigma):
    return 1/sqrt(2*pi*sigma^2)*exp(-1/(2*sigma**2)*(x-mu)^2)

x = var('x')
mu = var('m')
sigma = var('s')
assume(sigma>0)
child1 = NormalPDF(x,0,1)
child2 = NormalPDF(x,n(0),n(1))
parent = NormalPDF(x,mu,sigma)

# this expansion helps Sage to do the integral
integrand1 = ((parent-child1)^2).expand()
integrand2 = ((parent-child2)^2).expand()

int1 = integrate(integrand1,x,-infinity,infinity)
int2 = integrate(integrand2,x,-infinity,infinity)

print "THIS EXPRESSION:"
print int1
print "\nSHOULD BE VERY SIMILIAR TO THIS EXPRESSION:"
print int2

print "\nMAKING THIS NUMBER:"
print int1.subs({mu:0,sigma:1}).n()
print "\nVERY SIMILAR TO THIS NUMBER:"
print int2.subs({mu:0,sigma:1}).n()
```


The above produces the output:

```
THIS EXPRESSION:
1/2*((s + 1)*sqrt(s^2 + 1)*e^(1/2*m^2/(s^2 + 1)) - 2*sqrt(2)*s)*e^(-1/2*m^2/(s^2 + 1))/(sqrt(s^2 + 1)*sqrt(pi)*s)

SHOULD BE VERY SIMILIAR TO THIS EXPRESSION:
1/2*(sqrt(0.5*s^2 + 0.5)*e^(1/2*m^2/(s^2 + 1)) - sqrt(2)*s)*e^(-1/2*m^2/(s^2 + 1))/(sqrt(0.5*s^2 + 0.5)*sqrt(pi)*s)

MAKING THIS NUMBER:
0.000000000000000

VERY SIMILAR TO THIS NUMBER:
-0.116847488627555
```


Mathematica claims the correct integral is:

```
\frac{1+\sigma }{2 \sqrt{\pi } \sigma }-\frac{\sqrt{2} e^{-\frac{\mu ^2}{2+2 \sigma ^2}}}{\sqrt{\pi +\pi  \sigma ^2}}
```


Issue created by migration from https://trac.sagemath.org/ticket/6189





---

archive/issue_comments_049442.json:
```json
{
    "body": "This is now fixed, presumably in the Maxima upgrade.  Note that the integral in fact computes *without* expand(), and in that case there is no 'experimental error'!  Attached patch verifies this.",
    "created_at": "2009-09-29T14:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6189#issuecomment-49442",
    "user": "kcrisman"
}
```

This is now fixed, presumably in the Maxima upgrade.  Note that the integral in fact computes *without* expand(), and in that case there is no 'experimental error'!  Attached patch verifies this.



---

archive/issue_comments_049443.json:
```json
{
    "body": "Attachment [trac_6189-num-approx-integral.patch](tarball://root/attachments/some-uuid/ticket6189/trac_6189-num-approx-integral.patch) by kcrisman created at 2009-09-29 14:45:50\n\nBased on 4.1.2.alpha2",
    "created_at": "2009-09-29T14:45:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6189#issuecomment-49443",
    "user": "kcrisman"
}
```

Attachment [trac_6189-num-approx-integral.patch](tarball://root/attachments/some-uuid/ticket6189/trac_6189-num-approx-integral.patch) by kcrisman created at 2009-09-29 14:45:50

Based on 4.1.2.alpha2



---

archive/issue_comments_049444.json:
```json
{
    "body": "Despite what it says, actually based on 4.1.2.alpha4.",
    "created_at": "2009-09-29T14:46:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6189#issuecomment-49444",
    "user": "kcrisman"
}
```

Despite what it says, actually based on 4.1.2.alpha4.



---

archive/issue_comments_049445.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-16T08:14:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6189#issuecomment-49445",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_049446.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-10-16T08:14:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6189#issuecomment-49446",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_049447.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-16T08:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6189#issuecomment-49447",
    "user": "mhansen"
}
```

Resolution: fixed
