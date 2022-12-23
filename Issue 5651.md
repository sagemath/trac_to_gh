# Issue 5651: make it so plot(...) passes extra options to show (maybe only those that makes sense)

Issue created by migration from https://trac.sagemath.org/ticket/5651

Original creator: was

Original creation time: 2009-03-31 20:33:43

Assignee: wcauchois

CC:  wcauchois was jason

This works now:

```
plot(sin(x^2),(x,-3,3)).show(figsize=[8,2])
```


This would be nice:

```
plot(sin(x^2),(x,-3,3),figsize=[2,8])
```


The analogue of the above works systematically everywhere for 3d plotting.


---

Comment by was created at 2009-04-28 21:16:42

This is really awesome.  However, things like this should work too:

```
sage: line([(0,1), (3,4)],figsize=[10,2])
Traceback (most recent call last):
...
RuntimeError: Error in line(): option 'figsize' not valid.
```


Also, this should have gridlines:

```
plot(sin(x^2),(x,-3,3),gridlines=True) + plot(cos(x^2),(x,-3,3))
```


Clarify the comment

```
# If you add parameters to show(), you should update the code below. 
```

}}}


---

Comment by wcauchois created at 2009-05-11 22:33:25

Now it works for everything, ever!! With doctests too.


---

Comment by was created at 2009-05-12 21:12:29

Positive review modulo making so consistent with 3d plotting:

```
sphere((0,0,0),1, aspect_ratio=[1,4,7]) + sphere((1,1,1),1, aspect_ratio=[1,1,1])
```


Note that it is the *rightmost* thing that has precedence.   Otherwise positive review.


---

Attachment


---

Comment by wcauchois created at 2009-05-14 03:29:15

William,
I fixed the precedence issue.


---

Comment by mabshoff created at 2009-05-15 07:42:53

This one needs to be rebased due to a doctest merge conflict in arrow.py. On top of that: this is a diff, so please make sure you post a proper patch this time.

```
mabshoff@sage:/scratch/mabshoff/sage-4.0.alpha0/devel/sage$ patch -p1 --dry-run < trac_5651.patch 
patching file sage/plot/arrow.py
Hunk #1 FAILED at 310.
1 out of 1 hunk FAILED -- saving rejects to file sage/plot/arrow.py.rej
patching file sage/plot/bar_chart.py
patching file sage/plot/bezier_path.py
<SNIP>
```

Note that various doctest patches in plot/* are going into 4.0.alpha0, so please rebase post 4.0.a0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-15 07:48:47

Note that with #6006, #6023 and #6030 applied there are two more small rejects.

Cheers,

Michael


---

Comment by wcauchois created at 2009-05-22 06:44:48

I rebased the patch on Sage 4.0.rc0. As far as I could tell, the doctest failures I encountered were not related to this patch. My apologies for posting a diff beforehand, I'm still learning the idiosyncracies of Mercurial Queues :).


---

Comment by mhansen created at 2009-06-01 06:19:36

Hi Bill,

I tried applying this to 4.0 and got a bunch of failures.  I can probably rebase it later this evening.


---

Comment by wcauchois created at 2009-06-01 07:55:54

I would appreciate that mhansen, thanks!


---

Comment by wcauchois created at 2009-07-01 20:44:41

I added a new rebase, so if someone could review this then we can finally get this functionality into Sage.

I feel like I did a little bit of a dirty thing with the new linkmode parameter, which was added somewhere along the line. linkmode is intended to be consumed by show() before the keywords are passed onto save(), so I just popped it from the keyword dict at the beginning of the function.


---

Comment by wcauchois created at 2009-07-01 20:48:29

based on sage 4.1.alpha2 (fixed, whoops)


---

Attachment

The rebased patch applies fine to my 4.1 tree.  I tried a few examples and ran the doctests in plot/*.py[x] and plot/plot3d/*.py[x] and everything seems fine.  I'm giving a positive review to the rebasing. That combined with William's almost positive review above adds up to a positive review.

I also looked at the code and it looked reasonable.

Thanks and good work!


---

Comment by mvngu created at 2009-07-19 08:27:20

Resolution: fixed


---

Comment by mvngu created at 2009-07-19 08:27:20

Merged `trac5651-rebase.patch`. That rebased patch contains doctrings that doesn't conform with conventions for formatting docstrings. In particular, in `sage/plot/bar_chart.py`:

```
131	    Extra options will get passed on to show(), as long as they are valid:
```

In `sage/plot/bezier_path.py`:

```
171	    Extra options will get passed on to show(), as long as they are valid:
```

In `sage/plot/matrix_plot.py`:

```
58	    Extra options will get passed on to show(), as long as they are valid:
62	    Extra options will get passed on to show(), as long as they are valid:
```

In `sage/plot/polygon.py`:

```
255	    Extra options will get passed on to show(), as long as they are valid:
```

These issues should be addressed in another enhancement ticket.


---

Comment by mvngu created at 2009-07-20 20:56:00

See #6573 for an enhancement ticket.
