# Issue 8694: Improve schemes printing and LaTeXing

Issue created by migration from https://trac.sagemath.org/ticket/8694

Original creator: novoselt

Original creation time: 2010-04-15 19:56:11

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


---

Attachment


---

Attachment


---

Comment by novoselt created at 2010-04-15 20:10:28

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2010-05-18 12:55:25

Changing status from needs_review to positive_review.


---

Comment by AlexGhitza created at 2010-05-18 12:55:25

This is a very nice improvement!


---

Comment by leif created at 2010-05-23 06:40:57

In `AlgebraicScheme_quasi` plain-text and LaTeX descriptions do not match; I think it should be *sub*scheme in `_latex_()`, too.


---

Comment by novoselt created at 2010-05-23 17:29:26

Good point. It looks like it used to be "scheme" in repr and I changed it to "subscheme" but didn't do it in latex. Will post a new version shortly.


---

Attachment


---

Comment by novoselt created at 2010-05-23 17:45:42

Made the proposed change and fixed the doctest of _latex_ for quasi-subschemes accordingly.


---

Comment by leif created at 2010-05-23 18:20:38

Replying to [comment:5 novoselt]:
> Made the proposed change and fixed the doctest of _latex_ for quasi-subschemes accordingly.

You're too fast. ;-) (I wanted to remind you changing the doctests, too.)

Updated patch looks fine. (But haven't yet applied/tested it.)


---

Comment by mhansen created at 2010-06-06 07:55:28

Resolution: fixed
