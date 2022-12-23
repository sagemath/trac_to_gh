# Issue 4342: Add legends to plot.py

archive/issues_004342.json:
```json
{
    "body": "Assignee: anakha\n\nCC:  kcrisman slosoi novoselt abergeron jhpalmieri mvngu\n\nAdd support for placing legends on plots using the matplotlib facility for doing so.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4342\n\n",
    "created_at": "2008-10-22T22:48:14Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "Add legends to plot.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4342",
    "user": "anakha"
}
```
Assignee: anakha

CC:  kcrisman slosoi novoselt abergeron jhpalmieri mvngu

Add support for placing legends on plots using the matplotlib facility for doing so.

Issue created by migration from https://trac.sagemath.org/ticket/4342





---

archive/issue_comments_031851.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-10-22T22:48:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31851",
    "user": "anakha"
}
```

Attachment



---

archive/issue_comments_031852.json:
```json
{
    "body": "Add the option to put legends on plots.  \n\nAlso fixes three long test markers that where reading #long rather than #long time and two or three minor documentation mistakes elsewhere in the code.  These where bundled because they don't warrant a separate ticket for me but are still nice to fix.",
    "created_at": "2008-10-22T22:51:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31852",
    "user": "anakha"
}
```

Add the option to put legends on plots.  

Also fixes three long test markers that where reading #long rather than #long time and two or three minor documentation mistakes elsewhere in the code.  These where bundled because they don't warrant a separate ticket for me but are still nice to fix.



---

archive/issue_comments_031853.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-22T22:51:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31853",
    "user": "anakha"
}
```

Changing status from new to assigned.



---

archive/issue_comments_031854.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-10-23T21:35:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31854",
    "user": "anakha"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_031855.json:
```json
{
    "body": "New patch to pass options around in a better way.  Also now use `@`suboptions marker from #4203 so you need to apply that patch first.",
    "created_at": "2008-10-23T21:35:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31855",
    "user": "anakha"
}
```

New patch to pass options around in a better way.  Also now use `@`suboptions marker from #4203 so you need to apply that patch first.



---

archive/issue_comments_031856.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-10-23T21:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31856",
    "user": "anakha"
}
```

Attachment



---

archive/issue_comments_031857.json:
```json
{
    "body": "For the patch **trac_4342.patch**, here are possible fixes to your documentation:\n\n\n\n1.\n\n```\n-denoting a color or an rgb tuple. The string can be a color name\n+denoting a color or an RGB tuple. The string can be a color name\n```\n\n2.\n\n```\n-If called with no input return the current legend setting.\n+If called with no input, return the current legend setting.\n```\n\n3.\n\n```\n-Sets the legend label font\n+Sets the legend label font.\n```\n\n4.\n\n```\n-form is just a floating point rgb tuple with all values ranging\n+form is just a floating point RGB tuple with all values ranging\n```\n",
    "created_at": "2008-10-27T12:46:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31857",
    "user": "mvngu"
}
```

For the patch **trac_4342.patch**, here are possible fixes to your documentation:



1.

```
-denoting a color or an rgb tuple. The string can be a color name
+denoting a color or an RGB tuple. The string can be a color name
```

2.

```
-If called with no input return the current legend setting.
+If called with no input, return the current legend setting.
```

3.

```
-Sets the legend label font
+Sets the legend label font.
```

4.

```
-form is just a floating point rgb tuple with all values ranging
+form is just a floating point RGB tuple with all values ranging
```




---

archive/issue_comments_031858.json:
```json
{
    "body": "Attachment\n\nmvngu's doc fixes",
    "created_at": "2008-11-09T23:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31858",
    "user": "TimothyClemans"
}
```

Attachment

mvngu's doc fixes



---

archive/issue_comments_031859.json:
```json
{
    "body": "Replying to [comment:3 mvngu]:\n> For the patch **trac_4342.patch**, here are possible fixes to your documentation:\n> \n\n\n> 1.\n> {{{\n> -denoting a color or an rgb tuple. The string can be a color name\n> +denoting a color or an RGB tuple. The string can be a color name\n> }}}\n> 2.\n> {{{\n> -If called with no input return the current legend setting.\n> +If called with no input, return the current legend setting.\n> }}}\n> 3.\n> {{{\n> -Sets the legend label font\n> +Sets the legend label font.\n> }}}\n> 4.\n> {{{\n> -form is just a floating point rgb tuple with all values ranging\n> +form is just a floating point RGB tuple with all values ranging\n> }}}\n\nI uploaded a patch with these fixes. \n\nMvngu, in the future please upload patches with your doc fixes. Thanks :)",
    "created_at": "2008-11-09T23:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31859",
    "user": "TimothyClemans"
}
```

Replying to [comment:3 mvngu]:
> For the patch **trac_4342.patch**, here are possible fixes to your documentation:
> 


> 1.
> {{{
> -denoting a color or an rgb tuple. The string can be a color name
> +denoting a color or an RGB tuple. The string can be a color name
> }}}
> 2.
> {{{
> -If called with no input return the current legend setting.
> +If called with no input, return the current legend setting.
> }}}
> 3.
> {{{
> -Sets the legend label font
> +Sets the legend label font.
> }}}
> 4.
> {{{
> -form is just a floating point rgb tuple with all values ranging
> +form is just a floating point RGB tuple with all values ranging
> }}}

I uploaded a patch with these fixes. 

Mvngu, in the future please upload patches with your doc fixes. Thanks :)



---

archive/issue_comments_031860.json:
```json
{
    "body": "Attachment\n\nI've folded all the patches together and rebased them against plot.py refactoring.  These are in trac_4342.2.patch .\n\nI'll try to give this a proper review sometime this weekend.",
    "created_at": "2008-11-28T07:10:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31860",
    "user": "mhansen"
}
```

Attachment

I've folded all the patches together and rebased them against plot.py refactoring.  These are in trac_4342.2.patch .

I'll try to give this a proper review sometime this weekend.



---

archive/issue_comments_031861.json:
```json
{
    "body": "what's the status on this?  Mike, did you have time to look at it?",
    "created_at": "2008-12-12T21:25:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31861",
    "user": "jason"
}
```

what's the status on this?  Mike, did you have time to look at it?



---

archive/issue_comments_031862.json:
```json
{
    "body": "The good news is that Mike Hansen's patch does apply cleanly to 3.2.2.\n\nThe bad news is that this patch breaks some basic functionality:\n\n\n```\nsage: p = plot(tan(x), x, -1/2, 1/2)\nsage: show(p)\n\n```\n\nraises a TypeError exception.\n\nThat is serious but more serious (to me - maybe this exception is \nan easy-to-fix bug) is the design of this legend functionality. \n\nIt seems to me (and people who know about the Graphics class can hopefully\ncorrect me if I am wrong) the following is both possible and a fairly \nnatural way of writing a legend as another graphics object:\n\n1. given 2d plot objects P, Q (ie, instances of a Graphics class),\none could wrote a function which returns \n(a) the functions being plotted in P,Q (resp), \n(b) the line style used in P,Q (resp).\nFrom this data, one can write a function taking P,Q (and a cnter point)\nas arguments (more generally any list of such plot objects) and returning\na legend as an analog of a text plot. This can be placed anywhere \nby choosing the center point appropriately.\n\nI'm happy to change my opinion (since IMHO this added functionality would be great),\nespecially if someone with more knowledge of the plotting can comment positively\non this. I really greatly appreciate the hard programming work that went into this.\nMaybe I'm being naive but the design to me seems a bit awkward, and in any case \nit breaks show (which is bad, hence making it a \"show stopper\", if you excuse \nthe horribly bad pun).",
    "created_at": "2008-12-30T03:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31862",
    "user": "wdj"
}
```

The good news is that Mike Hansen's patch does apply cleanly to 3.2.2.

The bad news is that this patch breaks some basic functionality:


```
sage: p = plot(tan(x), x, -1/2, 1/2)
sage: show(p)

```

raises a TypeError exception.

That is serious but more serious (to me - maybe this exception is 
an easy-to-fix bug) is the design of this legend functionality. 

It seems to me (and people who know about the Graphics class can hopefully
correct me if I am wrong) the following is both possible and a fairly 
natural way of writing a legend as another graphics object:

1. given 2d plot objects P, Q (ie, instances of a Graphics class),
one could wrote a function which returns 
(a) the functions being plotted in P,Q (resp), 
(b) the line style used in P,Q (resp).
From this data, one can write a function taking P,Q (and a cnter point)
as arguments (more generally any list of such plot objects) and returning
a legend as an analog of a text plot. This can be placed anywhere 
by choosing the center point appropriately.

I'm happy to change my opinion (since IMHO this added functionality would be great),
especially if someone with more knowledge of the plotting can comment positively
on this. I really greatly appreciate the hard programming work that went into this.
Maybe I'm being naive but the design to me seems a bit awkward, and in any case 
it breaks show (which is bad, hence making it a "show stopper", if you excuse 
the horribly bad pun).



---

archive/issue_comments_031863.json:
```json
{
    "body": "There is no such thing as \"negative review\", but there is \"needs work\".\n\nCheers,\n\nMichael",
    "created_at": "2008-12-30T03:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31863",
    "user": "mabshoff"
}
```

There is no such thing as "negative review", but there is "needs work".

Cheers,

Michael



---

archive/issue_comments_031864.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-12-31T04:26:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31864",
    "user": "abergeron"
}
```

Attachment



---

archive/issue_comments_031865.json:
```json
{
    "body": "Attachment\n\nThe last patch (trac_4342_v3.2.patch) fixes the TypeError problem and add tests and documentation where appropriate (can't believe I missed these).\n\nAs far as I know, there is no way to get the function that's being plotted from the GraphicsPrimitve object (except maybe for some specialized primitives like Circle) because all you have is a matrix of sample points.  So I don't think it is a good way.\n\nAbout the center point, it is already possible to specify a tuple of floats between 0 and 1 that gives the relative coordinates of the legend box.\n\nAnd last, about the design, I kind of copied it from matplotlib where each object is labeled beforehand.  I could always provide an option to specify legend labels in show() and save() but due to the design of Graphics I think this would be shaky at best because the user has now reliable way of knowing the content of a Graphics object.\n\nAnyway if some clever way of overcoming the obstacle(s) above is found then something like what you want could be implemented in a later patch.",
    "created_at": "2008-12-31T04:46:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31865",
    "user": "abergeron"
}
```

Attachment

The last patch (trac_4342_v3.2.patch) fixes the TypeError problem and add tests and documentation where appropriate (can't believe I missed these).

As far as I know, there is no way to get the function that's being plotted from the GraphicsPrimitve object (except maybe for some specialized primitives like Circle) because all you have is a matrix of sample points.  So I don't think it is a good way.

About the center point, it is already possible to specify a tuple of floats between 0 and 1 that gives the relative coordinates of the legend box.

And last, about the design, I kind of copied it from matplotlib where each object is labeled beforehand.  I could always provide an option to specify legend labels in show() and save() but due to the design of Graphics I think this would be shaky at best because the user has now reliable way of knowing the content of a Graphics object.

Anyway if some clever way of overcoming the obstacle(s) above is found then something like what you want could be implemented in a later patch.



---

archive/issue_comments_031866.json:
```json
{
    "body": "Can you please explain exactly which patches to apply and in which order from a new clone of Sage? I can't get them to apply cleanly.",
    "created_at": "2008-12-31T12:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31866",
    "user": "wdj"
}
```

Can you please explain exactly which patches to apply and in which order from a new clone of Sage? I can't get them to apply cleanly.



---

archive/issue_comments_031867.json:
```json
{
    "body": "You only need trac_4342_v3.2.patch.  Ignore all others.",
    "created_at": "2008-12-31T19:30:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31867",
    "user": "abergeron"
}
```

You only need trac_4342_v3.2.patch.  Ignore all others.



---

archive/issue_comments_031868.json:
```json
{
    "body": "Again, I am having trouble running tests, so I can't say if they all pass. The examples seem fine (if somewhat too few). Still, which this very clever bit of programmming, this block of commands\n\n\n```\nsage: P1 = plot(exp(x), 0, 2, legend_label='$y=e^x$')\nsage: P2 = plot(sin(x), 0, 2, rgbcolor=(1,0,0),legend_label='$y=\\sin(x)$')\nsage: show(P1+P2)\n```\n\n\nproduces a beautiful plot of two curves, one red and the other blue, and the legend labels are collected into a distinctive light grey box with the correct labels.\n\nWonderful!!",
    "created_at": "2008-12-31T20:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31868",
    "user": "wdj"
}
```

Again, I am having trouble running tests, so I can't say if they all pass. The examples seem fine (if somewhat too few). Still, which this very clever bit of programmming, this block of commands


```
sage: P1 = plot(exp(x), 0, 2, legend_label='$y=e^x$')
sage: P2 = plot(sin(x), 0, 2, rgbcolor=(1,0,0),legend_label='$y=\sin(x)$')
sage: show(P1+P2)
```


produces a beautiful plot of two curves, one red and the other blue, and the legend labels are collected into a distinctive light grey box with the correct labels.

Wonderful!!



---

archive/issue_comments_031869.json:
```json
{
    "body": "Hi Arnaud,\n\nafter applying #4878 and #4884 to my Sage 3.3.alpha0 merge tree I am seeing rejects with trac_4342_v3.2.patch:\n\n```\nmabshoff@geom:/scratch/mabshoff/sage-3.3.alpha0/devel/sage$ patch -p1 --dry-run < trac_4342_v3.2.patch \npatching file sage/plot/arrow.py\npatching file sage/plot/bar_chart.py\npatching file sage/plot/circle.py\npatching file sage/plot/contour_plot.py\nHunk #1 succeeded at 54 with fuzz 2 (offset 1 line).\nHunk #2 succeeded at 73 (offset -13 lines).\nHunk #3 FAILED at 116.\nHunk #4 succeeded at 177 (offset -11 lines).\n1 out of 4 hunks FAILED -- saving rejects to file sage/plot/contour_plot.py.rej\npatching file sage/plot/disk.py\npatching file sage/plot/line.py\npatching file sage/plot/plot.py\nHunk #3 succeeded at 390 with fuzz 2.\nHunk #4 succeeded at 618 (offset 27 lines).\nHunk #5 succeeded at 726 (offset 27 lines).\nHunk #6 succeeded at 961 (offset 27 lines).\nHunk #7 succeeded at 982 (offset 27 lines).\nHunk #8 succeeded at 993 (offset 27 lines).\nHunk #9 succeeded at 1010 (offset 27 lines).\nHunk #10 succeeded at 1078 (offset 27 lines).\nHunk #11 succeeded at 1128 (offset 27 lines).\nHunk #12 succeeded at 1200 with fuzz 1 (offset 27 lines).\nHunk #13 succeeded at 1303 with fuzz 2 (offset 105 lines).\nHunk #14 succeeded at 1400 (offset 104 lines).\nHunk #15 succeeded at 1545 (offset 104 lines).\nHunk #16 succeeded at 1582 (offset 104 lines).\nHunk #17 succeeded at 1671 (offset 104 lines).\nHunk #18 succeeded at 1699 (offset 104 lines).\nHunk #19 succeeded at 1721 (offset 104 lines).\nHunk #20 succeeded at 1800 (offset 104 lines).\nHunk #21 succeeded at 1886 (offset 104 lines).\npatching file sage/plot/point.py\nHunk #1 FAILED at 1.\nHunk #2 succeeded at 24 (offset 9 lines).\nHunk #3 succeeded at 39 (offset 9 lines).\nHunk #4 succeeded at 106 (offset 9 lines).\nHunk #5 succeeded at 131 (offset 13 lines).\nHunk #6 succeeded at 140 (offset 13 lines).\n1 out of 6 hunks FAILED -- saving rejects to file sage/plot/point.py.rej\npatching file sage/plot/polygon.py\npatching file sage/plot/primitive.py\n```\n\n\nCan you rebase the patch against 3.2.3+#4878 and #4884?\n\nCheers,\n\nMichael",
    "created_at": "2009-01-12T01:44:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31869",
    "user": "mabshoff"
}
```

Hi Arnaud,

after applying #4878 and #4884 to my Sage 3.3.alpha0 merge tree I am seeing rejects with trac_4342_v3.2.patch:

```
mabshoff@geom:/scratch/mabshoff/sage-3.3.alpha0/devel/sage$ patch -p1 --dry-run < trac_4342_v3.2.patch 
patching file sage/plot/arrow.py
patching file sage/plot/bar_chart.py
patching file sage/plot/circle.py
patching file sage/plot/contour_plot.py
Hunk #1 succeeded at 54 with fuzz 2 (offset 1 line).
Hunk #2 succeeded at 73 (offset -13 lines).
Hunk #3 FAILED at 116.
Hunk #4 succeeded at 177 (offset -11 lines).
1 out of 4 hunks FAILED -- saving rejects to file sage/plot/contour_plot.py.rej
patching file sage/plot/disk.py
patching file sage/plot/line.py
patching file sage/plot/plot.py
Hunk #3 succeeded at 390 with fuzz 2.
Hunk #4 succeeded at 618 (offset 27 lines).
Hunk #5 succeeded at 726 (offset 27 lines).
Hunk #6 succeeded at 961 (offset 27 lines).
Hunk #7 succeeded at 982 (offset 27 lines).
Hunk #8 succeeded at 993 (offset 27 lines).
Hunk #9 succeeded at 1010 (offset 27 lines).
Hunk #10 succeeded at 1078 (offset 27 lines).
Hunk #11 succeeded at 1128 (offset 27 lines).
Hunk #12 succeeded at 1200 with fuzz 1 (offset 27 lines).
Hunk #13 succeeded at 1303 with fuzz 2 (offset 105 lines).
Hunk #14 succeeded at 1400 (offset 104 lines).
Hunk #15 succeeded at 1545 (offset 104 lines).
Hunk #16 succeeded at 1582 (offset 104 lines).
Hunk #17 succeeded at 1671 (offset 104 lines).
Hunk #18 succeeded at 1699 (offset 104 lines).
Hunk #19 succeeded at 1721 (offset 104 lines).
Hunk #20 succeeded at 1800 (offset 104 lines).
Hunk #21 succeeded at 1886 (offset 104 lines).
patching file sage/plot/point.py
Hunk #1 FAILED at 1.
Hunk #2 succeeded at 24 (offset 9 lines).
Hunk #3 succeeded at 39 (offset 9 lines).
Hunk #4 succeeded at 106 (offset 9 lines).
Hunk #5 succeeded at 131 (offset 13 lines).
Hunk #6 succeeded at 140 (offset 13 lines).
1 out of 6 hunks FAILED -- saving rejects to file sage/plot/point.py.rej
patching file sage/plot/polygon.py
patching file sage/plot/primitive.py
```


Can you rebase the patch against 3.2.3+#4878 and #4884?

Cheers,

Michael



---

archive/issue_comments_031870.json:
```json
{
    "body": "Note that I also applied a slightly changed #2770 since I fixed the patch to resolve a conflict in sage/plot/all.py due to trac_4878.patch.\n\nIf doctests pass I will merge all those three tickets shortly.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-12T01:52:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31870",
    "user": "mabshoff"
}
```

Note that I also applied a slightly changed #2770 since I fixed the patch to resolve a conflict in sage/plot/all.py due to trac_4878.patch.

If doctests pass I will merge all those three tickets shortly.

Cheers,

Michael



---

archive/issue_comments_031871.json:
```json
{
    "body": "Attachment\n\nrebase against 3.3.alpha1",
    "created_at": "2009-01-24T02:38:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31871",
    "user": "abergeron"
}
```

Attachment

rebase against 3.3.alpha1



---

archive/issue_comments_031872.json:
```json
{
    "body": "Rebase is done, and I changed the milestone since it can be merged now.  Sorry for the delay.",
    "created_at": "2009-01-24T02:40:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31872",
    "user": "abergeron"
}
```

Rebase is done, and I changed the milestone since it can be merged now.  Sorry for the delay.



---

archive/issue_comments_031873.json:
```json
{
    "body": "The last patch causes the following doctest failure in my 3.3.alpha2 merge tree:\n\n```\nsage -t -long \"devel/sage/sage/plot/contour_plot.py\"        \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/plot/contour_plot.py\", line 237:\n    sage: region_plot(cos(x^2+y^2) <= 0, (-3, 3), (-3, 3))\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-3.3.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.3.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.3.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[3]>\", line 1, in <module>\n        region_plot(cos(x**Integer(2)+y**Integer(2)) <= Integer(0), (-Integer(3), Integer(3)), (-Integer(3), Integer(3)))###line 237:\n    sage: region_plot(cos(x^2+y^2) <= 0, (-3, 3), (-3, 3))\n      File \"sage_object.pyx\", line 92, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1082)\n      File \"/scratch/mabshoff/sage-3.3.alpha2/local/lib/python2.5/site-packages/sage/plot/plot.py\", line 822, in _repr_\n        self.show()\n      File \"/scratch/mabshoff/sage-3.3.alpha2/local/lib/python2.5/site-packages/sage/plot/misc.py\", line 273, in wrapper\n        return func(*args, **kwds)\n      File \"/scratch/mabshoff/sage-3.3.alpha2/local/lib/python2.5/site-packages/sage/plot/plot.py\", line 1184, in show\n        hgridlinesstyle=hgridlinesstyle)\n      File \"/scratch/mabshoff/sage-3.3.alpha2/local/lib/python2.5/site-packages/sage/plot/misc.py\", line 273, in wrapper\n        return func(*args, **kwds)\n      File \"/scratch/mabshoff/sage-3.3.alpha2/local/lib/python2.5/site-packages/sage/plot/plot.py\", line 1402, in save\n        g._render_on_subplot(subplot)\n      File \"/scratch/mabshoff/sage-3.3.alpha2/local/lib/python2.5/site-packages/sage/plot/contour_plot.py\", line 80, in _render_on_subplot\n        subplot.contourf(self.xy_data_array, contours, cmap=cmap, extent=(x0,x1,y0,y1), label=options['legend_label'])\n    KeyError: 'legend_label'\n**********************************************************************\n<SNIP>\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T18:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31873",
    "user": "mabshoff"
}
```

The last patch causes the following doctest failure in my 3.3.alpha2 merge tree:

```
sage -t -long "devel/sage/sage/plot/contour_plot.py"        
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/plot/contour_plot.py", line 237:
    sage: region_plot(cos(x^2+y^2) <= 0, (-3, 3), (-3, 3))
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.3.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[3]>", line 1, in <module>
        region_plot(cos(x**Integer(2)+y**Integer(2)) <= Integer(0), (-Integer(3), Integer(3)), (-Integer(3), Integer(3)))###line 237:
    sage: region_plot(cos(x^2+y^2) <= 0, (-3, 3), (-3, 3))
      File "sage_object.pyx", line 92, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1082)
      File "/scratch/mabshoff/sage-3.3.alpha2/local/lib/python2.5/site-packages/sage/plot/plot.py", line 822, in _repr_
        self.show()
      File "/scratch/mabshoff/sage-3.3.alpha2/local/lib/python2.5/site-packages/sage/plot/misc.py", line 273, in wrapper
        return func(*args, **kwds)
      File "/scratch/mabshoff/sage-3.3.alpha2/local/lib/python2.5/site-packages/sage/plot/plot.py", line 1184, in show
        hgridlinesstyle=hgridlinesstyle)
      File "/scratch/mabshoff/sage-3.3.alpha2/local/lib/python2.5/site-packages/sage/plot/misc.py", line 273, in wrapper
        return func(*args, **kwds)
      File "/scratch/mabshoff/sage-3.3.alpha2/local/lib/python2.5/site-packages/sage/plot/plot.py", line 1402, in save
        g._render_on_subplot(subplot)
      File "/scratch/mabshoff/sage-3.3.alpha2/local/lib/python2.5/site-packages/sage/plot/contour_plot.py", line 80, in _render_on_subplot
        subplot.contourf(self.xy_data_array, contours, cmap=cmap, extent=(x0,x1,y0,y1), label=options['legend_label'])
    KeyError: 'legend_label'
**********************************************************************
<SNIP>
```


Cheers,

Michael



---

archive/issue_comments_031874.json:
```json
{
    "body": "Great.  This is what I get by developing related features separately.\n\nAnyway I noticed that this is fixed if you apply both this patch and the one at #4898 in that order.\n\nIf that is unacceptable, then I'll split the fix out.",
    "created_at": "2009-01-24T19:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31874",
    "user": "abergeron"
}
```

Great.  This is what I get by developing related features separately.

Anyway I noticed that this is fixed if you apply both this patch and the one at #4898 in that order.

If that is unacceptable, then I'll split the fix out.



---

archive/issue_comments_031875.json:
```json
{
    "body": "This seems like something kcrisman could be a big help on! :)",
    "created_at": "2009-12-31T03:39:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31875",
    "user": "jason"
}
```

This seems like something kcrisman could be a big help on! :)



---

archive/issue_comments_031876.json:
```json
{
    "body": "That last comment was pretty ambiguous.  Karl-Dieter, do you have time to look at this ticket?",
    "created_at": "2009-12-31T03:41:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31876",
    "user": "jason"
}
```

That last comment was pretty ambiguous.  Karl-Dieter, do you have time to look at this ticket?



---

archive/issue_comments_031877.json:
```json
{
    "body": "Sure, I'll take a peek, though I have a bowl game to watch that may take priority soon.  I imagine this will need a fairly significant rebase, since plotting has been improved so much in the last **year**!",
    "created_at": "2009-12-31T04:11:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31877",
    "user": "kcrisman"
}
```

Sure, I'll take a peek, though I have a bowl game to watch that may take priority soon.  I imagine this will need a fairly significant rebase, since plotting has been improved so much in the last **year**!



---

archive/issue_comments_031878.json:
```json
{
    "body": "Just for info:\n\n```\npatching file sage/plot/arrow.py\nHunk #1 FAILED at 71\nHunk #2 FAILED at 136\nHunk #3 FAILED at 150\nHunk #4 FAILED at 170\nHunk #5 FAILED at 177\n5 out of 5 hunks FAILED -- saving rejects to file sage/plot/arrow.py.rej\npatching file sage/plot/bar_chart.py\nHunk #1 FAILED at 55\nHunk #2 FAILED at 92\nHunk #3 FAILED at 109\n3 out of 4 hunks FAILED -- saving rejects to file sage/plot/bar_chart.py.rej\npatching file sage/plot/circle.py\nHunk #1 FAILED at 46\nHunk #2 FAILED at 65\nHunk #3 FAILED at 89\nHunk #4 FAILED at 103\nHunk #5 FAILED at 127\n5 out of 5 hunks FAILED -- saving rejects to file sage/plot/circle.py.rej\npatching file sage/plot/contour_plot.py\nHunk #1 FAILED at 53\nHunk #2 FAILED at 71\nHunk #3 FAILED at 116\nHunk #4 FAILED at 174\n4 out of 4 hunks FAILED -- saving rejects to file sage/plot/contour_plot.py.rej\npatching file sage/plot/disk.py\nHunk #1 FAILED at 52\nHunk #2 FAILED at 74\nHunk #3 FAILED at 98\n3 out of 3 hunks FAILED -- saving rejects to file sage/plot/disk.py.rej\npatching file sage/plot/line.py\nHunk #2 FAILED at 62\nHunk #4 FAILED at 218\nHunk #5 FAILED at 246\nHunk #6 FAILED at 320\n4 out of 6 hunks FAILED -- saving rejects to file sage/plot/line.py.rej\npatching file sage/plot/plot.py\nHunk #1 FAILED at 267\nHunk #2 succeeded at 433 with fuzz 2 (offset 99 lines).\nHunk #5 succeeded at 900 with fuzz 1 (offset 172 lines).\nHunk #6 FAILED at 960\nHunk #7 FAILED at 977\nHunk #8 FAILED at 987\nHunk #9 FAILED at 1004\nHunk #10 FAILED at 1071\nHunk #11 FAILED at 1119\nHunk #12 FAILED at 1191\nHunk #13 FAILED at 1292\nHunk #14 FAILED at 1388\nHunk #15 FAILED at 1513\nHunk #16 FAILED at 1549\nHunk #17 FAILED at 1637\nHunk #18 FAILED at 1665\nHunk #19 FAILED at 1684\nHunk #20 FAILED at 1769\nHunk #21 FAILED at 1854\n17 out of 21 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej\npatching file sage/plot/point.py\nHunk #2 FAILED at 23\nHunk #3 succeeded at 91 with fuzz 2 (offset 51 lines).\nHunk #4 FAILED at 104\nHunk #5 FAILED at 129\nHunk #6 FAILED at 138\n4 out of 6 hunks FAILED -- saving rejects to file sage/plot/point.py.rej\npatching file sage/plot/polygon.py\nHunk #1 FAILED at 43\nHunk #2 FAILED at 74\nHunk #3 FAILED at 90\nHunk #4 succeeded at 341 with fuzz 2 (offset 194 lines).\n3 out of 4 hunks FAILED -- saving rejects to file sage/plot/polygon.py.rej\npatching file sage/plot/primitive.py\nHunk #1 FAILED at 73\n1 out of 1 hunks FAILED -- saving rejects to file sage/plot/primitive.py.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2009-12-31T04:13:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31878",
    "user": "kcrisman"
}
```

Just for info:

```
patching file sage/plot/arrow.py
Hunk #1 FAILED at 71
Hunk #2 FAILED at 136
Hunk #3 FAILED at 150
Hunk #4 FAILED at 170
Hunk #5 FAILED at 177
5 out of 5 hunks FAILED -- saving rejects to file sage/plot/arrow.py.rej
patching file sage/plot/bar_chart.py
Hunk #1 FAILED at 55
Hunk #2 FAILED at 92
Hunk #3 FAILED at 109
3 out of 4 hunks FAILED -- saving rejects to file sage/plot/bar_chart.py.rej
patching file sage/plot/circle.py
Hunk #1 FAILED at 46
Hunk #2 FAILED at 65
Hunk #3 FAILED at 89
Hunk #4 FAILED at 103
Hunk #5 FAILED at 127
5 out of 5 hunks FAILED -- saving rejects to file sage/plot/circle.py.rej
patching file sage/plot/contour_plot.py
Hunk #1 FAILED at 53
Hunk #2 FAILED at 71
Hunk #3 FAILED at 116
Hunk #4 FAILED at 174
4 out of 4 hunks FAILED -- saving rejects to file sage/plot/contour_plot.py.rej
patching file sage/plot/disk.py
Hunk #1 FAILED at 52
Hunk #2 FAILED at 74
Hunk #3 FAILED at 98
3 out of 3 hunks FAILED -- saving rejects to file sage/plot/disk.py.rej
patching file sage/plot/line.py
Hunk #2 FAILED at 62
Hunk #4 FAILED at 218
Hunk #5 FAILED at 246
Hunk #6 FAILED at 320
4 out of 6 hunks FAILED -- saving rejects to file sage/plot/line.py.rej
patching file sage/plot/plot.py
Hunk #1 FAILED at 267
Hunk #2 succeeded at 433 with fuzz 2 (offset 99 lines).
Hunk #5 succeeded at 900 with fuzz 1 (offset 172 lines).
Hunk #6 FAILED at 960
Hunk #7 FAILED at 977
Hunk #8 FAILED at 987
Hunk #9 FAILED at 1004
Hunk #10 FAILED at 1071
Hunk #11 FAILED at 1119
Hunk #12 FAILED at 1191
Hunk #13 FAILED at 1292
Hunk #14 FAILED at 1388
Hunk #15 FAILED at 1513
Hunk #16 FAILED at 1549
Hunk #17 FAILED at 1637
Hunk #18 FAILED at 1665
Hunk #19 FAILED at 1684
Hunk #20 FAILED at 1769
Hunk #21 FAILED at 1854
17 out of 21 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej
patching file sage/plot/point.py
Hunk #2 FAILED at 23
Hunk #3 succeeded at 91 with fuzz 2 (offset 51 lines).
Hunk #4 FAILED at 104
Hunk #5 FAILED at 129
Hunk #6 FAILED at 138
4 out of 6 hunks FAILED -- saving rejects to file sage/plot/point.py.rej
patching file sage/plot/polygon.py
Hunk #1 FAILED at 43
Hunk #2 FAILED at 74
Hunk #3 FAILED at 90
Hunk #4 succeeded at 341 with fuzz 2 (offset 194 lines).
3 out of 4 hunks FAILED -- saving rejects to file sage/plot/polygon.py.rej
patching file sage/plot/primitive.py
Hunk #1 FAILED at 73
1 out of 1 hunks FAILED -- saving rejects to file sage/plot/primitive.py.rej
abort: patch failed to apply
```




---

archive/issue_comments_031879.json:
```json
{
    "body": "Okay, even after rebasing this needs some work - a number of the options raise DeprecationWarnings from matplotlib, the legends don't look quite right with current defaults, etc.  But this should all be doable; nothing seems to have completely changed in the meantime with respect to this.",
    "created_at": "2009-12-31T15:57:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31879",
    "user": "kcrisman"
}
```

Okay, even after rebasing this needs some work - a number of the options raise DeprecationWarnings from matplotlib, the legends don't look quite right with current defaults, etc.  But this should all be doable; nothing seems to have completely changed in the meantime with respect to this.



---

archive/issue_comments_031880.json:
```json
{
    "body": "I understand the current problem as follows.\n\n\n**Problem:** To locate where the function `text` should be applied to the function `plot` to be able to have legends for plots.\n\n**Example about the problem for one function when legend is at x=1**\n\n\n```\n   var('x');\n   x_cord = 1;\n   f = x**2;\n   p = plot(f,x)+text(f,(x_cord,f(x_cord))\n```\n\n\n\nfor one function.\n\n**Similarly for two functions (syntax may change), for instance, when all legends are at x=1:**\n\n\n\n```\n   g = x;\n   f = x**2;\n   p = plot(f,x);\n   x_cord = 1\n   (g + f) + text(f, (f,x_cord), g, (g,x_cord))             // not sure about the syntax\n```\n\n\nIf there are 7 functions, then it would be have nice to have a shortcut -command such as \n\n\n\n```\n(a + b + ... + g) + legends()\n```\n\n \nto put the legends automatically to each function.",
    "created_at": "2010-01-02T04:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31880",
    "user": "slosoi"
}
```

I understand the current problem as follows.


**Problem:** To locate where the function `text` should be applied to the function `plot` to be able to have legends for plots.

**Example about the problem for one function when legend is at x=1**


```
   var('x');
   x_cord = 1;
   f = x**2;
   p = plot(f,x)+text(f,(x_cord,f(x_cord))
```



for one function.

**Similarly for two functions (syntax may change), for instance, when all legends are at x=1:**



```
   g = x;
   f = x**2;
   p = plot(f,x);
   x_cord = 1
   (g + f) + text(f, (f,x_cord), g, (g,x_cord))             // not sure about the syntax
```


If there are 7 functions, then it would be have nice to have a shortcut -command such as 



```
(a + b + ... + g) + legends()
```

 
to put the legends automatically to each function.



---

archive/issue_comments_031881.json:
```json
{
    "body": "My understanding was that we were making a rather thin wrapper around the already-existing legends functionality in matplotlib, rather than trying to come up with our own implementation.  If we can write a better implementation, then great!  However, it's an easy first step to write a wrapper around matplotlib's implementation.  Here are some examples of matplotlib's legends:\n\n* http://matplotlib.sourceforge.net/examples/pylab_examples/dannys_example.html\n* http://matplotlib.sourceforge.net/examples/pylab_examples/figlegend_demo.html\n* http://matplotlib.sourceforge.net/examples/pylab_examples/findobj_demo.html\n* http://matplotlib.sourceforge.net/examples/pylab_examples/legend_auto.html\n* http://matplotlib.sourceforge.net/examples/pylab_examples/legend_demo3.html\n\nAs for a shortcut, I think it would be consistent to make it an option to show, like `(a+b+...+g).show(legends=True)`.",
    "created_at": "2010-01-02T06:04:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31881",
    "user": "jason"
}
```

My understanding was that we were making a rather thin wrapper around the already-existing legends functionality in matplotlib, rather than trying to come up with our own implementation.  If we can write a better implementation, then great!  However, it's an easy first step to write a wrapper around matplotlib's implementation.  Here are some examples of matplotlib's legends:

* http://matplotlib.sourceforge.net/examples/pylab_examples/dannys_example.html
* http://matplotlib.sourceforge.net/examples/pylab_examples/figlegend_demo.html
* http://matplotlib.sourceforge.net/examples/pylab_examples/findobj_demo.html
* http://matplotlib.sourceforge.net/examples/pylab_examples/legend_auto.html
* http://matplotlib.sourceforge.net/examples/pylab_examples/legend_demo3.html

As for a shortcut, I think it would be consistent to make it an option to show, like `(a+b+...+g).show(legends=True)`.



---

archive/issue_comments_031882.json:
```json
{
    "body": "Replying to [comment:22 kcrisman]:\n> Okay, even after rebasing this needs some work - a number of the options raise DeprecationWarnings from matplotlib, the legends don't look quite right with current defaults, etc.  But this should all be doable; nothing seems to have completely changed in the meantime with respect to this.  \n\nI just looked through, and the ideas behind the patch look like they are still very good and applicable.  I guess I'm not surprised that it doesn't apply; there's been a lot of reworking of plotting code in the past year.\n\nIt looks like a straightforward project to get this patch back up to speed and include it in Sage.",
    "created_at": "2010-01-02T06:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31882",
    "user": "jason"
}
```

Replying to [comment:22 kcrisman]:
> Okay, even after rebasing this needs some work - a number of the options raise DeprecationWarnings from matplotlib, the legends don't look quite right with current defaults, etc.  But this should all be doable; nothing seems to have completely changed in the meantime with respect to this.  

I just looked through, and the ideas behind the patch look like they are still very good and applicable.  I guess I'm not surprised that it doesn't apply; there's been a lot of reworking of plotting code in the past year.

It looks like a straightforward project to get this patch back up to speed and include it in Sage.



---

archive/issue_comments_031883.json:
```json
{
    "body": "Replying to [comment:26 jason]:\n> Replying to [comment:22 kcrisman]:\n> > Okay, even after rebasing this needs some work - a number of the options raise DeprecationWarnings from matplotlib, the legends don't look quite right with current defaults, etc.  But this should all be doable; nothing seems to have completely changed in the meantime with respect to this.  \n> \n> I just looked through, and the ideas behind the patch look like they are still very good and applicable.  I guess I'm not surprised that it doesn't apply; there's been a lot of reworking of plotting code in the past year.\n> \n> It looks like a straightforward project to get this patch back up to speed and include it in Sage.\n\nAgreed.  Here is a preliminary and very naive rebase - it still needs some work because of the change to save() using matplotlib(), as well as the defaults, I think, since mpl changed their legend options somewhat.",
    "created_at": "2010-01-02T13:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31883",
    "user": "kcrisman"
}
```

Replying to [comment:26 jason]:
> Replying to [comment:22 kcrisman]:
> > Okay, even after rebasing this needs some work - a number of the options raise DeprecationWarnings from matplotlib, the legends don't look quite right with current defaults, etc.  But this should all be doable; nothing seems to have completely changed in the meantime with respect to this.  
> 
> I just looked through, and the ideas behind the patch look like they are still very good and applicable.  I guess I'm not surprised that it doesn't apply; there's been a lot of reworking of plotting code in the past year.
> 
> It looks like a straightforward project to get this patch back up to speed and include it in Sage.

Agreed.  Here is a preliminary and very naive rebase - it still needs some work because of the change to save() using matplotlib(), as well as the defaults, I think, since mpl changed their legend options somewhat.



---

archive/issue_comments_031884.json:
```json
{
    "body": "Attachment\n\nBased on 4.3",
    "created_at": "2010-01-04T02:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31884",
    "user": "kcrisman"
}
```

Attachment

Based on 4.3



---

archive/issue_comments_031885.json:
```json
{
    "body": "Here is an update with (I think) all documentation correct, and with a better choice for one of the defaults.  However, it doesn't quite work right, because the initial intent was to be able to pass things like legend_loc in as a keyword to plot() or circle(), and the suboptions decorator is not working correctly.  Since I don't really understand it properly, I am putting this as needs_info for someone to tell me how to use it, or to fix what is wrong.  The place to do so is probably in SHOW_OPTIONS, show(), matplotlib(), and save() in plot.py, since that is where plot.options() looks for valid options and currently isn't finding them.",
    "created_at": "2010-01-04T03:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31885",
    "user": "kcrisman"
}
```

Here is an update with (I think) all documentation correct, and with a better choice for one of the defaults.  However, it doesn't quite work right, because the initial intent was to be able to pass things like legend_loc in as a keyword to plot() or circle(), and the suboptions decorator is not working correctly.  Since I don't really understand it properly, I am putting this as needs_info for someone to tell me how to use it, or to fix what is wrong.  The place to do so is probably in SHOW_OPTIONS, show(), matplotlib(), and save() in plot.py, since that is where plot.options() looks for valid options and currently isn't finding them.



---

archive/issue_comments_031886.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-01-04T03:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31886",
    "user": "kcrisman"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_031887.json:
```json
{
    "body": "Here is an example from contour_plot.py for using suboption:\n\n\n```\n@suboptions('label', fontsize=9, colors='blue', inline=None, inline_spacing=3, fmt=\"%1.2f\")\n```\n\n\nSo I think you need to specify the options that you are passing in, and their default values, in the `@`suboption decorator, rather than as a dictionary in your plotting function.  This will make the following keyword arguments available:\n\nlabel_fontsize, label_colors, label_inline, label_inline_spacing, label_fmt\n\nInside the function, though, you will see all of these keyword arguments as a single dictionary called label, and you'll access the options as label['fontsize'], label['colors'], label['inline'], etc.\n\nDoes that explanation help?",
    "created_at": "2010-05-25T15:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31887",
    "user": "jason"
}
```

Here is an example from contour_plot.py for using suboption:


```
@suboptions('label', fontsize=9, colors='blue', inline=None, inline_spacing=3, fmt="%1.2f")
```


So I think you need to specify the options that you are passing in, and their default values, in the `@`suboption decorator, rather than as a dictionary in your plotting function.  This will make the following keyword arguments available:

label_fontsize, label_colors, label_inline, label_inline_spacing, label_fmt

Inside the function, though, you will see all of these keyword arguments as a single dictionary called label, and you'll access the options as label['fontsize'], label['colors'], label['inline'], etc.

Does that explanation help?



---

archive/issue_comments_031888.json:
```json
{
    "body": "Boy, that got munged by wiki syntax.  You'll have access to the options as `label['fontsize']`, `label['colors']`, etc.",
    "created_at": "2010-05-25T15:49:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31888",
    "user": "jason"
}
```

Boy, that got munged by wiki syntax.  You'll have access to the options as `label['fontsize']`, `label['colors']`, etc.



---

archive/issue_comments_031889.json:
```json
{
    "body": "Yikes, once again needs major rebasing:\n\n```\npatching file sage/plot/circle.py\nHunk #2 FAILED at 149\n1 out of 6 hunks FAILED -- saving rejects to file sage/plot/circle.py.rej\npatching file sage/plot/contour_plot.py\nHunk #1 succeeded at 115 with fuzz 2 (offset 2 lines).\nHunk #2 FAILED at 165\nHunk #3 FAILED at 177\nHunk #4 FAILED at 243\nHunk #5 succeeded at 513 with fuzz 2 (offset 117 lines).\n3 out of 5 hunks FAILED -- saving rejects to file sage/plot/contour_plot.py.rej\npatching file sage/plot/plot.py\nHunk #11 FAILED at 2291\n1 out of 15 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej\npatching file sage/plot/point.py\nHunk #3 FAILED at 89\nHunk #5 FAILED at 301\nHunk #6 succeeded at 336 with fuzz 2 (offset 0 lines).\n2 out of 7 hunks FAILED -- saving rejects to file sage/plot/point.py.rej\npatching file sage/plot/arrow.py\nHunk #1 FAILED at 75\nHunk #2 FAILED at 83\nHunk #3 FAILED at 131\nHunk #4 FAILED at 196\nHunk #5 succeeded at 91 with fuzz 2 (offset -118 lines).\nHunk #6 FAILED at 315\nHunk #7 succeeded at 361 with fuzz 2 (offset 8 lines).\nHunk #8 succeeded at 395 with fuzz 2 (offset 12 lines).\nHunk #9 FAILED at 400\n6 out of 9 hunks FAILED -- saving rejects to file sage/plot/arrow.py.rej\npatching file sage/plot/bar_chart.py\nHunk #1 FAILED at 62\nHunk #2 FAILED at 105\nHunk #3 succeeded at 133 with fuzz 2 (offset 2 lines).\nHunk #4 FAILED at 161\n3 out of 4 hunks FAILED -- saving rejects to file sage/plot/bar_chart.py.rej\npatching file sage/plot/circle.py\nHunk #1 FAILED at 107\nHunk #2 FAILED at 148\nHunk #3 FAILED at 205\nHunk #4 succeeded at 237 with fuzz 2 (offset 5 lines).\nHunk #5 succeeded at 288 with fuzz 2 (offset 9 lines).\nHunk #6 FAILED at 298\n4 out of 6 hunks FAILED -- saving rejects to file sage/plot/circle.py.rej\npatching file sage/plot/contour_plot.py\nHunk #1 FAILED at 110\nHunk #2 FAILED at 164\nHunk #3 FAILED at 176\nHunk #4 FAILED at 239\nHunk #5 succeeded at 515 with fuzz 2 (offset 120 lines).\n4 out of 5 hunks FAILED -- saving rejects to file sage/plot/contour_plot.py.rej\npatching file sage/plot/disk.py\nHunk #1 FAILED at 117\nHunk #2 FAILED at 154\nHunk #3 FAILED at 212\nHunk #4 FAILED at 279\n4 out of 4 hunks FAILED -- saving rejects to file sage/plot/disk.py.rej\npatching file sage/plot/line.py\nHunk #1 FAILED at 59\nHunk #2 FAILED at 71\nHunk #3 FAILED at 214\nHunk #4 FAILED at 243\nHunk #5 succeeded at 271 with fuzz 2 (offset 6 lines).\nHunk #6 succeeded at 402 with fuzz 2 (offset 10 lines).\nHunk #7 FAILED at 403\n5 out of 7 hunks FAILED -- saving rejects to file sage/plot/line.py.rej\npatching file sage/plot/plot.py\nHunk #2 FAILED at 371\nHunk #3 FAILED at 434\nHunk #4 succeeded at 676 with fuzz 2 (offset 176 lines).\nHunk #5 FAILED at 1223\nHunk #6 FAILED at 1245\nHunk #7 FAILED at 1257\nHunk #8 FAILED at 1341\nHunk #9 succeeded at 1608 with fuzz 2 (offset 186 lines).\nHunk #10 FAILED at 1724\nHunk #11 FAILED at 1808\nHunk #13 FAILED at 2258\nHunk #14 succeeded at 2518 with fuzz 2 (offset 211 lines).\nHunk #15 succeeded at 2658 with fuzz 2 (offset 219 lines).\nHunk #16 FAILED at 2714\nHunk #17 FAILED at 2821\n11 out of 17 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej\npatching file sage/plot/point.py\nHunk #1 FAILED at 8\nHunk #2 FAILED at 27\nHunk #3 FAILED at 89\nHunk #4 FAILED at 268\nHunk #5 FAILED at 301\nHunk #6 succeeded at 340 with fuzz 2 (offset 4 lines).\nHunk #7 FAILED at 347\n6 out of 7 hunks FAILED -- saving rejects to file sage/plot/point.py.rej\npatching file sage/plot/polygon.py\nHunk #1 FAILED at 140\nHunk #2 FAILED at 157\nHunk #3 FAILED at 237\nHunk #4 FAILED at 265\nHunk #5 FAILED at 281\nHunk #6 FAILED at 338\n6 out of 6 hunks FAILED -- saving rejects to file sage/plot/polygon.py.rej\npatching file sage/plot/primitive.py\nHunk #1 FAILED at 105\n1 out of 1 hunks FAILED -- saving rejects to file sage/plot/primitive.py.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2010-05-25T19:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31889",
    "user": "kcrisman"
}
```

Yikes, once again needs major rebasing:

```
patching file sage/plot/circle.py
Hunk #2 FAILED at 149
1 out of 6 hunks FAILED -- saving rejects to file sage/plot/circle.py.rej
patching file sage/plot/contour_plot.py
Hunk #1 succeeded at 115 with fuzz 2 (offset 2 lines).
Hunk #2 FAILED at 165
Hunk #3 FAILED at 177
Hunk #4 FAILED at 243
Hunk #5 succeeded at 513 with fuzz 2 (offset 117 lines).
3 out of 5 hunks FAILED -- saving rejects to file sage/plot/contour_plot.py.rej
patching file sage/plot/plot.py
Hunk #11 FAILED at 2291
1 out of 15 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej
patching file sage/plot/point.py
Hunk #3 FAILED at 89
Hunk #5 FAILED at 301
Hunk #6 succeeded at 336 with fuzz 2 (offset 0 lines).
2 out of 7 hunks FAILED -- saving rejects to file sage/plot/point.py.rej
patching file sage/plot/arrow.py
Hunk #1 FAILED at 75
Hunk #2 FAILED at 83
Hunk #3 FAILED at 131
Hunk #4 FAILED at 196
Hunk #5 succeeded at 91 with fuzz 2 (offset -118 lines).
Hunk #6 FAILED at 315
Hunk #7 succeeded at 361 with fuzz 2 (offset 8 lines).
Hunk #8 succeeded at 395 with fuzz 2 (offset 12 lines).
Hunk #9 FAILED at 400
6 out of 9 hunks FAILED -- saving rejects to file sage/plot/arrow.py.rej
patching file sage/plot/bar_chart.py
Hunk #1 FAILED at 62
Hunk #2 FAILED at 105
Hunk #3 succeeded at 133 with fuzz 2 (offset 2 lines).
Hunk #4 FAILED at 161
3 out of 4 hunks FAILED -- saving rejects to file sage/plot/bar_chart.py.rej
patching file sage/plot/circle.py
Hunk #1 FAILED at 107
Hunk #2 FAILED at 148
Hunk #3 FAILED at 205
Hunk #4 succeeded at 237 with fuzz 2 (offset 5 lines).
Hunk #5 succeeded at 288 with fuzz 2 (offset 9 lines).
Hunk #6 FAILED at 298
4 out of 6 hunks FAILED -- saving rejects to file sage/plot/circle.py.rej
patching file sage/plot/contour_plot.py
Hunk #1 FAILED at 110
Hunk #2 FAILED at 164
Hunk #3 FAILED at 176
Hunk #4 FAILED at 239
Hunk #5 succeeded at 515 with fuzz 2 (offset 120 lines).
4 out of 5 hunks FAILED -- saving rejects to file sage/plot/contour_plot.py.rej
patching file sage/plot/disk.py
Hunk #1 FAILED at 117
Hunk #2 FAILED at 154
Hunk #3 FAILED at 212
Hunk #4 FAILED at 279
4 out of 4 hunks FAILED -- saving rejects to file sage/plot/disk.py.rej
patching file sage/plot/line.py
Hunk #1 FAILED at 59
Hunk #2 FAILED at 71
Hunk #3 FAILED at 214
Hunk #4 FAILED at 243
Hunk #5 succeeded at 271 with fuzz 2 (offset 6 lines).
Hunk #6 succeeded at 402 with fuzz 2 (offset 10 lines).
Hunk #7 FAILED at 403
5 out of 7 hunks FAILED -- saving rejects to file sage/plot/line.py.rej
patching file sage/plot/plot.py
Hunk #2 FAILED at 371
Hunk #3 FAILED at 434
Hunk #4 succeeded at 676 with fuzz 2 (offset 176 lines).
Hunk #5 FAILED at 1223
Hunk #6 FAILED at 1245
Hunk #7 FAILED at 1257
Hunk #8 FAILED at 1341
Hunk #9 succeeded at 1608 with fuzz 2 (offset 186 lines).
Hunk #10 FAILED at 1724
Hunk #11 FAILED at 1808
Hunk #13 FAILED at 2258
Hunk #14 succeeded at 2518 with fuzz 2 (offset 211 lines).
Hunk #15 succeeded at 2658 with fuzz 2 (offset 219 lines).
Hunk #16 FAILED at 2714
Hunk #17 FAILED at 2821
11 out of 17 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej
patching file sage/plot/point.py
Hunk #1 FAILED at 8
Hunk #2 FAILED at 27
Hunk #3 FAILED at 89
Hunk #4 FAILED at 268
Hunk #5 FAILED at 301
Hunk #6 succeeded at 340 with fuzz 2 (offset 4 lines).
Hunk #7 FAILED at 347
6 out of 7 hunks FAILED -- saving rejects to file sage/plot/point.py.rej
patching file sage/plot/polygon.py
Hunk #1 FAILED at 140
Hunk #2 FAILED at 157
Hunk #3 FAILED at 237
Hunk #4 FAILED at 265
Hunk #5 FAILED at 281
Hunk #6 FAILED at 338
6 out of 6 hunks FAILED -- saving rejects to file sage/plot/polygon.py.rej
patching file sage/plot/primitive.py
Hunk #1 FAILED at 105
1 out of 1 hunks FAILED -- saving rejects to file sage/plot/primitive.py.rej
abort: patch failed to apply
```




---

archive/issue_comments_031890.json:
```json
{
    "body": "If you rebase, I'll try to make it a priority to review quickly so we don't have to rebase again!",
    "created_at": "2010-05-25T19:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31890",
    "user": "jason"
}
```

If you rebase, I'll try to make it a priority to review quickly so we don't have to rebase again!



---

archive/issue_comments_031891.json:
```json
{
    "body": "[\u043e\u0434\u0435\u0441\u0441\u043a\u0430\u044f \u0434\u043e\u0441\u043a\u0430 \u0431\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u044b\u0445 \u043e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u0439](http://docka.kiev.ua/)",
    "created_at": "2010-05-26T08:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31891",
    "user": "bascorp2"
}
```

[одесская доска бесплатных объявлений](http://docka.kiev.ua/)



---

archive/issue_comments_031892.json:
```json
{
    "body": "based on 4.4.2",
    "created_at": "2010-05-26T14:07:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31892",
    "user": "kcrisman"
}
```

based on 4.4.2



---

archive/issue_comments_031893.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-05-26T14:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31893",
    "user": "kcrisman"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_031894.json:
```json
{
    "body": "Attachment\n\nReady for review.  I made legend -> show_legend and that seems to clear up the problems with the `@`suboptions dictionary.  I expect it to be \"needs work\", by the way, but I want extensive testing of this.  Things to watch out for include:\n\n* Whether there are any missing/needed plot3d method removals\n\n* What the defaults should really be for all the legend_options; I don't think they are that good.\n\n* Whether there are any other places where a KeyError might arise.\n\nIncidentally, the rebase wasn't quite as bad as it seemed - the earlier patch for some reason was a \"double patch\" that sometimes occurs, as will be obvious if read the above (which I didn't).",
    "created_at": "2010-05-26T14:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31894",
    "user": "kcrisman"
}
```

Attachment

Ready for review.  I made legend -> show_legend and that seems to clear up the problems with the `@`suboptions dictionary.  I expect it to be "needs work", by the way, but I want extensive testing of this.  Things to watch out for include:

* Whether there are any missing/needed plot3d method removals

* What the defaults should really be for all the legend_options; I don't think they are that good.

* Whether there are any other places where a KeyError might arise.

Incidentally, the rebase wasn't quite as bad as it seemed - the earlier patch for some reason was a "double patch" that sometimes occurs, as will be obvious if read the above (which I didn't).



---

archive/issue_comments_031895.json:
```json
{
    "body": "This applies cleanly against sage-4.6.alpha0, and most things seem to work well.\n\nI'm not sure I understand Jason's point about the suboptions and contour_plot.  It does seem like that while contour_plot accepts the legend_label argument, it doesn't do anything.  I'm not sure that's a deal-breaker though, maybe we can just add a note in the contour_plot docstring about that given contour_plot's nice sidebar functionality.\n\nAt least on my system (mac 10.5, firefox), font_style='italic' doesn't do anything.  Other font options seem to work though.\n\nSince the default behavior is to have this turned off, I am hoping this can get a positive review pretty soon.  It may not be perfect but it seems good enough for incremental improvement.  I will not give it a positive review myself yet since I don't understand all the issues.",
    "created_at": "2010-09-12T14:19:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31895",
    "user": "mhampton"
}
```

This applies cleanly against sage-4.6.alpha0, and most things seem to work well.

I'm not sure I understand Jason's point about the suboptions and contour_plot.  It does seem like that while contour_plot accepts the legend_label argument, it doesn't do anything.  I'm not sure that's a deal-breaker though, maybe we can just add a note in the contour_plot docstring about that given contour_plot's nice sidebar functionality.

At least on my system (mac 10.5, firefox), font_style='italic' doesn't do anything.  Other font options seem to work though.

Since the default behavior is to have this turned off, I am hoping this can get a positive review pretty soon.  It may not be perfect but it seems good enough for incremental improvement.  I will not give it a positive review myself yet since I don't understand all the issues.



---

archive/issue_comments_031896.json:
```json
{
    "body": "I browsed through the patch, and things look okay.  I'm downloading sage 4.6alpha so I can try it out.",
    "created_at": "2010-09-28T02:51:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31896",
    "user": "jason"
}
```

I browsed through the patch, and things look okay.  I'm downloading sage 4.6alpha so I can try it out.



---

archive/issue_comments_031897.json:
```json
{
    "body": "I rebased the patch for 4.6.alpha1 (depends on #9740 and #9746).  I also fixed a few small doc formatting issues.\n\nI'm going to doctest it all now.",
    "created_at": "2010-09-28T17:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31897",
    "user": "jason"
}
```

I rebased the patch for 4.6.alpha1 (depends on #9740 and #9746).  I also fixed a few small doc formatting issues.

I'm going to doctest it all now.



---

archive/issue_comments_031898.json:
```json
{
    "body": "When I build the docs `sage -docbuild reference html`, I get\n\n\n```\n/Users/grout/sage/devel/sage/doc/en/reference/sage/plot/plot.rst:1070: (ERROR/3) Unknown target name: \"legend\".\n```\n\n\nI can't find where this error is.",
    "created_at": "2010-09-28T17:45:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31898",
    "user": "jason"
}
```

When I build the docs `sage -docbuild reference html`, I get


```
/Users/grout/sage/devel/sage/doc/en/reference/sage/plot/plot.rst:1070: (ERROR/3) Unknown target name: "legend".
```


I can't find where this error is.



---

archive/issue_comments_031899.json:
```json
{
    "body": "I can't give this a positive review since I helped write the last iteration.\n\nI am not sure what's going on with the docbuild either.  `reference/plotting.rst` is where things come from, but it refers of course to all the usual files.",
    "created_at": "2010-09-28T18:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31899",
    "user": "kcrisman"
}
```

I can't give this a positive review since I helped write the last iteration.

I am not sure what's going on with the docbuild either.  `reference/plotting.rst` is where things come from, but it refers of course to all the usual files.



---

archive/issue_comments_031900.json:
```json
{
    "body": "I think that username anakha is really abergeron in a previous username incarnation. [Here](https://gna.org/users/anakha) is one example.",
    "created_at": "2010-09-28T18:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31900",
    "user": "kcrisman"
}
```

I think that username anakha is really abergeron in a previous username incarnation. [Here](https://gna.org/users/anakha) is one example.



---

archive/issue_comments_031901.json:
```json
{
    "body": "Okay, once we figure out where that problem with plotting.rst is, positive review.\n\nptestlong passes with the following tickets applied in order: #9221 (and new spkg), #9740, #9746, #4342.",
    "created_at": "2010-09-28T19:07:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31901",
    "user": "jason"
}
```

Okay, once we figure out where that problem with plotting.rst is, positive review.

ptestlong passes with the following tickets applied in order: #9221 (and new spkg), #9740, #9746, #4342.



---

archive/issue_comments_031902.json:
```json
{
    "body": "CCing two sphinx experts.  When we apply trac-4342-rebase-4.6.alpha1.patch (only), we get the following error when building docs:\n\n\n```\n/Users/grout/sage/devel/sage/doc/en/reference/sage/plot/plot.rst:1070: (ERROR/3) Unknown target name: \"legend\".\n```\n\n\nWe don't know where it is coming from.  Do you guys have any idea?\n\nPlease note that this ticket depends on #9740, then #9746.",
    "created_at": "2010-09-28T19:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31902",
    "user": "jason"
}
```

CCing two sphinx experts.  When we apply trac-4342-rebase-4.6.alpha1.patch (only), we get the following error when building docs:


```
/Users/grout/sage/devel/sage/doc/en/reference/sage/plot/plot.rst:1070: (ERROR/3) Unknown target name: "legend".
```


We don't know where it is coming from.  Do you guys have any idea?

Please note that this ticket depends on #9740, then #9746.



---

archive/issue_comments_031903.json:
```json
{
    "body": "In the line\n\n```\n        - ``legend_*`` - all the options valid for :meth:`set_legend_options` prefixed with 'legend_'\n```\n\nyou need to change `'legend_'` to ```legend_```.  Sphinx (maybe ReST?) gives special meaning to strings ending in underscores.",
    "created_at": "2010-09-28T19:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31903",
    "user": "jhpalmieri"
}
```

In the line

```
        - ``legend_*`` - all the options valid for :meth:`set_legend_options` prefixed with 'legend_'
```

you need to change `'legend_'` to ```legend_```.  Sphinx (maybe ReST?) gives special meaning to strings ending in underscores.



---

archive/issue_comments_031904.json:
```json
{
    "body": "ah, those are citation references, aren't they?  Thanks!",
    "created_at": "2010-09-28T19:45:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31904",
    "user": "jason"
}
```

ah, those are citation references, aren't they?  Thanks!



---

archive/issue_comments_031905.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-28T19:47:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31905",
    "user": "jason"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_031906.json:
```json
{
    "body": "John's fix is in the last patch.\n\nRelease manager: please merge trac-4342-rebase-4.6.alpha1.patch, then 4342-fix-docs.patch.\n\nPositive review.  Good job, everyone!  Sorry this took so long to review!",
    "created_at": "2010-09-28T19:47:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31906",
    "user": "jason"
}
```

John's fix is in the last patch.

Release manager: please merge trac-4342-rebase-4.6.alpha1.patch, then 4342-fix-docs.patch.

Positive review.  Good job, everyone!  Sorry this took so long to review!



---

archive/issue_comments_031907.json:
```json
{
    "body": "Attachment\n\napply only this patch; rebased to 4.6.alpha1",
    "created_at": "2010-09-28T20:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31907",
    "user": "jason"
}
```

Attachment

apply only this patch; rebased to 4.6.alpha1



---

archive/issue_comments_031908.json:
```json
{
    "body": "Attachment\n\napply on top of previous patches",
    "created_at": "2010-09-28T20:08:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31908",
    "user": "jason"
}
```

Attachment

apply on top of previous patches



---

archive/issue_comments_031909.json:
```json
{
    "body": "(I rebased to account for some changes on #9740)",
    "created_at": "2010-09-28T20:08:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31909",
    "user": "jason"
}
```

(I rebased to account for some changes on #9740)



---

archive/issue_comments_031910.json:
```json
{
    "body": "Replying to [comment:48 jason]:\n> (I rebased to account for some changes on #9740)\nCorrect - see the ticket order a few comments ago. Applies fine to the latest changes at #9740.",
    "created_at": "2010-09-28T20:16:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31910",
    "user": "kcrisman"
}
```

Replying to [comment:48 jason]:
> (I rebased to account for some changes on #9740)
Correct - see the ticket order a few comments ago. Applies fine to the latest changes at #9740.



---

archive/issue_comments_031911.json:
```json
{
    "body": "Do #9740, #9746 and #4342 depend on #9221?",
    "created_at": "2010-09-30T03:21:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31911",
    "user": "mpatel"
}
```

Do #9740, #9746 and #4342 depend on #9221?



---

archive/issue_comments_031912.json:
```json
{
    "body": "Replying to [comment:50 mpatel]:\n\n> Do #9740, #9746 and #4342 depend on #9221?\n\nI don't think so.  I originally tested them all without #9221.",
    "created_at": "2010-09-30T04:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31912",
    "user": "jason"
}
```

Replying to [comment:50 mpatel]:

> Do #9740, #9746 and #4342 depend on #9221?

I don't think so.  I originally tested them all without #9221.



---

archive/issue_comments_031913.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-10-03T06:35:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4342#issuecomment-31913",
    "user": "mpatel"
}
```

Resolution: fixed
