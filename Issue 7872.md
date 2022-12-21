# Issue 7872: Adding coordinate transformations to plot3d

Issue created by migration from Trac.

Original creator: olazo

Original creation time: 2010-01-08 17:44:47

Assignee: olazo

CC:  wcauchois jason mhampton olazo kcrisman

While developing a command called transform_plot3d, that generalized ploting in diferent coordinate systems, Jason Grout suggested to me that such a command would be better implemented within plot3d.

I agreed to that, so I propose an adition to plot3d's syntax: "plot3d(function,var1range,var2range,transformation=None,**kwds)" where transformation is a 4-tuple containing 3 functions of arity 3, and a variable which is to be interpreted as the function to be ploted. Like this (r*cos(fi),r*sin(fi),z,r), so the function will be ploted as r.

It's inclution within plot3d would be something on the likes of


```
def plot3d_new(f,v1ran,v2ran,transformation=None,**kwds):
    if transformation==None:
        return plot3d(f,v1ran,v2ran,**kwds)
    else:
        v1=v1ran[0]
        v2=v2ran[0]

        if transformation=='spherical':
            r=var('r')
            transformation=(r*cos(v1)*sin(v2),r*sin(v1)*sin(v2),r*cos(v2),r)
        elif transformation=='cylindrical':
            r=var('r')
            transformation=(r*cos(v1),r*sin(v1),v2,r)
        elif str(type(transformation))=="<type 'str'>":
            print 'Warning: the transformation given is not amongst the options, it will be ignored'
            return plot3d(f,v1ran,v2ran,**kwds)

        fvar=transformation[3]
        transformation=(transformation[0],transformation[1],transformation[2])

        try:
            R=[t.subs({fvar:f}) for t in transformation]
        except:
            def subs_func(t):
                return lambda x,y: t.subs({fvar:f(x,y), v1:x, v2:y})
            R=map(subs_func,transformation)
        return parametric_plot(R,v1ran,v2ran,**kwds)
```


Examples can be found in [http://www.sagenb.org/home/omologos/9/](http://www.sagenb.org/home/omologos/9/).

Spherical and cylindrical plots are now meant to be purely derived from plot3d. So tickets [http://trac.sagemath.org/sage_trac/ticket/7850](http://trac.sagemath.org/sage_trac/ticket/7850) and [http://trac.sagemath.org/sage_trac/ticket/7869](http://trac.sagemath.org/sage_trac/ticket/7869) should be updated


---

Comment by olazo created at 2010-01-08 17:53:52

Changing status from new to needs_work.


---

Comment by wcauchois created at 2010-01-11 07:21:30

Hi! William directed me to your thread on sage-devel. Since I have experience working on 3D plotting, I think I could help integrate this code into Sage.


---

Comment by wcauchois created at 2010-01-12 05:29:53

based on sage 4.3.1.alpha1


---

Attachment

The patch I just attached represents my initial work on this issue. I added Oscar's code to plot3d() to implement the transformation keyword parameter, and I added the two new plotting functions spherical_plot3d and cylindrical_plot3d.

I made some minor changes to the original code. I moved the formulae for the transformations for spherical and cylindrical coordinates out of the body of plot3d, and into the bodies of spherical_plot3d and cylindrical_plot3d, since I thought that was a better place for them. I also added some error handling; the urange and vrange given to plot3d may be 2-tuples, in which case the variables are implicit -- but we expect urange[0] and vrange[0] to be the plot variables.

We need to add some documentation for the new features. I think I can draw upon the examples Oscar provided in his published worksheets to create doctests for the new functions. Oscar, could you help me come up with descriptions of cylindrical_plot3d and spherical_plot3d for use in their docstrings? And more examples are always helpful.


---

Comment by olazo created at 2010-01-12 16:16:00

More examples now available at the bottom of: [http://sagenb.org/home/pub/1328/](http://sagenb.org/home/pub/1328/). I'll do the descriptions later.


---

Comment by olazo created at 2010-01-13 01:15:16

I have attatced a proposal for a docstring in spherical_plot #7850 . Also, I checked your code. Do you think it is best to use "spherical_plot3d" instead of "spherical_plot"? I find the 3d redundant, and I like to type less. Also, I noticed that your implementation will not allow adaptative refinement to be used together with "transformation". I have never used that option and I don't know whether it is important. When my plots are not sufficiently rounded I use plot_points, and that usually does the trick.


---

Attachment


---

Comment by olazo created at 2010-01-24 19:42:15

I've just added a patch with some improvements as well as the docstrings. However, the docstrings of spherical_plot3d and cylindrical_plot3d are impropperly formated. I could not manage format them right. Please review!


---

Comment by olazo created at 2010-01-24 19:42:15

Changing status from needs_work to needs_review.


---

Comment by wcauchois created at 2010-01-25 02:03:28

Changing status from needs_review to needs_work.


---

Comment by wcauchois created at 2010-01-25 02:03:28

I will be uploading a patch very soon with some improvements to Oscar's code.


---

Attachment

based on sage 4.3.1.rc0


---

Comment by wcauchois created at 2010-01-26 07:54:44

So here is what I've been working on: a very unambiguous system for specifying predefined transformations, that will work with symbolic expressions and Python callables alike.

It has turned out to be a lot of work.

Jason, could you take a look and tell me what you think of the code and the documentation I've added?


---

Comment by jason created at 2010-01-26 08:06:23

I like how you incorporated olazo's work and your work.  Hooray for collaborative development.

In the first reading through, it looks great to me.  olazo: what do you think?


---

Comment by olazo created at 2010-01-28 05:43:31

It seems fantastic to me! Many thanks to both of you!


---

Comment by olazo created at 2010-02-01 02:28:13

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-02-05 19:08:16

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2010-02-05 19:08:16

I haven't been able to do a thorough review yet, but in general I agree that this looks very nice!  Everything below should be interpreted as nitpicking; however, because of the last item (doctests) I must put this as 'needs work'.

In spherical_plot3d, it is a 'drop' of water, not a 'drom'.

In plot3d where the transformations are added, should it be

```
elif adaptive:
```

or 

```
if adaptive:
```

That is, does transformation exclude adaptive?  If so, this should be documented.  Also, shouldn't

```
+    from sage.symbolic.callable import is_CallableSymbolicExpression
```

be done only if transformation is not None?

The `@`interact doctests don't really make sense in the command-line format.  I tried them nonetheless, and it popped up a bunch of jmol windows - looked nice!  But there must be a better way to doctest this; perhaps just A;B;C;D;E or something.

Also, why are Cylindrical and Spherical imported in plot3d/all.py?    It's not clear to me why someone would want that available but not just use e.g. spherical_plot3d or just import Spherical if they really needed it? 

Also, doctests are needed for the abstract classes, and (for readability) a blank line between methods wouldn't hurt.


---

Comment by wcauchois created at 2010-02-08 01:53:05

Replying to [comment:17 kcrisman]:

First of all, thanks for taking a look at this. Your comments are very thorough and I will respond to each of them in turn.

> I haven't been able to do a thorough review yet, but in general I agree that this looks very nice!  Everything below should be interpreted as nitpicking; however, because of the last item (doctests) I must put this as 'needs work'.
> 
> In spherical_plot3d, it is a 'drop' of water, not a 'drom'.

Yes, I think that's correct.

> In plot3d where the transformations are added, should it be
> {{{
> elif adaptive:
> }}}
> or 
> {{{
> if adaptive:
> }}}
> That is, does transformation exclude adaptive?  If so, this should be documented.  Also, shouldn't

I think transformation excludes adaptive since parametric_plot3d doesn't support adaptive plots. I'll make sure to document this.

> {{{
> +    from sage.symbolic.callable import is_CallableSymbolicExpression
> }}}
> be done only if transformation is not None?

Sure. I don't see how that really matters though, since its just an import statement.

> The `@`interact doctests don't really make sense in the command-line format.  I tried them nonetheless, and it popped up a bunch of jmol windows - looked nice!  But there must be a better way to doctest this; perhaps just A;B;C;D;E or something.

How about `show(A + B + C + D + E)` in the TESTS section below?

> Also, why are Cylindrical and Spherical imported in plot3d/all.py?    It's not clear to me why someone would want that available but not just use e.g. spherical_plot3d or just import Spherical if they really needed it?

This is one of the major features of the transformation system. You can use spherical_plot3d, which will graph a function r in terms of phi and theta, or you can specify transformation=Spherical() which lets you choose the dependent and independent variables.

For example,

```
plot3d(..., transformation=Spherical('phi', ['r', 'theta']))
```

will graph a function phi in terms of r and theta. So basically you get more flexibility by using Spherical(). Is there a way I could make that clearer in the documentation?

> Also, doctests are needed for the abstract classes, and (for readability) a blank line between methods wouldn't hurt.

Okay.


---

Comment by wcauchois created at 2010-02-08 04:06:15

based on sage 4.3.1.rc0


---

Attachment

based on sage 4.3.1


---

Comment by wcauchois created at 2010-02-08 04:09:32

Please take a look at the changes in trac_7872_new-referee.patch. You can apply trac_7872_new-all.patch to a new sage branch to get all of the changes.


---

Comment by wcauchois created at 2010-02-08 04:09:32

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-02-12 19:55:05

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2010-02-12 19:55:05

> > Also, why are Cylindrical and Spherical imported in plot3d/all.py?    It's not clear to me why someone would want that available but not just use e.g. spherical_plot3d or just import Spherical if they really needed it?
> 
> This is one of the major features of the transformation system. You can use spherical_plot3d, which will graph a function r in terms of phi and theta, or you can specify transformation=Spherical() which lets you choose the dependent and independent variables.
> 
> For example,
> {{{
> plot3d(..., transformation=Spherical('phi', ['r', 'theta']))
> }}}
> will graph a function phi in terms of r and theta. So basically you get more flexibility by using Spherical(). Is there a way I could make that clearer in the documentation?
> 

Most of the changes seem fine.  I am still confused about this, though.  Isn't

```
sage: spherical_plot3d(e^-y,(x,0,2*pi),(y,0,pi))
```

already allowing one to use a different name for the variables?  

Ah, I think I see.  There are six different possibilities for order of independent variables and the dependent variable, and you want to allow all of these - it that it?  Maybe you should make it clearer that this is what is going on by saying that it's not the names, but rather which one is the dependent variable, you are changing - in fact, that the names look the same only to preserve the usual terminology - and then adding to

```
      sage: Spherical('theta', ['r', 'phi']) 
      Spherical coordinate system (theta in terms of r, phi) 
```

by actually plotting something with this.  

Also, in line 623, I think it should be

```
   sage: var('r,u,v')
}}} 
instead of r, u, u; I am surprised this doesn't give a doctest failure (I didn't get a chance to run that right now).

Is it ok if I make it still 'needs work' to just clarify these?  For most users it will all be irrelevant, of course, but if we are really going to import Spherical() at the top level, then it should be very clear what the point is.


---

Comment by wcauchois created at 2010-02-13 00:21:02

Replying to [comment:20 kcrisman]:
> Ah, I think I see.  There are six different possibilities for order of independent variables and the dependent variable, and you want to allow all of these - it that it?  Maybe you should make it clearer that this is what is going on by saying that it's not the names, but rather which one is the dependent variable, you are changing - in fact, that the names look the same only to preserve the usual terminology - and then adding to
> {{{
>       sage: Spherical('theta', ['r', 'phi']) 
>       Spherical coordinate system (theta in terms of r, phi) 
> }}}
> by actually plotting something with this.  

In the docstring on line 254, I do just that.

> Also, in line 623, I think it should be
> {{{
>    sage: var('r,u,v')
> }}} 
> instead of r, u, u; I am surprised this doesn't give a doctest failure (I didn't get a chance to run that right now).

Good catch!

> Is it ok if I make it still 'needs work' to just clarify these?  For most users it will all be irrelevant, of course, but if we are really going to import Spherical() at the top level, then it should be very clear what the point is.

I've done my best on the documentation, but it still might not be entirely clear on how to use Spherical and Cylindrical. Most users, of course, can simply use spherical_plot3d and cylindrical_plot3d. Can you make any concrete suggestions on how to improve the documentation? Does anyone have any ideas for sentences to add?


---

Comment by jason created at 2010-02-24 07:38:45

In your definition of spherical coordinates, is your second angle the *elevation*, or the *inclination*.  I think it might be the inclination, rather than what is stated in the docstring ("elevation").  Inclination is measured with 0 corresponding to the positive z-axis, and has a range of [0,pi].  Elevation is measured from the xy-plane, and has a range of [-pi/2,pi/2], if I understand things correctly.


---

Comment by jason created at 2010-02-24 07:45:23

Also, given the confusion surrounding different conventions and variable names for spherical coordinates, I think it would be better to use "radius", "azimuth", and "inclination" (or "elevation"), instead of "r", "phi", and "theta".  Then it's unambiguous what 


```
Spherical('radius', ['azimuth', 'inclination'])
```


represents.


---

Comment by jason created at 2010-02-24 07:54:17

Similarly, I think cylindrical coordinate components should be spelled out:


```
class Cylindrical(sage.plot.plot3d.plot3d._CoordTrans):
    all_vars = ['radius', 'azimuth', 'height']

    _name = 'Cylindrical (radius, azimuth, height) coordinate system'

    def gen_transform(self, radius=None, azimuth=None, height=None):
        return (radius * cos(azimuth),
                radius * sin(azimuth),
                height)
```



---

Comment by jason created at 2010-02-24 08:19:11

One more point that I thought of when trying to use this feature.  Why should I have to specify the names of variables more than once?  Introspection should be able to get these from my gen_transform function.  It seems like I should be able to do this:


```
class Cylindrical(sage.plot.plot3d.plot3d._CoordTrans):
    """
    Some docs for the mathematical definitions of the variables
    """
    def gen_transform(self, radius=None, azimuth=None, height=None):
        return (radius * cos(azimuth),
                radius * sin(azimuth),
                height)
```


and things should just work.  all_vars can be inferred from the keyword arguments to gen_transform.  It's pretty easy to come up with a good default _name (i.e., 'name of class (variables) coordinate system').


---

Comment by jason created at 2010-02-24 08:19:11

Changing assignee from olazo to jason.


---

Comment by jason created at 2010-02-24 08:27:55

Another polishing point: when given this syntax


```
spherical=(w*cos(u)*sin(v),w*sin(u)*sin(v),w*cos(v),w) 
plot3d(2,(u,-pi,pi),(v,0,pi),transformation=spherical,plot_points=[100,100])
```


why do I have to specify the fourth argument in spherical (i.e., "w")?  In the plot, you know that I'm specifying u and v to be numeric ranges, so it should be easy for Sage to realize that the function variable is w and the independent variables are u and v.


---

Comment by jason created at 2010-02-24 08:44:35

The current code might have a problem if I do:


```
spherical=(w*cos(u)*sin(v),w*sin(u)*sin(v),w*cos(v),w) 
plot3d(lambda x,y: 2,(-pi,pi),(0,pi),transformation=spherical,plot_points=[100,100])

```


because the current strategy does not specify if u or v is the first coordinate range.


---

Comment by jason created at 2010-02-25 04:09:51

Indeed, with the patch:


```
sage: var('u,v,w')
sage: spherical=(w*cos(u)*sin(v),w*sin(u)*sin(v),w*cos(v),w) 
sage: plot3d(lambda x,y: 2,(-pi,pi),(0,pi),transformation=spherical,plot_points=[100,100])
Traceback (most recent call last):
...
ValueError: expected 3-tuple for urange and vrange
```



---

Attachment

apply on top of trac_7872_new-all.patch; based on 4.3.2.


---

Comment by jason created at 2010-02-27 10:13:42

I've addressed every single one of my comments in the trac-7872-polish.patch.  I think this is great functionality, and definitely ready for review!


---

Comment by jason created at 2010-02-27 10:13:42

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-02-27 10:13:53

Changing priority from minor to major.


---

Comment by jason created at 2010-02-27 10:18:14

Remove assignee jason.


---

Comment by wcauchois created at 2010-02-27 10:21:02

Wow, great work Jason. Thank you so much. I've had a really tough quarter in school and I really didn't have time to work on this. I'm also excited to see this feature in Sage. Thanks to everyone who helped make this happen.


---

Comment by jason created at 2010-02-27 16:41:05

Replying to [comment:33 wcauchois]:
> Wow, great work Jason. Thank you so much. I've had a really tough quarter in school and I really didn't have time to work on this. I'm also excited to see this feature in Sage. Thanks to everyone who helped make this happen.

I totally understand.  Now I am talking about transformations in my calc 3 class, so I could take some time to finish this up.  I'm hoping it gets in fairly quickly, though I'll probably apply the patch to our class server anyway.

I positive review your code (well, except for the changes I made :).  Can you review my code?


---

Comment by wcauchois created at 2010-02-28 20:20:56

Jason,
I've taken a look at your code and you've done a great job of cleaning this up! I can't find any fault with it. Apply the following patches to Sage 4.3.3: trac-7872-polish.patch, trac_7872_new-all.patch. Applies fine and passes all doctests.

Now which one of us should mark this as a positive review, or should we bring in a 3rd party?


---

Comment by jason created at 2010-03-01 12:09:22

Changing status from needs_review to positive_review.


---

Comment by jason created at 2010-03-01 12:09:22

Replying to [comment:35 wcauchois]:
> Jason,
> I've taken a look at your code and you've done a great job of cleaning this up! I can't find any fault with it. Apply the following patches to Sage 4.3.3: trac-7872-polish.patch, trac_7872_new-all.patch. Applies fine and passes all doctests.
> 

Apply the patches in this order, though: trac_7872_new-all.patch, trac-7872-polish.patch.

There is precedent for two people collaboratively writing and reviewing each other's code as being okay.  Since you've passed off on my code, and I've passed off on your code, I'll mark this as positive review.  olazo: can you look at this as well, and if you find a problem, change it back to needs work?


---

Comment by jason created at 2010-03-01 12:10:14

(actually, in this case, it was three people because olazo wrote the initial implementation!)


---

Comment by olazo created at 2010-03-03 03:12:45

Replying to [comment:36 jason]:
> There is precedent for two people collaboratively writing and reviewing each other's code as being okay.  Since you've passed off on my code, and I've passed off on your code, I'll mark this as positive review.  olazo: can you look at this as well, and if you find a problem, change it back to needs work?

I can't find anything wrong with the code, it seems quite powerful already :) ! Thanks to you two for taking interest in this. I couldn't do any more recently because of school... It's been great so far though!


---

Comment by mvngu created at 2010-03-03 14:09:38

Resolution: fixed


---

Comment by mvngu created at 2010-03-03 14:09:38

Merged in this order:

 1. [trac_7872_new-all.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7872/trac_7872_new-all.patch)
 1. [trac-7872-polish.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7872/trac-7872-polish.patch)
