# Issue 8694: Improve schemes printing and LaTeXing

archive/issues_008694.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nI am attaching notebook printouts with old and new output in text and typeset mode.\n\n(In the \"before\" file typeset versions are for some reason on top of the last lines of text - this happens only after pressing \"Print\" button in the notebook, the usual editable version looks fine.)\n\nCurrent situation:\n* schemes don't have _latex_ methods, so typesetting just outputs the usual text representation;\n* this is not only not very good looking, but actually can be confusing since polynomials that were on different lines before are now separated just by a space, which may look like an omitted multiplication.\n\nThe patch provides _latex_ methods for pretty yet compact typesetting. In addition, while working on this I made the following changes to _repr_ methods:\n* put commas between polynomials: this may be important even in text mode if polynomials are long and some of them are printed on several lines;\n* replaced (no equations) by (no polynomials) for schemes that do not have defining polynomials: since the output does not include \"=0\", this seems to be more correct;\n* compactified printing of quasi-schemes: since both components are schemes in the same ambient space, there is no need to print it twice.\n\nApply on top of #8675 and #8682.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8694\n\n",
    "created_at": "2010-04-15T19:56:11Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "Improve schemes printing and LaTeXing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8694",
    "user": "novoselt"
}
```
Assignee: AlexGhitza

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

archive/issue_comments_079197.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-04-15T19:56:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8694#issuecomment-79197",
    "user": "novoselt"
}
```

Attachment



---

archive/issue_comments_079198.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-04-15T19:56:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8694#issuecomment-79198",
    "user": "novoselt"
}
```

Attachment



---

archive/issue_comments_079199.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-15T20:10:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8694#issuecomment-79199",
    "user": "novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079200.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-18T12:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8694#issuecomment-79200",
    "user": "AlexGhitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079201.json:
```json
{
    "body": "This is a very nice improvement!",
    "created_at": "2010-05-18T12:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8694#issuecomment-79201",
    "user": "AlexGhitza"
}
```

This is a very nice improvement!



---

archive/issue_comments_079202.json:
```json
{
    "body": "In `AlgebraicScheme_quasi` plain-text and LaTeX descriptions do not match; I think it should be **sub**scheme in `_latex_()`, too.",
    "created_at": "2010-05-23T06:40:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8694#issuecomment-79202",
    "user": "leif"
}
```

In `AlgebraicScheme_quasi` plain-text and LaTeX descriptions do not match; I think it should be **sub**scheme in `_latex_()`, too.



---

archive/issue_comments_079203.json:
```json
{
    "body": "Good point. It looks like it used to be \"scheme\" in repr and I changed it to \"subscheme\" but didn't do it in latex. Will post a new version shortly.",
    "created_at": "2010-05-23T17:29:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8694#issuecomment-79203",
    "user": "novoselt"
}
```

Good point. It looks like it used to be "scheme" in repr and I changed it to "subscheme" but didn't do it in latex. Will post a new version shortly.



---

archive/issue_comments_079204.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-05-23T17:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8694#issuecomment-79204",
    "user": "novoselt"
}
```

Attachment



---

archive/issue_comments_079205.json:
```json
{
    "body": "Made the proposed change and fixed the doctest of _latex_ for quasi-subschemes accordingly.",
    "created_at": "2010-05-23T17:45:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8694#issuecomment-79205",
    "user": "novoselt"
}
```

Made the proposed change and fixed the doctest of _latex_ for quasi-subschemes accordingly.



---

archive/issue_comments_079206.json:
```json
{
    "body": "Replying to [comment:5 novoselt]:\n> Made the proposed change and fixed the doctest of _latex_ for quasi-subschemes accordingly.\n\nYou're too fast. ;-) (I wanted to remind you changing the doctests, too.)\n\nUpdated patch looks fine. (But haven't yet applied/tested it.)",
    "created_at": "2010-05-23T18:20:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8694#issuecomment-79206",
    "user": "leif"
}
```

Replying to [comment:5 novoselt]:
> Made the proposed change and fixed the doctest of _latex_ for quasi-subschemes accordingly.

You're too fast. ;-) (I wanted to remind you changing the doctests, too.)

Updated patch looks fine. (But haven't yet applied/tested it.)



---

archive/issue_comments_079207.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T07:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8694#issuecomment-79207",
    "user": "mhansen"
}
```

Resolution: fixed
