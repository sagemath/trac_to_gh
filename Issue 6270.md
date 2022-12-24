# Issue 6270: [with patch, needs review] add some files from the plot directory to the reference manual

archive/issues_006270.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nThis adds the 8 files to the reference manual (since kcrisman has put so much work into getting them to 100% coverage).  It also adds a few cross-references to plot.py and makes one or two small changes (e.g., it removes a reference to `rgbcolor` at the beginning of plot.py, since that function isn't in the global name space, and its mention suggested that it might be).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6270\n\n",
    "created_at": "2009-06-12T18:20:59Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "title": "[with patch, needs review] add some files from the plot directory to the reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6270",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

This adds the 8 files to the reference manual (since kcrisman has put so much work into getting them to 100% coverage).  It also adds a few cross-references to plot.py and makes one or two small changes (e.g., it removes a reference to `rgbcolor` at the beginning of plot.py, since that function isn't in the global name space, and its mention suggested that it might be).


Issue created by migration from https://trac.sagemath.org/ticket/6270





---

archive/issue_comments_050093.json:
```json
{
    "body": "Attachment [trac_6270.patch](tarball://root/attachments/some-uuid/ticket6270/trac_6270.patch) by mvngu created at 2009-06-12 19:35:26\n\nWhen applying the patch, I got the following hunk failures:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: 6270\nsage: hg_sage.apply(\"../patch/6270/trac_6270.patch\")\ncd \"/scratch/mvngu/sage-4.0.1/devel/sage\" && hg status\ncd \"/scratch/mvngu/sage-4.0.1/devel/sage\" && hg status\ncd \"/scratch/mvngu/sage-4.0.1/devel/sage\" && hg import   \"/scratch/mvngu/patch/6270/trac_6270.patch\"\napplying /scratch/mvngu/patch/6270/trac_6270.patch\npatching file sage/plot/plot.py\nHunk #1 FAILED at 6\nHunk #2 FAILED at 1865\n2 out of 2 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej\nabort: patch failed to apply\n```\n\nThe patch was applied on a fresh clone of Sage 4.0.1. Should there be a rebase?",
    "created_at": "2009-06-12T19:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6270",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6270#issuecomment-50093",
    "user": "mvngu"
}
```

Attachment [trac_6270.patch](tarball://root/attachments/some-uuid/ticket6270/trac_6270.patch) by mvngu created at 2009-06-12 19:35:26

When applying the patch, I got the following hunk failures:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: 6270
sage: hg_sage.apply("../patch/6270/trac_6270.patch")
cd "/scratch/mvngu/sage-4.0.1/devel/sage" && hg status
cd "/scratch/mvngu/sage-4.0.1/devel/sage" && hg status
cd "/scratch/mvngu/sage-4.0.1/devel/sage" && hg import   "/scratch/mvngu/patch/6270/trac_6270.patch"
applying /scratch/mvngu/patch/6270/trac_6270.patch
patching file sage/plot/plot.py
Hunk #1 FAILED at 6
Hunk #2 FAILED at 1865
2 out of 2 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej
abort: patch failed to apply
```

The patch was applied on a fresh clone of Sage 4.0.1. Should there be a rebase?



---

archive/issue_comments_050094.json:
```json
{
    "body": "I'm sorry -- I forgot to say that this patch depends on #6257.  Please apply that one first and try again.",
    "created_at": "2009-06-12T19:56:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6270",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6270#issuecomment-50094",
    "user": "jhpalmieri"
}
```

I'm sorry -- I forgot to say that this patch depends on #6257.  Please apply that one first and try again.



---

archive/issue_comments_050095.json:
```json
{
    "body": "You might want to look at # 6269 as well regarding the rgbcolor thing; I have potentially moved that and hue to a new file.",
    "created_at": "2009-06-13T03:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6270",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6270#issuecomment-50095",
    "user": "kcrisman"
}
```

You might want to look at # 6269 as well regarding the rgbcolor thing; I have potentially moved that and hue to a new file.



---

archive/issue_comments_050096.json:
```json
{
    "body": "After applying the patch, the following modules are in the reference manual, but the ReST formatting need some polishing:\n\n```\nsage/plot/circle\nsage/plot/disk\n```\n\nThe following are referred to in the reference manual, but are not yet in the manual. So there's no hyperlink to any of them even if one is defined.\n\n```\nline()\nimplicit_plot()\nregion_plot()\nscatter_plot()\nbar_chart()\ncontour_plot()\ndensity_plot()\nplot_vector_field()\nplot_slope_field()\nmatrix_plot()\ncomplex_plot()\n```\n\nI can give the patch a positive review for adding files under the `sage/plot` directory to the reference manual. The formatting and referencing issues I mentioned above are **not** introduced by the patch, and should be addressed in another ticket. So patches should be applied in the following order:\n1. apply the patch at #6257\n2. then apply the patch on this ticket.",
    "created_at": "2009-06-13T11:04:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6270",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6270#issuecomment-50096",
    "user": "mvngu"
}
```

After applying the patch, the following modules are in the reference manual, but the ReST formatting need some polishing:

```
sage/plot/circle
sage/plot/disk
```

The following are referred to in the reference manual, but are not yet in the manual. So there's no hyperlink to any of them even if one is defined.

```
line()
implicit_plot()
region_plot()
scatter_plot()
bar_chart()
contour_plot()
density_plot()
plot_vector_field()
plot_slope_field()
matrix_plot()
complex_plot()
```

I can give the patch a positive review for adding files under the `sage/plot` directory to the reference manual. The formatting and referencing issues I mentioned above are **not** introduced by the patch, and should be addressed in another ticket. So patches should be applied in the following order:
1. apply the patch at #6257
2. then apply the patch on this ticket.



---

archive/issue_comments_050097.json:
```json
{
    "body": "See #6274 for a follow-up to this ticket.",
    "created_at": "2009-06-13T12:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6270",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6270#issuecomment-50097",
    "user": "mvngu"
}
```

See #6274 for a follow-up to this ticket.



---

archive/issue_comments_050098.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T21:42:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6270",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6270#issuecomment-50098",
    "user": "ncalexan"
}
```

Resolution: fixed
