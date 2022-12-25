# Issue 4102: Make special functions behave like PrimitiveFunction

archive/issues_004102.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @jasongrout @kcrisman @benjaminfjones dsm @burcin @eviatarbach\n\nThe motivation for this is\n\n\n```\nsage: plot(bessel_J(1, x), (x, 1, 10))\nTraceback (most recent call last):\n...\nTypeError: Unable to convert x (='1-1/8*x^2+1/192*x^4-1/9216*x^6+1/737280*x^8-1/88473600*x^10+1/14863564800*x^12-1/3329438515200*x^14+1/958878292377600*x^16+O(x^17)') to real number.\n```\n\n\nThe problem is that special functions, or at least `bessel_J`, can't currently be partially evaluated--that is, called with a `SymbolicExpression` as an argument.  The model of good behavior is `polylog`, for which the above method produces a perfectly nice plot\n\n\n```\nsage: polylog(1,x),(x,.1,.9) #makes a fine plot\n```\n\n\nSee discussion at http://groups.google.com/group/sage-support/browse_thread/thread/1b985b080ba2369e/7dee9eed953857f5#7dee9eed953857f5\n\nIssue created by migration from https://trac.sagemath.org/ticket/4102\n\n",
    "created_at": "2008-09-12T01:06:09Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.11",
    "title": "Make special functions behave like PrimitiveFunction",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4102",
    "user": "https://github.com/jicama"
}
```
Assignee: @burcin

CC:  @jasongrout @kcrisman @benjaminfjones dsm @burcin @eviatarbach

The motivation for this is


```
sage: plot(bessel_J(1, x), (x, 1, 10))
Traceback (most recent call last):
...
TypeError: Unable to convert x (='1-1/8*x^2+1/192*x^4-1/9216*x^6+1/737280*x^8-1/88473600*x^10+1/14863564800*x^12-1/3329438515200*x^14+1/958878292377600*x^16+O(x^17)') to real number.
```


The problem is that special functions, or at least `bessel_J`, can't currently be partially evaluated--that is, called with a `SymbolicExpression` as an argument.  The model of good behavior is `polylog`, for which the above method produces a perfectly nice plot


```
sage: polylog(1,x),(x,.1,.9) #makes a fine plot
```


See discussion at http://groups.google.com/group/sage-support/browse_thread/thread/1b985b080ba2369e/7dee9eed953857f5#7dee9eed953857f5

Issue created by migration from https://trac.sagemath.org/ticket/4102





---

archive/issue_comments_029539.json:
```json
{
    "body": "Orthogonal polynomials seem to work fine; you can plot the `legendre_P`, `hermite`, and `jacobi_P` polynomials with `plot(legendre_P(4, x), (x,-1,1))` and so on. So whatever magic they are using might work for the Bessel functions and other special functions.",
    "created_at": "2008-09-12T02:14:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29539",
    "user": "https://github.com/dandrake"
}
```

Orthogonal polynomials seem to work fine; you can plot the `legendre_P`, `hermite`, and `jacobi_P` polynomials with `plot(legendre_P(4, x), (x,-1,1))` and so on. So whatever magic they are using might work for the Bessel functions and other special functions.



---

archive/issue_comments_029540.json:
```json
{
    "body": "Changing keywords from \"\" to \"jason\".",
    "created_at": "2008-09-12T04:00:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29540",
    "user": "https://github.com/jasongrout"
}
```

Changing keywords from "" to "jason".



---

archive/issue_comments_029541.json:
```json
{
    "body": "Changing keywords from \"jason\" to \"\".",
    "created_at": "2008-09-12T04:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29541",
    "user": "https://github.com/jasongrout"
}
```

Changing keywords from "jason" to "".



---

archive/issue_comments_029542.json:
```json
{
    "body": "This ticket description was too broad. We have lots of tickets on fixing symbolic functions, see [symbolics/functions](symbolics-functions) for an overview.\n\nSee #3426 and #4230 for other tickets related to bessel functions. It would make sense to fix all these together, with a base class that handles the common properties of bessel functions (differentiation), and subclasses that implement numerical evaluation, etc. for each type.",
    "created_at": "2011-06-14T18:22:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29542",
    "user": "https://github.com/burcin"
}
```

This ticket description was too broad. We have lots of tickets on fixing symbolic functions, see [symbolics/functions](symbolics-functions) for an overview.

See #3426 and #4230 for other tickets related to bessel functions. It would make sense to fix all these together, with a base class that handles the common properties of bessel functions (differentiation), and subclasses that implement numerical evaluation, etc. for each type.



---

archive/issue_comments_029543.json:
```json
{
    "body": "See also #10636, which I somehow never saw before.  [This sage-support thread](https://groups.google.com/forum/?fromgroups=#!topic/sage-support/XzpN97E26qQ) yields an interesting related error:\n\n```\nsage: var('k')\nk\nsage: Z = sum( ((-1)^k*(x^(2*k+1))/factorial(2*k+1)),k,0,oo)\nsage: Z\n1/2*sqrt(pi)*sqrt(2)*sqrt(x)*bessel_j(1/2, x)\nsage: Z(x=3)\n1/2*sqrt(pi)*sqrt(2)*sqrt(3)*bessel_j(1/2, 3)\nsage: Z(x=3).n()\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\nsage.symbolic.expression.Expression._numerical_approx (sage/symbolic/expression.cpp:20822)()\n\nTypeError: cannot evaluate symbolic expression numerically\nsage: besse\nbessel_I  bessel_J  bessel_K  bessel_Y  \n```\n\nNote that we apparently aren't yet converting Maxima's Bessel properly to 'our' uppercase version because of this.",
    "created_at": "2012-09-16T03:05:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29543",
    "user": "https://github.com/kcrisman"
}
```

See also #10636, which I somehow never saw before.  [This sage-support thread](https://groups.google.com/forum/?fromgroups=#!topic/sage-support/XzpN97E26qQ) yields an interesting related error:

```
sage: var('k')
k
sage: Z = sum( ((-1)^k*(x^(2*k+1))/factorial(2*k+1)),k,0,oo)
sage: Z
1/2*sqrt(pi)*sqrt(2)*sqrt(x)*bessel_j(1/2, x)
sage: Z(x=3)
1/2*sqrt(pi)*sqrt(2)*sqrt(3)*bessel_j(1/2, 3)
sage: Z(x=3).n()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

sage.symbolic.expression.Expression._numerical_approx (sage/symbolic/expression.cpp:20822)()

TypeError: cannot evaluate symbolic expression numerically
sage: besse
bessel_I  bessel_J  bessel_K  bessel_Y  
```

Note that we apparently aren't yet converting Maxima's Bessel properly to 'our' uppercase version because of this.



---

archive/issue_comments_029544.json:
```json
{
    "body": "This wouldn't be hard to implement using #11143 as a template, but what to do about names? I guess new names for the symbolic Bessel functions should be chosen and deprecation notices added to the existing `Bessel_J` etc. \n\nWhat new names do people like in the interim? \n\n* `bessel_J_symbolic`\n* `bessel_J_sym`\n* `bessel_Js`\n\n???",
    "created_at": "2012-10-03T03:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29544",
    "user": "https://github.com/benjaminfjones"
}
```

This wouldn't be hard to implement using #11143 as a template, but what to do about names? I guess new names for the symbolic Bessel functions should be chosen and deprecation notices added to the existing `Bessel_J` etc. 

What new names do people like in the interim? 

* `bessel_J_symbolic`
* `bessel_J_sym`
* `bessel_Js`

???



---

archive/issue_comments_029545.json:
```json
{
    "body": "Replying to [comment:8 benjaminfjones]:\n> What new names do people like in the interim? \n> \n>  * `bessel_J_symbolic`\n>  * `bessel_J_sym`\n>  * `bessel_Js`\n> \n> ???\n\nWhat is wrong with taking over `bessel_{I,J,K,Y}`? Why do we need interim names?\n\n\nThanks for looking into this.",
    "created_at": "2012-10-03T11:22:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29545",
    "user": "https://github.com/burcin"
}
```

Replying to [comment:8 benjaminfjones]:
> What new names do people like in the interim? 
> 
>  * `bessel_J_symbolic`
>  * `bessel_J_sym`
>  * `bessel_Js`
> 
> ???

What is wrong with taking over `bessel_{I,J,K,Y}`? Why do we need interim names?


Thanks for looking into this.



---

archive/issue_comments_029546.json:
```json
{
    "body": "> What is wrong with taking over `bessel_{I,J,K,Y}`? Why do we need interim names?\nI concur.\n> >  * `bessel_J_symbolic`\nOne could use that as the \"symbolic\" class one and then do the usual `foo = Foo_Class()`?\n> Thanks for looking into this.\nAgreed!",
    "created_at": "2012-10-03T14:00:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29546",
    "user": "https://github.com/kcrisman"
}
```

> What is wrong with taking over `bessel_{I,J,K,Y}`? Why do we need interim names?
I concur.
> >  * `bessel_J_symbolic`
One could use that as the "symbolic" class one and then do the usual `foo = Foo_Class()`?
> Thanks for looking into this.
Agreed!



---

archive/issue_comments_029547.json:
```json
{
    "body": "Replying to [comment:8 benjaminfjones]:\n> What new names do people like in the interim? \n\nI agree with Burcin: just use `bessel_J` (etc) if possible.\n\nBut regardless of the name, I'd love to see this get in -- it will make teaching a PDE class a bit easier. (No more `lambda` expressions in the plots...) Thanks for working on this!",
    "created_at": "2012-10-03T16:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29547",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:8 benjaminfjones]:
> What new names do people like in the interim? 

I agree with Burcin: just use `bessel_J` (etc) if possible.

But regardless of the name, I'd love to see this get in -- it will make teaching a PDE class a bit easier. (No more `lambda` expressions in the plots...) Thanks for working on this!



---

archive/issue_comments_029548.json:
```json
{
    "body": "I thought I'd post some work in progress for all the Bessel function fans in the crowd. There is still work to be done, e.g.\n\n* getting symbolic integration via Maxima to work\n* adding maxima, scipy, PARI, etc. to the implemented backend systems\n* more documentation and doctests\n\nbut at this point the patch applies cleanly to 5.4.1 and all the doctests in `sage/functions/special.py` pass.\n\nIf you are interested, have a look at the doctests included with the `Bessel` function for examples and let me know if you see any serious problems (other than the deficits I've listed above).\n\nThanks!",
    "created_at": "2012-11-19T07:10:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29548",
    "user": "https://github.com/benjaminfjones"
}
```

I thought I'd post some work in progress for all the Bessel function fans in the crowd. There is still work to be done, e.g.

* getting symbolic integration via Maxima to work
* adding maxima, scipy, PARI, etc. to the implemented backend systems
* more documentation and doctests

but at this point the patch applies cleanly to 5.4.1 and all the doctests in `sage/functions/special.py` pass.

If you are interested, have a look at the doctests included with the `Bessel` function for examples and let me know if you see any serious problems (other than the deficits I've listed above).

Thanks!



---

archive/issue_comments_029549.json:
```json
{
    "body": "work in progress making Bessel functions symbolic",
    "created_at": "2012-11-19T07:11:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29549",
    "user": "https://github.com/benjaminfjones"
}
```

work in progress making Bessel functions symbolic



---

archive/issue_comments_029550.json:
```json
{
    "body": "Attachment [trac_symbolic_bessel.metaclass.2.patch](tarball://root/attachments/some-uuid/ticket4102/trac_symbolic_bessel.metaclass.2.patch) by @kcrisman created at 2012-11-20 01:01:12\n\nNice!  A few comments of the type you solicited:\n* Why `typ` and not `type`?  Some Python reserved thing, maybe?  But it looks like a typ-o to the (quickly reading) end user.\n* I'd like to be able to plot `f(x) = Bessel(0)` but maybe that doesn't make sense?  I guess a variable is necessary... anyway, just throwing it out there.\n* `f = maxima(Bessel(typ='K')(x,y))` turns out great, but does it convert back?  Like `f.derivative('y')` is `-(bessel_k(x+1,y)+bessel_k(x-1,y))/2`, but does it then (when put in the `_sage_` method) go back to \"our\" uppercase Bessel functions?\n* Maybe Python 3 string formatting?  Though I am not sure how to mix that with LaTeX braces.\n* At least some of the error messages should be in doctests, maybe the ones with the wrong type and a non-implemented system.\n* `class_attrs['_conversions'] = {} ` --- what do we do with this in Maxima, then?  Maybe it's better to raise an error; Maxima tends to otherwise just take things as new variables, which could be dangerous.\n* How many of the currently-deleted doctests do you think would be worth preserving in the long run?  Any deprecation needed here?\nAnyway, clearly a lot of planning and looks very promising!",
    "created_at": "2012-11-20T01:01:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29550",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_symbolic_bessel.metaclass.2.patch](tarball://root/attachments/some-uuid/ticket4102/trac_symbolic_bessel.metaclass.2.patch) by @kcrisman created at 2012-11-20 01:01:12

Nice!  A few comments of the type you solicited:
* Why `typ` and not `type`?  Some Python reserved thing, maybe?  But it looks like a typ-o to the (quickly reading) end user.
* I'd like to be able to plot `f(x) = Bessel(0)` but maybe that doesn't make sense?  I guess a variable is necessary... anyway, just throwing it out there.
* `f = maxima(Bessel(typ='K')(x,y))` turns out great, but does it convert back?  Like `f.derivative('y')` is `-(bessel_k(x+1,y)+bessel_k(x-1,y))/2`, but does it then (when put in the `_sage_` method) go back to "our" uppercase Bessel functions?
* Maybe Python 3 string formatting?  Though I am not sure how to mix that with LaTeX braces.
* At least some of the error messages should be in doctests, maybe the ones with the wrong type and a non-implemented system.
* `class_attrs['_conversions'] = {} ` --- what do we do with this in Maxima, then?  Maybe it's better to raise an error; Maxima tends to otherwise just take things as new variables, which could be dangerous.
* How many of the currently-deleted doctests do you think would be worth preserving in the long run?  Any deprecation needed here?
Anyway, clearly a lot of planning and looks very promising!



---

archive/issue_comments_029551.json:
```json
{
    "body": "Thanks for the patch. Bessel functions are symbolic with so few lines of code. Amazing. :)\n\nI like the metaclass idea. That never occured to me before as an option for functions with parameters, like the order here. I have a few questions:\n\n- what is the advantage of creating a new symbolic function for each (type, order) pair, instead of having a generic function for each type that takes the order as a parameter? The latter would be similar to the design of the `psi()` function in GiNaC/Pynac.\n\n- wouldn't this approach make life harder if in the future we want to add exact evaluation method for Bessel_J only?\n\nI am also concerned about blowing up the symbolic function registry with these instances. Note that we keep an entry in a C++ list with a pointer to all the possible custom methods, and a Python dictionary with a function -> Pynac id mapping for each subclass of `BuiltinFunction` that is instantiated.\n\nBTW, I suggest moving this code to a new file `sage/functions/bessel.py`.",
    "created_at": "2012-11-20T11:13:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29551",
    "user": "https://github.com/burcin"
}
```

Thanks for the patch. Bessel functions are symbolic with so few lines of code. Amazing. :)

I like the metaclass idea. That never occured to me before as an option for functions with parameters, like the order here. I have a few questions:

- what is the advantage of creating a new symbolic function for each (type, order) pair, instead of having a generic function for each type that takes the order as a parameter? The latter would be similar to the design of the `psi()` function in GiNaC/Pynac.

- wouldn't this approach make life harder if in the future we want to add exact evaluation method for Bessel_J only?

I am also concerned about blowing up the symbolic function registry with these instances. Note that we keep an entry in a C++ list with a pointer to all the possible custom methods, and a Python dictionary with a function -> Pynac id mapping for each subclass of `BuiltinFunction` that is instantiated.

BTW, I suggest moving this code to a new file `sage/functions/bessel.py`.



---

archive/issue_comments_029552.json:
```json
{
    "body": "Replying to [comment:13 kcrisman]:\n\nThanks for the comments. I finally found some time to get back to this ticket :) \n\n> Nice!  A few comments of the type you solicited:\n>  * Why `typ` and not `type`?  Some Python reserved thing, maybe?  But it looks like a typ-o to the (quickly reading) end user.\n\nThat was intentional, I was trying not to shadow the builtin name.\n\n>  * I'd like to be able to plot `f(x) = Bessel(0)` but maybe that doesn't make sense?  I guess a variable is necessary... anyway, just throwing it out there.\n\nI think `f(x) = Bessel(0,x)` is better, I don't like `x` being implicit on the right hand side.\n\n>  * `f = maxima(Bessel(typ='K')(x,y))` turns out great, but does it convert back?  Like `f.derivative('y')` is `-(bessel_k(x+1,y)+bessel_k(x-1,y))/2`, but does it then (when put in the `_sage_` method) go back to \"our\" uppercase Bessel functions?\n\nGood question, I haven't tested it out. I think I'm going to rewrite most of the code anyway so I'll keep this in mind.\n\n>  * Maybe Python 3 string formatting?  Though I am not sure how to mix that with LaTeX braces.\n\n???\n\n>  * At least some of the error messages should be in doctests, maybe the ones with the wrong type and a non-implemented system.\n\nGood point, I'll make sure to doctest the exceptions.\n\n>  * `class_attrs['_conversions'] = {} ` --- what do we do with this in Maxima, then?  Maybe it's better to raise an error; Maxima tends to otherwise just take things as new variables, which could be dangerous.\n\nI don't know about this. I had this in the case of the single parameter functions like `Bessel(1,'K')` that Maxima doesn't have equivalents for (it just has the two parameter functions). I think I'll scrap the idea of having all infinitely many one-parameter Bessel functions registered as their own symbolic functions (see Burcin's comments below).\n\n>  * How many of the currently-deleted doctests do you think would be worth preserving in the long run?  Any deprecation needed here?\n\nIdeally all of them. Some will need to be modified because of the change in numerical back-end.\n\n> Anyway, clearly a lot of planning and looks very promising!",
    "created_at": "2012-12-27T20:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29552",
    "user": "https://github.com/benjaminfjones"
}
```

Replying to [comment:13 kcrisman]:

Thanks for the comments. I finally found some time to get back to this ticket :) 

> Nice!  A few comments of the type you solicited:
>  * Why `typ` and not `type`?  Some Python reserved thing, maybe?  But it looks like a typ-o to the (quickly reading) end user.

That was intentional, I was trying not to shadow the builtin name.

>  * I'd like to be able to plot `f(x) = Bessel(0)` but maybe that doesn't make sense?  I guess a variable is necessary... anyway, just throwing it out there.

I think `f(x) = Bessel(0,x)` is better, I don't like `x` being implicit on the right hand side.

>  * `f = maxima(Bessel(typ='K')(x,y))` turns out great, but does it convert back?  Like `f.derivative('y')` is `-(bessel_k(x+1,y)+bessel_k(x-1,y))/2`, but does it then (when put in the `_sage_` method) go back to "our" uppercase Bessel functions?

Good question, I haven't tested it out. I think I'm going to rewrite most of the code anyway so I'll keep this in mind.

>  * Maybe Python 3 string formatting?  Though I am not sure how to mix that with LaTeX braces.

???

>  * At least some of the error messages should be in doctests, maybe the ones with the wrong type and a non-implemented system.

Good point, I'll make sure to doctest the exceptions.

>  * `class_attrs['_conversions'] = {} ` --- what do we do with this in Maxima, then?  Maybe it's better to raise an error; Maxima tends to otherwise just take things as new variables, which could be dangerous.

I don't know about this. I had this in the case of the single parameter functions like `Bessel(1,'K')` that Maxima doesn't have equivalents for (it just has the two parameter functions). I think I'll scrap the idea of having all infinitely many one-parameter Bessel functions registered as their own symbolic functions (see Burcin's comments below).

>  * How many of the currently-deleted doctests do you think would be worth preserving in the long run?  Any deprecation needed here?

Ideally all of them. Some will need to be modified because of the change in numerical back-end.

> Anyway, clearly a lot of planning and looks very promising!



---

archive/issue_comments_029553.json:
```json
{
    "body": "Replying to [comment:14 burcin]:\n\nThanks for looking at it!\n\n> Thanks for the patch. Bessel functions are symbolic with so few lines of code. Amazing. :)\n> \n> I like the metaclass idea. That never occured to me before as an option for functions with parameters, like the order here. I have a few questions:\n> \n>  - what is the advantage of creating a new symbolic function for each (type, order) pair, instead of having a generic function for each type that takes the order as a parameter? The latter would be similar to the design of the `psi()` function in GiNaC/Pynac.\n\nThe advantage I had in mind was just code reuse. In hindsight though, this approach makes the code more complicated and less maintainable that it needs to be. I'm going to refactor it into four generic functions in `sage/functions/bessel.py` as you suggest.\n\n>  - wouldn't this approach make life harder if in the future we want to add exact evaluation method for Bessel_J only?\n\nGood point.. \n\n> I am also concerned about blowing up the symbolic function registry with these instances. Note that we keep an entry in a C++ list with a pointer to all the possible custom methods, and a Python dictionary with a function -> Pynac id mapping for each subclass of `BuiltinFunction` that is instantiated.\n\nAlso a good point. This occurred to me, but I didn't think through the consequences very much. I can see it being a problem if a user can inadvertently create a very large number of symbolic functions at runtime by doing something innocuous like:\n\n\n```\nsage: point([ (k, Bessel(k, 'J')(pi)) for k in range(1000) ])\n... (1000 new symbolic function classes created!)\n```\n\n\n\n> BTW, I suggest moving this code to a new file `sage/functions/bessel.py`.\n\nGood idea. New patch coming soon...",
    "created_at": "2012-12-27T20:27:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29553",
    "user": "https://github.com/benjaminfjones"
}
```

Replying to [comment:14 burcin]:

Thanks for looking at it!

> Thanks for the patch. Bessel functions are symbolic with so few lines of code. Amazing. :)
> 
> I like the metaclass idea. That never occured to me before as an option for functions with parameters, like the order here. I have a few questions:
> 
>  - what is the advantage of creating a new symbolic function for each (type, order) pair, instead of having a generic function for each type that takes the order as a parameter? The latter would be similar to the design of the `psi()` function in GiNaC/Pynac.

The advantage I had in mind was just code reuse. In hindsight though, this approach makes the code more complicated and less maintainable that it needs to be. I'm going to refactor it into four generic functions in `sage/functions/bessel.py` as you suggest.

>  - wouldn't this approach make life harder if in the future we want to add exact evaluation method for Bessel_J only?

Good point.. 

> I am also concerned about blowing up the symbolic function registry with these instances. Note that we keep an entry in a C++ list with a pointer to all the possible custom methods, and a Python dictionary with a function -> Pynac id mapping for each subclass of `BuiltinFunction` that is instantiated.

Also a good point. This occurred to me, but I didn't think through the consequences very much. I can see it being a problem if a user can inadvertently create a very large number of symbolic functions at runtime by doing something innocuous like:


```
sage: point([ (k, Bessel(k, 'J')(pi)) for k in range(1000) ])
... (1000 new symbolic function classes created!)
```



> BTW, I suggest moving this code to a new file `sage/functions/bessel.py`.

Good idea. New patch coming soon...



---

archive/issue_comments_029554.json:
```json
{
    "body": "> >  * Maybe Python 3 string formatting?  Though I am not sure how to mix that with LaTeX braces.\n> \n> ???\n\nSuch as [this](http://docs.python.org/3.1/library/stdtypes.html#str.format) and [this](http://docs.python.org/3.1/library/string.html#formatstrings).  Just for forward-compatibility (instead of the percent business).  Problem is that when I looked for ways to get around braces \"naturally\" occurring in LaTeX, there weren't necessarily a lot of them.  (Ways, that is.)",
    "created_at": "2012-12-27T20:44:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29554",
    "user": "https://github.com/kcrisman"
}
```

> >  * Maybe Python 3 string formatting?  Though I am not sure how to mix that with LaTeX braces.
> 
> ???

Such as [this](http://docs.python.org/3.1/library/stdtypes.html#str.format) and [this](http://docs.python.org/3.1/library/string.html#formatstrings).  Just for forward-compatibility (instead of the percent business).  Problem is that when I looked for ways to get around braces "naturally" occurring in LaTeX, there weren't necessarily a lot of them.  (Ways, that is.)



---

archive/issue_comments_029555.json:
```json
{
    "body": "Replying to [comment:17 kcrisman]:\n> > >  * Maybe Python 3 string formatting?  Though I am not sure how to mix that with LaTeX braces.\n> > \n> > ???\n> \n> Such as [this](http://docs.python.org/3.1/library/stdtypes.html#str.format) and [this](http://docs.python.org/3.1/library/string.html#formatstrings).  Just for forward-compatibility (instead of the percent business).  Problem is that when I looked for ways to get around braces \"naturally\" occurring in LaTeX, there weren't necessarily a lot of them.  (Ways, that is.)\n\nOh, right. I just didn't see what in the code you were referring to. I see now.\n\nAnyway, to one of your earlier questions, with the new code I'm about to post the following conversions to and from Maxima work great:\n\n\n```\nsage: mb = maxima(bessel_I(1,x))\nsage: mb.sage()                 \nbessel_I(1, x)\nsage:  x,y = var('x,y')\nsage:  f = maxima(Bessel(typ='K')(x,y))\nsage: f.derivative('x')\n%pi*csc(%pi*x)*('diff(bessel_i(-x,y),x,1)-'diff(bessel_i(x,y),x,1))/2-%pi*bessel_k(x,y)*cot(%pi*x)\nsage: m = f.derivative('x')\nsage: m.sage()\n-1/2*(x*bessel_I(-x, y)/y - x*bessel_I(x, y)/y + bessel_I(-x - 1, y) + bessel_I(x - 1, y))*pi*csc(pi*x) - pi*cot(pi*x)*bessel_K(x, y)\n```\n",
    "created_at": "2012-12-27T23:53:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29555",
    "user": "https://github.com/benjaminfjones"
}
```

Replying to [comment:17 kcrisman]:
> > >  * Maybe Python 3 string formatting?  Though I am not sure how to mix that with LaTeX braces.
> > 
> > ???
> 
> Such as [this](http://docs.python.org/3.1/library/stdtypes.html#str.format) and [this](http://docs.python.org/3.1/library/string.html#formatstrings).  Just for forward-compatibility (instead of the percent business).  Problem is that when I looked for ways to get around braces "naturally" occurring in LaTeX, there weren't necessarily a lot of them.  (Ways, that is.)

Oh, right. I just didn't see what in the code you were referring to. I see now.

Anyway, to one of your earlier questions, with the new code I'm about to post the following conversions to and from Maxima work great:


```
sage: mb = maxima(bessel_I(1,x))
sage: mb.sage()                 
bessel_I(1, x)
sage:  x,y = var('x,y')
sage:  f = maxima(Bessel(typ='K')(x,y))
sage: f.derivative('x')
%pi*csc(%pi*x)*('diff(bessel_i(-x,y),x,1)-'diff(bessel_i(x,y),x,1))/2-%pi*bessel_k(x,y)*cot(%pi*x)
sage: m = f.derivative('x')
sage: m.sage()
-1/2*(x*bessel_I(-x, y)/y - x*bessel_I(x, y)/y + bessel_I(-x - 1, y) + bessel_I(x - 1, y))*pi*csc(pi*x) - pi*cot(pi*x)*bessel_K(x, y)
```




---

archive/issue_comments_029556.json:
```json
{
    "body": "Attachment [trac_symbolic_bessel_v2.patch](tarball://root/attachments/some-uuid/ticket4102/trac_symbolic_bessel_v2.patch) by @benjaminfjones created at 2012-12-28 01:48:57\n\nmore work in progress",
    "created_at": "2012-12-28T01:48:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29556",
    "user": "https://github.com/benjaminfjones"
}
```

Attachment [trac_symbolic_bessel_v2.patch](tarball://root/attachments/some-uuid/ticket4102/trac_symbolic_bessel_v2.patch) by @benjaminfjones created at 2012-12-28 01:48:57

more work in progress



---

archive/issue_comments_029557.json:
```json
{
    "body": "Just as an FYI, [this ask.sagemath question](http://ask.sagemath.org/question/2129/arbitrary-precision-bessely) wants lots and lots of precision on Bessel Y.  Which I think will be provided here via mpmath - just pointing out we should doctest it.",
    "created_at": "2013-01-03T15:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29557",
    "user": "https://github.com/kcrisman"
}
```

Just as an FYI, [this ask.sagemath question](http://ask.sagemath.org/question/2129/arbitrary-precision-bessely) wants lots and lots of precision on Bessel Y.  Which I think will be provided here via mpmath - just pointing out we should doctest it.



---

archive/issue_comments_029558.json:
```json
{
    "body": "Also, I think that #3426 and #4230 probably would be solved by a successful resolution of this ticket.  Let's make sure to include any suggested (and useful) doctests from there here.",
    "created_at": "2013-01-03T15:38:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29558",
    "user": "https://github.com/kcrisman"
}
```

Also, I think that #3426 and #4230 probably would be solved by a successful resolution of this ticket.  Let's make sure to include any suggested (and useful) doctests from there here.



---

archive/issue_comments_029559.json:
```json
{
    "body": "Yet more work in progress, added lots of doctests, in particular to show that problems in #4230 and #3426 are fixed by this patch. One feature this patch adds is the ability to solve\nBessel's diffeq (using Maxima) and get a usable symbolic solution back (see the doctests in the module level docstring and in the Bessel() function). \n\nAdded brief mathematical exposition on the module docstring as well as some usage EXAMPLES.\n\nI think the patch is more or less ready for initial review. All tests withing the new file `sage/functions/bessel.py` pass on my machine and sage-5.6.beta3, but there are several doctests failing in other places that reference the Bessel functions. I'll work on patching those up for the next iteration.",
    "created_at": "2013-01-13T05:05:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29559",
    "user": "https://github.com/benjaminfjones"
}
```

Yet more work in progress, added lots of doctests, in particular to show that problems in #4230 and #3426 are fixed by this patch. One feature this patch adds is the ability to solve
Bessel's diffeq (using Maxima) and get a usable symbolic solution back (see the doctests in the module level docstring and in the Bessel() function). 

Added brief mathematical exposition on the module docstring as well as some usage EXAMPLES.

I think the patch is more or less ready for initial review. All tests withing the new file `sage/functions/bessel.py` pass on my machine and sage-5.6.beta3, but there are several doctests failing in other places that reference the Bessel functions. I'll work on patching those up for the next iteration.



---

archive/issue_comments_029560.json:
```json
{
    "body": "more work in progress, v3",
    "created_at": "2013-01-13T05:06:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29560",
    "user": "https://github.com/benjaminfjones"
}
```

more work in progress, v3



---

archive/issue_comments_029561.json:
```json
{
    "body": "Attachment [trac_symbolic_bessel_v3.patch](tarball://root/attachments/some-uuid/ticket4102/trac_symbolic_bessel_v3.patch) by @kcrisman created at 2013-02-08 17:36:59\n\nDumb comments since I don't have time for proper review - and more importantly, there are no obvious horrible things (though I haven't gone in depth with branches yet).   If all this really works and there are no typos, I think this will be a VERY nice addition.\n* `unqiue` typo\n* `Verfify` typo\n* `increasin` typo\n* I don't know why, but the math following \"It follows from Bessel's...\" doesn't look right in the doc (the `:math:` directive is not parsed)\n* Is \\operatorname{bessel\\_I}(\\alpha, x) standard or should we just just the I sub whatever?\n* ``test_relation()`` needs to be in double back ticks or have a link to the appropriate place in the ref manual\n* Trac tickets should use `:trac:` syntax\n* Does `f(x) = Bessel(0): plot(f, (x, 1, 10))` work, or must one use `Bessel(0)(x)`?  The example after that makes it look like maybe not...\n* Bessel Y and Bessel K need a little filling out - and one of the `:math:` directives doesn't show up at all, the other isn't parsed right for some reason again\n* I'd personally get rid of the whitespace changes in sage/functions/special.py - unlikely to have an effect, but not really necessary.\n* How should we deal with the removal of the `\"maxima\"` and `\"pari\"` arguments?  I'm not sure if it's really feasible to have a deprecation period for that, but we should discuss it.\n* I suppose we don't need to keep *all* old tests, but some of them are rather different and might be worth putting in a TESTS section somewhere, just so that we don't have some unexpected regression only they catch.\n* The switch to alpha from nu - I would rather not deprecate this either, but in principle someone could have used it as a keyword argument in the past...",
    "created_at": "2013-02-08T17:36:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29561",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_symbolic_bessel_v3.patch](tarball://root/attachments/some-uuid/ticket4102/trac_symbolic_bessel_v3.patch) by @kcrisman created at 2013-02-08 17:36:59

Dumb comments since I don't have time for proper review - and more importantly, there are no obvious horrible things (though I haven't gone in depth with branches yet).   If all this really works and there are no typos, I think this will be a VERY nice addition.
* `unqiue` typo
* `Verfify` typo
* `increasin` typo
* I don't know why, but the math following "It follows from Bessel's..." doesn't look right in the doc (the `:math:` directive is not parsed)
* Is \operatorname{bessel\_I}(\alpha, x) standard or should we just just the I sub whatever?
* ``test_relation()`` needs to be in double back ticks or have a link to the appropriate place in the ref manual
* Trac tickets should use `:trac:` syntax
* Does `f(x) = Bessel(0): plot(f, (x, 1, 10))` work, or must one use `Bessel(0)(x)`?  The example after that makes it look like maybe not...
* Bessel Y and Bessel K need a little filling out - and one of the `:math:` directives doesn't show up at all, the other isn't parsed right for some reason again
* I'd personally get rid of the whitespace changes in sage/functions/special.py - unlikely to have an effect, but not really necessary.
* How should we deal with the removal of the `"maxima"` and `"pari"` arguments?  I'm not sure if it's really feasible to have a deprecation period for that, but we should discuss it.
* I suppose we don't need to keep *all* old tests, but some of them are rather different and might be worth putting in a TESTS section somewhere, just so that we don't have some unexpected regression only they catch.
* The switch to alpha from nu - I would rather not deprecate this either, but in principle someone could have used it as a keyword argument in the past...



---

archive/issue_comments_029562.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-02-08T18:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29562",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_029563.json:
```json
{
    "body": "Here's the only failures I got with 5.7.beta3.\n\n```\nsage -t  \"devel/sage-main/sage/calculus/desolvers.py\"       \n**********************************************************************\nFile \"/Users/.../sage-5.7.beta3/devel/sage-main/sage/calculus/desolvers.py\", line 252:\n    sage: desolve(x^2*diff(y,x,x)+x*diff(y,x)+(x^2-4)*y==0,y)\nExpected:\n    k1*bessel_j(2, x) + k2*bessel_y(2, x)\nGot:\n    k1*bessel_J(2, x) + k2*bessel_Y(2, x)\n**********************************************************************\n1 items had failures:\n   1 of  62 in __main__.example_1\n***Test Failed*** 1 failures.\n\t [10.1 s]\n```\n\nHmm, should we keep the lowercase versions around, or was that actually an error that we never parsed those?  Apparently it was pure Maxima output, looking at the old code, so just replace with the actual return value.\n\n```\nsage -t  \"devel/sage-main/sage/calculus/wester.py\"          \n**********************************************************************\nFile \"/Users/.../sage-5.7.beta3/devel/sage-main/sage/calculus/wester.py\", line 39:\n    sage: bessel_J (2, 1+I)\nExpected:\n    0.0415798869439621 + 0.247397641513306*I\nGot:\n    bessel_J(2, I + 1)\n**********************************************************************\n1 items had failures:\n   1 of 200 in __main__.example_0\n***Test Failed*** 1 failures.\n\t [4.4 s]\n```\n\nEasy enough to fix - we could even add the `n()` version there.  Actually, we probably should, since the test is probably testing for something - we'll have to just read that quick.\n\n```\nsage -t  \"devel/sage-main/sage/functions/special.py\"        \n**********************************************************************\nFile \"/Users/.../sage-5.7.beta3/devel/sage-main/sage/functions/special.py\", line 521:\n    sage: n(bessel_J(3,10,\"maxima\"))\nException raised:\n    Traceback (most recent call last):\n    sage: n(bessel_J(3,10,\"maxima\"))\n      File \"function.pyx\", line 354, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:3976)\n    TypeError: Symbolic function bessel_J takes exactly 2 arguments (3 given)\n**********************************************************************\nFile \"/Users/.../sage-5.7.beta3/devel/sage-main/sage/functions/special.py\", line 536:\n    sage: n(bessel_J(3,10,\"maxima\"))\nException raised:\n        n(bessel_J(Integer(3),Integer(10),\"maxima\"))###line 536:\n    sage: n(bessel_J(3,10,\"maxima\"))\n      File \"function.pyx\", line 354, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:3976)\n    TypeError: Symbolic function bessel_J takes exactly 2 arguments (3 given)\n**********************************************************************\n2 items had failures:\n   1 of   5 in __main__.example_8\n   1 of   5 in __main__.example_9\n***Test Failed*** 2 failures.\n\t [3.8 s]\n```\n\nHmm, here is where that potential deprecation I mentioned might come in.\n\n```\nsage -t  \"devel/sage-main/sage/symbolic/random_tests.py\"    \n**********************************************************************\nFile \"/Users/.../sage-5.7.beta3/devel/sage-main/sage/symbolic/random_tests.py\", line 236:\n    sage: print \"ignore this\";  random_expr(50, nvars=3, coeff_generator=CDF.random_element) # random\nException raised:\n<snip>\n      File \"misc.pyx\", line 209, in sage.structure.misc.getattr_from_other_class (sage/structure/misc.c:1488)\n    AttributeError: 'sage.rings.complex_interval.ComplexIntervalFieldElement' object has no attribute 'arcsin'\n**********************************************************************\n```\n\nApparently the usual craziness with random expression has reached new heights with these extra functions.   I suggest we just try a different seed or something.  Not every random expression will be meaningful, for instance.",
    "created_at": "2013-02-08T18:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29563",
    "user": "https://github.com/kcrisman"
}
```

Here's the only failures I got with 5.7.beta3.

```
sage -t  "devel/sage-main/sage/calculus/desolvers.py"       
**********************************************************************
File "/Users/.../sage-5.7.beta3/devel/sage-main/sage/calculus/desolvers.py", line 252:
    sage: desolve(x^2*diff(y,x,x)+x*diff(y,x)+(x^2-4)*y==0,y)
Expected:
    k1*bessel_j(2, x) + k2*bessel_y(2, x)
Got:
    k1*bessel_J(2, x) + k2*bessel_Y(2, x)
**********************************************************************
1 items had failures:
   1 of  62 in __main__.example_1
***Test Failed*** 1 failures.
	 [10.1 s]
```

Hmm, should we keep the lowercase versions around, or was that actually an error that we never parsed those?  Apparently it was pure Maxima output, looking at the old code, so just replace with the actual return value.

```
sage -t  "devel/sage-main/sage/calculus/wester.py"          
**********************************************************************
File "/Users/.../sage-5.7.beta3/devel/sage-main/sage/calculus/wester.py", line 39:
    sage: bessel_J (2, 1+I)
Expected:
    0.0415798869439621 + 0.247397641513306*I
Got:
    bessel_J(2, I + 1)
**********************************************************************
1 items had failures:
   1 of 200 in __main__.example_0
***Test Failed*** 1 failures.
	 [4.4 s]
```

Easy enough to fix - we could even add the `n()` version there.  Actually, we probably should, since the test is probably testing for something - we'll have to just read that quick.

```
sage -t  "devel/sage-main/sage/functions/special.py"        
**********************************************************************
File "/Users/.../sage-5.7.beta3/devel/sage-main/sage/functions/special.py", line 521:
    sage: n(bessel_J(3,10,"maxima"))
Exception raised:
    Traceback (most recent call last):
    sage: n(bessel_J(3,10,"maxima"))
      File "function.pyx", line 354, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:3976)
    TypeError: Symbolic function bessel_J takes exactly 2 arguments (3 given)
**********************************************************************
File "/Users/.../sage-5.7.beta3/devel/sage-main/sage/functions/special.py", line 536:
    sage: n(bessel_J(3,10,"maxima"))
Exception raised:
        n(bessel_J(Integer(3),Integer(10),"maxima"))###line 536:
    sage: n(bessel_J(3,10,"maxima"))
      File "function.pyx", line 354, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:3976)
    TypeError: Symbolic function bessel_J takes exactly 2 arguments (3 given)
**********************************************************************
2 items had failures:
   1 of   5 in __main__.example_8
   1 of   5 in __main__.example_9
***Test Failed*** 2 failures.
	 [3.8 s]
```

Hmm, here is where that potential deprecation I mentioned might come in.

```
sage -t  "devel/sage-main/sage/symbolic/random_tests.py"    
**********************************************************************
File "/Users/.../sage-5.7.beta3/devel/sage-main/sage/symbolic/random_tests.py", line 236:
    sage: print "ignore this";  random_expr(50, nvars=3, coeff_generator=CDF.random_element) # random
Exception raised:
<snip>
      File "misc.pyx", line 209, in sage.structure.misc.getattr_from_other_class (sage/structure/misc.c:1488)
    AttributeError: 'sage.rings.complex_interval.ComplexIntervalFieldElement' object has no attribute 'arcsin'
**********************************************************************
```

Apparently the usual craziness with random expression has reached new heights with these extra functions.   I suggest we just try a different seed or something.  Not every random expression will be meaningful, for instance.



---

archive/issue_comments_029564.json:
```json
{
    "body": "Needs work:\n* doctest fixes, various minor documentation and other issues\n\nAnd needs review on the code itself :-)\n\nBut now it's really looking tractable to finish this off.",
    "created_at": "2013-02-08T18:15:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29564",
    "user": "https://github.com/kcrisman"
}
```

Needs work:
* doctest fixes, various minor documentation and other issues

And needs review on the code itself :-)

But now it's really looking tractable to finish this off.



---

archive/issue_comments_029565.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-02-08T18:15:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29565",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_029566.json:
```json
{
    "body": "Replying to [comment:22 kcrisman]:\n\nThanks for looking over the patch!\n\n> Dumb comments since I don't have time for proper review - and more importantly, there are no obvious horrible things (though I haven't gone in depth with branches yet).   If all this really works and there are no typos, I think this will be a VERY nice addition.\n>  * `unqiue` typo\n>  * `Verfify` typo\n>  * `increasin` typo\n>  * I don't know why, but the math following \"It follows from Bessel's...\" doesn't look right in the doc (the `:math:` directive is not parsed)\n\nFixed, it was a one space indentation problem.\n\n>  * Is \\operatorname{bessel\\_I}(\\alpha, x) standard or should we just just the I sub whatever?\n\nI was unsure about this. I think now it makes most sense to just stick with I_\\alpha when in a math block.\n\n>  * ``test_relation()`` needs to be in double back ticks or have a link to the appropriate place in the ref manual\n>  * Trac tickets should use `:trac:` syntax\n>  * Does `f(x) = Bessel(0): plot(f, (x, 1, 10))` work, or must one use `Bessel(0)(x)`?  The example after that makes it look like maybe not...\n\nThe way the code works you have to specify the variable on the right hand side, e.g.:\n\n\n```\nsage: f(x) = Bessel(0)(x)\nsage: f(x) = bessel_I(0, x)\n```\n\n\nThis is because `Bessel()` returns lambda functions under the hood. Personally, I prefer having the variable dependence made explicit, but I'm open to suggestions if there are other\nways you can think of to get that functionality.\n\n>  * Bessel Y and Bessel K need a little filling out - and one of the `:math:` directives doesn't show up at all, the other isn't parsed right for some reason again\n\nI'll work on Bessel Y and K, I realize now that you mention it that I didn't fill in the definitions there :). Anyone with good doctest suggestions for these is welcome to chime in, I'll add the tests if you can think of interesting or relevant ones.\n\n>  * I'd personally get rid of the whitespace changes in sage/functions/special.py - unlikely to have an effect, but not really necessary.\n\nYep, you're right.\n\n>  * How should we deal with the removal of the `\"maxima\"` and `\"pari\"` arguments?  I'm not sure if it's really feasible to have a deprecation period for that, but we should discuss it.\n\nThis is a question that's been troubling me. I don't know how to make the deprecation happen and make progress here without renaming the new functions and then swapping them in when the deprecation period is over. The infrastructure we have for adding symbolic functions (inheriting from `BuiltinFunction`, etc) doesn't support any kind of system arguments without overriding `call()`.\n\nAt least existing code that uses the Bessel functions as they are now in Sage won't break unless they explicitly use the system argument.\n\nMaybe `@`burcin has a suggestion here?\n\n>  * I suppose we don't need to keep *all* old tests, but some of them are rather different and might be worth putting in a TESTS section somewhere, just so that we don't have some unexpected regression only they catch.\n\nGood point, I'll see what I can salvage.\n\n>  * The switch to alpha from nu - I would rather not deprecate this either, but in principle someone could have used it as a keyword argument in the past...\n\nIt doesn't make a difference to me, I used alpha because that's what's on the wikipedia page :) Abramowitz & Stegun uses n or \\nu and so does the mpmath documentation. I can easily switch \\alpha to \\nu with some editor-fu.",
    "created_at": "2013-02-13T07:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29566",
    "user": "https://github.com/benjaminfjones"
}
```

Replying to [comment:22 kcrisman]:

Thanks for looking over the patch!

> Dumb comments since I don't have time for proper review - and more importantly, there are no obvious horrible things (though I haven't gone in depth with branches yet).   If all this really works and there are no typos, I think this will be a VERY nice addition.
>  * `unqiue` typo
>  * `Verfify` typo
>  * `increasin` typo
>  * I don't know why, but the math following "It follows from Bessel's..." doesn't look right in the doc (the `:math:` directive is not parsed)

Fixed, it was a one space indentation problem.

>  * Is \operatorname{bessel\_I}(\alpha, x) standard or should we just just the I sub whatever?

I was unsure about this. I think now it makes most sense to just stick with I_\alpha when in a math block.

>  * ``test_relation()`` needs to be in double back ticks or have a link to the appropriate place in the ref manual
>  * Trac tickets should use `:trac:` syntax
>  * Does `f(x) = Bessel(0): plot(f, (x, 1, 10))` work, or must one use `Bessel(0)(x)`?  The example after that makes it look like maybe not...

The way the code works you have to specify the variable on the right hand side, e.g.:


```
sage: f(x) = Bessel(0)(x)
sage: f(x) = bessel_I(0, x)
```


This is because `Bessel()` returns lambda functions under the hood. Personally, I prefer having the variable dependence made explicit, but I'm open to suggestions if there are other
ways you can think of to get that functionality.

>  * Bessel Y and Bessel K need a little filling out - and one of the `:math:` directives doesn't show up at all, the other isn't parsed right for some reason again

I'll work on Bessel Y and K, I realize now that you mention it that I didn't fill in the definitions there :). Anyone with good doctest suggestions for these is welcome to chime in, I'll add the tests if you can think of interesting or relevant ones.

>  * I'd personally get rid of the whitespace changes in sage/functions/special.py - unlikely to have an effect, but not really necessary.

Yep, you're right.

>  * How should we deal with the removal of the `"maxima"` and `"pari"` arguments?  I'm not sure if it's really feasible to have a deprecation period for that, but we should discuss it.

This is a question that's been troubling me. I don't know how to make the deprecation happen and make progress here without renaming the new functions and then swapping them in when the deprecation period is over. The infrastructure we have for adding symbolic functions (inheriting from `BuiltinFunction`, etc) doesn't support any kind of system arguments without overriding `call()`.

At least existing code that uses the Bessel functions as they are now in Sage won't break unless they explicitly use the system argument.

Maybe `@`burcin has a suggestion here?

>  * I suppose we don't need to keep *all* old tests, but some of them are rather different and might be worth putting in a TESTS section somewhere, just so that we don't have some unexpected regression only they catch.

Good point, I'll see what I can salvage.

>  * The switch to alpha from nu - I would rather not deprecate this either, but in principle someone could have used it as a keyword argument in the past...

It doesn't make a difference to me, I used alpha because that's what's on the wikipedia page :) Abramowitz & Stegun uses n or \nu and so does the mpmath documentation. I can easily switch \alpha to \nu with some editor-fu.



---

archive/issue_comments_029567.json:
```json
{
    "body": "Attachment [trac_symbolic_bessel_doctests.patch](tarball://root/attachments/some-uuid/ticket4102/trac_symbolic_bessel_doctests.patch) by @benjaminfjones created at 2013-03-12 20:47:19\n\nfix doctests and tutorial references involving Bessel function API",
    "created_at": "2013-03-12T20:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29567",
    "user": "https://github.com/benjaminfjones"
}
```

Attachment [trac_symbolic_bessel_doctests.patch](tarball://root/attachments/some-uuid/ticket4102/trac_symbolic_bessel_doctests.patch) by @benjaminfjones created at 2013-03-12 20:47:19

fix doctests and tutorial references involving Bessel function API



---

archive/issue_comments_029568.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-03-12T20:51:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29568",
    "user": "https://github.com/benjaminfjones"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_029569.json:
```json
{
    "body": "I've uploaded two new patches addressing comments by `@`kcrisman. The two latest patches are finally ready for complete review.\n\nPatchbot:\n\nApply trac_symbolic_bessel_v5.patch trac_symbolic_bessel_doctests.patch",
    "created_at": "2013-03-12T20:51:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29569",
    "user": "https://github.com/benjaminfjones"
}
```

I've uploaded two new patches addressing comments by `@`kcrisman. The two latest patches are finally ready for complete review.

Patchbot:

Apply trac_symbolic_bessel_v5.patch trac_symbolic_bessel_doctests.patch



---

archive/issue_comments_029570.json:
```json
{
    "body": "Some additional notes regarding your comments, `@`kcrisman:\n\n- The doctest of `desolve` that was failing was returning unconverted Maxima output, that's what the `bessel_j`, etc are. With the v5 patch we now have an honest Sage symbolic function as the return value in that case (also, see the diff eq doctest examples I wrote).\n\n- I changes from using \\alpha as the order to \\nu for consistency with mpmath and Maxima.\n\n- I changed the random expression seed to 53 (my favorite random integer) and that test no longer raises an exception.",
    "created_at": "2013-03-12T20:58:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29570",
    "user": "https://github.com/benjaminfjones"
}
```

Some additional notes regarding your comments, `@`kcrisman:

- The doctest of `desolve` that was failing was returning unconverted Maxima output, that's what the `bessel_j`, etc are. With the v5 patch we now have an honest Sage symbolic function as the return value in that case (also, see the diff eq doctest examples I wrote).

- I changes from using \alpha as the order to \nu for consistency with mpmath and Maxima.

- I changed the random expression seed to 53 (my favorite random integer) and that test no longer raises an exception.



---

archive/issue_comments_029571.json:
```json
{
    "body": "Nice work.  I do feel like we should ask on sage-devel about deprecating the evaluation system keywords versus (as in the current version) simply removing them but leaving room for their return...\n\n```\nassert _system == 'mpmath' \n```\n\nI suppose we could at least doctest this as a todo with the error message it receives with the \"wrong\" input.\n\nI still want to give it a final go-over, but various testing of your tests and code makes me think this is ready.  What a job!",
    "created_at": "2013-03-13T16:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29571",
    "user": "https://github.com/kcrisman"
}
```

Nice work.  I do feel like we should ask on sage-devel about deprecating the evaluation system keywords versus (as in the current version) simply removing them but leaving room for their return...

```
assert _system == 'mpmath' 
```

I suppose we could at least doctest this as a todo with the error message it receives with the "wrong" input.

I still want to give it a final go-over, but various testing of your tests and code makes me think this is ready.  What a job!



---

archive/issue_comments_029572.json:
```json
{
    "body": "I spent some time today thinking about the deprecation issue. Here's my summary:\n\nThe current patches introduce two API changes. First, the new `bessel_I, bessel_J, etc` functions take two positional arguments whereas the old ones take 2 positional arguments and two optional keyword arguments (`algorithm` and `prec`). The second API change is the same change in arguments, but to the constructor `Bessel`.\n\nI can add deprecation warnings to the `Bessel` constructor easily and have it call the old `bessel_?` functions during the deprecation period. On the other hand, I don't know how to implement deprecation for the old `bessel_?` functions. I can imagine trying to override `BuiltinFunction`'s call method, or turning the new `bessel_?` functions into wrappers which call the new ones if two arguments are used, and give a deprecation warning and call the old versions if more than 2 arguments are given.\n\n----\n\nI can:\n\n1. try to implement the deprecation\n2. ask on sage-devel for a waiver from the deprecation policy in this case\n3. other?\n\nWhat say you all?",
    "created_at": "2013-03-26T00:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29572",
    "user": "https://github.com/benjaminfjones"
}
```

I spent some time today thinking about the deprecation issue. Here's my summary:

The current patches introduce two API changes. First, the new `bessel_I, bessel_J, etc` functions take two positional arguments whereas the old ones take 2 positional arguments and two optional keyword arguments (`algorithm` and `prec`). The second API change is the same change in arguments, but to the constructor `Bessel`.

I can add deprecation warnings to the `Bessel` constructor easily and have it call the old `bessel_?` functions during the deprecation period. On the other hand, I don't know how to implement deprecation for the old `bessel_?` functions. I can imagine trying to override `BuiltinFunction`'s call method, or turning the new `bessel_?` functions into wrappers which call the new ones if two arguments are used, and give a deprecation warning and call the old versions if more than 2 arguments are given.

----

I can:

1. try to implement the deprecation
2. ask on sage-devel for a waiver from the deprecation policy in this case
3. other?

What say you all?



---

archive/issue_comments_029573.json:
```json
{
    "body": "After chatting with `@`burcin, I decided to do 1. The new patch implements deprecation by retaining all the old code with names prefixed by an underscore. I preserved all the old doctests (which reference the underscored names). In the new code, I overrode `__call__` if more than 2 arguments are given.\n\nReady for review!",
    "created_at": "2013-03-26T21:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29573",
    "user": "https://github.com/benjaminfjones"
}
```

After chatting with `@`burcin, I decided to do 1. The new patch implements deprecation by retaining all the old code with names prefixed by an underscore. I preserved all the old doctests (which reference the underscored names). In the new code, I overrode `__call__` if more than 2 arguments are given.

Ready for review!



---

archive/issue_comments_029574.json:
```json
{
    "body": "Patchbot, apply trac_symbolic_bessel_v5.patch trac_symbolic_bessel_doctests.patch trac_symbolic_bessel_deprecation.patch",
    "created_at": "2013-03-26T21:18:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29574",
    "user": "https://github.com/benjaminfjones"
}
```

Patchbot, apply trac_symbolic_bessel_v5.patch trac_symbolic_bessel_doctests.patch trac_symbolic_bessel_deprecation.patch



---

archive/issue_comments_029575.json:
```json
{
    "body": "Can you remind me what the plan was for algorithm as a keyword?  Wasn't there some plan to *re*introduce it once we got the hooks in properly, so that people could easily compare e.g. Pari, mpmath, Mma (if available), etc.?  Doesn't mean this patch couldn't go in, just trying to get things straight.\n\nQuick glance at the latest patch looks good.  What a lot of underscores; did you write a script?",
    "created_at": "2013-03-27T01:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29575",
    "user": "https://github.com/kcrisman"
}
```

Can you remind me what the plan was for algorithm as a keyword?  Wasn't there some plan to *re*introduce it once we got the hooks in properly, so that people could easily compare e.g. Pari, mpmath, Mma (if available), etc.?  Doesn't mean this patch couldn't go in, just trying to get things straight.

Quick glance at the latest patch looks good.  What a lot of underscores; did you write a script?



---

archive/issue_comments_029576.json:
```json
{
    "body": "The algorithm keyword in _eval_ requires a work in progress branch of pynac that has probably bit rot by now. I have it on my agenda (since last year!) to look back into it..",
    "created_at": "2013-03-27T01:32:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29576",
    "user": "https://github.com/benjaminfjones"
}
```

The algorithm keyword in _eval_ requires a work in progress branch of pynac that has probably bit rot by now. I have it on my agenda (since last year!) to look back into it..



---

archive/issue_comments_029577.json:
```json
{
    "body": "Right, I understand - my point is that maybe the deprecation message should be slightly different, something like\n\n```\ndeprecation(4102, 'precision argument is deprecated\\nalgorithm argument will only be available as a named keyword in the future and is currently in mothballs')\n```\n\nor something somewhat more professional/accurate than that.",
    "created_at": "2013-03-27T01:39:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29577",
    "user": "https://github.com/kcrisman"
}
```

Right, I understand - my point is that maybe the deprecation message should be slightly different, something like

```
deprecation(4102, 'precision argument is deprecated\nalgorithm argument will only be available as a named keyword in the future and is currently in mothballs')
```

or something somewhat more professional/accurate than that.



---

archive/issue_comments_029578.json:
```json
{
    "body": "I see, sure, how about just:\n\n\"precision argument is deprecated, algorithm argument is currently deprecated, but will be available as a named keyword in the future\"",
    "created_at": "2013-03-27T17:13:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29578",
    "user": "https://github.com/benjaminfjones"
}
```

I see, sure, how about just:

"precision argument is deprecated, algorithm argument is currently deprecated, but will be available as a named keyword in the future"



---

archive/issue_comments_029579.json:
```json
{
    "body": "> I see, sure, how about just:\n> \"precision argument is deprecated, algorithm argument is currently deprecated, but will be available as a named keyword in the future\"\nThat sounds good, except that I would put a semicolon instead of a comma in the first comma spot.",
    "created_at": "2013-03-27T17:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29579",
    "user": "https://github.com/kcrisman"
}
```

> I see, sure, how about just:
> "precision argument is deprecated, algorithm argument is currently deprecated, but will be available as a named keyword in the future"
That sounds good, except that I would put a semicolon instead of a comma in the first comma spot.



---

archive/issue_comments_029580.json:
```json
{
    "body": "add deprecation of old API",
    "created_at": "2013-03-27T19:26:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29580",
    "user": "https://github.com/benjaminfjones"
}
```

add deprecation of old API



---

archive/issue_comments_029581.json:
```json
{
    "body": "Attachment [trac_symbolic_bessel_v5.patch](tarball://root/attachments/some-uuid/ticket4102/trac_symbolic_bessel_v5.patch) by @benjaminfjones created at 2013-03-28 00:08:11\n\nlatest symbolic Bessel functions patch, ready for review",
    "created_at": "2013-03-28T00:08:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29581",
    "user": "https://github.com/benjaminfjones"
}
```

Attachment [trac_symbolic_bessel_v5.patch](tarball://root/attachments/some-uuid/ticket4102/trac_symbolic_bessel_v5.patch) by @benjaminfjones created at 2013-03-28 00:08:11

latest symbolic Bessel functions patch, ready for review



---

archive/issue_comments_029582.json:
```json
{
    "body": "Latest attachment makes a tiny doc change to fix a latex mistake.",
    "created_at": "2013-03-28T00:09:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29582",
    "user": "https://github.com/benjaminfjones"
}
```

Latest attachment makes a tiny doc change to fix a latex mistake.



---

archive/issue_comments_029583.json:
```json
{
    "body": "Patchbot apply trac_symbolic_bessel_v5.patch trac_symbolic_bessel_doctests.patch trac_symbolic_bessel_deprecation.patch",
    "created_at": "2013-03-29T22:47:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29583",
    "user": "https://github.com/benjaminfjones"
}
```

Patchbot apply trac_symbolic_bessel_v5.patch trac_symbolic_bessel_doctests.patch trac_symbolic_bessel_deprecation.patch



---

archive/issue_comments_029584.json:
```json
{
    "body": "Patchbot shows test failures on sage-5.9.beta2",
    "created_at": "2013-04-01T20:55:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29584",
    "user": "https://github.com/vbraun"
}
```

Patchbot shows test failures on sage-5.9.beta2



---

archive/issue_comments_029585.json:
```json
{
    "body": "> Patchbot shows test failures on sage-5.9.beta2\nIn particular, they are relevant:\n\n```\nsage -t sage/functions/bessel.py\n**********************************************************************\nFile \"sage/functions/bessel.py\", line 977, in sage.functions.bessel.Bessel\nFailed example:\n    f = desolve(diffeq, y, [1, 1, 1]); f\nExpected:\n    (bessel_J(0, 1) + bessel_J(1, 1))*bessel_Y(0, x)/(bessel_Y(0, 1)*bessel_J(1, 1) - bessel_Y(1, 1)*bessel_J(0, 1)) - (bessel_Y(0, 1) + bessel_Y(1, 1))*bessel_J(0, x)/(bessel_Y(0, 1)*bessel_J(1, 1) - bessel_Y(1, 1)*bessel_J(0, 1))\nGot:\n    (bessel_Y(0, 1) + bessel_Y(1, 1))*bessel_j(0, x)/(bessel_j(0, 1)*bessel_Y(1, 1) - bessel_j(1, 1)*bessel_Y(0, 1)) - (bessel_j(0, 1) + bessel_j(1, 1))*bessel_Y(0, x)/(bessel_j(0, 1)*bessel_Y(1, 1) - bessel_j(1, 1)*bessel_Y(0, 1))\n**********************************************************************\nFile \"sage/functions/bessel.py\", line 983, in sage.functions.bessel.Bessel\nFailed example:\n    fp.subs(x=1).n()\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/storage2TB/patchbot/Sage/sage-5.9.beta2/local/lib/python2.7/site-packages/sage/doctest/forker.py\", line 460, in _run\n        self.execute(example, compiled, test.globs)\n      File \"/mnt/storage2TB/patchbot/Sage/sage-5.9.beta2/local/lib/python2.7/site-packages/sage/doctest/forker.py\", line 819, in execute\n        exec compiled in globs\n      File \"<doctest sage.functions.bessel.Bessel[29]>\", line 1, in <module>\n        fp.subs(x=Integer(1)).n()\n      File \"expression.pyx\", line 4381, in sage.symbolic.expression.Expression._numerical_approx (sage/symbolic/expression.cpp:21011)\n    TypeError: cannot evaluate symbolic expression numerically\n**********************************************************************\n1 item had failures:\n   2 of  46 in sage.functions.bessel.Bessel\n    [258 tests, 2 failures, 16.6 s]\n----------------------------------------------------------------------\nsage -t sage/functions/bessel.py  # 2 doctests failed\n----------------------------------------------------------------------\n```\n\nI don't like that some are lowercase and some uppercase.  I think that the second error is just a result of that - the derivative won't function properly.",
    "created_at": "2013-04-02T00:36:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29585",
    "user": "https://github.com/kcrisman"
}
```

> Patchbot shows test failures on sage-5.9.beta2
In particular, they are relevant:

```
sage -t sage/functions/bessel.py
**********************************************************************
File "sage/functions/bessel.py", line 977, in sage.functions.bessel.Bessel
Failed example:
    f = desolve(diffeq, y, [1, 1, 1]); f
Expected:
    (bessel_J(0, 1) + bessel_J(1, 1))*bessel_Y(0, x)/(bessel_Y(0, 1)*bessel_J(1, 1) - bessel_Y(1, 1)*bessel_J(0, 1)) - (bessel_Y(0, 1) + bessel_Y(1, 1))*bessel_J(0, x)/(bessel_Y(0, 1)*bessel_J(1, 1) - bessel_Y(1, 1)*bessel_J(0, 1))
Got:
    (bessel_Y(0, 1) + bessel_Y(1, 1))*bessel_j(0, x)/(bessel_j(0, 1)*bessel_Y(1, 1) - bessel_j(1, 1)*bessel_Y(0, 1)) - (bessel_j(0, 1) + bessel_j(1, 1))*bessel_Y(0, x)/(bessel_j(0, 1)*bessel_Y(1, 1) - bessel_j(1, 1)*bessel_Y(0, 1))
**********************************************************************
File "sage/functions/bessel.py", line 983, in sage.functions.bessel.Bessel
Failed example:
    fp.subs(x=1).n()
Exception raised:
    Traceback (most recent call last):
      File "/mnt/storage2TB/patchbot/Sage/sage-5.9.beta2/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 460, in _run
        self.execute(example, compiled, test.globs)
      File "/mnt/storage2TB/patchbot/Sage/sage-5.9.beta2/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 819, in execute
        exec compiled in globs
      File "<doctest sage.functions.bessel.Bessel[29]>", line 1, in <module>
        fp.subs(x=Integer(1)).n()
      File "expression.pyx", line 4381, in sage.symbolic.expression.Expression._numerical_approx (sage/symbolic/expression.cpp:21011)
    TypeError: cannot evaluate symbolic expression numerically
**********************************************************************
1 item had failures:
   2 of  46 in sage.functions.bessel.Bessel
    [258 tests, 2 failures, 16.6 s]
----------------------------------------------------------------------
sage -t sage/functions/bessel.py  # 2 doctests failed
----------------------------------------------------------------------
```

I don't like that some are lowercase and some uppercase.  I think that the second error is just a result of that - the derivative won't function properly.



---

archive/issue_comments_029586.json:
```json
{
    "body": "There is something strange going on. Here is sage-5.9.beta2 with the three patches applied:\n\n\n```\n[bjones@cabbage:devel/sage]% ../../sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage:  y = function('y', x)\nsage: diffeq = x^2*diff(y,x,x) + x*diff(y,x) + x^2*y == 0\nsage: f = desolve(diffeq, y, [1, 1, 1]); f\n(bessel_Y(0, 1) + bessel_Y(1, 1))*bessel_J(0, x)/(bessel_J(0, 1)*bessel_Y(1, 1) - bessel_J(1, 1)*bessel_Y(0, 1)) - (bessel_J(0, 1) + bessel_J(1, 1))*bessel_Y(0, x)/(bessel_J(0, 1)*bessel_Y(1, 1) - bessel_J(1, 1)*bessel_Y(0, 1))\n```\n\n| Sage Version 5.9.beta2, Release Date: 2013-03-28                   |\n| Type \"notebook()\" for the browser-based notebook interface.        |\n| Type \"help()\" for help.                                            |\nwhich is exactly what the doctest expects.\n\nNow doctesting `sage/functions/bessel.py` with sage in the exact same state:\n\n\n```\n[bjones@cabbage:devel/sage]% ../../sage -t sage/functions/bessel.py                \nRunning doctests with ID 2013-04-01-21-31-17-4bc246be.\nDoctesting 1 file.\nsage -t sage/functions/bessel.py\n**********************************************************************\nFile \"sage/functions/bessel.py\", line 977, in sage.functions.bessel.Bessel\nFailed example:\n    f = desolve(diffeq, y, [1, 1, 1]); f\nExpected:\n    (bessel_J(0, 1) + bessel_J(1, 1))*bessel_Y(0, x)/(bessel_Y(0, 1)*bessel_J(1, 1) - bessel_Y(1, 1)*bessel_J(0, 1)) - (bessel_Y(0, 1) + bessel_Y(1, 1))*bessel_J(0, x)/(bessel_Y(0, 1)*bessel_J(1, 1) - bessel_Y(1, 1)*bessel_J(0, 1))\nGot:\n    (bessel_Y(0, 1) + bessel_Y(1, 1))*bessel_j(0, x)/(bessel_j(0, 1)*bessel_Y(1, 1) - bessel_j(1, 1)*bessel_Y(0, 1)) - (bessel_j(0, 1) + bessel_j(1, 1))*bessel_Y(0, x)/(bessel_j(0, 1)*bessel_Y(1, 1) - bessel_j(1, 1)*bessel_Y(0, 1))\n```\n\n\nThe lower cased `bessel_j` is what Maxima returns if you don't register a conversion to `bessel_J`, the Sage symbolic version of J that these patches introduce.\n\nWhat is also strange is that the above output does actually represent a different form of the correct solution (modulo replacing bessel_j by bessel_J).\n\nSo what is going on here?\n\nFWIW, sage-5.8 with same three patches applied does not exhibit this behavior.",
    "created_at": "2013-04-02T04:46:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29586",
    "user": "https://github.com/benjaminfjones"
}
```

There is something strange going on. Here is sage-5.9.beta2 with the three patches applied:


```
[bjones@cabbage:devel/sage]% ../../sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage:  y = function('y', x)
sage: diffeq = x^2*diff(y,x,x) + x*diff(y,x) + x^2*y == 0
sage: f = desolve(diffeq, y, [1, 1, 1]); f
(bessel_Y(0, 1) + bessel_Y(1, 1))*bessel_J(0, x)/(bessel_J(0, 1)*bessel_Y(1, 1) - bessel_J(1, 1)*bessel_Y(0, 1)) - (bessel_J(0, 1) + bessel_J(1, 1))*bessel_Y(0, x)/(bessel_J(0, 1)*bessel_Y(1, 1) - bessel_J(1, 1)*bessel_Y(0, 1))
```

| Sage Version 5.9.beta2, Release Date: 2013-03-28                   |
| Type "notebook()" for the browser-based notebook interface.        |
| Type "help()" for help.                                            |
which is exactly what the doctest expects.

Now doctesting `sage/functions/bessel.py` with sage in the exact same state:


```
[bjones@cabbage:devel/sage]% ../../sage -t sage/functions/bessel.py                
Running doctests with ID 2013-04-01-21-31-17-4bc246be.
Doctesting 1 file.
sage -t sage/functions/bessel.py
**********************************************************************
File "sage/functions/bessel.py", line 977, in sage.functions.bessel.Bessel
Failed example:
    f = desolve(diffeq, y, [1, 1, 1]); f
Expected:
    (bessel_J(0, 1) + bessel_J(1, 1))*bessel_Y(0, x)/(bessel_Y(0, 1)*bessel_J(1, 1) - bessel_Y(1, 1)*bessel_J(0, 1)) - (bessel_Y(0, 1) + bessel_Y(1, 1))*bessel_J(0, x)/(bessel_Y(0, 1)*bessel_J(1, 1) - bessel_Y(1, 1)*bessel_J(0, 1))
Got:
    (bessel_Y(0, 1) + bessel_Y(1, 1))*bessel_j(0, x)/(bessel_j(0, 1)*bessel_Y(1, 1) - bessel_j(1, 1)*bessel_Y(0, 1)) - (bessel_j(0, 1) + bessel_j(1, 1))*bessel_Y(0, x)/(bessel_j(0, 1)*bessel_Y(1, 1) - bessel_j(1, 1)*bessel_Y(0, 1))
```


The lower cased `bessel_j` is what Maxima returns if you don't register a conversion to `bessel_J`, the Sage symbolic version of J that these patches introduce.

What is also strange is that the above output does actually represent a different form of the correct solution (modulo replacing bessel_j by bessel_J).

So what is going on here?

FWIW, sage-5.8 with same three patches applied does not exhibit this behavior.



---

archive/issue_comments_029587.json:
```json
{
    "body": "Maxima is the same version in sage-5.8 and 5.9.beta2, so thats not it.\n\nThe new doctesting framework was introduced in sage-5.9.beta, thats a likely suspect. It uses fork, so external interfaces need to be shut down / restarted. Perhaps the restarted maxima process is not set up correctly? Though just using ``@`fork` seems to work.",
    "created_at": "2013-04-02T08:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29587",
    "user": "https://github.com/vbraun"
}
```

Maxima is the same version in sage-5.8 and 5.9.beta2, so thats not it.

The new doctesting framework was introduced in sage-5.9.beta, thats a likely suspect. It uses fork, so external interfaces need to be shut down / restarted. Perhaps the restarted maxima process is not set up correctly? Though just using ``@`fork` seems to work.



---

archive/issue_comments_029588.json:
```json
{
    "body": "benjaminfjones: I don't understand the problem. It seems to me that the doctest should simply be changed to match the \"correct\" output.",
    "created_at": "2013-04-05T15:43:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29588",
    "user": "https://github.com/jdemeyer"
}
```

benjaminfjones: I don't understand the problem. It seems to me that the doctest should simply be changed to match the "correct" output.



---

archive/issue_comments_029589.json:
```json
{
    "body": "So the correct output is:\n\n\n```\n(bessel_J(0, 1) + bessel_J(1, 1))*bessel_Y(0, x)/(bessel_Y(0, 1)*bessel_J(1, 1) - bessel_Y(1, 1)*bessel_J(0, 1)) - (bessel_Y(0, 1) + bessel_Y(1, 1))*bessel_J(0, x)/(bessel_Y(0, 1)*bessel_J(1, 1) - bessel_Y(1, 1)*bessel_J(0, 1))\n```\n\n\nthat is both mathematically correct and what you get when you apply the patches, run sage, and execute the commands manually.\n\nThe problem is that when you **doctest** the same exact commands in the same exact sage, the output that comes back is different in two ways (explained in the comment above).",
    "created_at": "2013-04-05T16:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29589",
    "user": "https://github.com/benjaminfjones"
}
```

So the correct output is:


```
(bessel_J(0, 1) + bessel_J(1, 1))*bessel_Y(0, x)/(bessel_Y(0, 1)*bessel_J(1, 1) - bessel_Y(1, 1)*bessel_J(0, 1)) - (bessel_Y(0, 1) + bessel_Y(1, 1))*bessel_J(0, x)/(bessel_Y(0, 1)*bessel_J(1, 1) - bessel_Y(1, 1)*bessel_J(0, 1))
```


that is both mathematically correct and what you get when you apply the patches, run sage, and execute the commands manually.

The problem is that when you **doctest** the same exact commands in the same exact sage, the output that comes back is different in two ways (explained in the comment above).



---

archive/issue_comments_029590.json:
```json
{
    "body": "More clues: (?)\n\nHere are the three commands in question\n\n\n```\nsage: y = function('y', x)\nsage: diffeq = x^2*diff(y,x,x) + x*diff(y,x) + x^2*y == 0\nsage: f = desolve(diffeq, y, [1, 1, 1]); f\n```\n\n\n1. running the commands in an interactive sage session directly after startup, output is:\n\n\n```\n(bessel_Y(0, 1) + bessel_Y(1, 1))*bessel_J(0, x)/(bessel_J(0, 1)*bessel_Y(1, 1) - bessel_J(1, 1)*bessel_Y(0, 1)) - (bessel_J(0, 1) + bessel_J(1, 1))*bessel_Y(0, x)/(bessel_J(0, 1)*bessel_Y(1, 1) - bessel_J(1, 1)*bessel_Y(0, 1))\n```\n\n\n2. running the same commands as included in a doctest in `sage/functions/bessel.py`, output is:\n\n\n```\n(bessel_Y(0, 1) + bessel_Y(1, 1))*bessel_j(0, x)/(bessel_j(0, 1)*bessel_Y(1, 1) - bessel_j(1, 1)*bessel_Y(0, 1)) - (bessel_j(0, 1) + bessel_j(1, 1))*bessel_Y(0, x)/(bessel_j(0, 1)*bessel_Y(1, 1) - bessel_j(1, 1)*bessel_Y(0, 1))\n```\n\n\n3. putting the three commands in a docstring alone in a new file `foo.py` and doctesting that, output is:\n\n\n```\n(bessel_Y(0, 1) + bessel_Y(1, 1))*bessel_J(0, x)/(bessel_J(0, 1)*bessel_Y(1, 1) - bessel_J(1, 1)*bessel_Y(0, 1)) - (bessel_J(0, 1) + bessel_J(1, 1))*bessel_Y(0, x)/(bessel_J(0, 1)*bessel_Y(1, 1) - bessel_J(1, 1)*bessel_Y(0, 1))\n```\n\nnote: same output as in (1)\n\nSo it looks like there is some hidden state affecting the doctesting in scenario (2).",
    "created_at": "2013-04-05T16:58:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29590",
    "user": "https://github.com/benjaminfjones"
}
```

More clues: (?)

Here are the three commands in question


```
sage: y = function('y', x)
sage: diffeq = x^2*diff(y,x,x) + x*diff(y,x) + x^2*y == 0
sage: f = desolve(diffeq, y, [1, 1, 1]); f
```


1. running the commands in an interactive sage session directly after startup, output is:


```
(bessel_Y(0, 1) + bessel_Y(1, 1))*bessel_J(0, x)/(bessel_J(0, 1)*bessel_Y(1, 1) - bessel_J(1, 1)*bessel_Y(0, 1)) - (bessel_J(0, 1) + bessel_J(1, 1))*bessel_Y(0, x)/(bessel_J(0, 1)*bessel_Y(1, 1) - bessel_J(1, 1)*bessel_Y(0, 1))
```


2. running the same commands as included in a doctest in `sage/functions/bessel.py`, output is:


```
(bessel_Y(0, 1) + bessel_Y(1, 1))*bessel_j(0, x)/(bessel_j(0, 1)*bessel_Y(1, 1) - bessel_j(1, 1)*bessel_Y(0, 1)) - (bessel_j(0, 1) + bessel_j(1, 1))*bessel_Y(0, x)/(bessel_j(0, 1)*bessel_Y(1, 1) - bessel_j(1, 1)*bessel_Y(0, 1))
```


3. putting the three commands in a docstring alone in a new file `foo.py` and doctesting that, output is:


```
(bessel_Y(0, 1) + bessel_Y(1, 1))*bessel_J(0, x)/(bessel_J(0, 1)*bessel_Y(1, 1) - bessel_J(1, 1)*bessel_Y(0, 1)) - (bessel_J(0, 1) + bessel_J(1, 1))*bessel_Y(0, x)/(bessel_J(0, 1)*bessel_Y(1, 1) - bessel_J(1, 1)*bessel_Y(0, 1))
```

note: same output as in (1)

So it looks like there is some hidden state affecting the doctesting in scenario (2).



---

archive/issue_comments_029591.json:
```json
{
    "body": "Replying to [comment:45 benjaminfjones]:\n> So it looks like there is some hidden state affecting the doctesting in scenario (2). \nThe doctests which are run *before* that test are extra \"state\".",
    "created_at": "2013-04-09T12:28:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29591",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:45 benjaminfjones]:
> So it looks like there is some hidden state affecting the doctesting in scenario (2). 
The doctests which are run *before* that test are extra "state".



---

archive/issue_comments_029592.json:
```json
{
    "body": "See also #2516.",
    "created_at": "2013-04-25T02:21:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29592",
    "user": "https://github.com/kcrisman"
}
```

See also #2516.



---

archive/issue_comments_029593.json:
```json
{
    "body": "Copy of trac_symbolic_bessel_v5, minus one doctest block",
    "created_at": "2013-05-20T23:22:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29593",
    "user": "https://github.com/benjaminfjones"
}
```

Copy of trac_symbolic_bessel_v5, minus one doctest block



---

archive/issue_comments_029594.json:
```json
{
    "body": "Attachment [trac_symbolic_bessel_v6.patch](tarball://root/attachments/some-uuid/ticket4102/trac_symbolic_bessel_v6.patch) by @benjaminfjones created at 2013-05-20 23:23:06\n\nCopy of trac_symbolic_bessel_v5, minus one doctest block",
    "created_at": "2013-05-20T23:23:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29594",
    "user": "https://github.com/benjaminfjones"
}
```

Attachment [trac_symbolic_bessel_v6.patch](tarball://root/attachments/some-uuid/ticket4102/trac_symbolic_bessel_v6.patch) by @benjaminfjones created at 2013-05-20 23:23:06

Copy of trac_symbolic_bessel_v5, minus one doctest block



---

archive/issue_comments_029595.json:
```json
{
    "body": "I still have not been able to track down the doctesting issue (described starting at comment:41). I've tried bisecting the doctest state (delta debugging) to no avail. The problem seems to be intimately linked to the doctesting environment. I'm unable to reproduce the doctest failure when running __all__ the prior doctests which come before in `bessel.py`, in the right order, by hand, and then running the offending one.\n\nThe only thing I can tell for sure is that at some point as the doctests are run, one of the pynac symbol tables get's modified. This causes the `bessel_j` vs `bessel_J` problem.\n\nMy inclination is to remove the offending doctest and file a new ticket to resolve the problem. Meanwhile, the bessel function code can be reviewed and become useful. I've posted a patch `trac_symbolic_bessel_v6` which removes the offending doctest block.\n\nComments?\n\n----\n\nPatchbot, apply trac_symbolic_bessel_v6.patch trac_symbolic_bessel_doctests.patch trac_symbolic_bessel_deprecation.patch",
    "created_at": "2013-05-20T23:33:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29595",
    "user": "https://github.com/benjaminfjones"
}
```

I still have not been able to track down the doctesting issue (described starting at comment:41). I've tried bisecting the doctest state (delta debugging) to no avail. The problem seems to be intimately linked to the doctesting environment. I'm unable to reproduce the doctest failure when running __all__ the prior doctests which come before in `bessel.py`, in the right order, by hand, and then running the offending one.

The only thing I can tell for sure is that at some point as the doctests are run, one of the pynac symbol tables get's modified. This causes the `bessel_j` vs `bessel_J` problem.

My inclination is to remove the offending doctest and file a new ticket to resolve the problem. Meanwhile, the bessel function code can be reviewed and become useful. I've posted a patch `trac_symbolic_bessel_v6` which removes the offending doctest block.

Comments?

----

Patchbot, apply trac_symbolic_bessel_v6.patch trac_symbolic_bessel_doctests.patch trac_symbolic_bessel_deprecation.patch



---

archive/issue_comments_029596.json:
```json
{
    "body": "Tests are passing on 5.10.beta4. The startup time plugin is failing, however. Should we lazy import here? Also how about lazy import for all the special functions (the idea being that relatively few users will need any given special function)?",
    "created_at": "2013-05-27T16:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29596",
    "user": "https://github.com/benjaminfjones"
}
```

Tests are passing on 5.10.beta4. The startup time plugin is failing, however. Should we lazy import here? Also how about lazy import for all the special functions (the idea being that relatively few users will need any given special function)?



---

archive/issue_comments_029597.json:
```json
{
    "body": "Replying to [comment:49 benjaminfjones]:\n> Tests are passing on 5.10.beta4. The startup time plugin is failing, however. Should we lazy import here? Also how about lazy import for all the special functions (the idea being that relatively few users will need any given special function)?\n\n+100 to lazy import for all special functions, but in a separate ticket.\n\nIt would be great if you can use lazy import for the functions defined here to silence the startup time plugin.\n\n\nAbout the doctesting framework issue: I briefly tried to debug this and didn't get anywhere either. I agree that we should move this to a new ticket and not hold this one up longer. Instead of removing the test, can you mark it `# not tested` and mention the ticket number?\n\nThanks a lot for your work on this.",
    "created_at": "2013-05-27T17:09:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29597",
    "user": "https://github.com/burcin"
}
```

Replying to [comment:49 benjaminfjones]:
> Tests are passing on 5.10.beta4. The startup time plugin is failing, however. Should we lazy import here? Also how about lazy import for all the special functions (the idea being that relatively few users will need any given special function)?

+100 to lazy import for all special functions, but in a separate ticket.

It would be great if you can use lazy import for the functions defined here to silence the startup time plugin.


About the doctesting framework issue: I briefly tried to debug this and didn't get anywhere either. I agree that we should move this to a new ticket and not hold this one up longer. Instead of removing the test, can you mark it `# not tested` and mention the ticket number?

Thanks a lot for your work on this.



---

archive/issue_comments_029598.json:
```json
{
    "body": "I'm trying to understand how the interfacing works. Is this the intended output?\n\n```\nsage: maxima(bessel_I).sage()\nbessel_i\n```\n",
    "created_at": "2013-05-27T18:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29598",
    "user": "https://github.com/vbraun"
}
```

I'm trying to understand how the interfacing works. Is this the intended output?

```
sage: maxima(bessel_I).sage()
bessel_i
```




---

archive/issue_comments_029599.json:
```json
{
    "body": "`maxima_function()`, used in `sage.functions.bessel._bessel_J`, overwrites the symbol table entry:\n\n```\nsage: from sage.functions.special import maxima_function\nsage: type(sage.symbolic.pynac.symbol_table['maxima']['bessel_j'])\n<class 'sage.functions.bessel.Function_Bessel_J'>\nsage: maxima_function('bessel_j')\nbessel_j\nsage: type(sage.symbolic.pynac.symbol_table['maxima']['bessel_j'])\n<class 'sage.functions.special.NewMaximaFunction'>\n```\n",
    "created_at": "2013-05-27T19:07:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29599",
    "user": "https://github.com/vbraun"
}
```

`maxima_function()`, used in `sage.functions.bessel._bessel_J`, overwrites the symbol table entry:

```
sage: from sage.functions.special import maxima_function
sage: type(sage.symbolic.pynac.symbol_table['maxima']['bessel_j'])
<class 'sage.functions.bessel.Function_Bessel_J'>
sage: maxima_function('bessel_j')
bessel_j
sage: type(sage.symbolic.pynac.symbol_table['maxima']['bessel_j'])
<class 'sage.functions.special.NewMaximaFunction'>
```




---

archive/issue_comments_029600.json:
```json
{
    "body": "`@`burcin: Okay! Good idea. I'll lazy import the Bessel stuff and create a new ticket for the rest.\n\n`@`vbraun: Thanks! That's good detective work. How did you figure that out (I wasted a lot of time trying to find the culprit)?\n\n----\n\nI'll look into addressing the symbol table issue and report back with updated patches.",
    "created_at": "2013-05-28T16:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29600",
    "user": "https://github.com/benjaminfjones"
}
```

`@`burcin: Okay! Good idea. I'll lazy import the Bessel stuff and create a new ticket for the rest.

`@`vbraun: Thanks! That's good detective work. How did you figure that out (I wasted a lot of time trying to find the culprit)?

----

I'll look into addressing the symbol table issue and report back with updated patches.



---

archive/issue_comments_029601.json:
```json
{
    "body": "Replying to [comment:53 benjaminfjones]:\n> `@`vbraun: Thanks! That's good detective work. How did you figure that out\n\nYou better sit down for this one ;-)\n\n```\n$ grep bessel_j sage/functions/*\n```\n",
    "created_at": "2013-05-28T17:03:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29601",
    "user": "https://github.com/vbraun"
}
```

Replying to [comment:53 benjaminfjones]:
> `@`vbraun: Thanks! That's good detective work. How did you figure that out

You better sit down for this one ;-)

```
$ grep bessel_j sage/functions/*
```




---

archive/issue_comments_029602.json:
```json
{
    "body": "Damn.",
    "created_at": "2013-05-28T17:17:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29602",
    "user": "https://github.com/benjaminfjones"
}
```

Damn.



---

archive/issue_comments_029603.json:
```json
{
    "body": "Just updating status due to the last few comments.  This would be really good to have ready to review at Sage Days 48/Edu Days 5 next week.",
    "created_at": "2013-06-11T17:59:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29603",
    "user": "https://github.com/kcrisman"
}
```

Just updating status due to the last few comments.  This would be really good to have ready to review at Sage Days 48/Edu Days 5 next week.



---

archive/issue_comments_029604.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-06-11T17:59:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29604",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_029605.json:
```json
{
    "body": "This would be nice for my GSoC project as well.",
    "created_at": "2013-06-14T01:16:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29605",
    "user": "https://github.com/eviatarbach"
}
```

This would be nice for my GSoC project as well.



---

archive/issue_comments_029606.json:
```json
{
    "body": "OK, I'll try to set aside some time for this tomorrow (or weekend).",
    "created_at": "2013-06-14T01:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29606",
    "user": "https://github.com/benjaminfjones"
}
```

OK, I'll try to set aside some time for this tomorrow (or weekend).



---

archive/issue_comments_029607.json:
```json
{
    "body": "Thank you! That would be great :)",
    "created_at": "2013-06-14T01:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29607",
    "user": "https://github.com/eviatarbach"
}
```

Thank you! That would be great :)



---

archive/issue_comments_029608.json:
```json
{
    "body": "adds bessel.py, lazy imports in all.py",
    "created_at": "2013-06-15T05:25:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29608",
    "user": "https://github.com/benjaminfjones"
}
```

adds bessel.py, lazy imports in all.py



---

archive/issue_comments_029609.json:
```json
{
    "body": "Attachment [trac_symbolic_bessel_v7.patch](tarball://root/attachments/some-uuid/ticket4102/trac_symbolic_bessel_v7.patch) by @benjaminfjones created at 2013-06-15 05:26:15\n\nfixes/updates doctests external to sage/functions/bessel.py",
    "created_at": "2013-06-15T05:26:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29609",
    "user": "https://github.com/benjaminfjones"
}
```

Attachment [trac_symbolic_bessel_v7.patch](tarball://root/attachments/some-uuid/ticket4102/trac_symbolic_bessel_v7.patch) by @benjaminfjones created at 2013-06-15 05:26:15

fixes/updates doctests external to sage/functions/bessel.py



---

archive/issue_comments_029610.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-06-15T05:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29610",
    "user": "https://github.com/benjaminfjones"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_029611.json:
```json
{
    "body": "Attachment [trac_symbolic_bessel_v7-doctests.patch](tarball://root/attachments/some-uuid/ticket4102/trac_symbolic_bessel_v7-doctests.patch) by @benjaminfjones created at 2013-06-15 05:33:06\n\nOK, uploaded two new patches which:\n1. address the problem raised in comment:41, solution is to replace construction of a new `MaximaFunction` object (which alters the symbol table) to construcing and evaluating the function directly inside Maxima using `maxima.function()`.\n2. change Bessel imports in `sage/functions/all.py` to lazy imports\n\nDoctests in all the touched files pass, I'll wait for the patchbot to see about the rest.\n\nHope y'all at Sage Days have a chance to review the patches.\n\n---- \n\nPatchbot, apply trac_symbolic_bessel_v7.patch trac_symbolic_bessel_v7-doctests.patch",
    "created_at": "2013-06-15T05:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29611",
    "user": "https://github.com/benjaminfjones"
}
```

Attachment [trac_symbolic_bessel_v7-doctests.patch](tarball://root/attachments/some-uuid/ticket4102/trac_symbolic_bessel_v7-doctests.patch) by @benjaminfjones created at 2013-06-15 05:33:06

OK, uploaded two new patches which:
1. address the problem raised in comment:41, solution is to replace construction of a new `MaximaFunction` object (which alters the symbol table) to construcing and evaluating the function directly inside Maxima using `maxima.function()`.
2. change Bessel imports in `sage/functions/all.py` to lazy imports

Doctests in all the touched files pass, I'll wait for the patchbot to see about the rest.

Hope y'all at Sage Days have a chance to review the patches.

---- 

Patchbot, apply trac_symbolic_bessel_v7.patch trac_symbolic_bessel_v7-doctests.patch



---

archive/issue_comments_029612.json:
```json
{
    "body": "There is another problem in `sage/calculus/desolvers.py`, I'm looking into it now.",
    "created_at": "2013-06-15T17:13:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29612",
    "user": "https://github.com/benjaminfjones"
}
```

There is another problem in `sage/calculus/desolvers.py`, I'm looking into it now.



---

archive/issue_comments_029613.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-06-15T17:13:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29613",
    "user": "https://github.com/benjaminfjones"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_029614.json:
```json
{
    "body": "When a symbolic function is lazily imported, its constructor isn't called until the function is referenced and the constructor is responsible for populating the symbol tables that make conversion work (e.g. maxima <-> sage). So with lazy importing here, if I start up Sage and call `desolve` with Bessel's diffeq, we don't properly convert the result from Maxima to Sage because the Bessel functions are not in the symbol table (they haven't been constructed yet).\n\nAny thoughts on this?\n\nOne idea I had is that we can register the conversions somewhere else (not in the constructors). But that would mean maintaining each symbolic function's code and its conversions in separate places (seems like a bad idea).\n\nAnother idea: import from sage.functions.bessel strictly (i.e. not lazily), but in bessel.py use lazy imports for everything that's not needed in the constructors.",
    "created_at": "2013-06-15T17:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29614",
    "user": "https://github.com/benjaminfjones"
}
```

When a symbolic function is lazily imported, its constructor isn't called until the function is referenced and the constructor is responsible for populating the symbol tables that make conversion work (e.g. maxima <-> sage). So with lazy importing here, if I start up Sage and call `desolve` with Bessel's diffeq, we don't properly convert the result from Maxima to Sage because the Bessel functions are not in the symbol table (they haven't been constructed yet).

Any thoughts on this?

One idea I had is that we can register the conversions somewhere else (not in the constructors). But that would mean maintaining each symbolic function's code and its conversions in separate places (seems like a bad idea).

Another idea: import from sage.functions.bessel strictly (i.e. not lazily), but in bessel.py use lazy imports for everything that's not needed in the constructors.



---

archive/issue_comments_029615.json:
```json
{
    "body": "I think my preference would be to put 'lazy import symbolic functions' off to another ticket. We can discuss the issues involved there. Meanwhile, this can be reviewed.",
    "created_at": "2013-06-15T17:36:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29615",
    "user": "https://github.com/benjaminfjones"
}
```

I think my preference would be to put 'lazy import symbolic functions' off to another ticket. We can discuss the issues involved there. Meanwhile, this can be reviewed.



---

archive/issue_comments_029616.json:
```json
{
    "body": "Attachment [trac_symbolic_bessel_v7.2.patch](tarball://root/attachments/some-uuid/ticket4102/trac_symbolic_bessel_v7.2.patch) by @benjaminfjones created at 2013-06-16 01:21:59",
    "created_at": "2013-06-16T01:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29616",
    "user": "https://github.com/benjaminfjones"
}
```

Attachment [trac_symbolic_bessel_v7.2.patch](tarball://root/attachments/some-uuid/ticket4102/trac_symbolic_bessel_v7.2.patch) by @benjaminfjones created at 2013-06-16 01:21:59



---

archive/issue_comments_029617.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-06-16T01:24:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29617",
    "user": "https://github.com/benjaminfjones"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_029618.json:
```json
{
    "body": "I removed the lazy import.\n\nReady for review!\n\n----\n\nPatchbot apply trac_symbolic_bessel_v7.2.patch trac_symbolic_bessel_v7-doctests.patch",
    "created_at": "2013-06-16T01:24:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29618",
    "user": "https://github.com/benjaminfjones"
}
```

I removed the lazy import.

Ready for review!

----

Patchbot apply trac_symbolic_bessel_v7.2.patch trac_symbolic_bessel_v7-doctests.patch



---

archive/issue_comments_029619.json:
```json
{
    "body": "Thanks, I'm looking at it now.\n\nCan I just remove all the assertions in `Bessel`? Some of them are redundant and I'm not sure why it's asserting that the order is real.",
    "created_at": "2013-06-17T19:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29619",
    "user": "https://github.com/eviatarbach"
}
```

Thanks, I'm looking at it now.

Can I just remove all the assertions in `Bessel`? Some of them are redundant and I'm not sure why it's asserting that the order is real.



---

archive/issue_comments_029620.json:
```json
{
    "body": "Here's what I changed:\n* Added documentation to the manuals\n* Fixed a `bessel_K` identity that was incorrect\n* Added SymPy conversions\n* Minor formatting changes\n* Removed assertions (I'll add them back if they were necessary)\n* \"for an arbitrary real number `\\nu` (the order)\" > \"for an arbitrary complex number `\\nu` (the order)\"\n\nLooks good otherwise!",
    "created_at": "2013-06-17T21:34:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29620",
    "user": "https://github.com/eviatarbach"
}
```

Here's what I changed:
* Added documentation to the manuals
* Fixed a `bessel_K` identity that was incorrect
* Added SymPy conversions
* Minor formatting changes
* Removed assertions (I'll add them back if they were necessary)
* "for an arbitrary real number `\nu` (the order)" > "for an arbitrary complex number `\nu` (the order)"

Looks good otherwise!



---

archive/issue_comments_029621.json:
```json
{
    "body": "Attachment [bessel_2.patch](tarball://root/attachments/some-uuid/ticket4102/bessel_2.patch) by @eviatarbach created at 2013-06-17 21:36:06",
    "created_at": "2013-06-17T21:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29621",
    "user": "https://github.com/eviatarbach"
}
```

Attachment [bessel_2.patch](tarball://root/attachments/some-uuid/ticket4102/bessel_2.patch) by @eviatarbach created at 2013-06-17 21:36:06



---

archive/issue_comments_029622.json:
```json
{
    "body": "Thanks, those changes all look fine. The assertions aren't necessary, I should have removed them.\n\n----\n\nPatchbot apply trac_symbolic_bessel_v7.2.patch trac_symbolic_bessel_v7-doctests.patch bessel_2.patch",
    "created_at": "2013-06-17T22:10:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29622",
    "user": "https://github.com/benjaminfjones"
}
```

Thanks, those changes all look fine. The assertions aren't necessary, I should have removed them.

----

Patchbot apply trac_symbolic_bessel_v7.2.patch trac_symbolic_bessel_v7-doctests.patch bessel_2.patch



---

archive/issue_comments_029623.json:
```json
{
    "body": "Great. I just noticed that it was already in the manuals though. New patch.\n\n----\n\nPatchbot apply trac_symbolic_bessel_v7.2.patch trac_symbolic_bessel_v7-doctests.patch bessel_2.2.patch",
    "created_at": "2013-06-17T22:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29623",
    "user": "https://github.com/eviatarbach"
}
```

Great. I just noticed that it was already in the manuals though. New patch.

----

Patchbot apply trac_symbolic_bessel_v7.2.patch trac_symbolic_bessel_v7-doctests.patch bessel_2.2.patch



---

archive/issue_comments_029624.json:
```json
{
    "body": "Attachment [bessel_2.2.patch](tarball://root/attachments/some-uuid/ticket4102/bessel_2.2.patch) by @eviatarbach created at 2013-06-17 22:34:01",
    "created_at": "2013-06-17T22:34:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29624",
    "user": "https://github.com/eviatarbach"
}
```

Attachment [bessel_2.2.patch](tarball://root/attachments/some-uuid/ticket4102/bessel_2.2.patch) by @eviatarbach created at 2013-06-17 22:34:01



---

archive/issue_comments_029625.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd48\".",
    "created_at": "2013-06-17T22:49:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29625",
    "user": "https://github.com/burcin"
}
```

Changing keywords from "" to "sd48".



---

archive/issue_comments_029626.json:
```json
{
    "body": "All patches look good to me. We can switch this to positive review once the patchbot gives it a green light.",
    "created_at": "2013-06-17T22:49:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29626",
    "user": "https://github.com/burcin"
}
```

All patches look good to me. We can switch this to positive review once the patchbot gives it a green light.



---

archive/issue_comments_029627.json:
```json
{
    "body": "Nice work!  A lot of the thing Eviatar fixed were exactly the things I was thinking about on the train.  Good stuff.  Patchbot doesn't seem to be using the right patch, so:\n\nPatchbot apply trac_symbolic_bessel_v7.2.patch trac_symbolic_bessel_v7-doctests.patch bessel_2.2.patch",
    "created_at": "2013-06-18T04:43:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29627",
    "user": "https://github.com/kcrisman"
}
```

Nice work!  A lot of the thing Eviatar fixed were exactly the things I was thinking about on the train.  Good stuff.  Patchbot doesn't seem to be using the right patch, so:

Patchbot apply trac_symbolic_bessel_v7.2.patch trac_symbolic_bessel_v7-doctests.patch bessel_2.2.patch



---

archive/issue_comments_029628.json:
```json
{
    "body": "This passes all tests for me.",
    "created_at": "2013-06-18T17:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29628",
    "user": "https://github.com/kcrisman"
}
```

This passes all tests for me.



---

archive/issue_comments_029629.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-06-18T17:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29629",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_029630.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2013-06-18T17:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29630",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_029631.json:
```json
{
    "body": "I get several doctest failures:\n\n```\nsage -t --long devel/sage/sage/functions/bessel.py\n**********************************************************************\nFile \"devel/sage/sage/functions/bessel.py\", line 101, in sage.functions.bessel\nFailed example:\n    bessel_J(0, x).diff(x)\nExpected:\n    1/2*bessel_J(-1, x) - 1/2*bessel_J(1, x)\nGot:\n    -1/2*bessel_J(1, x) + 1/2*bessel_J(-1, x)\n**********************************************************************\nFile \"devel/sage/sage/functions/bessel.py\", line 248, in sage.functions.bessel.Function_Bessel_J\nFailed example:\n    f.diff(x)\nExpected:\n    1/2*bessel_J(1, x) - 1/2*bessel_J(3, x)\nGot:\n    -1/2*bessel_J(3, x) + 1/2*bessel_J(1, x)\n**********************************************************************\nFile \"devel/sage/sage/functions/bessel.py\", line 357, in sage.functions.bessel.Function_Bessel_J._derivative_\nFailed example:\n    derivative(f, z)\nExpected:\n    z |--> 1/2*bessel_J(9, z) - 1/2*bessel_J(11, z)\nGot:\n    z |--> -1/2*bessel_J(11, z) + 1/2*bessel_J(9, z)\n**********************************************************************\n```\n\n(and various similar failures)",
    "created_at": "2013-06-19T06:41:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29631",
    "user": "https://github.com/jdemeyer"
}
```

I get several doctest failures:

```
sage -t --long devel/sage/sage/functions/bessel.py
**********************************************************************
File "devel/sage/sage/functions/bessel.py", line 101, in sage.functions.bessel
Failed example:
    bessel_J(0, x).diff(x)
Expected:
    1/2*bessel_J(-1, x) - 1/2*bessel_J(1, x)
Got:
    -1/2*bessel_J(1, x) + 1/2*bessel_J(-1, x)
**********************************************************************
File "devel/sage/sage/functions/bessel.py", line 248, in sage.functions.bessel.Function_Bessel_J
Failed example:
    f.diff(x)
Expected:
    1/2*bessel_J(1, x) - 1/2*bessel_J(3, x)
Got:
    -1/2*bessel_J(3, x) + 1/2*bessel_J(1, x)
**********************************************************************
File "devel/sage/sage/functions/bessel.py", line 357, in sage.functions.bessel.Function_Bessel_J._derivative_
Failed example:
    derivative(f, z)
Expected:
    z |--> 1/2*bessel_J(9, z) - 1/2*bessel_J(11, z)
Got:
    z |--> -1/2*bessel_J(11, z) + 1/2*bessel_J(9, z)
**********************************************************************
```

(and various similar failures)



---

archive/issue_comments_029632.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-06-19T06:41:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29632",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_029633.json:
```json
{
    "body": "Perhaps this is due to #9880.",
    "created_at": "2013-06-19T06:42:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29633",
    "user": "https://github.com/jdemeyer"
}
```

Perhaps this is due to #9880.



---

archive/issue_comments_029634.json:
```json
{
    "body": "Attachment [trac_4102-bessel_doctest_fixes.patch](tarball://root/attachments/some-uuid/ticket4102/trac_4102-bessel_doctest_fixes.patch) by @burcin created at 2013-06-19 14:43:46",
    "created_at": "2013-06-19T14:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29634",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_4102-bessel_doctest_fixes.patch](tarball://root/attachments/some-uuid/ticket4102/trac_4102-bessel_doctest_fixes.patch) by @burcin created at 2013-06-19 14:43:46



---

archive/issue_comments_029635.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-06-19T14:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29635",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_029636.json:
```json
{
    "body": "I uploaded a new patch to fix doctest failures caused by #9880.",
    "created_at": "2013-06-19T14:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29636",
    "user": "https://github.com/burcin"
}
```

I uploaded a new patch to fix doctest failures caused by #9880.



---

archive/issue_comments_029637.json:
```json
{
    "body": "Looks good and passes tests.",
    "created_at": "2013-06-19T20:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29637",
    "user": "https://github.com/kcrisman"
}
```

Looks good and passes tests.



---

archive/issue_comments_029638.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-19T20:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29638",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_029639.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-06-20T19:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29639",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_029640.json:
```json
{
    "body": "On `silius` (ia64):\n\n```\nsage -t --long devel/sage/sage/functions/bessel.py\n**********************************************************************\nFile \"devel/sage/sage/functions/bessel.py\", line 258, in sage.functions.bessel.Function_Bessel_J\nFailed example:\n    A[0]\nExpected:\n    0.44005058574493355\nGot:\n    0.44005058574493366\n**********************************************************************\n```\n",
    "created_at": "2013-06-20T19:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29640",
    "user": "https://github.com/jdemeyer"
}
```

On `silius` (ia64):

```
sage -t --long devel/sage/sage/functions/bessel.py
**********************************************************************
File "devel/sage/sage/functions/bessel.py", line 258, in sage.functions.bessel.Function_Bessel_J
Failed example:
    A[0]
Expected:
    0.44005058574493355
Got:
    0.44005058574493366
**********************************************************************
```




---

archive/issue_comments_029641.json:
```json
{
    "body": "Attachment [trac_4102-bessel_doctest_fixes2.patch](tarball://root/attachments/some-uuid/ticket4102/trac_4102-bessel_doctest_fixes2.patch) by @eviatarbach created at 2013-06-20 20:17:30\n\nNew patch, adding a tolerance for the integral which is higher than the maximum error given by GSL.",
    "created_at": "2013-06-20T20:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29641",
    "user": "https://github.com/eviatarbach"
}
```

Attachment [trac_4102-bessel_doctest_fixes2.patch](tarball://root/attachments/some-uuid/ticket4102/trac_4102-bessel_doctest_fixes2.patch) by @eviatarbach created at 2013-06-20 20:17:30

New patch, adding a tolerance for the integral which is higher than the maximum error given by GSL.



---

archive/issue_comments_029642.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-06-20T20:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29642",
    "user": "https://github.com/eviatarbach"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_029643.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-20T20:46:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29643",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_029644.json:
```json
{
    "body": "Thanks!",
    "created_at": "2013-06-20T20:46:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29644",
    "user": "https://github.com/burcin"
}
```

Thanks!



---

archive/issue_comments_029645.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-07-31T12:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29645",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_029646.json:
```json
{
    "body": "This is wrong:\n\n\n```\nsage: var('nu z')\n(nu, z)\nsage: bessel_J(nu, z).diff(nu)\n-1/2*bessel_J(nu + 1, z) + 1/2*bessel_J(nu - 1, z)\nsage: bessel_J(nu, z).diff(z)\n-1/2*bessel_J(nu + 1, z) + 1/2*bessel_J(nu - 1, z)\n```\n",
    "created_at": "2013-08-07T06:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29646",
    "user": "https://github.com/eviatarbach"
}
```

This is wrong:


```
sage: var('nu z')
(nu, z)
sage: bessel_J(nu, z).diff(nu)
-1/2*bessel_J(nu + 1, z) + 1/2*bessel_J(nu - 1, z)
sage: bessel_J(nu, z).diff(z)
-1/2*bessel_J(nu + 1, z) + 1/2*bessel_J(nu - 1, z)
```




---

archive/issue_comments_029647.json:
```json
{
    "body": "Attachment [trac4102_diff.patch](tarball://root/attachments/some-uuid/ticket4102/trac4102_diff.patch) by @eviatarbach created at 2013-08-07 06:38:34",
    "created_at": "2013-08-07T06:38:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29647",
    "user": "https://github.com/eviatarbach"
}
```

Attachment [trac4102_diff.patch](tarball://root/attachments/some-uuid/ticket4102/trac4102_diff.patch) by @eviatarbach created at 2013-08-07 06:38:34



---

archive/issue_comments_029648.json:
```json
{
    "body": "New patch fixes this issue. Can this be merged in 5.11?",
    "created_at": "2013-08-07T06:40:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29648",
    "user": "https://github.com/eviatarbach"
}
```

New patch fixes this issue. Can this be merged in 5.11?



---

archive/issue_comments_029649.json:
```json
{
    "body": "Replying to [comment:83 eviatarbach]:\n> New patch fixes this issue. Can this be merged in 5.11?\nNo, you should make a follow-up ticket for this.",
    "created_at": "2013-08-07T07:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29649",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:83 eviatarbach]:
> New patch fixes this issue. Can this be merged in 5.11?
No, you should make a follow-up ticket for this.



---

archive/issue_comments_029650.json:
```json
{
    "body": "Oh okay, then can this ticket be removed from 5.11? I'm just worried about having mathematically incorrect answers in the release.",
    "created_at": "2013-08-07T07:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29650",
    "user": "https://github.com/eviatarbach"
}
```

Oh okay, then can this ticket be removed from 5.11? I'm just worried about having mathematically incorrect answers in the release.



---

archive/issue_comments_029651.json:
```json
{
    "body": "Replying to [comment:83 eviatarbach]:\n> New patch fixes this issue. Can this be merged in 5.11?\nSorry, I really meant: perhaps yes it can be in sage-5.11, but in any case there needs to be a follow-up ticket (make it milestone: sage-5.11 and priority: blocker) and the new patch needs to be reviewed.",
    "created_at": "2013-08-07T07:54:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29651",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:83 eviatarbach]:
> New patch fixes this issue. Can this be merged in 5.11?
Sorry, I really meant: perhaps yes it can be in sage-5.11, but in any case there needs to be a follow-up ticket (make it milestone: sage-5.11 and priority: blocker) and the new patch needs to be reviewed.



---

archive/issue_comments_029652.json:
```json
{
    "body": "Also, add a doctest for the `NotImplementedError` (like the tests from [comment:82])",
    "created_at": "2013-08-07T07:58:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29652",
    "user": "https://github.com/jdemeyer"
}
```

Also, add a doctest for the `NotImplementedError` (like the tests from [comment:82])



---

archive/issue_comments_029653.json:
```json
{
    "body": "Okay, thank you. This is now #15019.",
    "created_at": "2013-08-07T08:21:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4102",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4102#issuecomment-29653",
    "user": "https://github.com/eviatarbach"
}
```

Okay, thank you. This is now #15019.
