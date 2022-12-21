# Issue 6162: plot_histogram improvments

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2009-05-30 22:16:10

Assignee: tbd

CC:  cswiercz

Since R's histogram plotting is not working for me, I added some functionality to dft.py's plot_histogram method for IndexedSequences.
Hope this is useful to other.


---

Attachment

based on 4.0.rc1


---

Comment by wdj created at 2009-05-31 01:42:42

This passes sage -testall on an amd64 ubuntu 9.04 machine.


---

Comment by wdj created at 2009-06-01 03:03:18

Changing component from algebra to graphics.


---

Comment by wdj created at 2009-06-01 03:03:18

Changing assignee from tbd to was.


---

Comment by wdj created at 2009-06-01 03:03:18

Changing priority from major to minor.


---

Comment by ncalexan created at 2009-06-15 19:06:39

Original patch was not great; this one is more configurable, fixes a bug in the plot command, and fixes some of the zillion typos throughout.

wdj, ispell-comments-and-strings in emacs is your friend.  That and flyspell-mode.


---

Comment by ncalexan created at 2009-06-15 19:06:39

Changing keywords from "" to "plot histogram".


---

Attachment

Thanks Nick!

Should I review your patches or does someone other than the 2 of us review both patches?


---

Comment by cswiercz created at 2009-06-23 16:21:25

Nick,

I have very bad luck with your patches. :( Is `trac_6162-plotting.patch` also based on 4.0.rc1? I tried applying it to 4.0.2 after successfully applying `trac_6162-histogram.patch` and I received the following error:


```
sage: hg_sage.apply("trac_6162-plotting.patch")
cd "/home/cswiercz/sage/devel/sage" && hg status
cd "/home/cswiercz/sage/devel/sage" && hg status
cd "/home/cswiercz/sage/devel/sage" && hg import   "/home/cswiercz/trac_6162-plotting.patch"
applying /home/cswiercz/trac_6162-plotting.patch
patching file sage/gsl/dft.py
Hunk #2 FAILED at 52
Hunk #3 FAILED at 156
2 out of 4 hunks FAILED -- saving rejects to file sage/gsl/dft.py.rej
abort: patch failed to apply
```


This was done on a local sage.math install. I wonder if there were changes to `sage/gsl/dft.py` between the two versions...

I don't have a 4.0.rc1 install anywhere so I'll have to get that up and running in order to review.


---

Comment by ncalexan created at 2009-06-23 16:37:38

Replying to [comment:7 cswiercz]:
> Nick,
> 
> I have very bad luck with your patches. :( Is `trac_6162-plotting.patch` also based on 4.0.rc1? I tried applying it to 4.0.2 after successfully applying `trac_6162-histogram.patch` and I received the following error:

Sorry, I wasn't clear.  Apply *only* `-histogram.patch`.


---

Comment by cswiercz created at 2009-06-23 20:19:05

Replying to [comment:8 ncalexan]:
> Sorry, I wasn't clear.  Apply *only* `-histogram.patch`.

Perhaps I don't understand the difference between a histogram of a set of values and a histogram of an _indexed_ set of values but it seems to me that the following should output the familiar "bell-shaped" distribution:

```
sage: J = [ZZ(n) for n in range(10^3)]
sage: A = [RR(gauss(0,1)) for n in range(10^3)]
sage: s = IndexedSequence(A,J)
sage: P = s.plot_histogram()
```


However, this looks pretty much the same as

```
sage: Q = s.plot()
```


Also, the following is closer to the bell curve but it still doesn't capture what's going on: (swapping the `IndexedSequence` inputs)

```
sage: t = IndexedSequence(J,A)
sage: R = t.plot_histogram()
```


I'm just wondering if I'm missing something.

Finally, `finance.timeseries.TimeSeries` has a `plot_histogram` method that seems to work pretty well. Maybe you can use it somehow? Anyway, those are just my thoughts. Again, if I'm missing something I'll be happy to take another look.


---

Comment by wdj created at 2009-06-23 20:45:21

I don't know why you expect your example to look like a bell curve.
In any case, there are too many points for plot_histogram to work with your example. Try


```
sage: J = [ZZ(n) for n in range(10)]
sage: A = [RR(gauss(0,1)) for n in range(10)]
sage: s = IndexedSequence(A,J)
sage: P = s.plot_histogram()
sage: show(P)
```

Regarding your suggestion to use , I get:


```
sage: import finance.timeseries.TimeSeries
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

....
```

Can you be more specific?


---

Comment by wdj created at 2009-06-24 08:24:38

Now I see what you meant.

I think you meant to compare the following plots:


```
sage: J = [ZZ(n) for n in range(10)]
sage: A = [RR(gauss(0,1)) for n in range(10)]
sage: s = IndexedSequence(A,J)
sage: s.plot_histogram()
sage: t = finance.TimeSeries(A); t
[0.6636, 0.7983, -0.1451, 0.0838, -0.4355, -0.5719, 0.2572, 1.2802, -1.2696, -0.0642]
sage: t.plot_histogram()
```

If so, you can see that they are completely different. I don't see how to use the `sage/finance/time_series.pyx`
for this purpose.


---

Comment by cswiercz created at 2009-06-24 17:32:11

Using your example, I'm just curious is there's any difference between the following two plots: (aside from the default red indexing below each bar in the plot)


```
sage: J = [ZZ(n) for n in range(10)]
sage: A = [RR(gauss(0,1)) for n in range(10)]
sage: s = IndexedSequence(A,J)
sage: s.plot_histogram()
sage: bar_chart(s.list())
```


The only difference I can see is bar placement. (The indexing set easily allows you to place the bars in `IndexedSequence().plot_histogram()` wherever you like.) I'm sure that there's a lot of application for kind of plot with an indexed set.

I tested the functionality of your code and, from my observations, it works great! Therefore, I give it a positive review. I just wanted a little bit of clarification on what kind of information the `plot_histogram()` method was actually presenting.

Sorry if my questions caused too much of a problem.


---

Comment by wdj created at 2009-06-24 23:39:59

Thanks for the link to {{{bar_chart}}. It is similar, except that plot_histogram has an option which allows you to vary the thickness of the bars. 

These "improvements" to the `plot_histogram` function are used to present a histogram of the aggregate totals in a course, especially for a multiple-choice machine-graded exam. Boring but the specific format was required for what I was trying to do.


---

Comment by boothby created at 2009-06-26 17:42:07

Resolution: fixed


---

Comment by mvngu created at 2009-07-12 04:09:35

Merged `trac_6162-histogram.patch` in sage-4.1.alpha2. That is David Joyner's patch, and it is now changeset 12600:c169b5109084.
