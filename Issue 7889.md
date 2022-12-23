# Issue 7889: revolution plot

Issue created by migration from https://trac.sagemath.org/ticket/7889

Original creator: olazo

Original creation time: 2010-01-10 03:28:36

Assignee: olazo

CC:  jason

Keywords: revolution,plot

As a continuation of the recent cloning of ploting methods found in mathematica. I've started a clone of Mathematica's [RevolutionPlot3D](http://reference.wolfram.com/mathematica/ref/RevolutionPlot3D.html).

My version, however, can specify the axis of rotation of the curve, given as a line paralel to the z axis, located in the point of coordinates (x;y). And also, the posibility to display the revolved curve.

The code so far is:

```
def revolution_plot(cur,trange,phirange=None,axis=(0,0),showcurve=False,**kwds):
   def findvar(expr):
       try:
           vart=cur.args()[0]
       except:
           vart=var('t')
       return vart

   if phirange==None:#this if-else provides a phirange
       phi=var('phi')
       phirange=(phi,0,2*pi)
   else:
       phi=phirange[0]
       phirange=(phi,phirange[1],phirange[2])

   if str(type(cur)) == "<type 'tuple'>":#this if-else provides a vector v to be ploted
       vart=findvar(cur[0])        
       R=sqrt((cur[0]-axis[0])^2+axis[1]^2)
       v=(R*cos(phi)+axis[0],R*sin(phi)+axis[1],cur[1])
       curveplot=parametric_plot3d((cur[0],0,cur[1]),trange,thickness=2,rgbcolor=(1,0,0))
   elif str(type(cur))== "<type 'list'>":
       vart=findvar(cur[0])        
       R=sqrt((cur[0]-axis[0])^2+axis[1]^2)
       v=(R*cos(phi)+axis[0],R*sin(phi)+axis[1],cur[1])
       curveplot=parametric_plot3d((cur[0],0,cur[1]),trange,thickness=2,rgbcolor=(1,0,0))
   else:
       vart=findvar(cur)
       R=sqrt((vart-axis[0])^2+(axis[1])^2)
       v=(R*cos(phi)+axis[0],R*sin(phi)+axis[1],cur)
       curveplot=parametric_plot3d((vart,0,cur),trange,thickness=2,rgbcolor=(1,0,0))
       
   if showcurve:
       return parametric_plot3d(v,trange,phirange,**kwds)+curveplot
   return parametric_plot3d(v,trange,phirange,**kwds) 
```


Examples of it are available in [this worksheet](http://www.sagenb.org/home/pub/1342/)


---

Comment by olazo created at 2010-01-10 03:36:35

Changing type from defect to enhancement.


---

Comment by olazo created at 2010-01-30 14:53:40

Changing status from new to needs_review.


---

Comment by olazo created at 2010-01-30 15:29:03

I've just found a small bug i'll re-upload in a moment.


---

Comment by olazo created at 2010-01-30 15:29:03

Changing status from needs_review to needs_work.


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Comment by olazo created at 2010-01-30 16:29:52

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-02-05 19:41:45

Overall this patch is a great, needed addition to functionality.  However, it still needs some work, though nothing structural, as far as I can tell.

Trivial typos:

```
    Return a plot of a revoved curve. # should be revolved
    - ``axis`` - A 2-tuple that ... (paralel to the... # should be parallel
```

and here also, where 'plotted' and 'length' are needed:

```
        #this if-else provides a vector v to be ploted
        #if curve is a tuple or a list of lenght 2, it is interpreted as a parametric curve
        #in the x-z plane.
        #if it is of lenght 3 it is interpreted as a parametric curve in 3d space
```


Also in the docs, see plot/contour_plot.py and plot/plot3d/parametric_plot3d.py for an idea of how long to make docstring lines.  For some reason we don't make them wrap around, but cut them off at some number of characters.

I am uncomfortable with

```
    def findvar(expr):#find the dependent variable of the curve
        try:
            vart=curve.args()[0]
        except:
            vart=var('t')
        return vart
```

because even if there isn't a default choice, t could conceivably mean something else, but var() injects it into the global namespace (I think?).  Also, there appear to be several places where

```
vart=findvar(curve[0])
```

but then is not used to make the curveplot.

I think that using isinstance is generally preferred, also.  The timing isn't really that important here, but I think it is more "Pythonic" and:

```
sage: %timeit str(type(curve)) == "<type 'tuple'>"
625 loops, best of 3: 869 ns per loop
sage: %timeit isinstance(curve,tuple)
625 loops, best of 3: 264 ns per loop
```


Just curious - why the xz-plane and not the xy-plane for the default location of the axis of rotation?  Obviously it doesn't "really" matter, but at least in the US most texts start rotating from there, so if this is intended for pedagogical purposes it could be confusing.  I don't know what Mathematica does, though, nor whether this is standard for industrial or non-US uses of revolution plots.

Next,

```
    from sage.symbolic.constants import pi
    from sage.functions.other import sqrt
    from sage.functions.trig import sin
    from sage.functions.trig import cos
```

It looks like you probably need sin and cos to be symbolic, though I'm not sure whether you need to import them.  But I think your use of pi and sqrt would be sufficient to import from the Python/C library math, since they are only being used to compute actual numbers, not symbolics, correct?  Like this

```
from math import pi, sqrt
```


Please document phirange with examples - they are so cool!  You should probably also allow a tuple like (-pi,pi/2) in phirange, since there is absolutely no ambiguity (check len(phirange)==2 or ==3 to do this) and then people don't have to create a new variable

```
sage: var('phi')
sage: revolution_plot3d...(phi,-pi,pi/2)...
```

which would be quite annoying, as I just discovered when trying to get a phirange other than 0 to 2*pi.

You may also want 'curve' to be able to be a Vector object (symbolic), but I am not quite sure whether/how that is supported in such cases. Jason will know, since he has done stuff with this.


---

Comment by kcrisman created at 2010-02-05 19:41:45

Changing status from needs_review to needs_work.


---

Comment by olazo created at 2010-02-06 06:32:07

Wow! that was a lot of (good) criticism. I'll work on it tomorrow.


---

Comment by olazo created at 2010-02-06 21:38:07

Changing status from needs_work to needs_review.


---

Attachment

I just uploaded another patch. It rewrites a lot of things.

Replying to [comment:6 kcrisman]:
> Trivial typos:

Taken care of.



> I am uncomfortable with
> {{{
>     def findvar(expr):#find the dependent variable of the curve
>         try:
>             vart=curve.args()[0]
>         except:
>             vart=var('t')
>         return vart
> }}}
> because even if there isn't a default choice, t could conceivably mean something else, but var() injects it into the global namespace (I think?).
> I think that using isinstance is generally preferred, also.  The timing isn't really that important here, but I think it is more "Pythonic" and:
> {{{
> sage: %timeit str(type(curve)) == "<type 'tuple'>"
> 625 loops, best of 3: 869 ns per loop
> sage: %timeit isinstance(curve,tuple)
> 625 loops, best of 3: 264 ns per loop
> }}}
> 

All of that has been taken care of

> Just curious - why the xz-plane and not the xy-plane for the default location of the axis of rotation?  Obviously it doesn't "really" matter, but at least in the US most texts start rotating from there, so if this is intended for pedagogical purposes it could be confusing.  I don't know what Mathematica does, though, nor whether this is standard for industrial or non-US uses of revolution plots.

Actually, the xy plane is where the axis used to be by default (I left that unchanged). But I've added the posibility to choose to which coordinate axis the revolution axis will be parallel.

> Next,
> {{{
>     from sage.symbolic.constants import pi
>     from sage.functions.other import sqrt
>     from sage.functions.trig import sin
>     from sage.functions.trig import cos
> }}}
> It looks like you probably need sin and cos to be symbolic, though I'm not sure whether you need to import them.  But I think your use of pi and sqrt would be sufficient to import from the Python/C library math, since they are only being used to compute actual numbers, not symbolics, correct?  Like this
> {{{
> from math import pi, sqrt
> }}}

I tried that, but it produced errors

> Please document phirange with examples - they are so cool!  You should probably also allow a tuple like (-pi,pi/2) in phirange, since there is absolutely no ambiguity (check len(phirange)==2 or ==3 to do this) and then people don't have to create a new variable
> {{{
> sage: var('phi')
> sage: revolution_plot3d...(phi,-pi,pi/2)...
> }}}
> which would be quite annoying, as I just discovered when trying to get a phirange other than 0 to 2*pi.

phirange now takes a 2-tuple. I had quite a hard time making that work propper.

> You may also want 'curve' to be able to be a Vector object (symbolic), but I am not quite sure whether/how that is supported in such cases. Jason will know, since he has done stuff with this.

It should be enough to use revolution_plot3d(tuple(your_vector),...).

I'll upload some screenshots once my connection recovers a reasonable speed.


---

Attachment


---

Attachment

Just a few more small things; since this will be a nice new file and functionality, we can afford to start off being very picky.

The optional parameters should be clearly marked as optional, as well as the defaults - again, other docstrings should have good examples.

Please make sure the docstring lines are only a given length.  For whatever reason, we don't let them wrap around (except with error messages or very long output, of course).  I think 80 characters?

Don't need a double colon in line 38 since the examples come later.

Line 33 is confusing, and perhaps contradicts the opening statements of usage (maybe I'm just confused on that, though):

```
 - ``axis`` - A 2-tuple that specifies the position of the revolution axis given that it is parallel to parallel_axis. If parallel_axis is 'z' then axis the a point in which the revolution axis intersects the  `x y` plane. If parallel_axis is 'x' axis is a point in the `y z` plane. And if parallel_axis is 'y' axis is a point in the `x z` plane. 
```

In fact, one thing people often do is like

```
- ``axis`` - (default: 'z') Specifies position of...

   - 'z': The axis is parallel to the `z` axis, intersecting the `x y` plane at the specified point

   - etc.
```

Notice the spaces between the options for readability.  This might even be required in the Sage developer guidelines, I'm not sure.

Lines 65 and 69 should be capitalized?

Look at the plot3d files to see what we decided the convention was for 3d - I can't remember if it's "3D" or "3d" or "3-D" or ...

One should of course be able to input a 2 OR 3 tuple for phirange; I didn't mean you should completely get rid of that option, since it's an option in parametric_plot3d.    But it still bothers me that we are creating random new variables called 'phi' or 'fi'...  the fix makes sense, but what if phi meant something _else_ in the current Sage session?  Maybe you can avoid this using lambda functions (check timings, hopefully would be similar or better... look at the documentation for the third way to call parametric_plot3d:

```
        #. We draw a parametric surface using 3 Python functions (defined
           using lambda):
        
           ::
        
               sage: f = (lambda u,v: cos(u), lambda u,v: sin(u)+cos(v), lambda u,v: sin(v))
               sage: parametric_plot3d(f, (0, 2*pi), (-pi, pi))
        
```

So here we do not need to have a three-tuple for phirange, or indeed trange.  Of course, they now have to be Python or 'callable' functions.

Stylistically you could (optionally, obviously not necessary but does improve readability) 

```
from sage.plot.plot3d.parametric_plot3d import parametric_plot3d
...
curveplot = parametric_plot3d...
```


And feel free to disagree with any comments; after all, you wrote it!  I think these all make sense, though.


---

Comment by kcrisman created at 2010-02-12 19:38:31

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by olazo created at 2010-02-14 19:35:42

Replying to [comment:9 kcrisman]:

All of your comments have been taken care of in this latest patch, except for:

> Please make sure the docstring lines are only a given length.  For whatever reason, we don't let them wrap around (except with error messages or very long output, of course).  I think 80 characters?

making a new line after the 80th character made the docstring look bad in the notebook. I could not fix this.


---

Comment by olazo created at 2010-02-14 19:35:42

Changing status from needs_work to needs_review.


---

Comment by mhampton created at 2010-02-27 19:02:38

Changing status from needs_review to needs_work.


---

Comment by mhampton created at 2010-02-27 19:02:38

Coverage is not complete, unless I mis-applied the patches (but I don't think I did):


```
sage -coverage devel/sage-p1/sage/plot/plot3d/plot3d.py 
----------------------------------------------------------------------
devel/sage-p1/sage/plot/plot3d/plot3d.py
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE devel/sage-p1/sage/plot/plot3d/plot3d.py: 81% (13 of 16)

Missing documentation:
	 * triangle(self, a, b, c, color = None):
	 * smooth_triangle(self, a, b, c, da, db, dc, color = None):
	 * axes(scale=1, radius=None, **kwds):
```


So I'm switching this to needs work.  Otherwise things look OK, doctests pass, documentation looks good.


---

Comment by jason created at 2010-02-27 19:19:30

The patch does not touch these functions; those functions were not documented before.  The missing documentation should be addressed on another ticket, as it has nothing to do with this ticket.


---

Comment by jason created at 2010-02-27 19:19:30

Changing assignee from olazo to jason.


---

Comment by jason created at 2010-02-27 19:19:46

Changing assignee from jason to olazo.


---

Comment by olazo created at 2010-02-27 21:35:27

Changing priority from minor to major.


---

Comment by olazo created at 2010-02-27 22:15:34

Changing status from needs_work to needs_review.


---

Comment by olazo created at 2010-02-27 22:15:34

Replying to [comment:11 mhampton]:
> Coverage is not complete, unless I mis-applied the patches (but I don't think I did):
> 
> {{{
> sage -coverage devel/sage-p1/sage/plot/plot3d/plot3d.py 
> ----------------------------------------------------------------------
> devel/sage-p1/sage/plot/plot3d/plot3d.py
> ERROR: Please add a `TestSuite(s).run()` doctest.
> SCORE devel/sage-p1/sage/plot/plot3d/plot3d.py: 81% (13 of 16)
> 
> Missing documentation:
> 	 * triangle(self, a, b, c, color = None):
> 	 * smooth_triangle(self, a, b, c, da, db, dc, color = None):
> 	 * axes(scale=1, radius=None, **kwds):
> }}}
> 
> So I'm switching this to needs work.  Otherwise things look OK, doctests pass, documentation looks good.

In fact, this patch has nothing to do with those functions. So I'll move this to needs review.


---

Comment by mhampton created at 2010-02-28 14:35:05

Sorry about that.  I'll make a separate ticket.  -Marshall


---

Comment by jason created at 2010-03-04 02:13:11

mhampton: it looks like you pretty much gave this a positive review.  If so, could you change it to positive review?


---

Comment by mhampton created at 2010-03-04 12:32:24

Replying to [comment:17 jason]:
> mhampton: it looks like you pretty much gave this a positive review.  If so, could you change it to positive review?

Yes, I think so.  I haven't banged on it as much I might like, but given the multiple reviews of this I am happy to give it a positive review.  It would be nice to get it into sage-4.3.4.


---

Comment by mhampton created at 2010-03-04 12:32:24

Changing status from needs_review to positive_review.


---

Comment by olazo created at 2010-03-04 18:34:10

Replying to [comment:19 mhampton]:
> Replying to [comment:17 jason]:
> > mhampton: it looks like you pretty much gave this a positive review.  If so, could you change it to positive review?
> 
> Yes, I think so.  I haven't banged on it as much I might like, but given the multiple reviews of this I am happy to give it a positive review.  It would be nice to get it into sage-4.3.4.  

Great! thank you all!


---

Comment by jhpalmieri created at 2010-04-15 22:00:33

There are several problems here:

 - The patch (revolution_plot3d_3.patch -- I assume this is what I'm supposed to apply) doesn't apply cleanly to Sage 4.3.5.
 - This is easy to fix, but once I fix it, it shows no coverage.  I think this can be fixed by changing the triple quotes `'''` around the docstring to triple quotes `"""`.
 - Same issue: with triple quotes in the form `'''`, doctests don't get run.  With triple quotes `"""`, doctests run, but several of them fail:

```
**********************************************************************
File "/mnt/usb1/scratch/palmieri/sage-4.3.5-testing/devel/sage/sage/plot/plot3d/revolution_plot3d.py", line 56:
    sage: var('u')
Expected nothing
Got:
    u
**********************************************************************
File "/mnt/usb1/scratch/palmieri/sage-4.3.5-testing/devel/sage/sage/plot/plot3d/revolution_plot3d.py", line 75:
    sage: var('u')
Expected nothing
Got:
    u
**********************************************************************
File "/mnt/usb1/scratch/palmieri/sage-4.3.5-testing/devel/sage/sage/plot/plot3d/revolution_plot3d.py", line 89:
    sage: var('u')
Expected nothing
Got:
    u
**********************************************************************
File "/mnt/usb1/scratch/palmieri/sage-4.3.5-testing/devel/sage/sage/plot/plot3d/revolution_plot3d.py", line 95:
    sage: var('u')
Expected nothing
Got:
    u
**********************************************************************
File "/mnt/usb1/scratch/palmieri/sage-4.3.5-testing/devel/sage/sage/plot/plot3d/revolution_plot3d.py", line 97:
    sage: revolution_plot3d(curve,(u,0,pi),(0,pi/2),show_curve=True,parallel_axis='z',opacity=0.5).show(aspect_ratio=(1,1,1),frame=False)
Expected nothing
Got:
    ta
**********************************************************************
1 items had failures:
   5 of  22 in __main__.example_0
***Test Failed*** 5 failures.
For whitespace errors, see the file /home/palmieri/.sage//tmp/.doctest_revolution_plot3d.py
	 [6.8 s]
 
----------------------------------------------------------------------
```



---

Comment by jhpalmieri created at 2010-04-15 22:00:33

Changing status from positive_review to needs_work.


---

Attachment


---

Comment by olazo created at 2010-05-29 21:26:33

Changing status from needs_work to needs_review.


---

Comment by olazo created at 2010-05-29 21:26:33

I've uploaded a fourth patch correcting a minor bug, and using """. It patches correctly on sage 4.4.1 so i'm moving this back to needs review.


---

Comment by jhpalmieri created at 2010-06-22 22:24:44

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-06-22 22:24:44

I'm attaching a reviewer patch which should *replace* the original one.  This includes the trac number as part of the "commit" message and fixes the doctest failures which I mentioned earlier (and which hadn't been fixed by the most recent patch).


---

Attachment

apply only this patch


---

Comment by mpatel created at 2010-07-20 10:12:23

Resolution: fixed
