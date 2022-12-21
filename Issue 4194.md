# Issue 4194: pylab plots cut off

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-09-25 10:21:00

Assignee: was

CC:  mvgnu mhansen jason

Keywords: plot

On Thursday 25 September 2008, Stan Schymanski wrote on [sage-support]:
> Dear all,
>
> When I upgraded to 3.1.2, I found that some of my plots generated
> using pylab in the notebooks miss their bottom bits. It seems to be
> related to the dpi setting. Example:

```
import pylab
x1 = srange(0,1.1,0.01)
d1 = [2*x+x^2 for x in x1]
pylab.clf() # clear the figure first
pylab.figure(1)
pylab.plot(x1,d1, label="d1")
pylab.ylabel("$f(x)$") # label the axes
pylab.xlabel("$x$")
pylab.savefig('foo.png',dpi=72) # fire!
```

> If I leave the "dpi=72" out in the last line, the plot is larger and
> complete. This problem did not occur in sage 3.1.1, so I assume that
> it is a bug.


---

Comment by mhansen created at 2008-09-27 00:36:42

This is because matplotlib doesn't like the Sage Integer 72.  If you change the 72 to int(72), then things work.  We should probably write an email to the matplotlib mailing list asking them how hard it would be to make it play nicely with Sage types.

We also encounter similar issues with numpy and scipy.


---

Attachment

To release manager:
This now works, given #5448 (and possibly earlier).

```
sage: import pylab
sage: x1 = srange(0,1.1,0.01)
sage: d1 = [2*x+x^2 for x in x1]
sage: pylab.clf() # clear the figure first
sage: pylab.figure(1)
<matplotlib.figure.Figure object at 0x16d41d0>
sage: pylab.plot(x1,d1, label="d1")
[<matplotlib.lines.Line2D object at 0x102ceb0>]
sage: pylab.ylabel("$f(x)$") # label the axes
<matplotlib.text.Text object at 0x4413f0>
sage: pylab.xlabel("$x$")
<matplotlib.text.Text object at 0x1038890>
sage: pylab.savefig('foo.png',dpi=72)
```

foo.png is attached.


---

Comment by jason created at 2009-09-29 16:05:03

kcrisman says this works now, so should be closed.


---

Comment by jason created at 2009-10-01 03:49:55

Don't close this.

Something really, really weird is going on.

In a fresh Sage session (not even in the notebook, just in a Sage console session), running the following (simplified from above) code produces png that is cut off which is about 12K:


```
import matplotlib.pyplot as plt
import numpy
plt.figure()
plt.plot(numpy.arange(0,1.1,0.01))
plt.savefig('foo.png',dpi=72) # fire!
```


However, immediately saving the figure again using `plt.savefig('foo.png',dpi=72)` writes a 13K file which is not cut off.

Doing the same test with sage -python yields the correct figure the first time.  Doing the same test with the system python yields the correct figure the first time.  This is with the matplotlib 0.99.1 spkg installed.


---

Comment by jason created at 2009-10-01 16:35:31

I've posted to the matplotlib-user mailing list today about this issue.


---

Comment by ryan created at 2011-01-11 04:00:51

With sage 4.6.0 it is still cut off (matplotlib 1.0.0)


---

Comment by ryan created at 2011-01-11 04:23:19

for those interested, here is the matplotlib-users discussion

http://sourceforge.net/mailarchive/forum.php?thread_name=6e8d907b0910061125o4f93bfb4u2ec934042c057ddd%40mail.gmail.com&forum_name=matplotlib-users


---

Comment by ryan created at 2011-01-11 05:31:05

workaround for matplotlib 1.0.0 bug


---

Comment by ryan created at 2011-01-11 05:33:10

Changing status from new to needs_review.


---

Attachment

according to the matplotlib-users discussion, the issue arises because the file is not flushed before being closed.  This patch correctly opens, writes and most importantly flush the file before closing.

The bug still appears to exist upstream.


---

Comment by ryan created at 2011-01-11 06:04:11

Changing status from needs_review to needs_work.


---

Comment by ryan created at 2011-01-11 06:16:28

see #10588.  Upgrading to matplotlib 1.0.1 should fix the issue


---

Comment by jason created at 2011-10-18 18:25:30

Resolution: fixed


---

Comment by jason created at 2011-10-18 18:25:30

Indeed, this is now fixed.
