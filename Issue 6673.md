# Issue 6673: [with patch, needs review] Set up jsMath extensions, macros, etc., for the documentation

Issue created by migration from https://trac.sagemath.org/ticket/6673

Original creator: mpatel

Original creation time: 2009-08-04 06:59:38

Assignee: tba

CC:  schilly

Currently, the documentation uses a "vanilla" `easy/load.js` script to load jsMath.  This excludes Sage-specific customizations, including a number of LaTeX macros.  After this ticket is merged, we should be able to build all Sage documentation with `--jsmath` and have no "ugly-scary" warnings when browsing the offline documentation.

See #4714 for background.  That ticket is the "notebook" analogue of this one.


---

Comment by mpatel created at 2009-08-04 07:03:47

Depends on #6614.


---

Attachment

Note: Depending on the outcome of this ticket, we may need to update the "scripts" patch at #6187.


---

Comment by jhpalmieri created at 2009-08-20 21:47:44

With the patch, commands like `\ZZ` in the docs appear correctly in the off-line (html+jsmath) version of the reference manual, the tutorial, etc.

Is there any way to generate the list of macros automatically, the way it is done in `doc/common/conf.py` for the LaTeX version:

```
for macro in sage_latex_macros:
    # used when building latex and pdf versions
    latex_preamble += macro + '\n'
    # used when building html version
    pngmath_latex_preamble += macro + '\n'
```

I don't see anything helpful in the Sphinx documentation, unfortunately.  So instead, I'm attaching a small patch to the file `sage/misc/latex_macros.py`, suggesting that if the list of macros there gets changed, the list in `jsmath_sage.js` must be changed also, and I've put a pointer to `latex_macros.py` in `jsmath_sage.js`.

For the file jsmath_sage.js, it looks like a modified version of easy/load.js, but it's not the same as the one distributed with Sage (the one in local/notebook/javascript/jsmath/easy); there are white space differences, and there are differences below the line saying "DO NOT MAKE CHANGES BELOW THIS".  Do I need to worry about this?  Let me know, and if it's not a problem, I can give this a positive review.


---

Attachment

apply on top of the other patch


---

Comment by mpatel created at 2009-08-22 14:05:52

Rather inconveniently, I described the patch, briefly, in a [comment:ticket:4714:8 comment] at #4714.  I apologize for not adding some information here.

With Sphinx 0.6.2 (cf. #6586), we might use [static templates](http://sphinx.pocoo.org/theming.html#static-templates) to insert the macros on-the-fly.  A test:

 * Move `jsmath_sage.js` to `jsmath_sage.js_t`
 * Temporarily sandwich the `macros: { }` block between `{% raw %}` and `{% endraw %}` to placate Jinja.
 * Add the comment `// {{ foo }}` somewhere.
 * Run `sage -docbuild testreference html -jv3 -S -Afoo=bar`.

I find `// bar` in place of the "`foo`" statement in `_static/jsmath_sage.js`.  In the next few days, I'll try to create a new ticket with a proper patch.

Since we're not there yet, I give the "referee" patch a positive review.


---

Comment by mpatel created at 2009-08-22 14:18:48

I just noticed that jsMath complains about `\mathfrak` and `\mod` in

 * `doc/static/bordeaux_2008/integer_factorization.html`
 * `doc/static/bordeaux_2008/modular_forms_and_hecke_operators.html`
 * `doc/output/html/en/bordeaux_2008/modabvar.html`


---

Comment by jhpalmieri created at 2009-08-22 22:09:15

So the plan is to have this depend on #6586?  (That's fine with me, I just want to make sure I understand.)


---

Comment by mpatel created at 2009-08-23 06:10:32

The forthcoming alternative patch inserts macros on-the-fly.  It
 * Moves `jsmath_sage.js` to `jsmath_sage.js_t` and replaces the list of jsMath macros with a Jinja macro.
 * Adds `convert_to_latex_js_math_easy()` to and generates the string `sage_jsmath_macros_jinja` in `latex_macros.py`.
 * Includes the string in a command-line option to Sphinx, in `builder.py` [1].
 * Adds a trailing semcolon ("`;`") in `latex_macros.convert_latex_macro_to_jsmath()`.

[1] It seems that we can override the templates' default `html_context` dictionary only on the command-line, i.e., with the `-A` option (cf. `sphinx/config.py`).  This means that adding `html_context = <the macros>` in `conf.py` won't work.


---

Attachment

Template version. Depends on #6187, #6586. Apply only this patch.


---

Comment by mpatel created at 2009-08-23 06:29:41

I haven't added/fixed `\mathfrak`, `\mod`, or whatever is happening near the top of

 * `doc/static/reference/sage/modular/arithgroup/congroup_gammaH.html`


---

Comment by jhpalmieri created at 2009-08-23 17:32:19

Re congroup_gammaH.html, if it's the "\trianglelefteq", then I think it can safely be replaced with "\leq".  (It's a subgroup of an abelian group, so it's automatically normal.)


---

Comment by jhpalmieri created at 2009-08-23 17:43:07

(Although \trianglelefteq should be [available through the amssymbols package](http://www.math.union.edu/~dpvc/jsMath/symbols/AMSsymbols.html).  Hmm.)


---

Comment by mpatel created at 2009-10-16 07:11:42

Should we add new macros in a separate ticket?

If so, I can try to set up #4714 to use the same `sage_jsmath_macros_jinja` as this ticket.  But we can just call them `sage_jsmath_macros`, since we'll usually use just the template version.  Of course, we can keep `convert_latex_macro_to_jsmath` for on-the-fly definitions.


---

Comment by mpatel created at 2009-10-16 07:37:13

Also:  How should we set up tex2math in `jsmath_sage.js_t`?  Should we use the same settings for the notebook and docs?


---

Comment by mpatel created at 2009-10-21 12:12:29

Changing status from needs_review to needs_work.


---

Attachment

Updated template version.  Added 'sage' theme.  Apply only this patch.


---

Comment by mpatel created at 2009-10-21 19:05:42

Version 3:

 * Organizes a 'sage' theme for easier customization.  See `SAGE_DOC/themes/sage/theme.conf` for the settings.
 * Uses the theme to avoid passing jsMath macros on the command-line.
 * Disables tex2math.
 * Subsumes #7204.  In particular, this depends on [SageNB](http://nb.sagemath.org/) version 0.3.2 or later.
 * Makes the Sage logo a link to the top-level doc page.  For the doc page itself, the link is to [SageMath](http://www.sagemath.org/).
 * Adds `SAGE_DOC/themes` to `MANIFEST.in`.
 * Leaves alone the now empty `SAGE_DOC/templates` and `SAGE_DOC/static`.

Remarks:

 * We should add a friendly welcome message to the top-level doc page, e.g., near the top or in the sidebar.


---

Comment by mpatel created at 2009-10-21 19:05:42

Changing priority from minor to major.


---

Comment by mpatel created at 2009-10-21 19:05:42

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2009-10-27 04:55:09

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2009-10-27 04:55:09

The code looks good.  I've played around with it for a while, and it seems to do what it's supposed to.

Now schilly can get to work modifying "theme.conf" to produce a custom Sage theme...


---

Comment by jhpalmieri created at 2009-10-29 21:38:40

To the release manager: when merging this, please close #7204 also, since this resolves the problem reported there.


---

Comment by mhansen created at 2009-10-31 15:29:48

Resolution: fixed
