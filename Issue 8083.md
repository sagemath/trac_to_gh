# Issue 8083: fix accents in LaTeX output

archive/issues_008083.json:
```json
{
    "body": "Assignee: was\n\nKeywords: latex\n\nAccented letters produced in notebook by command like this\n\n```\n%latex\n\u011b\u0161\u010d\u0159\u017e\u00fd\u00e1\u00ed\u00e9\u010f\u010e\n```\n\nproduce letters composed from two objects - letter and accent - and this does not look good in some cases, especially the letter \u010f. The solution is to use correct fonts in LaTeX.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8083\n\n",
    "created_at": "2010-01-26T20:53:14Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "fix accents in LaTeX output",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8083",
    "user": "robert.marik"
}
```
Assignee: was

Keywords: latex

Accented letters produced in notebook by command like this

```
%latex
ěščřžýáíéďĎ
```

produce letters composed from two objects - letter and accent - and this does not look good in some cases, especially the letter ď. The solution is to use correct fonts in LaTeX.

Issue created by migration from https://trac.sagemath.org/ticket/8083





---

archive/issue_comments_070834.json:
```json
{
    "body": "Attachment [latex_T1_fonts.patch](tarball://root/attachments/some-uuid/ticket8083/latex_T1_fonts.patch) by robert.marik created at 2010-01-26 20:53:34",
    "created_at": "2010-01-26T20:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8083#issuecomment-70834",
    "user": "robert.marik"
}
```

Attachment [latex_T1_fonts.patch](tarball://root/attachments/some-uuid/ticket8083/latex_T1_fonts.patch) by robert.marik created at 2010-01-26 20:53:34



---

archive/issue_comments_070835.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-26T20:57:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8083#issuecomment-70835",
    "user": "robert.marik"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070836.json:
```json
{
    "body": "Works as advertised in the notebook.  Note that executing\n\n```\nsage: view(s = u\"\u011b\u0161\u010d\u0159\u017e\u00fd\u00e1\u00ed\u00e9\u010f\u010e\")\n```\n\nfrom the command line doesn't work at all, and I can't figure out how to fix it.  I can get it not to throw an error -- see the experimental patch.  I think that the command to write the LaTeX file (in the definition of the `view` function) should be something like\n\n```\ncodecs.open(tex_file, mode='w', encoding='utf_8').write(s)\n```\n\nbut this garbles the string s.  Anyway, this belongs on another ticket.",
    "created_at": "2010-01-28T22:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8083#issuecomment-70836",
    "user": "jhpalmieri"
}
```

Works as advertised in the notebook.  Note that executing

```
sage: view(s = u"ěščřžýáíéďĎ")
```

from the command line doesn't work at all, and I can't figure out how to fix it.  I can get it not to throw an error -- see the experimental patch.  I think that the command to write the LaTeX file (in the definition of the `view` function) should be something like

```
codecs.open(tex_file, mode='w', encoding='utf_8').write(s)
```

but this garbles the string s.  Anyway, this belongs on another ticket.



---

archive/issue_comments_070837.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-28T22:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8083#issuecomment-70837",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070838.json:
```json
{
    "body": "do not merge: for illustration and testing only",
    "created_at": "2010-01-28T22:11:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8083#issuecomment-70838",
    "user": "jhpalmieri"
}
```

do not merge: for illustration and testing only



---

archive/issue_comments_070839.json:
```json
{
    "body": "Attachment [trac_8083-experimental.patch](tarball://root/attachments/some-uuid/ticket8083/trac_8083-experimental.patch) by mpatel created at 2010-01-30 11:36:34\n\nOut of curiosity: Do other font encodings ever conflict with `T1`?  Other alphabets may require a different one, e.g., for\n\n\n```\n%latex\n\u0422\u0435\u043e\u0440\u0438\u044f \u0447\u0438\u0441\u0435\u043b\n```\n\none can use\n\n\n```python\nsage.misc.latex.latex.extra_preamble('\\\\usepackage[T2A]{fontenc}')\n```\n",
    "created_at": "2010-01-30T11:36:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8083#issuecomment-70839",
    "user": "mpatel"
}
```

Attachment [trac_8083-experimental.patch](tarball://root/attachments/some-uuid/ticket8083/trac_8083-experimental.patch) by mpatel created at 2010-01-30 11:36:34

Out of curiosity: Do other font encodings ever conflict with `T1`?  Other alphabets may require a different one, e.g., for


```
%latex
Теория чисел
```

one can use


```python
sage.misc.latex.latex.extra_preamble('\\usepackage[T2A]{fontenc}')
```




---

archive/issue_comments_070840.json:
```json
{
    "body": "Merged [latex_T1_fonts.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8083/latex_T1_fonts.patch).",
    "created_at": "2010-01-30T23:50:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8083#issuecomment-70840",
    "user": "mvngu"
}
```

Merged [latex_T1_fonts.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8083/latex_T1_fonts.patch).



---

archive/issue_comments_070841.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-30T23:50:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8083#issuecomment-70841",
    "user": "mvngu"
}
```

Resolution: fixed
