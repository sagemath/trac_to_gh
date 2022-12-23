# Issue 8625: plot_scalar_field (a scalar version of plot_vector_field)

archive/issues_008625.json:
```json
{
    "body": "Assignee: olazo\n\nCC:  jason\n\nKeywords: scalar,plot\n\nThis should be a function that plots a two variable funtion as a group of isolines along a given place of the xy plane.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8625\n\n",
    "created_at": "2010-03-29T18:46:11Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "plot_scalar_field (a scalar version of plot_vector_field)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8625",
    "user": "olazo"
}
```
Assignee: olazo

CC:  jason

Keywords: scalar,plot

This should be a function that plots a two variable funtion as a group of isolines along a given place of the xy plane.

Issue created by migration from https://trac.sagemath.org/ticket/8625





---

archive/issue_comments_078196.json:
```json
{
    "body": "Would this be like a density plot or contour plot?  Even after consulting the internet I'm not quite sure what the difference would be, though perhaps a shortcut would be useful (?).",
    "created_at": "2010-07-27T17:47:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8625#issuecomment-78196",
    "user": "kcrisman"
}
```

Would this be like a density plot or contour plot?  Even after consulting the internet I'm not quite sure what the difference would be, though perhaps a shortcut would be useful (?).



---

archive/issue_comments_078197.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-08-01T01:06:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8625#issuecomment-78197",
    "user": "olazo"
}
```

Attachment



---

archive/issue_comments_078198.json:
```json
{
    "body": "Attachment\n\nI have just attatched two pictures of the intended results. Both are plots of electric potentials the first one comes with a plot_vector_field of the corresponding electric field.\n\nI also attatched a picture of the 3d version, although I mean to make a new ticket for that once this one is finished.",
    "created_at": "2010-08-01T01:09:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8625#issuecomment-78198",
    "user": "olazo"
}
```

Attachment

I have just attatched two pictures of the intended results. Both are plots of electric potentials the first one comes with a plot_vector_field of the corresponding electric field.

I also attatched a picture of the 3d version, although I mean to make a new ticket for that once this one is finished.



---

archive/issue_comments_078199.json:
```json
{
    "body": "It sounds like you are looking for a contour plot (?).  Can you describe what command you used to create the first plot?  Maybe we could make a shortcut to the specific type of contour plot you need, which would give the functionality you are looking for.",
    "created_at": "2010-08-02T15:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8625#issuecomment-78199",
    "user": "kcrisman"
}
```

It sounds like you are looking for a contour plot (?).  Can you describe what command you used to create the first plot?  Maybe we could make a shortcut to the specific type of contour plot you need, which would give the functionality you are looking for.



---

archive/issue_comments_078200.json:
```json
{
    "body": "Yes! I had not seen that command. I used implicit_plot. Now that I've checked contour_plot it is exactly what I wanted.\n\nThe only thing I don't like is the automatic choosing of contour levels. They usually get too high values that concentrate around the poles of the function so that there are almost no curves in parts of the picture away from the poles. I'll make a patch to improve that.\n\nAlso, it seems like there's no contour_plot3d I'll also work on that.",
    "created_at": "2010-08-02T15:56:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8625#issuecomment-78200",
    "user": "olazo"
}
```

Yes! I had not seen that command. I used implicit_plot. Now that I've checked contour_plot it is exactly what I wanted.

The only thing I don't like is the automatic choosing of contour levels. They usually get too high values that concentrate around the poles of the function so that there are almost no curves in parts of the picture away from the poles. I'll make a patch to improve that.

Also, it seems like there's no contour_plot3d I'll also work on that.



---

archive/issue_comments_078201.json:
```json
{
    "body": "Replying to [comment:4 olazo]:\n> Yes! I had not seen that command. I used implicit_plot. Now that I've checked contour_plot it is exactly what I wanted.\n\nGreat!\n\n> The only thing I don't like is the automatic choosing of contour levels. They usually get too high values that concentrate around the poles of the function so that there are almost no curves in parts of the picture away from the poles. I'll make a patch to improve that.\n\nWhat I would do is leave the current functionality alone, but add an option for the sorts of situations you encounter - or something like that.  You can also choose the contours you want - see\n\n```\nsage: contour_plot?\n```\n\n\n\n> Also, it seems like there's no contour_plot3d I'll also work on that.\n\nHave you tried `implicit_plot3d`? Presumably one would use this to start.",
    "created_at": "2010-08-02T16:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8625#issuecomment-78201",
    "user": "kcrisman"
}
```

Replying to [comment:4 olazo]:
> Yes! I had not seen that command. I used implicit_plot. Now that I've checked contour_plot it is exactly what I wanted.

Great!

> The only thing I don't like is the automatic choosing of contour levels. They usually get too high values that concentrate around the poles of the function so that there are almost no curves in parts of the picture away from the poles. I'll make a patch to improve that.

What I would do is leave the current functionality alone, but add an option for the sorts of situations you encounter - or something like that.  You can also choose the contours you want - see

```
sage: contour_plot?
```



> Also, it seems like there's no contour_plot3d I'll also work on that.

Have you tried `implicit_plot3d`? Presumably one would use this to start.



---

archive/issue_comments_078202.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-08-02T16:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8625#issuecomment-78202",
    "user": "kcrisman"
}
```

Changing priority from major to minor.



---

archive/issue_comments_078203.json:
```json
{
    "body": "Replying to [comment:5 kcrisman]:\n> What I would do is leave the current functionality alone, but add an option for the sorts of situations you encounter - or something like that.  You can also choose the contours you want - see\n\nYes, that's what I was thinking of, add something like an `,avoid_poles=False` option. Yes, I have seen the option to choose the contours.\n\n> Have you tried `implicit_plot3d`? Presumably one would use this to start.\n\nYes, that is what I used to produce the 3d picture. I have just made #9669",
    "created_at": "2010-08-02T16:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8625#issuecomment-78203",
    "user": "olazo"
}
```

Replying to [comment:5 kcrisman]:
> What I would do is leave the current functionality alone, but add an option for the sorts of situations you encounter - or something like that.  You can also choose the contours you want - see

Yes, that's what I was thinking of, add something like an `,avoid_poles=False` option. Yes, I have seen the option to choose the contours.

> Have you tried `implicit_plot3d`? Presumably one would use this to start.

Yes, that is what I used to produce the 3d picture. I have just made #9669



---

archive/issue_comments_078204.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-10-23T23:19:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8625#issuecomment-78204",
    "user": "olazo"
}
```

Attachment
