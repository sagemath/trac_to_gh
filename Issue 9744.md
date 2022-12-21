# Issue 9744: implicit_plot fill option fills entire plot

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-08-14 09:13:18

Assignee: jason, was

CC:  kcrisman

I was browsing the docs and noticed this example completely fills the plot black:


```
x,y = var('x,y')
f(x,y) = x^2 + y^2 - 2
implicit_plot(f, (-3, 3), (-3, 3),fill=True).show(aspect_ratio=1)
```


The docs say it should fill the region f(x)<0.


---

Attachment


---

Comment by jason created at 2010-08-14 16:43:03

Changing status from new to needs_work.


---

Comment by jason created at 2010-08-14 16:43:03

Here is a rough patch which conflicts with #9654, but gives an idea of how this issue could be resolved.


---

Comment by kcrisman created at 2011-04-20 03:02:05

Hmm, I feel like there's another ticket about this... but anyway, this is important to fix.


---

Comment by kcrisman created at 2011-06-14 05:26:49

I think it's #8529 that you meant.  Anyway, is there anything wrong with this rough patch?  I don't see what the problem might be.


---

Attachment

This is just a modification of Jason's fix to work with the current version. I had to change 'contour' to 'contours', and also remove the 'cmap' option in order for it to work (you can see what I mean by comparing the two patches). I'm pretty new to this, so I'm not sure if this is the appropriate fix or not, but it has the desired effect.


---

Comment by kcrisman created at 2011-11-22 16:42:00

Thanks for this; this would be good for [Sage Days 35.5](http://wiki.sagemath.org/days35.5/bugs).   Please change your name in the Author section to your real name, and (if you don't mind) add it to [the main Trac page](http://trac.sagemath.org/sage_trac/)!


---

Comment by kcrisman created at 2011-11-22 16:42:00

Changing status from needs_work to needs_review.


---

Comment by benjaminfjones created at 2012-01-16 20:09:13

I ran into this bug and thought I would review the patch here. The patch applies cleanly to 4.8.alpha6 (I'm still waiting for 4.8.rc0 to build). Doctests on `sage/plot/contour_plot.py` pass. More importantly, I went through all the docstring examples for `implicit_plot` by hand in the notebook to make sure they look correct, and they all do so that's great!

However, when I try the following (a modification of one of the doctests):


```
sage: def mandel(n):
...       c = polygen(CDF, 'c')
...       z = 0
...       for i in range(n):
...           z = z*z + c
...       def f(x, y):
...           val = z(CDF(x, y))
...           return val.norm() - 4
...       return f
sage: implicit_plot(mandel(1), (-3, 3), (-3, 3), fill=True)
```

I get an error:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_21.py", line 10, in <module>
    exec compile(u'open("___code___.py","w").write("# -*- coding: utf-8 -*-\\n" + _support_.preparse_worksheet_cell(base64.b64decode("aW1wbGljaXRfcGxvdChtYW5kZWwoMSksICgtMywgMyksICgtMywgMyksIGZpbGw9VHJ1ZSk="),globals())+"\\n"); execfile(os.path.abspath("___code___.py"))
  File "", line 1, in <module>
    
  File "/tmp/tmpp9xXZj/___code___.py", line 3, in <module>
    exec compile(u'implicit_plot(mandel(_sage_const_1 ), (-_sage_const_3 , _sage_const_3 ), (-_sage_const_3 , _sage_const_3 ), fill=True)
  File "", line 1, in <module>
    
  File "/home/jonesbe/sage/sage-4.8.alpha6/local/lib/python2.6/site-packages/sage/misc/decorators.py", line 534, in wrapper
    return func(*args, **options)
  File "/home/jonesbe/sage/sage-4.8.alpha6/local/lib/python2.6/site-packages/sage/plot/contour_plot.py", line 609, in implicit_plot
    return region_plot(f<0, xrange, yrange, borderwidth=linewidths, borderstyle=linestyles, **options)
  File "/home/jonesbe/sage/sage-4.8.alpha6/local/lib/python2.6/site-packages/sage/misc/decorators.py", line 534, in wrapper
    return func(*args, **options)
  File "/home/jonesbe/sage/sage-4.8.alpha6/local/lib/python2.6/site-packages/sage/plot/contour_plot.py", line 726, in region_plot
    for func in g],dtype=float)
  File "/home/jonesbe/sage/sage-4.8.alpha6/local/lib/python2.6/site-packages/sage/plot/contour_plot.py", line 783, in <lambda>
    return lambda x,y: -1 if f(x,y) else 1
TypeError: 'bool' object is not callable
```


Any idea what's going on here?


---

Comment by kcrisman created at 2012-01-27 04:56:03

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2012-01-27 04:56:03

Changing priority from major to critical.


---

Comment by kcrisman created at 2012-01-27 04:56:03

BFJ, I assume this means positive review apart from this error?

Huh, yeah, this definitely means 'needs work'.  Even though the functionality didn't work at all before, lambdas shouldn't break too many things, and this is a very natural change to make.    The problem is in `equify` (see the [very bottom of the file](http://hg.sagemath.org/sage-main/file/c239be1054e0/sage/plot/contour_plot.py#l748).


```
sage: c = polygen(CDF,'c')
sage: z = 0
sage: for i in range(1):
    z = z*z + c
....: 
sage: def g(x,y):
    val = z(CDF(x, y))
    return val.norm() - 4
....: 
sage: implicit_plot(g,(-3,3),(-3,3))  # looks fine, no surprise

sage: sage.plot.contour_plot.equify(g)  # no problem, so plotting should work with fill
<function <lambda> at 0x10df9d578>
sage: implicit_plot(g,(-3,3),(-3,3),fill=True) # error above
```

Got it.  The problem is 

```
f<0
```

in `region_plot`.   In the case I just did, 

```
sage: g<0
True
```

so we are now plotting `True` instead of `g`, which of course makes the error message quite understandable.

I tried a few things to see if I could fix it in a few minutes, but I think the "right" answer might be more complicated.

Unless we think we _should_ just fix this and put in a warning about lambdas being broken?  Seems poor form.


---

Comment by benjaminfjones created at 2012-02-06 17:56:24

Yeah, seems like we should make it work for lambda's since implicit_plot works just fine, it's only when you set `fill=True` that you get a problem. I'll take a crack at it this afternoon.


---

Comment by benjaminfjones created at 2012-02-24 01:48:34

Changing status from needs_work to needs_review.


---

Comment by benjaminfjones created at 2012-02-24 01:48:34

I uploaded [attachment:trac_9744_v2.patch] which solves the main problem by calling `region_plot(lambda x,y: f(x,y)<0, ...)` instead of `region_plot(f<0, ...)` 

...but it introduces a strange artefact. Try the following (this doesn't require applying the patch).


```
sage: region_plot(x^2+y^2-2<0, (x,-3,3), (y,-3,3))
# looks normal
sage: region_plot(lambda x,y: x^2+y^2-2<0, (x,-3,3), (y,-3,3))
# looks ragged around the edges
sage: region_plot(lambda x,y: x^2+y^2-2<0, (x,-3,3), (y,-3,3), plot_points=200)
# better, but not great
sage: region_plot(lambda x,y: x^2+y^2-2<0, (x,-3,3), (y,-3,3), plot_points=500)
# looks about like the original, but takes a long time.
```



---

Comment by benjaminfjones created at 2012-02-24 02:14:20

The following doctest that is currently in `region_plot` has the same artefact:


```
region_plot(lambda x,y: x^2+y^2<1 or x<y, (x,-2,2), (y,-2,2))
```


I uploaded a new, new patch that only has the artefact when a python function is passed
to implicit_plot in which case the user should increase the point count appropriately. I
added a doctest to that effect as well.

With the patch applied, compare:


```
sage: x,y=var('x,y')
sage: implicit_plot(x^2+y^2-2, (x,-3,3), (y,-3,3), fill=True)
sage: g = lambda x,y: x^2+y^2-2
sage: implicit_plot(g,  (x,-3,3), (y,-3,3), fill=True)
```



---

Comment by kcrisman created at 2012-02-24 15:50:56

I'm between classes now, but I'll check it out later.  In the meantime, what is going on with the new code?  When is the last line

```
return contour_plot(f, xrange, yrange, linewidths=linewidths, linestyles=linestyles, **options)
```

ever reached?

Also, 

```
if options.pop('fill'):
```

will give a `KeyError` if `'fill'` isn't defined in the options dictionary.  Could that happen?  If so, you may want to take the previous entry

```
if 'color' in options: 
```

and go from there... this may not be a problem, but it's probably wisest to guard against it.


---

Comment by benjaminfjones created at 2012-02-24 18:04:48

The `if options.pop('fill'):` is okay because of the `@`options decorator before `def implicit_plot(...):`


```
`@`options(plot_points=150, contours=(0,0), fill=False, cmap=["blue"])
```


You're correct about that last line, somehow I let that slip through. I updated the patch. I think it's more readable and less redundant now.


---

Comment by kcrisman created at 2012-02-24 20:06:59

> The `if options.pop('fill'):` is okay because of the `@`options decorator before `def implicit_plot(...):`

I figured, but was too rushed to check.


```
x,y = var('x,y')
f(x,y) = x^2 + y^2 - 2
implicit_plot(f, (-3, 3), (-3, 3),fill=True).show(aspect_ratio=1)
```

It works!

Let me just look at a few more things.  I think I'll want to add something to the other example you give, with the region plot lambda, so that it looks nicer in the doc.

----

I was going to complain about `artefact` but then read [this](http://www.worldwidewords.org/qa/qa-art1.htm).  Harrumph.


---

Comment by benjaminfjones created at 2012-02-24 20:15:03

That sounds good. Go ahead and change artefact if you want. I'll admit I'm of the generation whose spelling abilities were destroyed by the spell checker. 

I was thinking about opening a new ticket to improve results of region_plot when passing a lambda function, but I don't know enough about why the "artefacts" occur. Any thoughts?


---

Comment by kcrisman created at 2012-02-24 21:23:39

No, I don't know - I haven't plotted too many lambda functions recently, of course.

I'm going to fix a few other doc things.  One that looks like a change, but isn't, is removing the variable declaration - but this is not needed with `f(x,y)` notation.


---

Comment by benjaminfjones created at 2012-02-24 21:30:55

Reviewer patch looks good to me. Thanks.


---

Comment by kcrisman created at 2012-02-24 21:39:29

Wow, I wasn't even done reviewing my own reviewer patch :)   I got hung up on trying to decide whether to add any more `# long time`s, but decided it wasn't worth it.

The code currently allows this.  

```
sage: f(x,y) = x^2 + y^2 - 2
sage: implicit_plot(f, (-3, 3), (-3, 3),fill='55').show(aspect_ratio=1)  # nice graph is filled
```

Should we maybe raise an error if this happens?  Given that one can ask for all kinds of fills in regular plots, not just `True` or `False`, perhaps this should be disallowed.


---

Comment by kcrisman created at 2012-02-24 21:40:18

Also, it's okay to be a reviewer and an author - you definitely have done both here!


---

Comment by benjaminfjones created at 2012-02-24 22:25:11

I updated my patch to make the code more readable at the end of `implicit_plot` and to raise an error if fill option is passed and does not equal either `True` or `False`.

The reviewer patch still applies on top (with a tiny bit of fuzz).


---

Comment by kcrisman created at 2012-02-24 23:33:55

I think you might want to do 

```
if foo is True
```

not

```
if foo == True
```

for reasons that escape me right now.


---

Comment by jason created at 2012-02-24 23:45:00

'is' does a pointer comparison, which is much faster and works because True is a singleton.  == does a __eq__ comparison, which is much slower.  When comparing to True, False, or None, you should use 'is' to be much faster.


---

Comment by benjaminfjones created at 2012-02-25 02:28:32

fixes filled implicit plotting with lambdas


---

Attachment

Ah, good point. The new patch should do the job.


---

Comment by kcrisman created at 2012-02-25 04:07:22

I can't think of any other reasons to hold this up.  I've uploaded a new reviewer patch testing the error raised.  I tested the looks of the implicit plots in schemes and rings, even.  I think we're done here.


---

Comment by kcrisman created at 2012-02-25 04:07:37

reviewer patch


---

Comment by kcrisman created at 2012-02-25 04:09:23

Changing status from needs_review to positive_review.


---

Attachment


---

Comment by jdemeyer created at 2012-02-27 11:19:59

Resolution: fixed
