# Issue 2517: ignore bad values in plot

Issue created by migration from https://trac.sagemath.org/ticket/2517

Original creator: jason

Original creation time: 2008-03-14 16:58:53

Assignee: was


```
> >  Hi,
> >
> >  With sage-2.10.3 the following plot fails:
> >
> >  plot(-x*log(x),0,1, plot_points=1000)
> >
> >  This worked fine in sage-2.10.2. Note that the left hand limit is
> >  well-defined and can be approximated:
> >
> >  plot(-x*log(x),0.00000000000000001,1, plot_points=1000)
> >
> >  Is this a feature or a bug?

It fails because it used to be that there was a bug where when
plotting the left and right endpoints were omitted, because the sample
points were *all* randomized!  This really
annoyed a lot of people, especially people making animations,
but allowed the above example to work.

I think the solution is to fix our plotting code so that it just automatically
completely ignores a few bad values (like it used to), possibly printing
a warning.

 -- William
```




---

Comment by robertwb created at 2008-03-14 18:29:22

We should possible plot the endpoints *and* randomized values just inside the endpoints for cases like this.


---

Comment by jason created at 2008-03-14 21:21:42

The patch above takes care of two things:
  * ignores points that have OverflowError when evaluated
  * deletes erroneous points from the plot, thereby solving the longstanding bug of "float not subscriptable" mentioned lots of times previously, for example, when plotting x^(1/3).


---

Comment by was created at 2008-03-14 21:36:26

I think this line in the patch

```
print i, data[i], i+1, data[i+1] 
```

was for debugging purposes and should be deleted.


---

Attachment


---

Comment by jason created at 2008-03-15 01:51:07

Sorry, I thought I uploaded a new patch before anyone saw :).  The current patch does not have that line.


---

Comment by was created at 2008-03-15 09:04:04

I applied your patch and it doesn't work.  The example above failes with `<type 'exceptions.TypeError'>: 'tuple' object is not callable`:


```

sage:  plot(-x*log(x),0,1, plot_points=1000)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/was/papers/current/modabvar/<ipython console> in <module>()

/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/plot/plot.py in __call__(self, funcs, *args, **kwds)
   3380             del kwds['show']
   3381         if hasattr(funcs, 'plot'):
-> 3382             G = funcs.plot(*args, **kwds)
   3383         # if we are using the generic plotting method
   3384         else:

/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/calculus/calculus.py in plot(self, *args, **kwds)
    913         else:
    914             f = self.function(param)
--> 915         return plot(f, *args, **kwds)
    916 
    917     def __lt__(self, right):

/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/plot/plot.py in __call__(self, funcs, *args, **kwds)
   3380             del kwds['show']
   3381         if hasattr(funcs, 'plot'):
-> 3382             G = funcs.plot(*args, **kwds)
   3383         # if we are using the generic plotting method
   3384         else:

/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/calculus/calculus.py in plot(self, *args, **kwds)
    913         else:
    914             f = self.function(param)
--> 915         return plot(f, *args, **kwds)
    916 
    917     def __lt__(self, right):

/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/plot/plot.py in __call__(self, funcs, *args, **kwds)
   3395                 xmax = args[1]
   3396                 args = args[2:]
-> 3397                 G = self._call(funcs, (xmin, xmax), *args, **kwds)
   3398             else:
   3399                 print "there were %s extra arguments (besides %s)" % (n, funcs)

/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/plot/plot.py in _call(self, funcs, xrange, parametric, polar, label, **kwds)
   3463                 exceptions += 1
   3464                 exception_indices.append(i)
-> 3465         data = [data[i] for i in xrange(len(data)) if i not in exception_indices]
   3466             
   3467         # adaptive refinement

<type 'exceptions.TypeError'>: 'tuple' object is not callable

```



---

Comment by jason created at 2008-03-18 21:51:23

Apply the second patch instead of the first.

Second patch is rebased against 2.10.4 and works correctly.


---

Attachment


---

Comment by mhansen created at 2008-03-18 23:10:44

Looks good to me.


---

Comment by mabshoff created at 2008-03-19 00:34:57

Resolution: fixed


---

Comment by mabshoff created at 2008-03-19 00:34:57

Merged plot_undefined.2.patch in Sage 2.11.alpha0
