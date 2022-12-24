# Issue 5712: notebook -- Get rid of the stupid "unable to immediately interrupt computation" alert that drives me nuts

archive/issues_005712.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  acleone was boothby mpatel\n\nMore precisely, one could keep the alert, but make it so that it can *not* appear if it already appeared in the last 5 seconds (say).  It is so annoying!\n\nIssue created by migration from https://trac.sagemath.org/ticket/5712\n\n",
    "created_at": "2009-04-08T14:46:55Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook -- Get rid of the stupid \"unable to immediately interrupt computation\" alert that drives me nuts",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5712",
    "user": "was"
}
```
Assignee: boothby

CC:  acleone was boothby mpatel

More precisely, one could keep the alert, but make it so that it can *not* appear if it already appeared in the last 5 seconds (say).  It is so annoying!

Issue created by migration from https://trac.sagemath.org/ticket/5712





---

archive/issue_comments_044629.json:
```json
{
    "body": "The \"2.0\" thing to do is to inject a div somewhere, and just keep sending interrupts to the server until it works or the interrupt process gets cancelled.\n\n\"Couldn't immediately interrupt.  Trying again in (seconds 'till next retry) [cancel] [restart worksheet]\"\n\n[x] <- is a button that says x.",
    "created_at": "2009-04-08T15:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5712#issuecomment-44629",
    "user": "boothby"
}
```

The "2.0" thing to do is to inject a div somewhere, and just keep sending interrupts to the server until it works or the interrupt process gets cancelled.

"Couldn't immediately interrupt.  Trying again in (seconds 'till next retry) [cancel] [restart worksheet]"

[x] <- is a button that says x.



---

archive/issue_comments_044630.json:
```json
{
    "body": "Is this a high priority issue? I am not convinced and since there is no patch and no sign of anyone working on fixing this I am bumping this to 3.4.2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T18:46:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5712#issuecomment-44630",
    "user": "mabshoff"
}
```

Is this a high priority issue? I am not convinced and since there is no patch and no sign of anyone working on fixing this I am bumping this to 3.4.2.

Cheers,

Michael



---

archive/issue_comments_044631.json:
```json
{
    "body": "Attachment [trac_5712-interrupt-notification.patch](tarball://root/attachments/some-uuid/ticket5712/trac_5712-interrupt-notification.patch) by timdumol created at 2010-01-18 04:25:12\n\nUses Achtung (jQuery library) for notifications instead.",
    "created_at": "2010-01-18T04:25:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5712#issuecomment-44631",
    "user": "timdumol"
}
```

Attachment [trac_5712-interrupt-notification.patch](tarball://root/attachments/some-uuid/ticket5712/trac_5712-interrupt-notification.patch) by timdumol created at 2010-01-18 04:25:12

Uses Achtung (jQuery library) for notifications instead.



---

archive/issue_comments_044632.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-18T04:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5712#issuecomment-44632",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_044633.json:
```json
{
    "body": "This should do the thing.",
    "created_at": "2010-01-18T04:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5712#issuecomment-44633",
    "user": "timdumol"
}
```

This should do the thing.



---

archive/issue_comments_044634.json:
```json
{
    "body": "Fixes #7702 and a typo in notebook_lib.js from the previous patch. Apply this patch alone.",
    "created_at": "2010-01-18T06:55:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5712#issuecomment-44634",
    "user": "timdumol"
}
```

Fixes #7702 and a typo in notebook_lib.js from the previous patch. Apply this patch alone.



---

archive/issue_comments_044635.json:
```json
{
    "body": "Attachment [trac_5712-interrupt-notification.2.patch](tarball://root/attachments/some-uuid/ticket5712/trac_5712-interrupt-notification.2.patch) by timdumol created at 2010-01-18 06:56:05",
    "created_at": "2010-01-18T06:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5712#issuecomment-44635",
    "user": "timdumol"
}
```

Attachment [trac_5712-interrupt-notification.2.patch](tarball://root/attachments/some-uuid/ticket5712/trac_5712-interrupt-notification.2.patch) by timdumol created at 2010-01-18 06:56:05



---

archive/issue_comments_044636.json:
```json
{
    "body": "To note, the patch series for this is:\n\n\n```\ntrac_7650-sagenb_doctesting_v6.patch\ntrac_7650-reviewer.patch\ntrac_7648-missing_indent.patch\ntrac_7663-rstrip_prompt.patch\ntrac_7847-empty-trash-no-referer.patch\ntrac_7786-template-jinja-idiomatic.patch\ntrac_7863-declare_vars_aux_js_v2.patch\ntrac_7874-typeset_interact_labels.patch\ntrac_7858-key_binding_vars_v2.patch\ntrac_7666-alphanumeric_cell_ids_B5.patch\ntrac_7666-reviewer.patch\ntrac_7835-preparsing-unicode_v2.patch\ntrac_7249_jinja2_v5.patch\ntrac_2779-sagenb-error-message.patch\n2779_2_banner.patch\ntrac_3154-spurious-u0027-output.patch\ntrac_7969-escaped-backslash.patch\ntrac_7937-sass_manifest.patch\ntrac_4217-html-system-formatting.patch\ntrac_3083-print-documentation.patch\ntrac_7962-link-worksheets-zip-file.patch\ntrac_5177-delete-cell-dirs.patch\ntrac_5712-interrupt-notification.patch\n```\n",
    "created_at": "2010-01-18T07:02:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5712#issuecomment-44636",
    "user": "timdumol"
}
```

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

archive/issue_comments_044637.json:
```json
{
    "body": "* I get a doctest failure from `Worksheet.interrupt`.\n\n  * Just to check: Is `_ui-achtung.sass` just `ui.achtung.css` run through `css2sass`?  I suggest describing the conversion method briefly in `sass/readme.txt`.\n\n  * Interrupting an idle worksheet also brings up the alert.\n\n  * V2 does not fix #7702's example (`interrupt test.sws`).  A new alert appears every time I try to interrupt the calculation, but the calculation keeps going (e.g., according to `top`).  (I stopped after about 10 attempts.)  Restarting the worksheet does stop the calculation.  But this need not hold up this ticket, as I can interrupt other examples, such as `import time; time.sleep(10)` and `factor(factorial(100000000))`.\n\n  * When we do show the alert (with #7702's example or a different one), maybe we should add, e.g., \"Please try again in a few seconds.  If that doesn't work, please try restarting the worksheet.\"?",
    "created_at": "2010-01-20T00:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5712#issuecomment-44637",
    "user": "mpatel"
}
```

* I get a doctest failure from `Worksheet.interrupt`.

  * Just to check: Is `_ui-achtung.sass` just `ui.achtung.css` run through `css2sass`?  I suggest describing the conversion method briefly in `sass/readme.txt`.

  * Interrupting an idle worksheet also brings up the alert.

  * V2 does not fix #7702's example (`interrupt test.sws`).  A new alert appears every time I try to interrupt the calculation, but the calculation keeps going (e.g., according to `top`).  (I stopped after about 10 attempts.)  Restarting the worksheet does stop the calculation.  But this need not hold up this ticket, as I can interrupt other examples, such as `import time; time.sleep(10)` and `factor(factorial(100000000))`.

  * When we do show the alert (with #7702's example or a different one), maybe we should add, e.g., "Please try again in a few seconds.  If that doesn't work, please try restarting the worksheet."?



---

archive/issue_comments_044638.json:
```json
{
    "body": "Replying to [comment:7 mpatel]:\n>  * I get a doctest failure from `Worksheet.interrupt`.\n> \n>  * Just to check: Is `_ui-achtung.sass` just `ui.achtung.css` run through `css2sass`?  I suggest describing the conversion method briefly in `sass/readme.txt`.\n\nYes. Sure, I'll do so.\n\n> \n>  * Interrupting an idle worksheet also brings up the alert.\n\nGood catch.\n\n> \n>  * V2 does not fix #7702's example (`interrupt test.sws`).  A new alert appears every time I try to interrupt the calculation, but the calculation keeps going (e.g., according to `top`).  (I stopped after about 10 attempts.)  Restarting the worksheet does stop the calculation.  But this need not hold up this ticket, as I can interrupt other examples, such as `import time; time.sleep(10)` and `factor(factorial(100000000))`.\n> \n\nThe point of #7702 is not to interrupt uninterruptible calculations, but to recognize that a calculation cannot be interrupted and display an appropriate alert.\n\n>  * When we do show the alert (with #7702's example or a different one), maybe we should add, e.g., \"Please try again in a few seconds.  If that doesn't work, please try restarting the worksheet.\"?",
    "created_at": "2010-01-20T11:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5712#issuecomment-44638",
    "user": "timdumol"
}
```

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

archive/issue_comments_044639.json:
```json
{
    "body": "Replying to [comment:8 timdumol]:\n> Replying to [comment:7 mpatel]:\n> >  * I get a doctest failure from `Worksheet.interrupt`.\n> > \n> >  * Just to check: Is `_ui-achtung.sass` just `ui.achtung.css` run through `css2sass`?  I suggest describing the conversion method briefly in `sass/readme.txt`.\n> \n> Yes. Sure, I'll do so.\n\nIn another ticket, that is.\n\n> \n> > \n> >  * Interrupting an idle worksheet also brings up the alert.\n> \n> Good catch.\n> \n> > \n> >  * V2 does not fix #7702's example (`interrupt test.sws`).  A new alert appears every time I try to interrupt the calculation, but the calculation keeps going (e.g., according to `top`).  (I stopped after about 10 attempts.)  Restarting the worksheet does stop the calculation.  But this need not hold up this ticket, as I can interrupt other examples, such as `import time; time.sleep(10)` and `factor(factorial(100000000))`.\n> > \n> \n> The point of #7702 is not to interrupt uninterruptible calculations, but to recognize that a calculation cannot be interrupted and display an appropriate alert.\n> \n> >  * When we do show the alert (with #7702's example or a different one), maybe we should add, e.g., \"Please try again in a few seconds.  If that doesn't work, please try restarting the worksheet.\"?\n\nWill do so.",
    "created_at": "2010-01-20T11:46:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5712#issuecomment-44639",
    "user": "timdumol"
}
```

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

archive/issue_comments_044640.json:
```json
{
    "body": "This patch should do it.",
    "created_at": "2010-01-20T11:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5712#issuecomment-44640",
    "user": "timdumol"
}
```

This patch should do it.



---

archive/issue_comments_044641.json:
```json
{
    "body": "Attachment [trac_5712-interrupt-notification.3.patch](tarball://root/attachments/some-uuid/ticket5712/trac_5712-interrupt-notification.3.patch) by timdumol created at 2010-01-20 12:09:21\n\nAdds the requested changes.",
    "created_at": "2010-01-20T12:09:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5712#issuecomment-44641",
    "user": "timdumol"
}
```

Attachment [trac_5712-interrupt-notification.3.patch](tarball://root/attachments/some-uuid/ticket5712/trac_5712-interrupt-notification.3.patch) by timdumol created at 2010-01-20 12:09:21

Adds the requested changes.



---

archive/issue_comments_044642.json:
```json
{
    "body": "Attachment [trac_5712-interrupt-notification.4.patch](tarball://root/attachments/some-uuid/ticket5712/trac_5712-interrupt-notification.4.patch) by mpatel created at 2010-01-21 13:39:39\n\nSee comment.  Replaces previous.",
    "created_at": "2010-01-21T13:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5712#issuecomment-44642",
    "user": "mpatel"
}
```

Attachment [trac_5712-interrupt-notification.4.patch](tarball://root/attachments/some-uuid/ticket5712/trac_5712-interrupt-notification.4.patch) by mpatel created at 2010-01-21 13:39:39

See comment.  Replaces previous.



---

archive/issue_comments_044643.json:
```json
{
    "body": "Periodically re-attempt to interrupt.  Replaces previous.",
    "created_at": "2010-01-22T03:13:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5712#issuecomment-44643",
    "user": "mpatel"
}
```

Periodically re-attempt to interrupt.  Replaces previous.



---

archive/issue_comments_044644.json:
```json
{
    "body": "Attachment [trac_5712-interrupt-notification.5.patch](tarball://root/attachments/some-uuid/ticket5712/trac_5712-interrupt-notification.5.patch) by mpatel created at 2010-01-22 03:33:09\n\nPlease ignore V4.  V5\n\n* Adds optional callbacks for the [jQuery achtung plug-in's](http://achtung-ui.googlecode.com/) timeout and close events.  See `ui.achtung-mod.js`.  The notebook actually loads `ui.achtung-mod.min.js`, which I made with the [YUI Compressor](http://developer.yahoo.com/yui/compressor/).\n\n* Uses the new callbacks to send additional interrupt requests and update an alert every 5 seconds, until a request succeeds or the user closes the alert.  If the process *is* interrupted, or the user restarts it, or the computation is done, etc., the alert should close itself.\n\nPlease test (and post feedback)!",
    "created_at": "2010-01-22T03:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5712#issuecomment-44644",
    "user": "mpatel"
}
```

Attachment [trac_5712-interrupt-notification.5.patch](tarball://root/attachments/some-uuid/ticket5712/trac_5712-interrupt-notification.5.patch) by mpatel created at 2010-01-22 03:33:09

Please ignore V4.  V5

* Adds optional callbacks for the [jQuery achtung plug-in's](http://achtung-ui.googlecode.com/) timeout and close events.  See `ui.achtung-mod.js`.  The notebook actually loads `ui.achtung-mod.min.js`, which I made with the [YUI Compressor](http://developer.yahoo.com/yui/compressor/).

* Uses the new callbacks to send additional interrupt requests and update an alert every 5 seconds, until a request succeeds or the user closes the alert.  If the process *is* interrupted, or the user restarts it, or the computation is done, etc., the alert should close itself.

Please test (and post feedback)!



---

archive/issue_comments_044645.json:
```json
{
    "body": "Rebased against SageNB 0.7 at #8051.  Replaces previous.",
    "created_at": "2010-01-25T04:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5712#issuecomment-44645",
    "user": "mpatel"
}
```

Rebased against SageNB 0.7 at #8051.  Replaces previous.



---

archive/issue_comments_044646.json:
```json
{
    "body": "Attachment [trac_5712-interrupt-notification.6.patch](tarball://root/attachments/some-uuid/ticket5712/trac_5712-interrupt-notification.6.patch) by mpatel created at 2010-01-25 04:40:57\n\nV6 is rebased against #8051's SageNB 0.7.",
    "created_at": "2010-01-25T04:40:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5712#issuecomment-44646",
    "user": "mpatel"
}
```

Attachment [trac_5712-interrupt-notification.6.patch](tarball://root/attachments/some-uuid/ticket5712/trac_5712-interrupt-notification.6.patch) by mpatel created at 2010-01-25 04:40:57

V6 is rebased against #8051's SageNB 0.7.



---

archive/issue_comments_044647.json:
```json
{
    "body": "Works for me against 0.7.5.3. Can't see anything wrong with the changes. Positive review for your changes. Should we mark this positive review, or ask for a third party?",
    "created_at": "2010-03-11T13:23:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5712#issuecomment-44647",
    "user": "timdumol"
}
```

Works for me against 0.7.5.3. Can't see anything wrong with the changes. Positive review for your changes. Should we mark this positive review, or ask for a third party?



---

archive/issue_comments_044648.json:
```json
{
    "body": "LGTM.",
    "created_at": "2010-03-11T16:13:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5712#issuecomment-44648",
    "user": "acleone"
}
```

LGTM.



---

archive/issue_comments_044649.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-11T16:13:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5712#issuecomment-44649",
    "user": "acleone"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_044650.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-04T04:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5712#issuecomment-44650",
    "user": "timdumol"
}
```

Resolution: fixed
