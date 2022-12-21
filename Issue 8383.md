# Issue 8383: should sigma(x) produce an error?

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-02-26 23:10:51

Assignee: burcin

CC:  leif benjaminfjones eviatarbach slelievre

I hit the following problem:

```
sage: f(x) = sigma(x)-x
...
TypeError: unable to convert x (=x) to an integer
```

Wouldn't it better to keep sigma(x) unevaluated for x not an integer?
Note that `f = lambda(x):sigma(x)-x` works but it less nice.


---

Comment by kcrisman created at 2010-05-26 20:15:43

We'd have to produce a symbolic version of sigma somewhere.  Do you want this for all arithmetic functions?  We really should have an arithmetic function class anyway, but it's probably more trouble than it's worth to actually do it.


---

Comment by zimmerma created at 2010-05-27 14:18:51

Replying to [comment:1 kcrisman]:
> We'd have to produce a symbolic version of sigma somewhere.  Do you want this for all arithmetic functions?

yes, in Maple for example numtheory[sigma](x) remains symbolic, and does not produce an error.


---

Comment by kcrisman created at 2010-05-27 14:55:10

Changing component from calculus to symbolics.


---

Comment by kcrisman created at 2010-05-27 14:55:10

Okay, then I think I will update the summary of this.  Also changing component since it's more at symbolics than calculus.   

We would need to have a uniform error message as well, and hopefully use plot_step_function as a unified plotting method (?).


---

Comment by burcin created at 2010-05-27 15:14:47

Can you either provide a list of "arithmetic functions" which should be made symbolic, or just make this ticket about `sigma()`?

Tickets with blanket statements about symbolic functions (see #4102, #1158, #4229) are hard to attack since nobody takes on the task of making a list of functions which need to be fixed.


---

Comment by kcrisman created at 2010-05-27 15:39:43

Well, at the very least the ones in rings/arith.py which have 'standard' representations should be, so Moebius, Euler_Phi, Sigma.   Someday we will hopefully also implement things like the Mertens function (not to be confused with the constant), and those should also be able to remain symbolic.  If Paul has others which we have and Maple leaves symbolic, that would be great.


---

Comment by zimmerma created at 2010-05-27 16:24:34

Replying to [comment:4 burcin]:
> Can you either provide a list of "arithmetic functions" which should be made symbolic, or just make this ticket about `sigma()`?

doesn't Sage provide such a list? It would then be easy to do a loop over all functions and
determine those which don't work with symbolic arguments.

Paul


---

Comment by kcrisman created at 2010-05-27 16:58:19

But I don't think we want ALL such functions (if you are referring to all functions in rings/arith.py).  I don't think we have a keyword otherwise, and it certainly isn't worth the time to do four_squares or primitive_root (which just gives the smallest one) as a symbolic function before we have even implemented some of these other functions.  Anyway, I'll change the summary again to make my preference clear :)

Interestingly, these three functions all give different errors upon giving them 'x' as an argument.  That's probably irrelevant, but still fun to point out.


---

Comment by burcin created at 2010-08-28 16:16:31

Changing keywords from "" to "beginner".


---

Comment by afleckenstein created at 2013-01-04 14:15:50

Is the best way to do this by just making all of the functions BuiltinFunctions? I'm trying to import BuiltinFunction in rings/arith.py, but when I do: 


```
from sage.symbolic.function import BuiltinFunction
```


in rings/arith.py, I get the error:



```
ImportError: cannot import name QuotientRing
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.
```



---

Comment by burcin created at 2013-01-04 14:22:06

You're running into circular imports. Symbolic functions are considerably slower compared to the current implementations in `sage/rings/arith.py`. Since these are used in many places in the Sage library, it would make sense to keep those and introduce symbolic versions in a new file (`sage/functions/arith.py` say). Then you need to make sure that the functions imported at the Sage command line are the symbolic ones.

Thanks for looking into this.


---

Comment by afleckenstein created at 2013-01-06 15:44:16

As I'm writing the symbolic version of sigma, it appears that a symbolic function created using BuiltinFunction has to have an explicit number of arguments. It is a little more work to write

```
sage: sigma(5, 1)
```

than just

```
sage: sigma(5)
```

but I'm not sure if there's a way around it.


---

Comment by benjaminfjones created at 2013-01-06 22:48:23

Hi, thanks for working on this!

One solution (this is one I'm using on #4102), is to write a wrapper function `sigma` that will take either one or two arguments and return the general symbolic function of two arguments accordingly:


```
sage: sigma(5)
symbolic_sigma(5, 1)
sage: sigma(x, 2)
symbolic_sigma(x, 2)
```


The symbolic function `symbolic_sigma` would inherit from `BuiltinFunction` and have two arguments. It's printed name could be just `sigma` instead of `symbolic_sigma` to lessen confusion.


---

Comment by rws created at 2014-06-11 05:56:54

But all functions mentioned so far are expressible using Dirichlet generating functions, and it would make much more sense to make them just wrappers around that (nonexisting) functionality. The same applies to C-finite "functions" like `fibonacci`, `lucas_number1`, `lucas_number2`, which are generalized with #15714.


---

Comment by kcrisman created at 2014-06-11 12:23:27

Did somebody say [defining Dirichlet series](http://ask.sagemath.org/question/2540/defining-dirichlet-series)?  [Here is an implementation](http://www.wordpress.jonhanke.com/Software/Sage__Dirichlet_series/Dirichlet_series.sage) that I haven't had time to try out but which might be a good basis for that.  [This sage-support thread](https://groups.google.com/d/topic/sage-support/v7TFXKbAV0E) may also be relevant, though I don't know how advanced that psage code is.


---

Comment by rws created at 2014-06-12 16:29:32

Thanks. I copied your comment to create #16477.


---

Comment by @DaveWitteMorris created at 2020-05-27 02:54:22

Changing keywords from "beginner" to "".


---

Comment by @DaveWitteMorris created at 2020-05-27 02:54:22

Removing the "beginner" tag from old tickets. Some could be returned to beginner-friendly status by adding a comment about what needs to be done. Some others might be easy for an experienced developer to finish.
