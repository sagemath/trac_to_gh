# Issue 5711: [with patch, needs review] Enhanced Typesetting of Symbolic Functions

Issue created by migration from https://trac.sagemath.org/ticket/5711

Original creator: gmhossain

Original creation time: 2009-04-08 11:55:14

Assignee: cwitty

CC:  burcin jason jhpalmieri schymans

Keywords: Enhance Typesetting, LaTeX, Symbolic Functions

Here is a patch that enhances current typesetting capability
of symbolic functions within sage.

This issue has been under a long discussion in the thread

http://groups.google.com/group/sage-devel/browse_thread/thread/a51f269f057d8223/536b4ef2493bb20c

Main enhancements are:

(1) Symbolics functions with name in Greek letters (with possible
suffixes), are typeset nicely in LaTeX.

Ex:  psi(x)  =>  \psi(x)

(2) Functions such as "diff", "integrate", "limit", "conjugate",
"laplace", "inverse_lapse" are now typeset within Sage itself.

Ex:  psi(x).conjugate()  =>    {\psi}^*(x)

(3) Default (fall-back) typesetting for unknown functions (as
in Maxima).

Ex:  myfn(x)   =>  {\it myfn}(x)

(4) Allows users to define their own/custom LaTeX expression
for any symbolic functions via a new method "set_latex()" for
the class SymbolicFunctionEvaluation.

Ex: 


```
var('t');
hubble(t) = function('hubble',t)
hubble(t).set_latex('\\mathcal{H}')

#To reset custom LaTeX expression
hubble(t).set_latex()
```


(5)  If the arguments of a symbolic function are all symbolic
variables then typesetting will avoid using \left(, \right).

Ex:  Phi(x,y) => \Phi(x, y)  (if x,y are symbolic vars)


Note: You need to apply a small patch

http://trac.sagemath.org/sage_trac/ticket/5678

before you apply the attached patch. This patch is
created using sage-3.4.


---

Attachment


---

Comment by jason created at 2009-05-30 05:40:05

burcin: do you want to review this?  Does the move to the new symbolics affect this patch?


---

Comment by jhpalmieri created at 2009-06-09 21:59:42

Patch doesn't apply cleanly against 4.0.1.


---

Comment by gmhossain created at 2009-06-09 22:20:49

Replying to [comment:4 jhpalmieri]:
> Patch doesn't apply cleanly against 4.0.1.

Yes, recent switch to new symbolics has affected this patch quite a bit.
In fact, the class "SymbolicFunctionEvaluation" (whose enhancement was aimed
through this patch) doesn't exist anymore. I am now looking into the 
new symbolics code to properly rebase the patch.


---

Comment by kcrisman created at 2009-06-12 19:46:58

This is really impressive.   I assume that stan s and the others will want to review this more since they would use it more intensely and understand LaTeX better than I do, but I threw it a lot of stuff and the only "problems" I found were additional cases one might want, which could easily be a separate ticket after this is merged.  The integrals, limits, Laplace, derivatives work out nice now, as does the option for D.  
 1. Only some underscore things do subscripts, and double subscripts don't work.  That's fine, but might as well search for them if possible, e.g. HH_sigma or WWW_xy_z or something could also typeset.
 1. The weird cases mentioned in various threads such as D[0](f)(sin(x)*cos(x)) look nice but have e.g. dcos(x)*sin(x) in the denominator, not giving Jason's suggestion of -(sin(x)<sup>2-cos(x)</sup>2)*\frac{df}{dx}(sin(x)*cos(x)).  I assume that's okay but wanted to check.
 1. There is still the same typesetting for e.g. variables mu and mu_.  I think that sort of makes sense, since mu_1 and mu1 give the same thing, but it does seem strange.
 1. Some stuff still doesn't work, but I don't know if it did before.  For instance, sqrt(mu) is okay, but e^(sqrt(mu)) is not, or even e^(sqrt(x)).  So #6211 can't be closed, not that you claimed it could - but it would fit naturally here.  Check out show(e^function(f_mu,x)) for a real kick.
 1. Limit and integral syntax don't (yet) allow multiple things for multiple variables, but since they are nested by parentheses it would be nice for those to show up, which they currently don't (however, they do calculate properly).  This definitely is not within the purview of this ticket.
Great work from my view!  Except I almost always declare my function f(x)=x^2, not symbolic, so I will probably not use it much.  But it will be good for subscripts for sure!


---

Comment by jhpalmieri created at 2009-06-12 23:10:40

This patch does not pass doctests on sage.math:

```
sage -t  "devel/sage/sage/symbolic/function.pyx"            
**********************************************************************
File "/scratch/palmieri/sage-4.0.1/devel/sage/sage/symbolic/function.pyx", line 121:
    sage: latex(foo(x,y^z))
Expected:
    \mbox{t}\left(x, y^{z}\right)
Got:
    t\left(x, y^{z}\right)
**********************************************************************
File "/scratch/palmieri/sage-4.0.1/devel/sage/sage/symbolic/function.pyx", line 129:
    sage: latex(foo(x,y^z))
Expected:
    \mbox{foo}\left(x, y^{z}\right)
Got:
    foo\left(x, y^{z}\right)
**********************************************************************
1 items had failures:
   2 of  45 in __main__.example_2
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/palmieri/sage-4.0.1/tmp/.doctest_function.py
	 [1.2 s]
exit code: 1024
```

Should be easy enough to fix.


---

Attachment


---

Comment by gmhossain created at 2009-06-13 00:21:15

Thanks! I have fixed these two doctest failure and updated the rebased patch.


---

Comment by gmhossain created at 2009-06-13 12:17:20

Thanks kcrisman! As you have suggested, I would also prefer to fix only the blockers 
in this patch and leave other enhancements for follow-up patches. 

>  1. Some stuff still doesn't work, but I don't know if it did before.  For instance, sqrt(mu) is okay, but e^(sqrt(mu)) is not, or even e^(sqrt(x)).  So #6211 can't be closed, not that you claimed it could - but it would fit naturally here.  Check out show(e^function(f_mu,x)) for a real kick.

This seems to be a bug for "exp" function. Other functions such as "abs", "sin" etc work fine. I have posted
my comments there with a easy fix. It would be better to have a separate patch for that bug.


---

Comment by burcin created at 2009-06-14 14:40:14

Changing component from misc to symbolics.


---

Comment by burcin created at 2009-06-14 14:40:14

Hi Golam,

Thanks for your continued work on this. I see that your patch improves the typesetting of symbolic functions dramatically. I believe with a few improvements it would fit better in the new symbolics framework.

Here is my referee report:

Quotes from the description:
> 
> (2) Functions such as "diff", "integrate", "limit", "conjugate",
> "laplace", "inverse_laplace" are now typeset within Sage itself.
> 
> Ex:  integrate(f(x),x)  =>    \int f(x) dx

These should be handled using the custom printing facilities of `sage.symbolic.function.SFunction`. Special casing them in the new `latex_symbolic_function()` function is not scalable. This approach would also make the checks for the number of arguments as well as the calls to `_symbolic_function_default_latex_()` in each of these functions redundant.

I see that there is already a `_limit` function defined in `sage/calculus/calculus.py`. I think the best solution for the short term would be to put these printing functions there, and give them as an argument to the `SFunction` constructor.

Conjugates are already printed as:


```
sage: latex(x.conjugate())
\bar{x}
```


Why is `\overline` better?

> (6) *[New in the rebased patch]* New symbolics uses "D" 
> format for derivatives instead of old "diff" format. 
> The rebased patch typesets symbolic derivatives in old "diff" format by default as in this format typeset version looks similar to those found in text books, journals.
> 
> However see this thread for known limitations of current conversion between these two formats
>  http://groups.google.com/group/sage-devel/browse_thread/thread/7479c3eeb96348a2
> 
> One can switch between two typesetting format as follows
> 
> {{{
> f(x) = function('f',x)
> g = diff(f(x),x)
> latex(g) 
> \frac{d f\left(x\right)}{d x}
> # Switch to D format
> sage.symbolic.pynac.typeset_d_as_diff=False
> latex(g)
> D[0]f\left(x\right)
> }}}

I believe this issue needs more debate, preferably with examples of how Maple and MMA handle this problem. I will post a new message about this to sage-devel soon. For now, I suggest we split this to a different ticket.

> (1) Symbolics functions with name in Greek letters (with possible
> suffixes), are typeset nicely in LaTeX.
> 
> Ex:  psi(x)  =>  \psi(x)
>      f0(x)  =>  f_0(x)

Can't this be handled by a call to the new `latex_function_name()` from `sage.symbolic.pynac.py_latex_function_pystring()`?

> (3) Default (fall-back) typesetting for unknown functions (as
> in Maxima).
> 
> Ex:  myfn(x)   =>  {\it myfn}(x)

We have the GiNaC convention of falling back to `\mbox` at the moment. Previously, maxima didn't do anything for function names with one variable, and added an `\it`:


```
sage: version()
'Sage Version 3.4.2, Release Date: 2009-05-05'
sage: var('a')
a
sage: f = function('f')
sage: latex(f(a))
f\left(a\right)

```


As you mention in the docstring for `latex_function_name()`, there is considerable code duplication between this function and `latex_variable_name()`. Your previous response to my question about the differences between these two functions is here:

http://groups.google.com/group/sage-devel/msg/071207efa39c5356

It seems that your goal of returning a different response as default behavior can be achieved by passing a parameter to the `latex_varify()` calls at the end of `latex_variable_name()`. Is there a reason why the further recursions performed by `latex_variable_name()` are not relevant for function names? In any case, the string processing code in `latex_variable_name()` shouldn't be duplicated.

> (7) *[New in the rebased patch]*  The rebased patch resolves
> the issue
> 
> http://trac.sagemath.org/sage_trac/ticket/6268

This seems to be caused by a thinko on my part. It can be fixed by modifying lines 416-149 in `sage/symbolic/pynac.pyx`. You seem to do something similar at the end of `latex_symbolic_function()` and `_symbolic_function_default_latex_()` functions.


Overall I think the patch looks very crowded and confusing. With the changes suggested above, 
 * the new functions  `latex_symbolic_function()`, `_symbolic_function_default_latex_()`, `_args_latex_()`, can be eliminated.
 * derivative related functions `latex_d_derivative()` and `_derivative_latex_()` should be split to a new ticket.
 * specialized printing functions `_integrate_latex_()`, `_inverse_laplace_latex_()`, `_laplace_latex_()`, `_limit_latex_()` should be moved to `sage/calculus/calculus.py` and hooked up to the right `sage.symbolic.function.SFunction` instance.
 * `_conjugate_latex_()` doesn't seem necessary.


---

Comment by gmhossain created at 2009-06-15 01:30:40

Thanks Burcin for your detailed review. See below for my responses. I would be happy to
hear you back before I start making some of the changes, you have suggested.



> > (2) Functions such as "diff", "integrate", "limit", "conjugate",
> > "laplace", "inverse_laplace" are now typeset within Sage itself.
> These should be handled using the custom printing facilities of `sage.symbolic.function.SFunction`. 


I fully agree! However, does new symbolics has such framework ready for the mentioned functions?


> I see that there is already a `_limit` function defined in `sage/calculus/calculus.py`. 
> I think the best solution for the short term would be to put these printing functions 
> there, and give them as an argument to the `SFunction` constructor.

Could you please give an short example for such construction (my current understanding 
of new symbolics is limited)? 

What is your "long-term" solution? 

Why is it better to put these functions in calculus/calculus.py 
even as a "short term" solution?  (I gather from William's note http://480.sagenb.org/home/pub/45/ that 
"calculus" direcotory is to be deleted. This conflicts with your suggestion.)


> {{{
> sage: latex(x.conjugate())
> \bar{x}
> }}}
> 
> Why is `\overline` better?


"\bar" is ok for variable but is insufficient for symbolic functions. Please try the
followings in the notebook: 

```
jsmath('\\bar{\\psi\\left(x, y\\right)}') 
jsmath('\\overline{\\psi\\left(x, y\\right)}') 
```

then you will see the reason yourself.

 
> > (6) *[New in the rebased patch]* New symbolics uses "D"  format 
> I believe this issue needs more debate, 
> I suggest we split this to a different ticket.


Sure, I will open a new ticket for this.


> 
> > (1) Symbolics functions with name in Greek letters (with possible
> > suffixes), are typeset nicely in LaTeX.
> > 
> > Ex:  psi(x)  =>  \psi(x)
> >      f0(x)  =>  f_0(x)
> 
> Can't this be handled by a call to the new `latex_function_name()` from `sage.symbolic.pynac.py_latex_function_pystring()`?


Provided all other symbolic "functions" ("integrate",...) have been typeset 
somewhere else which is not the case at present.


> > (3) Default (fall-back) typesetting for unknown functions (as
> > in Maxima).
> > 
> > Ex:  myfn(x)   =>  {\it myfn}(x)
> 
> We have the GiNaC convention of falling back to `\mbox` at the moment. 


Frankly, it is disappointing to see another inconsistent typesetting.
 
Why should a function named "sin" should be typseset as "\sin" (=>"\rm sin")
where as another function named "mysin" is typeset as "\mbox{mysin}"? Please compare 
them side-by-side to see the contrast.


> Previously, maxima didn't do anything for function names with one variable, and added an `\it`:


So as in this patch!  Though, I wanted to use "\rm" as {\rm myfunc} but decided to
stick to maxima usage.



> As you mention in the docstring for `latex_function_name()`, there is 
> considerable code duplication between this function and `latex_variable_name()`. 


I agree that we should avoid duplication of code. 


> Is there a reason why the further recursions performed by `latex_variable_name()` 
> are not relevant for function names? 


In physics, we often use functions such as "f_{\alpha\beta}". In sage, if I use
current latex_variable_name() to typeset "f_alpha_beta" then it would typeset 
as f_{{\alpha}_{\beta}} which is completely different. 

However I guees, thats my own preference and I shouldn't argue anymore on this.
I guess #6290 will solve my problem altogether.

I will remove latex_function_name() and use latex_variable_name() instead.


---

Attachment


---

Comment by gmhossain created at 2009-06-23 11:59:50

Burcin: I have updated the patch as you suggested. List of changes is given in the description.


---

Attachment

doctest fixes


---

Comment by burcin created at 2009-06-23 13:35:30

Thanks Golam. The patch looks good to me. I added a small patch that fixes doctests in two places.

Only apply 

 * trac_5711-enhanced-symbolic-typesetting-rebased_to_4.0.2.patch
 * trac_5711-doctest_fixes.patch


---

Comment by rlm created at 2009-06-24 09:52:03

Resolution: fixed


---

Comment by schymans created at 2009-06-24 10:47:59

Replying to [comment:7 kcrisman]:
> This is really impressive.   I assume that stan s and the others will want to review this more since they would use it more intensely and understand LaTeX better than I do, but I threw it a lot of stuff and the only "problems" I found were additional cases one might want, which could easily be a separate ticket after this is merged.  The integrals, limits, Laplace, derivatives work out nice now, as does the option for D.  
>  1. Only some underscore things do subscripts, and double subscripts don't work.  That's fine, but might as well search for them if possible, e.g. HH_sigma or WWW_xy_z or something could also typeset.
[Snip]
I am very fond of the set_latex() method for defining custom latex representations, which would allow for multiple subscripts etc. Unfortunately, it has been disabled with the new symbolics. Is there a plan to re-enable it again? In general, I think that it would be nice to give as much control to the user as possible, rather than hard-coding certain latex representations. Sorry I haven't been of any help with reviewing/patching, but I only now got back to the typesetting issues and found that my previous ad-hoc latex definitions don't work in Sage 4.x any more. :(

Great work, anyway, and many thanks to those that invested time and effort into improving the typesetting in Sage!


---

Comment by gmhossain created at 2009-06-24 10:56:09

Replying to [comment:16 schymans]:
> I am very fond of the set_latex() method for defining custom latex representations, 
> which would allow for multiple subscripts etc. Unfortunately, it has been disabled 
> with the new symbolics. Is there a plan to re-enable it again? 

Yes but in a new avatar! The new method would be more powerful. The patch is
here

http://trac.sagemath.org/sage_trac/ticket/6290
