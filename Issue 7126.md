# Issue 7126: Doc sidebar broken by Sphinx 0.6.3 JS compression

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2009-10-05 19:02:35

Assignee: tba

The doc sidebar provided by #6507 is broken by the JS compression applied by Sphinx 0.6.3 (#6586). This patch changes line comments to block comments, and adds some missing semicolons.


---

Attachment

Changes line comments to block comments. Adds missing semicolons.


---

Comment by timdumol created at 2009-10-05 19:05:17

Changing priority from major to minor.


---

Comment by mpatel created at 2009-10-06 00:22:56

Thanks very much for finding these problems.  I ran the JS code in `layout.html` through [JSLint](http://www.jslint.com/) on the "The Good Parts" setting and made the attached changes.  Note: I didn't add ["use strict";](http://ejohn.org/blog/ecmascript-5-strict-mode-json-and-more/), since ECMAScript5 is not in widespread use.  I also prepended a "global" comment for `jQuery` and `window`, the latter for its [resize event](http://www.quirksmode.org/dom/events/resize.html).

I don't think Sphinx does any JS compression.  I think a lone `$` in Sphinx's `layout.html` causes `misc.html.math_parse()` and `notebook.docHTMLProcessor.process_doc_html()` effectively to strip the `\n`'s from the toggle code.

We should still fix the `$` problem, since Firebug and Opera's DragonFly complain about it.  Worse yet, it makes Chromium's Developer Tools hang.


---

Comment by mpatel created at 2009-10-06 00:24:15

v2: Added JSLint tweaks. Apply only this patch.


---

Comment by mhansen created at 2009-10-16 04:50:38

Changing status from needs_review to positive_review.


---

Attachment

Looks good to me.


---

Comment by mhansen created at 2009-10-16 04:52:02

Resolution: fixed
