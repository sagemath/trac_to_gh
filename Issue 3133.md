# Issue 3133: allow parametric_plot and parametric_plot3d to take a vector as input

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-05-08 13:58:14

Assignee: was

CC:  kcrisman jason


```


On Thu, May 8, 2008 at 1:32 AM, Dan Drake <drake`@`mathsci.kaist.ac.kr> wrote:
> I'm teaching ODEs right now and I'd like to plot the usual sort of
>  solution to a 2-by-2 linear DE system, but the following doesn't work:
>  
>   sage: evec = vector([1,2])
>   sage: var('t')
>   sage: parametric_plot( exp(-t) * evec, 0, 2)
>  
>  The traceback's complaint is "<type 'exceptions.TypeError'>: function
>  takes at most 1 positional arguments (2 given)".
>  
>  I know I could manually do (exp(-t), 2*exp(-t)), but the above form
>  seems so natural. Is there a way to get that to work?

You could type

sage: parametric_plot( list(exp(-t) * evec), 0, 2)

I think it would be reasonable for us to improve parametric_plot so that it takes a vector 
as input instead of just a list or tuple. 

 -- William
```



---

Comment by jason created at 2009-03-06 21:25:43

Changing assignee from was to jason.


---

Comment by jason created at 2009-03-06 21:25:43

Changing status from new to assigned.


---

Comment by jason created at 2009-03-06 21:25:43

As a test, the following should work:


```
sage: var('x')
sage: parametric_plot(vector([x,2*x,3*x^2]), (x,-1,3))
```



---

Comment by jason created at 2009-03-06 21:26:44

The error is different now too:


```
sage: sage: var('x')
x
sage: sage: parametric_plot(vector([x,2*x,3*x^2]), (x,-1,3))
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (21, 0))

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/grout/.sage/temp/good/20161/_home_grout__sage_init_sage_0.py in <module>()

/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot.pyc in parametric_plot(funcs, *args, **kwargs)
   1892         return plot(funcs, *args, **kwargs)
   1893     elif (num_funcs == 3 and num_vars <= 2):
-> 1894         return sage.plot.plot3d.parametric_plot3d.parametric_plot3d(funcs, *args, **kwargs)
   1895     else:
   1896         raise ValueError, "the number of functions and the number of free variables is not a possible combination for 2d or 3d parametric plots"

/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_plot3d.pyc in parametric_plot3d(f, urange, vrange, plot_points, **kwds)
    372             
    373     if not isinstance(f, (tuple, list)) or len(f) != 3:
--> 374         raise ValueError, "f must be a list or tuple of length 3"
    375 
    376     if vrange is None:

ValueError: f must be a list or tuple of length 3
sage: 
```



---

Comment by jason created at 2009-03-06 21:36:31

See #3315 for another input format that parametric_plot should take (functions returning tuples)


---

Attachment


---

Comment by kcrisman created at 2009-09-18 12:59:42

Positive review of the content.  My only concern is that the "internal" functions now have their names changed so we could possibly have to deprecate the non-underscored versions of them (however, only using the underscored ones).   What do you think?  Probably it's unnecessary, since they were never in the global namespace.


---

Comment by jason created at 2009-09-18 14:12:22

Replying to [comment:5 kcrisman]:
> Positive review of the content.  My only concern is that the "internal" functions now have their names changed so we could possibly have to deprecate the non-underscored versions of them (however, only using the underscored ones).   What do you think?  Probably it's unnecessary, since they were never in the global namespace.

I thought it was probably okay since they were not in the global namespace *and* their documentation said that they were internal functions.  I was just making them more conventional internal functions.

If you'd like I can make them deprecated.  Let me know.  I think it's okay in this case to just change the names.


---

Comment by kcrisman created at 2009-09-18 14:43:16

My thoughts exactly, actually - just wanted to see what your reasoning was.


---

Comment by mvngu created at 2009-09-19 20:07:29

Resolution: fixed


---

Comment by mvngu created at 2009-09-19 20:07:29

See #6963 for a follow up to this ticket.
