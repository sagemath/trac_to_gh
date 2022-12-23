# Issue 6956: cannot differentiate cotangent

archive/issues_006956.json:
```json
{
    "body": "CC:  jason kcrisman\n\nFrom sage-support:\n\n\n```\nOn Fri, 18 Sep 2009 13:15:46 -0500\nJason Grout <jason-sage@creativetrax.com> wrote:\n\n> On alpha.sagenb.org, I get the following:\n> \n> sage: t=var('t')\n> sage: diff(cot(t),t)\n> D[0](cot)(t)\n> sage: diff(cos(t)/sin(t),t)\n> -cos(t)^2/sin(t)^2 - 1\n> \n> \n> Does Sage not know that cot(t) is cos(t)/sin(t)? \n```\n\nUnfortunately it doesn't. \n\nGiNaC doesn't define the function `cot`. Sage defines it in the file\n`sage/functions/trig.py` starting at line 184. I suppose it was written quickly by Mike during the symbolics switch.\n\nDefining a custom derivative function (named `_derivative_`) in that\nclass should fix this.\n\nHere is the thread:\n\nhttp://groups.google.com/group/sage-support/browse_thread/thread/752de34c876720cc\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6956\n\n",
    "created_at": "2009-09-18T18:32:18Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "cannot differentiate cotangent",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6956",
    "user": "burcin"
}
```
CC:  jason kcrisman

From sage-support:


```
On Fri, 18 Sep 2009 13:15:46 -0500
Jason Grout <jason-sage@creativetrax.com> wrote:

> On alpha.sagenb.org, I get the following:
> 
> sage: t=var('t')
> sage: diff(cot(t),t)
> D[0](cot)(t)
> sage: diff(cos(t)/sin(t),t)
> -cos(t)^2/sin(t)^2 - 1
> 
> 
> Does Sage not know that cot(t) is cos(t)/sin(t)? 
```

Unfortunately it doesn't. 

GiNaC doesn't define the function `cot`. Sage defines it in the file
`sage/functions/trig.py` starting at line 184. I suppose it was written quickly by Mike during the symbolics switch.

Defining a custom derivative function (named `_derivative_`) in that
class should fix this.

Here is the thread:

http://groups.google.com/group/sage-support/browse_thread/thread/752de34c876720cc


Issue created by migration from https://trac.sagemath.org/ticket/6956





---

archive/issue_comments_057540.json:
```json
{
    "body": "Attachment\n\nAdded _derivative() functions to all functions in `trig.py` and `hyperbolic.py`",
    "created_at": "2009-09-19T00:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6956#issuecomment-57540",
    "user": "timdumol"
}
```

Attachment

Added _derivative() functions to all functions in `trig.py` and `hyperbolic.py`



---

archive/issue_comments_057541.json:
```json
{
    "body": "This should do the trick.",
    "created_at": "2009-09-19T00:25:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6956#issuecomment-57541",
    "user": "timdumol"
}
```

This should do the trick.



---

archive/issue_comments_057542.json:
```json
{
    "body": "Thanks for the quick patch.\n\nHere is my review:\n* the keyword argument `diff_param` is only useful for multivariate functions. In this case since all these functions are univariate, so we know the argument is `args[0]`. You can safely drop the first two lines of the `_derivative_()` methods and replace the third with `x = args[0]`.\n* continuing the previous item, we should tell these functions they are univariate. ATM, they silently drop the second argument:\n\n```\nsage: arccsc(a,b)\narccsc(a)\n```\n\n You can do this by giving `nargs=1` as a parameter to the base class constructor.\n* It is better to give the variable as an argument to `diff` in the doctests, for example `diff(asech(x), x)`. I actually prefer `asech(x).derivative(x)`, but this is your patch. :)\n* The formula for the derivative of `asech(x)` you use is only true for x real. You need `-1/(x * (x+1) * sqrt( (1-x)/(1+x) ))`.\n* Similarly, the derivative of `acsch(x)` is `-1/(x^2 * sqrt(1 + 1/x^2) )`\n\nCan someone else check the derivatives to make sure there is no mistake?",
    "created_at": "2009-09-19T16:44:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6956#issuecomment-57542",
    "user": "burcin"
}
```

Thanks for the quick patch.

Here is my review:
* the keyword argument `diff_param` is only useful for multivariate functions. In this case since all these functions are univariate, so we know the argument is `args[0]`. You can safely drop the first two lines of the `_derivative_()` methods and replace the third with `x = args[0]`.
* continuing the previous item, we should tell these functions they are univariate. ATM, they silently drop the second argument:

```
sage: arccsc(a,b)
arccsc(a)
```

 You can do this by giving `nargs=1` as a parameter to the base class constructor.
* It is better to give the variable as an argument to `diff` in the doctests, for example `diff(asech(x), x)`. I actually prefer `asech(x).derivative(x)`, but this is your patch. :)
* The formula for the derivative of `asech(x)` you use is only true for x real. You need `-1/(x * (x+1) * sqrt( (1-x)/(1+x) ))`.
* Similarly, the derivative of `acsch(x)` is `-1/(x^2 * sqrt(1 + 1/x^2) )`

Can someone else check the derivatives to make sure there is no mistake?



---

archive/issue_comments_057543.json:
```json
{
    "body": "Added `_derivative_()` functions to all functions in trig.py and hyperbolic.py. Rev 2. Apply this patch only.",
    "created_at": "2009-09-20T00:26:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6956#issuecomment-57543",
    "user": "timdumol"
}
```

Added `_derivative_()` functions to all functions in trig.py and hyperbolic.py. Rev 2. Apply this patch only.



---

archive/issue_comments_057544.json:
```json
{
    "body": "Attachment\n\nFunctions that inherit from `PrimitiveFunction` are automatically given `nargs = 1` on L800 of `symbolic/function.pyx`. So the silent dropping of arguments is more of a usability problem on the Symbolic side.\n\nI've made the changes for the derivatives of `asech(x)` and `acsch(x)`. I've also generalized the derivatives for `asec(x)` and `acsc(x)`.\n\nAnyone who wants to review the derivatives can check: http://mathworld.wolfram.com/Derivative.html, http://mathworld.wolfram.com/InverseHyperbolicFunctions.html and http://mathworld.wolfram.com/InverseTrigonometricFunctions.html",
    "created_at": "2009-09-20T00:31:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6956#issuecomment-57544",
    "user": "timdumol"
}
```

Attachment

Functions that inherit from `PrimitiveFunction` are automatically given `nargs = 1` on L800 of `symbolic/function.pyx`. So the silent dropping of arguments is more of a usability problem on the Symbolic side.

I've made the changes for the derivatives of `asech(x)` and `acsch(x)`. I've also generalized the derivatives for `asec(x)` and `acsc(x)`.

Anyone who wants to review the derivatives can check: http://mathworld.wolfram.com/Derivative.html, http://mathworld.wolfram.com/InverseHyperbolicFunctions.html and http://mathworld.wolfram.com/InverseTrigonometricFunctions.html



---

archive/issue_comments_057545.json:
```json
{
    "body": "Replying to [comment:3 timdumol]:\n> Functions that inherit from `PrimitiveFunction` are automatically given `nargs = 1` on L800 of `symbolic/function.pyx`. So the silent dropping of arguments is more of a usability problem on the Symbolic side.\n\nYou're right. I fixed this and many other things about symbolic functions last weekend, by rewriting sage/symbolic/function.pyx. Unfortunately I don't think I'll be able to clean up my changes and submit them any time soon... oh, well...\n\n\nI'm giving your patch a positive review. It applies cleanly, and passes all tests on my 4.1.1.alpha. Great job! Many thanks.",
    "created_at": "2009-09-22T11:01:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6956#issuecomment-57545",
    "user": "burcin"
}
```

Replying to [comment:3 timdumol]:
> Functions that inherit from `PrimitiveFunction` are automatically given `nargs = 1` on L800 of `symbolic/function.pyx`. So the silent dropping of arguments is more of a usability problem on the Symbolic side.

You're right. I fixed this and many other things about symbolic functions last weekend, by rewriting sage/symbolic/function.pyx. Unfortunately I don't think I'll be able to clean up my changes and submit them any time soon... oh, well...


I'm giving your patch a positive review. It applies cleanly, and passes all tests on my 4.1.1.alpha. Great job! Many thanks.



---

archive/issue_comments_057546.json:
```json
{
    "body": "burcin: it seems that there are several people interested in helping with symbolics, so maybe if you just posted what you had, people could clean it up for you, if that would be easier for your time situation?",
    "created_at": "2009-09-22T13:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6956#issuecomment-57546",
    "user": "jason"
}
```

burcin: it seems that there are several people interested in helping with symbolics, so maybe if you just posted what you had, people could clean it up for you, if that would be easier for your time situation?



---

archive/issue_comments_057547.json:
```json
{
    "body": "Merged `trac_6956-derivatives.2.patch`.",
    "created_at": "2009-09-24T15:21:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6956#issuecomment-57547",
    "user": "mvngu"
}
```

Merged `trac_6956-derivatives.2.patch`.



---

archive/issue_comments_057548.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-24T15:21:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6956#issuecomment-57548",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057549.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6956#issuecomment-57549",
    "user": "mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
