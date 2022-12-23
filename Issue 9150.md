# Issue 9150: add colorbars to density plots

archive/issues_009150.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  kcrisman\n\nSee #8368 for the contour plot patch; probably much of it can be recycled for density plots.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9150\n\n",
    "created_at": "2010-06-05T16:54:10Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "add colorbars to density plots",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9150",
    "user": "jason"
}
```
Assignee: jason, was

CC:  kcrisman

See #8368 for the contour plot patch; probably much of it can be recycled for density plots.

Issue created by migration from https://trac.sagemath.org/ticket/9150





---

archive/issue_comments_085431.json:
```json
{
    "body": "Kirill Vankov (on sage-devel just now) also asked that colorbars be added as an option to matrix plots as well, which would be straightforward once they were added to density plots.",
    "created_at": "2011-04-07T17:01:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9150#issuecomment-85431",
    "user": "jason"
}
```

Kirill Vankov (on sage-devel just now) also asked that colorbars be added as an option to matrix plots as well, which would be straightforward once they were added to density plots.



---

archive/issue_comments_085432.json:
```json
{
    "body": "[This ask.sagemath.org question](http://ask.sagemath.org/question/1902/colorbar-for-density-plots) asks for exactly the same thing, and user \"Shashank\" has a nice mpl example of it.",
    "created_at": "2012-10-24T02:26:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9150#issuecomment-85432",
    "user": "kcrisman"
}
```

[This ask.sagemath.org question](http://ask.sagemath.org/question/1902/colorbar-for-density-plots) asks for exactly the same thing, and user "Shashank" has a nice mpl example of it.



---

archive/issue_comments_085433.json:
```json
{
    "body": "The `Colorbar` class in mpl is a bit strange. It doesn't take in all the options for all kinds of figures. The way it is used in `contour_plot` in Sage works only for that case.",
    "created_at": "2012-10-28T16:47:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9150#issuecomment-85433",
    "user": "ppurka"
}
```

The `Colorbar` class in mpl is a bit strange. It doesn't take in all the options for all kinds of figures. The way it is used in `contour_plot` in Sage works only for that case.
