# Issue 8383: should sigma(x) produce an error?

archive/issues_008383.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @nexttime @benjaminfjones @eviatarbach @slel\n\nI hit the following problem:\n\n```\nsage: f(x) = sigma(x)-x\n...\nTypeError: unable to convert x (=x) to an integer\n```\n\nWouldn't it better to keep sigma(x) unevaluated for x not an integer?\nNote that `f = lambda(x):sigma(x)-x` works but it less nice.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8383\n\n",
    "created_at": "2010-02-26T23:10:51Z",
    "labels": [
        "calculus",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "should sigma(x) produce an error?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8383",
    "user": "@zimmermann6"
}
```
Assignee: @burcin

CC:  @nexttime @benjaminfjones @eviatarbach @slel

I hit the following problem:

```
sage: f(x) = sigma(x)-x
...
TypeError: unable to convert x (=x) to an integer
```

Wouldn't it better to keep sigma(x) unevaluated for x not an integer?
Note that `f = lambda(x):sigma(x)-x` works but it less nice.

Issue created by migration from https://trac.sagemath.org/ticket/8383





---

archive/issue_comments_074979.json:
```json
{
    "body": "We'd have to produce a symbolic version of sigma somewhere.  Do you want this for all arithmetic functions?  We really should have an arithmetic function class anyway, but it's probably more trouble than it's worth to actually do it.",
    "created_at": "2010-05-26T20:15:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8383#issuecomment-74979",
    "user": "@kcrisman"
}
```

We'd have to produce a symbolic version of sigma somewhere.  Do you want this for all arithmetic functions?  We really should have an arithmetic function class anyway, but it's probably more trouble than it's worth to actually do it.



---

archive/issue_comments_074980.json:
```json
{
    "body": "Replying to [comment:1 kcrisman]:\n> We'd have to produce a symbolic version of sigma somewhere.  Do you want this for all arithmetic functions?\n\nyes, in Maple for example numtheory[sigma](x) remains symbolic, and does not produce an error.",
    "created_at": "2010-05-27T14:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8383#issuecomment-74980",
    "user": "@zimmermann6"
}
```

Replying to [comment:1 kcrisman]:
> We'd have to produce a symbolic version of sigma somewhere.  Do you want this for all arithmetic functions?

yes, in Maple for example numtheory[sigma](x) remains symbolic, and does not produce an error.



---

archive/issue_comments_074981.json:
```json
{
    "body": "Changing component from calculus to symbolics.",
    "created_at": "2010-05-27T14:55:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8383#issuecomment-74981",
    "user": "@kcrisman"
}
```

Changing component from calculus to symbolics.



---

archive/issue_comments_074982.json:
```json
{
    "body": "Okay, then I think I will update the summary of this.  Also changing component since it's more at symbolics than calculus.   \n\nWe would need to have a uniform error message as well, and hopefully use plot_step_function as a unified plotting method (?).",
    "created_at": "2010-05-27T14:55:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8383#issuecomment-74982",
    "user": "@kcrisman"
}
```

Okay, then I think I will update the summary of this.  Also changing component since it's more at symbolics than calculus.   

We would need to have a uniform error message as well, and hopefully use plot_step_function as a unified plotting method (?).



---

archive/issue_comments_074983.json:
```json
{
    "body": "Can you either provide a list of \"arithmetic functions\" which should be made symbolic, or just make this ticket about `sigma()`?\n\nTickets with blanket statements about symbolic functions (see #4102, #1158, #4229) are hard to attack since nobody takes on the task of making a list of functions which need to be fixed.",
    "created_at": "2010-05-27T15:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8383#issuecomment-74983",
    "user": "@burcin"
}
```

Can you either provide a list of "arithmetic functions" which should be made symbolic, or just make this ticket about `sigma()`?

Tickets with blanket statements about symbolic functions (see #4102, #1158, #4229) are hard to attack since nobody takes on the task of making a list of functions which need to be fixed.



---

archive/issue_comments_074984.json:
```json
{
    "body": "Well, at the very least the ones in rings/arith.py which have 'standard' representations should be, so Moebius, Euler_Phi, Sigma.   Someday we will hopefully also implement things like the Mertens function (not to be confused with the constant), and those should also be able to remain symbolic.  If Paul has others which we have and Maple leaves symbolic, that would be great.",
    "created_at": "2010-05-27T15:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8383#issuecomment-74984",
    "user": "@kcrisman"
}
```

Well, at the very least the ones in rings/arith.py which have 'standard' representations should be, so Moebius, Euler_Phi, Sigma.   Someday we will hopefully also implement things like the Mertens function (not to be confused with the constant), and those should also be able to remain symbolic.  If Paul has others which we have and Maple leaves symbolic, that would be great.



---

archive/issue_comments_074985.json:
```json
{
    "body": "Replying to [comment:4 burcin]:\n> Can you either provide a list of \"arithmetic functions\" which should be made symbolic, or just make this ticket about `sigma()`?\n\ndoesn't Sage provide such a list? It would then be easy to do a loop over all functions and\ndetermine those which don't work with symbolic arguments.\n\nPaul",
    "created_at": "2010-05-27T16:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8383#issuecomment-74985",
    "user": "@zimmermann6"
}
```

Replying to [comment:4 burcin]:
> Can you either provide a list of "arithmetic functions" which should be made symbolic, or just make this ticket about `sigma()`?

doesn't Sage provide such a list? It would then be easy to do a loop over all functions and
determine those which don't work with symbolic arguments.

Paul



---

archive/issue_comments_074986.json:
```json
{
    "body": "But I don't think we want ALL such functions (if you are referring to all functions in rings/arith.py).  I don't think we have a keyword otherwise, and it certainly isn't worth the time to do four_squares or primitive_root (which just gives the smallest one) as a symbolic function before we have even implemented some of these other functions.  Anyway, I'll change the summary again to make my preference clear :)\n\nInterestingly, these three functions all give different errors upon giving them 'x' as an argument.  That's probably irrelevant, but still fun to point out.",
    "created_at": "2010-05-27T16:58:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8383#issuecomment-74986",
    "user": "@kcrisman"
}
```

But I don't think we want ALL such functions (if you are referring to all functions in rings/arith.py).  I don't think we have a keyword otherwise, and it certainly isn't worth the time to do four_squares or primitive_root (which just gives the smallest one) as a symbolic function before we have even implemented some of these other functions.  Anyway, I'll change the summary again to make my preference clear :)

Interestingly, these three functions all give different errors upon giving them 'x' as an argument.  That's probably irrelevant, but still fun to point out.



---

archive/issue_comments_074987.json:
```json
{
    "body": "Changing keywords from \"\" to \"beginner\".",
    "created_at": "2010-08-28T16:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8383#issuecomment-74987",
    "user": "@burcin"
}
```

Changing keywords from "" to "beginner".



---

archive/issue_comments_074988.json:
```json
{
    "body": "Is the best way to do this by just making all of the functions BuiltinFunctions? I'm trying to import BuiltinFunction in rings/arith.py, but when I do: \n\n\n```\nfrom sage.symbolic.function import BuiltinFunction\n```\n\n\nin rings/arith.py, I get the error:\n\n\n\n```\nImportError: cannot import name QuotientRing\nError importing ipy_profile_sage - perhaps you should run %upgrade?\nWARNING: Loading of ipy_profile_sage failed.\n```\n",
    "created_at": "2013-01-04T14:15:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8383#issuecomment-74988",
    "user": "afleckenstein"
}
```

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

archive/issue_comments_074989.json:
```json
{
    "body": "You're running into circular imports. Symbolic functions are considerably slower compared to the current implementations in `sage/rings/arith.py`. Since these are used in many places in the Sage library, it would make sense to keep those and introduce symbolic versions in a new file (`sage/functions/arith.py` say). Then you need to make sure that the functions imported at the Sage command line are the symbolic ones.\n\nThanks for looking into this.",
    "created_at": "2013-01-04T14:22:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8383#issuecomment-74989",
    "user": "@burcin"
}
```

You're running into circular imports. Symbolic functions are considerably slower compared to the current implementations in `sage/rings/arith.py`. Since these are used in many places in the Sage library, it would make sense to keep those and introduce symbolic versions in a new file (`sage/functions/arith.py` say). Then you need to make sure that the functions imported at the Sage command line are the symbolic ones.

Thanks for looking into this.



---

archive/issue_comments_074990.json:
```json
{
    "body": "As I'm writing the symbolic version of sigma, it appears that a symbolic function created using BuiltinFunction has to have an explicit number of arguments. It is a little more work to write\n\n```\nsage: sigma(5, 1)\n```\n\nthan just\n\n```\nsage: sigma(5)\n```\n\nbut I'm not sure if there's a way around it.",
    "created_at": "2013-01-06T15:44:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8383#issuecomment-74990",
    "user": "afleckenstein"
}
```

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

archive/issue_comments_074991.json:
```json
{
    "body": "Hi, thanks for working on this!\n\nOne solution (this is one I'm using on #4102), is to write a wrapper function `sigma` that will take either one or two arguments and return the general symbolic function of two arguments accordingly:\n\n\n```\nsage: sigma(5)\nsymbolic_sigma(5, 1)\nsage: sigma(x, 2)\nsymbolic_sigma(x, 2)\n```\n\n\nThe symbolic function `symbolic_sigma` would inherit from `BuiltinFunction` and have two arguments. It's printed name could be just `sigma` instead of `symbolic_sigma` to lessen confusion.",
    "created_at": "2013-01-06T22:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8383#issuecomment-74991",
    "user": "@benjaminfjones"
}
```

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

archive/issue_comments_074992.json:
```json
{
    "body": "But all functions mentioned so far are expressible using Dirichlet generating functions, and it would make much more sense to make them just wrappers around that (nonexisting) functionality. The same applies to C-finite \"functions\" like `fibonacci`, `lucas_number1`, `lucas_number2`, which are generalized with #15714.",
    "created_at": "2014-06-11T05:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8383#issuecomment-74992",
    "user": "@rwst"
}
```

But all functions mentioned so far are expressible using Dirichlet generating functions, and it would make much more sense to make them just wrappers around that (nonexisting) functionality. The same applies to C-finite "functions" like `fibonacci`, `lucas_number1`, `lucas_number2`, which are generalized with #15714.



---

archive/issue_comments_074993.json:
```json
{
    "body": "Did somebody say [defining Dirichlet series](http://ask.sagemath.org/question/2540/defining-dirichlet-series)?  [Here is an implementation](http://www.wordpress.jonhanke.com/Software/Sage__Dirichlet_series/Dirichlet_series.sage) that I haven't had time to try out but which might be a good basis for that.  [This sage-support thread](https://groups.google.com/d/topic/sage-support/v7TFXKbAV0E) may also be relevant, though I don't know how advanced that psage code is.",
    "created_at": "2014-06-11T12:23:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8383#issuecomment-74993",
    "user": "@kcrisman"
}
```

Did somebody say [defining Dirichlet series](http://ask.sagemath.org/question/2540/defining-dirichlet-series)?  [Here is an implementation](http://www.wordpress.jonhanke.com/Software/Sage__Dirichlet_series/Dirichlet_series.sage) that I haven't had time to try out but which might be a good basis for that.  [This sage-support thread](https://groups.google.com/d/topic/sage-support/v7TFXKbAV0E) may also be relevant, though I don't know how advanced that psage code is.



---

archive/issue_comments_074994.json:
```json
{
    "body": "Thanks. I copied your comment to create #16477.",
    "created_at": "2014-06-12T16:29:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8383#issuecomment-74994",
    "user": "@rwst"
}
```

Thanks. I copied your comment to create #16477.



---

archive/issue_comments_074995.json:
```json
{
    "body": "Changing keywords from \"beginner\" to \"\".",
    "created_at": "2020-05-27T02:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8383#issuecomment-74995",
    "user": "@DaveWitteMorris"
}
```

Changing keywords from "beginner" to "".



---

archive/issue_comments_074996.json:
```json
{
    "body": "Removing the \"beginner\" tag from old tickets. Some could be returned to beginner-friendly status by adding a comment about what needs to be done. Some others might be easy for an experienced developer to finish.",
    "created_at": "2020-05-27T02:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8383#issuecomment-74996",
    "user": "@DaveWitteMorris"
}
```

Removing the "beginner" tag from old tickets. Some could be returned to beginner-friendly status by adding a comment about what needs to be done. Some others might be easy for an experienced developer to finish.
