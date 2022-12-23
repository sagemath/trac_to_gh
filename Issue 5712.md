# Issue 5712: notebook -- Get rid of the stupid "unable to immediately interrupt computation" alert that drives me nuts

Issue created by migration from https://trac.sagemath.org/ticket/5712

Original creator: was

Original creation time: 2009-04-08 14:46:55

Assignee: boothby

CC:  acleone was boothby mpatel

More precisely, one could keep the alert, but make it so that it can *not* appear if it already appeared in the last 5 seconds (say).  It is so annoying!


---

Comment by boothby created at 2009-04-08 15:48:24

The "2.0" thing to do is to inject a div somewhere, and just keep sending interrupts to the server until it works or the interrupt process gets cancelled.

"Couldn't immediately interrupt.  Trying again in (seconds 'till next retry) [cancel] [restart worksheet]"

[x] <- is a button that says x.


---

Comment by mabshoff created at 2009-04-09 18:46:34

Is this a high priority issue? I am not convinced and since there is no patch and no sign of anyone working on fixing this I am bumping this to 3.4.2.

Cheers,

Michael


---

Attachment

Uses Achtung (jQuery library) for notifications instead.


---

Comment by timdumol created at 2010-01-18 04:25:38

Changing status from new to needs_review.


---

Comment by timdumol created at 2010-01-18 04:25:38

This should do the thing.


---

Comment by timdumol created at 2010-01-18 06:55:29

Fixes #7702 and a typo in notebook_lib.js from the previous patch. Apply this patch alone.


---

Attachment


---

Comment by timdumol created at 2010-01-18 07:02:38

To note, the patch series for this is:


```
trac_7650-sagenb_doctesting_v6.patch
trac_7650-reviewer.patch
trac_7648-missing_indent.patch
trac_7663-rstrip_prompt.patch
trac_7847-empty-trash-no-referer.patch
trac_7786-template-jinja-idiomatic.patch
trac_7863-declare_vars_aux_js_v2.patch
trac_7874-typeset_interact_labels.patch
trac_7858-key_binding_vars_v2.patch
trac_7666-alphanumeric_cell_ids_B5.patch
trac_7666-reviewer.patch
trac_7835-preparsing-unicode_v2.patch
trac_7249_jinja2_v5.patch
trac_2779-sagenb-error-message.patch
2779_2_banner.patch
trac_3154-spurious-u0027-output.patch
trac_7969-escaped-backslash.patch
trac_7937-sass_manifest.patch
trac_4217-html-system-formatting.patch
trac_3083-print-documentation.patch
trac_7962-link-worksheets-zip-file.patch
trac_5177-delete-cell-dirs.patch
trac_5712-interrupt-notification.patch
```



---

Comment by mpatel created at 2010-01-20 00:14:48

* I get a doctest failure from `Worksheet.interrupt`.

 * Just to check: Is `_ui-achtung.sass` just `ui.achtung.css` run through `css2sass`?  I suggest describing the conversion method briefly in `sass/readme.txt`.

 * Interrupting an idle worksheet also brings up the alert.

 * V2 does not fix #7702's example (`interrupt test.sws`).  A new alert appears every time I try to interrupt the calculation, but the calculation keeps going (e.g., according to `top`).  (I stopped after about 10 attempts.)  Restarting the worksheet does stop the calculation.  But this need not hold up this ticket, as I can interrupt other examples, such as `import time; time.sleep(10)` and `factor(factorial(100000000))`.

 * When we do show the alert (with #7702's example or a different one), maybe we should add, e.g., "Please try again in a few seconds.  If that doesn't work, please try restarting the worksheet."?


---

Comment by timdumol created at 2010-01-20 11:41:59

Replying to [comment:7 mpatel]:
>  * I get a doctest failure from `Worksheet.interrupt`.
> 
>  * Just to check: Is `_ui-achtung.sass` just `ui.achtung.css` run through `css2sass`?  I suggest describing the conversion method briefly in `sass/readme.txt`.

Yes. Sure, I'll do so.

> 
>  * Interrupting an idle worksheet also brings up the alert.

Good catch.

> 
>  * V2 does not fix #7702's example (`interrupt test.sws`).  A new alert appears every time I try to interrupt the calculation, but the calculation keeps going (e.g., according to `top`).  (I stopped after about 10 attempts.)  Restarting the worksheet does stop the calculation.  But this need not hold up this ticket, as I can interrupt other examples, such as `import time; time.sleep(10)` and `factor(factorial(100000000))`.
> 

The point of #7702 is not to interrupt uninterruptible calculations, but to recognize that a calculation cannot be interrupted and display an appropriate alert.

>  * When we do show the alert (with #7702's example or a different one), maybe we should add, e.g., "Please try again in a few seconds.  If that doesn't work, please try restarting the worksheet."?


---

Comment by timdumol created at 2010-01-20 11:46:05

Replying to [comment:8 timdumol]:
> Replying to [comment:7 mpatel]:
> >  * I get a doctest failure from `Worksheet.interrupt`.
> > 
> >  * Just to check: Is `_ui-achtung.sass` just `ui.achtung.css` run through `css2sass`?  I suggest describing the conversion method briefly in `sass/readme.txt`.
> 
> Yes. Sure, I'll do so.

In another ticket, that is.

> 
> > 
> >  * Interrupting an idle worksheet also brings up the alert.
> 
> Good catch.
> 
> > 
> >  * V2 does not fix #7702's example (`interrupt test.sws`).  A new alert appears every time I try to interrupt the calculation, but the calculation keeps going (e.g., according to `top`).  (I stopped after about 10 attempts.)  Restarting the worksheet does stop the calculation.  But this need not hold up this ticket, as I can interrupt other examples, such as `import time; time.sleep(10)` and `factor(factorial(100000000))`.
> > 
> 
> The point of #7702 is not to interrupt uninterruptible calculations, but to recognize that a calculation cannot be interrupted and display an appropriate alert.
> 
> >  * When we do show the alert (with #7702's example or a different one), maybe we should add, e.g., "Please try again in a few seconds.  If that doesn't work, please try restarting the worksheet."?

Will do so.


---

Comment by timdumol created at 2010-01-20 11:54:14

This patch should do it.


---

Attachment

Adds the requested changes.


---

Attachment

See comment.  Replaces previous.


---

Comment by mpatel created at 2010-01-22 03:13:50

Periodically re-attempt to interrupt.  Replaces previous.


---

Attachment

Please ignore V4.  V5

 * Adds optional callbacks for the [jQuery achtung plug-in's](http://achtung-ui.googlecode.com/) timeout and close events.  See `ui.achtung-mod.js`.  The notebook actually loads `ui.achtung-mod.min.js`, which I made with the [YUI Compressor](http://developer.yahoo.com/yui/compressor/).

 * Uses the new callbacks to send additional interrupt requests and update an alert every 5 seconds, until a request succeeds or the user closes the alert.  If the process _is_ interrupted, or the user restarts it, or the computation is done, etc., the alert should close itself.

Please test (and post feedback)!


---

Comment by mpatel created at 2010-01-25 04:36:57

Rebased against SageNB 0.7 at #8051.  Replaces previous.


---

Attachment

V6 is rebased against #8051's SageNB 0.7.


---

Comment by timdumol created at 2010-03-11 13:23:01

Works for me against 0.7.5.3. Can't see anything wrong with the changes. Positive review for your changes. Should we mark this positive review, or ask for a third party?


---

Comment by acleone created at 2010-03-11 16:13:44

LGTM.


---

Comment by acleone created at 2010-03-11 16:13:44

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-05-04 04:42:27

Resolution: fixed
