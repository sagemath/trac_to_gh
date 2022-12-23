# Issue 4809: the installation guide and constructions guide should be CC licensed

Issue created by migration from https://trac.sagemath.org/ticket/4809

Original creator: ddrake

Original creation time: 2008-12-16 06:22:54

Assignee: tba

Our documentation should be clearly licensed.


```
15:09 < hampton|home> what is the license of the sage documentation?
15:09 < hampton|home> is it a type of creative commons?
15:11 < ddrake> hrm, I dunno. It should be, I think.
15:13 < ddrake> yep: by-sa
15:13 < ddrake> http://sagemath.org/doc/tut/node1.html
15:14 < hampton|home> that's the tutorial - are they are under that?
15:14 < hampton|home> the others don't have a notice I think
15:14 < ddrake> the installation guide and constructions don't have a notice
15:15 < ddrake> ref manual is attribution-sharealike
15:15 < ddrake> programming guide too
15:15 < hampton|home> cool, thanks
```



---

Comment by ddrake created at 2008-12-16 06:47:32

The attached patches license the constructions guide and installation guide as CC Attribution-Sharealike, which is the same as the other Sage documentation. Since David Joyner is listed as the/an author of both documents, I suppose he should approve or sign off on these patches.


---

Comment by wdj created at 2008-12-17 03:22:22

Actually, href will not work for a few reasons. 

(1)  The href (or whatever it's called) package is commented out, so it won't compile. 

(2) But I think the href latex package somehow conflicts with the Python doc latex package (?), and uncommenting it doesn't work either. (After moving to rest/sphinyx is this an issue?)

The solution is easy though - use \url{...} instead. It is used in other places in const.tex and inst.tex as well. If you just swap href with url it compiles fine and I'll give this a positive review.


---

Attachment


---

Attachment


---

Comment by ddrake created at 2009-04-14 01:32:20

Updated versions of the patches for the spinx-ified documentation.


---

Comment by jhpalmieri created at 2009-04-21 17:55:58

trac_4809_constructions.patch and trac_4809_installation.patch are ready to go: positive review.  Meanwhile, I can't find any license information for the tutorial, reference manual, or developer's guide.  Did they disappear in the Sphinx conversion?  Here's a new patch which adds them.  It also removes the line "Contents:" from various index.rst files -- if you produce a PDF from the docs, the table of contents is printed first, then whatever is in index.rst, so you would end up with an introduction followed by "Contents:", and then the rest of the page was blank.


---

Attachment


---

Comment by ddrake created at 2009-04-22 04:02:52

Changing assignee from tba to ddrake.


---

Comment by ddrake created at 2009-04-22 04:02:52

We should definitely license the rest of the documentation, too. Positive review to trac_4809_other.patch.

I'll also open a French version of this ticket. I'm sure I could cut and paste something into the French tutorial, but I'll let one of our Francophone developers handle that.

I'm changing the milestone to 3.4.2 since these are not big or invasive patches, and should get in as soon as possible.


---

Comment by ddrake created at 2009-04-22 04:02:52

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-04-24 04:55:08

Resolution: fixed


---

Comment by mabshoff created at 2009-04-24 04:55:08

Merged all three patches in Sage 3.4.2.alpha0.

Cheers,

Michael
