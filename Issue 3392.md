# Issue 3392: upgrade matplotlib to 0.98.0 release

Issue created by migration from https://trac.sagemath.org/ticket/3392

Original creator: mabshoff

Original creation time: 2008-06-10 19:08:37

Assignee: mabshoff

matplotlib 0.98.0 is a major release which requires python2.4 and numpy 1.1. It contains significant improvements and may require some advanced users to update their code; see migration and API_CHANGES. We are supporting a maintenance 


---

Comment by jason created at 2008-07-14 20:43:27

I think we need to upgrade to numpy 1.1.0 and do this upgrade simultaneously.  I think they each require the other.


---

Comment by jason created at 2008-07-14 20:45:13

(see #3390 for the numpy 1.1.0 upgrade spkg).


---

Comment by tabbott created at 2008-07-20 23:33:02

matplotlib-sage.patch is (at least part of) what is needed to get sage to work with matplotlib 0.98;  (they renamed matplotlib.patches.lines to matplotlib.lines).

Ignore matplotlib-sage.2.patch.


---

Comment by jason created at 2008-08-15 13:17:39

We might as well upgrade to matplotlib 0.98.3 now.


---

Comment by jason created at 2008-08-21 22:27:16

Apply instead of above


---

Attachment

the matplotlib-sage.3.patch above includes the other two patches and should be applied instead.  the .3.patch file also includes several more fixes for things added in 3.1.1.


---

Comment by jason created at 2008-08-21 22:34:56

New spkg up at http://sage.math.washington.edu/home/jason/matplotlib-0.98.3.spkg

This depends on the numpy 1.1 spkg at #3390.


---

Comment by mabshoff created at 2008-08-27 09:58:16

Spkg and patch look good to me. I integrated Ondrej's fix from #3792 and did some cleanups to SPKG.txt. The new spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha1/matplotlib-0.98.3.p0.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-27 10:50:15

We have some deprecation warning that causes a number of doctests:

```
        sage -t -long devel/sage/sage/schemes/elliptic_curves/lseries_ell.py # 1 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py # 1 doctests failed
        sage -t -long devel/sage/sage/rings/padics/padic_base_generic.py # 1 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/polynomial_element.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/modules/free_module_element.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/gsl/interpolation.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/gsl/fft.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/gsl/dwt.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/gsl/ode.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/plot/plot.py # 1 doctests failed
        sage -t -long devel/sage/sage/finance/time_series.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/calculus/desolvers.py # 1 doctests failed
```

Specifically:

```
sage -t -long devel/sage/sage/finance/time_series.pyx       
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/tmp/time_series.py", line 926:
    sage: v.plot(points=True)
Expected nothing
Got:
    doctest:4821: DeprecationWarning: replace "faceted=False" with "edgecolors='none'"
    <BLANKLINE>
**********************************************************************
```

Patch coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-27 11:29:25

With the following code all doctests pass:

```
    def _render_on_subplot(self,subplot):
        options = self.options()
        c = to_mpl_color(options['rgbcolor'])
        a = float(options['alpha'])
        s = int(options['pointsize'])
        scatteroptions={}
        if not faceted: scatteroptions['edgecolors'] = 'none'
        subplot.scatter(self.xdata, self.ydata, s=s, c=c, alpha=a, **scatteroptions)

```



---

Comment by mabshoff created at 2008-08-27 12:16:03

Resolution: fixed


---

Attachment

Merged both patches in Sage 3.1.2.alpha1


---

Comment by jason created at 2008-08-27 12:20:19

uh, as per mabshoff's request that I post something here, that last patch that he merged fixing the doctest looks reasonable, but I haven't actually applied it or doctested it or anything.
