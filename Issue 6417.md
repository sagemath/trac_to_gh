# Issue 6417: Unicode in LaTeX

Issue created by migration from https://trac.sagemath.org/ticket/6417

Original creator: mora

Original creation time: 2009-06-25 21:53:59

Assignee: cwitty

Keywords: unicode LaTeX

In a %latex cell I couldn't use any accentuated letter. I had to write \"o to get ö.

Using this patch I can write unicode characters directly. For example Hungarian chars:

 http://www.math.bme.hu/~morap/sage_unicode_latex.png

This feature is important because most of the world uses more than the first 128 characters of ANSII.


---

Attachment


---

Comment by jhpalmieri created at 2009-06-27 17:36:56

Looks good to me except that it doesn't pass doctests.  Apply the patch at #6434 and you're good to go.

So this patch depends on #6434; modulo that, positive review.


---

Comment by rlm created at 2009-07-03 18:47:56

`sage -t  "devel/sage-main/sage/misc/latex.py"` fails after applying this patch.


---

Comment by jhpalmieri created at 2009-07-03 20:42:27

> sage -t "devel/sage-main/sage/misc/latex.py" fails after applying this patch.

As my comment says, doctests don't pass until you apply the patch at #6434.  Once #6434 gets in, this one is ready to go.  Is there some way to label this besides "positive review" to indicate this?


---

Comment by rlm created at 2009-07-04 00:43:05

Replying to [comment:4 jhpalmieri]:
> > sage -t "devel/sage-main/sage/misc/latex.py" fails after applying this patch.
> 
> As my comment says, doctests don't pass until you apply the patch at #6434.

My bad, wasn't paying enough attention.


---

Comment by rlm created at 2009-07-04 00:58:47

Resolution: fixed


---

Comment by mvngu created at 2009-07-05 02:07:08

See #6464 for a related issue. It concerns Unicode in Notebook worksheets.
