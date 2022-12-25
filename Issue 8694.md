# Issue 8694: Improve schemes printing and LaTeXing

archive/issues_008694.json:
```json
{
    "body": "Assignee: @aghitza\n\nI am attaching notebook printouts with old and new output in text and typeset mode.\n\n(In the \"before\" file typeset versions are for some reason on top of the last lines of text - this happens only after pressing \"Print\" button in the notebook, the usual editable version looks fine.)\n\nCurrent situation:\n* schemes don't have _latex_ methods, so typesetting just outputs the usual text representation;\n* this is not only not very good looking, but actually can be confusing since polynomials that were on different lines before are now separated just by a space, which may look like an omitted multiplication.\n\nThe patch provides _latex_ methods for pretty yet compact typesetting. In addition, while working on this I made the following changes to _repr_ methods:\n* put commas between polynomials: this may be important even in text mode if polynomials are long and some of them are printed on several lines;\n* replaced (no equations) by (no polynomials) for schemes that do not have defining polynomials: since the output does not include \"=0\", this seems to be more correct;\n* compactified printing of quasi-schemes: since both components are schemes in the same ambient space, there is no need to print it twice.\n\nApply on top of #8675 and #8682.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8694\n\n",
    "created_at": "2010-04-15T19:56:11Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Improve schemes printing and LaTeXing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8694",
    "user": "https://github.com/novoselt"
}
```
Assignee: @aghitza

I am attaching notebook printouts with old and new output in text and typeset mode.

(In the "before" file typeset versions are for some reason on top of the last lines of text - this happens only after pressing "Print" button in the notebook, the usual editable version looks fine.)

Current situation:
* schemes don't have _latex_ methods, so typesetting just outputs the usual text representation;
* this is not only not very good looking, but actually can be confusing since polynomials that were on different lines before are now separated just by a space, which may look like an omitted multiplication.

The patch provides _latex_ methods for pretty yet compact typesetting. In addition, while working on this I made the following changes to _repr_ methods:
* put commas between polynomials: this may be important even in text mode if polynomials are long and some of them are printed on several lines;
* replaced (no equations) by (no polynomials) for schemes that do not have defining polynomials: since the output does not include "=0", this seems to be more correct;
* compactified printing of quasi-schemes: since both components are schemes in the same ambient space, there is no need to print it twice.

Apply on top of #8675 and #8682.

Issue created by migration from https://trac.sagemath.org/ticket/8694





---

archive/issue_comments_079067.json:
```json
{
    "body": "Attachment [schemes_output_before.pdf](tarball://root/attachments/some-uuid/ticket8694/schemes_output_before.pdf) by @novoselt created at 2010-04-15 19:56:41",
    "created_at": "2010-04-15T19:56:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8694#issuecomment-79067",
    "user": "https://github.com/novoselt"
}
```

Attachment [schemes_output_before.pdf](tarball://root/attachments/some-uuid/ticket8694/schemes_output_before.pdf) by @novoselt created at 2010-04-15 19:56:41



---

archive/issue_comments_079068.json:
```json
{
    "body": "Attachment [schemes_output_after.pdf](tarball://root/attachments/some-uuid/ticket8694/schemes_output_after.pdf) by @novoselt created at 2010-04-15 19:56:51",
    "created_at": "2010-04-15T19:56:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8694#issuecomment-79068",
    "user": "https://github.com/novoselt"
}
```

Attachment [schemes_output_after.pdf](tarball://root/attachments/some-uuid/ticket8694/schemes_output_after.pdf) by @novoselt created at 2010-04-15 19:56:51



---

archive/issue_comments_079069.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-15T20:10:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8694#issuecomment-79069",
    "user": "https://github.com/novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079070.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-18T12:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8694#issuecomment-79070",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079071.json:
```json
{
    "body": "This is a very nice improvement!",
    "created_at": "2010-05-18T12:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8694#issuecomment-79071",
    "user": "https://github.com/aghitza"
}
```

This is a very nice improvement!



---

archive/issue_comments_079072.json:
```json
{
    "body": "In `AlgebraicScheme_quasi` plain-text and LaTeX descriptions do not match; I think it should be **sub**scheme in `_latex_()`, too.",
    "created_at": "2010-05-23T06:40:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8694#issuecomment-79072",
    "user": "https://github.com/nexttime"
}
```

In `AlgebraicScheme_quasi` plain-text and LaTeX descriptions do not match; I think it should be **sub**scheme in `_latex_()`, too.



---

archive/issue_comments_079073.json:
```json
{
    "body": "Good point. It looks like it used to be \"scheme\" in repr and I changed it to \"subscheme\" but didn't do it in latex. Will post a new version shortly.",
    "created_at": "2010-05-23T17:29:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8694#issuecomment-79073",
    "user": "https://github.com/novoselt"
}
```

Good point. It looks like it used to be "scheme" in repr and I changed it to "subscheme" but didn't do it in latex. Will post a new version shortly.



---

archive/issue_comments_079074.json:
```json
{
    "body": "Attachment [trac_8694_improve_schemes_printing_and_latexing.patch](tarball://root/attachments/some-uuid/ticket8694/trac_8694_improve_schemes_printing_and_latexing.patch) by @novoselt created at 2010-05-23 17:44:27",
    "created_at": "2010-05-23T17:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8694#issuecomment-79074",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_8694_improve_schemes_printing_and_latexing.patch](tarball://root/attachments/some-uuid/ticket8694/trac_8694_improve_schemes_printing_and_latexing.patch) by @novoselt created at 2010-05-23 17:44:27



---

archive/issue_comments_079075.json:
```json
{
    "body": "Made the proposed change and fixed the doctest of _latex_ for quasi-subschemes accordingly.",
    "created_at": "2010-05-23T17:45:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8694#issuecomment-79075",
    "user": "https://github.com/novoselt"
}
```

Made the proposed change and fixed the doctest of _latex_ for quasi-subschemes accordingly.



---

archive/issue_comments_079076.json:
```json
{
    "body": "Replying to [comment:5 novoselt]:\n> Made the proposed change and fixed the doctest of _latex_ for quasi-subschemes accordingly.\n\nYou're too fast. ;-) (I wanted to remind you changing the doctests, too.)\n\nUpdated patch looks fine. (But haven't yet applied/tested it.)",
    "created_at": "2010-05-23T18:20:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8694#issuecomment-79076",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:5 novoselt]:
> Made the proposed change and fixed the doctest of _latex_ for quasi-subschemes accordingly.

You're too fast. ;-) (I wanted to remind you changing the doctests, too.)

Updated patch looks fine. (But haven't yet applied/tested it.)



---

archive/issue_comments_079077.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T07:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8694#issuecomment-79077",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
