# Issue 3732: calculus -- some examples of sage integration failing

archive/issues_003732.json:
```json
{
    "body": "Assignee: gfurnish\n\nThese should be integrated into the doctest framework for sage's calculus. See attached.  This is by Elliot Brossard.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3732\n\n",
    "created_at": "2008-07-28T04:11:23Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "title": "calculus -- some examples of sage integration failing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3732",
    "user": "was"
}
```
Assignee: gfurnish

These should be integrated into the doctest framework for sage's calculus. See attached.  This is by Elliot Brossard.

Issue created by migration from https://trac.sagemath.org/ticket/3732





---

archive/issue_comments_026495.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-07-28T04:11:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3732#issuecomment-26495",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_026496.json:
```json
{
    "body": "There's another example (that's with 3.1.2.alpha2), here it shouldn't need assumption on a:\n\n\n```\nsage: var('a')\na\nsage: integrate((x-a)^2*exp(-(x-a)^2), x, -Infinity, +Infinity)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/giniu/<ipython console> in <module>()\n\n/opt/sage/local/lib/python2.5/site-packages/sage/calculus/functional.py in integral(f, *args, **kwds)\n    252     \"\"\"\n    253     try:\n--> 254         return f.integral(*args, **kwds)\n    255     except ValueError, err:\n    256         raise err\n\n/opt/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in integral(self, v, a, b)\n   2532                     raise ValueError, \"Integral is divergent.\"\n   2533                 else:\n-> 2534                     raise TypeError, error\n   2535                     \n   2536 \n\nTypeError: Computation failed since Maxima requested additional constraints (use assume):\nIs  a  positive or negative?\n\n```\n",
    "created_at": "2008-09-01T23:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3732#issuecomment-26496",
    "user": "aginiewicz"
}
```

There's another example (that's with 3.1.2.alpha2), here it shouldn't need assumption on a:


```
sage: var('a')
a
sage: integrate((x-a)^2*exp(-(x-a)^2), x, -Infinity, +Infinity)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/giniu/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/calculus/functional.py in integral(f, *args, **kwds)
    252     """
    253     try:
--> 254         return f.integral(*args, **kwds)
    255     except ValueError, err:
    256         raise err

/opt/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in integral(self, v, a, b)
   2532                     raise ValueError, "Integral is divergent."
   2533                 else:
-> 2534                     raise TypeError, error
   2535                     
   2536 

TypeError: Computation failed since Maxima requested additional constraints (use assume):
Is  a  positive or negative?

```




---

archive/issue_comments_026497.json:
```json
{
    "body": "another failing integral",
    "created_at": "2008-10-24T10:25:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3732#issuecomment-26497",
    "user": "gnprice"
}
```

another failing integral



---

archive/issue_comments_026498.json:
```json
{
    "body": "Attachment\n\nI added a testcase for another integral, namely `integral( s^2 * exp(- (a + b) * s^2 ), s)`, that fails to integrate.  This is reproduced on Sage 3.1.1.",
    "created_at": "2008-10-24T10:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3732#issuecomment-26498",
    "user": "gnprice"
}
```

Attachment

I added a testcase for another integral, namely `integral( s^2 * exp(- (a + b) * s^2 ), s)`, that fails to integrate.  This is reproduced on Sage 3.1.1.



---

archive/issue_comments_026499.json:
```json
{
    "body": "Added clearer summary.  The second attachment is not relevant to this ticket, though certainly we should be able to integrate arbitrary functions!\n\nWhat is the purpose of this ticket long-term?  These could be added, complete with their error messages, to calculus.py examples - but we already have several of those.  Or one could say this is just a reminder of what we would eventually like Sage to be able to use Maxima to do, and put them in but not test them.  \n\nOtherwise this is in some sense related to solving #780 (among several others), which is a thornier problem.",
    "created_at": "2009-01-29T16:45:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3732#issuecomment-26499",
    "user": "kcrisman"
}
```

Added clearer summary.  The second attachment is not relevant to this ticket, though certainly we should be able to integrate arbitrary functions!

What is the purpose of this ticket long-term?  These could be added, complete with their error messages, to calculus.py examples - but we already have several of those.  Or one could say this is just a reminder of what we would eventually like Sage to be able to use Maxima to do, and put them in but not test them.  

Otherwise this is in some sense related to solving #780 (among several others), which is a thornier problem.



---

archive/issue_comments_026500.json:
```json
{
    "body": "With the latest Maxima upgrade and Pynac conversion, the last two integrals are correct - the penultimate one is, of course, \n\n```\n1/2*sqrt(pi)\n```\n\nand the last one is \n\n```\n1/2*(a+b)^(3/2)*s^3*gamma_incomplete(-3/2,(a+b)/s^2)/(s^2)^(3/2)\n```\n",
    "created_at": "2009-09-24T00:43:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3732#issuecomment-26500",
    "user": "kcrisman"
}
```

With the latest Maxima upgrade and Pynac conversion, the last two integrals are correct - the penultimate one is, of course, 

```
1/2*sqrt(pi)
```

and the last one is 

```
1/2*(a+b)^(3/2)*s^3*gamma_incomplete(-3/2,(a+b)/s^2)/(s^2)^(3/2)
```




---

archive/issue_comments_026501.json:
```json
{
    "body": "Here is the current state of this ticket.  Of the examples in the first attached file, the following are legitimate bugs of this type.\n\nThe first example has unnecessary questions.\n\n```\nsage: integrate(1/sqrt(x-q), x, 1, 2)\n2 sqrt(2 - q) - 2 sqrt(1 - q) # should be this always\n```\n\n\nThe third example is definitely a case for this, as of Maxima 5.19.1:\n\n```\n(%i19) integrate(log(q-x), x, a, b);\nIs  b - a  positive, negative, or zero?\n\npositive;\n(%o19)          (b - q) log(q - b) - (a - q) log(q - a) - b + a\n(%i20) integrate(log(q-x), x, a, b);\nIs  b - a  positive, negative, or zero?\n\nnegative;\n(%o20)          (b - q) log(q - b) - (a - q) log(q - a) - b + a\n(%i21) integrate(log(q-x), x, a, b);\nIs  b - a  positive, negative, or zero?\n\nzero;\n(%o21)          (b - q) log(q - b) - (a - q) log(q - a) - b + a\n```\n\n\nThe fifth example has MANY questions to ask, always the same answer:\n\n```\n(%i36) integrate(1/sqrt(q^2-x^2),x, a, b);\nIs  b - a  positive, negative, or zero?\n\nnegative;\nIs  q - a  positive, negative, or zero?\n\nzero;\nIs  q + a  positive, negative, or zero?\n\nzero;\nIs  q + b  positive, negative, or zero?\n\npositive;\n                                 b              a\n(%o36)                    asin(------) - asin(------)\n                               abs(q)         abs(q)\n\n```\n\n\n++++++++++++++++++++++++++++++++\n\nThe following should not be considered bugs, at least not for the reason given.\n\nThe second example is okay:\n\n```\nsage: integrate(1/(x-q),x,1,2)\n```\n\nMaxima adds pi*I and/or switches q-2 to 2-q as appropriate.  If we don't like those differences, that should be on a different ticket.\n\nThe fourth example is:\n\n```\nsage: integrate(1/(q-x^2), x)\n```\n\nThe answers given are a constant away from each other, but look very different.  This probably should be considered a bug (Maxima can't connect between logs and arctan/h stuff), but is likely to not be resolved soon, or by questions. \n\nThe last example is definitely not a bug, as for q=-1 you should get a different answer!",
    "created_at": "2009-10-02T16:37:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3732#issuecomment-26501",
    "user": "kcrisman"
}
```

Here is the current state of this ticket.  Of the examples in the first attached file, the following are legitimate bugs of this type.

The first example has unnecessary questions.

```
sage: integrate(1/sqrt(x-q), x, 1, 2)
2 sqrt(2 - q) - 2 sqrt(1 - q) # should be this always
```


The third example is definitely a case for this, as of Maxima 5.19.1:

```
(%i19) integrate(log(q-x), x, a, b);
Is  b - a  positive, negative, or zero?

positive;
(%o19)          (b - q) log(q - b) - (a - q) log(q - a) - b + a
(%i20) integrate(log(q-x), x, a, b);
Is  b - a  positive, negative, or zero?

negative;
(%o20)          (b - q) log(q - b) - (a - q) log(q - a) - b + a
(%i21) integrate(log(q-x), x, a, b);
Is  b - a  positive, negative, or zero?

zero;
(%o21)          (b - q) log(q - b) - (a - q) log(q - a) - b + a
```


The fifth example has MANY questions to ask, always the same answer:

```
(%i36) integrate(1/sqrt(q^2-x^2),x, a, b);
Is  b - a  positive, negative, or zero?

negative;
Is  q - a  positive, negative, or zero?

zero;
Is  q + a  positive, negative, or zero?

zero;
Is  q + b  positive, negative, or zero?

positive;
                                 b              a
(%o36)                    asin(------) - asin(------)
                               abs(q)         abs(q)

```


++++++++++++++++++++++++++++++++

The following should not be considered bugs, at least not for the reason given.

The second example is okay:

```
sage: integrate(1/(x-q),x,1,2)
```

Maxima adds pi*I and/or switches q-2 to 2-q as appropriate.  If we don't like those differences, that should be on a different ticket.

The fourth example is:

```
sage: integrate(1/(q-x^2), x)
```

The answers given are a constant away from each other, but look very different.  This probably should be considered a bug (Maxima can't connect between logs and arctan/h stuff), but is likely to not be resolved soon, or by questions. 

The last example is definitely not a bug, as for q=-1 you should get a different answer!



---

archive/issue_comments_026502.json:
```json
{
    "body": "Update: these (the three remaining ones above) are still in Maxima 5.20.1.",
    "created_at": "2009-12-22T17:02:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3732#issuecomment-26502",
    "user": "kcrisman"
}
```

Update: these (the three remaining ones above) are still in Maxima 5.20.1.



---

archive/issue_comments_026503.json:
```json
{
    "body": "Here is a particularly easy one (that sympy and giac can do, of course):\n\n```\nsage: var(\"a\");\nsage: integrate(cos(x), x, 0, a)\n    <snip>\nValueError: ...\nIs a positive, negative or zero?\n\nsage: integrate(cos(x), x, 0, a, algorithm=\"sympy\")\nsin(a)\n\nsage: integrate(cos(x), x, 0, a, algorithm=\"giac\")\nsin(a)\n```\n",
    "created_at": "2021-01-27T18:57:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3732#issuecomment-26503",
    "user": "@DaveWitteMorris"
}
```

Here is a particularly easy one (that sympy and giac can do, of course):

```
sage: var("a");
sage: integrate(cos(x), x, 0, a)
    <snip>
ValueError: ...
Is a positive, negative or zero?

sage: integrate(cos(x), x, 0, a, algorithm="sympy")
sin(a)

sage: integrate(cos(x), x, 0, a, algorithm="giac")
sin(a)
```

