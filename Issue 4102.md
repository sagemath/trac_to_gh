# Issue 4102: Make special functions behave like PrimitiveFunction

Issue created by migration from Trac.

Original creator: jwmerrill

Original creation time: 2008-09-12 01:06:09

Assignee: burcin

CC:  jason kcrisman benjaminfjones dsm burcin eviatarbach

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


---

Comment by ddrake created at 2008-09-12 02:14:56

Orthogonal polynomials seem to work fine; you can plot the `legendre_P`, `hermite`, and `jacobi_P` polynomials with `plot(legendre_P(4, x), (x,-1,1))` and so on. So whatever magic they are using might work for the Bessel functions and other special functions.


---

Comment by jason created at 2008-09-12 04:00:02

Changing keywords from "" to "jason".


---

Comment by jason created at 2008-09-12 04:00:09

Changing keywords from "jason" to "".


---

Comment by burcin created at 2011-06-14 18:22:41

This ticket description was too broad. We have lots of tickets on fixing symbolic functions, see [symbolics/functions](symbolics-functions) for an overview.

See #3426 and #4230 for other tickets related to bessel functions. It would make sense to fix all these together, with a base class that handles the common properties of bessel functions (differentiation), and subclasses that implement numerical evaluation, etc. for each type.


---

Comment by kcrisman created at 2012-09-16 03:05:40

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

Comment by benjaminfjones created at 2012-10-03 03:03:29

This wouldn't be hard to implement using #11143 as a template, but what to do about names? I guess new names for the symbolic Bessel functions should be chosen and deprecation notices added to the existing `Bessel_J` etc. 

What new names do people like in the interim? 

 * `bessel_J_symbolic`
 * `bessel_J_sym`
 * `bessel_Js`

???


---

Comment by burcin created at 2012-10-03 11:22:29

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

Comment by kcrisman created at 2012-10-03 14:00:33

> What is wrong with taking over `bessel_{I,J,K,Y}`? Why do we need interim names?
I concur.
> >  * `bessel_J_symbolic`
One could use that as the "symbolic" class one and then do the usual `foo = Foo_Class()`?
> Thanks for looking into this.
Agreed!


---

Comment by ddrake created at 2012-10-03 16:29:27

Replying to [comment:8 benjaminfjones]:
> What new names do people like in the interim? 

I agree with Burcin: just use `bessel_J` (etc) if possible.

But regardless of the name, I'd love to see this get in -- it will make teaching a PDE class a bit easier. (No more `lambda` expressions in the plots...) Thanks for working on this!


---

Comment by benjaminfjones created at 2012-11-19 07:10:06

I thought I'd post some work in progress for all the Bessel function fans in the crowd. There is still work to be done, e.g.

 * getting symbolic integration via Maxima to work
 * adding maxima, scipy, PARI, etc. to the implemented backend systems
 * more documentation and doctests

but at this point the patch applies cleanly to 5.4.1 and all the doctests in `sage/functions/special.py` pass.

If you are interested, have a look at the doctests included with the `Bessel` function for examples and let me know if you see any serious problems (other than the deficits I've listed above).

Thanks!


---

Comment by benjaminfjones created at 2012-11-19 07:11:09

work in progress making Bessel functions symbolic


---

Attachment

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

Comment by burcin created at 2012-11-20 11:13:08

Thanks for the patch. Bessel functions are symbolic with so few lines of code. Amazing. :)

I like the metaclass idea. That never occured to me before as an option for functions with parameters, like the order here. I have a few questions:

 - what is the advantage of creating a new symbolic function for each (type, order) pair, instead of having a generic function for each type that takes the order as a parameter? The latter would be similar to the design of the `psi()` function in GiNaC/Pynac.

 - wouldn't this approach make life harder if in the future we want to add exact evaluation method for Bessel_J only?

I am also concerned about blowing up the symbolic function registry with these instances. Note that we keep an entry in a C++ list with a pointer to all the possible custom methods, and a Python dictionary with a function -> Pynac id mapping for each subclass of `BuiltinFunction` that is instantiated.

BTW, I suggest moving this code to a new file `sage/functions/bessel.py`.


---

Comment by benjaminfjones created at 2012-12-27 20:18:41

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

Comment by benjaminfjones created at 2012-12-27 20:27:10

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

Comment by kcrisman created at 2012-12-27 20:44:38

> >  * Maybe Python 3 string formatting?  Though I am not sure how to mix that with LaTeX braces.
> 
> ???

Such as [this](http://docs.python.org/3.1/library/stdtypes.html#str.format) and [this](http://docs.python.org/3.1/library/string.html#formatstrings).  Just for forward-compatibility (instead of the percent business).  Problem is that when I looked for ways to get around braces "naturally" occurring in LaTeX, there weren't necessarily a lot of them.  (Ways, that is.)


---

Comment by benjaminfjones created at 2012-12-27 23:53:51

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

Attachment

more work in progress


---

Comment by kcrisman created at 2013-01-03 15:25:29

Just as an FYI, [this ask.sagemath question](http://ask.sagemath.org/question/2129/arbitrary-precision-bessely) wants lots and lots of precision on Bessel Y.  Which I think will be provided here via mpmath - just pointing out we should doctest it.


---

Comment by kcrisman created at 2013-01-03 15:38:06

Also, I think that #3426 and #4230 probably would be solved by a successful resolution of this ticket.  Let's make sure to include any suggested (and useful) doctests from there here.


---

Comment by benjaminfjones created at 2013-01-13 05:05:37

Yet more work in progress, added lots of doctests, in particular to show that problems in #4230 and #3426 are fixed by this patch. One feature this patch adds is the ability to solve
Bessel's diffeq (using Maxima) and get a usable symbolic solution back (see the doctests in the module level docstring and in the Bessel() function). 

Added brief mathematical exposition on the module docstring as well as some usage EXAMPLES.

I think the patch is more or less ready for initial review. All tests withing the new file `sage/functions/bessel.py` pass on my machine and sage-5.6.beta3, but there are several doctests failing in other places that reference the Bessel functions. I'll work on patching those up for the next iteration.


---

Comment by benjaminfjones created at 2013-01-13 05:06:15

more work in progress, v3


---

Attachment

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
 * I suppose we don't need to keep _all_ old tests, but some of them are rather different and might be worth putting in a TESTS section somewhere, just so that we don't have some unexpected regression only they catch.
 * The switch to alpha from nu - I would rather not deprecate this either, but in principle someone could have used it as a keyword argument in the past...


---

Comment by kcrisman created at 2013-02-08 18:14:01

Changing status from new to needs_review.


---

Comment by kcrisman created at 2013-02-08 18:14:01

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

Comment by kcrisman created at 2013-02-08 18:15:03

Needs work:
 * doctest fixes, various minor documentation and other issues

And needs review on the code itself :-)

But now it's really looking tractable to finish this off.


---

Comment by kcrisman created at 2013-02-08 18:15:03

Changing status from needs_review to needs_work.


---

Comment by benjaminfjones created at 2013-02-13 07:06:17

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

>  * I suppose we don't need to keep _all_ old tests, but some of them are rather different and might be worth putting in a TESTS section somewhere, just so that we don't have some unexpected regression only they catch.

Good point, I'll see what I can salvage.

>  * The switch to alpha from nu - I would rather not deprecate this either, but in principle someone could have used it as a keyword argument in the past...

It doesn't make a difference to me, I used alpha because that's what's on the wikipedia page :) Abramowitz & Stegun uses n or \nu and so does the mpmath documentation. I can easily switch \alpha to \nu with some editor-fu.


---

Attachment

fix doctests and tutorial references involving Bessel function API


---

Comment by benjaminfjones created at 2013-03-12 20:51:54

Changing status from needs_work to needs_review.


---

Comment by benjaminfjones created at 2013-03-12 20:51:54

I've uploaded two new patches addressing comments by `@`kcrisman. The two latest patches are finally ready for complete review.

Patchbot:

Apply trac_symbolic_bessel_v5.patch trac_symbolic_bessel_doctests.patch


---

Comment by benjaminfjones created at 2013-03-12 20:58:35

Some additional notes regarding your comments, `@`kcrisman:

 - The doctest of `desolve` that was failing was returning unconverted Maxima output, that's what the `bessel_j`, etc are. With the v5 patch we now have an honest Sage symbolic function as the return value in that case (also, see the diff eq doctest examples I wrote).

 - I changes from using \alpha as the order to \nu for consistency with mpmath and Maxima.

 - I changed the random expression seed to 53 (my favorite random integer) and that test no longer raises an exception.


---

Comment by kcrisman created at 2013-03-13 16:11:51

Nice work.  I do feel like we should ask on sage-devel about deprecating the evaluation system keywords versus (as in the current version) simply removing them but leaving room for their return...

```
assert _system == 'mpmath' 
```

I suppose we could at least doctest this as a todo with the error message it receives with the "wrong" input.

I still want to give it a final go-over, but various testing of your tests and code makes me think this is ready.  What a job!


---

Comment by benjaminfjones created at 2013-03-26 00:54:33

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

Comment by benjaminfjones created at 2013-03-26 21:15:48

After chatting with `@`burcin, I decided to do 1. The new patch implements deprecation by retaining all the old code with names prefixed by an underscore. I preserved all the old doctests (which reference the underscored names). In the new code, I overrode `__call__` if more than 2 arguments are given.

Ready for review!


---

Comment by benjaminfjones created at 2013-03-26 21:18:05

Patchbot, apply trac_symbolic_bessel_v5.patch trac_symbolic_bessel_doctests.patch trac_symbolic_bessel_deprecation.patch


---

Comment by kcrisman created at 2013-03-27 01:11:51

Can you remind me what the plan was for algorithm as a keyword?  Wasn't there some plan to _re_introduce it once we got the hooks in properly, so that people could easily compare e.g. Pari, mpmath, Mma (if available), etc.?  Doesn't mean this patch couldn't go in, just trying to get things straight.

Quick glance at the latest patch looks good.  What a lot of underscores; did you write a script?


---

Comment by benjaminfjones created at 2013-03-27 01:32:20

The algorithm keyword in _eval_ requires a work in progress branch of pynac that has probably bit rot by now. I have it on my agenda (since last year!) to look back into it..


---

Comment by kcrisman created at 2013-03-27 01:39:12

Right, I understand - my point is that maybe the deprecation message should be slightly different, something like

```
deprecation(4102, 'precision argument is deprecated\nalgorithm argument will only be available as a named keyword in the future and is currently in mothballs')
```

or something somewhat more professional/accurate than that.


---

Comment by benjaminfjones created at 2013-03-27 17:13:58

I see, sure, how about just:

"precision argument is deprecated, algorithm argument is currently deprecated, but will be available as a named keyword in the future"


---

Comment by kcrisman created at 2013-03-27 17:29:40

> I see, sure, how about just:
> "precision argument is deprecated, algorithm argument is currently deprecated, but will be available as a named keyword in the future"
That sounds good, except that I would put a semicolon instead of a comma in the first comma spot.


---

Comment by benjaminfjones created at 2013-03-27 19:26:51

add deprecation of old API


---

Attachment

latest symbolic Bessel functions patch, ready for review


---

Comment by benjaminfjones created at 2013-03-28 00:09:06

Latest attachment makes a tiny doc change to fix a latex mistake.


---

Comment by benjaminfjones created at 2013-03-29 22:47:44

Patchbot apply trac_symbolic_bessel_v5.patch trac_symbolic_bessel_doctests.patch trac_symbolic_bessel_deprecation.patch


---

Comment by vbraun created at 2013-04-01 20:55:00

Patchbot shows test failures on sage-5.9.beta2


---

Comment by kcrisman created at 2013-04-02 00:36:11

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

Comment by benjaminfjones created at 2013-04-02 04:46:31

There is something strange going on. Here is sage-5.9.beta2 with the three patches applied:


```
[bjones`@`cabbage:devel/sage]% ../../sage
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
[bjones`@`cabbage:devel/sage]% ../../sage -t sage/functions/bessel.py                
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

Comment by vbraun created at 2013-04-02 08:29:40

Maxima is the same version in sage-5.8 and 5.9.beta2, so thats not it.

The new doctesting framework was introduced in sage-5.9.beta, thats a likely suspect. It uses fork, so external interfaces need to be shut down / restarted. Perhaps the restarted maxima process is not set up correctly? Though just using ``@`fork` seems to work.


---

Comment by jdemeyer created at 2013-04-05 15:43:40

benjaminfjones: I don't understand the problem. It seems to me that the doctest should simply be changed to match the "correct" output.


---

Comment by benjaminfjones created at 2013-04-05 16:00:00

So the correct output is:


```
(bessel_J(0, 1) + bessel_J(1, 1))*bessel_Y(0, x)/(bessel_Y(0, 1)*bessel_J(1, 1) - bessel_Y(1, 1)*bessel_J(0, 1)) - (bessel_Y(0, 1) + bessel_Y(1, 1))*bessel_J(0, x)/(bessel_Y(0, 1)*bessel_J(1, 1) - bessel_Y(1, 1)*bessel_J(0, 1))
```


that is both mathematically correct and what you get when you apply the patches, run sage, and execute the commands manually.

The problem is that when you **doctest** the same exact commands in the same exact sage, the output that comes back is different in two ways (explained in the comment above).


---

Comment by benjaminfjones created at 2013-04-05 16:58:54

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

Comment by jdemeyer created at 2013-04-09 12:28:41

Replying to [comment:45 benjaminfjones]:
> So it looks like there is some hidden state affecting the doctesting in scenario (2). 
The doctests which are run _before_ that test are extra "state".


---

Comment by kcrisman created at 2013-04-25 02:21:45

See also #2516.


---

Comment by benjaminfjones created at 2013-05-20 23:22:14

Copy of trac_symbolic_bessel_v5, minus one doctest block


---

Attachment

Copy of trac_symbolic_bessel_v5, minus one doctest block


---

Comment by benjaminfjones created at 2013-05-20 23:33:58

I still have not been able to track down the doctesting issue (described starting at comment:41). I've tried bisecting the doctest state (delta debugging) to no avail. The problem seems to be intimately linked to the doctesting environment. I'm unable to reproduce the doctest failure when running __all__ the prior doctests which come before in `bessel.py`, in the right order, by hand, and then running the offending one.

The only thing I can tell for sure is that at some point as the doctests are run, one of the pynac symbol tables get's modified. This causes the `bessel_j` vs `bessel_J` problem.

My inclination is to remove the offending doctest and file a new ticket to resolve the problem. Meanwhile, the bessel function code can be reviewed and become useful. I've posted a patch `trac_symbolic_bessel_v6` which removes the offending doctest block.

Comments?

----

Patchbot, apply trac_symbolic_bessel_v6.patch trac_symbolic_bessel_doctests.patch trac_symbolic_bessel_deprecation.patch


---

Comment by benjaminfjones created at 2013-05-27 16:58:09

Tests are passing on 5.10.beta4. The startup time plugin is failing, however. Should we lazy import here? Also how about lazy import for all the special functions (the idea being that relatively few users will need any given special function)?


---

Comment by burcin created at 2013-05-27 17:09:42

Replying to [comment:49 benjaminfjones]:
> Tests are passing on 5.10.beta4. The startup time plugin is failing, however. Should we lazy import here? Also how about lazy import for all the special functions (the idea being that relatively few users will need any given special function)?

+100 to lazy import for all special functions, but in a separate ticket.

It would be great if you can use lazy import for the functions defined here to silence the startup time plugin.


About the doctesting framework issue: I briefly tried to debug this and didn't get anywhere either. I agree that we should move this to a new ticket and not hold this one up longer. Instead of removing the test, can you mark it `# not tested` and mention the ticket number?

Thanks a lot for your work on this.


---

Comment by vbraun created at 2013-05-27 18:49:37

I'm trying to understand how the interfacing works. Is this the intended output?

```
sage: maxima(bessel_I).sage()
bessel_i
```



---

Comment by vbraun created at 2013-05-27 19:07:37

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

Comment by benjaminfjones created at 2013-05-28 16:55:59

`@`burcin: Okay! Good idea. I'll lazy import the Bessel stuff and create a new ticket for the rest.

`@`vbraun: Thanks! That's good detective work. How did you figure that out (I wasted a lot of time trying to find the culprit)?

----

I'll look into addressing the symbol table issue and report back with updated patches.


---

Comment by vbraun created at 2013-05-28 17:03:08

Replying to [comment:53 benjaminfjones]:
> `@`vbraun: Thanks! That's good detective work. How did you figure that out

You better sit down for this one ;-)

```
$ grep bessel_j sage/functions/*
```



---

Comment by benjaminfjones created at 2013-05-28 17:17:07

Damn.


---

Comment by kcrisman created at 2013-06-11 17:59:19

Just updating status due to the last few comments.  This would be really good to have ready to review at Sage Days 48/Edu Days 5 next week.


---

Comment by kcrisman created at 2013-06-11 17:59:19

Changing status from needs_review to needs_work.


---

Comment by eviatarbach created at 2013-06-14 01:16:24

This would be nice for my GSoC project as well.


---

Comment by benjaminfjones created at 2013-06-14 01:20:11

OK, I'll try to set aside some time for this tomorrow (or weekend).


---

Comment by eviatarbach created at 2013-06-14 01:31:52

Thank you! That would be great :)


---

Comment by benjaminfjones created at 2013-06-15 05:25:41

adds bessel.py, lazy imports in all.py


---

Attachment

fixes/updates doctests external to sage/functions/bessel.py


---

Comment by benjaminfjones created at 2013-06-15 05:33:06

Changing status from needs_work to needs_review.


---

Attachment

OK, uploaded two new patches which:
 1. address the problem raised in comment:41, solution is to replace construction of a new `MaximaFunction` object (which alters the symbol table) to construcing and evaluating the function directly inside Maxima using `maxima.function()`.
 2. change Bessel imports in `sage/functions/all.py` to lazy imports

Doctests in all the touched files pass, I'll wait for the patchbot to see about the rest.

Hope y'all at Sage Days have a chance to review the patches.

---- 

Patchbot, apply trac_symbolic_bessel_v7.patch trac_symbolic_bessel_v7-doctests.patch


---

Comment by benjaminfjones created at 2013-06-15 17:13:47

There is another problem in `sage/calculus/desolvers.py`, I'm looking into it now.


---

Comment by benjaminfjones created at 2013-06-15 17:13:47

Changing status from needs_review to needs_work.


---

Comment by benjaminfjones created at 2013-06-15 17:27:29

When a symbolic function is lazily imported, its constructor isn't called until the function is referenced and the constructor is responsible for populating the symbol tables that make conversion work (e.g. maxima <-> sage). So with lazy importing here, if I start up Sage and call `desolve` with Bessel's diffeq, we don't properly convert the result from Maxima to Sage because the Bessel functions are not in the symbol table (they haven't been constructed yet).

Any thoughts on this?

One idea I had is that we can register the conversions somewhere else (not in the constructors). But that would mean maintaining each symbolic function's code and its conversions in separate places (seems like a bad idea).

Another idea: import from sage.functions.bessel strictly (i.e. not lazily), but in bessel.py use lazy imports for everything that's not needed in the constructors.


---

Comment by benjaminfjones created at 2013-06-15 17:36:41

I think my preference would be to put 'lazy import symbolic functions' off to another ticket. We can discuss the issues involved there. Meanwhile, this can be reviewed.


---

Attachment


---

Comment by benjaminfjones created at 2013-06-16 01:24:01

Changing status from needs_work to needs_review.


---

Comment by benjaminfjones created at 2013-06-16 01:24:01

I removed the lazy import.

Ready for review!

----

Patchbot apply trac_symbolic_bessel_v7.2.patch trac_symbolic_bessel_v7-doctests.patch


---

Comment by eviatarbach created at 2013-06-17 19:26:49

Thanks, I'm looking at it now.

Can I just remove all the assertions in `Bessel`? Some of them are redundant and I'm not sure why it's asserting that the order is real.


---

Comment by eviatarbach created at 2013-06-17 21:34:56

Here's what I changed:
* Added documentation to the manuals
* Fixed a `bessel_K` identity that was incorrect
* Added SymPy conversions
* Minor formatting changes
* Removed assertions (I'll add them back if they were necessary)
* "for an arbitrary real number `\nu` (the order)" > "for an arbitrary complex number `\nu` (the order)"

Looks good otherwise!


---

Attachment


---

Comment by benjaminfjones created at 2013-06-17 22:10:49

Thanks, those changes all look fine. The assertions aren't necessary, I should have removed them.

----

Patchbot apply trac_symbolic_bessel_v7.2.patch trac_symbolic_bessel_v7-doctests.patch bessel_2.patch


---

Comment by eviatarbach created at 2013-06-17 22:33:22

Great. I just noticed that it was already in the manuals though. New patch.

----

Patchbot apply trac_symbolic_bessel_v7.2.patch trac_symbolic_bessel_v7-doctests.patch bessel_2.2.patch


---

Attachment


---

Comment by burcin created at 2013-06-17 22:49:10

Changing keywords from "" to "sd48".


---

Comment by burcin created at 2013-06-17 22:49:10

All patches look good to me. We can switch this to positive review once the patchbot gives it a green light.


---

Comment by kcrisman created at 2013-06-18 04:43:10

Nice work!  A lot of the thing Eviatar fixed were exactly the things I was thinking about on the train.  Good stuff.  Patchbot doesn't seem to be using the right patch, so:

Patchbot apply trac_symbolic_bessel_v7.2.patch trac_symbolic_bessel_v7-doctests.patch bessel_2.2.patch


---

Comment by kcrisman created at 2013-06-18 17:20:20

This passes all tests for me.


---

Comment by kcrisman created at 2013-06-18 17:20:20

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2013-06-18 17:20:36

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2013-06-19 06:41:30

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

Comment by jdemeyer created at 2013-06-19 06:41:30

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2013-06-19 06:42:24

Perhaps this is due to #9880.


---

Attachment


---

Comment by burcin created at 2013-06-19 14:45:49

Changing status from needs_work to needs_review.


---

Comment by burcin created at 2013-06-19 14:45:49

I uploaded a new patch to fix doctest failures caused by #9880.


---

Comment by kcrisman created at 2013-06-19 20:55:12

Looks good and passes tests.


---

Comment by kcrisman created at 2013-06-19 20:55:12

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-06-20 19:53:46

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2013-06-20 19:53:46

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

Attachment

New patch, adding a tolerance for the integral which is higher than the maximum error given by GSL.


---

Comment by eviatarbach created at 2013-06-20 20:17:30

Changing status from needs_work to needs_review.


---

Comment by burcin created at 2013-06-20 20:46:27

Changing status from needs_review to positive_review.


---

Comment by burcin created at 2013-06-20 20:46:27

Thanks!


---

Comment by jdemeyer created at 2013-07-31 12:52:56

Resolution: fixed


---

Comment by eviatarbach created at 2013-08-07 06:21:24

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

Attachment


---

Comment by eviatarbach created at 2013-08-07 06:40:02

New patch fixes this issue. Can this be merged in 5.11?


---

Comment by jdemeyer created at 2013-08-07 07:44:07

Replying to [comment:83 eviatarbach]:
> New patch fixes this issue. Can this be merged in 5.11?
No, you should make a follow-up ticket for this.


---

Comment by eviatarbach created at 2013-08-07 07:46:03

Oh okay, then can this ticket be removed from 5.11? I'm just worried about having mathematically incorrect answers in the release.


---

Comment by jdemeyer created at 2013-08-07 07:54:11

Replying to [comment:83 eviatarbach]:
> New patch fixes this issue. Can this be merged in 5.11?
Sorry, I really meant: perhaps yes it can be in sage-5.11, but in any case there needs to be a follow-up ticket (make it milestone: sage-5.11 and priority: blocker) and the new patch needs to be reviewed.


---

Comment by jdemeyer created at 2013-08-07 07:58:47

Also, add a doctest for the `NotImplementedError` (like the tests from [comment:82])


---

Comment by eviatarbach created at 2013-08-07 08:21:07

Okay, thank you. This is now #15019.
