# Issue 2590: plotting a line with no points throws a nonsensical error

Issue created by migration from https://trac.sagemath.org/ticket/2590

Original creator: jason

Original creation time: 2008-03-19 01:38:27

Assignee: was

The first attached patch returns an empty graphic when plotting a line with no points.

This addresses the concern in #2038 about not having any valid points in a plot (by returning an empty plot).

The second patch modifies using a tidbit from moretti's patch in #2038---he should get credit for it.


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2008-03-19 10:13:36

If I apply those two patches I get an additional doctest failure besides the one caused by #2583:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha0$ ./sage -t -long devel/sage/sage/plot/plot.py
sage -t -long devel/sage-main/sage/plot/plot.py             **********************************************************************
File "plot.py", line 3466:
    sage: p[0][1][0]
Expected:
    -0.66666666666666...
Got:
    -0.5
**********************************************************************
File "plot.py", line 3513:
    sage: plot(x^(1/3), (x,-1,1))
Expected nothing
Got:
    WARNING: When plotting, failed to evaluate function at 99 points.
    Last error message: 'negative number cannot be raised to a fractional power'
    <BLANKLINE>
**********************************************************************
1 items had failures:
   2 of  28 in __main__.example_111
***Test Failed*** 2 failures.
For whitespace errors, see the file .doctest_plot.py
         [70.3 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:

```


Cheers,

Michael


---

Attachment

apply instead of plot_use_data.patch


---

Comment by jason created at 2008-03-19 15:44:25

The plot_use_data-2.patch fixes the doctest failures.  I also realized the docs for plot_division were incorrect, so that is corrected.

Score one more for doctests---they helped find both the off-by-one error fixed in the patch and the incorrect plot_division documentation.

Apply zero-point-line.patch and plot_use_data-2.patch and don't apply plot_use_data.patch.


---

Comment by mabshoff created at 2008-03-28 08:01:33

Jason, this patch set needs rebasing past 2.11.alpha2.

Cheers,

Michael


---

Attachment


---

Comment by jason created at 2008-04-09 04:24:04

Apply trac-2590-rebased.patch only.  This is a rebased version of all previous changes, rebased to sage 3.0alpha2.

Doctests in sage/plot/ pass.


---

Comment by mabshoff created at 2008-04-09 04:44:23

trac-2590-rebased.patch applied against my 3.0.alpha3 merge tree doctests fine. I am no expert on the code in question, so somebody else needs to review it.

Thumbs up from me.

Cheers,

Michael


---

Comment by mhansen created at 2008-04-12 07:43:32

Looks good to me.


---

Comment by mabshoff created at 2008-04-12 11:29:26

Merged trac-2590-rebased.patch in Sage 3.0.alpha4


---

Comment by mabshoff created at 2008-04-12 11:29:26

Resolution: fixed
