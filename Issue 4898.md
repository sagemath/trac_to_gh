# Issue 4898: [with patch; needs review] Add style and labels to contour_plot()

Issue created by migration from https://trac.sagemath.org/ticket/4898

Original creator: abergeron

Original creation time: 2008-12-31 21:49:27

Assignee: abergeron

CC:  wcauchois jason

This patch add the option of styling lines, either individually or all at once, and adding contour level labels.

Another one is coming to support this in combination with #2770.


---

Comment by abergeron created at 2008-12-31 22:02:04

I think it would just be better to wait until #2770 and #4884 are merged since they conflict with this.  I'll post an updated patch then.


---

Attachment

Update patch is posted.  Start reviewing!


---

Comment by abergeron created at 2009-01-24 05:02:25

Changing status from new to assigned.


---

Comment by jason created at 2009-02-11 05:33:13

What was this updated to?  I get conflicts applying it to 3.3alpha3.


---

Comment by jason created at 2009-02-11 06:44:49

I tried applying it to 3.3rc0:


```
jason@sage:~$ patch contour_plot.py < trac_4898.patch 
patching file contour_plot.py
Hunk #2 FAILED at 53.
Hunk #3 FAILED at 75.
Hunk #4 FAILED at 136.
Hunk #5 succeeded at 167 (offset -1 lines).
Hunk #6 succeeded at 180 (offset -1 lines).
Hunk #7 FAILED at 226.
Hunk #8 succeeded at 272 (offset -2 lines).
Hunk #9 succeeded at 293 (offset -2 lines).
Hunk #10 succeeded at 308 (offset -2 lines).
Hunk #11 succeeded at 317 (offset -2 lines).
Hunk #12 succeeded at 345 (offset -2 lines).
4 out of 12 hunks FAILED -- saving rejects to file contour_plot.py.rej
```



---

Comment by jason created at 2009-05-30 08:27:07

abergeron: what is the status of your work on this patch (and how can we help?)  It looks like it is very useful.  Thanks for doing this!


---

Comment by abergeron created at 2009-05-31 02:48:02

It is on my TODO list (which is rather long) and which I started attacking since the end of my finals.

I don't have a recent version of Sage on my machine right now so it'll be a couple of days before I can rebase it.

If somebody else wants to do it in the meantime, that could help.


---

Comment by kcrisman created at 2009-10-05 20:24:53

Here is a somewhat significant rebase based on 4.1.2.alpha2, also more or less ReSTified.  There have been some definite changes in this file and matplotlib since then, so a few things now behave slightly differently from the original patch; however, I think they are just different, not wrong (especially when it comes to axes).   In particular I hope I got the option popping in the right spots.

Great thanks to Arnaud's work here - especially labeling contours is a great thing to have now!


---

Comment by jason created at 2009-10-06 20:52:35

Changing status from needs_review to needs_work.


---

Comment by jason created at 2009-10-06 20:52:35

Unfortunately, it still needs more rebasing.  Here is the result of applying it to 4.1.2.rc0:


```
jason@sage:~/sage-4.1.2.rc0-sage.math.washington.edu-x86_64-Linux/devel/sage/sage$ hg qpush
applying trac_4898-contour-labels-rebase.patch
patching file sage/plot/contour_plot.py
Hunk #11 succeeded at 517 with fuzz 1 (offset 3 lines).
Hunk #12 FAILED at 549
1 out of 12 hunks FAILED -- saving rejects to file sage/plot/contour_plot.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh trac_4898-contour-labels-rebase.patch
```


I'm excited for this to get in!


---

Attachment

Based on 4.1.2.rc1.alpha3


---

Comment by kcrisman created at 2009-10-08 02:41:03

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2009-10-08 02:41:03

Hmm, I had intended to delete the previous version...

Anyway, there was a one-character (in fact, one space) thing that prevented it from applying.  So silly.  It should actually apply to rc0 as well, I suspect, but you never know... anyway, can you check that if the only issue is a space, that you fix it manually to at least see if doctests pass?


---

Attachment

Based on 4.2 - apply only this!


---

Comment by jason created at 2009-11-10 16:50:08

I tweaked two of the defaults and add a bit more documentation.  This is great; I'm excited to see this go in!


---

Comment by jason created at 2009-11-10 16:50:08

Changing status from needs_review to positive_review.


---

Attachment

apply on top of previous patch


---

Comment by mhansen created at 2009-11-12 06:53:24

Resolution: fixed
