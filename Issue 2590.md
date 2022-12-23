# Issue 2590: plotting a line with no points throws a nonsensical error

archive/issues_002590.json:
```json
{
    "body": "Assignee: was\n\nThe first attached patch returns an empty graphic when plotting a line with no points.\n\nThis addresses the concern in #2038 about not having any valid points in a plot (by returning an empty plot).\n\nThe second patch modifies using a tidbit from moretti's patch in #2038---he should get credit for it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2590\n\n",
    "created_at": "2008-03-19T01:38:27Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "plotting a line with no points throws a nonsensical error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2590",
    "user": "jason"
}
```
Assignee: was

The first attached patch returns an empty graphic when plotting a line with no points.

This addresses the concern in #2038 about not having any valid points in a plot (by returning an empty plot).

The second patch modifies using a tidbit from moretti's patch in #2038---he should get credit for it.

Issue created by migration from https://trac.sagemath.org/ticket/2590





---

archive/issue_comments_017724.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-19T01:38:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2590#issuecomment-17724",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_017725.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-19T01:43:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2590#issuecomment-17725",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_017726.json:
```json
{
    "body": "If I apply those two patches I get an additional doctest failure besides the one caused by #2583:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha0$ ./sage -t -long devel/sage/sage/plot/plot.py\nsage -t -long devel/sage-main/sage/plot/plot.py             **********************************************************************\nFile \"plot.py\", line 3466:\n    sage: p[0][1][0]\nExpected:\n    -0.66666666666666...\nGot:\n    -0.5\n**********************************************************************\nFile \"plot.py\", line 3513:\n    sage: plot(x^(1/3), (x,-1,1))\nExpected nothing\nGot:\n    WARNING: When plotting, failed to evaluate function at 99 points.\n    Last error message: 'negative number cannot be raised to a fractional power'\n    <BLANKLINE>\n**********************************************************************\n1 items had failures:\n   2 of  28 in __main__.example_111\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file .doctest_plot.py\n         [70.3 s]\nexit code: 256\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-03-19T10:13:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2590#issuecomment-17726",
    "user": "mabshoff"
}
```

If I apply those two patches I get an additional doctest failure besides the one caused by #2583:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha0$ ./sage -t -long devel/sage/sage/plot/plot.py
sage -t -long devel/sage-main/sage/plot/plot.py             **********************************************************************
File "plot.py", line 3466:
    sage: p[0][1][0]
Expected:
    -0.66666666666666...
Got:
    -0.5
**********************************************************************
File "plot.py", line 3513:
    sage: plot(x^(1/3), (x,-1,1))
Expected nothing
Got:
    WARNING: When plotting, failed to evaluate function at 99 points.
    Last error message: 'negative number cannot be raised to a fractional power'
    <BLANKLINE>
**********************************************************************
1 items had failures:
   2 of  28 in __main__.example_111
***Test Failed*** 2 failures.
For whitespace errors, see the file .doctest_plot.py
         [70.3 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:

```


Cheers,

Michael



---

archive/issue_comments_017727.json:
```json
{
    "body": "Attachment\n\napply instead of plot_use_data.patch",
    "created_at": "2008-03-19T15:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2590#issuecomment-17727",
    "user": "jason"
}
```

Attachment

apply instead of plot_use_data.patch



---

archive/issue_comments_017728.json:
```json
{
    "body": "The plot_use_data-2.patch fixes the doctest failures.  I also realized the docs for plot_division were incorrect, so that is corrected.\n\nScore one more for doctests---they helped find both the off-by-one error fixed in the patch and the incorrect plot_division documentation.\n\nApply zero-point-line.patch and plot_use_data-2.patch and don't apply plot_use_data.patch.",
    "created_at": "2008-03-19T15:44:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2590#issuecomment-17728",
    "user": "jason"
}
```

The plot_use_data-2.patch fixes the doctest failures.  I also realized the docs for plot_division were incorrect, so that is corrected.

Score one more for doctests---they helped find both the off-by-one error fixed in the patch and the incorrect plot_division documentation.

Apply zero-point-line.patch and plot_use_data-2.patch and don't apply plot_use_data.patch.



---

archive/issue_comments_017729.json:
```json
{
    "body": "Jason, this patch set needs rebasing past 2.11.alpha2.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-28T08:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2590#issuecomment-17729",
    "user": "mabshoff"
}
```

Jason, this patch set needs rebasing past 2.11.alpha2.

Cheers,

Michael



---

archive/issue_comments_017730.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-09T04:22:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2590#issuecomment-17730",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_017731.json:
```json
{
    "body": "Apply trac-2590-rebased.patch only.  This is a rebased version of all previous changes, rebased to sage 3.0alpha2.\n\nDoctests in sage/plot/ pass.",
    "created_at": "2008-04-09T04:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2590#issuecomment-17731",
    "user": "jason"
}
```

Apply trac-2590-rebased.patch only.  This is a rebased version of all previous changes, rebased to sage 3.0alpha2.

Doctests in sage/plot/ pass.



---

archive/issue_comments_017732.json:
```json
{
    "body": "trac-2590-rebased.patch applied against my 3.0.alpha3 merge tree doctests fine. I am no expert on the code in question, so somebody else needs to review it.\n\nThumbs up from me.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-09T04:44:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2590#issuecomment-17732",
    "user": "mabshoff"
}
```

trac-2590-rebased.patch applied against my 3.0.alpha3 merge tree doctests fine. I am no expert on the code in question, so somebody else needs to review it.

Thumbs up from me.

Cheers,

Michael



---

archive/issue_comments_017733.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-12T07:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2590#issuecomment-17733",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_017734.json:
```json
{
    "body": "Merged trac-2590-rebased.patch in Sage 3.0.alpha4",
    "created_at": "2008-04-12T11:29:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2590#issuecomment-17734",
    "user": "mabshoff"
}
```

Merged trac-2590-rebased.patch in Sage 3.0.alpha4



---

archive/issue_comments_017735.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-12T11:29:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2590#issuecomment-17735",
    "user": "mabshoff"
}
```

Resolution: fixed
