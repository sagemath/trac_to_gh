# Issue 7310: Use modal dialogs instead of javascript prompts for the rename prompt.

Issue created by migration from https://trac.sagemath.org/ticket/7310

Original creator: timdumol

Original creation time: 2009-10-26 13:27:43

Assignee: boothby

CC:  was mpatel

Javascript prompts are jarring, and more importantly, are not properly handled by Selenium.


---

Attachment

Replaces the javascript prompt with a modal dialog. Light dependency on #7309


---

Comment by timdumol created at 2009-10-26 13:33:15

Changing status from new to needs_review.


---

Comment by timdumol created at 2009-10-26 13:33:15

This patch relies on an additional body id introduced in #7309, but can easily be rebased if #7309 is not accepted.


---

Attachment

Adds a 100ms fade in effect and prevents a warning under strict warnings mode (trailing comma).


---

Comment by timdumol created at 2009-10-26 15:36:32

Makes the rename dialog appear only when the page is fully loaded.


---

Attachment

I tried v3, but the rename dialog was improperly rendered, possibly because an icon is missing?  But why not use [jQuery UI dialog](http://jqueryui.com/demos/dialog/#modal-form), since we're already loading the library and it has built-in theme support?

I don't mean to pile on --- I'm happy to go through the Sage templates and code, converting alerts and prompts to dialogs.


---

Attachment

Adds a new function `modal_prompt(...)` to replace `prompt()` dialogs based on jQuery UI Dialog.


---

Comment by timdumol created at 2009-10-27 15:05:53

This should do the job. `ack`ing spotted only those two prompts. Alerts should probably be dealt in another ticket, if at all. This may be useful, if you're interested: http://boedesign.com/blog/2009/07/11/growl-for-jquery-gritter/.


---

Comment by mpatel created at 2009-10-27 15:20:34

I'll try to take a closer look tomorrow.  A quick note: The bgiframe plugin is already in `sagenb/data/jqueryui/development-bundle/external`.


---

Attachment

Adds the requisite imports to `worksheet_listing.html`


---

Comment by timdumol created at 2009-10-27 15:40:06

Replying to [comment:4 mpatel]:
> I'll try to take a closer look tomorrow.  A quick note: The bgiframe plugin is already in `sagenb/data/jqueryui/development-bundle/external`.
Depending on the presence of the bgiframe plugin in the development kit (or the presence of the development kit itself) of an external package does not seem like a good idea to me.


---

Comment by timdumol created at 2009-10-28 13:45:59

Removes the dialog from the DOM if `destroy` option is given -- this is done for performance and efficiency.


---

Attachment

Minified three JS files.  Various small changes.  Apply only this patch.


---

Comment by mpatel created at 2009-10-31 08:17:46

Version 7:

 * Updates a few JS functions per [JSLint](http://www.jslint.com/) in "The Good Parts" mode.
 * Includes `farbtastic.min.js`, `jquery.event.extendedclick.min.js`, and `jquery.form.min.js`, all made with the [YUI Compressor](http://developer.yahoo.com/yui/compressor/) 2.4.2:

```
java -jar yuicompressor-2.4.2.jar foo.js > foo.min.js
```

 * Uses `src="/javascript/jquery/plugins/jquery.bgiframe.min.js"` consistently.

To the extent it counts, my review is positive.


---

Comment by mpatel created at 2009-11-01 11:22:38

Pre-select input text and use `width: auto`. Apply only this patch.


---

Attachment

Version 8:

 * Uses `width: auto` for the input field.
 * Pre-selects the input text.


---

Attachment


---

Comment by mpatel created at 2009-11-01 11:25:56

Please use v8.2 instead of v8.


---

Comment by was created at 2009-11-11 19:39:27

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-11-11 19:39:27

Extra positive review from me.


---

Comment by was created at 2009-11-11 19:39:39

merged into sagenb-0.4.2 (sage-4.2.1)


---

Comment by was created at 2009-11-11 19:39:39

Resolution: fixed
