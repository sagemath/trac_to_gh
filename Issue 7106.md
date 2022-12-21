# Issue 7106: [with patch, needs review] Add keyboard shortcut ctrl-0 to reference manual

Issue created by migration from Trac.

Original creator: hgranath

Original creation time: 2009-10-04 05:45:59

Assignee: tba

Keywords: keyboard shortcuts

The new parenthesis matching keyboard shortcut ctrl-0 introduced in
#3646 was not documented in the doc string of config.py. Once all
information is in the doc string, I would suggest to shorten the help
page text a little.


---

Attachment

Depends on #7104


---

Comment by hgranath created at 2009-10-04 06:02:28

Changing type from defect to enhancement.


---

Comment by hgranath created at 2009-10-04 06:02:28

Changing priority from major to minor.


---

Comment by awebb created at 2009-10-07 19:17:35

Changing status from needs_review to positive_review.


---

Comment by awebb created at 2009-10-07 19:17:35

Works with sage -docbuild reference html. ~! Adam


---

Comment by was created at 2009-10-19 06:27:32

This needs to be rebased against the new sagenb project. http://nb.sagemath.org/


---

Comment by was created at 2009-10-19 06:27:32

Changing component from documentation to notebook.


---

Attachment

Rebased for sagenb 0.4.  Apply only this patch to the sagenb repository.


---

Comment by mpatel created at 2009-11-01 12:22:16

The [attachment:trac_7106-paren_match_doc.patch new patch] applies to sagenb 0.4 (or so).


---

Attachment

Fix Sphinx warning, better spacing. Apply only this patch to the sagenb repository.


---

Comment by mpatel created at 2009-11-01 13:31:16

Version 2:

 * Fixes a Sphinx warning.
 * Inserts space between the list items.


---

Comment by awebb created at 2009-11-03 18:55:18

The files look good to me. Silly question: where do these parts show up in the docbuild or in the help?

Cheers,
Adam


---

Comment by mpatel created at 2009-11-04 04:08:42

I apologize, if I'm misinterpreting your question.  The changes to

 * `config.py` should appear on ["this" page](http://www.sagemath.org/doc/reference/notebook.html).
 * `tutorial.py` should appear on the main notebook help page, e.g., http://www.sagenb.org/help/ .

To rebuild the docs after applying a patch to the `sage` repository (i.e., the main Sage library), try, e.g.,

 * `sage -b`
 * `sage -docbuild reference html -j`
 * Browse to `$SAGE_ROOT/devel/sage/doc/output/html/en/reference/index.html`

Please see `sage -docbuild -H` for more options.  If/after #7367 merges, the post-patch procedure for the `sagenb` repository could be

 * `cd sagenb-0.4/`
 * `sage -python setup.py install`
 * `sage -docbuild reference html -j`

Should we move `tutorial.notebook_help` to a HTML page or template?


---

Comment by awebb created at 2009-11-04 14:44:01

Thanks! That more or less answers my question. I had run the docbuild but was having difficulty finding where the exact changes were. I am still looking but I have a better idea where to look. ~ Adam


---

Comment by was created at 2009-11-11 19:53:33

I'm merging this.  Note that it says "only python comments" and I think Python should be capitalized.  I made this one trivial change in the official sagenb repo.


---

Comment by was created at 2009-11-11 19:55:50

merged into sagenb-0.4.2 (sage-4.2.1)


---

Comment by was created at 2009-11-11 19:55:50

Resolution: fixed
