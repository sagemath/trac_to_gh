# Issue 4104: Create plot_slope_field function

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-09-12 04:15:51

Assignee: was

The attached patch adds a plot_slope_field function and also exposes a bit more of the quiver API to the vector field plotting routines.  I wish I had had this when I started teaching differential equations!


---

Attachment


---

Comment by jason created at 2008-09-12 04:16:37

This patch depends on #4103.


---

Comment by wdj created at 2008-09-13 12:54:24

It refused to apply for me:


```
wdj`@`hera:~/sagefiles/sage-3.1.2.alpha4$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: plot-slope
sage: hg_sage.apply("/home/wdj/sagefiles/plot_slope_field.patch")
cd "/home/wdj/sagefiles/sage-3.1.2.alpha4/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.2.alpha4/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.2.alpha4/devel/sage" && hg import   "/home/wdj/sagefiles/plot_slope_field.patch"
applying /home/wdj/sagefiles/plot_slope_field.patch
patching file sage/plot/plot.py
Hunk #1 FAILED at 2242
1 out of 2 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej
abort: patch failed to apply
```



---

Comment by jason created at 2008-09-17 16:17:02

wdj: just checking, did you apply #4103 first?  This patch depends on that one (i.e., it's supposed to be applied on top of that one).


---

Comment by wdj created at 2008-09-17 18:09:03

I just tried (to 3.1.2.alpha4) and the patch for #4103 would not apply. Could you rebase them both for 3.1.2? It is probably a mistake on my part and I hate to make you go to extra effort. 
Maybe someone else who doesn't have trouble can referee them easier?


---

Comment by jason created at 2008-09-18 04:26:59

I just applied both #4103 and this patch to 3.1.2final and they didn't give any errors.  It's quite possible that I was working from something later than alpha4.  Can you try them against 3.1.2final?

Thanks.


---

Comment by wdj created at 2008-09-18 13:59:04

This and #4103 apply to 3.1.2 and pass sage -testall. It does a great job and is a very valuable addition.

A question for possibly a future patch: it will not plot

```
plot_slope_field(x/y, (x,-3,3), (y,-3,3)).show(aspect_ratio=1)
```

because of the problem at y=0. However, should it? A slope of plus or minus infinity has a well-defined meaning. Should one try to trap singularities like that and just plot them as vertical direction fields in the future?

Anyway, thanks Jason for this nice addition! This will be very useful for teaching differential equations.


---

Comment by jason created at 2008-09-18 14:40:22

I'm aware of the problem, but decided to post the patch anyway when I saw that plot_vector_field had the same problem: the plot is blank when an evaluation is undefined.  I thought about trapping these things and plotting them as vertical lines, but really we ought to do something in plot_vector_field to take care of things when a vector has an infinite or NaN coordinate.  I ran out of time to fix plot_vector_field.


---

Comment by mabshoff created at 2008-09-19 03:14:04

Resolution: fixed


---

Comment by mabshoff created at 2008-09-19 03:14:04

Merged in Sage 3.1.3.alpha0
