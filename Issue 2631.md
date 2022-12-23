# Issue 2631: Distinguishing between (un)evaluated  cells

Issue created by migration from https://trac.sagemath.org/ticket/2631

Original creator: dunfield

Original creation time: 2008-03-21 16:06:47

Assignee: boothby

There should be a visual distinction between input cells which have been evaluated and those that have not, and also to indicate when a previously evaluated cell has been edited and thus the (apparent) output is not actually the output of the input cell (cf Mathematica's behavior on this). A simple way to do this would be to change the color of evaluated input cells to blue, or to change the color of the boarder of input box.  One reason to do this is that it is difficult to tell if you have evaluated a cell whose contents don't return anything (e.g. "a = 1+2").


---

Comment by was created at 2008-03-21 18:55:59

> There should be a visual distinction between input cells 
> which have been evaluated and those that have not, 

There already is such a distinction!  Unevaluated cells have
a red line to the left of them.  Maybe this isn't clear enough?
Or maybe it is once one knows about it.

> also to indicate when a previously evaluated cell 
> has been edited and thus the (apparent) output is 
> not actually the output of the input cell (cf Mathematica's behavior on this).

This is a good idea.  Note that having a cell such that "previously evaluated cell 
has been edited and thus the (apparent) output is  not actually the output of the input cell" was only first added to Sage (by Boothby) I think in 2.10.4 (I just
noticed it has a massive bug in it too).  What does Mathematica do?


---

Comment by dunfield created at 2008-03-21 19:22:23

> There already is such a distinction! Unevaluated cells have a red line to the left of them. Maybe this isn't clear enough? Or : maybe it is once one knows about it.

Now that you mention them, I do see these red lines when I load up an old worksheet.   But they don't appear when new input cells are created, which is a bug, I think.   I was working with fresh worksheets since I've only just started using the notebook, so I didn't see the red lines.

Now that I do see the red lines, I think they're too subtle and a little "busy".  I'd suggest changing the color of the input cell frame to red instead --- it would be hard to miss that.

> What does Mathematica do?

On evaluation, Mathematica labels the input and output cells by "In[n] :=" and "Out[n] :=" so you can refer to the output later.  When you start editing a previously evaluated input cell, the "In" and "Out" disappear.   For Sage, you could just have the red line/box reappear if the user starts editing a cell (but not if they simply select it, move the cursor around, but don't actually edit).


---

Comment by boothby created at 2020-03-29 02:12:30

Resolution: invalid


---

Comment by boothby created at 2020-03-29 02:12:30

Closing deprecated notebook tickets
