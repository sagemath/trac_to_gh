# Issue 7310: Use modal dialogs instead of javascript prompts for the rename prompt.

archive/issues_007310.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  was mpatel\n\nJavascript prompts are jarring, and more importantly, are not properly handled by Selenium.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7310\n\n",
    "created_at": "2009-10-26T13:27:43Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "Use modal dialogs instead of javascript prompts for the rename prompt.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7310",
    "user": "timdumol"
}
```
Assignee: boothby

CC:  was mpatel

Javascript prompts are jarring, and more importantly, are not properly handled by Selenium.

Issue created by migration from https://trac.sagemath.org/ticket/7310





---

archive/issue_comments_061049.json:
```json
{
    "body": "Attachment\n\nReplaces the javascript prompt with a modal dialog. Light dependency on #7309",
    "created_at": "2009-10-26T13:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-61049",
    "user": "timdumol"
}
```

Attachment

Replaces the javascript prompt with a modal dialog. Light dependency on #7309



---

archive/issue_comments_061050.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-26T13:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-61050",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061051.json:
```json
{
    "body": "This patch relies on an additional body id introduced in #7309, but can easily be rebased if #7309 is not accepted.",
    "created_at": "2009-10-26T13:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-61051",
    "user": "timdumol"
}
```

This patch relies on an additional body id introduced in #7309, but can easily be rebased if #7309 is not accepted.



---

archive/issue_comments_061052.json:
```json
{
    "body": "Attachment\n\nAdds a 100ms fade in effect and prevents a warning under strict warnings mode (trailing comma).",
    "created_at": "2009-10-26T13:42:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-61052",
    "user": "timdumol"
}
```

Attachment

Adds a 100ms fade in effect and prevents a warning under strict warnings mode (trailing comma).



---

archive/issue_comments_061053.json:
```json
{
    "body": "Makes the rename dialog appear only when the page is fully loaded.",
    "created_at": "2009-10-26T15:36:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-61053",
    "user": "timdumol"
}
```

Makes the rename dialog appear only when the page is fully loaded.



---

archive/issue_comments_061054.json:
```json
{
    "body": "Attachment\n\nI tried v3, but the rename dialog was improperly rendered, possibly because an icon is missing?  But why not use [jQuery UI dialog](http://jqueryui.com/demos/dialog/#modal-form), since we're already loading the library and it has built-in theme support?\n\nI don't mean to pile on --- I'm happy to go through the Sage templates and code, converting alerts and prompts to dialogs.",
    "created_at": "2009-10-26T23:00:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-61054",
    "user": "mpatel"
}
```

Attachment

I tried v3, but the rename dialog was improperly rendered, possibly because an icon is missing?  But why not use [jQuery UI dialog](http://jqueryui.com/demos/dialog/#modal-form), since we're already loading the library and it has built-in theme support?

I don't mean to pile on --- I'm happy to go through the Sage templates and code, converting alerts and prompts to dialogs.



---

archive/issue_comments_061055.json:
```json
{
    "body": "Attachment\n\nAdds a new function `modal_prompt(...)` to replace `prompt()` dialogs based on jQuery UI Dialog.",
    "created_at": "2009-10-27T15:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-61055",
    "user": "timdumol"
}
```

Attachment

Adds a new function `modal_prompt(...)` to replace `prompt()` dialogs based on jQuery UI Dialog.



---

archive/issue_comments_061056.json:
```json
{
    "body": "This should do the job. `ack`ing spotted only those two prompts. Alerts should probably be dealt in another ticket, if at all. This may be useful, if you're interested: http://boedesign.com/blog/2009/07/11/growl-for-jquery-gritter/.",
    "created_at": "2009-10-27T15:05:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-61056",
    "user": "timdumol"
}
```

This should do the job. `ack`ing spotted only those two prompts. Alerts should probably be dealt in another ticket, if at all. This may be useful, if you're interested: http://boedesign.com/blog/2009/07/11/growl-for-jquery-gritter/.



---

archive/issue_comments_061057.json:
```json
{
    "body": "I'll try to take a closer look tomorrow.  A quick note: The bgiframe plugin is already in `sagenb/data/jqueryui/development-bundle/external`.",
    "created_at": "2009-10-27T15:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-61057",
    "user": "mpatel"
}
```

I'll try to take a closer look tomorrow.  A quick note: The bgiframe plugin is already in `sagenb/data/jqueryui/development-bundle/external`.



---

archive/issue_comments_061058.json:
```json
{
    "body": "Attachment\n\nAdds the requisite imports to `worksheet_listing.html`",
    "created_at": "2009-10-27T15:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-61058",
    "user": "timdumol"
}
```

Attachment

Adds the requisite imports to `worksheet_listing.html`



---

archive/issue_comments_061059.json:
```json
{
    "body": "Replying to [comment:4 mpatel]:\n> I'll try to take a closer look tomorrow.  A quick note: The bgiframe plugin is already in `sagenb/data/jqueryui/development-bundle/external`.\nDepending on the presence of the bgiframe plugin in the development kit (or the presence of the development kit itself) of an external package does not seem like a good idea to me.",
    "created_at": "2009-10-27T15:40:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-61059",
    "user": "timdumol"
}
```

Replying to [comment:4 mpatel]:
> I'll try to take a closer look tomorrow.  A quick note: The bgiframe plugin is already in `sagenb/data/jqueryui/development-bundle/external`.
Depending on the presence of the bgiframe plugin in the development kit (or the presence of the development kit itself) of an external package does not seem like a good idea to me.



---

archive/issue_comments_061060.json:
```json
{
    "body": "Removes the dialog from the DOM if `destroy` option is given -- this is done for performance and efficiency.",
    "created_at": "2009-10-28T13:45:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-61060",
    "user": "timdumol"
}
```

Removes the dialog from the DOM if `destroy` option is given -- this is done for performance and efficiency.



---

archive/issue_comments_061061.json:
```json
{
    "body": "Attachment\n\nMinified three JS files.  Various small changes.  Apply only this patch.",
    "created_at": "2009-10-31T08:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-61061",
    "user": "mpatel"
}
```

Attachment

Minified three JS files.  Various small changes.  Apply only this patch.



---

archive/issue_comments_061062.json:
```json
{
    "body": "Version 7:\n\n* Updates a few JS functions per [JSLint](http://www.jslint.com/) in \"The Good Parts\" mode.\n* Includes `farbtastic.min.js`, `jquery.event.extendedclick.min.js`, and `jquery.form.min.js`, all made with the [YUI Compressor](http://developer.yahoo.com/yui/compressor/) 2.4.2:\n\n```\njava -jar yuicompressor-2.4.2.jar foo.js > foo.min.js\n```\n\n* Uses `src=\"/javascript/jquery/plugins/jquery.bgiframe.min.js\"` consistently.\n\nTo the extent it counts, my review is positive.",
    "created_at": "2009-10-31T08:17:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-61062",
    "user": "mpatel"
}
```

Version 7:

* Updates a few JS functions per [JSLint](http://www.jslint.com/) in "The Good Parts" mode.
* Includes `farbtastic.min.js`, `jquery.event.extendedclick.min.js`, and `jquery.form.min.js`, all made with the [YUI Compressor](http://developer.yahoo.com/yui/compressor/) 2.4.2:

```
java -jar yuicompressor-2.4.2.jar foo.js > foo.min.js
```

* Uses `src="/javascript/jquery/plugins/jquery.bgiframe.min.js"` consistently.

To the extent it counts, my review is positive.



---

archive/issue_comments_061063.json:
```json
{
    "body": "Pre-select input text and use `width: auto`. Apply only this patch.",
    "created_at": "2009-11-01T11:22:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-61063",
    "user": "mpatel"
}
```

Pre-select input text and use `width: auto`. Apply only this patch.



---

archive/issue_comments_061064.json:
```json
{
    "body": "Attachment\n\nVersion 8:\n\n* Uses `width: auto` for the input field.\n* Pre-selects the input text.",
    "created_at": "2009-11-01T11:24:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-61064",
    "user": "mpatel"
}
```

Attachment

Version 8:

* Uses `width: auto` for the input field.
* Pre-selects the input text.



---

archive/issue_comments_061065.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-11-01T11:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-61065",
    "user": "mpatel"
}
```

Attachment



---

archive/issue_comments_061066.json:
```json
{
    "body": "Please use v8.2 instead of v8.",
    "created_at": "2009-11-01T11:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-61066",
    "user": "mpatel"
}
```

Please use v8.2 instead of v8.



---

archive/issue_comments_061067.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-11T19:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-61067",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061068.json:
```json
{
    "body": "Extra positive review from me.",
    "created_at": "2009-11-11T19:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-61068",
    "user": "was"
}
```

Extra positive review from me.



---

archive/issue_comments_061069.json:
```json
{
    "body": "merged into sagenb-0.4.2 (sage-4.2.1)",
    "created_at": "2009-11-11T19:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-61069",
    "user": "was"
}
```

merged into sagenb-0.4.2 (sage-4.2.1)



---

archive/issue_comments_061070.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-11T19:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-61070",
    "user": "was"
}
```

Resolution: fixed
