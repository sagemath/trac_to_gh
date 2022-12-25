# Issue 6673: Set up jsMath extensions, macros, etc., for the documentation

archive/issues_006673.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @haraldschilly\n\nCurrently, the documentation uses a stock jsMath loader script.  This excludes Sage-specific customizations, e.g., the notebook's default jsMath macros.  The patch\n\n* [attachment:trac_6673-jsmath_macros_docs_v3.patch]\n\ninserts the settings via a template when the docs are built.  The patch also sets up a 'sage' HTML theme (cf. [Sphinx docs](http://sphinx.pocoo.org/theming.html#creating-themes)) for later customization.\n\nSee #4714 for a \"notebook\" version.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6673\n\n",
    "closed_at": "2009-10-31T15:29:48Z",
    "created_at": "2009-08-04T06:59:38Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "Set up jsMath extensions, macros, etc., for the documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6673",
    "user": "https://github.com/qed777"
}
```
Assignee: tba

CC:  @haraldschilly

Currently, the documentation uses a stock jsMath loader script.  This excludes Sage-specific customizations, e.g., the notebook's default jsMath macros.  The patch

* [attachment:trac_6673-jsmath_macros_docs_v3.patch]

inserts the settings via a template when the docs are built.  The patch also sets up a 'sage' HTML theme (cf. [Sphinx docs](http://sphinx.pocoo.org/theming.html#creating-themes)) for later customization.

See #4714 for a "notebook" version.

Issue created by migration from https://trac.sagemath.org/ticket/6673





---

archive/issue_comments_054726.json:
```json
{
    "body": "Depends on #6614.",
    "created_at": "2009-08-04T07:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6673#issuecomment-54726",
    "user": "https://github.com/qed777"
}
```

Depends on #6614.



---

archive/issue_comments_054727.json:
```json
{
    "body": "Attachment [trac_6673-jsmath_macros_docs.patch](tarball://root/attachments/some-uuid/ticket6673/trac_6673-jsmath_macros_docs.patch) by @qed777 created at 2009-08-04 07:07:27\n\nNote: Depending on the outcome of this ticket, we may need to update the \"scripts\" patch at #6187.",
    "created_at": "2009-08-04T07:07:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6673#issuecomment-54727",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6673-jsmath_macros_docs.patch](tarball://root/attachments/some-uuid/ticket6673/trac_6673-jsmath_macros_docs.patch) by @qed777 created at 2009-08-04 07:07:27

Note: Depending on the outcome of this ticket, we may need to update the "scripts" patch at #6187.



---

archive/issue_comments_054728.json:
```json
{
    "body": "With the patch, commands like `\\ZZ` in the docs appear correctly in the off-line (html+jsmath) version of the reference manual, the tutorial, etc.\n\nIs there any way to generate the list of macros automatically, the way it is done in `doc/common/conf.py` for the LaTeX version:\n\n```\nfor macro in sage_latex_macros:\n    # used when building latex and pdf versions\n    latex_preamble += macro + '\\n'\n    # used when building html version\n    pngmath_latex_preamble += macro + '\\n'\n```\nI don't see anything helpful in the Sphinx documentation, unfortunately.  So instead, I'm attaching a small patch to the file `sage/misc/latex_macros.py`, suggesting that if the list of macros there gets changed, the list in `jsmath_sage.js` must be changed also, and I've put a pointer to `latex_macros.py` in `jsmath_sage.js`.\n\nFor the file jsmath_sage.js, it looks like a modified version of easy/load.js, but it's not the same as the one distributed with Sage (the one in local/notebook/javascript/jsmath/easy); there are white space differences, and there are differences below the line saying \"DO NOT MAKE CHANGES BELOW THIS\".  Do I need to worry about this?  Let me know, and if it's not a problem, I can give this a positive review.",
    "created_at": "2009-08-20T21:47:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6673#issuecomment-54728",
    "user": "https://github.com/jhpalmieri"
}
```

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

archive/issue_events_015745.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2009-08-20T21:47:44Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6673#event-15745"
}
```



---

archive/issue_comments_054729.json:
```json
{
    "body": "Attachment [trac_6673-referee.patch](tarball://root/attachments/some-uuid/ticket6673/trac_6673-referee.patch) by @jhpalmieri created at 2009-08-20 21:48:13\n\napply on top of the other patch",
    "created_at": "2009-08-20T21:48:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6673#issuecomment-54729",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_6673-referee.patch](tarball://root/attachments/some-uuid/ticket6673/trac_6673-referee.patch) by @jhpalmieri created at 2009-08-20 21:48:13

apply on top of the other patch



---

archive/issue_comments_054730.json:
```json
{
    "body": "Rather inconveniently, I described the patch, briefly, in a [comment:ticket:4714:8 comment] at #4714.  I apologize for not adding some information here.\n\nWith Sphinx 0.6.2 (cf. #6586), we might use [static templates](http://sphinx.pocoo.org/theming.html#static-templates) to insert the macros on-the-fly.  A test:\n\n* Move `jsmath_sage.js` to `jsmath_sage.js_t`\n* Temporarily sandwich the `macros: { }` block between `{% raw %}` and `{% endraw %}` to placate Jinja.\n* Add the comment `// {{ foo }}` somewhere.\n* Run `sage -docbuild testreference html -jv3 -S -Afoo=bar`.\n\nI find `// bar` in place of the \"`foo`\" statement in `_static/jsmath_sage.js`.  In the next few days, I'll try to create a new ticket with a proper patch.\n\nSince we're not there yet, I give the \"referee\" patch a positive review.",
    "created_at": "2009-08-22T14:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6673#issuecomment-54730",
    "user": "https://github.com/qed777"
}
```

Rather inconveniently, I described the patch, briefly, in a [comment:ticket:4714:8 comment] at #4714.  I apologize for not adding some information here.

With Sphinx 0.6.2 (cf. #6586), we might use [static templates](http://sphinx.pocoo.org/theming.html#static-templates) to insert the macros on-the-fly.  A test:

* Move `jsmath_sage.js` to `jsmath_sage.js_t`
* Temporarily sandwich the `macros: { }` block between `{% raw %}` and `{% endraw %}` to placate Jinja.
* Add the comment `// {{ foo }}` somewhere.
* Run `sage -docbuild testreference html -jv3 -S -Afoo=bar`.

I find `// bar` in place of the "`foo`" statement in `_static/jsmath_sage.js`.  In the next few days, I'll try to create a new ticket with a proper patch.

Since we're not there yet, I give the "referee" patch a positive review.



---

archive/issue_comments_054731.json:
```json
{
    "body": "I just noticed that jsMath complains about `\\mathfrak` and `\\mod` in\n\n* `doc/static/bordeaux_2008/integer_factorization.html`\n* `doc/static/bordeaux_2008/modular_forms_and_hecke_operators.html`\n* `doc/output/html/en/bordeaux_2008/modabvar.html`",
    "created_at": "2009-08-22T14:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6673#issuecomment-54731",
    "user": "https://github.com/qed777"
}
```

I just noticed that jsMath complains about `\mathfrak` and `\mod` in

* `doc/static/bordeaux_2008/integer_factorization.html`
* `doc/static/bordeaux_2008/modular_forms_and_hecke_operators.html`
* `doc/output/html/en/bordeaux_2008/modabvar.html`



---

archive/issue_comments_054732.json:
```json
{
    "body": "So the plan is to have this depend on #6586?  (That's fine with me, I just want to make sure I understand.)",
    "created_at": "2009-08-22T22:09:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6673#issuecomment-54732",
    "user": "https://github.com/jhpalmieri"
}
```

So the plan is to have this depend on #6586?  (That's fine with me, I just want to make sure I understand.)



---

archive/issue_comments_054733.json:
```json
{
    "body": "The forthcoming alternative patch inserts macros on-the-fly.  It\n* Moves `jsmath_sage.js` to `jsmath_sage.js_t` and replaces the list of jsMath macros with a Jinja macro.\n* Adds `convert_to_latex_js_math_easy()` to and generates the string `sage_jsmath_macros_jinja` in `latex_macros.py`.\n* Includes the string in a command-line option to Sphinx, in `builder.py` [1].\n* Adds a trailing semcolon (\"`;`\") in `latex_macros.convert_latex_macro_to_jsmath()`.\n\n[1] It seems that we can override the templates' default `html_context` dictionary only on the command-line, i.e., with the `-A` option (cf. `sphinx/config.py`).  This means that adding `html_context = <the macros>` in `conf.py` won't work.",
    "created_at": "2009-08-23T06:10:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6673#issuecomment-54733",
    "user": "https://github.com/qed777"
}
```

The forthcoming alternative patch inserts macros on-the-fly.  It
* Moves `jsmath_sage.js` to `jsmath_sage.js_t` and replaces the list of jsMath macros with a Jinja macro.
* Adds `convert_to_latex_js_math_easy()` to and generates the string `sage_jsmath_macros_jinja` in `latex_macros.py`.
* Includes the string in a command-line option to Sphinx, in `builder.py` [1].
* Adds a trailing semcolon ("`;`") in `latex_macros.convert_latex_macro_to_jsmath()`.

[1] It seems that we can override the templates' default `html_context` dictionary only on the command-line, i.e., with the `-A` option (cf. `sphinx/config.py`).  This means that adding `html_context = <the macros>` in `conf.py` won't work.



---

archive/issue_comments_054734.json:
```json
{
    "body": "Attachment [trac_6673-jsmath_macros_docs_v2.patch](tarball://root/attachments/some-uuid/ticket6673/trac_6673-jsmath_macros_docs_v2.patch) by @qed777 created at 2009-08-23 06:26:08\n\nTemplate version. Depends on #6187, #6586. Apply only this patch.",
    "created_at": "2009-08-23T06:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6673#issuecomment-54734",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6673-jsmath_macros_docs_v2.patch](tarball://root/attachments/some-uuid/ticket6673/trac_6673-jsmath_macros_docs_v2.patch) by @qed777 created at 2009-08-23 06:26:08

Template version. Depends on #6187, #6586. Apply only this patch.



---

archive/issue_comments_054735.json:
```json
{
    "body": "I haven't added/fixed `\\mathfrak`, `\\mod`, or whatever is happening near the top of\n\n* `doc/static/reference/sage/modular/arithgroup/congroup_gammaH.html`",
    "created_at": "2009-08-23T06:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6673#issuecomment-54735",
    "user": "https://github.com/qed777"
}
```

I haven't added/fixed `\mathfrak`, `\mod`, or whatever is happening near the top of

* `doc/static/reference/sage/modular/arithgroup/congroup_gammaH.html`



---

archive/issue_comments_054736.json:
```json
{
    "body": "Re congroup_gammaH.html, if it's the \"\\trianglelefteq\", then I think it can safely be replaced with \"\\leq\".  (It's a subgroup of an abelian group, so it's automatically normal.)",
    "created_at": "2009-08-23T17:32:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6673#issuecomment-54736",
    "user": "https://github.com/jhpalmieri"
}
```

Re congroup_gammaH.html, if it's the "\trianglelefteq", then I think it can safely be replaced with "\leq".  (It's a subgroup of an abelian group, so it's automatically normal.)



---

archive/issue_comments_054737.json:
```json
{
    "body": "(Although \\trianglelefteq should be [available through the amssymbols package](http://www.math.union.edu/~dpvc/jsMath/symbols/AMSsymbols.html).  Hmm.)",
    "created_at": "2009-08-23T17:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6673#issuecomment-54737",
    "user": "https://github.com/jhpalmieri"
}
```

(Although \trianglelefteq should be [available through the amssymbols package](http://www.math.union.edu/~dpvc/jsMath/symbols/AMSsymbols.html).  Hmm.)



---

archive/issue_comments_054738.json:
```json
{
    "body": "Should we add new macros in a separate ticket?\n\nIf so, I can try to set up #4714 to use the same `sage_jsmath_macros_jinja` as this ticket.  But we can just call them `sage_jsmath_macros`, since we'll usually use just the template version.  Of course, we can keep `convert_latex_macro_to_jsmath` for on-the-fly definitions.",
    "created_at": "2009-10-16T07:11:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6673#issuecomment-54738",
    "user": "https://github.com/qed777"
}
```

Should we add new macros in a separate ticket?

If so, I can try to set up #4714 to use the same `sage_jsmath_macros_jinja` as this ticket.  But we can just call them `sage_jsmath_macros`, since we'll usually use just the template version.  Of course, we can keep `convert_latex_macro_to_jsmath` for on-the-fly definitions.



---

archive/issue_comments_054739.json:
```json
{
    "body": "Also:  How should we set up tex2math in `jsmath_sage.js_t`?  Should we use the same settings for the notebook and docs?",
    "created_at": "2009-10-16T07:37:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6673#issuecomment-54739",
    "user": "https://github.com/qed777"
}
```

Also:  How should we set up tex2math in `jsmath_sage.js_t`?  Should we use the same settings for the notebook and docs?



---

archive/issue_comments_054740.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-21T12:12:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6673#issuecomment-54740",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_054741.json:
```json
{
    "body": "Attachment [trac_6673-jsmath_macros_docs_v3.patch](tarball://root/attachments/some-uuid/ticket6673/trac_6673-jsmath_macros_docs_v3.patch) by @qed777 created at 2009-10-21 18:44:34\n\nUpdated template version.  Added 'sage' theme.  Apply only this patch.",
    "created_at": "2009-10-21T18:44:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6673#issuecomment-54741",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6673-jsmath_macros_docs_v3.patch](tarball://root/attachments/some-uuid/ticket6673/trac_6673-jsmath_macros_docs_v3.patch) by @qed777 created at 2009-10-21 18:44:34

Updated template version.  Added 'sage' theme.  Apply only this patch.



---

archive/issue_comments_054742.json:
```json
{
    "body": "Version 3:\n\n* Organizes a 'sage' theme for easier customization.  See `SAGE_DOC/themes/sage/theme.conf` for the settings.\n* Uses the theme to avoid passing jsMath macros on the command-line.\n* Disables tex2math.\n* Subsumes #7204.  In particular, this depends on [SageNB](http://nb.sagemath.org/) version 0.3.2 or later.\n* Makes the Sage logo a link to the top-level doc page.  For the doc page itself, the link is to [SageMath](http://www.sagemath.org/).\n* Adds `SAGE_DOC/themes` to `MANIFEST.in`.\n* Leaves alone the now empty `SAGE_DOC/templates` and `SAGE_DOC/static`.\n\nRemarks:\n\n* We should add a friendly welcome message to the top-level doc page, e.g., near the top or in the sidebar.",
    "created_at": "2009-10-21T19:05:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6673#issuecomment-54742",
    "user": "https://github.com/qed777"
}
```

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

archive/issue_comments_054743.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-21T19:05:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6673#issuecomment-54743",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_054744.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-27T04:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6673#issuecomment-54744",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_054745.json:
```json
{
    "body": "The code looks good.  I've played around with it for a while, and it seems to do what it's supposed to.\n\nNow schilly can get to work modifying \"theme.conf\" to produce a custom Sage theme...",
    "created_at": "2009-10-27T04:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6673#issuecomment-54745",
    "user": "https://github.com/jhpalmieri"
}
```

The code looks good.  I've played around with it for a while, and it seems to do what it's supposed to.

Now schilly can get to work modifying "theme.conf" to produce a custom Sage theme...



---

archive/issue_comments_054746.json:
```json
{
    "body": "To the release manager: when merging this, please close #7204 also, since this resolves the problem reported there.",
    "created_at": "2009-10-29T21:38:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6673#issuecomment-54746",
    "user": "https://github.com/jhpalmieri"
}
```

To the release manager: when merging this, please close #7204 also, since this resolves the problem reported there.



---

archive/issue_events_015746.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-31T15:29:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6673#event-15746"
}
```



---

archive/issue_comments_054747.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-31T15:29:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6673#issuecomment-54747",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
