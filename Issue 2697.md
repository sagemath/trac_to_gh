# Issue 2697: stupid bug in integrate (easy to fix)

Issue created by migration from https://trac.sagemath.org/ticket/2697

Original creator: was

Original creation time: 2008-03-28 07:39:54

Assignee: was

CC:  robertwb

This is right:


```
sage: integrate(x, x,-1,1)
0
```


This error message (which is because I forgot to give the variable of integration) is
completely broken. The "raise err" line in the source code should be just "raise", i.e., delete err, which makes no sense. Or?  Anyway, this is just wrong as is.

```
sage: integrate(x, -1,1)
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/build/sage-2.10.4/local/lib/python2.5/site-packages/sage/calculus/functional.py in integral(f, *args, **kwds)
    255         return f.integral(*args, **kwds)
    256     except ValueError, err:
--> 257         raise err
    258     except AttributeError:
    259         pass

<type 'exceptions.ValueError'>: variable name is not a valid Python identifier

```



---

Comment by mabshoff created at 2008-04-09 02:11:28

I am not sure that the suggested fix does solve the problem:

```
sage: integrate(x, -1,1)
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/scratch/mabshoff/release-cycle/sage-3.0.alpha3/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/calculus/functional.py in integral(f, *args, **kwds)
    253     """
    254     try:
--> 255         return f.integral(*args, **kwds)
    256     except ValueError, err:
    257         raise

/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/calculus/calculus.py in integral(self, v, a, b)
   2475
   2476         if not isinstance(v, SymbolicVariable):
-> 2477             v = var(repr(v))
   2478             #raise TypeError, 'must integrate with respect to a variable'
   2479         if (a is None and (not b is None)) or (b is None and (not a is None)):

/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/calculus/calculus.py in var(s, create)
   5238             raise ValueError, "the variable '%s' has not been defined"%var
   5239         pass
-> 5240     v = SymbolicVariable(s)
   5241     _vars[s] = v
   5242     _syms[s] = v

/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/calculus/calculus.py in __init__(self, name)
   5072             raise ValueError, "variable name must be nonempty"
   5073         elif not is_python_identifier.match(name):
-> 5074             raise ValueError, "variable name is not a valid Python identifier"
   5075
   5076     def __hash__(self):

<type 'exceptions.ValueError'>: variable name is not a valid Python identifier
sage:
```


Thoughts?

Cheers,

Michael


---

Comment by kcrisman created at 2008-10-17 02:55:07

Apply this patch to 3.1.4 to integrate without variables (sometimes)


---

Comment by kcrisman created at 2008-10-17 03:02:38

Changing type from defect to enhancement.


---

Attachment

These should now work:


```
sage: integrate(x, -1,1)
0
sage: integrate(sin(x),0,pi)
2
```


Sadly, because I don't know enough about Maxima to get it to accept the default variable, we still get this joke one might make in freshman calculus:


```
sage: integrate(sin,0,pi) 
pi*sin 
```



---

Comment by robertwb created at 2008-10-30 21:31:47

I'm getting


```
sage: integrate(sin(x), pi, 2*pi)
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/calculus/functional.py", line 254, in integral
    return f.integral(*args, **kwds)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 2586, in integral
    raise TypeError, 'only one endpoint given'
TypeError: only one endpoint given
```


Rather than catching the error that, say, 0 is not a valid variable name, perhaps one should look at the number of variables passed to determine how to integrate. E.g. 


```
sage: integrate(sin(x))               # 0 args, implicit indefinite
cos(x)
sage: integrate(sin(x), y)            # 1 arg, explicit indefinite
sin(x)*y
sage: integrate(sin(x), pi, 2*pi)     # 2 args, implicit definite
-2
sage: integrate(sin(x), y, pi, 2*pi)  # 3 args, explicit definite
pi*sin(x)
```



---

Comment by kcrisman created at 2008-11-01 03:19:53

Changing assignee from was to kcrisman.


---

Comment by kcrisman created at 2008-11-01 03:19:53

Replying to [comment:3 robertwb]:

Posting (final? I hope) version of patch, based on 3.2.alpha0.  Passed doctests for calculus.py once, all other times it timed out for me, but I do not believe it changes pre-existing correct behavior.

> I'm getting
> 
> {{{
> sage: integrate(sin(x), pi, 2*pi)
> ------------------------------------------------------------
> Traceback (most recent call last):
>   File "<ipython console>", line 1, in <module>
>   File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/calculus/functional.py", line 254, in integral
>     return f.integral(*args, **kwds)
>   File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 2586, in integral
>     raise TypeError, 'only one endpoint given'
> TypeError: only one endpoint given
> }}}
> 

Turns out that this actually comes from the original code, where the second item was turned into a variable in case someone used some already-in-use identifier for the variable; the problem was that it turned things like e and pi into variables.  

> Rather than catching the error that, say, 0 is not a valid variable name, perhaps one should look at the number of variables passed to determine how to integrate. E.g. 
> 
> {{{
> sage: integrate(sin(x))               # 0 args, implicit indefinite
> cos(x)
> sage: integrate(sin(x), y)            # 1 arg, explicit indefinite
> sin(x)*y
> sage: integrate(sin(x), pi, 2*pi)     # 2 args, implicit definite
> -2
> sage: integrate(sin(x), y, pi, 2*pi)  # 3 args, explicit definite
> pi*sin(x)
> }}}

Good idea!  In the end, though, it was easier for me to just jury-rig the code as is.  When I make my own functions I try to do that sort of planning, but I don't feel confident enough (or have enough time) to completely change the way this type of code works.  Hopefully my final solution is still pretty good, though; it does all of the above, except you will have to declare y beforehand (I couldn't find a way around that), and the first integral is -cos(x) :)

As a bonus, I was finally able to figure out how to do this, which now works:

```
sage: integrate(sin,0,pi)
2
```

That alone is worth it for me.


---

Attachment

Based on 3.2.alpha0


---

Comment by robertwb created at 2008-11-01 03:40:20

Hmm... now I get


```
sage: var('x,a,b')
(x, a, b)
sage: integral(x^2, a, b)
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/misc/functional.py", line 418, in integral
    return x.integral(*args, **kwds)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 2594, in integral
    raise TypeError, 'only one endpoint given'
TypeError: only one endpoint given
```


where I'd expect `(b^3 - a^3)/3`.


---

Comment by kcrisman created at 2008-11-04 02:43:27

Okay, fair enough.  My philosophy was to improve what was there - all the examples you gave were errors before, too - but I agree that having a very robust function is the best goal long term.  However, it may take a little longer to get there.  Thanks for the careful reading of the code to find these (so far) non-examples; if we can get all of them it will make integrate very intuitive indeed.


---

Comment by robertwb created at 2008-12-20 02:52:59

I've attached a new patch that resolves this issue. It should be more robust, as it figures out to do first rather than catching errors.


---

Attachment

I don't have a chance to review this yet (tomorrow?) but at least want to point out that the other day I noticed that the functionality did also not work for CallableSymbolicExpression (e.g. lines 5779 or so the integral() method), which seems to have an even more primitive version of the same code.  E.g., to try the original example for this ticket:

```
sage: f(x)=x
sage: f
x |--> x
sage: type(f)
<class 'sage.calculus.calculus.CallableSymbolicExpression'>
sage: integrate(f,-1,1)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<snip>
sage: f.integral(-1,1)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<snip>
```

But this does work, so I think one would really have to fix the CallableSymbolicVariable piece:

```
sage: f.integral(x,-1,1)
0
sage: integral(f,x,-1,1)
0
```

Thanks for working on this - I knew it would be impossible for me to get to it until after the semester, and that proved to be true.


---

Comment by robertwb created at 2008-12-23 18:49:46

Thanks for starting to look at this. I think integrating symbolic equations should be a separate ticket.


---

Comment by kcrisman created at 2008-12-27 04:36:06

Okay, I like your patch.  I do think that there should be support for 

```
sage: f(x)=x
sage: integrate(f,-1,1)
0
```

I wasn't suggesting integrating a symbolic equation, just that the same behavior results for 

```
sage: integrate(f,-1,1)
0
sage: integrate(x,-1,1)
0
```

because I don't think most newbie Sage users will get the difference between f(x)=x and f=x, for instance.
Anyway, the latest patch applies the appropriate parts of your patch to CallableSymbolicExpression as well; there needs to be less checking because of the different return expected, e.g. indefinite integral is already handled by the previous code (still returning a CallableSymbolicExpression, though).

Unfortunately, calculus.py always times out for me when I test it.  I tried to check that I did not change any existing behavior but hopefully you (or someone else) can check this.

Otherwise positive review!


---

Comment by kcrisman created at 2009-01-15 02:25:20

Changing summary - would be good to get this in before bitrot sets in, but wanted robertwb's final followup review on my last tiny change, or to reject that but to open a new ticket for the other thing.  Or whoever else is interested in this ticket could do that; since I made a change I don't feel comfortable doing the last positive review.


---

Comment by mabshoff created at 2009-01-15 02:29:32

Yes, this would be very nice to get into 3.3, so Robert if you can spare the time please deal with this.

Cheers,

Michael


---

Comment by robertwb created at 2009-01-15 03:28:05

Sorry this got lost in the shuffle--yes, I approve of this patch.


---

Comment by mabshoff created at 2009-01-15 12:11:43

Replying to [comment:14 robertwb]:
> Sorry this got lost in the shuffle--yes, I approve of this patch. 

And I approve of your approval and change this formally to a positive review :)

I assume I should only apply trac_2697.patch and authorship as well as review credit is shared between Robert and Karl-Dieter?

Cheers,

Michael


---

Comment by kcrisman created at 2009-01-15 15:50:02

Replying to [comment:15 mabshoff]:
> And I approve of your approval and change this formally to a positive review :)
> 
> I assume I should only apply trac_2697.patch and authorship as well as review credit is shared between Robert and Karl-Dieter?

I think that's right.  It will be good to have this available.


---

Comment by robertwb created at 2009-01-15 19:50:01

Re authorship, yep, that's right.


---

Comment by mabshoff created at 2009-01-18 17:52:26

trac_2697.patch causes a doctest failure:

```
sage -t -long devel/sage/sage/functions/piecewise.py
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha0/devel/sage-main/sage/functions/piecewise.py", line 600:
    sage: f.integral()
Expected:
    1/2
Got:
    2 - x
**********************************************************************
```


Cheers,

Michael


---

Comment by kcrisman created at 2009-01-20 02:12:00

Replying to [comment:18 mabshoff]:
> trac_2697.patch causes a doctest failure:

Ok, this is on the CallableSymbolicExpression side so it's my fault; looks like it is adding 1+(1-x) for some reason, which I think I should be able to track down.  I am downloading 3.3.alpha0 currently, it should build overnight, and then hopefully sometime tomorrow I can fix this.


---

Comment by kcrisman created at 2009-01-20 02:33:33

Replying to [comment:19 kcrisman]:
> Replying to [comment:18 mabshoff]:
> > trac_2697.patch causes a doctest failure:
> 

For reference (mainly to myself not to forget in morning) - fix is to replace lines 5806 to 5812

```
	        elif b is None and a is not None: 
	            # two arguments, must be endpoints 
	            a, b = x, a 
	            x = self.default_variable() 
	 
	        if not isinstance(x, SymbolicVariable): 
	            x = var(repr(x)) 
```

with

```
	        elif b is None and a is not None: 
	            # two arguments, must be endpoints 
	            a, b = x, a 
	            x = None

                if x is None:
                    x = self.default_variable()

	        elif not isinstance(x, SymbolicVariable): 
	            x = var(repr(x)) 
```

as robertwb did in the first part of this. Never occurred to me someone might actually _intentionally_ pass None for the variable...

Also need to add a doctest, and perhaps a comment that Maxima interprets variable=None as intending for integration to be "d1" or something like that, while Sage usually looks for whatever variable makes sense. E.g. the surprising last line below:

```
sage: j(x)=x^2
sage: integral(j,None,0,1)
1/3
sage: j._maxima_().integrate(None,0,1)
x^2
sage: j._maxima_().integrate(None,0,2)
2*x^2
```

Does anyone know if that is a feature or a bug in Maxima?  Either seems plausible, though I would think maybe feature.


---

Comment by kcrisman created at 2009-01-21 03:48:21

Based on 3.3.alpha0


---

Attachment

This patch (trac_2697.patch) should take care of the piecewise error and still do the new things, plus adds a little documentation for things like f(x)=x^2.  My calculus.py always times out in testing, but hopefully running that test and the piecewise.py test should lead to a final positive review.


---

Comment by rlm created at 2009-01-24 15:20:05

I'm going to go ahead and give this a positive review. I applied the patch, everything passes doctests, and the code looks reasonable. Robert and Karl should still get review credit, though, since they did much more work than me.


---

Comment by mabshoff created at 2009-01-24 18:41:51

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 18:41:51

Merged trac_2697.patch in Sage 3.3.alpha2
