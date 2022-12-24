# Issue 2769: matplotlib produces invalid PDFs with axes=False

archive/issues_002769.json:
```json
{
    "body": "Assignee: was\n\nKeywords: pdf, plot, matplotlib, axes\n\nWhen saving plots without axes, matplotlib produces invalid PDFs:\n\n\n```\np = plot(x^2, x, 0, 1)\np.save('withaxes.pdf')\np.save('withoutaxes.pdf', axes=False)\n```\n\n\nthe second file is not valid; if you use it in a LaTeX document, it makes the text shrink for the rest of the page -- see the attached PDF. If you try to convert withoutaxes.pdf to postscript using pdf2ps, you get:\n\n\n```\ndrake@sansu5:~$ pdf2ps withoutaxes.pdf \n   **** Warning: File has imbalanced q/Q operators (too many q's)\n\n   **** This file had errors that were repaired or ignored.\n   **** The file was produced by: \n   **** >>>> matplotlib pdf backend <<<<\n   **** Please notify the author of the software that produced this\n   **** file that it does not conform to Adobe's published PDF\n   **** specification.\n```\n\n\nThis is probably a matplotlib problem, and I think it's [been noticed and fixed in the most recent version](http://www.nabble.com/Problem-with-matplotlib-and-pdflatex-td16210144.html).\n\nIssue created by migration from https://trac.sagemath.org/ticket/2769\n\n",
    "created_at": "2008-04-02T06:31:26Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "matplotlib produces invalid PDFs with axes=False",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2769",
    "user": "ddrake"
}
```
Assignee: was

Keywords: pdf, plot, matplotlib, axes

When saving plots without axes, matplotlib produces invalid PDFs:


```
p = plot(x^2, x, 0, 1)
p.save('withaxes.pdf')
p.save('withoutaxes.pdf', axes=False)
```


the second file is not valid; if you use it in a LaTeX document, it makes the text shrink for the rest of the page -- see the attached PDF. If you try to convert withoutaxes.pdf to postscript using pdf2ps, you get:


```
drake@sansu5:~$ pdf2ps withoutaxes.pdf 
   **** Warning: File has imbalanced q/Q operators (too many q's)

   **** This file had errors that were repaired or ignored.
   **** The file was produced by: 
   **** >>>> matplotlib pdf backend <<<<
   **** Please notify the author of the software that produced this
   **** file that it does not conform to Adobe's published PDF
   **** specification.
```


This is probably a matplotlib problem, and I think it's [been noticed and fixed in the most recent version](http://www.nabble.com/Problem-with-matplotlib-and-pdflatex-td16210144.html).

Issue created by migration from https://trac.sagemath.org/ticket/2769





---

archive/issue_comments_019027.json:
```json
{
    "body": "Attachment [axes.pdf](tarball://root/attachments/some-uuid/ticket2769/axes.pdf) by ddrake created at 2008-04-02 06:32:07",
    "created_at": "2008-04-02T06:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2769#issuecomment-19027",
    "user": "ddrake"
}
```

Attachment [axes.pdf](tarball://root/attachments/some-uuid/ticket2769/axes.pdf) by ddrake created at 2008-04-02 06:32:07



---

archive/issue_comments_019028.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-02T20:14:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2769#issuecomment-19028",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_019029.json:
```json
{
    "body": "This has been fixed by #3392.",
    "created_at": "2008-09-02T20:14:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2769#issuecomment-19029",
    "user": "mhansen"
}
```

This has been fixed by #3392.
