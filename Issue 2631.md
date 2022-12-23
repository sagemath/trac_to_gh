# Issue 2631: Distinguishing between (un)evaluated  cells

archive/issues_002631.json:
```json
{
    "body": "Assignee: boothby\n\nThere should be a visual distinction between input cells which have been evaluated and those that have not, and also to indicate when a previously evaluated cell has been edited and thus the (apparent) output is not actually the output of the input cell (cf Mathematica's behavior on this). A simple way to do this would be to change the color of evaluated input cells to blue, or to change the color of the boarder of input box.  One reason to do this is that it is difficult to tell if you have evaluated a cell whose contents don't return anything (e.g. \"a = 1+2\").\n\nIssue created by migration from https://trac.sagemath.org/ticket/2631\n\n",
    "created_at": "2008-03-21T16:06:47Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "title": "Distinguishing between (un)evaluated  cells",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2631",
    "user": "dunfield"
}
```
Assignee: boothby

There should be a visual distinction between input cells which have been evaluated and those that have not, and also to indicate when a previously evaluated cell has been edited and thus the (apparent) output is not actually the output of the input cell (cf Mathematica's behavior on this). A simple way to do this would be to change the color of evaluated input cells to blue, or to change the color of the boarder of input box.  One reason to do this is that it is difficult to tell if you have evaluated a cell whose contents don't return anything (e.g. "a = 1+2").

Issue created by migration from https://trac.sagemath.org/ticket/2631





---

archive/issue_comments_018081.json:
```json
{
    "body": "> There should be a visual distinction between input cells \n> which have been evaluated and those that have not, \n\nThere already is such a distinction!  Unevaluated cells have\na red line to the left of them.  Maybe this isn't clear enough?\nOr maybe it is once one knows about it.\n\n> also to indicate when a previously evaluated cell \n> has been edited and thus the (apparent) output is \n> not actually the output of the input cell (cf Mathematica's behavior on this).\n\nThis is a good idea.  Note that having a cell such that \"previously evaluated cell \nhas been edited and thus the (apparent) output is  not actually the output of the input cell\" was only first added to Sage (by Boothby) I think in 2.10.4 (I just\nnoticed it has a massive bug in it too).  What does Mathematica do?",
    "created_at": "2008-03-21T18:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2631#issuecomment-18081",
    "user": "was"
}
```

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

archive/issue_comments_018082.json:
```json
{
    "body": "> There already is such a distinction! Unevaluated cells have a red line to the left of them. Maybe this isn't clear enough? Or : maybe it is once one knows about it.\n\nNow that you mention them, I do see these red lines when I load up an old worksheet.   But they don't appear when new input cells are created, which is a bug, I think.   I was working with fresh worksheets since I've only just started using the notebook, so I didn't see the red lines.\n\nNow that I do see the red lines, I think they're too subtle and a little \"busy\".  I'd suggest changing the color of the input cell frame to red instead --- it would be hard to miss that.\n\n> What does Mathematica do?\n\nOn evaluation, Mathematica labels the input and output cells by \"In[n] :=\" and \"Out[n] :=\" so you can refer to the output later.  When you start editing a previously evaluated input cell, the \"In\" and \"Out\" disappear.   For Sage, you could just have the red line/box reappear if the user starts editing a cell (but not if they simply select it, move the cursor around, but don't actually edit).",
    "created_at": "2008-03-21T19:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2631#issuecomment-18082",
    "user": "dunfield"
}
```

> There already is such a distinction! Unevaluated cells have a red line to the left of them. Maybe this isn't clear enough? Or : maybe it is once one knows about it.

Now that you mention them, I do see these red lines when I load up an old worksheet.   But they don't appear when new input cells are created, which is a bug, I think.   I was working with fresh worksheets since I've only just started using the notebook, so I didn't see the red lines.

Now that I do see the red lines, I think they're too subtle and a little "busy".  I'd suggest changing the color of the input cell frame to red instead --- it would be hard to miss that.

> What does Mathematica do?

On evaluation, Mathematica labels the input and output cells by "In[n] :=" and "Out[n] :=" so you can refer to the output later.  When you start editing a previously evaluated input cell, the "In" and "Out" disappear.   For Sage, you could just have the red line/box reappear if the user starts editing a cell (but not if they simply select it, move the cursor around, but don't actually edit).



---

archive/issue_comments_018083.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2631#issuecomment-18083",
    "user": "boothby"
}
```

Resolution: invalid



---

archive/issue_comments_018084.json:
```json
{
    "body": "Closing deprecated notebook tickets",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2631#issuecomment-18084",
    "user": "boothby"
}
```

Closing deprecated notebook tickets
