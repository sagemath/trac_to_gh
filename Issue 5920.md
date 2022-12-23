# Issue 5920: Implements view(object, format='pdf')

Issue created by migration from https://trac.sagemath.org/ticket/5920

Original creator: nthiery

Original creation time: 2009-04-28 19:35:58

Assignee: nthiery

CC:  sage-combinat

Keywords: latex view

This patch allows for:

```
sage: view(object, format = "pdf")
```


Typical use cases:
 - you prefer your pdf browser
 - view latex snippets which are not displayed in dvi viewers (e.g. tikzpicture)

Should this use 'output=' rather than 'format='

Potential extensions: `view(object, format='png')`, `view(object, format='html')`


---

Comment by nthiery created at 2009-04-28 19:40:58

Changing keywords from "latex view" to "view, latex, dvi, pdf".


---

Comment by was created at 2009-04-28 22:44:01

It should be 

```
sage: view(object, viewer='pdf')
```

for consistency with all the 3d plotting code, which has viewer='tachyon' and viewer='jmol' options.


---

Comment by mabshoff created at 2009-04-28 23:13:57

Replying to [comment:4 was]:
> It should be 
> {{{
> sage: view(object, viewer='pdf')
> }}}
> for consistency with all the 3d plotting code, which has viewer='tachyon' and viewer='jmol' options.

Hmm, how can you give this a positive review in light of this comment? I would much rather have the trivial rename in the original patch before merging it.

Cheers,

Michael


---

Comment by nthiery created at 2009-04-28 23:36:09

Done in the new update patch. I switched back to needs review, though a quick glance from any of the two of you should do.


---

Comment by AlexGhitza created at 2009-04-29 00:10:17

Looks good.


---

Comment by nthiery created at 2009-04-29 06:46:39

Replying to [comment:10 was]:
Which work does it still need?


---

Comment by mabshoff created at 2009-04-29 11:14:23

Replying to [comment:11 nthiery]:
> Replying to [comment:10 was]:
> Which work does it still need?

This had a positive review by Alex since you addressed William's concern. Why did you change that?

Reinstating positive review.

Cheers,

Michaell


---

Comment by nthiery created at 2009-04-29 21:34:22

Replying to [comment:12 mabshoff]:
> This had a positive review by Alex since you addressed William's concern. Why did you change that?

William changed that, and that's precisely what I was puzzled about.

> Reinstating positive review.

Thanks.


---

Comment by mabshoff created at 2009-04-30 07:18:26

This one needs a rebase post 3.4.2:

```
sage-3.4.2.rc0/devel/sage$ hg import trac_5920_view_as_pdf-5920-nt.patch 
applying trac_5920_view_as_pdf-5920-nt.patch
patching file sage/misc/latex.py
Hunk #1 succeeded at 894 with fuzz 2 (offset 369 lines).
Hunk #4 FAILED at 575
1 out of 6 hunks FAILED -- saving rejects to file sage/misc/latex.py.rej
abort: patch failed to apply
```

Once the rebase has been done the positive review can be reinstated [assuming doctests pass obviously ;)].

Cheers,

Michael


---

Comment by nthiery created at 2009-04-30 17:29:43

Replying to [comment:14 mabshoff]:
> This one needs a rebase post 3.4.2:

Done

Pfiew. The workflow overhead has been large on this patch ...


---

Comment by nthiery created at 2009-04-30 17:35:50

Oops, please ignore the updated patch for a second


---

Attachment


---

Comment by nthiery created at 2009-04-30 17:42:38

Replying to [comment:16 nthiery]:
> Oops, please ignore the updated patch for a second

Finally good to go!


---

Comment by mabshoff created at 2009-04-30 22:47:37

Marked as needing review again, i.e. that it applies and passes doctests.

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-05-01 00:24:46

It applies cleanly to 3.4.2.rc0, passes doctests, and does what it should when I try it out.


---

Comment by mabshoff created at 2009-05-01 04:47:23

Replying to [comment:15 nthiery]:

> Pfiew. The workflow overhead has been large on this patch ...

Yeah, given the amount of code this didn't go as smoothly as it should have :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-07 07:09:55

Merged in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-07 07:09:55

Resolution: fixed
