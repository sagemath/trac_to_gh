# Issue 6875: [with patch, needs review] fill option is broken for polar_plot

Issue created by migration from Trac.

Original creator: whuss

Original creation time: 2009-09-03 11:03:40

Assignee: was

Keywords: polar_plot, fill

The fill option for polar_plot does not work correctly anymore.

The following two doctests don't produce the supposed output:

* Fill the area between two functions:

```
sage: polar_plot(cos(4*x) + 1.5, 0, 2*pi, fill=0.5 * cos(4*x) + 2.5, fillcolor='orange').show(aspect_ratio=1)
```


* Fill the area between several spirals:

```
sage: polar_plot([(1.2+k*0.2)*log(x) for k in range(6)], 1, 3 * pi, fill = {0: [1], 2: [3], 4: [5]})
```


This regression has been introduced with the changeset 12287 (Ticket: #5930).

Sage really needs a test framework for plots. Otherwise more and more regressions will creep in, without anybody noticing.



---

Attachment


---

Comment by jason created at 2009-09-15 09:14:45

It still doesn't seem like the first example above works for me---I get a single solid figure.  Is it supposed to have a band around it's edge?


---

Attachment

The correct output of the first example


---

Attachment

The correct output of the second example


---

Comment by whuss created at 2009-09-15 09:22:58

Replying to [comment:1 jason]:
> It still doesn't seem like the first example above works for me---I get a single solid figure.  Is it supposed to have a band around it's edge?

I've attached two images with the correct output of the two examples.
Is this what you get with the patch?


---

Comment by jason created at 2009-09-15 15:08:30

I compiled a fresh version of 4.1.1.alpha1 overnight, and everything seems to work on that.  So positive review!

(Note to everyone else: the functions above were already in the doctests, but just were not working).

I wish this would have been working last week when I taught finding areas in polar coordinates! I'm glad you found the fix.


---

Comment by mvngu created at 2009-09-15 23:30:12

Merged `trac_6875_fill_regression.patch`.


---

Comment by mvngu created at 2009-09-15 23:30:12

Resolution: fixed
