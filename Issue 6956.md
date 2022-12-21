# Issue 6956: cannot differentiate cotangent

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2009-09-18 18:32:18

CC:  jason kcrisman

From sage-support:


```
On Fri, 18 Sep 2009 13:15:46 -0500
Jason Grout <jason-sage`@`creativetrax.com> wrote:

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



---

Attachment

Added _derivative() functions to all functions in `trig.py` and `hyperbolic.py`


---

Comment by timdumol created at 2009-09-19 00:25:19

This should do the trick.


---

Comment by burcin created at 2009-09-19 16:44:13

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

Comment by timdumol created at 2009-09-20 00:26:14

Added `_derivative_()` functions to all functions in trig.py and hyperbolic.py. Rev 2. Apply this patch only.


---

Attachment

Functions that inherit from `PrimitiveFunction` are automatically given `nargs = 1` on L800 of `symbolic/function.pyx`. So the silent dropping of arguments is more of a usability problem on the Symbolic side.

I've made the changes for the derivatives of `asech(x)` and `acsch(x)`. I've also generalized the derivatives for `asec(x)` and `acsc(x)`.

Anyone who wants to review the derivatives can check: http://mathworld.wolfram.com/Derivative.html, http://mathworld.wolfram.com/InverseHyperbolicFunctions.html and http://mathworld.wolfram.com/InverseTrigonometricFunctions.html


---

Comment by burcin created at 2009-09-22 11:01:22

Replying to [comment:3 timdumol]:
> Functions that inherit from `PrimitiveFunction` are automatically given `nargs = 1` on L800 of `symbolic/function.pyx`. So the silent dropping of arguments is more of a usability problem on the Symbolic side.

You're right. I fixed this and many other things about symbolic functions last weekend, by rewriting sage/symbolic/function.pyx. Unfortunately I don't think I'll be able to clean up my changes and submit them any time soon... oh, well...


I'm giving your patch a positive review. It applies cleanly, and passes all tests on my 4.1.1.alpha. Great job! Many thanks.


---

Comment by jason created at 2009-09-22 13:42:46

burcin: it seems that there are several people interested in helping with symbolics, so maybe if you just posted what you had, people could clean it up for you, if that would be easier for your time situation?


---

Comment by mvngu created at 2009-09-24 15:21:00

Merged `trac_6956-derivatives.2.patch`.


---

Comment by mvngu created at 2009-09-24 15:21:00

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 10:22:49

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
