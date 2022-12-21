# Issue 5567: [with patch, needs review] bug in region_plot

Issue created by migration from Trac.

Original creator: whuss

Original creation time: 2009-03-19 16:29:16

Assignee: whuss


```
Hello, this command produces one half of a cirle, not 1/4 as excepted.
I think that this is a bug in sage 3.4

Robert

region_plot([y>0,x>0,x^2+y^2<3], (-3, 3), (-3,3),plot_points=100,incol='gray').show(aspect_ratio=1)
```


The attached patch fixes this.


---

Comment by wcauchois created at 2009-04-13 22:28:40

REFEREE REPORT:

Applies fine to Sage 3.4, fixes the bug as described, passes its doctests. This looks like a solid patch. Positive review.


---

Comment by mabshoff created at 2009-04-15 00:47:57

This has bitrottet, please rebase:

```
sage-3.4.1.rc3/devel/sage$ patch -p1 < trac_5567_region_plot.patch 
patching file sage/plot/contour_plot.py
Hunk #1 FAILED at 234.
Hunk #2 FAILED at 247.
Hunk #3 succeeded at 277 (offset 14 lines).
Hunk #4 succeeded at 308 (offset 14 lines).
2 out of 4 hunks FAILED -- saving rejects to file sage/plot/contour_plot.py.rej
```


Bill: When you review please always review against the latest release snapshot.

Cheers,

Michael


---

Comment by whuss created at 2009-04-17 14:54:38

rebased for sage-3.4.1.rc3


---

Attachment


---

Comment by wcauchois created at 2009-04-21 05:12:50

REFEREE REPORT:

Applies fine to Sage 3.4.1.rc4. Still passes its doctests and implements the changes as described in the ticket. Positive review.


---

Comment by mabshoff created at 2009-04-23 07:33:19

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-23 07:33:19

Resolution: fixed


---

Comment by jason created at 2009-04-24 01:09:19

Shouldn't the code in the doctest be deprecated in light of http://trac.sagemath.org/sage_trac/ticket/5413 ?

In fact, the equify function seems like it is in direct conflict with the deprecation in http://trac.sagemath.org/sage_trac/ticket/5413, is it not?


---

Comment by wcauchois created at 2009-05-04 21:54:42

Replying to [comment:6 jason]:
> Shouldn't the code in the doctest be deprecated in light of http://trac.sagemath.org/sage_trac/ticket/5413 ?
> 
> In fact, the equify function seems like it is in direct conflict with the deprecation in http://trac.sagemath.org/sage_trac/ticket/5413, is it not?

Playing around in the REPL, I don't see a way to define an inequality with explicit variables -- since its not really a function. `f(x) = x^2 < 2` throws an exception, for example. For region_plot, the variables can be made explicit by specifying them in the plot ranges, in which case they are passed on to equify via an argument. So the ambiguity which was the motivation for #5413 can be avoided. I think that this is a subtly different situation, and that `equify` is fine.


---

Comment by jason created at 2009-05-05 01:37:41

Replying to [comment:7 wcauchois]:
> Replying to [comment:6 jason]:
> > Shouldn't the code in the doctest be deprecated in light of http://trac.sagemath.org/sage_trac/ticket/5413 ?
> > 
> > In fact, the equify function seems like it is in direct conflict with the deprecation in http://trac.sagemath.org/sage_trac/ticket/5413, is it not?
> 
> Playing around in the REPL, I don't see a way to define an inequality with explicit variables -- since its not really a function. `f(x) = x^2 < 2` throws an exception, for example. For region_plot, the variables can be made explicit by specifying them in the plot ranges, in which case they are passed on to equify via an argument. So the ambiguity which was the motivation for #5413 can be avoided. I think that this is a subtly different situation, and that `equify` is fine.

The point is that equify lets variables default to None, and in that case, automatically chooses the order of variables in the call signature.  That's what the deprecation is about---making sure that the user always specified the order of evaluation, and not automatically choosing an order.

And while the ambiguity can be avoided in the function call, the doctest in the patch still uses deprecated syntax (which should throw a deprecation warning).  The doctest should still be changed to have the variables specified.
