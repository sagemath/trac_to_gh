# Issue 9654: implicit_plot does not accept color or rgbcolor as keywords

archive/issues_009654.json:
```json
{
    "body": "Assignee: olazo\n\nCC:  @kcrisman\n\nBoth\n\n`implicit_plot(x^2 +  y^2-1,(x,-1,1),(y,-1,1),aspect_ratio=1,color='red')`\n\nand\n\n`implicit_plot(x^2 +  y^2-1,(x,-1,1),(y,-1,1),aspect_ratio=1,color='red')`\n\ndo not produce a red circle as would be expected. matplotlib's cmap options don't get it quite good.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9654\n\n",
    "created_at": "2010-08-01T01:35:14Z",
    "labels": [
        "component: graphics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.3",
    "title": "implicit_plot does not accept color or rgbcolor as keywords",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9654",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```
Assignee: olazo

CC:  @kcrisman

Both

`implicit_plot(x^2 +  y^2-1,(x,-1,1),(y,-1,1),aspect_ratio=1,color='red')`

and

`implicit_plot(x^2 +  y^2-1,(x,-1,1),(y,-1,1),aspect_ratio=1,color='red')`

do not produce a red circle as would be expected. matplotlib's cmap options don't get it quite good.

Issue created by migration from https://trac.sagemath.org/ticket/9654





---

archive/issue_comments_093523.json:
```json
{
    "body": "Changing keywords from \"\" to \"implicit_plot\".",
    "created_at": "2010-08-01T01:36:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93523",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

Changing keywords from "" to "implicit_plot".



---

archive/issue_comments_093524.json:
```json
{
    "body": "Solved by #8529.",
    "created_at": "2010-08-14T08:41:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93524",
    "user": "https://github.com/jasongrout"
}
```

Solved by #8529.



---

archive/issue_comments_093525.json:
```json
{
    "body": "Not quite.  `color` is ok, apparently not `rgbcolor`.\n\n```\nimplicit_plot(x^2+y^2 == 2, (x,-3,3), (y,-3,3), rgbcolor=(0,1,0))\nverbose 0 (138: primitive.py, options) WARNING: Ignoring option\n'rgbcolor'=(0, 1, 0)\nverbose 0 (138: primitive.py, options) \nThe allowed options for ContourPlot defined by a 150 x 150 data grid\nare:\n    cmap           the name of a predefined colormap, \n                        a list of colors, or an instance of a \n                        matplotlib Colormap. Type: import matplotlib.cm;\nmatplotlib.cm.datad.keys()\n                        for available colormap names.\n    colorbar       Include a colorbar indicating the levels             \n\n    colorbar_optionsa dictionary of options for colorbars               \n\n    contours       Either an integer specifying the number of \n                        contour levels, or a sequence of numbers giving\n                        the actual contours to use.\n    fill           Fill contours or not                                 \n\n    label_options  a dictionary of options for the labels               \n\n    labels         show line labels or not                              \n\n    legend_label   The label for this item in the legend.               \n\n    linestyles     the style of the lines to be plotted                 \n\n    linewidths     the width of the lines to be plotted                 \n\n    plot_points    How many points to use for plotting precision        \n\n    zorder         The layer level in which to draw   \n```\n",
    "created_at": "2011-04-20T03:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93525",
    "user": "https://github.com/kcrisman"
}
```

Not quite.  `color` is ok, apparently not `rgbcolor`.

```
implicit_plot(x^2+y^2 == 2, (x,-3,3), (y,-3,3), rgbcolor=(0,1,0))
verbose 0 (138: primitive.py, options) WARNING: Ignoring option
'rgbcolor'=(0, 1, 0)
verbose 0 (138: primitive.py, options) 
The allowed options for ContourPlot defined by a 150 x 150 data grid
are:
    cmap           the name of a predefined colormap, 
                        a list of colors, or an instance of a 
                        matplotlib Colormap. Type: import matplotlib.cm;
matplotlib.cm.datad.keys()
                        for available colormap names.
    colorbar       Include a colorbar indicating the levels             

    colorbar_optionsa dictionary of options for colorbars               

    contours       Either an integer specifying the number of 
                        contour levels, or a sequence of numbers giving
                        the actual contours to use.
    fill           Fill contours or not                                 

    label_options  a dictionary of options for the labels               

    labels         show line labels or not                              

    legend_label   The label for this item in the legend.               

    linestyles     the style of the lines to be plotted                 

    linewidths     the width of the lines to be plotted                 

    plot_points    How many points to use for plotting precision        

    zorder         The layer level in which to draw   
```




---

archive/issue_comments_093526.json:
```json
{
    "body": "The right way to do this is to use `get_cmap`, but it's tricky to avoid some kind of weird circularity.",
    "created_at": "2011-06-14T05:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93526",
    "user": "https://github.com/kcrisman"
}
```

The right way to do this is to use `get_cmap`, but it's tricky to avoid some kind of weird circularity.



---

archive/issue_comments_093527.json:
```json
{
    "body": "This appears to be a simple fix for this issue. Do I need to add anything more than the doctest?\n----\nNew commits:",
    "created_at": "2016-07-04T20:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93527",
    "user": "https://github.com/paulmasson"
}
```

This appears to be a simple fix for this issue. Do I need to add anything more than the doctest?
----
New commits:



---

archive/issue_comments_093528.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-07-04T20:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93528",
    "user": "https://github.com/paulmasson"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093529.json:
```json
{
    "body": "You should raise an error if both `color` and `rgbcolor` are given akin to\n\n```\nsage: x,y = var('x,y')\nsage: plot(x^2 - 2, rgbcolor=(0,1,0), color='red')\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n...\nRuntimeError: Error in line(): option 'color' not valid.\n```\n\nAlthough I think `RuntimeError` is not the correct error, nor should `plot` go through so much to error out either. However that is a separate issue. The correct error is a `ValueError` in this situation.",
    "created_at": "2016-07-05T06:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93529",
    "user": "https://github.com/tscrim"
}
```

You should raise an error if both `color` and `rgbcolor` are given akin to

```
sage: x,y = var('x,y')
sage: plot(x^2 - 2, rgbcolor=(0,1,0), color='red')
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
...
RuntimeError: Error in line(): option 'color' not valid.
```

Although I think `RuntimeError` is not the correct error, nor should `plot` go through so much to error out either. However that is a separate issue. The correct error is a `ValueError` in this situation.



---

archive/issue_comments_093530.json:
```json
{
    "body": "I've updated the branch to raise a `ValueError` for conflicting input, as well as added a doctest.\n\nThe error in `plot.py` appears to arise from this line:\n\n\n```\n@rename_keyword(color='rgbcolor')\n```\n\n\nOnce we agree on how to handle the two arguments here, I can remove that line and update the code accordingly.",
    "created_at": "2016-07-05T23:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93530",
    "user": "https://github.com/paulmasson"
}
```

I've updated the branch to raise a `ValueError` for conflicting input, as well as added a doctest.

The error in `plot.py` appears to arise from this line:


```
@rename_keyword(color='rgbcolor')
```


Once we agree on how to handle the two arguments here, I can remove that line and update the code accordingly.



---

archive/issue_comments_093531.json:
```json
{
    "body": "Replying to [comment:13 paulmasson]:\n> I've updated the branch to raise a `ValueError` for conflicting input, as well as added a doctest.\n\nThanks. Looks good.\n\n> The error in `plot.py` appears to arise from this line:\n> \n> {{{\n> `@`rename_keyword(color='rgbcolor')\n> }}}\n> \n> Once we agree on how to handle the two arguments here, I can remove that line and update the code accordingly.\n\nWhich error where? I don't see any doctest failures.\n----\nNew commits:",
    "created_at": "2016-07-06T21:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93531",
    "user": "https://github.com/tscrim"
}
```

Replying to [comment:13 paulmasson]:
> I've updated the branch to raise a `ValueError` for conflicting input, as well as added a doctest.

Thanks. Looks good.

> The error in `plot.py` appears to arise from this line:
> 
> {{{
> `@`rename_keyword(color='rgbcolor')
> }}}
> 
> Once we agree on how to handle the two arguments here, I can remove that line and update the code accordingly.

Which error where? I don't see any doctest failures.
----
New commits:



---

archive/issue_comments_093532.json:
```json
{
    "body": "Replying to [comment:14 tscrim]:\n> Which error where? I don't see any doctest failures.\nI was unclear: I meant the `RunTime` error arising from specifying both `color` and `rgbcolor`. Presumably it arises from trying to rename a keyword argument with a name that already exists.",
    "created_at": "2016-07-06T21:30:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93532",
    "user": "https://github.com/paulmasson"
}
```

Replying to [comment:14 tscrim]:
> Which error where? I don't see any doctest failures.
I was unclear: I meant the `RunTime` error arising from specifying both `color` and `rgbcolor`. Presumably it arises from trying to rename a keyword argument with a name that already exists.



---

archive/issue_comments_093533.json:
```json
{
    "body": "Replying to [comment:15 paulmasson]:\n> Replying to [comment:14 tscrim]:\n> > Which error where? I don't see any doctest failures.\n> I was unclear: I meant the `RunTime` error arising from specifying both `color` and `rgbcolor`. Presumably it arises from trying to rename a keyword argument with a name that already exists.\n\nAh, the one coming from using `plot`. Yes, the failure is probably due to that. However, that is something for a separate ticket. If you could add a doctest checking that both inputs is invalid, then I will be happy to set a positive review.",
    "created_at": "2016-07-07T06:45:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93533",
    "user": "https://github.com/tscrim"
}
```

Replying to [comment:15 paulmasson]:
> Replying to [comment:14 tscrim]:
> > Which error where? I don't see any doctest failures.
> I was unclear: I meant the `RunTime` error arising from specifying both `color` and `rgbcolor`. Presumably it arises from trying to rename a keyword argument with a name that already exists.

Ah, the one coming from using `plot`. Yes, the failure is probably due to that. However, that is something for a separate ticket. If you could add a doctest checking that both inputs is invalid, then I will be happy to set a positive review.



---

archive/issue_comments_093534.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-07-07T21:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93534",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_093535.json:
```json
{
    "body": "Done.",
    "created_at": "2016-07-07T21:34:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93535",
    "user": "https://github.com/paulmasson"
}
```

Done.



---

archive/issue_comments_093536.json:
```json
{
    "body": "Thanks.",
    "created_at": "2016-07-08T04:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93536",
    "user": "https://github.com/tscrim"
}
```

Thanks.



---

archive/issue_comments_093537.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-07-08T04:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93537",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093538.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2016-07-08T12:37:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93538",
    "user": "https://github.com/vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_093539.json:
```json
{
    "body": "Merge conflict",
    "created_at": "2016-07-08T12:37:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93539",
    "user": "https://github.com/vbraun"
}
```

Merge conflict



---

archive/issue_comments_093540.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-07-08T19:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93540",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_093541.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-07-08T20:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93541",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_093542.json:
```json
{
    "body": "Fixed merge conflict. Doctests all pass.\n\nWhat is the protocol for this situation? Do I reset the positive review or wait for someone else? Thanks.",
    "created_at": "2016-07-08T20:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93542",
    "user": "https://github.com/paulmasson"
}
```

Fixed merge conflict. Doctests all pass.

What is the protocol for this situation? Do I reset the positive review or wait for someone else? Thanks.



---

archive/issue_comments_093543.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-07-08T20:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93543",
    "user": "https://github.com/paulmasson"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093544.json:
```json
{
    "body": "Just set it back to positive review if its just a straightforward merge fix",
    "created_at": "2016-07-08T21:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93544",
    "user": "https://github.com/vbraun"
}
```

Just set it back to positive review if its just a straightforward merge fix



---

archive/issue_comments_093545.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-07-08T21:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93545",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093546.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-07-09T16:29:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9654#issuecomment-93546",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_009789.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2016-07-09T16:29:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9654",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9654#event-9789"
}
```
