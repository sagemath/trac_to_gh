# Issue 7126: Doc sidebar broken by Sphinx 0.6.3 JS compression

archive/issues_007126.json:
```json
{
    "body": "Assignee: tba\n\nThe doc sidebar provided by #6507 is broken by the JS compression applied by Sphinx 0.6.3 (#6586). This patch changes line comments to block comments, and adds some missing semicolons.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7126\n\n",
    "created_at": "2009-10-05T19:02:35Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "Doc sidebar broken by Sphinx 0.6.3 JS compression",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7126",
    "user": "timdumol"
}
```
Assignee: tba

The doc sidebar provided by #6507 is broken by the JS compression applied by Sphinx 0.6.3 (#6586). This patch changes line comments to block comments, and adds some missing semicolons.

Issue created by migration from https://trac.sagemath.org/ticket/7126





---

archive/issue_comments_059112.json:
```json
{
    "body": "Attachment [trac_7126-doc-sidebar-fix.patch](tarball://root/attachments/some-uuid/ticket7126/trac_7126-doc-sidebar-fix.patch) by timdumol created at 2009-10-05 19:04:15\n\nChanges line comments to block comments. Adds missing semicolons.",
    "created_at": "2009-10-05T19:04:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7126#issuecomment-59112",
    "user": "timdumol"
}
```

Attachment [trac_7126-doc-sidebar-fix.patch](tarball://root/attachments/some-uuid/ticket7126/trac_7126-doc-sidebar-fix.patch) by timdumol created at 2009-10-05 19:04:15

Changes line comments to block comments. Adds missing semicolons.



---

archive/issue_comments_059113.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-10-05T19:05:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7126#issuecomment-59113",
    "user": "timdumol"
}
```

Changing priority from major to minor.



---

archive/issue_comments_059114.json:
```json
{
    "body": "Thanks very much for finding these problems.  I ran the JS code in `layout.html` through [JSLint](http://www.jslint.com/) on the \"The Good Parts\" setting and made the attached changes.  Note: I didn't add [\"use strict\";](http://ejohn.org/blog/ecmascript-5-strict-mode-json-and-more/), since ECMAScript5 is not in widespread use.  I also prepended a \"global\" comment for `jQuery` and `window`, the latter for its [resize event](http://www.quirksmode.org/dom/events/resize.html).\n\nI don't think Sphinx does any JS compression.  I think a lone `$` in Sphinx's `layout.html` causes `misc.html.math_parse()` and `notebook.docHTMLProcessor.process_doc_html()` effectively to strip the `\\n`'s from the toggle code.\n\nWe should still fix the `$` problem, since Firebug and Opera's DragonFly complain about it.  Worse yet, it makes Chromium's Developer Tools hang.",
    "created_at": "2009-10-06T00:22:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7126#issuecomment-59114",
    "user": "mpatel"
}
```

Thanks very much for finding these problems.  I ran the JS code in `layout.html` through [JSLint](http://www.jslint.com/) on the "The Good Parts" setting and made the attached changes.  Note: I didn't add ["use strict";](http://ejohn.org/blog/ecmascript-5-strict-mode-json-and-more/), since ECMAScript5 is not in widespread use.  I also prepended a "global" comment for `jQuery` and `window`, the latter for its [resize event](http://www.quirksmode.org/dom/events/resize.html).

I don't think Sphinx does any JS compression.  I think a lone `$` in Sphinx's `layout.html` causes `misc.html.math_parse()` and `notebook.docHTMLProcessor.process_doc_html()` effectively to strip the `\n`'s from the toggle code.

We should still fix the `$` problem, since Firebug and Opera's DragonFly complain about it.  Worse yet, it makes Chromium's Developer Tools hang.



---

archive/issue_comments_059115.json:
```json
{
    "body": "v2: Added JSLint tweaks. Apply only this patch.",
    "created_at": "2009-10-06T00:24:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7126#issuecomment-59115",
    "user": "mpatel"
}
```

v2: Added JSLint tweaks. Apply only this patch.



---

archive/issue_comments_059116.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-16T04:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7126#issuecomment-59116",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059117.json:
```json
{
    "body": "Attachment [trac_7126-doc-sidebar-fix_v2.patch](tarball://root/attachments/some-uuid/ticket7126/trac_7126-doc-sidebar-fix_v2.patch) by mhansen created at 2009-10-16 04:50:38\n\nLooks good to me.",
    "created_at": "2009-10-16T04:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7126#issuecomment-59117",
    "user": "mhansen"
}
```

Attachment [trac_7126-doc-sidebar-fix_v2.patch](tarball://root/attachments/some-uuid/ticket7126/trac_7126-doc-sidebar-fix_v2.patch) by mhansen created at 2009-10-16 04:50:38

Looks good to me.



---

archive/issue_comments_059118.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-16T04:52:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7126#issuecomment-59118",
    "user": "mhansen"
}
```

Resolution: fixed
