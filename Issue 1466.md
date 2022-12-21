# Issue 1466: improve the "click to the left" aspect of the notebook

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-12 06:22:38

Assignee: boothby

CC:  mpatel


```
Aha!  Great!

This reminds we that when I started using the notebook interface, it
took me an embarrassingly long time to discover what was meant by the
phrase
'click to the left for traceback'.  I found this message confusing
because there is nothing to the left to click on.  At first I thought
this was a strange way
of saying `left-click'.  Eventually I worked it out by accident.  I
suggest a more verbose message along the lines of
`for traceback, click in the blank area just to the left of this
line'.  Or put something to click on, maybe along the lines of the
brackets in
the mathematica notebook, which has a hierarchical grouping mechanism
whereby groups of cells can be hidden or expanded together.
(Of course maybe sage does too, and I just don't know about it!)

Cheers,

Peter
```



---

Comment by timdumol created at 2009-11-15 15:41:16

Makes the traceback message: "click to the left of this block for traceback" instead.


---

Attachment

In case anyone considers this confusing enough, this patch makes the error message slightly more verbose.


---

Comment by timdumol created at 2009-11-15 15:41:57

Changing status from new to needs_review.


---

Comment by awebb created at 2009-11-19 15:47:22

Seems to work as described and is a bit more clear to read. ~ Adam


---

Comment by awebb created at 2009-11-19 15:47:22

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-11-19 21:39:56

merge into sagenb-0.4.4


---

Comment by was created at 2009-11-19 21:39:56

Resolution: fixed
