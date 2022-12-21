# Issue 1575: plotting -- fix vector plotting

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-20 18:47:13

Assignee: was


```
On Dec 19, 2007 12:24 PM, Jason Grout <> wrote:
> I'm teaching linear algebra next semester and plan to use Sage.  In
> trying the "obvious" way to plot a vector:
> 
> sage: v=vector([1,2])
> sage: v.plot().show()
> 
> I get what looks like a step function of the coordinates. 

Yes, that's what it is.  This is very useful, e.g., when using
vectors of data, computing Fourier transforms of them, etc. 
And it works in arbitrary dimensions.  

>  Instead, I
> have to do:
> 
> sage: v=vector([1,2])
> sage: arrow((0,0),v).show()
> 
> which doesn't seem quite so natural to an undergraduate linear algebra
> student.  First, is there an easier way to plot a vector (yes, I know I
> don't have to define v above and could just give the coordinates to
> arrow, but usually I'll be doing something with v as a vector)?  Is it
> reasonable to redefine v.plot() to return the arrow for a vector with 3
> or fewer dimensions, or is there some bigger reason to have things the
> way they are now?

I think that would be bad, because it's potentially confusing and
unsystematic.  However, the following -- which you will like --
would be acceptable to me:

   Redefine v.plot() so for dimensions <= 3 it does what you describe above,
i.e., draws an arrow, but for dimensions >= 4 it gives an error message.
Then add an option to plot called "step", which if set to True restores
the current behavior.    

In fact, this was my intention all along, and somehow I screwed up. 
The current plot signature for vectors is:

    def plot(self, xmin=0, xmax=1, eps=None, res=None,
             connect=True, step=False, **kwds):

Notice that step=False is already there!  



-- William

```



---

Comment by was created at 2007-12-20 18:47:39

Changing assignee from was to jason grout.


---

Comment by jason created at 2007-12-21 09:01:59

Changing status from new to assigned.


---

Comment by jason created at 2007-12-21 09:01:59

Changing assignee from jason grout to jason.


---

Attachment


---

Comment by jason created at 2007-12-21 09:06:40

In vector-plot.patch, plot is redefined to behave thusly:

* the option "type" has values 'arrow', 'point', and 'step'
* if 1 <= dimension <= 3, default type='arrow'
* if dimension > 3, default type='step'

The old plot function was renamed plot_step.


---

Comment by jason created at 2008-01-15 12:37:06

I just discovered that Arrow has been changed to arrow3d in sage 2.9.3.  The patch should be updated accordingly.


---

Attachment


---

Comment by jason created at 2008-01-15 23:24:25

I've renamed the "type" option to "plot_type" and fixed the Arrow issue (the graphics interface changed around 2.9.3) and the doctest "eps" issue.

The vector-plot-updated.patch should be applied instead of vector-plot.patch.


---

Comment by cwitty created at 2008-01-27 03:23:23

Looks good; doctests pass.


---

Comment by mabshoff created at 2008-01-27 03:32:26

Resolution: fixed


---

Comment by mabshoff created at 2008-01-27 03:32:26

vector-plot-updated.patch merged in Sage 2.10.1.rc1.
