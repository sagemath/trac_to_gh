# Issue 7310: Use modal dialogs instead of javascript prompts for the rename prompt.

archive/issues_007310.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @williamstein @qed777\n\nJavascript prompts are jarring, and more importantly, are not properly handled by Selenium.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7310\n\n",
    "created_at": "2009-10-26T13:27:43Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "Use modal dialogs instead of javascript prompts for the rename prompt.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7310",
    "user": "https://github.com/TimDumol"
}
```
Assignee: boothby

CC:  @williamstein @qed777

Javascript prompts are jarring, and more importantly, are not properly handled by Selenium.

Issue created by migration from https://trac.sagemath.org/ticket/7310





---

archive/issue_comments_060936.json:
```json
{
    "body": "Attachment [trac_7310-modals.patch](tarball://root/attachments/some-uuid/ticket7310/trac_7310-modals.patch) by @TimDumol created at 2009-10-26 13:32:18\n\nReplaces the javascript prompt with a modal dialog. Light dependency on #7309",
    "created_at": "2009-10-26T13:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-60936",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7310-modals.patch](tarball://root/attachments/some-uuid/ticket7310/trac_7310-modals.patch) by @TimDumol created at 2009-10-26 13:32:18

Replaces the javascript prompt with a modal dialog. Light dependency on #7309



---

archive/issue_comments_060937.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-26T13:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-60937",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060938.json:
```json
{
    "body": "This patch relies on an additional body id introduced in #7309, but can easily be rebased if #7309 is not accepted.",
    "created_at": "2009-10-26T13:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-60938",
    "user": "https://github.com/TimDumol"
}
```

This patch relies on an additional body id introduced in #7309, but can easily be rebased if #7309 is not accepted.



---

archive/issue_comments_060939.json:
```json
{
    "body": "Attachment [trac_7310-modals.2.patch](tarball://root/attachments/some-uuid/ticket7310/trac_7310-modals.2.patch) by @TimDumol created at 2009-10-26 13:42:09\n\nAdds a 100ms fade in effect and prevents a warning under strict warnings mode (trailing comma).",
    "created_at": "2009-10-26T13:42:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-60939",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7310-modals.2.patch](tarball://root/attachments/some-uuid/ticket7310/trac_7310-modals.2.patch) by @TimDumol created at 2009-10-26 13:42:09

Adds a 100ms fade in effect and prevents a warning under strict warnings mode (trailing comma).



---

archive/issue_comments_060940.json:
```json
{
    "body": "Makes the rename dialog appear only when the page is fully loaded.",
    "created_at": "2009-10-26T15:36:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-60940",
    "user": "https://github.com/TimDumol"
}
```

Makes the rename dialog appear only when the page is fully loaded.



---

archive/issue_comments_060941.json:
```json
{
    "body": "Attachment [trac_7310-modals.3.patch](tarball://root/attachments/some-uuid/ticket7310/trac_7310-modals.3.patch) by @qed777 created at 2009-10-26 23:00:24\n\nI tried v3, but the rename dialog was improperly rendered, possibly because an icon is missing?  But why not use [jQuery UI dialog](http://jqueryui.com/demos/dialog/#modal-form), since we're already loading the library and it has built-in theme support?\n\nI don't mean to pile on --- I'm happy to go through the Sage templates and code, converting alerts and prompts to dialogs.",
    "created_at": "2009-10-26T23:00:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-60941",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7310-modals.3.patch](tarball://root/attachments/some-uuid/ticket7310/trac_7310-modals.3.patch) by @qed777 created at 2009-10-26 23:00:24

I tried v3, but the rename dialog was improperly rendered, possibly because an icon is missing?  But why not use [jQuery UI dialog](http://jqueryui.com/demos/dialog/#modal-form), since we're already loading the library and it has built-in theme support?

I don't mean to pile on --- I'm happy to go through the Sage templates and code, converting alerts and prompts to dialogs.



---

archive/issue_comments_060942.json:
```json
{
    "body": "Attachment [trac_7310-modals.4.patch](tarball://root/attachments/some-uuid/ticket7310/trac_7310-modals.4.patch) by @TimDumol created at 2009-10-27 15:03:40\n\nAdds a new function `modal_prompt(...)` to replace `prompt()` dialogs based on jQuery UI Dialog.",
    "created_at": "2009-10-27T15:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-60942",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7310-modals.4.patch](tarball://root/attachments/some-uuid/ticket7310/trac_7310-modals.4.patch) by @TimDumol created at 2009-10-27 15:03:40

Adds a new function `modal_prompt(...)` to replace `prompt()` dialogs based on jQuery UI Dialog.



---

archive/issue_comments_060943.json:
```json
{
    "body": "This should do the job. `ack`ing spotted only those two prompts. Alerts should probably be dealt in another ticket, if at all. This may be useful, if you're interested: http://boedesign.com/blog/2009/07/11/growl-for-jquery-gritter/.",
    "created_at": "2009-10-27T15:05:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-60943",
    "user": "https://github.com/TimDumol"
}
```

This should do the job. `ack`ing spotted only those two prompts. Alerts should probably be dealt in another ticket, if at all. This may be useful, if you're interested: http://boedesign.com/blog/2009/07/11/growl-for-jquery-gritter/.



---

archive/issue_comments_060944.json:
```json
{
    "body": "I'll try to take a closer look tomorrow.  A quick note: The bgiframe plugin is already in `sagenb/data/jqueryui/development-bundle/external`.",
    "created_at": "2009-10-27T15:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-60944",
    "user": "https://github.com/qed777"
}
```

I'll try to take a closer look tomorrow.  A quick note: The bgiframe plugin is already in `sagenb/data/jqueryui/development-bundle/external`.



---

archive/issue_comments_060945.json:
```json
{
    "body": "Attachment [trac_7310-modals.5.patch](tarball://root/attachments/some-uuid/ticket7310/trac_7310-modals.5.patch) by @TimDumol created at 2009-10-27 15:39:06\n\nAdds the requisite imports to `worksheet_listing.html`",
    "created_at": "2009-10-27T15:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-60945",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7310-modals.5.patch](tarball://root/attachments/some-uuid/ticket7310/trac_7310-modals.5.patch) by @TimDumol created at 2009-10-27 15:39:06

Adds the requisite imports to `worksheet_listing.html`



---

archive/issue_comments_060946.json:
```json
{
    "body": "Replying to [comment:4 mpatel]:\n> I'll try to take a closer look tomorrow.  A quick note: The bgiframe plugin is already in `sagenb/data/jqueryui/development-bundle/external`.\n\nDepending on the presence of the bgiframe plugin in the development kit (or the presence of the development kit itself) of an external package does not seem like a good idea to me.",
    "created_at": "2009-10-27T15:40:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-60946",
    "user": "https://github.com/TimDumol"
}
```

Replying to [comment:4 mpatel]:
> I'll try to take a closer look tomorrow.  A quick note: The bgiframe plugin is already in `sagenb/data/jqueryui/development-bundle/external`.

Depending on the presence of the bgiframe plugin in the development kit (or the presence of the development kit itself) of an external package does not seem like a good idea to me.



---

archive/issue_comments_060947.json:
```json
{
    "body": "Removes the dialog from the DOM if `destroy` option is given -- this is done for performance and efficiency.",
    "created_at": "2009-10-28T13:45:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-60947",
    "user": "https://github.com/TimDumol"
}
```

Removes the dialog from the DOM if `destroy` option is given -- this is done for performance and efficiency.



---

archive/issue_comments_060948.json:
```json
{
    "body": "Attachment [trac_7310-modals.7.patch](tarball://root/attachments/some-uuid/ticket7310/trac_7310-modals.7.patch) by @qed777 created at 2009-10-31 08:02:48\n\nMinified three JS files.  Various small changes.  Apply only this patch.",
    "created_at": "2009-10-31T08:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-60948",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7310-modals.7.patch](tarball://root/attachments/some-uuid/ticket7310/trac_7310-modals.7.patch) by @qed777 created at 2009-10-31 08:02:48

Minified three JS files.  Various small changes.  Apply only this patch.



---

archive/issue_comments_060949.json:
```json
{
    "body": "Version 7:\n\n* Updates a few JS functions per [JSLint](http://www.jslint.com/) in \"The Good Parts\" mode.\n* Includes `farbtastic.min.js`, `jquery.event.extendedclick.min.js`, and `jquery.form.min.js`, all made with the [YUI Compressor](http://developer.yahoo.com/yui/compressor/) 2.4.2:\n\n```\njava -jar yuicompressor-2.4.2.jar foo.js > foo.min.js\n```\n* Uses `src=\"/javascript/jquery/plugins/jquery.bgiframe.min.js\"` consistently.\n\nTo the extent it counts, my review is positive.",
    "created_at": "2009-10-31T08:17:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-60949",
    "user": "https://github.com/qed777"
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

archive/issue_comments_060950.json:
```json
{
    "body": "Pre-select input text and use `width: auto`. Apply only this patch.",
    "created_at": "2009-11-01T11:22:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-60950",
    "user": "https://github.com/qed777"
}
```

Pre-select input text and use `width: auto`. Apply only this patch.



---

archive/issue_comments_060951.json:
```json
{
    "body": "Attachment [trac_7310-modals.8.patch](tarball://root/attachments/some-uuid/ticket7310/trac_7310-modals.8.patch) by @qed777 created at 2009-11-01 11:24:02\n\nVersion 8:\n\n* Uses `width: auto` for the input field.\n* Pre-selects the input text.",
    "created_at": "2009-11-01T11:24:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-60951",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7310-modals.8.patch](tarball://root/attachments/some-uuid/ticket7310/trac_7310-modals.8.patch) by @qed777 created at 2009-11-01 11:24:02

Version 8:

* Uses `width: auto` for the input field.
* Pre-selects the input text.



---

archive/issue_comments_060952.json:
```json
{
    "body": "Attachment [trac_7310-modals.8.2.patch](tarball://root/attachments/some-uuid/ticket7310/trac_7310-modals.8.2.patch) by @qed777 created at 2009-11-01 11:25:03",
    "created_at": "2009-11-01T11:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-60952",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7310-modals.8.2.patch](tarball://root/attachments/some-uuid/ticket7310/trac_7310-modals.8.2.patch) by @qed777 created at 2009-11-01 11:25:03



---

archive/issue_comments_060953.json:
```json
{
    "body": "Please use v8.2 instead of v8.",
    "created_at": "2009-11-01T11:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-60953",
    "user": "https://github.com/qed777"
}
```

Please use v8.2 instead of v8.



---

archive/issue_comments_060954.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-11T19:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-60954",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060955.json:
```json
{
    "body": "Extra positive review from me.",
    "created_at": "2009-11-11T19:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-60955",
    "user": "https://github.com/williamstein"
}
```

Extra positive review from me.



---

archive/issue_comments_060956.json:
```json
{
    "body": "merged into sagenb-0.4.2 (sage-4.2.1)",
    "created_at": "2009-11-11T19:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-60956",
    "user": "https://github.com/williamstein"
}
```

merged into sagenb-0.4.2 (sage-4.2.1)



---

archive/issue_comments_060957.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-11T19:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7310#issuecomment-60957",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_017323.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-11-11T19:39:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7310#event-17323"
}
```



---

archive/issue_events_017324.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-11-11T19:44:31Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7310",
    "milestone": "sage-4.2.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7310#event-17324"
}
```
