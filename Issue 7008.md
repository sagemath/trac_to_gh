# Issue 7008: consolidate in plotting all extraction of variables, ranges, and fast_float setup

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-09-25 04:09:34

Assignee: was

CC:  kcrisman mhansen rbeezer robertwb

Currently, code for extracting variables, dealing with ranges of variables, and making the functions fast_float is scattered throughout the plotting directory.  There are multiple implementations, each having its own quirks.

This patch consolidates all of this to two functions in sage.plot.misc and makes all the necessary changes to use this consolidated function.


---

Attachment


---

Comment by jason created at 2009-09-25 05:59:29

I believe this depends on #6985


---

Comment by kcrisman created at 2009-09-25 14:58:21

Cursory review reveals a bit of a slowdown.  Try even

```
sage: f(x)=sin(x)
sage: timeit('plot(f,(-pi,pi))')
```

Also notice that 

```
sage: timeit('plot(f(x),(-pi,pi))')
```

is even slower yet.  These are all milliseconds, not seconds, of course, but in a large plot of many functions, a contour plot with a very dense grid, or for making interacts snappy...  Is there any way to fix that? 

Also, what is the rationale for using fast_float and not fast_callable?  I ask only because there has been so much talk about "we should really use fast_callable instead of fast_float for X".  But I may not understand the difference between the two.

Finally, there should be at least one test to demonstrate that 

```
sage: plot(f, -pi, pi)
```

and friends still work in the one-variable case, because there is no reason for that to disappear in the name of consistency.  The more parentheses, the more confused students get.  But it can be a test, since of course we don't have to promote that syntax.

These are all nitpicky.  Nice refactoring, and all tests pass!


---

Comment by jason created at 2009-09-25 21:18:46

Replying to [comment:5 kcrisman]:
> Cursory review reveals a bit of a slowdown.  Try even
> {{{
> sage: f(x)=sin(x)
> sage: timeit('plot(f,(-pi,pi))')
> }}}
> Also notice that 
> {{{
> sage: timeit('plot(f(x),(-pi,pi))')
> }}}
> is even slower yet.  These are all milliseconds, not seconds, of course, but in a large plot of many functions, a contour plot with a very dense grid, or for making interacts snappy...  Is there any way to fix that? 

I will check into this.  My guess is that any slowdown is in a fixed cost, not a marginal cost, so the slowdown should not scale.  Can you test, for example, contour plots with varying grid sizes (before/after the patch) to see if there is a huge slowdown?

I wonder how much moving this function to cython might help.  Well, I guess checking and then profiling is the right course of action.


> 
> Also, what is the rationale for using fast_float and not fast_callable?  I ask only because there has been so much talk about "we should really use fast_callable instead of fast_float for X".  But I may not understand the difference between the two.

fast_callable has not matured to the point that we need it yet.  For example, fast_callable(0) does not work, whereas fast_float(0) does.  #5572 lists some of the things that fast_callable needs to still implement.

That said, fast_float uses fast_callable where it can.  So for most functions, I am actually using fast_callable underneath things.

> 
> Finally, there should be at least one test to demonstrate that 
> {{{
> sage: plot(f, -pi, pi)
> }}}
> and friends still work in the one-variable case, because there is no reason for that to disappear in the name of consistency.  The more parentheses, the more confused students get.  But it can be a test, since of course we don't have to promote that syntax.

Hmmm...did I delete a test doing that?  I didn't mean to.

I did change the parametric_plot syntax to deprecate ranges without parenthesis.  This was to maintain consistency with the 3d parametric plot.  For example, currently, parametric_plot((t,t^2), 0, 2*pi) works, but parametric_plot((t,t<sup>2,t</sup>3), 0, 2*pi) does not work.  


> 
> These are all nitpicky.  Nice refactoring, and all tests pass!

Thanks!


---

Comment by kcrisman created at 2009-09-26 02:38:22

> 
> I will check into this.  My guess is that any slowdown is in a fixed cost, not a marginal cost, so the slowdown should not scale.  Can you test, for example, contour plots with varying grid sizes (before/after the patch) to see if there is a huge slowdown?

I  had already done some of this.  After trying some more stuff, it looks like it's just not enough to be worthwhile to do anything else - possibly a little more than fixed, but not much.  Just thought you might have a thought.

> That said, fast_float uses fast_callable where it can.  So for most functions, I am actually using fast_callable underneath things.

Ah, I didn't know that.  Neat.

> > Finally, there should be at least one test to demonstrate that 
> > {{{
> > sage: plot(f, -pi, pi)
> > }}}
> > and friends still work in the one-variable case, because there is no reason for that to disappear in the name of consistency.  The more parentheses, the more confused students get.  But it can be a test, since of course we don't have to promote that syntax.
> 
> Hmmm...did I delete a test doing that?  I didn't mean to.
> 
Didn't delete, but a couple of ones in graphics_array got changed.  Not a big deal, as there are plenty of others in the main docs - I just didn't have time to check if those were the only ones earlier today.

I like the use of "ignore".

Okay, code checks out, and a bevy of examples don't just pass tests but also look like they are supposed to :)


---

Comment by mvngu created at 2009-09-26 03:30:42

I'm getting the following doctest failures, all of which are deprecation warnings:

```
sage -t -long devel/sage/doc/en/tutorial/tour_plotting.rst
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/doc/en/tutorial/tour_plotting.rst", line 176:
    sage: implicit_plot3d(x^2 + y^2 + z^2 - 4, (-2, 2), (-2, 2), (-2, 2))
Expected nothing
Got:
    doctest:245: DeprecationWarning: Unnamed ranges for more than one variable is deprecated and will be removed from a future release of Sage; you can used named ranges instead, like (x,0,2)
    <BLANKLINE>
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/doc/en/tutorial/tour_plotting.rst", line 74:
    sage: parametric_plot((cos(x),sin(x)^3),0,2*pi,rgbcolor=hue(0.6))
Expected nothing
Got:
    doctest:1: DeprecationWarning: variable ranges to parametric_plot must be given as tuples, like (2,4) or (t,2,3)
    <BLANKLINE>
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/doc/en/tutorial/tour_plotting.rst", line 81:
    sage: p1 = parametric_plot((cos(x),sin(x)),0,2*pi,rgbcolor=hue(0.2))
Expected nothing
Got:
    doctest:1: DeprecationWarning: variable ranges to parametric_plot must be given as tuples, like (2,4) or (t,2,3)
**********************************************************************
3 items had failures:
   1 of   4 in __main__.example_13
   1 of   4 in __main__.example_4
   1 of   7 in __main__.example_5
***Test Failed*** 3 failures.
For whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_tour_plotting.py
	 [10.1 s]

<SNIP>

sage -t -long devel/sage/doc/fr/tutorial/tour_plotting.rst
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/doc/fr/tutorial/tour_plotting.rst", line 75:
    sage: parametric_plot((cos(x),sin(x)^3),0,2*pi,rgbcolor=hue(0.6))
Expected nothing
Got:
    doctest:1: DeprecationWarning: variable ranges to parametric_plot must be given as tuples, like (2,4) or (t,2,3)
    <BLANKLINE>
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/doc/fr/tutorial/tour_plotting.rst", line 82:
    sage: p1 = parametric_plot((cos(x),sin(x)),0,2*pi,rgbcolor=hue(0.2))
Expected nothing
Got:
    doctest:1: DeprecationWarning: variable ranges to parametric_plot must be given as tuples, like (2,4) or (t,2,3)
**********************************************************************
2 items had failures:
   1 of   4 in __main__.example_4
   1 of   7 in __main__.example_5
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_tour_plotting.py
	 [8.0 s]

<SNIP>

sage -t -long devel/sage/sage/calculus/desolvers.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/calculus/desolvers.py", line 235:
    sage: parametric_plot((solnx,solny),0,1)
Expected nothing
Got:
    doctest:1: DeprecationWarning: variable ranges to parametric_plot must be given as tuples, like (2,4) or (t,2,3)
    <BLANKLINE>
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/calculus/desolvers.py", line 307:
    sage: P2 = parametric_plot((solnx,solny),0,1)
Expected nothing
Got:
    doctest:1: DeprecationWarning: variable ranges to parametric_plot must be given as tuples, like (2,4) or (t,2,3)
**********************************************************************
2 items had failures:
   1 of  12 in __main__.example_4
   1 of  17 in __main__.example_5
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_desolvers.py
	 [6.2 s]

<SNIP>

sage -t -long devel/sage/doc/en/tutorial/tour_algebra.rst
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/doc/en/tutorial/tour_algebra.rst", line 263:
    sage: P = parametric_plot((cos(2*t) + 2*cos(t), 4*cos(t) - cos(2*t) ),   0, 2*pi, rgbcolor=hue(0.9))
Expected nothing
Got:
    doctest:1: DeprecationWarning: variable ranges to parametric_plot must be given as tuples, like (2,4) or (t,2,3)
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_15
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_tour_algebra.py
	 [5.8 s]

<SNIP>

sage -t -long devel/sage/doc/fr/tutorial/tour_algebra.rst
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/doc/fr/tutorial/tour_algebra.rst", line 242:
    sage: P = parametric_plot((cos(2*t) + 2*cos(t), 4*cos(t) - cos(2*t) ),   0, 2*pi, rgbcolor=hue(0.9))
Expected nothing
Got:
    doctest:1: DeprecationWarning: variable ranges to parametric_plot must be given as tuples, like (2,4) or (t,2,3)
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_15
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_tour_algebra.py
	 [5.7 s]
```



---

Comment by jason created at 2009-09-26 04:05:57

The implicit_plot3d warnings should have been turned on before, but they weren't since they used their own version of the setup function, and so we missed them when we did the deprecation warnings.  So I'll just fix those tests.

The parametric_plot deprecation warnings are new with this patch, though (as pointed about above).  However, especially if they were in our basic documentation like the tour, maybe I should bring this up on sage-devel.


---

Comment by jason created at 2009-09-29 06:06:26

apply on top of previous patch


---

Attachment

I posted about the parametric_plot deprecation and no one opposed the deprecation.  So the new patch should fix everything up just right.


---

Comment by kcrisman created at 2009-09-29 14:35:18

All looks good, doctests pass.


---

Comment by mvngu created at 2009-09-29 14:53:29

Merged both patches.


---

Comment by mvngu created at 2009-09-29 14:53:29

Resolution: fixed
