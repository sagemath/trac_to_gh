# Issue 6591: Implement view(object, viewer='pdf') and view(object, tightpage = True)

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-07-22 14:38:27

Assignee: was

CC:  sage-combinat rbeezer fidelbarrera jhpalmieri

This small patch implements:

```
sage: view(object, viewer = "pdf")
```

which works even under the notebook.

Typical use cases:

    * you prefer your pdf browser to your dvi browser
    * you want to view latex snippets which are not displayed well in dvi viewers or jsmath (e.g. tikzpicture) 

Potential extensions: view(object, viewer='png'), view(object, viewer='html') 

This partially reinstates #5920 which got a positive review and was said to be merged and closed, but apparently later discarded upon the merge of the overlapping #6012 (pdflatex option)


This patch also adds a tightpage option, which uses the preview package to create a document with each displaymath on a single page whose size is exactly that of the displaymath. This is for example useful for very large pictures (graphs!) generated with tikz.


---

Comment by nthiery created at 2009-07-22 14:40:40

Changing assignee from was to nthiery.


---

Comment by nthiery created at 2009-07-22 14:41:05

Changing keywords from "" to "view, pdflatex, tightpage, tikz".


---

Comment by jhpalmieri created at 2009-07-22 21:47:12

Everything works as advertised, both from the command-line and the notebook (except that tightpage=True has no effect in the notebook if viewer is None).  I would give it a positive review except that the new options aren't documented at all.  I'm attaching a patch with documentation; if you're happy with it, the whole thing can get a positive review.

I have no idea how to doctest this, by the way...


---

Attachment

apply on top of the other patch


---

Comment by nthiery created at 2009-07-23 07:12:10

Replying to [comment:3 jhpalmieri]:
> Everything works as advertised, both from the command-line and the notebook (except that tightpage=True has no effect in the notebook if viewer is None).  I would give it a positive review except that the new options aren't documented at all.  I'm attaching a patch with documentation; if you're happy with it, the whole thing can get a positive review.
> 
> I have no idea how to doctest this, by the way...

Oops, sorry, I forgot about the doc ... Thanks!

In the meantime, I actually found a shortcoming in tightpage. I'll probably add a little fix later today.


---

Comment by nthiery created at 2009-07-23 21:23:53

I folded the patches together, and fixed the shortcoming in tightpage (using displaymath did put a limit on the width of the page). I also updated and reedited a bit the documentation.
Btw: I am wondering whether the description of what happens in notebook mode should not go first.


---

Comment by nthiery created at 2009-07-23 21:28:40

Apply only this one (it includes the doc patch)


---

Attachment

apply on top of the other patch


---

Attachment

Positive review.  A few very minor doc fixes added (for the change from `\LaTeX` to `LaTeX`, it seems that jsMath doesn't know about this command, so it doesn't look good in the notebook with #5653 applied).

Apply patches trac_6591_view_viewer_tightpage-nt.patch and trac_6591-doc2.patch.

I think it's fine to leave the description of notebook mode second; it would take actual thought to change it at this point.  When I worked on this docstring a while ago, my feeling was that since most of the options are ignored in notebook mode, command-line mode should come first.


---

Comment by nthiery created at 2009-07-24 07:39:02

Thanks John! That was quick. Time difference is a good thing :-)


---

Comment by mvngu created at 2009-07-24 21:57:46

Resolution: fixed
