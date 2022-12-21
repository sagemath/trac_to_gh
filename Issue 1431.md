# Issue 1431: basic plotting: add support for setting the location and labels of all tick marks on the x and y axes

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-09 02:49:00

Assignee: was

Amazingly some very basic functionality for plotting hasn't yet been implemented!  In particular, there is nothing yet for setting the location and labels of all tick marks on the x and y axes.  This need to be implemented.


---

Comment by was created at 2007-12-09 02:49:08

Changing component from algebraic geometry to graphics.


---

Comment by kcrisman created at 2009-09-15 17:28:23

This should be available now with #5448, but this ticket would now be to expose that functionality from matplotlib.


---

Comment by jason created at 2009-11-12 00:17:34

Changing status from new to needs_work.


---

Attachment

Still needs doctest examples.

Example:


```

def multiple_of_pi(n,pos):
    m = n*1.0/float(pi)
    c=[i for i in convergents(m) if i.denominator()<12]
    q=c[-1]
    if q.denominator()==1:
        if q.numerator()==1:
            return r'$\pi$'
        elif q.numerator()==-1:
            return r'$-\pi$'            
        else:
            return r'$%s\pi$'%q
    else:
        if q.numerator()==1:
            return r'$\frac{\pi}{%s}$'%q.denominator()
        elif q.numerator()==-1:
            return r'$\frac{-\pi}{%s}$'%q.denominator()
        else:
            return r'$\frac{%s\pi}{%s}$'%(q.numerator(),q.denominator())

from matplotlib.ticker import MultipleLocator, FuncFormatter
plot(sin(x), (x, -4, 4), tick_locator=MultipleLocator(float(pi/3)), tick_formatter=FuncFormatter(multiple_of_pi))

```



---

Comment by kcrisman created at 2009-11-12 03:25:47

This looks like a great start.  Now we need a wrapper to make creating the formatters and locators easy for the average user.  I will try to help with that, and documentation, as I get a chance.  Thanks!


---

Comment by jason created at 2009-11-12 03:36:05

Personally, I think creating formatters and locators *is* easy.  Notice what I did to create the locator: `MultipleLocator(float(pi/3))`.  The formatter is slightly harder because it's a harder problem I was trying to solve---given a floating point number, find a nice multiple of pi expression for a label.  In general, though, it's easy to just give a list of tick values and strings.

What did you have in mind for an easier wrapper?


---

Comment by jason created at 2009-11-12 03:45:10

A simpler example:


```
def multiple_of_pi(n,pos):
    m = n*1.0/float(pi)
    c=[i for i in convergents(m) if i.denominator()<12]
    q=c[-1]
    return '$%s$'%latex(q*pi)

from matplotlib.ticker import MultipleLocator, FuncFormatter
plot(sin(x), (x, -4, 4), tick_locator=MultipleLocator(float(pi/4)), tick_formatter=FuncFormatter(multiple_of_pi))

```



---

Comment by jason created at 2009-11-12 04:13:32

See #4529 for a related ticket---logarithmic scales.


---

Comment by jason created at 2009-11-12 04:14:32

One last one that is even simpler:


```
def multiple_of_pi(n,pos):
    c=[i for i in convergents(n/pi) if i.denominator()<=12]
    return '$%s$'%latex(c[-1]*pi)

from matplotlib.ticker import MultipleLocator, FuncFormatter
plot(sin(x), (x, -10, 10), tick_locator=MultipleLocator(float(pi/2)), tick_formatter=FuncFormatter(multiple_of_pi),figsize=[10,4])
```



---

Comment by kcrisman created at 2009-11-12 15:38:16

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2009-11-12 15:38:16

This is what I meant:


```
sage: plot(sin(x), (x,0,2*pi), tick_locator=pi/3, tick_formatter='pi')
sage: plot(1.5/(1+e^(-x)), (x,-10,10), tick_locator=[None, 1.5/4]) # shows the inflection point height!
```


See soon-to-be-attached patch.  Thanks SO much for making this possible - my additions just make it easier for people like me who don't know matplotlib :)

Also, positive review to the parts I didn't do.


---

Comment by kcrisman created at 2009-11-12 15:43:53

Perhaps a followup is what sort of object is a Locator?  Just a list?  I couldn't find this in the built-in documentation for ticker (and wasn't online when I created it).  If so, then the documentation should be updated to reflect that; I still think this having the option of just a number is a good one, though I was cludgy in dealing with some of the Errors that might arise.


---

Comment by kcrisman created at 2009-11-12 15:45:58

Based on 4.2


---

Attachment

Two comments:

* tick_formatter should accept rational multiples of *any* symbolic constant.  I think the code ought to be generalized before going into Sage.  For example, I should have ticks that are rational multiples of e as well.

* I like the idea of having tick_locator be a number.  I think it should be expanded to being a list (if symbolic expressions, then latexing them can give the formatters), or a function.

See http://reference.wolfram.com/mathematica/ref/Ticks.html for the equivalent mathematica feature.


---

Comment by jason created at 2009-11-12 17:46:23

Changing status from needs_review to needs_work.


---

Comment by jason created at 2009-11-12 17:46:48

I'm putting this as needs_work while we flush out a nice design.


---

Comment by kcrisman created at 2009-11-12 18:03:08

Replying to [comment:12 jason]:
> Two comments:
> 
> * tick_formatter should accept rational multiples of *any* symbolic constant.  I think the code ought to be generalized before going into Sage.  For example, I should have ticks that are rational multiples of e as well.
> 
> * I like the idea of having tick_locator be a number.  I think it should be expanded to being a list (if symbolic expressions, then latexing them can give the formatters), or a function.

These make lots of sense.  It should be easy to check if the string is in symbolic.constants or something (or even accept those as input), and then of course one would have to check if there was a symbolic expression in the list, and (possibly override) use tick_formatter appropriately.  After all, multiple_of_pi could be made generic to multiple_of_symbolic_constant, and then we could make a dummy function to input into FuncFormatter or something.


---

Comment by kcrisman created at 2010-04-20 17:41:34

Okay, I've finally had time to return to this, and I'm almost done dealing with this.  It is actually really cool!

Formatting by multiples of constants (or numbers) will be implemented, as well as locating by arbitrary lists.  Note that 

```
    ``LogLocator``
       logarithmically ticks from min to max
```

could solve our log problems, though I think that would not belong on this ticket (and I think there is one for this).


---

Attachment

Based on 4.3.5, apply only this patch to Sage library


---

Comment by kcrisman created at 2010-04-20 19:42:26

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-04-20 20:29:52

Changing assignee from was to jason.


---

Comment by jason created at 2010-04-20 20:29:52

1. "Private" functions (like the first one) should begin with an underscore
 1. plot(2*x+1,(x,0,5),tick_locator=[[0,1,e,pi,sqrt(20)],2],tick_formatter="latex") looks really bad since the minor ticks do not pay attention to the major ticks
 1. in general, it looks really weird to have very small latex numbers on one axis while having large non-latex numbers on the other axis.  I'm not sure what we can do about this.


---

Comment by jason created at 2010-04-20 20:29:59

Changing status from needs_review to needs_work.


---

Comment by jason created at 2010-04-20 20:30:23

Changing assignee from jason to kcrisman.


---

Comment by kcrisman created at 2010-04-20 20:42:00

Replying to [comment:18 jason]:
>  1. "Private" functions (like the first one) should begin with an underscore
You mean the multiple one?  Ok.
>  1. plot(2*x+1,(x,0,5),tick_locator=[[0,1,e,pi,sqrt(20)],2],tick_formatter="latex") looks really bad since the minor ticks do not pay attention to the major ticks
I totally agree, but I figured it was best to respond to your suggestion first, and then take ideas for how to fix this issue.  Any ideas?
>  1. in general, it looks really weird to have very small latex numbers on one axis while having large non-latex numbers on the other axis.  I'm not sure what we can do about this.
I see.  I don't think this is a problem - we can just make it so that "latex" is applied to both axes, if used.  What do you think?


---

Comment by kcrisman created at 2010-04-21 03:20:42

Okay, I've fixed all of these things.  Note that Mma only includes major ticks for lists of ticks, so I just went with that (much easier!).  The latex thing was annoying - there was a bug in sage.misc.latex.str_function:

```
sage: sage.misc.latex.str_function('4')
'4'
sage: sage.misc.latex.str_function('4.0')
'\\texttt{4.0}'
```

At least I view this as a bug, and in any case it prevents the latexing from working properly even if the tick_locator had [0,1.0,e] rather than [0,1,e].  Unified patch coming up.


---

Comment by kcrisman created at 2010-04-21 03:27:48

Apply only ticks, formatting, and latex patch.


---

Comment by kcrisman created at 2010-04-21 03:27:48

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-04-21 03:40:29

Changing status from needs_review to needs_work.


---

Comment by jason created at 2010-04-21 03:40:29

Very nice now!  One last thing that I saw: the examples for _multiple_... still have the problem of halfof the ticks being in latex and the other half not.  For example, plot(x!^2, (x, -2, 2), tick_formatter=pi) has the vertical labels in the standard font and the horizontal labels in tex.


---

Comment by kcrisman created at 2010-04-21 12:52:27

Replying to [comment:24 jason]:
> Very nice now!  One last thing that I saw: the examples for _multiple_... still have the problem of halfof the ticks being in latex and the other half not.  For example, plot(x!^2, (x, -2, 2), tick_formatter=pi) has the vertical labels in the standard font and the horizontal labels in tex.

Hmm, that's true.  I don't know - this is more of a design decision than anything.  In theory, we could latex ALL our tick labels, but that seems overkill.  On the other hand, the solution to this would be kind of cludgy.

Also, I was thinking about it this morning and wondered whether it would make sense to have the "tick_locator" keyword be just "ticks" or "tick" instead.  Mma using "ticks", and "tick_locator" is a little longish ("tick_formatter" makes sense, though).

Let me know if you have any ideas.


---

Comment by was created at 2010-05-18 05:28:46

Thanks for all the work on this ticket.  I'm helping my wife with a final project for an environmental science class (involving measuring "smog"), and not having tick control is devastating.   Finally, for the first time, I personally really need this capability :-)

Another killer is not have a legend.  Is that also easy to add via something similar?  (Probably.)


---

Comment by jason created at 2010-05-18 05:31:36

Replying to [comment:26 was]:

> Another killer is not have a legend.  Is that also easy to add via something similar?  (Probably.)

See #4342


---

Comment by jason created at 2010-05-18 05:33:25

Of course, you can also always use straight matplotlib to do these things right now.


---

Comment by was created at 2010-05-18 05:53:30

And it turned out that this patch 100% totally worked to solve my problem.  Yes!  

  http://tutorial.sagenb.org/home/pub/19/

Of course, it will be nice when the capabilities are doctested. 

Regarding using "straight matplotlib", that would be a bit annoying, since all my plot commands are in Sage, so I have to get at the secret underlying matplotlib fig/canvas, right?  Or rewrite all my code to use pylab directly.   I don't want to do that "on principle".


---

Comment by jason created at 2010-05-18 06:48:19

Replying to [comment:29 was]:

> Regarding using "straight matplotlib", that would be a bit annoying, since all my plot commands are in Sage, so I have to get at the secret underlying matplotlib fig/canvas, right?  

Well, it's not so secret, though, as it is exposed in a public function:

p=plot(x^2,(x,-3,4))
figure=p.matplotlib()
from matplotlib.backends.backend_agg import FigureCanvasAgg
figure.set_canvas(FigureCanvasAgg(figure))
figure.savefig('test.png')

(the last three lines are a bit esoteric, but they are fairly straightforward matplotlib...)


---

Comment by kcrisman created at 2010-05-18 16:28:18

Replying to [comment:29 was]:
> And it turned out that this patch 100% totally worked to solve my problem.  Yes!  
> 
>   http://tutorial.sagenb.org/home/pub/19/

Sweet!  Looks great.

> 
> Of course, it will be nice when the capabilities are doctested. 

Okay, that and figuring out what to do with the Latex situation are all this ticket needs, then.  I can't work on this until after the first PREP workshop, but after that it's very high on my list.


---

Comment by jason created at 2010-05-25 15:33:09

From private email, in response to kcrisman's comment above:

>
>
> Hmm, that's true. I don't know - this is more of a design decision
> than anything. In theory, we could latex ALL our tick labels, but that
> seems overkill. On the other hand, the solution to this would be kind
> of cludgy.
>
> Also, I was thinking about it this morning and wondered whether it
> would make sense to have the "tick_locator" keyword be just "ticks" or
> "tick" instead. Mma using "ticks", and "tick_locator" is a little
> longish ("tick_formatter" makes sense, though).
>
> Let me know if you have any ideas.

+1 to "ticks"

I'm not sure what to do about the latex issue.  I suppose the real problem here is that matplotlib does not use compatible fonts for $1$ and just straight 1.  That's a bummer.  Still, in the common case (i.e., people didn't specify formatters), I think we should make it all latex or all not latex.  plot(sin(x), (x,0,pi), tick_formatter=pi) is likely to be a very common case, and we shouldn't have "ugly" output for it.  It looks like it might be as easy as changing the line:


```
 1818            if y_formatter is None:  
1819                y_formatter = OldScalarFormatter()
```

to

```
if y_formatter is None:
    y_formatter = copy(x_formatter)  # maybe copy isn't needed
```

We could then also delete the if statement above dealing with setting both formatters to "latex" if tick_formatter="latex".

The one problem with this is that plot(..., ticks=pi) would change both the x and the y axis.  Maybe we could special-case that situation.


---

Comment by kcrisman created at 2010-05-25 18:17:47

> > Also, I was thinking about it this morning and wondered whether it
> > would make sense to have the "tick_locator" keyword be just "ticks" or
> > "tick" instead. Mma using "ticks", and "tick_locator" is a little
> > longish ("tick_formatter" makes sense, though).
> >
> +1 to "ticks"

Ok, done.

> I'm not sure what to do about the latex issue.  I suppose the real problem here is that matplotlib does not use compatible fonts for $1$ and just straight 1.  That's a bummer.  Still, in the common case (i.e., people didn't specify formatters), I think we should make it all latex or all not latex.  plot(sin(x), (x,0,pi), tick_formatter=pi) is likely to be a very common case, and we shouldn't have "ugly" output for it.  It looks like it might be as easy as changing the line:
> 
> {{{
>  1818            if y_formatter is None:  
> 1819                y_formatter = OldScalarFormatter()
> }}}
> to
> {{{
> if y_formatter is None:
>     y_formatter = copy(x_formatter)  # maybe copy isn't needed
> }}}
> We could then also delete the if statement above dealing with setting both formatters to "latex" if tick_formatter="latex".
> 
> The one problem with this is that plot(..., ticks=pi) would change both the x and the y axis.  Maybe we could special-case that situation.

If you note, the documentation is already quite explicit that you should not do that example in 'real life' :-)  though I'll make it even more explicit.  Luckily that example is also in an underscore function.

I think a better solution is that if y_formatter is None and x_formatter was in SR, then we should do y_formatter='latex'.  I propose to do this via 

```
        from sage.symbolic.ring import SR
        if not isinstance(tick_formatter, (list, tuple)):
            if tick_formatter == "latex" or tick_formatter in SR:
                tick_formatter = (tick_formatter, "latex")
            else:
                tick_formatter = (tick_formatter, None)        
```

I also will check for the much rarer case of plotting arcsin, so to speak.  Patch coming up.


---

Comment by kcrisman created at 2010-05-25 18:46:09

Based on 4.3.5, apply only this patch to Sage library


---

Attachment

Needs review.  Notice that for some reason it kept the old message - but this latest one is based on 4.4.2, no worries :-)


---

Comment by kcrisman created at 2010-05-25 18:46:48

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-09-03 22:06:49

Looks great, applies to 4.5.2, and doctests pass in changed files.  Great job!


---

Comment by jason created at 2010-09-03 22:06:49

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-15 10:40:29

Resolution: fixed
