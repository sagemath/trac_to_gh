# Issue 3385: plot_vector_field does not deal with aspect ratios correctly

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2008-06-08 23:22:38

Assignee: was

As [reported to sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/8f409c06fc3a291c), `plot_vector_field()` does not change the angle of the arrows as appropriate for the aspect ratio.

To see this, take [this `@`interact demo](http://wiki.sagemath.org/interact/diffeq#head-f79d3195e10d507bda57064c8b8d10d15e55a5e4) and change `xmin` to 1/4. The plotted solution is correct, but the angles of the arrows for the vector field aren't changed correctly. (Also see https://www.sagenb.org/home/pub/1794/, if it's actually loading.)


---

Comment by mhansen created at 2008-09-03 01:05:30

Changing status from new to assigned.


---

Comment by mhansen created at 2008-09-03 01:05:30

Changing assignee from was to mhansen.


---

Comment by jason created at 2008-09-12 05:08:58

From the quiver documentation:

```
    In all cases the arrow aspect ratio is 1, so that if *U*==*V* the
    angle of the arrow on the plot is 45 degrees CCW from the *x*-axis.
```


Basically, if you want the arrows to match up with the axes in the plot, you *must* have aspect_ratio=1. (that is, unless the arrows are horizontal or vertical :).


---

Comment by jason created at 2008-09-12 05:11:19


```
[23:03] <jason> okay, so basically vector plots are junk unless you plot it with aspect_ratio=1
[23:03] <jason> This is *very* good to know.
[23:05] <mhansen> If I get bored, I may change it to use actual arrows.
[23:06] <jason> You could use my new arrow class :)
[23:06] <mhansen> Yep
[23:06] <jason> well, you've probably got enough on your plate to not get bored for a while
[23:06] <jason> for now, I think we ought to change the plot_vector_field and plot_slope_field documentation
[23:06] <jason> to put a huge warning in there that these plots must be plotted with aspect_ratio=1 to make any sense
[23:07] <jason> And maybe also to issue a warning when actually drawing a plot if it's not aspect_ratio=1
```



---

Comment by jason created at 2008-09-19 01:17:49

Wow, ask and ye shall receive!  In response to a query on the matplotlib list, efiring (on the matplotlib team) added an 'angles' keyword that allows us to have arrows that are scaled to respect the aspect ratio:

http://matplotlib.svn.sourceforge.net/viewvc/matplotlib/trunk/matplotlib/lib/matplotlib/quiver.py?r1=6067&r2=6112&pathrev=6112

So I guess the problem is pretty much solved if we update to matplotlib svn.


---

Comment by jason created at 2008-09-19 01:18:13

That is a keyword argument to the matplotlib quiver command.


---

Comment by jason created at 2008-09-20 19:20:44

I updated the matplotlib spkg to matplotlib-0.98.3.p2.spkg to include the SVN version of quiver.py that adds this keyword.  Everything seems to work great and tests pass in the plot directory.

The new spkg is at http://sage.math.washington.edu/home/jason/matplotlib-0.98.3.p2.spkg

This spkg needs to be installed before the attached patch is applied.


---

Attachment


---

Comment by mhansen created at 2008-10-02 02:10:56

Nice work Jason! +1


---

Comment by jason created at 2008-10-02 02:13:36

Thanks!  efiring on the matplotlib team did the real work, though; he deserves the thanks.


---

Comment by ddrake created at 2008-10-02 02:16:11

I see mhansen already reviewed this, but as I was the first to complain, I feel like I should too. :)

I am embarrassed to admit, though, that I don't know how to install the manually-downloaded `.spkg` file. I know it's just a `tar.bz2` file and so on, but what's the proper way to install it?


---

Comment by jason created at 2008-10-02 02:20:46

Dan,

Just do "sage -f <file-name>.spkg"

That forces an install of the spkg.


---

Comment by jason created at 2008-10-02 02:36:29

To answer some inquiries about patch conflicts, this patch depends on #4103 (in 3.1.3alpha0) and #4104 (in 3.1.3alpha0), in that order.

Sorry for not noting that.


---

Comment by mabshoff created at 2008-10-02 08:32:30

Resolution: fixed


---

Comment by mabshoff created at 2008-10-02 08:32:30

Merged in Sage 3.1.3.alpha3
