# Issue 3813: Improve adaptive rendering in plot()

Issue created by migration from https://trac.sagemath.org/ticket/3813

Original creator: anakha

Original creation time: 2008-08-12 05:43:05

Assignee: was

William said at Sage Days 9 that he wanted better adaptive rendering.  So I did it.  

It actually looks much better by default.  Better enough that I don't think users will have to touch plot_points anymore.

And it runs just as fast.


---

Attachment

Better adaptive rendering


---

Comment by saliola created at 2008-08-13 01:23:45

reviewers changes


---

Attachment

slabbe and I have some suggestions that we are submitting as trac_3813-review.patch. Most are documentation edits. Two noteworthy changes:

1. Below data is a list of floats since that is the output of var_and_list_of_values:

```
3632		        x, data = var_and_list_of_values(xrange, plot_points) 
3633	- 	        data = list(data) 
```


2. Lines 3683--3699: We moved the adaptive refinement algorithm into a standalone function and added documentation and doctests for it. It's an interesting enough function that a user might want to play with it.

(sage-adaptive-plot.patch needs to be applied first.)


---

Comment by was created at 2008-08-13 03:13:49

REVIEW:

  * watch out -- sage-adaptive-plot.patch is not a mercurial patch, so no log message.  maybe copy in the message from the ticket. 

  * The very first plot I tried (after applying both patches) is wrong: `plot(sin(1/x), (x,0,3), plot_points=5)`.  For me, it's missing the left-hand side of the plot.   I.e., for some reason inputting a small number of sample points results in only a small part of the plot being plotted.  This is not good.

  * It seems like it is no longer possible to make a plot that *doesn't* use adaptive refinement, since this now fails even though it used to work:

```
time plot(sin(1/x), (x,-1,3),plot_points=10000, plot_division=0)
```

Thus you've broken all code that uses plot_division.  You need to either support plot_division (why not??), or at the worst put in a deprecation warning.  If you do deprecation, see `rings/polynomial/polynomial_ring_constructor.py` for an example of how to do this using the warnings.warn function in the warnings module. 

  * The default option for adaptive_tolerance is not giving in the docstring, but is 0.01.  It should be given here (which appears in two places in the file now):

```
        adaptive_tolerance -- how large a difference should be before the
                              adaptive refinement code considers it significant.
                              This depends on the interval you use by default.

```


  * This line in adaptive_refinement has a bug:

```
    x = (p1[0] + p2[0])/2
```

In particular, if you make p1[0] and p2[0] both Python int's then you can easily get a completely wrong answer.  You must coerce the entries of the pi's to floats first or replace 2 by 2.0.  For example:

```
from sage.plot.plot import adaptive_refinement
a = adaptive_refinement(sin, (int(0),1), (int(1),1), 0.01)
b = adaptive_refinement(sin, (0,1), (1,1), 0.01)
a == b
///
False
```

Same comments about

```
    if abs((p1[1] + p2[1])/2 - y) > adaptive_tolerance:
```



---

Comment by was created at 2008-08-13 03:19:39

IMPORTANT:

 I want to emphasize that I'm not claiming that some of the bugs mentioned today are a result of this patch!  If you don't want to fix them or don't know how, just let me know.   For example the first patch involving `plot(sin(1/x), (x,0,3), plot_points=5)` has been in Sage forever.


---

Comment by was created at 2008-08-13 03:20:30

OH, I realized that I can make a plot that doesn't use adaptive refinement by using adaptive_recursion=0, and that this is clearly documented.


---

Attachment


---

Comment by anakha created at 2008-08-13 19:35:56

Integrate all feedback and fix all reported issues.  This patch is cumulative, so you don't need the first two patches before.


---

Attachment


---

Comment by ncalexan created at 2008-08-13 21:35:28

I made some documentation changes and changed the meaning of adaptive_tolerance slightly.  `3813-diff.patch` is a relative patch showing those changes.

Apply only `3813-anakha-adaptive-plot-v3.patch`.

I think this is ready to be applied even if my changes are not appreciated.


---

Comment by anakha created at 2008-08-13 21:53:14

I kind of agree with these changes.  The only one I have some issues is the adaptive_tolerance change.

I had a personal debate on whether making it work like I did and what you did.  I decided on my way, so as to have a reasonable default in case nothing was specified and leave full control to the user otherwise.

In the end I don't really care either way.


---

Comment by ncalexan created at 2008-08-13 22:08:17

This sounds like a positive review.  Thanks for this fantastic improvement to the sage plotting library!


---

Comment by mabshoff created at 2008-08-15 06:26:53

This patch has some slight reject issues:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.rc0/devel/sage$ patch -p1 < trac_3813-anakha-adaptive-plot-v3.patch 
patching file sage/plot/plot.py
Hunk #1 succeeded at 3449 (offset 35 lines).
Hunk #2 succeeded at 3504 (offset 35 lines).
Hunk #3 succeeded at 3531 (offset 35 lines).
Hunk #4 succeeded at 3599 (offset 35 lines).
Hunk #5 succeeded at 3679 (offset 46 lines).
Hunk #6 FAILED at 3704.
Hunk #7 FAILED at 4536.
2 out of 7 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej
```

Please rebase it against 3.1.rc0 once it is out.

Cheers,

Michael


---

Attachment

Rebase of the patch against 3.1.1.  Includes all prior patches.


---

Comment by anakha created at 2008-08-20 07:32:32

Rebase done.  Sorry for the delay.


---

Comment by mabshoff created at 2008-08-21 22:12:11

Resolution: fixed


---

Comment by mabshoff created at 2008-08-21 22:12:11

Merged in Sage 3.1.2.alpha0


---

Attachment


---

Comment by mabshoff created at 2008-08-21 23:40:04

trac_3813_doctestfixes.patch fixes the following two doctest failures:

```
sage -t  devel/sage/sage/plot/plot.py                       
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha0/tmp/plot.py", line 4762:
    sage: n1 = len(adaptive_refinement(f, (0,0), (pi,0), adaptive_tolerance=0.01)); n1
Expected:
    79
Got:
    15
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha0/tmp/plot.py", line 4766:
    sage: n3 = len(adaptive_refinement(f, (0,0), (pi,0), adaptive_tolerance=0.005)); n3
Expected:
    88
Got:
    16
**********************************************************************
```

It also makes two doctests long.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-22 00:36:06

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-08-22 00:36:06

Arnaut, Franco, 

after discussing this in IRC we thought it might be a good idea to sort out the problems with those two failed doctests before merging this patch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-22 00:36:06

Changing status from closed to reopened.


---

Comment by anakha created at 2008-08-22 04:24:26

I think this is because I changed the default value of adaptive_recursion in the adaptive_refinement() at the last moment.  It seems I forgot to rebuild when running the doctests.  

So just changing the value for what you get should be enough.  Or you can add an adaptive_recursion parameter set to 10 and you should get the same results as in the tests.  If you get differing results then something is wrong.


---

Comment by anakha created at 2008-08-23 21:55:16

I just realized I forgot to change the summary after the argument I made.  

Also, just to make it clear, the two patches that are needed for anybody wanting to try this out are trac_3813_rebase.patch and trac_3813_doctestfixes.patch


---

Attachment

The latest trac_3813-final.patch should apply to the latest Sage.


---

Comment by mabshoff created at 2008-08-27 00:59:03

Merged trac_3813-final.patch in Sage 3.1.2.alpha1


---

Comment by mabshoff created at 2008-08-27 00:59:03

Resolution: fixed
