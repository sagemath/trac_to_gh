# Issue 7763: make nintegrate/nintegral top-level functions

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-12-24 18:19:08

Assignee: burcin

CC:  kcrisman jason mhampton

We just need to add them to sage/devel/sage/misc/functional.py.  Modifying the versions of integrate/integral in that file would probably be easiest.


---

Comment by jason created at 2010-05-26 15:16:59

Changing keywords from "" to "beginner".


---

Comment by ryan created at 2010-09-11 23:02:43

Is this supposed to be a numerical approximation of the integral function?


---

Comment by kcrisman created at 2010-09-11 23:58:01

Replying to [comment:3 ryan]:
> Is this supposed to be a numerical approximation of the integral function?
No, this is an existing method of symbolic functions, which uses a different algorithm to get a numerical integral.  But you can only call it in 

```
sage: f(x)=some_formula_with_x
sage: f.nintegrate(...)
```

not as a top-level

```
nintegral(f,...)
```

type function.  

We should also probably make the syntax like that of `numerical_integral` *and* make that syntax consistent (at least as an option) with that of `integral` itself (see ask.sagemath.org for various problems this causes).


---

Comment by gagansekhon created at 2011-01-11 01:31:14

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-01-11 03:58:49

There are two issues with this.  First, because of the extreme possibility for confusion with the already top-level `numerical_integral`function, this will need some work in documentation.  See some of the documentation in 

```
sage: sage.calculus.calculus.nintegral??
```

for what I mean.   I don't think all of that needs to be there, but there should then be a reference for how to access the rest of it.  Basically, Maxima numerical integration and GSL numerical integration are different.  In particular, one would want to use Maxima for symbolic expressions - in case there is an exact answer known! - and then have a variety of options for numerical integration if that fails.

Anyway, that was a longish digression.  More importantly, this patch doesn't exactly do what is asked.   The point isn't to be able to approximate exact answers to integrals, but rather to expose to the top level the Maxima integration.  

```
sage: a = e^(-x^4 + x)
sage: a.nintegral(x,0,1)
(1.3638178766496709, 1.5141420080518571e-14, 21, 0)
sage: integral(a,(x,0,1)).n()
1.3638178766496716
```

Note the slight difference in output, incidentally - presumably within the error tolerance, of course.  This is because we apparently have a THIRD way to evaluate integrals - Pynac!

```
sage: R = RealField(53)
sage: integral(a,(x,0,1))._convert(R)
1.3638178766496716
```

If you check the code for `_convert`, it turns out this goes to Pynac.  See [here](http://www.ginac.de/reference/integral_8cpp_source.html#l00169) for some of how this happens in Ginac... crazy.  We really need to unify this.  But at any rate, we shouldn't use two different algorithms and do two different things for the same name `nintegrate`.   

Anyone have ideas for what the best resolution on this would be?

Oh, and just for comparison:

```
sage: numerical_integral(a,0,1)
(1.3638178766496716, 1.5141420080518571e-14)
```



---

Comment by kcrisman created at 2011-01-11 03:58:49

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2011-01-11 03:59:31

And of course a more informative commit message :)

Don't worry, this is on the way to being a good contribution; we just have to figure out what the right thing to do is.


---

Comment by gagansekhon created at 2011-01-11 04:42:18

Thank you, this actually gives me a better project and finding random tickets. I will try doing what you asked here.


---

Comment by gagansekhon created at 2011-01-12 06:02:53

There are two different inconsistency 

numerical_integral is top level only function and it uses gsl

nintegral is not top level and uses maxima

for consistency purpose I was thinking of doing the following:

1. to both add algorithm input, (the default would be gsl for top level and maxima for non-top level)

2. make both functions top level and methods

Any thoughts?


---

Comment by gagansekhon created at 2011-01-12 06:33:44

As for other *integra* all have either no algorithm option and uses maxima or only uses maxima. Still thinking the least complicated way to clean this up with most flexibility.


---

Comment by kcrisman created at 2011-01-12 15:38:09

Maybe the best thing to do would be to have ONE top level function for numerical integration (`numerical_integral`), of which `nintegrate` and `nintegral` would be aliases.   Then one would have to really at this time change the syntax of `numerical_integral` so that it accepts the same syntax as integration in general does; you'll notice that currently it does not accept a variable, only the endpoints:

```
            if hasattr(func, 'arguments'):
                vars = func.arguments()
            else:
                vars = func.variables()
```

so that it guesses what the correct variable is.   It also makes it really hard to do numerical integration on the fly with it, because you can't do [this](http://ask.sagemath.org/question/95/numerical-integration-in-a-function) very easily.

In that case, it would be easy to have several different algorithms. I don't know which would be better; in some sense, it would be best to always first see if we get an exact answer from Maxima, and if not, then do a numerical integral.  Or should it always do a straight-up numerical integral (whether from GSL, Maxima, Gi/Pynac...)?

As you can see, even trying to solve pretty 'easy' tickets can open a can of worms! Keep up the effort, though, it is much appreciated.


---

Comment by gagansekhon created at 2011-01-13 18:43:16

I am still working on this, but wanted to add a patch to show the progress.


---

Comment by gagansekhon created at 2011-01-13 18:44:18

Replying to [comment:12 gagansekhon]:
> I am still working on this, but wanted to add a patch to show the progress. 

the new patch integration.patch has the new and only progress.


---

Comment by kcrisman created at 2011-01-13 19:15:09

Thanks, good to see this!  

I would caution that for annoying reasons we like to have the lines in the documentation be fairly short; see some of the other calculus or plotting files for examples of about how many characters (80? 84?) are appropriate.  (Otherwise it looks really bad in command line.)  So any updates should fix that.


---

Attachment


---

Comment by gagansekhon created at 2011-01-17 17:15:30

Changing status from needs_work to needs_review.


---

Comment by gagansekhon created at 2011-01-17 17:16:12

Replying to [comment:15 gagansekhon]:
apply trac_7763.patch only


---

Attachment


---

Comment by kcrisman created at 2011-01-17 17:22:20

To buildbot: apply trac_7763.7.patch only.

(I think that the .6 and .7 patches must be identical, but it doesn't matter.)


---

Comment by gagansekhon created at 2011-01-18 02:31:48

Trac_7763.8.patch is the patch with everything, including commit line.


---

Comment by kcrisman created at 2011-01-18 16:09:48

Changing keywords from "beginner" to "".


---

Comment by kcrisman created at 2011-01-18 16:09:48

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2011-01-18 16:09:48

Again, a good start at this!  

Unfortunately, there are now MANY small issues that need to be cleared up before testing and positive review can occur.  I don't see any of these as insurmountable.  However, I'm definitely removing the 'beginner' tag, given that this has become a more subtle ticket.

First, there are still a fair number of typos, English issues like `every floating point evaluation of return` (which was in the original, not introduced by the author of the patch, but should be fixed), etc.   There should be better formatting (`Examples::` should be capitalized, for example), and hopefully links to the functions put in - see the plotting functions, especially plot.py, for examples of how to do that in Sphinx.

> I would caution that for annoying reasons we like to have the lines in the documentation be fairly short; see some of the other calculus or plotting files for examples of about how many characters (80? 84?) are appropriate.  (Otherwise it looks really bad in command line.)  So any updates should fix that.

This comment still applies.

Another interesting thing is the use of `*args` and `**kwds`.  Really, we expect only a few cases of args, and only one keyword.  I think the syntax for this should be like for symbolic integrals, e.g. `f.integrate(algorithm="mathematica_free")` - that is to say, maybe it should be `algorithm` instead of `alg`.  Maybe even specifically check the args?  I don't know.

The private function `_numerical_integral` needs documentation.


```
#This is so the old numerical_integral will still work
```

is not quite accurate, as it's doing more than that :)

I'm not sure whether the Mma or sympy ones actually will return numerical values.  Also, one should doctest all those options.

What is the idea with calling the other numerical integral (from Maxima) `_nintegral_sym`, since it's not symbolic?  Maybe I'm missing something.

I think you now have `Note that in exotic cases` twice in the same docstring - is that correct?

Anyway, all doable things, and the final produce will be quite valuable.  

(As a final comment, it would be worth seeing whether the issues at [this discussion](http://ask.sagemath.org/question/95/numerical-integration-in-a-function) are solved with this ticket.  I don't believe so - since these integrals aren't made symbolic - but it's worth checking.)


---

Comment by gagansekhon created at 2011-01-19 21:57:24

Replying to [comment:19 kcrisman]:
> Again, a good start at this!  
> 
> Unfortunately, there are now MANY small issues that need to be cleared up before testing and positive review can occur.  I don't see any of these as insurmountable.  However, I'm definitely removing the 'beginner' tag, given that this has become a more subtle ticket.
> 
> First, there are still a fair number of typos, English issues like `every floating point evaluation of return` . (which was in the original, not introduced by the author of the patch, but should be fixed), etc.

I have read this line several time and can't figure out what it is trying to say, perhaps someone else can tell me what it should be. 
   There should be better formatting (`Examples::` should be capitalized, for example),

Fixed

 and hopefully links to the functions put in - see the plotting functions, especially plot.py, for examples of how to do that in Sphinx.
> 
Did you want links each function listed in the file? Like a table of contents.

> > I would caution that for annoying reasons we like to have the lines in the documentation be fairly short; see some of the other calculus or plotting files for examples of about how many characters (80? 84?) are appropriate.  (Otherwise it looks really bad in command line.)  So any updates should fix that.
> 
> This comment still applies.
> 
I tried to make the lines shorter, but the html file looked wierd. Html file formats each line and wraps it around. If I make them them shorter the documentation doesn't come out right. 
> Another interesting thing is the use of `*args` and `**kwds`.  Really, we expect only a few cases of args, and only one keyword. 

Actually, there are several different sets of keywords depending on the algorithm provided. 

 I think the syntax for this should be like for symbolic integrals, e.g. `f.integrate(algorithm="mathematica_free")` - that is to say, maybe it should be `algorithm` instead of `alg`.  Maybe even specifically check the args?  I don't know.

The reason I went with alg, was that for alg="gsl", algorithm is one of the keywords already being used. 
> 
> The private function `_numerical_integral` needs documentation.
added
> 
> {{{
> #This is so the old numerical_integral will still work
> }}}
> is not quite accurate, as it's doing more than that :)
> 
> I'm not sure whether the Mma or sympy ones actually will return numerical values.  Also, one should doctest all those options.

I tested mma and you are right it gives an error, though the actual function it is calling makes it seem like it should work.

Sympy, however does return numerical values for symbolic functions with closed form. 

Added doctest for all algorithms

> 
> What is the idea with calling the other numerical integral (from Maxima) `_nintegral_sym`, since it's not symbolic?  Maybe I'm missing something.

This used to be nintegral and is imported by symbolic.integration for f.nintegral. I kept this because it has different output than numerical_integral (both old and new)

> 
> I think you now have `Note that in exotic cases` twice in the same docstring - is that correct?
> 
This was already there, I will read the documentation for that function and see if it is still needed. 

> Anyway, all doable things, and the final produce will be quite valuable.  
> 
> (As a final comment, it would be worth seeing whether the issues at [this discussion](http://ask.sagemath.org/question/95/numerical-integration-in-a-function) are solved with this ticket.  I don't believe so - since these integrals aren't made symbolic - but it's worth checking.)

This is still open, but if one uses integral instead of numerical_integral it works. Since the result until the numerical values are inputed is not numeric, but a function in x, and y , numerical_integral should perhaps not be used.


---

Attachment

Thanks for clearing up some of my misunderstandings.  I don't have time to look at this today, but hopefully within a week?  Just a couple clarifications:
>  and hopefully links to the functions put in - see the plotting functions, especially plot.py, for examples of how to do that in Sphinx.
> > 
> Did you want links each function listed in the file? Like a table of contents.

I mean like `:func:`~sage.plot.plot.plot`` referring to the function `plot`; one can do the same here, I think.
> > > I would caution that for annoying reasons we like to have the lines in the documentation be fairly short; see some of the other calculus or plotting files for examples of about how many characters (80? 84?) are appropriate.  (Otherwise it looks really bad in command line.)  So any updates should fix that.
> > 
> > This comment still applies.
> > 
> I tried to make the lines shorter, but the html file looked wierd. Html file formats each line and wraps it around. If I make them them shorter the documentation doesn't come out right. 

Hmm, that's odd.  I'll have to check it out; in most files we do this.  Maybe we've just been living with weird HTML :)


---

Comment by kcrisman created at 2011-04-18 15:25:08

See also #8321.  We continue to get support requests because of the non-unified nature of our options.


---

Comment by kcrisman created at 2011-10-12 12:21:21

It turns out that the current top-level function, `numerical_integral`, isn't even in the reference manual.  See #11916.  I don't think this is addressed here yet, though if it eventually is then that ticket would be closed as a dup.
